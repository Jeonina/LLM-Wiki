---
type: summary
title: "SHARE-seq reveals chromatin potential (NRG perspective on Ma et al. 2020)"
aliases: [SHARE-seq perspective, Clyde 2020 NRG SHARE-seq, Ma 2020 SHARE-seq]
tags: [share-seq, single-cell-multiomics, atac-seq, scRNA-seq, joint-assay, split-pool, chromatin-potential]
created: 2026-05-12
updated: 2026-05-12
sources: ["00-Sources/papers/SHARE-seq reveals chromatin potential - Nature Reviews Genetics.md"]
---

# SHARE-seq reveals chromatin potential — Dorothy Clyde, *Nature Reviews Genetics* (Nov 2020)

> Nature Reviews Genetics Research Highlight on Ma S. et al., *Cell* **183**, 1103–1116 (2020) — "Chromatin potential identified by shared single-cell profiling of RNA and chromatin." NRG version: https://www.nature.com/articles/s41576-020-00308-6.

## Thesis

**SHARE-seq** (Simultaneous High-throughput ATAC and RNA Expression with sequencing) is a high-throughput joint single-cell assay for chromatin accessibility + transcription in the same cell. The conceptual payoff is the **chromatin potential** framework: a cell's future transcriptional state can be inferred from its current chromatin accessibility profile at lineage-specifying loci, enabling lineage-fate prediction from chromatin alone.

## Method (one-paragraph mechanism)

Built on the **SPLiT-seq / Paired-seq split-pool barcoding** logic. Cells are fixed and permeabilized, accessible chromatin is tagged by Tn5 transposition, and mRNA is reverse-transcribed to cDNA — both in the same cell. The cells are then run through three rounds of 96-well split-pool barcoding, so each cell is exposed to a unique trio of barcodes out of 96³ combinations. Chromatin and mRNA reads from the same cell pair through the shared barcode trio after pooled sequencing. Scaling is trivial: more rounds of barcoding → more cells uniquely labeled.

## Key claims

1. **Throughput**: 34,774 high-quality paired (chromatin, RNA) profiles from a single adult mouse skin sample.
2. **DORCs (Domains of Regulatory Chromatin)**: regions with high density of peak-to-gene associations identified by covariance across paired profiles. DORCs are enriched for lineage-specifying genes and overlap known super-enhancers.
3. **Chromatin potential**: in hair follicle differentiation, **chromatin accessibility at DORCs precedes target gene expression** in time. The chromatin state can be used to compute the most likely future expression state of a cell — its "potential" lineage choice.
4. **Compatibility**: works with single cells, single nuclei, multiple mouse + human cell lines and tissues.

## Surprising / load-bearing

- The "DORC chromatin opens before gene expression" finding is a single-cell, time-resolved version of the long-suspected idea that accessibility is a permissive precondition for transcription. SHARE-seq is the first method to demonstrate it at the resolution needed to compute a cell-specific potential.
- For this wiki's DNA-centric review framing: SHARE-seq is methodologically a **scATAC + scRNA** assay (it does not directly measure DNA sequence variants). It belongs in §4.6 joint-assay coverage as the scaling-by-split-pool exemplar — analogous in throughput class to [[10-Summaries/joint-profiling-of-chromatin-accessibility-and-gene-expression-in-thousands-of-single-cells]] (sci-CAR), but uses split-pool barcoding rather than combinatorial-indexing wells.

## Entities / concepts touched

[[chromatin-accessibility]] · [[atac-seq]] · [[scatac-seq]] · [[tn5-tagmentation]] · [[combinatorial-indexing]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/chromatin-architecture]]

## Related summaries

- [[joint-profiling-of-chromatin-accessibility-and-gene-expression-in-thousands-of-single-cells]] — sci-CAR, the combinatorial-indexing equivalent.
- [[scnmt-seq-enables-joint-profiling-of-chromatin-accessibility-dna-methylation-and-transcription-in-single-cells]] — scNMT-seq, lower-throughput but three-modality.

## Related

- [[40-Topics/single-cell-multiomics]]
- This is a perspective/research-highlight summary; the primary Ma et al. *Cell* 2020 paper is not yet in this wiki's sources.
