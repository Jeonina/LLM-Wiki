---
type: summary
title: "Vandereyken et al. 2023 — Methods and applications for single-cell and spatial multi-omics"
source: "[[00-Sources/papers/Katy_2023_NatureReviewsGenetics]]"
source_kind: paper
author: "Katy Vandereyken, Alejandro Sifrim, Bernard Thienpont, Thierry Voet"
published: 2023-08
ingested: 2026-05-11
doi: "10.1038/s41576-023-00580-2"
journal: "Nature Reviews Genetics 24:494–515"
tags: [review, multi-omics, scDNA-scRNA, spatial-omics, KU-Leuven]
entities:
  - "[[20-Entities/thierry-voet]]"
concepts:
  - "[[30-Concepts/single-cell-multiomics]]"
  - "[[30-Concepts/gt-seq]]"
  - "[[30-Concepts/scdna-seq]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
---

**Citation:** Vandereyken et al. (2023) — *Methods and applications for single-cell and spatial multi-omics* — *Nature Reviews Genetics*. [DOI](https://doi.org/10.1038/s41576-023-00580-2)

# Vandereyken et al. 2023 — Methods and applications for single-cell and spatial multi-omics

> Thesis: single-cell multi-omics methods can be organized by *when* the molecular analytes are uncoupled — before, during, or after library preparation — and this organizing principle reveals the underlying design space. Spatial multi-omics is a parallel field with both NGS-based and imaging-based approaches. Data integration across modalities is the remaining computational challenge.

## Key claims

- **Four organizing principles** for multi-omic methods:
  - Physical separation of analytes before sequencing (e.g., G&T-seq separates polyA RNA and gDNA via oligo-dT beads).
  - Nuclear-cytosolic partitioning (SIDR-seq, DNTR-seq).
  - Pre-amplification + split (DR-seq).
  - Targeted enrichment within combined library.
- **G&T-seq family** (G&T-seq, scONE-seq, scDNA + scRNA): polyA RNA isolated on beads, gDNA in supernatant; both processed independently. Compatible with MDA, PCR, DA-PCR for WGA and Smart-seq2 for transcriptome.
- **Tn5-based scDNA + scRNA methods** (DNTR-seq) skip the WGA step by directly tagmenting nuclear DNA — circumventing WGA artifacts entirely at the cost of lower coverage breadth.
- **Spatial multi-omics**: NGS-based (Slide-seq, Visium, Stereo-seq, DBiT-seq) tag mRNA / DNA / protein with positional barcodes; imaging-based (MERFISH, seqFISH, in situ sequencing) read transcripts in their native location through sequential hybridization.
- **Integration computational toolkit**: vertical (same cells, paired modalities), horizontal (different samples, same modality), diagonal (different cells, different modalities) integration. Anchor-based (Seurat WNN), latent-space (MOFA, totalVI), graph-based (Conos).

## Methods / evidence

Methodological review from KU Leuven (Voet lab — co-developer of G&T-seq). Heavily protocol-focused with supplementary figures for each method.

## Surprising or load-bearing bits

- **The before/during/after-library-prep organizing axis** is a clearer way to think about multi-omic chemistry than the modality-pair axis Alev 2023 uses. It reveals why physical-separation methods (G&T-seq family) are mature while diagonal-integration methods rely on computational bridges.
- **Skipping WGA entirely** (DNTR-seq) is a genuine architectural alternative that trades coverage for accuracy — same tradeoff space as [[got-cha]]'s switch from cDNA to gDNA capture.
- **Spatial multi-omics maturity**: at writing, NGS-based and imaging-based approaches were complementary; by 2025 they remain so, with no convergence on a single architecture.

## Entities mentioned

- [[20-Entities/thierry-voet]] — senior author; KU Leuven; co-developer of G&T-seq.

## Concepts touched

- [[30-Concepts/single-cell-multiomics]]
- [[30-Concepts/gt-seq]] — G&T-seq method.
- [[30-Concepts/scdna-seq]] — covered in the multi-omic context.

## Connections to other sources

- **Complementary to** [[10-Summaries/alev-2023-naturereviewsmolecularcellbiology]] — same year, parallel reviews of single-cell multi-omics with different organizing principles (Katy: chemistry-axis; Alev: modality-axis).
- **Method-level reference for** [[10-Summaries/franco-2024-nature]] (GoT–ChA + DOGMA), [[10-Summaries/anna-2019-nature]] (GoT), [[10-Summaries/elliott-2025-naturebiotechnology]] (DAF-seq).
- **Spatial omics coverage links to** the spatial sub-field that this vault has not yet ingested primary sources on.

## Open questions

- How to scale plate-based G&T-seq family to thousands of cells (microfluidic on-chip approaches are noted as in development).
- Integration accuracy benchmarking — diagonal integration is computationally demanding and produces results that are hard to validate.
- When to skip WGA (DNTR-seq style) vs. perform it — application-dependent, not yet a consensus heuristic.

---
**Source:** [DOI](https://doi.org/10.1038/s41576-023-00580-2)
