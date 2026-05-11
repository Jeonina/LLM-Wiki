#!/usr/bin/env bash
# List sources in 00-Sources/ that don't yet have a summary in 10-Summaries/.
# Slug rule: <basename without extension>, lowercased, spaces -> hyphens.
# Run from anywhere; resolves the vault root relative to this script.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCES="$VAULT/00-Sources"
SUMMARIES="$VAULT/10-Summaries"

slugify() {
  basename "$1" \
    | sed -E 's/\.[^.]+$//' \
    | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g'
}

pending=0
total=0

while IFS= read -r -d '' src; do
  total=$((total + 1))
  slug=$(slugify "$src")
  if [[ ! -f "$SUMMARIES/$slug.md" ]]; then
    pending=$((pending + 1))
    rel="${src#$VAULT/}"
    echo "PENDING  $rel  ->  10-Summaries/$slug.md"
  fi
done < <(find "$SOURCES" -type f \! -name '.*' -print0)

echo
echo "$pending pending of $total total source file(s)."
