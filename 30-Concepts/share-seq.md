---
type: concept
title: SHARE-seq
aliases: [SHARE-seq, simultaneous high-throughput ATAC and RNA expression]
tags: [joint-assay, single-cell-multiomics, split-pool, scATAC-seq, scRNA-seq, method]
created: 2026-05-12
updated: 2026-05-12
---

# SHARE-seq

> Split-pool-based joint assay for chromatin accessibility + transcription in tens of thousands of single cells. Built from SPLiT-seq / Paired-seq logic, scales by adding barcoding rounds rather than wells.

## Definition

Ma et al. 2020 (*Cell* 183, 1103) developed SHARE-seq as a high-throughput alternative to sci-CAR. Fixed, permeabilized cells undergo Tn5 tagmentation (chromatin) and reverse transcription (mRNA) in the same tube, then three rounds of 96-well split-pool barcoding give each cell a unique trio of barcodes from 96³ = 884,736 possible combinations. Wiki summary based on the *Nature Reviews Genetics* perspective: [[10-Summaries/ma-2020-share-seq]].

## Why it matters

- **Throughput**: 34,774 high-quality paired profiles from a single adult mouse skin sample. Scales further by adding split-pool rounds.
- **Chromatin potential**: introduces the concept of **DORCs (Domains of Regulatory Chromatin)** — regions with high density of peak-to-gene associations, enriched for lineage-specifying genes, overlapping super-enhancers. Chromatin accessibility at DORCs **precedes** target gene expression in hair-follicle differentiation, so chromatin state predicts future expression — a cell's "potential" lineage choice.
- Compatible with fixed cells, fresh cells, and nuclei.

## Variants and refinements

- **SHARE-seq** ([[10-Summaries/ma-2020-share-seq]]) — accessibility + RNA.
- Conceptual analog of [[sci-car|sci-CAR]] but with split-pool instead of combinatorial-indexing well plates.

## Contested points

- Sparsity of single-cell ATAC arm — same family of issues as sci-CAR.
- Chromatin potential is correlational over pseudotime; causal inference (does opening DORC chromatin *cause* later expression?) requires perturbation.

## Related

- [[sci-car]]
- [[chromatin-accessibility]]
- [[scatac-seq]]
- [[tn5-tagmentation]]
- [[combinatorial-indexing]]
- [[40-Topics/single-cell-multiomics]]
- [[40-Topics/single-cell-multiomics]]
