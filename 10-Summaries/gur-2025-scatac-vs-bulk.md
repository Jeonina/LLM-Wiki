---
type: summary
title: "Gur & Hughes 2025 — scATAC-seq pseudobulk vs bulk ATAC-seq: same signal, better data quality"
source: "[[00-Sources/papers/scATAC-seq generates more accurate and complete regulatory maps than bulk ATAC-seq]]"
source_kind: paper
author: "E. Ravza Gur, Jim R. Hughes (corresponding)"
published: 2025-01-29
ingested: 2026-05-12
doi: "10.1038/s41598-025-87351-7"
journal: "Scientific Reports"
tags: [scATAC-seq, ATAC-seq, regulatory-elements, erythroblasts, PBMCs, NK-cells, comparison-study]
entities:
  - "[[20-Entities/jim-hughes]]"
  - "[[20-Entities/ravza-gur]]"
concepts:
  - "[[30-Concepts/atac-seq]]"
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/pseudo-bulk]]"
topics:
  - "[[40-Topics/single-cell-atac-seq]]"
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Gur et al. (2025) — *scATAC-seq pseudobulk vs bulk ATAC-seq: same signal, better data quality* — *Scientific Reports*. [DOI](https://doi.org/10.1038/s41598-025-87351-7)

# Gur & Hughes 2025 — scATAC-seq vs bulk ATAC-seq

> Thesis: Researchers using bulk ATAC-seq commonly assume that single-cell data with comparable cell counts is methodologically equivalent. This comparison study, on aliquots of the same erythroblast and NK-cell populations from the same donor, shows that scATAC-seq with pseudo-bulk aggregation gives the **same chromatin architecture signal but higher data quality, sensitivity to weak functional peaks, and the ability to detect heterogeneity within nominally homogeneous populations** — at comparable cost when heterogeneity matters.

## Key claims

- Chromatin-architecture signal between bulk and scATAC-seq is concordant when aliquots of the same cell population are compared (late erythroblasts differentiated from CD34+ cells, NK cells).
- scATAC-seq provides **substantially higher data quality**: improved sensitivity for weak but functionally important peaks (e.g., distal enhancers identifiable by H3K4me1 vs H3K4me3 sorting).
- **Heterogeneity detection**: scATAC-seq on a "homogeneous" CD34-derived erythroblast population (cisTopic-clustered) reveals **two distinct clusters**, falsifying the assumption of homogeneity. GO enrichment shows the clusters reflect different functional states.
- **Minimum-cell guidance**: scATAC-seq requires ~hundreds of cells to generate robust pseudo-bulk profiles and ~thousands to identify biologically meaningful sub-clusters. Below this threshold, scATAC-seq quality degrades.
- Practical guidance for the field: if you want to compare cell types, scATAC-seq with pseudo-bulk is at least as good as bulk ATAC-seq and is better at detecting unexpected within-population heterogeneity.

## Methods / evidence

Comparison of (a) bulk ATAC-seq on FACS-isolated erythroblasts and NK cells from the same human donor; (b) 10X scATAC-seq on the same cell populations; (c) publicly available PBMC scATAC-seq integrated via Azimuth. Peak calling with LanceOtron. Downstream clustering via cisTopic and ArchR. Peak annotation by H3K4me1/me3, H3K27ac ChIP-seq cross-referencing.

## Surprising or load-bearing bits

- The heterogeneity finding is what matters: erythroblasts derived from a single CD34+ source were assumed homogeneous; scATAC-seq says they aren't. This **directly contradicts the standard practice** of using bulk ATAC-seq on "purified" populations as the gold standard.
- Bulk ATAC-seq remains valuable for sequencing depth and cost-per-peak; scATAC-seq is essential when heterogeneity is the question or population is uncharacterized.

## Connections to other sources

- Quantitative complement to [[10-Summaries/sandy-2019-naturereviewsgenetics]] (Klemm/Greenleaf chromatin accessibility review) which articulated the conceptual case for single-cell methods.
- Uses [[10-Summaries/bravo-2019-cistopic]] (cisTopic) for clustering and ArchR for analysis.
- Provides cell-number practical floor for designs guided by frameworks like [[10-Summaries/danese-2021-episcanpy]] (EpiScanpy) and [[10-Summaries/fang-2021-snapatac]] (SnapATAC).

## Open questions

- The minimum cell-count threshold for "robust pseudo-bulk" likely depends on signal-to-noise of the cell type; not universally applicable.
- No comparison to combinatorial-indexing scATAC-seq (sciATAC); only droplet-based.

---
**Source:** [DOI](https://doi.org/10.1038/s41598-025-87351-7)
## Related

- [[40-Topics/single-cell-atac-seq]] · [[30-Concepts/atac-seq]] · [[30-Concepts/pseudo-bulk]]
