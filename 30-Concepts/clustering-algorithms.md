---
type: concept
title: Clustering Algorithms
aliases: [community detection, Louvain, Leiden, k-means clustering, clustering]
tags: [clustering, Leiden, Louvain, community-detection, resolution]
created: 2026-08-10
updated: 2026-10-12
---

# Clustering Algorithms

> Partitioning cells into groups, usually by community detection on a *k*-nearest-neighbour graph — the step that produces "cell types," and therefore the step whose parameters determine how many cell types a study reports ([[10-Summaries/cao-2019-moca|Cao 2019]]; [[10-Summaries/wolf-2019-paga|PAGA]]).

> [!abstract] 한눈에
> Single-cell clustering은 대개 kNN graph 위에서 Louvain이나 Leiden으로 세포를 나누는 작업이고, 이 단계의 resolution 설정이 연구가 보고하는 cell type 수를 결정한다 ([[10-Summaries/cao-2019-moca|Cao 2019]]). Louvain은 내부가 끊어진 community를 돌려줄 수 있어서 Leiden이 이를 고쳤고, cluster 수는 발견이 아니라 선택이라는 점이 핵심이다 ([[10-Summaries/traag-2019-leiden|Leiden]]; [[10-Summaries/wolf-2019-paga|PAGA]]).

## Definition

Clustering partitions cells into groups, usually by community detection on a *k*-nearest-neighbour graph ([[10-Summaries/wolf-2019-paga|PAGA]]). It is the step that produces "cell types" and feeds [[cell-type-annotation]], so its parameters determine how many cell types a study reports ([[10-Summaries/cao-2019-moca|Cao 2019]]).

## Why it matters

- **Resolution is a choice, not a discovery.** "Cell type" and "subtype" are operational definitions specific to a given manuscript ([[10-Summaries/cao-2019-moca|Cao 2019]]), so subtype counts are not directly comparable across atlases (synthesis).
- Varying partition resolution produces graph abstractions at multiple scales, enabling hierarchical exploration rather than one committed answer ([[10-Summaries/wolf-2019-paga|PAGA]]).

## Methods in use

| Method | Approach | Notes | Source |
|---|---|---|---|
| Louvain | Modularity optimization | The long-standing default | ([[10-Summaries/cao-2019-moca\|Cao 2019]]; [[10-Summaries/wolf-2019-paga\|PAGA]]) |
| Leiden | Modularity optimization with a refinement phase | Fixes Louvain's guarantee problem — Louvain can return internally disconnected communities | ([[10-Summaries/traag-2019-leiden\|Leiden]]) |
| Soft *k*-means | Fractional cluster membership | Preserves continuous cell-state gradients; clusters serve as surrogate variables rather than as cell-type calls | ([[10-Summaries/korsunsky-2019-harmony\|Harmony]]) |
| *K*-means on top principal components | Partitioning in a reduced space (see [[dimensionality-reduction]]) | Used for sparse contact data after imputation | ([[10-Summaries/zhou-2019-schicluster\|scHiCluster]]) |

## Evaluation

- Adjusted Rand index against known labels is the standard accuracy measure for benchmarking ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).
- Cell-type-level LISI checks that integration has not merged distinct types ([[10-Summaries/korsunsky-2019-harmony|Harmony]]).

## Evidence and examples

- Iterative re-clustering of 38 major types yielded 655 subclusters in MOCA ([[10-Summaries/cao-2019-moca|Cao 2019]]).
- Louvain produced up to 25% badly connected and up to 16% disconnected communities, and iterating it made this worse ([[10-Summaries/traag-2019-leiden|Leiden]]).

## Contested points

- **Clusters versus trajectories.** Clustering assumes discrete groups while [[trajectory-inference]] assumes a connected manifold; treating these as alternatives rather than as two views of one graph is the framing PAGA rejects ([[10-Summaries/wolf-2019-paga|PAGA]]).
- **Distances between cluster means.** Comparing clusters by Euclidean distance between cluster means is a local-validity error — such distances quantify biological similarity only at small scales and break down for cluster-scale objects ([[10-Summaries/wolf-2019-paga|PAGA]]). The critique applies well beyond trajectory inference (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/dimensionality-reduction|Dimensionality reduction]] — The embedding the kNN graph is usually built on.
> - `concept` [[30-Concepts/cell-type-annotation|Cell-type annotation]] — Naming the clusters this step produces.
> - `concept` [[30-Concepts/trajectory-inference|Trajectory inference]] — The continuous view of the same graph.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — Analysis methods for single-cell data.

## All sources on this page

> [!info]- 5 summaries cited here
> - [[10-Summaries/cao-2019-moca|Cao 2019]]
> - [[10-Summaries/korsunsky-2019-harmony|Korsunsky 2019]]
> - [[10-Summaries/traag-2019-leiden|Traag 2019]]
> - [[10-Summaries/wolf-2019-paga|Wolf 2019]]
> - [[10-Summaries/zhou-2019-schicluster|Zhou 2019]]
