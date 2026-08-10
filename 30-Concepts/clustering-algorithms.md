---
type: concept
title: Clustering Algorithms
aliases: [community detection, Louvain, Leiden, k-means clustering]
tags: [clustering, Leiden, Louvain, community-detection, resolution]
created: 2026-08-10
updated: 2026-08-10
---

# Clustering Algorithms

> Partitioning cells into groups, usually by community detection on a *k*-nearest-neighbour graph. The step that produces "cell types," and therefore the step whose parameters determine how many cell types a study reports.

## Methods in use

- **Louvain** modularity optimization, the long-standing default ([[cao-2019-moca]], [[wolf-2019-paga]]).
- **Leiden**, which fixes Louvain's guarantee problem — Louvain can return internally disconnected communities ([[traag-2019-leiden]]).
- **Soft *k*-means**, where fractional cluster membership preserves continuous cell-state gradients and clusters serve as surrogate variables rather than as cell-type calls ([[korsunsky-2019-harmony]]).
- **K-means on top principal components** for sparse contact data after imputation ([[zhou-2019-schicluster]]).

## Resolution is a choice, not a discovery

- Iterative re-clustering of 38 major types yielded **655 subclusters**, and the paper states explicitly that "cell type" and "subtype" are operational definitions specific to that manuscript ([[cao-2019-moca]]). Subtype counts are therefore not directly comparable across atlases (synthesis).
- Varying partition resolution produces graph abstractions at multiple scales, enabling hierarchical exploration rather than one committed answer ([[wolf-2019-paga]]).
- Clustering assumes discrete groups while trajectory inference assumes a connected manifold; treating these as alternatives rather than as two views of one graph is the framing PAGA rejects ([[wolf-2019-paga]]).

## Evaluation

Adjusted Rand index against known labels is the standard accuracy measure for benchmarking ([[zhou-2019-schicluster]]). Cell-type-level LISI checks that integration has not merged distinct types ([[korsunsky-2019-harmony]]).

## Caution

Comparing clusters by Euclidean distance between cluster means is a local-validity error — such distances quantify biological similarity only at small scales and break down for cluster-scale objects ([[wolf-2019-paga]]). The critique applies well beyond trajectory inference (synthesis).

## Related

- [[dimensionality-reduction]] · [[cell-type-annotation]] · [[trajectory-inference]] · [[computational-methods]]
