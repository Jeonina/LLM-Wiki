---
type: concept
title: STARK
aliases: [Structural Topology Analysis and Rich Knowledge base]
tags: [3D-genome, software, single-cell-Hi-C, pipeline]
created: 2026-05-12
updated: 2026-10-12
---

# STARK

> A unified analysis framework (Jiang et al. 2026) for single-cell 3D-genome sequencing data. Three modules: Preprocess (alignment, demultiplexing, .cool generation), Cell QC (EmptyCells filtering, GiniQC, SSCE metric), and Downstream Analysis (imputation, clustering, A/B compartments, TADs, loops, 3D reconstruction) ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

> [!abstract] 한눈에
> STARK는 15종 이상의 sc3DG-seq 기술을 하나의 pipeline으로 처리하는 분석 framework로, 전처리·세포 QC·downstream 분석의 세 모듈로 이뤄진다. 균일하게 처리한 데이터 저장소 scNucleome과 함께 나와 연구 간 비교를 가능하게 한다 ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

## Definition

Handles 15+ sc3DG-seq technologies in a single pipeline. Introduces EmptyCells (Monte-Carlo-based barcode filtering) and SSCE (Spatial Structure Capture Efficiency) as novel QC metrics ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

## Why it matters

Eliminates the per-method data-processing fragmentation that has hampered cross-study sc3DG-seq comparisons. Paired with **scNucleome**, a public repository of uniformly processed sc3DG-seq datasets ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

## Examples

- Jiang et al. benchmark 15 sc3DG-seq technologies under STARK ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — Methods that profile genome contacts in individual cells.
> - `concept` [[30-Concepts/empty-cells-algorithm|EmptyCells algorithm]] — Separates real-cell barcodes from empty or low-quality ones.
> - `concept` [[30-Concepts/sscce|SSCE]] — QC score for how much TAD and compartment structure a cell captures.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Nuclear organization from territories to loops.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]
