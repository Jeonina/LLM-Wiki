---
type: concept
title: Nyström method
aliases: [Nyström approximation]
tags: [linear-algebra, dimensionality-reduction, scalability]
created: 2026-05-12
updated: 2026-10-12
---

# Nyström method

> A low-rank matrix-approximation technique that computes the spectral decomposition of a large kernel matrix using only a sampled subset (landmark) of rows/columns. Reduces complexity from O(n²) to O(nm) where m is the number of landmarks.

> [!abstract] 한눈에
> Nyström method는 일부 landmark 행·열만으로 큰 kernel 행렬의 저차원 분해를 근사해 계산량을 O(n²)에서 O(nm)으로 줄이는 기법이다. SnapATAC는 여러 번 sampling한 결과를 합치는 ensemble Nyström으로 scATAC-seq 차원 축소를 백만 세포 규모까지 확장했다 ([[10-Summaries/fang-2021-snapatac|SnapATAC]]).

## Definition

Given a similarity matrix K (here, cell × cell Jaccard), select m landmarks → compute eigenvector decomposition on the m × m sub-matrix → project all n cells onto that low-dimensional embedding ([[10-Summaries/fang-2021-snapatac|SnapATAC]]).

## Why it matters

Enables scATAC-seq dimensionality reduction at the million-cell scale. SnapATAC uses ensemble Nyström (multiple sampling rounds combined via consensus) to improve reproducibility ([[10-Summaries/fang-2021-snapatac|SnapATAC]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/snapatac|SnapATAC]] — Peak-free scATAC-seq pipeline that uses ensemble Nyström embedding.
> - `concept` [[30-Concepts/jaccard-similarity|Jaccard similarity]] — The cell × cell similarity that SnapATAC decomposes.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Single-cell chromatin accessibility assays and analysis.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/fang-2021-snapatac|Fang 2021]]
