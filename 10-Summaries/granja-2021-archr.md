---
type: summary
title: "Granja et al. 2021 — ArchR: scalable scATAC-seq analysis software in R"
source: "[[00-Sources/papers/ArchR is a scalable software package for integrative single-cell chromatin accessibility analysis]]"
source_kind: paper
author: "Jeffrey M. Granja, M. Ryan Corces, Sarah E. Pierce, S. Tansu Bagdatli, Hani Choudhry, Howard Y. Chang, William J. Greenleaf (corresponding)"
published: 2021-02-25
ingested: 2026-05-18
ingest_depth: abstract+intro
doi: "10.1038/s41588-021-00790-6"
journal: "Nature Genetics"
tags: [ArchR, scATAC-seq, software, R-package, Greenleaf-lab, Chang-lab, doublet-detection, trajectory, multi-omics-integration]
entities: []
concepts:
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/chromatin-accessibility]]"
topics:
  - "[[40-Topics/single-cell-atac-seq]]"
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Granja et al. (2021) — *ArchR: scalable scATAC-seq analysis software in R* — *Nature Genetics*. [DOI](https://doi.org/10.1038/s41588-021-00790-6)

# Granja et al. 2021 — ArchR

> Thesis: scATAC-seq data generation has outpaced analysis software. ArchR provides an end-to-end R package for **doublet removal, clustering, cell-type identification, peak calling, trajectory inference, gene-to-element linkage, TF footprinting, expression prediction, and multi-omic integration with scRNA-seq** — capable of processing **1.2 million cells on a standard Unix laptop in 8 hours**.

## Key claims (abstract + intro)

- **End-to-end analysis pipeline**: every common scATAC-seq operation from raw fragments through final cell-type-specific regulatory maps, integrated into one R package.
- **Scalability is the load-bearing claim**: 1.2 M cells / 8 h on a laptop — order-of-magnitude faster than alternatives (Signac, SnapATAC2).
- **Integration with scRNA-seq**: ArchR can co-cluster scATAC + scRNA, predict gene expression from chromatin accessibility, and assign TFs to cells.
- **TF footprinting** at single-cell aggregate resolution; identifies cell-type-specific regulatory programs.

## Why this matters

ArchR has become a dominant scATAC analysis package alongside Signac (Seurat ecosystem) and SnapATAC2. Anchors the scATAC analysis tools cluster in the wiki alongside chromVAR (Schep 2017), cisTopic (Bravo 2019), SnapATAC (Fang 2021), and EpiScanpy (Danese 2021).

## Note on ingest depth

Abstract + intro only; full PDF re-ingest will deepen benchmark comparisons and the multi-omic integration algorithm details.

---
**Source:** [DOI](https://doi.org/10.1038/s41588-021-00790-6) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33633365/)

## Related

- [[30-Concepts/scatac-seq]] · [[30-Concepts/chromatin-accessibility]]
- [[10-Summaries/schep-2017-chromvar]] · [[10-Summaries/bravo-2019-cistopic]] · [[10-Summaries/fang-2021-snapatac]] · [[10-Summaries/danese-2021-episcanpy]]
- [[40-Topics/single-cell-atac-seq]]
