---
type: concept
title: scTEM-seq
aliases: [single-cell transposable element methylation sequencing]
tags: [methylation, single-cell, transposable-elements, bisulfite, low-cost]
created: 2026-05-12
updated: 2026-10-12
---

# scTEM-seq

> A low-cost single-cell DNA-methylation method that targets high-copy SINE Alu transposable elements via bisulfite + amplicon PCR. Estimates global methylation per cell at ~0.1% the cost of genome-wide scBS-seq (~20k vs ~20M reads per cell).

> [!abstract] 한눈에
> scTEM-seq는 SINE Alu 반복서열을 bisulfite amplicon으로 읽어 세포마다 전체 DNA methylation 수준을 싸게 추정하는 방법이다 ([[10-Summaries/hunt-2022-sctem-seq|Hunt 2022]]). locus별 해상도를 포기하는 대신 처리량을 크게 늘려 AML 약물 반응 같은 연구를 단일세포 규모로 할 수 있게 한다 ([[10-Summaries/hunt-2022-sctem-seq|Hunt 2022]]).

## Definition

Amplicon bisulfite sequencing on SINE Alu (28 indexed primers, up to 18,432 cells per pool) gives global DNA methylation estimates that correlate with whole-genome averages at R²=0.91 in matched data. Combined with G&T-seq, methylation and transcriptome are profiled from the same cell.

## Why it matters

Most experiments need a global methylation readout, not per-locus calls. scTEM-seq trades per-locus resolution for 1000× throughput, enabling AML drug-response studies (e.g., decitabine treatment) at single-cell scale.

## Examples

- KG1a / HL60 AML cells ± decitabine: heterogeneous demethylation; subset of cells coordinately upregulates LINE-1/SINE Alu/ERV families (viral mimicry response) ([[10-Summaries/hunt-2022-sctem-seq]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/bisulfite-sequencing|Bisulfite sequencing]] — Conversion chemistry that reads 5mC as C and unmethylated C as T.
> - `concept` [[30-Concepts/transposable-elements|Transposable elements]] — High-copy repeats such as SINE Alu that scTEM-seq targets.
> - `concept` [[30-Concepts/viral-mimicry|Viral mimicry]] — Interferon-like response to derepressed repeats after demethylation.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation chemistry, assays and analysis.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/hunt-2022-sctem-seq|Hunt 2022]]
