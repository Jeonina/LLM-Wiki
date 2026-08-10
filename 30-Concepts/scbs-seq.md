---
type: concept
title: scBS-seq
aliases: [single-cell bisulfite sequencing, single-cell whole-genome bisulfite sequencing]
tags: [methylation, single-cell, bisulfite, genome-wide]
created: 2026-05-12
updated: 2026-08-10
---

# scBS-seq

> Single-cell bisulfite sequencing. Profiles genome-wide CpG methylation per cell using bisulfite conversion. Sparse coverage (~10–40% of CpGs detected per cell at ~20M reads); bisulfite-induced DNA degradation limits library complexity.

## Why it matters

- Foundational method for single-cell methylomics (Smallwood et al. 2014).
- Cost-prohibitive at atlas scale; motivates alternatives like [[30-Concepts/sctem-seq]] (TE-targeted), sci-MET (combinatorial-indexing), and TAPS-based methods.

## Preprocessing is not neutral

- **Tile-averaging dilutes signal.** The standard 100 kb-tile-and-average recipe drowns small variably-methylated regions in uninformative CpGs, and sparse per-cell coverage means different cells are represented by reads at *different positions* within a tile ([[10-Summaries/kremer-2024-methscan]]).
- **Read-position-aware quantitation**: compare each cell to a kernel-smoothed cross-cell average at the CpGs it actually observed, and average the signed residuals with shrinkage ([[10-Summaries/kremer-2024-methscan]]).
- **VMRs beat annotation.** 63,421 de novo variably methylated regions match the cell-typing performance of 339,815 ENCODE cCREs, and outperform an equal-sized cCRE subset; VMR methylation also predicts expression better than promoter methylation ([[10-Summaries/kremer-2024-methscan]]).
- **DMR detection for scBS did not exist before 2024** — sliding-window *t* statistics with permutation-based FDR now make it possible ([[10-Summaries/kremer-2024-methscan]]).
- **All bisulfite-based single-cell methylomes report 5mC+5hmC combined** — a 22% confound in hippocampal neurons ([[10-Summaries/chen-2025-sctaps-sccaps-plus]]).

## Related

- [[30-Concepts/bisulfite-sequencing]] · [[40-Topics/dna-methylation]] · [[30-Concepts/taps]]
- [[10-Summaries/kremer-2024-methscan]] · [[10-Summaries/chen-2025-sctaps-sccaps-plus]] · [[10-Summaries/jones-2012-dna-methylation-functions]]
