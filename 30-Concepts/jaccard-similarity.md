---
type: concept
title: Jaccard similarity
aliases: [Jaccard index]
tags: [similarity-metric, set-theory, clustering]
created: 2026-05-12
updated: 2026-05-12
---

# Jaccard similarity

> A set-similarity metric: |A ∩ B| / |A ∪ B|. Ranges 0 (disjoint) to 1 (identical). Used in [[30-Concepts/snapatac]] to measure similarity between pairs of single cells based on overlap of accessible 5-kb genomic bins.

## Why it matters

- Naturally handles binary presence/absence data (a bin is open or not).
- Penalizes cells with too many or too few open bins, requiring depth normalization (which SnapATAC handles via regression).

## Related

- [[30-Concepts/snapatac]] · [[40-Topics/single-cell-atac-seq]]
