---
type: concept
title: SHARE-seq
aliases: [SHARE-seq, simultaneous high-throughput ATAC and RNA expression]
tags: [joint-assay, single-cell-multiomics, split-pool, scATAC-seq, scRNA-seq, method]
created: 2026-05-12
updated: 2026-10-12
---

# SHARE-seq

> Split-pool-based joint assay for chromatin accessibility and transcription in tens of thousands of single cells; built from SPLiT-seq / Paired-seq logic, it scales by adding barcoding rounds rather than wells ([[10-Summaries/ma-2020-share-seq|Ma 2020]]).

> [!abstract] 한눈에
> SHARE-seq는 같은 세포에서 Tn5로 열린 chromatin을 표지하고 mRNA를 역전사한 뒤 split-pool barcoding으로 둘을 묶는 scATAC + scRNA joint assay다. DORC의 accessibility가 유전자 발현보다 먼저 열린다는 "chromatin potential" 개념을 제시했지만, 이는 pseudotime 위의 상관관계다 ([[10-Summaries/ma-2020-share-seq|Ma 2020]]).

## Definition

Ma et al. 2020 (*Cell* 183, 1103) developed SHARE-seq as a high-throughput alternative to [[sci-car|sci-CAR]] ([[10-Summaries/ma-2020-share-seq|Ma 2020]]). Fixed, permeabilized cells undergo Tn5 tagmentation (chromatin) and reverse transcription (mRNA) in the same tube, then three rounds of 96-well split-pool barcoding give each cell a unique trio of barcodes from 96³ = 884,736 possible combinations ([[10-Summaries/ma-2020-share-seq|Ma 2020]]). The wiki summary is based on the *Nature Reviews Genetics* perspective, not the primary paper ([[10-Summaries/ma-2020-share-seq|Ma 2020]]).

## Why it matters

- **Throughput**: 34,774 high-quality paired profiles from a single adult mouse skin sample; it scales further by adding split-pool rounds ([[10-Summaries/ma-2020-share-seq|Ma 2020]]).
- **Chromatin potential**: chromatin state at lineage loci predicts a cell's future expression — its "potential" lineage choice ([[10-Summaries/ma-2020-share-seq|Ma 2020]]).
- Compatible with fixed cells, fresh cells, and nuclei ([[10-Summaries/ma-2020-share-seq|Ma 2020]]).

## Variants and refinements

- **SHARE-seq** — accessibility + RNA ([[10-Summaries/ma-2020-share-seq|Ma 2020]]).
- Conceptual analog of [[sci-car|sci-CAR]], but with split-pool barcoding instead of combinatorial-indexing well plates ([[10-Summaries/ma-2020-share-seq|Ma 2020]]).

## Evidence and examples

- **DORCs (Domains of Regulatory Chromatin)** are regions with a high density of peak-to-gene associations, enriched for lineage-specifying genes and overlapping super-enhancers ([[10-Summaries/ma-2020-share-seq|Ma 2020]]).
- In hair-follicle differentiation, accessibility at DORCs **precedes** target gene expression ([[10-Summaries/ma-2020-share-seq|Ma 2020]]).

## Contested points

- Sparsity of the single-cell ATAC arm — the same family of issues as sci-CAR (synthesis).
- Chromatin potential is correlational over pseudotime; causal inference (does opening DORC chromatin *cause* later expression?) requires perturbation (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/sci-car|sci-CAR]] — Combinatorial-indexing co-assay of accessibility and mRNA.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Whether DNA is open or nucleosome-wrapped.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Genome-wide accessibility in individual cells.
> - `concept` [[30-Concepts/tn5-tagmentation|Tn5 tagmentation]] — Simultaneous fragmentation and adapter insertion by Tn5.
> - `concept` [[30-Concepts/combinatorial-indexing|Combinatorial indexing]] — Split-pool barcoding that gives each cell a unique barcode combination.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Methods that measure two or more modalities in the same cell.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/ma-2020-share-seq|Ma 2020]]
