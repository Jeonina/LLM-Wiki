---
type: summary
title: "Luo 2024 — Benchmarking computational methods for single-cell chromatin data analysis"
source: "[[00-Sources/papers/Benchmarking computational methods for single-cell chromatin data analysis]]"
aliases: ["Luo 2024", "scATAC benchmark", "von Meyenn benchmark"]
tags: [benchmark, scATAC-seq, dimensionality-reduction, clustering, ArchR, Signac, SnapATAC2, vonMeyenn-lab, Robinson-lab, ETH-Zurich]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Luo et al. (2024) — *Benchmarking computational methods for single-cell chromatin data analysis* — *Genome Biology*. [DOI](https://doi.org/10.1186/s13059-024-03356-x)

Luo, Germain, Robinson and von Meyenn (ETH Zurich, SIB) benchmarked eight feature-engineering pipelines derived from five major scATAC-seq analysis methods on their ability to discover and discriminate cell types. The benchmark spans 10 metrics across cell embedding, shared-nearest-neighbor graph, and partition levels.

Methods tested cover four paradigms: (i) NLP-derived (Signac LSI/TF-IDF+SVD, ArchR iterative LSI, cisTopic LDA); (ii) graph/nonlinear (SnapATAC diffusion maps, SnapATAC2 Laplacian eigenmaps); (iii) feature-aggregation (BROCKMAN k-mer, SCRAT motif/DHS, Cicero gene-activity); (iv) neural network (PeakVI VAE, scBasset CNN, CellSpace).

Key findings: **feature-aggregation, SnapATAC and SnapATAC2 outperform latent-semantic-based methods** for cell-type discovery. SnapATAC and SnapATAC2 are preferred for datasets with complex cell-type structures. SnapATAC2 and ArchR are most scalable for large datasets.

## Why this matters

An independent, multi-method benchmark of scATAC-seq analysis tools — the chromatin-accessibility analog of Heumos 2023 (scRNA-seq best practices). Validates our review's emphasis on SnapATAC2 (Zhang 2024) as the current state-of-the-art for large-scale scATAC analysis. Anchors §4 (computational tools for accessibility) and §6 (limitations — different methods can give discordant cell-type assignments; benchmark-driven choice is essential).

---
**Source:** [DOI](https://doi.org/10.1186/s13059-024-03356-x) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/39152456/)

## Related

- [[10-Summaries/zhang-2024-snapatac2]]
- [[10-Summaries/stuart-2021-signac]]
- [[10-Summaries/granja-2021-archr]]
- [[30-Concepts/single-cell-analysis-tools]]
