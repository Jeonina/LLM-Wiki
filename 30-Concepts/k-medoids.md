---
type: concept
title: k-medoids clustering
aliases: [PAM, Partitioning Around Medoids]
tags: [clustering, machine-learning]
created: 2026-05-12
updated: 2026-10-12
---

# k-medoids clustering

> A clustering algorithm similar to k-means but using actual data points as cluster centers ("medoids") rather than computed means. Robust to outliers and well-suited for sparse, ranked, or non-Euclidean data.

> [!abstract] 한눈에
> k-medoids는 평균 대신 실제 데이터 점을 cluster 중심으로 쓰는 clustering 방법이라 outlier에 덜 흔들린다. scABC는 read 수로 세포에 가중치를 준 k-medoids로 scATAC-seq 세포를 비지도 clustering한다 ([[10-Summaries/zamanighomi-2018-scabc|scABC]]).

## Definition

Partitions n data points into k clusters by minimizing total distance to k medoid points. Each iteration: assign points to nearest medoid → for each cluster, find the point minimizing within-cluster distance → repeat until convergence.

## Why it matters

- More robust than k-means for noisy single-cell data.
- Used in [[30-Concepts/scabc]] for unsupervised scATAC-seq clustering, with sample-depth-based cell weighting.

## Related

> [!cards]
> - `concept` [[30-Concepts/scabc|scABC]] — Coverage-weighted k-medoids clustering for scATAC-seq.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Chromatin accessibility measured one cell at a time.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/zamanighomi-2018-scabc|Zamanighomi 2018]]
