---
type: concept
title: TAPS
aliases: [TET-assisted pyridine borane sequencing]
tags: [methylation, bisulfite-free, 5mC, TET, base-resolution]
created: 2026-05-12
updated: 2026-05-12
---

# TAPS

> A bisulfite-free chemistry that detects 5mC at single-base resolution by **TET oxidation of 5mC to 5caC**, then **pyridine-borane reduction of 5caC to DHU** (which reads as T). Developed by the Chun-Xiao Song lab. Used in scEpi²-seq and other methods that need to preserve DNA integrity.

## Definition

Sequential enzymatic + chemical reactions: TET enzymes oxidize 5mC → 5fC → 5caC → (borane reduction) → DHU. The unmodified C remains unchanged. After PCR, 5mC sites appear as C→T conversions but **DNA is not degraded** as it is by bisulfite.

## Why it matters

Bisulfite degrades up to 90% of input DNA and destroys cell-barcode adaptors used in single-cell methods that ligate barcodes before conversion. TAPS preserves them.

## Examples

- Single-cell joint methylation + histone-mark profiling: [[10-Summaries/geisenberger-2025-scepi2-seq]] (scEpi²-seq).
- 5mC labeling in [[10-Summaries/bai-2024-simple-seq]] (SIMPLE-seq).
- TAPS does not distinguish 5mC from 5hmC alone; pairing with hmC-CATCH (in SIMPLE-seq) or with sequential blocking can resolve them.

## Related

- [[30-Concepts/bisulfite-sequencing]] · [[30-Concepts/5hmc]] · [[30-Concepts/tet-enzymes]] · [[40-Topics/dna-methylation]] · [[20-Entities/chun-xiao-song]]
