---
type: concept
title: scATAC-seq
aliases: [single-cell ATAC-seq, single-cell ATAC]
tags: [chromatin-accessibility, single-cell, ATAC, Tn5]
created: 2026-05-12
updated: 2026-05-21
---

# scATAC-seq

> Single-cell Assay for Transposase-Accessible Chromatin using sequencing. Profiles genome-wide chromatin accessibility in individual cells using hyperactive Tn5 transposase to insert sequencing adapters preferentially at open chromatin (regulatory elements) ([[10-Summaries/buenrostro-2015-nature]]; [[10-Summaries/cusanovich-2015-sciatac]]).

## Definition

Workflow: lyse cells / isolate nuclei → Tn5 tagmentation → barcoded library prep → sequencing ([[10-Summaries/buenrostro-2015-nature]]). Each cell yields ~1k–20k unique accessibility fragments ([[10-Summaries/buenrostro-2015-nature]]). The diploid genome inherently caps per-locus reads at 2, making scATAC-seq matrices extremely sparse — a structural property that drives downstream tool design ([[10-Summaries/derop-2024-natbiotech]]).

## Platforms

Two parallel cell-barcoding strategies emerged in 2015 and define the family today:

- **Microfluidic plate (Fluidigm C1)** — Buenrostro 2015 ([[10-Summaries/buenrostro-2015-nature]]); ~100 cells per run, deeper per-cell coverage.
- **Combinatorial indexing (sci-ATAC-seq)** — Cusanovich 2015 ([[10-Summaries/cusanovich-2015-sciatac]]); thousands of cells per run, no microfluidics, lower per-cell depth.

Subsequent platforms split along the same axis:

- **Nanowell / nanoliter Tn5** — µATAC-seq ([[10-Summaries/mezger-2018-uatac]]) increases throughput while preserving per-cell coverage.
- **Droplet** — 10x Genomics Chromium scATAC (and 10x Multiome, which co-captures RNA in the same droplet); the dominant commercial platform today.
- **Combinatorial-droplet hybrids** — benchmarked by De Rop 2024's PUMATAC pipeline across 10x, sci-ATAC, dscATAC, ddSEQ-ATAC ([[10-Summaries/derop-2024-natbiotech]]).

## Why it matters

- Maps cell-type-specific regulatory landscapes from heterogeneous tissue ([[10-Summaries/cusanovich-2015-sciatac]]).
- Provides the per-cell substrate for [[40-Topics/single-cell-multiomics]] when paired with RNA (10x Multiome, sci-CAR — [[10-Summaries/cao-2018-sci-car]]) or with genotype (GoT-ChA — [[10-Summaries/izzo-2024-got-cha]]).
- Foundation for the [[40-Topics/single-cell-atac-seq]] tooling stack: chromVAR ([[10-Summaries/schep-2017-chromvar]]), cisTopic ([[10-Summaries/bravo-2019-cistopic]]), SnapATAC2 ([[10-Summaries/zhang-2024-snapatac2]]), ArchR ([[10-Summaries/granja-2021-archr]]), EpiScanpy ([[10-Summaries/danese-2021-episcanpy]]), scABC ([[10-Summaries/zamanighomi-2018-scabc]]).

## Quality metrics

- **TSS enrichment** — fold-enrichment of reads at transcription start sites; primary per-cell QC signal ([[10-Summaries/derop-2024-natbiotech]]).
- **Unique fragments per cell** — typical thresholds 1,000–5,000 depending on platform ([[10-Summaries/derop-2024-natbiotech]]).
- **Fraction of reads in peaks (FRiP)** — proxy for signal-to-noise; varies systematically across platforms ([[10-Summaries/derop-2024-natbiotech]]).
- **Doublet rate** — droplet platforms inherit doublet artifacts from 10x scRNA chemistry.

## Contested points

- **Platform comparability** — PUMATAC benchmarking ([[10-Summaries/derop-2024-natbiotech]]) shows non-trivial systematic differences in peak calls and cell-type assignment across 10x / sci-ATAC / dscATAC / ddSEQ-ATAC; cross-platform meta-analysis requires platform-aware correction.
- **Peak vs bin matrix** — fixed-genomic-bin matrices (SnapATAC2 — [[10-Summaries/zhang-2024-snapatac2]]) avoid peak-calling bias but inflate feature count; peak-based matrices (ArchR — [[10-Summaries/granja-2021-archr]]) are more interpretable but sensitive to peak-call parameters.
- **Sparsity vs information content** — only ~5–15% of accessible peaks fire per cell; binarization vs continuous count modeling remains a live methods debate ([[10-Summaries/yuan-2022-scbasset]]).

## Variants and refinements

- **scATAC-seq (Tn5 only)** — Buenrostro 2015 ([[10-Summaries/buenrostro-2015-nature]]) and the family above.
- **scCUT&Tag / nano-CUT&Tag** — Tn5 fused to protein-A-pAG-MNase variants for histone-mark / TF profiling ([[10-Summaries/bartosovic-2021-sccut-tag]]; [[10-Summaries/bartosovic-2022-nano-cut-tag]]).
- **Multimodal** — sci-CAR (RNA + ATAC, [[10-Summaries/cao-2018-sci-car]]), SHARE-seq (RNA + ATAC, [[10-Summaries/ma-2020-cell]]), scNMT-seq (RNA + methylation + accessibility, [[10-Summaries/clark-2018-scnmt-seq]]), GoT-ChA (genotype + ATAC, [[10-Summaries/izzo-2024-got-cha]]), DOGMA-seq (RNA + ATAC + protein).

## Examples

- Cell-type-specific accessibility in heterogeneous hematopoietic populations ([[10-Summaries/buenrostro-2015-nature]]; [[10-Summaries/cusanovich-2015-sciatac]]).
- JAK2-V617F cell-intrinsic pro-inflammatory chromatin priming in HSCs, visible only by linking genotype to accessibility in the same cell ([[10-Summaries/izzo-2024-got-cha]]).
- Systematic benchmark of 4 scATAC platforms across human PBMC / cell lines via the PUMATAC pipeline ([[10-Summaries/derop-2024-natbiotech]]).
- Computational benchmark of analysis methods across multiple datasets ([[10-Summaries/luo-2024-scatac-benchmark]]).

## Related

- [[30-Concepts/atac-seq]] · [[30-Concepts/tn5-tagmentation]] · [[30-Concepts/chromatin-accessibility]]
- [[30-Concepts/chromvar]] · [[30-Concepts/cistopic]] · [[30-Concepts/snapatac]] · [[30-Concepts/episcanpy]] · [[30-Concepts/scabc]]
- [[30-Concepts/cut-and-tag]] · [[30-Concepts/scchic-seq]] · [[30-Concepts/single-cell-multiomics]]
- [[40-Topics/single-cell-atac-seq]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/chromatin-architecture]]
