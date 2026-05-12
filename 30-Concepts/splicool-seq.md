---
type: concept
title: SpliCOOL-seq
aliases: [split-pool ligation-based multi-omics sequencing]
tags: [methylation, accessibility, single-cell, multi-omics, GpC-methylation]
created: 2026-05-12
updated: 2026-05-12
---

# SpliCOOL-seq

> A high-throughput single-cell method that simultaneously profiles whole-genome DNA methylation (WCG) and chromatin accessibility (GCH, via in-situ GpC methylation) using **universal (unindexed) Tn5 tagmentation** followed by split-pool ligation-based combinatorial barcoding.

## Definition

Workflow: in-situ M.CviPI GpC methylation labels accessible regions → light SDS nucleosome depletion → universal Tn5 tagmentation (uniform fragmentation across cells, unlike sciMETv3's indexed Tn5) → two-round split-pool barcoding with T4 ligase → bisulfite conversion → sequencing. WCG = endogenous CpG methylation; GCH = exogenous GpC methylation = NDR/accessibility readout.

## Why it matters

Universal Tn5 removes per-cell fragmentation variability that hampered sciMETv2/v3. Both modalities profiled at higher data quality and throughput than cell-lysate-based scNMT-seq, scNOMe-seq, snmCAT-seq.

## Examples

- Lung cancer cell lines distinguished by joint WCG + GCH + NDR features.
- Decitabine vs 5-azacytidine cause **distinct demethylation patterns** in the same cells.
- Primary LUAD: identifies tumor subclones; biomarkers FAM124B, SFN, OR7E47P linked to survival; accelerated epigenetic aging in tumor subclones ([[10-Summaries/high-throughput-single-cell-dna-methylation-and-chromatin-accessibility-co-profiling-with-splicool-seq]]).

## Related

- [[30-Concepts/nome-seq]] · [[30-Concepts/combinatorial-indexing]] · [[30-Concepts/dna-methylation]] · [[30-Concepts/chromatin-accessibility]] · [[40-Topics/single-cell-multiomics]]
