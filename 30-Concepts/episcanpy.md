---
type: concept
title: EpiScanpy
aliases: [scanpy for epigenomics]
tags: [scATAC-seq, scBS-seq, scanpy, Python, software, Theis-lab]
created: 2026-05-12
updated: 2026-05-12
---

# EpiScanpy

> A Python toolkit that brings scATAC-seq and single-cell DNA methylation data into the scanpy / AnnData ecosystem. Generates count matrices over flexible feature spaces (peaks, windows, genes, enhancers, custom .bed) and inherits scanpy's clustering, manifold learning, trajectory analysis, and atlas-integration tools.

## Definition

Pre-processing: build cells × features matrix from BAM or methylation-call files. Methylation: average β over CpGs in each feature; explicit handling of "not observed" vs "not methylated." ATAC: binarize and library-size normalize. Downstream: tSNE, UMAP, Louvain, PAGA, diffusion pseudotime, BBKNN batch correction.

## Why it matters

- Lowest barrier-to-entry tool for scATAC-seq analysis in Python.
- Benchmarks at or near top across 11 scATAC-seq methods (Chen et al. framework); most robust across datasets.
- Adult-neuron DNA methylation at enhancers gives strongest cell-type separation (silhouette 0.41 vs 0.32/0.28/0.09 for windows/promoters/gene-bodies).

## Examples

- 81k mouse atlas cells in 18 min / 14 GB RAM. PBMC scATAC integration. Brain snmC-seq cell-type discovery ([[10-Summaries/episcanpy-integrated-single-cell-epigenomic-analysis]]).

## Related

- [[30-Concepts/scanpy]] · [[30-Concepts/anndata]] · [[30-Concepts/scatac-seq]] · [[30-Concepts/scbs-seq]] · [[40-Topics/single-cell-atac-seq]] · [[20-Entities/fabian-theis]]
