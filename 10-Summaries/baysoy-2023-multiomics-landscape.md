---
type: summary
title: "Baysoy et al. 2023 — Technological landscape and applications of single-cell multi-omics"
source: "[[00-Sources/papers/The technological landscape and applications of single-cell multi-omics]]"
source_kind: paper
author: "Alev Baysoy, Zhiliang Bai, Rahul Satija, Rong Fan"
published: 2023-10
ingested: 2026-05-11
doi: "10.1038/s41580-023-00615-w"
journal: "Nature Reviews Molecular Cell Biology 24:695–713"
tags: [review, single-cell-multiomics, spatial-omics, integration-methods]
entities:
  - "[[20-Entities/rong-fan]]"
  - "[[20-Entities/rahul-satija]]"
concepts:
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[30-Concepts/cite-seq]]"
  - "[[30-Concepts/spatial-multiomics]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
---

**Citation:** Baysoy et al. (2023) — *Technological landscape and applications of single-cell multi-omics* — *Nature Reviews Molecular Cell Biology*. [DOI](https://doi.org/10.1038/s41580-023-00615-w)

# Baysoy et al. 2023 — Technological landscape and applications of single-cell multi-omics

> Thesis: single-cell multi-omics is now mature enough that nearly any pair (or triple) of modalities — transcriptome, genome, epigenome, proteome, metabolome, spatial — can be measured in the same cell. The reviewer's framework is **throughput / resolution / modality integration / uniqueness / accuracy** — five axes along which to compare any multi-omic method. Applications include lineage tracing, tissue/cell-type atlases, tumour immunology, and spatial mapping of cellular function.

## Key claims

- **Multi-omics catalog by modality combination**: scRNA + scATAC (10x Multiome, SHARE-seq); scRNA + protein (CITE-seq, REAP-seq); scDNA + scRNA (G&T-seq, DR-seq, SIDR-seq); scRNA + methylome (scM&T-seq); CRISPR-perturbed scRNA (Perturb-seq, CROP-seq); scRNA + spatial (Slide-seq, MERFISH, Visium).
- **Spatial multi-omics** is treated as a co-equal modality: tissue context preserved while measuring molecular profiles. Imaging-based (MERFISH, seqFISH) and NGS-based (Slide-seq, Visium, Stereo-seq) approaches each have strengths.
- **Computational integration** is now the bottleneck more than wet-lab measurement. Tools: Seurat (Weighted Nearest Neighbor), Scanpy/scvi-tools, MOFA, totalVI for joint embeddings.
- **Three integration paradigms**: horizontal (same modality, different samples), vertical (same cells, different modalities), diagonal (different cells, different modalities — most computationally demanding).
- **Bridge integration** (e.g., GoT–ChA + DOGMA-seq in [[10-Summaries/izzo-2024-got-cha]]) is a special case of diagonal integration where overlapping modalities act as bridges.

## Methods / evidence

Comprehensive landscape review with Table 1 cataloging dozens of methods. From Yale (Fan lab — bioengineering) + NYGC (Satija — Seurat).

## Surprising or load-bearing bits

- **Computational integration is now the bottleneck**: the wet-lab proliferation has outpaced the analysis tools. This is the central message that distinguishes this review from earlier multi-omics surveys.
- **The throughput-resolution tradeoff**: high-cell-number methods (droplet) give shallow per-cell data; low-cell-number methods (plate-based) give deep per-cell data. Method choice is application-specific.
- **Spatial multi-omics as a first-class modality** rather than a 2D extension of single-cell methods — preserves tissue architecture, neighborhood relationships, and cell-cell communication signals that dissociation destroys.

## Entities mentioned

- [[20-Entities/rong-fan]] — senior author; Yale; spatial-omics and bioengineering PI.
- [[20-Entities/rahul-satija]] — co-senior; NYGC/NYU; developer of Seurat and major multi-omic integration toolkit.

## Concepts touched

- [[40-Topics/single-cell-multiomics]]
- [[30-Concepts/cite-seq]]
- [[30-Concepts/spatial-multiomics]]

## Connections to other sources

- **Catalogs and contextualizes** [[10-Summaries/nam-2019-got]] (GoT — genotype + RNA), [[10-Summaries/izzo-2024-got-cha]] (GoT–ChA — genotype + chromatin), [[10-Summaries/swanson-2025-daf-seq]] (DAF-seq — single-molecule chromatin + DNA).
- **Complementary to** [[10-Summaries/vandereyken-2023-scmultiomics-review]] — both 2023 multi-omics reviews; Alev 2023 is broader (includes proteome, metabolome) while Katy 2023 focuses on genome-proteome combinations with deeper method-by-method protocol detail.
- **Best-practices counterpart**: [[10-Summaries/heumos-2023-best-practices]] provides the analysis workflow recommendations for the methods cataloged here.

## Open questions

- Standardized benchmarks across multi-omic integration tools.
- Quadruple or quintuple modality measurements — currently in development but no clear winner.
- Cost-per-cell scaling — multi-omic methods are still substantially more expensive than unimodal at equal cell number.

---
**Source:** [DOI](https://doi.org/10.1038/s41580-023-00615-w)
