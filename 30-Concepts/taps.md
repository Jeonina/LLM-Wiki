---
type: concept
title: TAPS
aliases: [TET-assisted pyridine borane sequencing]
tags: [methylation, bisulfite-free, 5mC, TET, base-resolution]
created: 2026-05-12
updated: 2026-08-10
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

## Single-cell implementation

- **scTAPS / scCAPS+** bring TAPS and CAPS+ chemistry to single cells by pairing barcoded Tn5 fragmentation with pooling of 96 barcoded cells *before* the conversion chemistry ([[10-Summaries/chen-2025-sctaps-sccaps-plus]]).
- **Direct conversion preserves complexity.** TAPS converts the modified base (5mC/5hmC → T) rather than unmodified cytosine, so mapping reaches 93.0% (scTAPS) and 89.4% (scCAPS+) ([[10-Summaries/chen-2025-sctaps-sccaps-plus]]).
- **Quantified accuracy.** Spike-in conversion rates: scTAPS 5mCG 96.6% / 5hmCG 85.0%; scCAPS+ 5hmCG 93.0%. False positives 0.19% and 0.38% on unmodified C, and 0.25% on 5mCG for scCAPS+ ([[10-Summaries/chen-2025-sctaps-sccaps-plus]]).
- **Depth over throughput.** 2.0–2.3 M CpG sites covered per cell (8.08–10.88% of all CpGs), against 1.96%/0.79% for the higher-throughput SIMPLE-seq, which also needs a standard curve to correct its ~87% 5mC conversion ([[10-Summaries/chen-2025-sctaps-sccaps-plus]]).

## Related

- [[30-Concepts/bisulfite-sequencing]] · [[30-Concepts/5hmc]] · [[30-Concepts/tet-enzymes]] · [[40-Topics/dna-methylation]] · [[20-Entities/chun-xiao-song]]
- [[10-Summaries/chen-2025-sctaps-sccaps-plus]] · [[30-Concepts/simple-seq]] · [[10-Summaries/tahiliani-2009-tet1-5hmc]]
