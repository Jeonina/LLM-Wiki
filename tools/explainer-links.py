#!/usr/bin/env python3
"""Link hub pages and their concept pages to the teaching pages in 60-Explainers/.

A hub opts in with `explainer: <file stem>` in its frontmatter (e.g. `explainer:
wga-simulator` for 60-Explainers/wga-simulator.html). This tool then:

  * puts a `> [!tip] 📘 교재` callout right after the page's `한눈에` callout on the hub
    and on every concept page listed in the hub's "Start here" cards (a concept that
    belongs to several hubs lists every explainer);
  * rewrites the card list in 60-Explainers/index.md between the marker comments.

The callout is wrapped in <!-- explainer-links --> markers and regenerated on each
run, so the tool is idempotent. Use --check to report stale pages without writing.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BEGIN, END = "<!-- explainer-links -->", "<!-- /explainer-links -->"
IDX_BEGIN, IDX_END = "<!-- explainer-index -->", "<!-- /explainer-index -->"


def frontmatter_field(text: str, key: str) -> str | None:
    if not text.startswith("---"):
        return None
    fm = text.split("\n---", 1)[0]
    m = re.search(rf"^{key}:\s*\"?([^\"\n]+)\"?\s*$", fm, re.M)
    return m.group(1).strip() if m else None


def html_title(path: Path) -> str:
    m = re.search(r"<title>(.*?)</title>", path.read_text(encoding="utf-8"), re.S)
    return m.group(1).strip() if m else path.stem


def hub_concepts(text: str) -> list[str]:
    m = re.search(r"^## Start here\n(.*?)(?=^## )", text, re.S | re.M)
    return re.findall(r"\[\[30-Concepts/([^\]|#]+)", m.group(1)) if m else []


def strip_block(text: str) -> str:
    return re.sub(rf"\n?{re.escape(BEGIN)}.*?{re.escape(END)}\n?", "\n", text, flags=re.S)


def insert_block(text: str, links: list[tuple[str, str]], depth: str) -> str:
    text = strip_block(text)
    if not links:
        return text
    lines = [BEGIN, "> [!tip] 📘 교재"]
    for stem, title in links:
        lines.append(f"> [{title}]({depth}60-Explainers/{stem}.html)")
        lines.append(">")
    lines[-1] = END
    block = "\n".join(lines)
    L = text.split("\n")
    anchor = next((i for i, l in enumerate(L) if l.startswith("> [!abstract] 한눈에")), None)
    if anchor is None:  # fall back to after the first heading
        anchor = next((i for i, l in enumerate(L) if l.startswith("# ")), 0)
    j = anchor + 1
    while j < len(L) and L[j].startswith(">"):
        j += 1
    L[j:j] = ["", block]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(L))


def main(argv: list[str]) -> int:
    check = "--check" in argv
    hubs = sorted((ROOT / "40-Topics").glob("*.md"))
    page_links: dict[Path, list[tuple[str, str]]] = {}
    index_cards = []
    for hub in hubs:
        text = hub.read_text(encoding="utf-8")
        stem = frontmatter_field(text, "explainer")
        if not stem:
            continue
        html = ROOT / "60-Explainers" / f"{stem}.html"
        if not html.exists():
            print(f"missing explainer for {hub.name}: {html}", file=sys.stderr)
            return 2
        title = html_title(html)
        hub_title = frontmatter_field(text, "title") or hub.stem
        page_links.setdefault(hub, []).append((stem, title))
        for c in hub_concepts(text):
            cp = ROOT / "30-Concepts" / f"{c}.md"
            if cp.exists() and (stem, title) not in page_links.setdefault(cp, []):
                page_links[cp].append((stem, title))
        index_cards.append(f"> - `{hub_title}` [{title}](../60-Explainers/{stem}.html) — [[40-Topics/{hub.stem}|{hub_title}]] hub의 교재.")

    # pages that used to carry a block but no longer qualify
    for p in list((ROOT / "30-Concepts").glob("*.md")) + hubs:
        if p not in page_links and BEGIN in p.read_text(encoding="utf-8"):
            page_links[p] = []

    stale = []
    for p, links in sorted(page_links.items()):
        old = p.read_text(encoding="utf-8")
        new = insert_block(old, links, "../")
        if new != old:
            stale.append(p.relative_to(ROOT))
            if not check:
                p.write_text(new, encoding="utf-8")

    idx = ROOT / "60-Explainers" / "index.md"
    itext = idx.read_text(encoding="utf-8")
    cards = "\n".join([IDX_BEGIN, "> [!cards]", *index_cards, IDX_END])
    if IDX_BEGIN in itext:
        new_idx = re.sub(rf"{re.escape(IDX_BEGIN)}.*?{re.escape(IDX_END)}", lambda _: cards, itext, flags=re.S)
    else:
        new_idx = re.sub(r"> \[!cards\]\n(> - .*\n)+", cards + "\n", itext, count=1)
    if new_idx != itext:
        stale.append(idx.relative_to(ROOT))
        if not check:
            idx.write_text(new_idx, encoding="utf-8")

    if check:
        if stale:
            print("stale explainer links:", *stale, sep="\n  ")
            return 1
        return 0
    print(f"updated {len(stale)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
