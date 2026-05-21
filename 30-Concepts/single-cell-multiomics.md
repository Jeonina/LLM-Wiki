---
type: concept
title: Single-cell multi-omics
aliases: [single-cell multiomics, multimodal omics, sc-multiomics]
tags: [single-cell, multi-omics, methods]
created: 2026-05-11
updated: 2026-05-11
---

# Single-cell multi-omics

> Measurement of two or more molecular modalities — transcriptome, genome, epigenome, proteome, metabolome, spatial — from the same single cell. The maturing axis of single-cell biology: most modality *pairs* (and some triples) are now technically feasible, and computational integration has become the dominant bottleneck.

## Definition

Two organizing axes ([[10-Summaries/baysoy-2023-multiomics-landscape]], [[10-Summaries/vandereyken-2023-scmultiomics-review]]):

**1. By modality pair**:
- scRNA + scATAC (10x Multiome, SHARE-seq).
- scRNA + protein (CITE-seq, REAP-seq) — see [[cite-seq]].
- scDNA + scRNA (G&T-seq — see [[gt-seq]], DR-seq, SIDR-seq, DNTR-seq).
- scRNA + methylome (scM&T-seq, snmCT-seq).
- CRISPR-perturbed scRNA (Perturb-seq, CROP-seq).
- scDNA + scRNA + protein (DOGMA-seq variants) — see [[dogma-seq]].
- scDNA + scATAC + RNA + protein (GoT–ChA + DOGMA via imputation — [[10-Summaries/izzo-2024-got-cha]]).

**2. By when modalities are uncoupled**:
- Before library prep — physical separation (G&T-seq, SIDR-seq).
- During library prep — joint barcoding.
- After library prep — diagonal computational integration.

## Why it matters

- Lets the same cell answer multiple questions at once: "what is this cell's genotype, and what does it express?"
- Provides the **phenotypic association** capability of [[scdna-capabilities-framework]].
- Cell-type atlases (Human Cell Atlas) and disease atlases are increasingly multi-omic by default.

## Variants and refinements

- **Spatial multi-omics** — preserves tissue context. Imaging-based (MERFISH, seqFISH, in situ) vs NGS-based (Visium, Slide-seq, Stereo-seq).
- **Multi-omic best practices** documented in [[10-Summaries/heumos-2023-best-practices]] — modality-specific QC and integration recommendations.

## Contested points

- Cost-per-cell scaling: multi-omic methods are substantially more expensive than unimodal at equal cell number.
- Integration accuracy across diagonal (different cells, different modalities) approaches is hard to benchmark.

## Examples

- [[10-Summaries/nam-2019-got]] — scDNA + scRNA via amplicon spike-in on 10x ([[got]]).
- [[10-Summaries/izzo-2024-got-cha]] — scDNA + scATAC + RNA + protein via gDNA capture + imputation bridges.
- [[10-Summaries/swanson-2025-daf-seq]] — sequence + chromatin via deaminase footprinting on the same fiber.

## Related

- [[got]], [[got-cha]], [[daf-seq]]
- [[cite-seq]]
- [[gt-seq]]
- [[dogma-seq]]
- [[spatial-multiomics]]
- [[40-Topics/single-cell-multiomics]]
