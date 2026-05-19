---
type: concept
title: STARK
aliases: [Structural Topology Analysis and Rich Knowledge base]
tags: [3D-genome, software, single-cell-Hi-C, pipeline]
created: 2026-05-12
updated: 2026-05-12
---

# STARK

> A unified analysis framework (Jiang et al. 2026) for single-cell 3D-genome sequencing data. Three modules: Preprocess (alignment, demultiplexing, .cool generation), Cell QC (EmptyCells filtering, GiniQC, SSCE metric), and Downstream Analysis (imputation, clustering, A/B compartments, TADs, loops, 3D reconstruction).

## Definition

Handles 15+ sc3DG-seq technologies in a single pipeline. Introduces EmptyCells (Monte-Carlo-based barcode filtering) and SSCE (Spatial Structure Capture Efficiency) as novel QC metrics.

## Why it matters

Eliminates the per-method data-processing fragmentation that has hampered cross-study sc3DG-seq comparisons. Paired with **scNucleome**, a public repository of uniformly processed sc3DG-seq datasets.

## Examples

- [[10-Summaries/jiang-2026-stark-scnucleome]] benchmarks 15 sc3DG-seq technologies under STARK.

## Related

- [[30-Concepts/single-cell-hi-c]] · [[30-Concepts/empty-cells-algorithm]] · [[30-Concepts/sscce]] · [[40-Topics/3d-genome]]
