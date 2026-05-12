---
type: concept
title: k-medoids clustering
aliases: [PAM, Partitioning Around Medoids]
tags: [clustering, machine-learning]
created: 2026-05-12
updated: 2026-05-12
---

# k-medoids clustering

> A clustering algorithm similar to k-means but using actual data points as cluster centers ("medoids") rather than computed means. Robust to outliers and well-suited for sparse, ranked, or non-Euclidean data.

## Definition

Partitions n data points into k clusters by minimizing total distance to k medoid points. Each iteration: assign points to nearest medoid → for each cluster, find the point minimizing within-cluster distance → repeat until convergence.

## Why it matters

- More robust than k-means for noisy single-cell data.
- Used in [[30-Concepts/scabc]] for unsupervised scATAC-seq clustering, with sample-depth-based cell weighting.

## Related

- [[30-Concepts/scabc]] · [[40-Topics/single-cell-atac-seq]]
