---
type: concept
title: chromVAR
aliases: [chromatin variability]
tags: [scATAC-seq, TF-motif, Greenleaf-lab, software]
created: 2026-05-12
updated: 2026-05-12
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

- AML patient stratification: leukemic stem cells cluster between LMPPs and monocytes; SPI1 + CEBPA motifs distinguish stem-like vs differentiated AML ([[10-Summaries/chromvar-inferring-transcription-factor-associated-accessibility-from-single-cell-epigenomic-data]]).

## Related

- [[30-Concepts/scatac-seq]] · [[30-Concepts/transcription-factor-motif]] · [[30-Concepts/de-novo-motif-discovery]] · [[40-Topics/single-cell-atac-seq]] · [[20-Entities/william-greenleaf]]
