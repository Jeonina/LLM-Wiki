---
type: concept
title: scABC
aliases: [single cell Accessibility Based Clustering]
tags: [scATAC-seq, clustering, k-medoids, Wong-lab, software]
created: 2026-05-12
updated: 2026-05-12
---

# scABC

> An R package for unsupervised clustering of scATAC-seq data that weights cells by read coverage, applies weighted k-medoids on rank-transformed peak signals, refines via landmark-Spearman-correlation reassignment, and identifies cluster-specific peaks via empirical-Bayes regression.

## Definition

Two-stage clustering: initial weighted k-medoids on ranked peak signals → landmark cells (top-ranked peaks per cluster) → Spearman-correlation reassignment of all cells to nearest landmark. Cluster-specific peaks identified by hypothesis testing.

## Why it matters

- 99.6% accuracy on in silico 6-cell-line mixtures (966 cells).
- Discovers heterogeneity in nominally homogeneous populations (e.g., RA-treated mouse EBs split into 67 neuroectoderm vs 28 visceral-endoderm cells).
- Used as comparator for newer scATAC-seq tools.

## Examples

- See [[10-Summaries/unsupervised-clustering-and-epigenetic-classification-of-single-cells]].

## Related

- [[30-Concepts/scatac-seq]] · [[30-Concepts/k-medoids]] · [[30-Concepts/chromvar]] · [[40-Topics/single-cell-atac-seq]]
