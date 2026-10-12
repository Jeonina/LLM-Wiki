---
type: concept
title: sci-CAR
aliases: [sci-CAR, single-cell combinatorial-indexing CAR]
tags: [joint-assay, single-cell-multiomics, combinatorial-indexing, scATAC-seq, scRNA-seq, method]
created: 2026-05-12
updated: 2026-10-12
---

# sci-CAR

> Single-cell combinatorial-indexing co-assay that jointly profiles chromatin accessibility and mRNA in thousands of single cells per experiment, by paired-well barcoding of sci-ATAC-seq and sci-RNA-seq libraries from the same nuclei ([[10-Summaries/cao-2018-sci-car|Cao 2018]]).

> [!abstract] 한눈에
> sci-CAR는 sci-ATAC-seq와 sci-RNA-seq를 하나의 combinatorial indexing 흐름으로 합쳐 같은 nucleus에서 chromatin accessibility와 mRNA를 함께 읽는 방법이다 ([[10-Summaries/cao-2018-sci-car|Cao 2018]]). 이후 joint assay를 대규모로 키우는 표준 설계가 되었지만, ATAC 쪽 library complexity가 낮다는 한계가 있다 ([[10-Summaries/cao-2018-sci-car|Cao 2018]]).

## Definition

Cao et al. 2018 merged sci-ATAC-seq and sci-RNA-seq into a single workflow ([[10-Summaries/cao-2018-sci-car|Cao 2018]]). Nuclei pass through two rounds of barcoding (first in situ via RT primer + Tn5 transposase, second in liquid-phase amplification); the resulting two-barcode pair uniquely identifies the cell of origin ([[10-Summaries/cao-2018-sci-car|Cao 2018]]). mRNA and ATAC reads from the same nucleus share the same barcode pair, so each cell yields paired (transcriptome, chromatin accessibility) profiles ([[10-Summaries/cao-2018-sci-car|Cao 2018]]).

## Why it matters

- sci-CAR is the **combinatorial-indexing template** that the field then followed for scaling joint assays ([[10-Summaries/cao-2018-sci-car|Cao 2018]]).
- The paper explicitly framed sci-CAR as a template for future DNA-anchored joint coassays ("methylation + transcripts, chromosome conformation + transcripts, or DNA sequence + transcripts") ([[10-Summaries/cao-2018-sci-car|Cao 2018]]).

## Variants and refinements

| Assay | Layers | Relation to sci-CAR | Source |
|---|---|---|---|
| **sci-CAR** | Accessibility + RNA | Original combinatorial-indexing coassay | ([[10-Summaries/cao-2018-sci-car\|Cao 2018]]) |
| [[10-Summaries/clark-2018-scnmt-seq\|scNMT-seq]] | Adds methylation | Three modalities, lower throughput | ([[10-Summaries/clark-2018-scnmt-seq\|scNMT-seq]]) |
| [[10-Summaries/ma-2020-share-seq\|SHARE-seq]] | Accessibility + RNA | Split-pool scaling alternative | ([[10-Summaries/ma-2020-share-seq\|SHARE-seq]]) |
| 10x Genomics Multiome | Accessibility + RNA | Commercial sci-CAR-style coassay — essentially the commercial sci-CAR | ([[10-Summaries/cao-2018-sci-car\|Cao 2018]]) |

## Evidence and examples

- 4,825 jointly profiled A549 cells across a 0/1/3-hr dexamethasone time course captured glucocorticoid-receptor activation kinetics at both layers ([[10-Summaries/cao-2018-sci-car|Cao 2018]]).
- 11,296 jointly profiled adult mouse kidney nuclei across 14 cell types ([[10-Summaries/cao-2018-sci-car|Cao 2018]]).
- In kidney, distal cis-regulatory linking by covariance gave a 4× improvement over promoter-only prediction of expression ([[10-Summaries/cao-2018-sci-car|Cao 2018]]).

## Contested points

- The ATAC arm has ~10× lower complexity than RNA-only sci-ATAC-seq, due to half-lysate use and buffer modifications ([[10-Summaries/cao-2018-sci-car|Cao 2018]]).
- Distal-element linking is correlative, not causal ([[10-Summaries/cao-2018-sci-car|Cao 2018]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/combinatorial-indexing|Combinatorial indexing]] — Split-pool barcoding that labels cells without physical isolation.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Single-cell chromatin accessibility by Tn5 tagmentation.
> - `concept` [[30-Concepts/tn5-tagmentation|Tn5 tagmentation]] — Transposase insertion that fragments and tags DNA in one step.
> - `entity` [[20-Entities/vijay-ramani|Vijay Ramani]] — Co-author of sci-CAR.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Joint measurement of several layers in one cell.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/cao-2018-sci-car|Cao 2018]]
> - [[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]
> - [[10-Summaries/ma-2020-share-seq|Ma 2020]]
