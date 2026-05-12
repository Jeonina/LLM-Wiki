---
type: concept
title: MulTI-Tag
aliases: [multiple target identification by tagmentation]
tags: [CUT&Tag, single-cell, multi-modal, Henikoff-lab]
created: 2026-05-12
updated: 2026-05-12
---

# MulTI-Tag

> A multi-epitope per-cell CUT&Tag variant from the Henikoff lab. Profiles several chromatin marks within the same single cell by loading different antibody-barcoded pA-Tn5 complexes.

## Definition

Each chromatin epitope has its own pA-Tn5 transposome loaded with a distinct mosaic-end barcode. After single-cell partitioning, reads are demultiplexed by their epitope-specific barcode. Combinatorial indexing on the sciCUT&Tag scaffold provides the per-cell partitioning.

## Why it matters

Enables joint multi-mark single-cell chromatin profiling — a parallel approach to scChIX-seq's computational deconvolution.

## Examples

- Used to resolve human embryonic stem cell trilineage differentiation (endoderm/mesoderm/neuroectoderm) by combining H3K4me1-2-3 and H3K27me3 within the same cells ([[10-Summaries/scalable-single-cell-profiling-of-chromatin-modifications-with-scicut-tag]]).

## Related

- [[30-Concepts/cut-and-tag]] · [[30-Concepts/scicut-tag]] · [[30-Concepts/scchix-seq]] · [[40-Topics/histone-modifications]] · [[20-Entities/steven-henikoff]]
