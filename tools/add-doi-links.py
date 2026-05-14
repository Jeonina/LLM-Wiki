#!/usr/bin/env python3
"""
Retrofit DOI/URL links into 10-Summaries/ pages.

For each summary file, this script:
  1. Skips if the body already contains a doi.org or https:// link.
  2. If frontmatter has a `doi:` field, inserts a clickable [DOI] line near the end.
  3. Else if `sources:` points to an .md clipping in 00-Sources/papers/ that
     has a `source:` URL in its own frontmatter, inserts a clickable link.
  4. Else emits a TODO line to stderr (summary needs manual / PubMed lookup).

Idempotent. Run from repo root.

Output format inserted just before the first "## Related" header (if any),
otherwise appended to file end:

    ---
    Source link: [DOI](https://doi.org/10.XXXX/XXXX)

Run:  python3 tools/add-doi-links.py [--dry-run]
"""
import sys
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
SUMMARIES = VAULT / "10-Summaries"
SOURCES_DIR = VAULT / "00-Sources" / "papers"

DRY = "--dry-run" in sys.argv

FM_DELIM = re.compile(r"^---\s*$", re.M)


def split_frontmatter(text):
    parts = text.split("---", 2)
    if len(parts) >= 3 and parts[0] == "":
        return parts[1], parts[2]
    return None, text


def parse_field(fm, field):
    """Return string value of a top-level YAML field, or None."""
    pattern = rf'^{re.escape(field)}\s*:\s*(.+)$'
    m = re.search(pattern, fm, re.M)
    if not m:
        return None
    val = m.group(1).strip()
    # strip surrounding quotes
    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        val = val[1:-1]
    return val


def parse_sources(fm):
    """Return list of source filenames (string list from sources: [...] or sources: "...")."""
    # Look for sources: ["a.pdf", "b.md"]
    m = re.search(r'^sources\s*:\s*\[(.+?)\]', fm, re.M | re.S)
    if m:
        inner = m.group(1)
        return re.findall(r'"([^"]+)"|\'([^\']+)\'', inner) and [
            a or b for a, b in re.findall(r'"([^"]+)"|\'([^\']+)\'', inner)
        ]
    # Look for source: "..."
    val = parse_field(fm, "source")
    if val:
        # Strip [[...]] wrapper if present
        val = re.sub(r'^\[\[(.+?)\]\]$', r'\1', val.strip())
        return [val]
    return []


def find_source_url(source_ref):
    """Given a source filename or wikilink, look in 00-Sources/papers/<base>.md for source: URL."""
    base = Path(source_ref).name
    # Strip extension if it's a wikilink stripped of suffix
    if not base.endswith(".md") and not base.endswith(".pdf"):
        candidate = SOURCES_DIR / f"{base}.md"
    else:
        candidate = SOURCES_DIR / base
    if candidate.suffix == ".pdf":
        # check sibling .md
        candidate = candidate.with_suffix(".md")
    if not candidate.exists():
        return None
    text = candidate.read_text(encoding="utf-8", errors="replace")
    fm, _ = split_frontmatter(text)
    if not fm:
        return None
    return parse_field(fm, "source")


def has_link(body):
    return bool(re.search(r'https?://', body))


def insert_link(text, link_line):
    """Insert link block before '## Related' or at end."""
    rel = re.search(r'^## Related\s*$', text, re.M)
    if rel:
        idx = rel.start()
        return text[:idx] + link_line + "\n" + text[idx:]
    # Append at end
    return text.rstrip() + "\n\n" + link_line + "\n"


def make_link_line(url, doi=None):
    if doi:
        return f"---\n**Source:** [DOI](https://doi.org/{doi}){' · [Open paper](' + url + ')' if url and 'doi.org' not in url else ''}"
    return f"---\n**Source:** [Open paper]({url})"


def process_summary(path):
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    if fm is None:
        return ("no-frontmatter", None)
    if has_link(body):
        return ("already-linked", None)

    doi = parse_field(fm, "doi")
    if doi:
        # Clean possible quotes / wrapper
        doi = doi.strip().strip('"\'')
        link_line = make_link_line(None, doi=doi)
        return ("doi-frontmatter", link_line)

    sources = parse_sources(fm)
    for src in sources:
        url = find_source_url(src)
        if url:
            return ("source-md-url", make_link_line(url))
    return ("needs-lookup", None)


def main():
    if not SUMMARIES.exists():
        print("ERROR: 10-Summaries/ not found", file=sys.stderr)
        sys.exit(1)
    stats = {"already-linked": 0, "doi-frontmatter": 0, "source-md-url": 0,
             "needs-lookup": 0, "no-frontmatter": 0}
    todo = []
    fixed = []
    for path in sorted(SUMMARIES.glob("*.md")):
        status, link_line = process_summary(path)
        stats[status] += 1
        if status in ("doi-frontmatter", "source-md-url") and link_line:
            text = path.read_text(encoding="utf-8")
            new_text = insert_link(text, link_line)
            if not DRY:
                path.write_text(new_text, encoding="utf-8")
            fixed.append((path.name, status))
        elif status == "needs-lookup":
            todo.append(path.name)

    print(f"\nSummary file scan: {sum(stats.values())} files")
    for k, v in stats.items():
        print(f"  {k:20s} {v}")

    if fixed:
        print(f"\n{'WOULD FIX' if DRY else 'FIXED'} ({len(fixed)} files):")
        for name, kind in fixed[:20]:
            print(f"  [{kind}] {name}")
        if len(fixed) > 20:
            print(f"  ... and {len(fixed) - 20} more")

    if todo:
        print(f"\nNEED PUBMED LOOKUP ({len(todo)} files) — PDF-only sources without DOI metadata:")
        for name in todo[:30]:
            print(f"  {name}")
        if len(todo) > 30:
            print(f"  ... and {len(todo) - 30} more")


if __name__ == "__main__":
    main()
