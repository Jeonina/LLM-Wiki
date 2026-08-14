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

## Added 2026-08-13

Protocol source ingested 2026-08-13: [[10-Summaries/clark-2017-scbs-seq-protocol]].

**PBAT is the enabling inversion.** In conventional bisulfite sequencing, adaptor-tagged molecules are bisulfite-treated and most are destroyed; PBAT uses bisulfite to do both the conversion and the fragmentation, tagging afterwards ([[10-Summaries/clark-2017-scbs-seq-protocol]]). Protocol topology, not chemistry, is what set the input floor. (synthesis)

**Five rounds of random priming with intermediate heat denaturation** is the single-cell modification — five chances to capture each locus, and multiple copies per fragment so purification does not collapse complexity ([[10-Summaries/clark-2017-scbs-seq-protocol]]). Random hexamers are recommended over tetramers (yield) or nonamers (trimming burden) ([[10-Summaries/clark-2017-scbs-seq-protocol]]).

**Coverage: up to ~50% of CpGs per single mouse cell** — the highest per-cell coverage of any single-cell methylation method in the corpus, and the opposite end of the design axis from [[10-Summaries/mulqueen-2018-sci-met|sci-MET]] (~1%) and [[10-Summaries/zhang-2023-drop-bs|Drop-BS]] ([[10-Summaries/clark-2017-scbs-seq-protocol]]). Whole methylomes of rare cell types are reconstructed by merging <20 cells ([[10-Summaries/clark-2017-scbs-seq-protocol]]).

The protocol's own analysis advice — sliding-window averaging for cross-cell comparison — is the part that was superseded: tile-averaging dilutes signal, and VMR-based discovery replaces it ([[10-Summaries/kremer-2024-methscan]]). (synthesis)
