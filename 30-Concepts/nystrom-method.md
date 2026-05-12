---
type: concept
title: Nyström method
aliases: [Nyström approximation]
tags: [linear-algebra, dimensionality-reduction, scalability]
created: 2026-05-12
updated: 2026-05-12
---

# Nyström method

> A low-rank matrix-approximation technique that computes the spectral decomposition of a large kernel matrix using only a sampled subset (landmark) of rows/columns. Reduces complexity from O(n²) to O(nm) where m is the number of landmarks.

## Definition

Given a similarity matrix K (here, cell × cell Jaccard), select m landmarks → compute eigenvector decomposition on the m × m sub-matrix → project all n cells onto that low-dimensional embedding.

## Why it matters

Enables scATAC-seq dimensionality reduction at the million-cell scale. SnapATAC uses ensemble Nyström (multiple sampling rounds combined via consensus) to improve reproducibility.

## Related

- [[30-Concepts/snapatac]] · [[30-Concepts/jaccard-similarity]] · [[40-Topics/single-cell-atac-seq]]
