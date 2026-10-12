---
type: concept
title: MulTI-Tag
aliases: [multiple target identification by tagmentation]
tags: [CUT&Tag, single-cell, multi-modal, Henikoff-lab]
created: 2026-05-12
updated: 2026-10-12
---

# MulTI-Tag

> A multi-epitope per-cell CUT&Tag variant from the Henikoff lab. Profiles several chromatin marks within the same single cell by loading different antibody-barcoded pA-Tn5 complexes ([[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]).

> [!abstract] 한눈에
> MulTI-Tag는 epitope마다 다른 barcode를 실은 pA-Tn5를 써서 한 세포 안에서 여러 histone mark를 동시에 측정하는 CUT&Tag 변형이다. hESC 삼배엽 분화를 H3K4me1-2-3과 H3K27me3를 같은 세포에서 함께 읽어 구분하는 데 쓰였다 ([[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]).

## Definition

Each chromatin epitope has its own pA-Tn5 transposome loaded with a distinct mosaic-end barcode. After single-cell partitioning, reads are demultiplexed by their epitope-specific barcode. Combinatorial indexing on the sciCUT&Tag scaffold provides the per-cell partitioning.

## Why it matters

Enables joint multi-mark single-cell chromatin profiling — a parallel approach to scChIX-seq's computational deconvolution.

## Examples

- Used to resolve human embryonic stem cell trilineage differentiation (endoderm/mesoderm/neuroectoderm) by combining H3K4me1-2-3 and H3K27me3 within the same cells ([[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — pA-Tn5 tagmentation at antibody-bound chromatin.
> - `concept` [[30-Concepts/scicut-tag|sciCUT&Tag]] — Combinatorial-indexing scaffold that MulTI-Tag runs on.
> - `concept` [[30-Concepts/scchix-seq|scChIX-seq]] — Multi-mark profiling by computational deconvolution instead of barcoding.
> - `entity` [[20-Entities/steven-henikoff|Steven Henikoff]] — Lab that developed the CUT&-family methods.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone marks and how they are profiled.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]
