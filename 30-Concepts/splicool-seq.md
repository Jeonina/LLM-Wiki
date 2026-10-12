---
type: concept
title: SpliCOOL-seq
aliases: [split-pool ligation-based multi-omics sequencing]
tags: [methylation, accessibility, single-cell, multi-omics, GpC-methylation]
created: 2026-05-12
updated: 2026-10-12
---

# SpliCOOL-seq

> A high-throughput single-cell method that simultaneously profiles whole-genome DNA methylation (WCG) and chromatin accessibility (GCH, via in-situ GpC methylation) using **universal (unindexed) Tn5 tagmentation** followed by split-pool ligation-based combinatorial barcoding ([[10-Summaries/shen-2026-splicool-seq|Shen 2026]]).

> [!abstract] 한눈에
> SpliCOOL-seq는 세포 안에서 GpC methylation으로 열린 chromatin을 표지하고, barcode 없는 universal Tn5와 split-pool ligation barcoding을 써서 한 세포의 CpG methylation과 accessibility를 함께 읽는다. 세포마다 달랐던 Tn5 절단 편차를 없앤 것이 sciMET 계열과의 핵심 차이다 ([[10-Summaries/shen-2026-splicool-seq|Shen 2026]]).

## Definition

Workflow: in-situ M.CviPI GpC methylation labels accessible regions → light SDS nucleosome depletion → universal Tn5 tagmentation (uniform fragmentation across cells, unlike sciMETv3's indexed Tn5) → two-round split-pool barcoding with T4 ligase → bisulfite conversion → sequencing. WCG = endogenous CpG methylation; GCH = exogenous GpC methylation = NDR/accessibility readout ([[10-Summaries/shen-2026-splicool-seq|Shen 2026]]).

## Why it matters

Universal Tn5 removes per-cell fragmentation variability that hampered sciMETv2/v3. Both modalities profiled at higher data quality and throughput than cell-lysate-based scNMT-seq, scNOMe-seq, snmCAT-seq ([[10-Summaries/shen-2026-splicool-seq|Shen 2026]]).

## Examples

- Lung cancer cell lines distinguished by joint WCG + GCH + NDR features ([[10-Summaries/shen-2026-splicool-seq|Shen 2026]]).
- Decitabine vs 5-azacytidine cause **distinct demethylation patterns** in the same cells ([[10-Summaries/shen-2026-splicool-seq|Shen 2026]]).
- Primary LUAD: identifies tumor subclones; biomarkers FAM124B, SFN, OR7E47P linked to survival; accelerated epigenetic aging in tumor subclones ([[10-Summaries/shen-2026-splicool-seq|Shen 2026]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/nome-seq|NOMe-seq]] — M.CviPI GpC methylation as an accessibility readout alongside endogenous CpG methylation.
> - `concept` [[30-Concepts/combinatorial-indexing|Combinatorial indexing]] — Split-pool barcoding that gives each cell a unique barcode combination.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Whether DNA is open or nucleosome-wrapped.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC biology and the methods that measure it.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Methods that measure two or more modalities in the same cell.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/shen-2026-splicool-seq|Shen 2026]]
