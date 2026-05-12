---
type: concept
title: scChIX-seq
aliases: [single-cell ChIC and unmixing]
tags: [histone-modifications, single-cell, multi-modal, deconvolution, LDA]
created: 2026-05-12
updated: 2026-05-12
---

# scChIX-seq

> Multiplexes two histone-mark antibodies in the same cell during sortChIC, then computationally **deconvolves the superimposed cut-site profiles** using single-incubated reference datasets and LDA topic modeling.

## Definition

Three datasets per experiment: single-incubated dataset A (mark 1 only), single-incubated dataset B (mark 2 only), double-incubated dataset C (both marks). LDA learns topic models on A and B; for each cell in C, select the most-likely (topic-A, topic-B) pair and probabilistically assign each fragment to mark 1 or mark 2.

## Why it matters

- Per-cell relationships between marks (mutually exclusive, co-occurring, transitions) are visible from a single cell. Bulk averages obscure cell-type-specific transitions.
- Enables "chromatin velocity" — coordinated mark dynamics through differentiation trajectories.

## Examples

- H3K27me3 + H3K9me3 in mouse BM (B cells, granulocytes, NK cells): FDR 10/3/1% respectively, recovers mutual exclusivity.
- H3K4me1 + H3K27me3 in BM: resolves pro-B → B-cell transition via *IgK* chromatin opening.
- Macrophage differentiation: H3K4me1 + H3K36me3 chromatin velocity ([[10-Summaries/scchix-seq-infers-dynamic-relationships-between-histone-modifications-in-single-cells]]).

## Related

- [[30-Concepts/sortchic]] · [[30-Concepts/latent-dirichlet-allocation]] · [[30-Concepts/chromatin-velocity]] · [[30-Concepts/histone-modifications]] · [[40-Topics/histone-modifications]] · [[20-Entities/alexander-van-oudenaarden]]
