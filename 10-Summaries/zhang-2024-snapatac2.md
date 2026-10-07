---
type: summary
title: "Zhang 2024 — A fast, scalable and versatile tool for analysis of single-cell omics data (SnapATAC2)"
source: "[[00-Sources/papers/A fast, scalable and versatile tool for analysis of single-cell omics data]]"
source_quality: full
source_sha256: "9545f5aeb641dc6a5eb28f7e7a6590bf73045ddc46c64592e8f8dfb1ed850b81"
aliases: ["Zhang 2024", "SnapATAC2", "snapatac-2"]
tags: [SnapATAC2, computational, dimensionality-reduction, scATAC, multimodal, Ren-lab, UCSD]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Zhang et al. (2024) — *A fast, scalable and versatile tool for analysis of single-cell omics data (SnapATAC2)* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-023-02139-9)

Zhang, Zemke, Armand and Ren (Ren lab, UCSD) released **SnapATAC2**, a major rewrite of the original SnapATAC package with a new nonlinear dimensionality-reduction algorithm based on a matrix-free spectral embedding (Lanczos algorithm on the Laplacian implicit matrix). The method achieves linear time and space complexity in cell number while preserving the geometric properties of the underlying data — eliminating the quadratic memory blow-up of conventional spectral embedding for million-cell datasets.

Benchmarked across scATAC-seq, scRNA-seq, scHi-C, and multimodal (10x Multiome) data, SnapATAC2 outperforms ArchR/Signac (LSI), cisTopic, EpiScanpy, PeakVI, scBasset and SCALE on embedding precision. Its runtime scales as well as ArchR/Signac/EpiScanpy, with far lower memory (21 GB for 200,000 cells; a ~650,000-cell atlas processed). The package is modular, integrates with the scverse ecosystem, and is implemented in Rust with a Python interface.

## Why this matters

A major computational anchor for §4: SnapATAC2 is the current best-in-class scalable embedder for scATAC-seq and multimodal omics. Companion to ArchR/Signac/EpiScanpy in the analysis-tool section. Especially relevant for cohort-scale mosaicism studies (e.g., brain banks with millions of nuclei) where O(N²) memory growth is the bottleneck. The cross-modal versatility (scHi-C, scATAC, multimodal) supports our argument for a unified locus-state analysis framework rather than modality-specific siloed tools.

---
**Source:** [DOI](https://doi.org/10.1038/s41592-023-02139-9) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/38191932/)

## Related

- [[10-Summaries/stuart-2021-natmethods]]
- [[10-Summaries/granja-2021-archr]]
- single cell analysis tools
