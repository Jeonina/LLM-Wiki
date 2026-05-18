---
type: summary
title: "Bartosovic et al. 2022 — nano-CUT&Tag: multimodal single-cell chromatin profiling with nanobody-Tn5 fusions"
source: "[[00-Sources/papers/Multimodal chromatin profiling using nanobody-based single-cell CUT&Tag]]"
source_kind: paper
author: "Marek Bartosovic, Gonçalo Castelo-Branco (corresponding)"
published: 2022-12-19
ingested: 2026-05-18
ingest_depth: abstract+intro
doi: "10.1038/s41587-022-01535-4"
journal: "Nature Biotechnology"
tags: [nano-CUT&Tag, nanobody-Tn5, multimodal, single-cell, H3K27ac, H3K27me3, ATAC, oligodendrocyte, chromatin-velocity, Castelo-Branco-lab]
entities: []
concepts:
  - "[[30-Concepts/cut-and-tag]]"
  - "[[30-Concepts/histone-modifications]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/chromatin-velocity]]"
topics:
  - "[[40-Topics/chromatin-architecture]]"
  - "[[40-Topics/histone-modifications]]"
  - "[[40-Topics/single-cell-multiomics]]"
---

**Citation:** Bartosovic et al. (2022) — *nano-CUT&Tag: multimodal single-cell chromatin profiling with nanobody-Tn5 fusions* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-022-01535-4)

# Bartosovic et al. 2022 — nano-CUT&Tag (nano-CT)

> Thesis: scCUT&Tag (Bartosovic 2021) measures one histone mark per cell. nano-CUT&Tag (nano-CT) replaces the antibody-Tn5 system with **direct nanobody-Tn5 fusions**, enabling **simultaneous profiling of up to three epigenomic modalities** (chromatin accessibility + two histone marks) in the same single cell. Significantly higher sensitivity than scCUT&Tag.

## Key claims (abstract + intro)

- **Chemistry**: nanobodies (single-domain antibody fragments) fused directly to Tn5 — eliminates the secondary antibody step, reduces background.
- **Multimodal**: simultaneously profile ATAC + H3K27ac + H3K27me3 in same cell.
- **Sensitivity**: significantly more fragments per cell than unimodal scCUT&Tag.
- **Low input**: compatible with 25,000–200,000 starting cells.
- **Biological findings (juvenile mouse brain)**:
  - More cell types/states resolved than unimodal data.
  - **Chromatin velocity** inferred between ATAC and H3K27ac in oligodendrocyte lineage — accessibility precedes acetylation.
  - **Two sequential H3K27me3 repression waves** during oligodendrocyte differentiation at distinct gene modules.

## Why this matters

Establishes **multimodal single-cell chromatin** as feasible at scale. Bridges the histone-modification axis with chromatin accessibility, enabling causal-direction analysis (ATAC vs H3K27ac chromatin velocity). Complements nano-CT to the lineage that includes scEpi²-seq (methylation + histone mark) and SHARE-seq (RNA + ATAC).

## Note on ingest depth

Abstract + intro only; full PDF re-ingest will deepen the nanobody-Tn5 engineering details and the chromatin-velocity model.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-022-01535-4) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/36536074/)

## Related

- [[30-Concepts/cut-and-tag]] · [[30-Concepts/histone-modifications]] · [[30-Concepts/chromatin-accessibility]] · [[30-Concepts/chromatin-velocity]]
- [[10-Summaries/bartosovic-2021-sccut-tag]] · [[10-Summaries/janssens-2023-scicut-tag]] · [[10-Summaries/geisenberger-2025-scepi2-seq]] · [[10-Summaries/ma-2020-share-seq]]
- [[40-Topics/single-cell-multiomics]] · [[40-Topics/chromatin-architecture]]
