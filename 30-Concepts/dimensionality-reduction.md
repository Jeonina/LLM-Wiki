---
type: concept
title: Dimensionality Reduction
aliases: [embedding, PCA, UMAP, t-SNE, latent space]
tags: [embedding, PCA, UMAP, visualization, manifold-learning]
created: 2026-08-10
updated: 2026-10-12
---

# Dimensionality Reduction

> Projecting high-dimensional single-cell measurements into a few coordinates for clustering, visualization and downstream modelling ([[10-Summaries/korsunsky-2019-harmony|Harmony]]; [[10-Summaries/mcinnes-2018-umap|UMAP]]). The step where most analytical decisions become invisible (synthesis).

> [!abstract] 한눈에
> 차원 축소는 고차원 single-cell 측정값을 몇 개의 좌표로 투영해 clustering, 시각화, 후속 모델링에 쓰는 단계다 ([[10-Summaries/korsunsky-2019-harmony|Harmony]]). 어떤 방법이 나은지는 modality마다 달라서, histone PTM 데이터에서는 TF-IDF 기반 embedding이, scATAC-seq에서는 SnapATAC 계열이 앞선다 ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]; [[10-Summaries/luo-2024-scatac-benchmark|Luo 2024]]).

## Definition

Dimensionality reduction projects high-dimensional single-cell measurements into a few coordinates. PCA supplies the working embedding that batch correction and clustering operate on ([[10-Summaries/korsunsky-2019-harmony|Harmony]]), and UMAP supplies the 2D visualization ([[10-Summaries/mcinnes-2018-umap|UMAP]]).

## Why it matters

[[30-Concepts/batch-effect|Batch correction]] and [[30-Concepts/clustering-algorithms|clustering]] operate on the embedding rather than on the raw data ([[10-Summaries/korsunsky-2019-harmony|Harmony]]), so choices made here carry into every later result; what the axes encode, and what a 2D layout preserves, is rarely checked (synthesis).

## Methods

| Method family | Example | Role | Source |
|---|---|---|---|
| PCA | [[10-Summaries/korsunsky-2019-harmony\|Harmony]] | Working embedding that batch correction and clustering operate on | ([[10-Summaries/korsunsky-2019-harmony\|Harmony]]) |
| Manifold layout | [[10-Summaries/mcinnes-2018-umap\|UMAP]] | 2D visualization | ([[10-Summaries/mcinnes-2018-umap\|UMAP]]) |
| Matrix factorization | [[10-Summaries/welch-2019-liger\|LIGER]] | Interpretable shared and dataset-specific factors | ([[10-Summaries/welch-2019-liger\|LIGER]]) |
| Multi-omics factor analysis | [[10-Summaries/argelaguet-2018-mofa\|MOFA]] | Generalisation of PCA to multiple data modalities, with sparse loadings for interpretability and an ARD prior that prunes factors explaining less than a user-set variance threshold (2% in the paper), so the number of factors is learned | ([[10-Summaries/argelaguet-2018-mofa\|MOFA]]) |
| Hypergraph neural network | [[10-Summaries/zhang-2022-higashi\|Higashi]] | Learned representations for sparse contact data | ([[10-Summaries/zhang-2022-higashi\|Higashi]]) |
| TF-IDF / LSI | ChromSCape_LSI, TFIDF-NMF, Signac | Embeddings for single-cell histone PTM data | ([[10-Summaries/raimundo-2023-schptm-benchmark\|Raimundo 2023]]) |

## Evidence and examples

**What the axes mean, when anyone checks**

- In single-cell Hi-C the principal components are interpretable: **PC1 weights lie uniformly parallel to the diagonal**, capturing the contact–distance curve and hence cell-cycle state, while **PC2 weights are region-specific**, capturing compartment strength ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).
- This explains why oocytes and zygotes separate on PC1 while cancer cell lines separate on PC2 ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]), and it corroborates the finding that a single scalar — the *P(s)* scaling coefficient — separates mitotic from interphase cells ([[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]).
- MOFA's key readout is a factor × modality R² matrix showing whether each axis is shared across omics layers or private to one ([[10-Summaries/argelaguet-2018-mofa|MOFA]]).

**Global structure is not preserved by default**

- UMAP's layout depends on initialization, so a random start can place globally distant populations adjacently ([[10-Summaries/wolf-2019-paga|PAGA]]).
- Seeding with a coarse graph abstraction makes the global arrangement meaningful and converges about six times faster, with faithfulness quantified by a geodesic-distance cost function ([[10-Summaries/wolf-2019-paga|PAGA]]).

**Method rankings by modality**

- For single-cell histone PTM data, TF-IDF-based embeddings (ChromSCape_LSI, TFIDF-NMF, Signac) consistently outperform CPM-PCA, cisTopic's LDA and the VAEs PeakVI and SCALE ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).
- In the same benchmark, the matrix-construction (bin size) choice has an even larger effect than the method choice ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).
- In scATAC-seq, SnapATAC/SnapATAC2 and feature aggregation beat LSI ([[10-Summaries/luo-2024-scatac-benchmark|Luo 2024]]).
- In scCUT&Tag practice, LSI dimensions 2–30 are typically kept, and the first component is dropped because it tracks sequencing depth ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).

## Contested points

- **Rankings are modality-specific.** TF-IDF methods lead for histone PTM data ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]) while LSI trails SnapATAC in scATAC-seq ([[10-Summaries/luo-2024-scatac-benchmark|Luo 2024]]), so a ranking from one modality should not be carried to another (synthesis).
- **Depth is not cleanly removable.** Coverage or depth can be the dominant axis of variation, and is not cleanly removable by dropping PC1 because PC1 also carries biology ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]); scCUT&Tag practice nonetheless drops the first LSI component as a depth axis ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).
- **Embedding dimension matters for some methods.** The choice affects some methods more than others; robustness to it is worth reporting ([[10-Summaries/zhang-2022-higashi|Higashi]]).
- **Good mixing can hide merged cell types.** An embedding that mixes datasets well may have merged cell types; the two must be measured separately ([[10-Summaries/korsunsky-2019-harmony|Harmony]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/batch-effect|Batch effect]] — Systematic variation from when, where or how data were generated.
> - `concept` [[30-Concepts/clustering-algorithms|Clustering algorithms]] — Partitioning cells into groups, usually on a k-nearest-neighbour graph.
> - `concept` [[30-Concepts/trajectory-inference|Trajectory inference]] — Ordering cells along a continuous process rather than into discrete groups.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — The tool layer: aligners, callers, imputers and integrators.

## All sources on this page

> [!info]- 11 summaries cited here
> - [[10-Summaries/argelaguet-2018-mofa|Argelaguet 2018]]
> - [[10-Summaries/korsunsky-2019-harmony|Korsunsky 2019]]
> - [[10-Summaries/luo-2024-scatac-benchmark|Luo 2024]]
> - [[10-Summaries/mcinnes-2018-umap|McInnes 2018]]
> - [[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]
> - [[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]
> - [[10-Summaries/welch-2019-liger|Welch 2019]]
> - [[10-Summaries/wolf-2019-paga|Wolf 2019]]
> - [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]
> - [[10-Summaries/zhang-2022-higashi|Zhang 2022]]
> - [[10-Summaries/zhou-2019-schicluster|Zhou 2019]]
