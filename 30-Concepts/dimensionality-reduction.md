---
type: concept
title: Dimensionality Reduction
aliases: [embedding, PCA, UMAP, t-SNE, latent space]
tags: [embedding, PCA, UMAP, visualization, manifold-learning]
created: 2026-08-10
updated: 2026-08-10
---

# Dimensionality Reduction

> Projecting high-dimensional single-cell measurements into a few coordinates for clustering, visualization and downstream modelling. The step where most analytical decisions become invisible.

## Common practice

PCA supplies the working embedding that batch correction and clustering operate on ([[korsunsky-2019-harmony]]); UMAP supplies the 2D visualization ([[mcinnes-2018-umap]]); matrix factorization supplies interpretable shared and dataset-specific factors ([[welch-2019-liger]]); learned embeddings from hypergraph neural networks supply representations for sparse contact data ([[zhang-2022-higashi]]).

## What the axes mean, when anyone checks

In single-cell Hi-C the principal components are interpretable and worth interrogating: **PC1 weights lie uniformly parallel to the diagonal**, capturing the contact–distance curve and hence cell-cycle state, while **PC2 weights are region-specific**, capturing compartment strength ([[zhou-2019-schicluster]]). This explains why oocytes and zygotes separate on PC1 while cancer cell lines separate on PC2 ([[zhou-2019-schicluster]]), and it corroborates the finding that a single scalar — the *P(s)* scaling coefficient — separates mitotic from interphase cells ([[ramani-2017-scihi-c]]).

## Global structure is not preserved by default

UMAP's layout depends on initialization, so a random start can place globally distant populations adjacently. Seeding with a coarse graph abstraction makes the global arrangement meaningful and converges about six times faster, with faithfulness quantified by a geodesic-distance cost function ([[wolf-2019-paga]]).

## Cautions

- Coverage or depth can be the dominant axis of variation, and is not cleanly removable by dropping PC1 because PC1 also carries biology ([[zhou-2019-schicluster]]).
- Embedding dimension choice affects some methods more than others; robustness to it is worth reporting ([[zhang-2022-higashi]]).
- An embedding that mixes datasets well may have merged cell types; the two must be measured separately ([[korsunsky-2019-harmony]]).

## Related

- [[batch-effect]] · [[clustering-algorithms]] · [[trajectory-inference]] · [[computational-methods]]
