---
type: summary
title: "Hong et al. 2025 — Navigating the 3D genome at single-cell resolution (review)"
source: "[[00-Sources/papers/Navigating the 3D genome at single-cell resolution_ techniques, computation, and mechanistic landscapes]]"
source_kind: paper
author: "Feitong Hong, Kaiyuan Han, ... Hao Lin, Fuying Dao (corresponding)"
published: 2025-10-06
ingested: 2026-05-12
doi: "10.1093/bib/bbaf520"
journal: "Briefings in Bioinformatics"
tags: [review, 3D-genome, single-cell-HiC, TADs, compartments, chromatin-loops, cell-cycle]
entities:
  - "[[20-Entities/fuying-dao]]"
  - "[[20-Entities/hao-lin]]"
concepts:
  - "[[30-Concepts/3d-genome]]"
  - "[[30-Concepts/single-cell-hi-c]]"
  - "[[30-Concepts/topologically-associating-domain]]"
  - "[[30-Concepts/chromatin-compartments]]"
  - "[[30-Concepts/sc-sprite]]"
  - "[[30-Concepts/dip-c]]"
topics:
  - "[[40-Topics/3d-genome]]"
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Hong et al. (2025) — *Navigating the 3D genome at single-cell resolution (review)* — *Briefings in Bioinformatics*. [DOI](https://doi.org/10.1093/bib/bbaf520)

# Hong et al. 2025 — Navigating the 3D genome at single-cell resolution

> Thesis: Bulk Hi-C and its derivatives revealed the principles of 3D genome organization (compartments, TADs, loops) but masked single-cell variability. Over the past decade, scHi-C and related single-cell methods have exposed how heterogeneous chromatin folding is between cells — variability that drives lineage decisions, disease phenotypes, and transcriptional plasticity. This review summarizes the experimental platforms, computational algorithms, and mechanistic insights of single-cell 3D genomics circa 2025.

## Key claims

- **Three classes of single-cell 3D-genome methods**: (1) bulk-Hi-C-adapted per-cell methods (scHi-C, snHi-C), (2) cell-barcode-based high-throughput (sciHi-C, scHi-C⁺, snHi-C⁺), (3) multi-omics combinations (sn-m3C, HiRES, scMethyl that pair Hi-C with methylation/expression).
- **Notable platforms**: scSPRITE (sonication-based, captures higher-order multi-way contacts), scNanoHi-C (long-read Hi-C, first of its kind), Droplet Hi-C and Paired Hi-C (microfluidic-based scale).
- **Computational challenges**: high dimensionality, extreme sparsity (most cells get <100k contacts), noise. Algorithms for QC, normalization, imputation, structural reconstruction, A/B compartment calling, TAD/loop identification under single-cell sparsity.
- **Mechanistic insights**: TAD boundaries fluctuate between cells; compartmentalization varies through the cell cycle; loop dynamics reflect transcriptional state. Cancer, brain disorders, aging, and stem-cell fate all show distinctive 3D-genome heterogeneity patterns.
- **Future directions**: integration with chromatin marks / methylation / transcription at the same cell; topology-guided therapeutic strategies; deep-learning models for structure inference.

## Methods / evidence

Authoritative narrative review with tables comparing >15 sc3DG-seq technologies on year, resolution, throughput, and cost. Cites mechanistic findings from cancer (intra-tumor heterogeneity), brain (neuropsychiatric structural variation), and developmental biology (cell-fate transitions).

## Surprising or load-bearing bits

- The framing that **3D genome architecture is a regulatory layer that varies cell-to-cell**, not just a structural scaffold, is the conceptual through-line. Bulk Hi-C produced a misleading picture of stable architecture.
- scNanoHi-C as the first long-read single-cell Hi-C is noteworthy — the long-read advantage is **detecting higher-order interactions** (multi-way contacts) that ligation-based short-read methods can't see.
- Multi-omics integration is the field's active frontier: simultaneous 3D contacts + methylation (sn-m3C-seq) or + expression (HiRES) reveals causal-relationship questions inaccessible to single-modality work.

## Connections to other sources

- Provides the conceptual scaffold for [[10-Summaries/jiang-2026-stark-scnucleome]] (STARK + scNucleome) which benchmarks 15 sc3DG-seq technologies under a unified pipeline.
- Connects to [[10-Summaries/sandy-2019-naturereviewsgenetics]] (Klemm/Greenleaf chromatin-accessibility review) and [[10-Summaries/alev-2023-naturereviewsmolecularcellbiology]] (Baysoy/Fan/Satija multi-omics landscape).
- Mentions 3D-genome long-read methods that overlap with [[10-Summaries/profiling-the-epigenome-using-long-read-sequencing]] (Liu/Conesa 2025 review).

## Open questions

- Single-cell 3D-genome resolution still much coarser than bulk Hi-C (~kb vs ~100 bp). Will single-molecule long-read or imaging methods close the gap?
- Causality: do 3D-architecture changes drive expression changes or follow them? Single-cell joint readouts begin to answer this but biology is far from settled.

---
**Source:** [DOI](https://doi.org/10.1093/bib/bbaf520)
## Related

- [[40-Topics/3d-genome]] · [[30-Concepts/single-cell-hi-c]] · [[30-Concepts/topologically-associating-domain]] · [[10-Summaries/jiang-2026-stark-scnucleome]]
