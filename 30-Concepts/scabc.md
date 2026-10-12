---
type: concept
title: scABC
aliases: [single cell Accessibility Based Clustering]
tags: [scATAC-seq, clustering, k-medoids, Wong-lab, software]
created: 2026-05-12
updated: 2026-10-12
---

# scABC

> An R package for unsupervised clustering of scATAC-seq data that weights cells by read coverage, applies weighted k-medoids on rank-transformed peak signals, refines via landmark-Spearman-correlation reassignment, and identifies cluster-specific peaks via empirical-Bayes regression ([[10-Summaries/zamanighomi-2018-scabc|Zamanighomi 2018]]).

> [!abstract] 한눈에
> scABC는 scATAC-seq 세포를 read coverage로 가중한 k-medoids로 1차 clustering한 뒤, landmark 세포와의 Spearman 상관으로 다시 배정하는 R package다 ([[10-Summaries/zamanighomi-2018-scabc|Zamanighomi 2018]]). 966개 세포의 in silico 혼합에서 99.6% 정확도를 보였고, 균질하다고 여겨진 세포 집단 안에서도 이질성을 찾아냈다 ([[10-Summaries/zamanighomi-2018-scabc|Zamanighomi 2018]]).

## Definition

Two-stage clustering: initial weighted k-medoids on ranked peak signals → landmark cells (top-ranked peaks per cluster) → Spearman-correlation reassignment of all cells to nearest landmark. Cluster-specific peaks identified by hypothesis testing.

## Why it matters

- 99.6% accuracy on in silico 6-cell-line mixtures (966 cells) ([[10-Summaries/zamanighomi-2018-scabc|Zamanighomi 2018]]).
- Discovers heterogeneity in nominally homogeneous populations (e.g., RA-treated mouse EBs split into 67 neuroectoderm vs 28 visceral-endoderm cells) ([[10-Summaries/zamanighomi-2018-scabc|Zamanighomi 2018]]).
- Used as comparator for newer scATAC-seq tools.

## Examples

- See [[10-Summaries/zamanighomi-2018-scabc|Zamanighomi 2018]].

## Related

> [!cards]
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Genome-wide chromatin accessibility in single cells via Tn5.
> - `concept` [[30-Concepts/k-medoids|k-medoids]] — Clustering with actual data points as cluster centres.
> - `concept` [[30-Concepts/chromvar|chromVAR]] — Bias-corrected TF-motif deviation scores per cell.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Analysis methods for sparse per-cell accessibility data.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/zamanighomi-2018-scabc|Zamanighomi 2018]]
