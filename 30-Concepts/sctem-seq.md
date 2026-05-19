---
type: concept
title: scTEM-seq
aliases: [single-cell transposable element methylation sequencing]
tags: [methylation, single-cell, transposable-elements, bisulfite, low-cost]
created: 2026-05-12
updated: 2026-05-12
---

# scTEM-seq

> A low-cost single-cell DNA-methylation method that targets high-copy SINE Alu transposable elements via bisulfite + amplicon PCR. Estimates global methylation per cell at ~0.1% the cost of genome-wide scBS-seq (~20k vs ~20M reads per cell).

## Definition

Amplicon bisulfite sequencing on SINE Alu (28 indexed primers, up to 18,432 cells per pool) gives global DNA methylation estimates that correlate with whole-genome averages at R²=0.91 in matched data. Combined with G&T-seq, methylation and transcriptome are profiled from the same cell.

## Why it matters

Most experiments need a global methylation readout, not per-locus calls. scTEM-seq trades per-locus resolution for 1000× throughput, enabling AML drug-response studies (e.g., decitabine treatment) at single-cell scale.

## Examples

- KG1a / HL60 AML cells ± decitabine: heterogeneous demethylation; subset of cells coordinately upregulates LINE-1/SINE Alu/ERV families (viral mimicry response) ([[10-Summaries/hunt-2022-sctem-seq]]).

## Related

- [[30-Concepts/dna-methylation]] · [[30-Concepts/bisulfite-sequencing]] · [[30-Concepts/transposable-elements]] · [[30-Concepts/viral-mimicry]] · [[40-Topics/dna-methylation]]
