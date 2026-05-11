---
type: summary
title: "Heumos et al. 2023 — Best practices for single-cell analysis across modalities"
source: "[[00-Sources/papers/Lukas_2023_NatureReviewsGenetics]]"
source_kind: paper
author: "Lukas Heumos, Anna C. Schaar, Single-cell Best Practices Consortium, Fabian J. Theis"
published: 2023-08
ingested: 2026-05-11
doi: "10.1038/s41576-023-00586-w"
journal: "Nature Reviews Genetics 24:550–572"
tags: [review, best-practices, single-cell-analysis, computational, benchmarking]
entities:
  - "[[20-Entities/fabian-theis]]"
concepts:
  - "[[30-Concepts/single-cell-multiomics]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
---

# Heumos et al. 2023 — Best practices for single-cell analysis across modalities

> Thesis: with >1,400 single-cell analysis tools available, the field needs explicit best-practice workflows. This consortium review summarizes independent benchmarks across modalities — transcriptome, chromatin accessibility, surface protein, immune receptors, spatial — and recommends modality-specific defaults grounded in those benchmarks rather than in popularity.

## Key claims

- **Quality control** is modality-specific:
  - **scRNA-seq**: filter low-count cells, high-mito cells; remove ambient RNA (SoupX, CellBender); detect doublets (Scrublet, scDblFinder).
  - **scATAC-seq**: TSS enrichment, fragment size distribution, peak count.
  - **CITE-seq (protein)**: handle isotype-control normalization, antibody-derived tag (ADT) contamination.
- **Normalization**: log-transform for scRNA-seq is the default, but pearson residuals (sctransform v2) are better for highly variable genes; for scATAC-seq use TF-IDF.
- **Doublet detection**, **batch correction** (Harmony, scVI, scANVI), **cell-type annotation** (CellTypist, automated reference-mapping) all have benchmarked best-practice choices.
- **Multimodal integration**: Seurat v4 WNN, totalVI, MOFA. Each has tradeoffs documented through benchmarks.
- The recommendations are explicitly tied to *independent* benchmark publications wherever those exist; otherwise, popular methods are listed with explicit caveats.

## Methods / evidence

Consortium consensus document. Helmholtz Munich (Theis group) led with contributions from across the field. Each section reviews published benchmarks and converges on recommendations.

## Surprising or load-bearing bits

- **Benchmark-driven rather than popularity-driven recommendations** is the explicit organizing principle. Many widely-used tools are not best-in-class on independent benchmarks; the review names this gap.
- **Modality-specific best practices** rather than a one-size-fits-all workflow — scATAC-seq normalization is genuinely different from scRNA-seq normalization, and ignoring this produces biased clusters.
- **Companion online book** at sc-best-practices.org maintains the recommendations as the field evolves — recognition that any printed best-practices document is out-of-date within a year.

## Entities mentioned

- [[20-Entities/fabian-theis]] — senior author; Helmholtz Munich; major computational biology PI for single-cell.

## Concepts touched

- [[30-Concepts/single-cell-multiomics]] — analysis side rather than wet-lab side.

## Connections to other sources

- **Workflow companion to** [[10-Summaries/alev-2023-naturereviewsmolecularcellbiology]] and [[10-Summaries/katy-2023-naturereviewsgenetics]] — those describe what to *measure*, this describes how to *analyze*.
- **Applies to analysis of data from** [[10-Summaries/anna-2019-nature]], [[10-Summaries/franco-2024-nature]], [[10-Summaries/elliott-2025-naturebiotechnology]] — each paper's downstream pipelines would be benchmarked against the recommendations here.

## Open questions

- Benchmark coverage is uneven — heavily weighted toward scRNA-seq, less so for scATAC-seq and emerging modalities.
- Recommendations age fast — the printed version is already partially superseded by 2025 tools.
- Cross-modality benchmarks are limited — most are within-modality, leaving multi-omic integration choices under-benchmarked.
