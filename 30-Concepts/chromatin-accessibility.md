---
type: concept
title: Chromatin accessibility
aliases: [open chromatin, chromatin openness]
tags: [chromatin, regulation]
created: 2026-05-07
updated: 2026-05-07
---

# Chromatin accessibility

> Whether a region of DNA is "open" (free of nucleosomes, available for TF binding and transcription machinery) or "closed" (wrapped in nucleosomes / heterochromatin) — a regulatory readout that varies by cell type, cell state, and (per [[daf-seq]]) per fiber within a cell.

## Definition

The operational definition depends on the assay. ATAC-seq / DNase-seq measure accessibility as susceptibility to Tn5 transposase or DNase I cleavage in *bulk*, producing peaks where many cells have open chromatin at that locus. Single-cell ATAC-seq (scATAC-seq) generalizes to a per-cell binary or count matrix per peak. Single-molecule footprinting ([[fiber-seq]], [[daf-seq]]) refines further to a per-fiber occupancy pattern, distinguishing nucleosome-protected from TF-protected from fully-accessible bases.

## Why it matters

Accessibility is the most upstream measurable consequence of regulatory state. Mutations that do not change DNA sequence in coding regions can still drive disease by altering accessibility — see the [[jak2-v617f]] cell-intrinsic chromatin priming finding in [[10-Summaries/franco-2024-nature]] and the rs2280838 SLC39A4 nucleosome-positioning eQTL in [[10-Summaries/elliott-2025-naturebiotechnology]].

In single-cell genomics, accessibility complements RNA: it captures regulatory potential before transcription, and it captures it for non-coding regions that scRNA-seq does not see.

## Variants and refinements

- **Bulk ATAC-seq / DNase-seq** — population-averaged accessibility peaks.
- **Single-cell ATAC-seq** — per-cell peak occupancy; powers cell-type identification and differential accessibility analysis. The base layer of [[got-cha]] ([[10-Summaries/franco-2024-nature]]).
- **Single-molecule footprinting** ([[daf-seq]], [[fiber-seq]]) — per-fiber, per-base accessibility plus protein occupancy patterns; resolves what bulk and single-cell assays smear together.
- **[[chromatin-actuation]]** — DAF-seq's term for an element being in the "open + bound" state on a specific fiber; a per-fiber refinement of accessibility.

## Contested points

- Tn5-based assays under-call accessibility at GC-rich regions and have well-known tagmentation biases; long-read footprinting methods do not share these biases but have their own (sequence-context biases of the methylating/deaminating enzyme).
- "Accessible peak" calls in scATAC-seq are often binarized at thresholds that hide quantitative differences observed in single-molecule data.

## Examples

- JAK2V617F-mutant HSCs show increased accessibility at NF-κB target genes (TRAPPC9), TGF-β receptor BMPR1B, and matrix-remodeling MMP15 ([[10-Summaries/franco-2024-nature]]).
- The SLC39A4 promoter has distinct chromatin epialleles in liver vs lymphoblastoid cells, and the rs2280838-T variant biases the actuation state ([[10-Summaries/elliott-2025-naturebiotechnology]]).

## Related

- [[chromatin-actuation]]
- [[fiber-seq]]
- [[daf-seq]]
- [[got-cha]]
- [[single-molecule-footprinting]]
- [[40-Topics/chromatin-architecture]]
