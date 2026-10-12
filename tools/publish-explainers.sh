#!/usr/bin/env bash
# Copy hand-built explainer pages into the Quartz build output with their .html
# extension. Quartz copies non-Markdown files as assets but strips ".html", which
# would make GitHub Pages serve them as downloads. Run after `npx quartz build`.
set -euo pipefail
cd "$(dirname "$0")/.."
out=".quartz/public/60-Explainers"
mkdir -p "$out"
for f in 60-Explainers/*.html 60-Explainers/*.css 60-Explainers/*.js; do
  [ -e "$f" ] || continue
  name="$(basename "$f")"
  cp "$f" "$out/$name"
  case "$name" in *.html) rm -f "$out/${name%.html}" ;; esac
  echo "published $out/$name"
done
