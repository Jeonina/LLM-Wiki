---
type: summary
title: "Yeung 2023 — scChIX-seq: dynamic relationships between histone modifications in single cells"
aliases: ["Yeung 2023 scChIX-seq", "scChIX-seq"]
tags: [scChIX-seq, multiplexed-histone-marks, H3K27me3, H3K9me3, H3K4me1, H3K36me3, deconvolution, van-Oudenaarden-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["scChIX-seq infers dynamic relationships between histone modifications in single cells.md"]
---

Yeung, Florescu, Zeller et al. (van Oudenaarden lab; Hubrecht Institute) developed **scChIX-seq** (single-cell chromatin immunocleavage and unmixing sequencing) to profile TWO histone modifications per cell. Workflow: incubate cells with each antibody separately (single-incubated, training data) and with both antibodies together (double-incubated). LDA learns cell-type-specific genomic distributions; statistical model deconvolves multiplexed cut fragments back to one of the two marks. Validated on H3K27me3/H3K9me3 (mutually exclusive), H3K4me1/H3K36me3 (correlated), and applied to mouse organogenesis and macrophage differentiation for chromatin velocity.

## Why this matters

The first scalable method for joint histone-mark profiling in single cells. Anchors §3.4 (chromatin state — multi-mark). Critical for understanding bivalency, mark-switching dynamics, and chromatin velocity.

## Related

- [[10-Summaries/janssens-2023-scicut-tag]]
- [[10-Summaries/ku-2019-scchic-seq]]
- [[10-Summaries/dey-2015-dr-seq]]
