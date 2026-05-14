#!/usr/bin/env python3
"""
Look up DOIs via NCBI E-utilities for summary pages that lack source links.

For each summary in 10-Summaries/*.md that has no https:// link in its body:
  1. Parse the title from frontmatter (format: "Author YYYY — Paper title")
  2. Strip prefix, query PubMed esearch by remaining title (plus year if available)
  3. Take the top PMID, esummary to extract DOI
  4. Insert "**Source:** [DOI](https://doi.org/...)" line before "## Related" (or at EOF)

Rate-limited to NCBI's no-key limit (3 req/sec). State written to
tools/pubmed-lookup.state.json so re-runs resume on failures.

Run:  python3 tools/pubmed-lookup.py [--dry-run] [--limit N] [--verbose]
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
SUMMARIES = VAULT / "10-Summaries"
STATE_FILE = Path(__file__).resolve().parent / "pubmed-lookup.state.json"

DRY = "--dry-run" in sys.argv
VERBOSE = "--verbose" in sys.argv or "-v" in sys.argv
LIMIT = None
for i, a in enumerate(sys.argv):
    if a == "--limit" and i + 1 < len(sys.argv):
        LIMIT = int(sys.argv[i + 1])

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
HEADERS = {"User-Agent": "LLM-Wiki-DOI-Retrofit/1.0 (mailto:claude_group1@baelab.org)"}
SLEEP = 0.4  # seconds between requests (~2.5 req/s, under the 3/s no-key limit)


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"resolved": {}, "failed": {}}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def parse_frontmatter(text):
    parts = text.split("---", 2)
    if len(parts) >= 3 and parts[0] == "":
        return parts[1], parts[2]
    return None, text


def field(fm, key):
    m = re.search(rf'^{re.escape(key)}\s*:\s*(.+)$', fm, re.M)
    if not m:
        return None
    v = m.group(1).strip()
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        v = v[1:-1]
    return v


def has_link(body):
    return bool(re.search(r'https?://', body))


def parse_title_for_query(title):
    """
    Title formats observed:
      "Tang 2009 — mRNA-Seq whole-transcriptome analysis of a single cell"
      "Nam 2019 — Genotyping of Transcriptomes (GoT) links somatic mutations to cell identity"
      "Bannister & Kouzarides 2011 — Regulation of chromatin by histone modifications"
      "Comprehensive analysis of single cell ATAC-seq data with SnapATAC"  (no prefix)
    Returns (clean_title, year, first_author_surname).
    """
    year = None
    author = None
    m = re.search(r'\b(19|20)\d{2}\b', title)
    if m:
        year = m.group(0)
    # Try to extract "Author(s) YYYY —" prefix
    pre_m = re.match(r'^(.{1,80}?)\s+(19|20)\d{2}\s*[—–\-]+\s*(.*)$', title)
    if pre_m:
        author_block = pre_m.group(1).strip()
        cleaned = pre_m.group(3).strip()
        # Author block may be "Smith", "Smith & Jones", "Smith et al.", "Smith, Jones & Lee"
        # Take first surname-looking word
        words = re.split(r'[\s,&]+', author_block)
        for w in words:
            if w and w[0].isupper() and len(w) > 1 and w.lower() not in {"et", "al", "and"}:
                author = w
                break
    else:
        cleaned = title
    return cleaned.strip(), year, author


def looks_like_match(info, query_title, year_expected, author_expected):
    """Strict verification:
       - if author given, MUST appear in matched authors list
       - year within ±1 of expected
       - at least 2 significant title words shared (or all if title is short)
    """
    matched_title = info["title"]
    matched_year = info["year"]
    matched_authors = info.get("authors", [])

    if year_expected and matched_year:
        try:
            if abs(int(matched_year) - int(year_expected)) > 1:
                return False
        except ValueError:
            pass

    if author_expected:
        # Author surname must appear in matched authors (case-insensitive substring)
        au_lower = author_expected.lower()
        found = any(au_lower in a.lower() for a in matched_authors)
        if not found:
            return False

    def words(s):
        return {w.lower() for w in re.findall(r'[A-Za-z]{4,}', s)
                if w.lower() not in {"single", "cell", "cells", "with", "from", "using",
                                     "analysis", "data", "between", "approach", "method",
                                     "review", "study", "human", "humans"}}

    qw = words(query_title)
    mw = words(matched_title)
    if not qw:
        return True
    overlap = qw & mw
    if len(qw) <= 3:
        return len(overlap) >= 1
    return len(overlap) >= 2


def http_get_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def clean_for_query(q):
    """Strip punctuation that confuses PubMed; keep alphanumerics and spaces."""
    q = re.sub(r'\([^)]*\)', ' ', q)  # remove parenthetical contents
    q = re.sub(r'[^A-Za-z0-9\- ]+', ' ', q)
    q = re.sub(r'\s+', ' ', q).strip()
    return q


def short_title_query(q, n_words=6):
    """Take first n significant words for title query."""
    q = clean_for_query(q)
    words = [w for w in q.split() if len(w) > 2]
    return ' '.join(words[:n_words])


def esearch(query, year=None, author=None, retmax=5, use_title_field=True):
    parts = []
    if author:
        parts.append(f'{author}[Author]')
    if query:
        if use_title_field and len(query) < 100:
            parts.append(f'{query}[Title]')
        else:
            parts.append(query)
    if year:
        parts.append(f'{year}[pdat]')
    term = ' AND '.join(parts)
    params = {"db": "pubmed", "term": term, "retmode": "json", "retmax": str(retmax)}
    url = f"{EUTILS}/esearch.fcgi?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    return data.get("esearchresult", {}).get("idlist", [])


def esummary(pmid):
    params = {"db": "pubmed", "id": pmid, "retmode": "json"}
    url = f"{EUTILS}/esummary.fcgi?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    result = data.get("result", {}).get(pmid, {})
    doi = None
    for aid in result.get("articleids", []):
        if aid.get("idtype") == "doi":
            doi = aid.get("value")
            break
    pubdate = result.get("pubdate", "")
    year = pubdate.split()[0] if pubdate else ""
    authors = [a.get("name", "") for a in result.get("authors", [])]
    return {
        "doi": doi,
        "title": result.get("title", ""),
        "year": year,
        "journal": result.get("source", ""),
        "authors": authors,
    }


def insert_link(text, link_line):
    rel = re.search(r'^## Related\s*$', text, re.M)
    if rel:
        return text[:rel.start()] + link_line + "\n\n" + text[rel.start():]
    return text.rstrip() + "\n\n" + link_line + "\n"


def make_link_line(doi, pmid):
    return f"---\n**Source:** [DOI](https://doi.org/{doi}) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)"


def process(path, state):
    name = path.name
    if name in state["resolved"]:
        return ("cached-resolved", None, None)
    if name in state["failed"] and state["failed"][name].get("attempts", 0) >= 2:
        return ("cached-failed", None, None)

    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if fm is None:
        return ("no-frontmatter", None, None)
    if has_link(body):
        return ("already-linked", None, None)

    title = field(fm, "title")
    if not title:
        return ("no-title", None, None)

    query, year, author = parse_title_for_query(title)
    if len(query) < 8:
        return ("title-too-short", None, None)

    # Build multiple query variants: full, short title, cleaned
    full_q = clean_for_query(query)
    short_q = short_title_query(query, n_words=6)
    very_short_q = short_title_query(query, n_words=4)

    # Strategy: try queries in decreasing strictness, verify each result
    attempts = []
    if author and year:
        attempts.append({"query": short_q, "year": year, "author": author})
        attempts.append({"query": very_short_q, "year": year, "author": author})
    if author:
        attempts.append({"query": short_q, "year": None, "author": author})
        # Title-only via PubMed default field (less strict)
        attempts.append({"query": short_q, "year": None, "author": author, "use_title_field": False})
    if year:
        attempts.append({"query": short_q, "year": year, "author": None})
    attempts.append({"query": short_q, "year": None, "author": None})

    best_match = None
    for att in attempts:
        try:
            pmids = esearch(**att)
            time.sleep(SLEEP)
        except Exception as e:
            return ("esearch-error", None, str(e))
        if VERBOSE:
            print(f"      attempt {att} -> {pmids}", flush=True)
        if not pmids:
            continue
        # Examine each candidate, prefer first verified match
        for pmid in pmids[:3]:
            try:
                info = esummary(pmid)
                time.sleep(SLEEP)
            except Exception:
                continue
            if not info["doi"]:
                continue
            if looks_like_match(info, query, year, author):
                return ("resolved", (info["doi"], pmid, info["title"]), None)
            elif best_match is None:
                best_match = (info["doi"], pmid, info["title"], "unverified")
        # Always try the next, looser attempt — strict-verified beats unverified

    if best_match:
        # Unverified — log but don't insert
        return ("unverified-match", best_match[:3], None)

    return ("no-match", None, None)


def main():
    state = load_state()
    pending = []
    for path in sorted(SUMMARIES.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        if fm is None or has_link(body):
            continue
        if path.name in state["resolved"]:
            continue
        pending.append(path)

    print(f"Pending: {len(pending)} summaries to look up", flush=True)
    if LIMIT:
        pending = pending[:LIMIT]
        print(f"Limited to first {LIMIT}", flush=True)

    counts = {}
    for i, path in enumerate(pending, 1):
        status, payload, err = process(path, state)
        counts[status] = counts.get(status, 0) + 1

        if status == "resolved":
            doi, pmid, pm_title = payload
            state["resolved"][path.name] = {"doi": doi, "pmid": pmid, "matched_title": pm_title}
            if not DRY:
                text = path.read_text(encoding="utf-8")
                new_text = insert_link(text, make_link_line(doi, pmid))
                path.write_text(new_text, encoding="utf-8")
            if VERBOSE or i % 10 == 0:
                print(f"[{i}/{len(pending)}] {status:18s} {path.name} -> {doi}", flush=True)
        else:
            f = state["failed"].setdefault(path.name, {"attempts": 0, "last_status": ""})
            f["attempts"] = f.get("attempts", 0) + 1
            f["last_status"] = status
            if err:
                f["last_error"] = err
            if VERBOSE or status not in ("no-match", "title-too-short"):
                print(f"[{i}/{len(pending)}] {status:18s} {path.name}", flush=True)

        if i % 25 == 0:
            save_state(state)

    save_state(state)

    print("\n=== Summary ===", flush=True)
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {k:20s} {v}", flush=True)
    print(f"\nTotal resolved: {len(state['resolved'])}", flush=True)
    print(f"Total failed:   {len(state['failed'])}", flush=True)


if __name__ == "__main__":
    main()
