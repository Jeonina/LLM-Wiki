---
type: concept
title: EmptyCells algorithm
aliases: []
tags: [3D-genome, quality-control, single-cell, barcode-filtering]
created: 2026-05-12
updated: 2026-10-12
---

# EmptyCells algorithm

> A filtering algorithm for sc3DG-seq data that distinguishes barcodes corresponding to real cells from empty-droplet or low-quality barcodes, using Monte Carlo simulation against an empty-barcode null distribution ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

> [!abstract] 한눈에
> EmptyCells는 STARK의 cell QC 단계에서 contact 수와 Monte Carlo로 만든 빈 barcode null 분포를 비교해, 고처리량 sc3DG-seq의 barcode 중 실제 세포만 골라내는 알고리즘이다. scRNA-seq의 EmptyDrops와 같은 역할을 한다 ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

## Definition

Analogous to the EmptyDrops algorithm in scRNA-seq. Filters cells based on contact count + statistical separation from an empty-barcode null model ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

## Why it matters

Critical first-pass QC for high-throughput sc3DG-seq experiments where many barcodes contain little signal.

## Related

> [!cards]
> - `concept` [[30-Concepts/stark|STARK]] — Unified analysis framework for single-cell 3D-genome data; EmptyCells sits in its Cell QC module.
> - `concept` [[30-Concepts/sscce|SSCE]] — STARK's structural QC metric combining TAD-boundary and compartment-switch signals.
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — The family of methods that profile genome-wide chromatin contacts in single cells.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromosome territories, compartments, TADs and loops inside the nucleus.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]
