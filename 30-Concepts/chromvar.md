---
type: concept
title: chromVAR
aliases: [chromatin variability]
tags: [scATAC-seq, TF-motif, Greenleaf-lab, software]
created: 2026-05-12
updated: 2026-10-07
---

# chromVAR

> An R package that aggregates scATAC-seq signal across peaks sharing a TF motif, computes a bias-corrected deviation score per cell (controlling for GC content and mean accessibility), and outputs a robust TF-motif × cell matrix for clustering and de novo motif discovery.

## Definition

For each motif: count fragments in motif-containing peaks per cell, subtract expected based on cell average, then subtract mean deviation from GC- and accessibility-matched background peak sets, divide by background SD. Result is a z-score per motif per cell. Robust at ~10,000 fragments/cell (typical scATAC yield).

## Why it matters

- Solves the per-locus sparsity problem of scATAC-seq by aggregating across many peaks per motif.
- Identifies master regulators of hematopoiesis (HOXA9, SPI1, GATA1, TBX21) from sparse single-cell data.
- Standard downstream tool used with cisTopic, SnapATAC, EpiScanpy, scABC.

## Examples

- AML patient stratification: leukemic stem cells are most similar to LMPPs, while AML blasts cluster with monocytes; SPI1 + CEBPA motifs distinguish stem-like vs differentiated AML ([[10-Summaries/schep-2017-chromvar]]).

## Added 2026-10-07

BROCKMAN, developed concurrently, argues chromVAR's dependence on predefined peaks and ungapped 7-mers may reduce sensitivity to rare cell types and interpretability, and represents cells by gapped k-mers (k = 1–8) around all Tn5 insertions instead ([[10-Summaries/de-boer-2018-brockman]]). In PeakVI's benchmark chromVAR mixed batches best but separated sorted cell types worse than PeakVI, cisTopic and LSA ([[10-Summaries/ashuach-2022-peakvi]]).

chromVAR with JASPAR motifs is used for TF enrichment on cell-type and condition-specific peaks in archival FFPE scATAC data ([[10-Summaries/yadav-2025-scffpe-atac]]). In a bootstrap benchmark, CellSpace's embedding-based motif scores matched chromVAR on correlation with TF expression (17/19 neurodevelopmental TFs positive) while also yielding a batch-mitigated embedding, which chromVAR-based embeddings did not ([[10-Summaries/tayyebi-2024-cellspace]]).


## Related

- [[30-Concepts/scatac-seq]] · [[30-Concepts/transcription-factor-motif]] · [[30-Concepts/de-novo-motif-discovery]] · [[40-Topics/single-cell-atac-seq]] · [[20-Entities/william-greenleaf]]
