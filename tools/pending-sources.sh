#!/usr/bin/env bash
# List sources in 00-Sources/ that don't yet have a summary in 10-Summaries/,
# and covered sources whose file changed since the summary recorded its
# source_sha256 (e.g. a re-clipped paper). See tools/source-hash.py.
#
# A source is "covered" if any 10-Summaries/*.md has a frontmatter line
#   source: "[[00-Sources/<subdir>/<filename>]]"
# pointing at it (basename match, case-insensitive).
#
# This replaces the older slug-match logic, which produced false positives
# whenever a summary used the project's author-year slug convention
# (e.g. summary `creyghton-2010-h3k27ac-enhancers.md` vs source
# `Histone H3K27ac separates active from poised enhancers...md`).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCES="$VAULT/00-Sources"
SUMMARIES="$VAULT/10-Summaries"

cd "$VAULT"

python3 - "$SOURCES" "$SUMMARIES" <<'PY'
import os, re, sys, glob, hashlib

sources_dir, summaries_dir = sys.argv[1], sys.argv[2]

# 1. Index every summary's `source:` frontmatter reference (basename, lowercased)
covered = set()  # set of lowercased source basenames (no .md)
recorded = {}    # source basename -> (summary slug, source_sha256 recorded in it)
for sm in glob.glob(os.path.join(summaries_dir, '*.md')):
    try:
        with open(sm, encoding='utf-8') as f:
            head = f.read(4096)
    except Exception:
        continue
    # match the `source:` field in frontmatter, either a single link
    #   source: "[[00-Sources/.../Filename]]"
    # or a YAML list spanning several lines (used for merged summaries)
    #   source: [ "[[...]]", "[[...]]" ]
    fm = re.match(r'---\n(.*?)\n---', head, re.S)
    if not fm:
        continue
    field = re.search(r'^source:(.*?)(?=^\w[\w-]*:|\Z)', fm.group(1), re.M | re.S)
    if not field:
        continue
    refs = re.findall(r'\[\[(00-Sources/[^\]|"]+)', field.group(1))
    hashes = re.findall(r'[0-9a-f]{64}', (re.search(r'^source_sha256:(.*)$', fm.group(1), re.M) or [None, ''])[1])
    for i, ref in enumerate(refs):
        base = os.path.basename(ref.strip())
        base = re.sub(r'\.(md|pdf)$', '', base, flags=re.IGNORECASE)
        covered.add(base.lower())
        recorded[base.lower()] = (os.path.basename(sm)[:-3], hashes[i] if i < len(hashes) else None)

# 2. Walk all source files; flag those whose basename is not covered.
#    Skip hidden directories (e.g. stray .moai/ scratch state inside 00-Sources/).
total = 0
pending = []
changed = []
nohash = []
for root, dirs, files in os.walk(sources_dir):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for fn in files:
        if fn.startswith('.'):
            continue
        total += 1
        base = re.sub(r'\.[^.]+$', '', fn)
        rel = os.path.relpath(os.path.join(root, fn), os.path.dirname(sources_dir))
        if base.lower() not in covered:
            pending.append((rel, base))
            continue
        # 3. Covered: compare the file with the hash its summary recorded
        slug, want = recorded[base.lower()]
        if want is None:
            nohash.append(slug)
        else:
            with open(os.path.join(root, fn), 'rb') as f:
                if hashlib.sha256(f.read()).hexdigest() != want:
                    changed.append((slug, rel))

pending.sort()
for rel, _ in pending:
    print(f"PENDING  {rel}")
for slug, rel in sorted(changed):
    print(f"CHANGED  {slug}  <- {rel}")
for slug in sorted(set(nohash)):
    print(f"NOHASH   {slug}")
print()
print(f"{len(pending)} pending, {len(changed)} changed since summary, "
      f"{len(set(nohash))} without hash, of {total} total source file(s).")
if changed or nohash:
    print("After re-summarising, refresh hashes with: tools/source-hash.py <slug>")
PY
