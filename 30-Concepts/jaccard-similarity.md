---
type: concept
title: Jaccard similarity
aliases: [Jaccard index]
tags: [similarity-metric, set-theory, clustering]
created: 2026-05-12
updated: 2026-10-12
---

# Jaccard similarity

> A set-similarity metric: |A ∩ B| / |A ∪ B|. Ranges 0 (disjoint) to 1 (identical). Used in [[30-Concepts/snapatac]] to measure similarity between pairs of single cells based on overlap of accessible 5-kb genomic bins.

> [!abstract] 한눈에
> Jaccard similarity는 두 집합의 교집합 크기를 합집합 크기로 나눈 값으로, scATAC-seq에서는 세포 사이에 열린 bin이 얼마나 겹치는지를 잰다. scCASE는 이 값으로 세포 간 유사도 행렬을 초기화하고, SegmentNT는 genome segmentation 평가 지표로 쓴다 ([[10-Summaries/tang-2024-sccase|scCASE]]; [[10-Summaries/dealmeida-2025-segmentnt|SegmentNT]]).

## Why it matters

- Naturally handles binary presence/absence data (a bin is open or not).
- Penalizes cells with too many or too few open bins, requiring depth normalization (which SnapATAC handles via regression).

## Examples

- scCASE initialises its learned cell-to-cell similarity matrix from the cell–cell Jaccard similarity of the scCAS matrix ([[10-Summaries/tang-2024-sccase|scCASE]]). The authors report that random initialisation of Z still converges but enhances the data less well ([[10-Summaries/tang-2024-sccase|scCASE]]).
- SegmentNT reports per-nucleotide Jaccard similarity alongside MCC, auPRC and F1 when scoring multilabel genome segmentation ([[10-Summaries/dealmeida-2025-segmentnt|SegmentNT]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/snapatac|SnapATAC]] — Peak-free scATAC-seq pipeline built on cell–cell Jaccard similarity over 5-kb bins.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Chromatin accessibility measured one cell at a time.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/dealmeida-2025-segmentnt|SegmentNT 2025]]
> - [[10-Summaries/tang-2024-sccase|Tang 2024]]
