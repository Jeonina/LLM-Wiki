---
type: concept
title: Joint single-cell multi-omics
aliases: [joint multi-omics, paired multi-omics, same-cell multi-modal]
tags: [single-cell, multiomics, paired-measurement]
created: 2026-05-19
updated: 2026-05-19
---

# Joint single-cell multi-omics

> Single-cell methods that measure two or more molecular modalities from the same individual cell (or nucleus) — as opposed to integrating mono-omic datasets computationally. The defining feature is *physical co-capture* of modalities within a single droplet, well, or fiber. See [[40-Topics/single-cell-multiomics]] for the methods landscape and [[10-Summaries/wang-2023-multimodal-review]] for the catalog.

## Definition

A joint multi-omic assay reads ≥2 of: DNA sequence, RNA, chromatin accessibility, DNA methylation, histone modifications, surface protein, intracellular protein, 3D contacts — within the same physical compartment. This contrasts with **integration of unpaired data** (matrix factorization, manifold alignment) which infers joint structure from separately-measured modalities ([[10-Summaries/wang-2023-multimodal-review]]).

## Why it matters

- Pairs cause and effect at single-cell resolution — e.g., does this mutation alter this cell's accessibility? Only joint measurement can answer.
- Avoids batch effects and clustering artifacts that confound unpaired integration ([[10-Summaries/heumos-2023-best-practices]]).

## Variants

- **Joint genome + transcriptome** — G&T-seq ([[10-Summaries/macaulay-2015-gt-seq]]), DR-seq ([[10-Summaries/dey-2015-dr-seq]]), GoT ([[10-Summaries/nam-2019-got]]).
- **Scalable droplet DNA + RNA** — DEFND-seq (whole-genome, nucleosome depletion + 10x Multiome, [[10-Summaries/olsen-2025-defnd-seq]]) and SDR-seq (targeted, Tapestri, low allelic dropout, [[10-Summaries/lindenhofer-2025-sdr-seq]]); these trade off **genome-wide breadth (high ADO)** vs **targeted depth (low ADO, per-cell zygosity)** ([[10-Summaries/lindenhofer-2025-sdr-seq]]).
- **Joint chromatin + transcriptome** — sci-CAR ([[10-Summaries/cao-2018-sci-car]]), SHARE-seq ([[10-Summaries/ma-2020-share-seq]]).
- **Joint methylation + chromatin + RNA** — scNMT-seq ([[10-Summaries/clark-2018-scnmt-seq]]).
- **Joint mutation + chromatin + RNA** — Duplex-Multiome ([[10-Summaries/kriz-2025-duplex-multiome]]).

## Related

- [[40-Topics/single-cell-multiomics]] · [[30-Concepts/single-cell-multiomics]] · [[30-Concepts/defnd-seq]] · [[30-Concepts/sdr-seq]] · [[30-Concepts/allele-dropout]] · [[50-Notes/regulatory-layers-overview]] · [[50-Notes/droplet-vs-single-molecule-scdna]]
