---
type: summary
title: "Granja 2021 — ArchR: a scalable software package for integrative single-cell chromatin accessibility analysis"
source: "[[00-Sources/papers/ArchR is a scalable software package for integrative single-cell chromatin accessibility analysis]]"
aliases: [Granja 2021, ArchR, Jeffrey 2021]
tags: [scATAC-seq, computational-tool, ArchR, software, Greenleaf, foundational]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Granja et al. (2021) — *ArchR: a scalable software package for integrative single-cell chromatin accessibility analysis* — *Nature Genetics*. [DOI](https://doi.org/10.1038/s41588-021-00790-6)

# Granja et al. 2021 — ArchR

> Jeffrey M. Granja, M. Ryan Corces, Sarah E. Pierce, S. Tansu Bagdatli, Hani Choudhry, Howard Y. Chang, **William J. Greenleaf\***. *Nature Genetics* **53**, 403–411 (March 2021). DOI: 10.1038/s41588-021-00790-6. Stanford.

## Thesis

**ArchR** is a scalable R-based software framework for end-to-end scATAC-seq analysis: marker-feature ID, doublet removal, clustering, cell-type ID, peak generation, DNA-to-gene linking, TF footprinting, scRNA-seq integration, trajectory inference. Analyzes **1.2 million cells in 8 hours on a standard Unix laptop** (vs SnapATAC/Signac requiring 128 GB RAM, 20 cores). Becomes a de facto standard for scATAC analysis pipelines.

## Mechanism

1. **Arrow files** (HDF5-based per-chromosome chunks) replace in-memory matrices → low-memory disk-backed analysis.
2. **500-bp tile matrix** (vs SnapATAC's 5-kb bins) → fine-grained genome-wide accessibility while avoiding peak-calling-first ambiguity.
3. **ArchR doublet detection**: bioinformatically generated synthetic doublets projected onto UMAP → nearest neighbors identified as doublets (ROC AUC 0.918 on 10 cell-line mixture).
4. **Iterative LSI** for dimensionality reduction → less batch-effect sensitive than fixed-feature LSI.

## Key claims

- **Runtime**: 70,000-cell dataset in <1 hour with 32 GB RAM + 8 cores (SnapATAC exceeded 128 GB; Signac exceeded 32 GB).
- **Doublet detection**: ROC AUC 0.918 by fragment count + nearest-neighbor; outperforms Scrublet for scATAC-seq.
- **Dimensionality reduction**: outperforms LSI + diffusion maps for batch robustness across hematopoietic samples.
- Scales to **1.2M cells in 8h** on standard laptop.

## Surprising / load-bearing for the review

- For §4.3 (Open Chromatin & DNA-Binding Profiles computational), ArchR replaces SnapATAC and Signac as the modern default. Together with [[snapatac]], [[chromvar]], [[cistopic]], [[episcanpy]], it forms the scATAC-seq tooling stack.
- The **doublet-detection approach** (synthetic-doublet projection) is one of the most-cited methodological contributions to the field.

## Entities / concepts touched

[[scatac-seq]] · [[snapatac]] · [[scanpy]] · [[anndata]] · [[chromvar]] · [[20-Entities/william-greenleaf]] · [[40-Topics/single-cell-atac-seq]]

## Related summaries

- comprehensive analysis of single cell atac seq data with snapatac — SnapATAC, predecessor.
- chromvar inferring transcription factor associated accessibility from single cell epigenomic data — chromVAR TF analysis, integrates into ArchR.
- episcanpy integrated single cell epigenomic analysis — EpiScanpy, Python alternative.

---
**Source:** [DOI](https://doi.org/10.1038/s41588-021-00850-x) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33790476/)

---
**Source:** [DOI](https://doi.org/10.1038/s41588-021-00850-x) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33790476/)
