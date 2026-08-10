---
type: summary
title: "Bartosovic et al. 2021 — scCUT&Tag: single-cell CUT&Tag for histone modifications + TFs in tissue"
source: "[[00-Sources/papers/Single-cell CUT&Tag profiles histone modifications and transcription factors in complex tissues]]"
source_kind: paper
author: "Marek Bartosovic, Mukund Kabbe, Gonçalo Castelo-Branco (corresponding)"
published: 2021-04-12
ingested: 2026-05-18
ingest_depth: abstract+intro
doi: "10.1038/s41587-021-00869-9"
journal: "Nature Biotechnology"
tags: [scCUT&Tag, histone-modifications, transcription-factors, droplet, CUT&Tag, OLIG2, RAD21, Castelo-Branco-lab]
entities: []
concepts:
  - "[[30-Concepts/cut-and-tag]]"
  - "[[40-Topics/histone-modifications]]"
  - "[[30-Concepts/transcription-factor-motif]]"
topics:
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Bartosovic et al. (2021) — *scCUT&Tag: single-cell CUT&Tag for histone modifications + TFs in tissue* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-021-00869-9)

# Bartosovic et al. 2021 — single-cell CUT&Tag

> Thesis: while scRNA-seq and scATAC-seq scaled to tens-of-thousands of cells, **single-cell histone-modification profiling** lagged in sensitivity and throughput. Bartosovic et al. combine **CUT&Tag chemistry with droplet-based single-cell library prep**, producing high-quality scCUT&Tag profiles for active marks (H3K4me3, H3K27ac, H3K36me3), repressive marks (H3K27me3), and even individual transcription factors (OLIG2) and cohesin (RAD21) in the mouse CNS.

## Key claims (abstract + intro)

- **scCUT&Tag** = CUT&Tag + 10x Chromium droplet barcoding. Compatible with low-input nuclei (no flow sorting needed).
- Applied to **tens of thousands of mouse CNS cells**; recovers cell identity from histone-mark profiles alone — no scRNA-seq needed.
- **Profiled marks**: H3K4me3 (active promoters), H3K27ac (active enhancers), H3K36me3 (gene bodies), H3K27me3 (Polycomb repression).
- **Regulatory principles deconvoluted**: promoter bivalency, H3K4me3 spreading, promoter-enhancer connectivity — all from single-cell data.
- **TF mapping**: OLIG2 (oligodendrocyte master TF) and RAD21 (cohesin) chromatin occupancy at single-cell resolution.

## Why this matters

Founding paper of the **scalable single-cell CUT&Tag** lineage. Predecessor to nano-CUT&Tag (Bartosovic 2022) and sciCUT&Tag (Janssens 2023). Anchors the histone-modification single-cell axis alongside scChIC-seq (Ku 2019), scChIX-seq (Yeung 2023), and the methylation-mark joint readouts (scEpi²-seq).

## Note on ingest depth

Abstract + intro only; full PDF re-ingest will deepen comparison vs bulk CUT&Tag and the regulatory-principle deconvolution figures.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-021-00869-9) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33846645/)

## Related

- [[30-Concepts/cut-and-tag]] · [[40-Topics/histone-modifications]] · [[30-Concepts/transcription-factor-motif]]
- [[10-Summaries/bartosovic-2022-nano-cut-tag]] · [[10-Summaries/janssens-2023-scicut-tag]] · [[10-Summaries/ku-2019-scchic-seq]] · [[10-Summaries/yeung-2023-scchix-seq]]
- [[40-Topics/chromatin-architecture]] · [[40-Topics/histone-modifications]]
