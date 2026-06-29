---
type: concept
title: sci-CAR
aliases: [sci-CAR, single-cell combinatorial-indexing CAR]
tags: [joint-assay, single-cell-multiomics, combinatorial-indexing, scATAC-seq, scRNA-seq, method]
created: 2026-05-12
updated: 2026-05-12
---

# sci-CAR

> Single-cell combinatorial-indexing co-assay that jointly profiles chromatin accessibility and mRNA in thousands of single cells per experiment, by paired-well barcoding of sci-ATAC-seq and sci-RNA-seq libraries from the same nuclei.

## Definition

Cao et al. 2018 ([[10-Summaries/cao-2018-sci-car]]) merged sci-ATAC-seq and sci-RNA-seq into a single workflow. Nuclei pass through two rounds of barcoding (first in situ via RT primer + Tn5 transposase, second in liquid-phase amplification); the resulting two-barcode pair uniquely identifies the cell of origin. mRNA and ATAC reads from the same nucleus share the same barcode pair, so each cell yields paired (transcriptome, chromatin accessibility) profiles.

## Why it matters

sci-CAR is the **combinatorial-indexing template** that the field then followed for scaling joint assays. Two demonstrated applications in the original paper:

- 4,825 jointly profiled A549 cells across a 0/1/3-hr dexamethasone time course — captured glucocorticoid-receptor activation kinetics at both layers.
- 11,296 jointly profiled adult mouse kidney nuclei across 14 cell types — distal cis-regulatory linking by covariance gave a 4× improvement over promoter-only prediction of expression.

The paper explicitly framed sci-CAR as a template for future DNA-anchored joint coassays ("methylation + transcripts, chromosome conformation + transcripts, or DNA sequence + transcripts"). 10x Genomics Multiome is essentially the commercial sci-CAR.

## Variants and refinements

- **sci-CAR** ([[10-Summaries/cao-2018-sci-car]]) — accessibility + RNA.
- [[10-Summaries/clark-2018-scnmt-seq|scNMT-seq]] — adds methylation, lower throughput.
- [[10-Summaries/ma-2020-share-seq|SHARE-seq]] — split-pool scaling alternative.
- 10x Genomics Multiome — commercial sci-CAR-style coassay.

## Contested points

- ATAC arm has ~10× lower complexity than RNA-only sci-ATAC-seq, due to half-lysate use and buffer modifications.
- Distal-element linking is correlative, not causal.

## Related

- [[combinatorial-indexing]]
- [[scatac-seq]]
- [[tn5-tagmentation]]
- [[30-Concepts/single-cell-multiomics]]
- [[20-Entities/vijay-ramani]]
- [[40-Topics/single-cell-multiomics]]
