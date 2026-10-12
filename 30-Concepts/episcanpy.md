---
type: concept
title: EpiScanpy
aliases: [scanpy for epigenomics]
tags: [scATAC-seq, scBS-seq, scanpy, Python, software, Theis-lab]
created: 2026-05-12
updated: 2026-10-12
---

# EpiScanpy

> A Python toolkit that brings scATAC-seq and single-cell DNA methylation data into the scanpy / AnnData ecosystem. Generates count matrices over flexible feature spaces (peaks, windows, genes, enhancers, custom .bed) and inherits scanpy's clustering, manifold learning, trajectory analysis, and atlas-integration tools ([[10-Summaries/danese-2021-episcanpy|Danese 2021]]).

> [!abstract] 한눈에
> EpiScanpy는 scATAC-seq와 single-cell DNA methylation 데이터를 scanpy·AnnData 생태계에서 분석하게 해 주는 Python toolkit이다 ([[10-Summaries/danese-2021-episcanpy|Danese 2021]]). Peak, window, gene, enhancer 같은 feature 공간을 골라 count matrix를 만들고 scanpy의 clustering·trajectory 도구를 그대로 쓴다 ([[10-Summaries/danese-2021-episcanpy|Danese 2021]]).

## Definition

Pre-processing: build cells × features matrix from BAM or methylation-call files. Methylation: average β over CpGs in each feature; explicit handling of "not observed" vs "not methylated." ATAC: binarize and library-size normalize. Downstream: tSNE, UMAP, Louvain, PAGA, diffusion pseudotime, BBKNN batch correction.

## Why it matters

- Lowest barrier-to-entry tool for scATAC-seq analysis in Python.
- Benchmarks at or near top across 11 scATAC-seq methods (Chen et al. framework); most robust across datasets.
- Adult-neuron DNA methylation at enhancers gives strongest cell-type separation (silhouette 0.41 vs 0.32/0.28/0.09 for windows/promoters/gene-bodies).

## Examples

- 81k mouse atlas cells in 18 min / 14 GB RAM. PBMC scATAC integration. Brain snmC-seq cell-type discovery ([[10-Summaries/danese-2021-episcanpy]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/scanpy|Scanpy]] — Python single-cell analysis framework EpiScanpy builds on.
> - `concept` [[30-Concepts/anndata|AnnData]] — The annotated data matrix format shared with scanpy.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Single-cell chromatin accessibility assay.
> - `concept` [[30-Concepts/scbs-seq|scBS-seq]] — Single-cell bisulfite sequencing for DNA methylation.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Hub for single-cell accessibility methods and analysis.
> - `entity` [[20-Entities/fabian-theis|Fabian Theis]] — Co-author of EpiScanpy (Theis lab).

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/danese-2021-episcanpy|Danese 2021]]
