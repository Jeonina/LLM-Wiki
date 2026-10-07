#!/usr/bin/env python3
"""
Record each summary's source provenance in its frontmatter:

    source_sha256: "<sha256 of the source file>"        (a list for multi-source summaries)
    source_quality: full | partial | abstract           (only with --quality)

Both lines are placed right after the `source:` field. Run this after writing or
rewriting a summary, so that tools/pending-sources.sh can tell when a source file
has changed since its summary was written.

Usage:
    tools/source-hash.py <slug> [<slug> ...]            refresh the hash for these summaries
    tools/source-hash.py --missing                      add hashes to summaries that have none
    tools/source-hash.py --quality partial <slug> ...   also set source_quality
"""
import argparse, hashlib, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUMMARIES = ROOT / "10-Summaries"
SOURCES = ROOT / "00-Sources"
QUALITIES = ("full", "partial", "abstract")


def source_index():
    idx = {}
    for root, dirs, files in os.walk(SOURCES):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fn in files:
            if not fn.startswith("."):
                idx[re.sub(r"\.(md|pdf)$", "", fn, flags=re.I).lower()] = Path(root) / fn
    return idx


def source_field(text):
    """Return (frontmatter, match of the `source:` field) or (None, None)."""
    fm = re.match(r"---\n(.*?)\n---", text, re.S)
    if not fm:
        return None, None
    return fm, re.search(r"^source:(.*?)(?=^\w[\w-]*:|\Z)", fm.group(1), re.M | re.S)


def source_paths(text, idx):
    fm, field = source_field(text)
    if not field:
        return []
    out = []
    for ref in re.findall(r"\[\[(00-Sources/[^\]|\"]+)", field.group(1)):
        key = re.sub(r"\.(md|pdf)$", "", os.path.basename(ref.strip()), flags=re.I).lower()
        if key not in idx:
            sys.exit(f"source not found for {ref}")
        out.append(idx[key])
    return out


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def set_fields(text, fields):
    """Replace or insert `key: value` lines right after the source: field."""
    fm = re.match(r"---\n(.*?)\n---", text, re.S)
    body = fm.group(1)
    for key in fields:
        body = re.sub(rf"^{key}:.*(\n|\Z)", "", body, flags=re.M)
    lines = "".join(f"{k}: {v}\n" for k, v in fields.items())
    # the source: field ends where the next top-level key starts
    field = re.search(r"^source:.*?(?=^\w[\w-]*:|\Z)", body, re.M | re.S)
    if field.end() == len(body):
        body = body.rstrip("\n") + "\n" + lines.rstrip("\n")
    else:
        body = body[: field.end()] + lines + body[field.end():]
    return text[: fm.start(1)] + body + text[fm.end(1):]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--missing", action="store_true")
    ap.add_argument("--quality", choices=QUALITIES)
    a = ap.parse_args()
    idx = source_index()
    if a.missing:
        targets = [p for p in sorted(SUMMARIES.glob("*.md"))
                   if p.name != "index.md" and not re.search(r"^source_sha256:", p.read_text(), re.M)]
    else:
        targets = [SUMMARIES / f"{s.removesuffix('.md')}.md" for s in a.slugs]
    if not targets:
        ap.error("give slugs or --missing")
    for p in targets:
        text = p.read_text()
        paths = source_paths(text, idx)
        if not paths:
            print(f"skip (no source field): {p.name}")
            continue
        hashes = [sha256(x) for x in paths]
        fields = {"source_sha256": f'"{hashes[0]}"' if len(hashes) == 1
                  else "[" + ", ".join(f'"{h}"' for h in hashes) + "]"}
        if a.quality:
            fields = {"source_quality": a.quality, **fields}
        elif m := re.search(r"^source_quality:\s*(\S+)", text, re.M):
            fields = {"source_quality": m.group(1), **fields}
        p.write_text(set_fields(text, fields))
        print(f"ok {p.stem}")


if __name__ == "__main__":
    main()
