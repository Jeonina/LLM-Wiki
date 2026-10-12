---
type: concept
title: Spatial Structure Capture Efficiency (SSCE)
aliases: [SSCE]
tags: [3D-genome, quality-control, single-cell-Hi-C, metric]
created: 2026-05-12
updated: 2026-10-12
---

# Spatial Structure Capture Efficiency (SSCE)

> A single-cell 3D-genome quality-control metric introduced in STARK that integrates TAD-boundary counts and A/B-compartment switches (normalized against inter-chromosomal and unattributable contacts) into a unified score ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

> [!abstract] 한눈에
> SSCE는 single-cell 3D genome 데이터에서 TAD 경계와 A/B compartment 전환을 얼마나 잡아냈는지를 하나의 점수로 묶은 QC 지표다. contact 수가 적어도 구조 정보가 풍부한 세포를 버리지 않게 해 준다 ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

## Definition

SSCE penalizes cells with few contacts but rewards cells whose contacts span informative structural features. Complements contact-count metrics that bias toward shallow-data cells ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

## Why it matters

Rescues "low-contact-count but high-structure-quality" cells that simple thresholding would discard. Important for sparse sc3DG-seq data where average contacts per cell can be <100k ([[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/stark|STARK]] — Unified sc3DG-seq analysis framework that introduced SSCE.
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — Methods that profile genome contacts in individual cells.
> - `concept` [[30-Concepts/topologically-associating-domain|TAD]] — Self-interacting genomic neighbourhood bounded by sharp contact drops.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Nuclear organization from territories to loops.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]
