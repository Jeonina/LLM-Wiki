---
type: concept
title: Chromatin accessibility
aliases: [open chromatin, chromatin openness]
tags: [chromatin, regulation]
created: 2026-05-07
updated: 2026-05-19
---

# Chromatin accessibility

> Whether a region of DNA is "open" (free of nucleosomes, available for TF binding and transcription machinery) or "closed" (wrapped in nucleosomes / heterochromatin) — a regulatory readout that varies by cell type ([[10-Summaries/buenrostro-2015-nature]]), cell state, and (per [[10-Summaries/swanson-2025-daf-seq|DAF-seq]]) per fiber within a cell.

## Definition

The operational definition depends on the assay. ATAC-seq / DNase-seq measure accessibility as susceptibility to Tn5 transposase or DNase I cleavage in *bulk*, producing peaks where many cells have open chromatin at that locus ([[10-Summaries/buenrostro-2015-nature]]). Single-cell ATAC-seq (scATAC-seq) generalizes to a per-cell binary or count matrix per peak ([[10-Summaries/buenrostro-2015-nature]]; [[10-Summaries/cusanovich-2015-sciatac]]). Single-molecule footprinting ([[10-Summaries/andrewc-2020-science|Fiber-seq]]; [[10-Summaries/swanson-2025-daf-seq|DAF-seq]]) refines further to a per-fiber occupancy pattern, distinguishing nucleosome-protected from TF-protected from fully-accessible bases.

## Why it matters

Accessibility is the most upstream measurable consequence of regulatory state. Mutations that do not change DNA sequence in coding regions can still drive disease by altering accessibility — see the [[jak2-v617f]] cell-intrinsic chromatin priming finding in [[10-Summaries/izzo-2024-got-cha]] and the rs2280838 SLC39A4 nucleosome-positioning eQTL in [[10-Summaries/swanson-2025-daf-seq]].

In single-cell genomics, accessibility complements RNA: it captures regulatory potential before transcription, and it captures it for non-coding regions that scRNA-seq does not see ([[10-Summaries/cao-2018-sci-car]]; [[10-Summaries/ma-2020-share-seq]]).

## Variants and refinements

- **Bulk ATAC-seq / DNase-seq** — population-averaged accessibility peaks ([[10-Summaries/buenrostro-2015-nature]]).
- **Single-cell ATAC-seq** — per-cell peak occupancy; powers cell-type identification and differential accessibility analysis ([[10-Summaries/buenrostro-2015-nature]]; [[10-Summaries/cusanovich-2015-sciatac]]). The base layer of [[got-cha]] ([[10-Summaries/izzo-2024-got-cha]]).
- **Single-molecule footprinting** ([[daf-seq]], [[fiber-seq]]) — per-fiber, per-base accessibility plus protein occupancy patterns; resolves what bulk and single-cell assays smear together ([[10-Summaries/andrewc-2020-science]]; [[10-Summaries/swanson-2025-daf-seq]]).
- **[[chromatin-actuation]]** — DAF-seq's term for an element being in the "open + bound" state on a specific fiber; a per-fiber refinement of accessibility ([[10-Summaries/swanson-2025-daf-seq]]).
- **TF-associated accessibility deviation** — chromVAR aggregates scATAC peaks by TF motif to extract motif-level accessibility signal from sparse single-cell data ([[10-Summaries/schep-2017-chromvar]]).

## Contested points

- Tn5-based assays under-call accessibility at GC-rich regions and have well-known tagmentation biases (synthesis — Tn5 sequence preference is broadly acknowledged in scATAC tooling, e.g. [[10-Summaries/schep-2017-chromvar]]); long-read footprinting methods do not share these biases but have their own — m6A methyltransferase sequence preference for Fiber-seq ([[10-Summaries/andrewc-2020-science]]) and cytidine deaminase context bias for DAF-seq ([[10-Summaries/swanson-2025-daf-seq]]).
- "Accessible peak" calls in scATAC-seq are often binarized at thresholds that hide quantitative differences observed in single-molecule data ([[10-Summaries/swanson-2025-daf-seq]] vs [[10-Summaries/buenrostro-2015-nature]]).
- ~61% intra-cell haplotype divergence in actuation state ≈ ~63% inter-cell divergence ([[10-Summaries/swanson-2025-daf-seq]]) — suggests per-fiber stochasticity rather than per-cell programs.

## Examples

- JAK2V617F-mutant HSCs show increased accessibility at NF-κB target genes (TRAPPC9), TGF-β receptor BMPR1B, and matrix-remodeling MMP15 ([[10-Summaries/izzo-2024-got-cha]]).
- The SLC39A4 promoter has distinct chromatin epialleles in liver vs lymphoblastoid cells, and the rs2280838-T variant biases the actuation state ([[10-Summaries/swanson-2025-daf-seq]]).
- Chromatin potential — accessibility precedes transcription during differentiation, predicting cell-fate decisions in keratinocytes ([[10-Summaries/ma-2020-share-seq]]).

## Related

- [[chromatin-actuation]]
- [[fiber-seq]]
- [[daf-seq]]
- [[got-cha]]
- [[single-molecule-footprinting]]
- [[40-Topics/chromatin-architecture]]
- [[50-Notes/regulatory-layers-overview]] — accessibility as one of the four molecular regulatory layers
