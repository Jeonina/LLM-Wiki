#!/usr/bin/env python3
"""
Lint 10-Summaries/ and report concept-page gaps. Read-only: prints a report, edits nothing.

Checks
  1. Provenance  — every summary has source_quality (full | partial | abstract) and source_sha256.
  2. Sections    — the canonical sections of 90-Meta/templates/summary.md are present.
                   `## Limitations` (authors' own vs reviewer notes) is required only for
                   summaries ingested after LIMITATIONS_FROM; older ones are not back-filled.
                   Summaries in the older short format are counted as "legacy", not errors.
  3. Concept gaps — tags carried by >= --min summaries that match no concept/entity/topic
                   page (by filename, title or alias). A near-match column suggests when the
                   tag is just a synonym of an existing page (add an alias) rather than a gap.

Usage:
    tools/lint-summaries.py                 full report
    tools/lint-summaries.py --min 4         lower the concept-gap threshold
    tools/lint-summaries.py --verbose       also list every legacy-format summary
"""
import argparse, difflib, glob, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUALITIES = {"full", "partial", "abstract"}
REQUIRED = ["## Key claims", "## Methods / evidence", "## Connections to other sources", "## Related"]
LIMITATIONS_FROM = "2026-10-07"  # summaries ingested after this date need ## Limitations
# Tags that describe the kind of paper rather than a concept; never reported as gaps.
GENERIC = {"review", "single-cell", "foundational", "founding-method", "computational",
           "computational-tool", "benchmark", "benchmarking", "protocol", "software", "tool",
           "method", "methods", "cancer", "brain", "chromatin", "human", "mouse", "dataset",
           "atlas", "perspective", "commentary", "preprint", "partial-clipping"}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    return m.group(1) if m else ""


def list_field(fm, key):
    m = re.search(rf"^{key}:\s*\[(.*?)\]", fm, re.M)
    return [x.strip(" \"'") for x in m.group(1).split(",") if x.strip(" \"'")] if m else []


def scalar(fm, key):
    m = re.search(rf'^{key}:\s*"?([^"\n]*)"?', fm, re.M)
    return m.group(1).strip() if m else ""


def known_pages():
    names = {}
    for d in ("20-Entities", "30-Concepts", "40-Topics"):
        for p in glob.glob(os.path.join(ROOT, d, "*.md")):
            stem = os.path.basename(p)[:-3]
            fm = frontmatter(open(p, encoding="utf-8").read())
            for n in [stem, scalar(fm, "title"), *list_field(fm, "aliases")]:
                if n:
                    names[slug(n)] = f"{d}/{stem}"
    return names


def near(tag, names):
    """An existing page the tag probably means, judged on page filenames only:
    the filename contains every word of the tag plus at most two more, or is a close spelling."""
    stems = {page.split("/")[1]: page for page in names.values()}
    toks = tag.split("-")
    for stem, page in stems.items():
        st = stem.split("-")
        if all(any(min(len(s), len(t)) >= 3 and (s.startswith(t) or t.startswith(s)) for s in st) for t in toks) and len(st) - len(toks) <= 2:
            return page
    m = difflib.get_close_matches(tag, list(stems), n=1, cutoff=0.8)
    return stems[m[0]] if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=int, default=5)
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    no_prov, bad_quality, weak, missing, legacy, no_limits = [], [], [], [], [], []
    tags = Counter()
    files = sorted(glob.glob(os.path.join(ROOT, "10-Summaries", "*.md")))
    files = [f for f in files if not f.endswith("/index.md")]
    for path in files:
        s = os.path.basename(path)[:-3]
        text = open(path, encoding="utf-8").read()
        fm = frontmatter(text)
        q = scalar(fm, "source_quality")
        if not q or not re.search(r"^source_sha256:", fm, re.M):
            no_prov.append(s)
        elif q not in QUALITIES:
            bad_quality.append(f"{s} ({q})")
        elif q != "full":
            weak.append(f"{s} ({q})")
        heads = set(re.findall(r"^## .*?$", text, re.M))
        heads = {h.strip() for h in heads}
        gone = [h for h in REQUIRED if h not in heads]
        if len(gone) >= 3:
            legacy.append(s)
        elif gone:
            missing.append(f"{s}: {', '.join(gone)}")
        if scalar(fm, "ingested") > LIMITATIONS_FROM and "## Limitations" not in heads:
            no_limits.append(s)
        for t in {slug(t) for t in list_field(fm, "tags")}:
            tags[t] += 1

    def show(title, items, always=True):
        if items or always:
            print(f"\n## {title}: {len(items)}")
            for i in items:
                print(f"  - {i}")

    print(f"# Summary lint — {len(files)} summaries")
    show("Missing source_quality or source_sha256 (run tools/source-hash.py)", no_prov)
    show("Invalid source_quality value", bad_quality, always=False)
    show("Not full text (partial / abstract)", weak)
    show("Missing canonical sections", missing)
    show(f"Missing ## Limitations (ingested after {LIMITATIONS_FROM})", no_limits)
    print(f"\n## Legacy short format (3+ canonical sections absent): {len(legacy)}")
    if a.verbose:
        for s in legacy:
            print(f"  - {s}")

    names = known_pages()
    gaps = [(t, n) for t, n in tags.most_common()
            if n >= a.min and t not in GENERIC and not t.endswith("-lab") and t not in names]
    print(f"\n## Concept gaps: tags on >= {a.min} summaries with no page: {len(gaps)}")
    print("  (near match = probably a synonym; add it as an alias there instead of a new page)")
    for t, n in gaps:
        m = near(t, names)
        print(f"  - {t} ({n})" + (f"  ~ near match: [[{m}]]" if m else ""))


if __name__ == "__main__":
    main()
