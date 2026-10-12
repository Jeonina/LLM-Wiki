---
type: concept
title: "Latent semantic indexing (TF-IDF + SVD)"
aliases: []
tags: []
created: 2026-10-07
updated: 2026-10-12
sources: ["[[10-Summaries/luo-2024-scatac-benchmark]]", "[[10-Summaries/raimundo-2023-schptm-benchmark]]", "[[10-Summaries/wu-2026-sccut-tag-review]]"]
---

# Latent semantic indexing (TF-IDF + SVD)

> Latent semantic indexing (LSI) is the two-step embedding of TF-IDF normalization followed by SVD/PCA, borrowed from information retrieval and now the default dimensionality reduction for sparse single-cell chromatin data ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).

> [!abstract] 한눈에
> LSI는 TF-IDF 정규화 뒤 SVD/PCA를 적용하는 2단계 embedding으로, 희소한 single-cell chromatin 데이터의 기본 차원 축소 방법이다 ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]). histone PTM 데이터에서는 TF-IDF 기반 embedding이 가장 좋았지만 scATAC-seq에서는 SnapATAC 계열이 LSI보다 나아, 장점은 modality에 따라 다르다 ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]; [[10-Summaries/luo-2024-scatac-benchmark|Luo 2024]]).

## In practice

- Implemented in Signac and ArchR (iterative LSI); the first component is usually dropped because it correlates with sequencing depth, and dimensions 2–30 are kept ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).
- Variants differ in post-processing: ChromSCape_LSI weights components by eigenvalue, while Signac whitens and uses 50 dimensions by default, which the benchmark links to Signac's weaker results on the low-coverage PBMC data ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).
- TF-IDF can also be paired with NMF (scOpen-style TFIDF-NMF) ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).

## Evidence

- For single-cell histone PTM data, the three best embeddings all use TF-IDF, and the gap between NMF and TFIDF-NMF isolates the effect of the transform ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).
- For scATAC-seq, an independent benchmark found SnapATAC/SnapATAC2 and feature aggregation outperform LSI-based methods ([[10-Summaries/luo-2024-scatac-benchmark|Luo 2024]]), so the advantage is modality-dependent (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/dimensionality-reduction|Dimensionality reduction]] — Projecting single-cell measurements into a few coordinates; LSI is one such embedding.
> - `concept` [[30-Concepts/snapatac|SnapATAC]] — Peak-free scATAC-seq pipeline that outperformed LSI-based methods in one benchmark.
> - `concept` [[30-Concepts/cistopic|cisTopic]] — LDA topic modelling, an alternative embedding for scATAC-seq.
> - `concept` [[30-Concepts/scopen|scOpen]] — NMF on a TF-IDF-transformed matrix, the TFIDF-NMF variant.
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — Antibody-directed chromatin profiling whose single-cell data LSI often embeds.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Single-cell chromatin accessibility, the main LSI use case.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/luo-2024-scatac-benchmark|Luo 2024]]
> - [[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]
> - [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]
