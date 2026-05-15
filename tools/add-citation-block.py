#!/usr/bin/env python3
"""
Insert a standardized one-line citation block at the top of every 10-Summaries/*.md
file so first-author, year, journal, and paper title are findable at a glance.

Format inserted right after frontmatter (idempotent — won't duplicate):

    **Citation:** LastName et al. (YYYY) — *Paper title* — *Journal*. [DOI](https://doi.org/...)

Sources (in priority order):
1. Frontmatter fields (author / published / journal / doi / title)
2. Title field, pattern "LastName YYYY — Title"
3. Source filename like "FirstName_YYYY_Journal.pdf"
4. First "Source: [DOI](...)" line in body
"""
import os, re, sys, yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUMMARIES = ROOT / "10-Summaries"

# Normalize journal names (filename-style → human-readable)
JOURNAL_NORMALIZE = {
    "naturebiotechnology": "Nature Biotechnology",
    "naturemethods": "Nature Methods",
    "naturegenetics": "Nature Genetics",
    "naturecommunications": "Nature Communications",
    "naturereviewsgenetics": "Nature Reviews Genetics",
    "naturereviewsmolecularcellbiology": "Nature Reviews Molecular Cell Biology",
    "naturereviewsneuroscience": "Nature Reviews Neuroscience",
    "naturereviewscancer": "Nature Reviews Cancer",
    "natureaging": "Nature Aging",
    "naturereviewsmicrobiology": "Nature Reviews Microbiology",
    "nature": "Nature",
    "science": "Science",
    "cell": "Cell",
    "cellresearch": "Cell Research",
    "cellsystems": "Cell Systems",
    "cellstemcell": "Cell Stem Cell",
    "cellreports": "Cell Reports",
    "molecularcell": "Molecular Cell",
    "neuron": "Neuron",
    "elife": "eLife",
    "pnas": "PNAS",
    "genomeresearch": "Genome Research",
    "genomebiology": "Genome Biology",
    "bioinformatics": "Bioinformatics",
    "briefingsinbioinformatics": "Briefings in Bioinformatics",
    "biorxiv": "bioRxiv (preprint)",
    "plosone": "PLOS One",
    "ploscompbio": "PLOS Comp Biol",
    "plosbiology": "PLOS Biology",
    "trendsingenetics": "Trends in Genetics",
    "annualreviewofgenomicsandhumangenetics": "Annu Rev Genomics Hum Genet",
    "experimentalmolecularmedicine": "Exp Mol Med",
    "genomicsproteomicsbioinformatics": "Genomics, Proteomics & Bioinformatics",
    "journalofappliedbiologyandbiotechnology": "J Appl Biol Biotechnol",
    "methodsinmolecularbiology": "Methods Mol Biol",
}

def normalize_journal(j):
    if not j: return None
    key = re.sub(r'[^a-z]', '', str(j).lower())
    return JOURNAL_NORMALIZE.get(key, str(j).strip())

def parse_frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m: return None, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        fm = {}
    body = text[m.end():]
    return fm, body

def extract_last_name_from_title(title):
    """Title like 'Abdulhay 2020 — SAMOSA: ...' → 'Abdulhay'"""
    if not title: return None
    title = str(title)
    # match leading "LastName [et al.] YYYY"
    m = re.match(r'^([A-Z][A-Za-z\'-]+)(?:\s+et\s+al\.?)?\s+(?:19|20)\d{2}\b', title)
    return m.group(1) if m else None

def extract_paper_title_from_title(title):
    """Title like 'Abdulhay 2020 — SAMOSA: massively multiplex ...' → 'SAMOSA: massively multiplex ...'"""
    if not title: return None
    title = str(title)
    # split on em dash / en dash / hyphen-space
    for sep in [' — ', ' – ', ' - ']:
        if sep in title:
            parts = title.split(sep, 1)
            if len(parts) == 2:
                return parts[1].strip()
    return title

def extract_year(fm, title, filename=None):
    """Year-in-title is most reliable (always pub year). Then explicit `published`. `created`/`ingested` only as last resort because they are ingest dates."""
    if title:
        m = re.search(r'\b((?:19|20)\d{2})\b', str(title))
        if m: return m.group(1)
    pub = fm.get("published")
    if pub:
        m = re.search(r'(19|20)\d{2}', str(pub))
        if m: return m.group(0)
    if filename:
        m = re.search(r'\b((?:19|20)\d{2})\b', filename)
        if m: return m.group(1)
    pub2 = fm.get("created") or fm.get("ingested")
    if pub2:
        m = re.search(r'(19|20)\d{2}', str(pub2))
        if m: return m.group(0)
    return None

def extract_journal_from_source(fm):
    """sources field like 'Nour_2020_eLife.pdf' → 'eLife'"""
    src = fm.get("sources") or fm.get("source")
    if isinstance(src, list):
        src = src[0] if src else None
    if not src: return None
    s = str(src)
    # strip path and extension
    s = re.sub(r'.*?([^/\]]+?)(\.pdf|\.md|\]?)$', r'\1', s)
    s = s.replace("[[", "").replace("]]", "")
    parts = s.split("_")
    if len(parts) >= 3:
        # Last part = journal (might have semicolons)
        j = parts[-1].split(".")[0].split(";")[0]
        return j
    return None

def extract_doi_from_body(body):
    m = re.search(r'(?:doi\.org/|doi:\s*)([\w./()\-]+)', body, re.IGNORECASE)
    if m:
        doi = m.group(1).rstrip('.,);')
        return doi
    return None

def has_citation_block(body):
    """Check if standard citation block already present (idempotent guard)."""
    head = body[:600]
    return bool(re.search(r'\*\*Citation:\*\*', head))

def build_citation(fm, title, body, filename=None):
    # 1. First-author last name
    author_str = fm.get("author")
    last_name = None
    if author_str:
        # author field may be "Last F, Last2 F2, ..." or "First Last, First2 Last2"
        first_author = str(author_str).split(",")[0].strip()
        # Heuristic: if first token capitalized as "Word", last word is last name
        tokens = first_author.split()
        if tokens:
            last_name = tokens[-1].strip(".,;:")
    if not last_name:
        last_name = extract_last_name_from_title(title)
    if not last_name:
        last_name = "?"

    # 2. Year
    year = extract_year(fm, title, filename=filename) or "????"

    # 3. Paper title
    ptitle = extract_paper_title_from_title(title) or str(title or "(no title)")
    # Strip any leading method-name colon spam — keep as is for safety

    # 4. Journal
    journal = normalize_journal(fm.get("journal")) or normalize_journal(extract_journal_from_source(fm)) or "?"

    # 5. DOI
    doi = fm.get("doi") or extract_doi_from_body(body)
    doi_part = f" [DOI](https://doi.org/{doi})" if doi else ""

    # Build line
    et_al = " et al." if (author_str and "," in str(author_str)) or "et al" not in (title or "") else ""
    return f"**Citation:** {last_name}{et_al} ({year}) — *{ptitle}* — *{journal}*.{doi_part}"

def process_file(path, dry_run=False):
    text = path.read_text()
    fm, body = parse_frontmatter(text)
    if fm is None:
        return False, "no frontmatter"
    if has_citation_block(body):
        return False, "already has citation block"

    title = fm.get("title")
    citation = build_citation(fm, title, body, filename=path.name)

    # Insert citation right after frontmatter close, on its own line, with blank lines around it
    new_text = text[:text.find('---\n', 3)+4]  # up to and including second '---\n'
    # Find end of frontmatter properly
    m = re.match(r'^(---\n.*?\n---\n)', text, re.DOTALL)
    if not m:
        return False, "frontmatter regex failed"
    fm_block = m.group(1)
    rest = text[m.end():]
    # Strip leading blank lines from rest
    rest_stripped = rest.lstrip('\n')
    new_text = fm_block + "\n" + citation + "\n\n" + rest_stripped

    if not dry_run:
        path.write_text(new_text)
    return True, citation

def main():
    dry_run = "--dry" in sys.argv
    limit = None
    if "--limit" in sys.argv:
        i = sys.argv.index("--limit")
        limit = int(sys.argv[i+1])

    files = sorted(SUMMARIES.glob("*.md"))
    if limit: files = files[:limit]

    n_done = n_skip = 0
    for p in files:
        ok, msg = process_file(p, dry_run=dry_run)
        if ok:
            n_done += 1
            if dry_run or n_done <= 5:
                print(f"+ {p.name}")
                print(f"  {msg}")
        else:
            n_skip += 1

    mode = "DRY-RUN" if dry_run else "APPLIED"
    print(f"\n{mode}: inserted {n_done}, skipped {n_skip}, total {len(files)}")

if __name__ == "__main__":
    main()
