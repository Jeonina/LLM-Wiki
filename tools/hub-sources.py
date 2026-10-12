#!/usr/bin/env python3
"""Rebuild the folded "All sources on this page" block on hub pages.

The block lists every 10-Summaries page the hub links to, labelled with the
author/year (or tool) prefix of its entry in 10-Summaries/index.md. It is the
last section of a hub page and is replaced wholesale on each run.

Usage:
  tools/hub-sources.py 40-Topics/<slug>.md [...]   rewrite the block in place
  tools/hub-sources.py --check 40-Topics/*.md      exit 1 if any block is stale
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADING = "## All sources on this page"
LINK = re.compile(r"\[\[10-Summaries/([A-Za-z0-9_.-]+)")
ENTRY = re.compile(r"- \[\[10-Summaries/([A-Za-z0-9_.-]+)\]\] — (.*)")


def catalog_labels() -> dict[str, str]:
    labels = {}
    for line in (ROOT / "10-Summaries/index.md").read_text(encoding="utf-8").splitlines():
        m = ENTRY.match(line)
        if m:
            # "Navin 2011, tumour evolution ..." -> "Navin 2011"
            desc = re.sub(r"^\([^)]*\)\s*", "", m.group(2))  # drop "(genotype gap)" tags
            label = re.split(r"[,:]", desc, maxsplit=1)[0].strip().rstrip(".")
            if label.count("(") != label.count(")"):  # "Wang 2024 (bioRxiv preprint"
                label = label.split("(")[0].strip()
            if not (0 < len(label) <= 40 and re.search(r"\d{4}|^[A-Z]", label)):
                s = re.match(r"([a-z]+)-(\d{4})", m.group(1))  # fall back to "Weinstock 2025"
                label = f"{s.group(1).capitalize()} {s.group(2)}" if s else m.group(1)
            labels[m.group(1)] = label
    return labels


def build(text: str, labels: dict[str, str]) -> str:
    body = text.split(HEADING)[0].rstrip("\n")
    slugs = sorted(set(LINK.findall(body)))
    if not slugs:
        return body + "\n"
    lines = [f"> - [[10-Summaries/{s}|{labels.get(s, s)}]]" for s in slugs]
    block = f"{HEADING}\n\n> [!info]- {len(slugs)} summaries cited here\n" + "\n".join(lines)
    return f"{body}\n\n{block}\n"


def main(argv: list[str]) -> int:
    check = "--check" in argv
    paths = [Path(a) for a in argv if a != "--check"]
    labels = catalog_labels()
    stale = []
    for p in paths:
        old = p.read_text(encoding="utf-8")
        new = build(old, labels)
        if new != old:
            stale.append(str(p))
            if not check:
                p.write_text(new, encoding="utf-8")
    if check and stale:
        print("stale source blocks:", *stale, sep="\n  ")
        return 1
    if not check:
        print(f"updated {len(stale)} of {len(paths)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
