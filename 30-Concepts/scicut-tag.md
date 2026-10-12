---
type: concept
title: sciCUT&Tag
aliases: [single-cell combinatorial indexing CUT&Tag]
tags: [CUT&Tag, single-cell, combinatorial-indexing, Henikoff-lab, ICELL8]
created: 2026-05-12
updated: 2026-10-12
---

# sciCUT&Tag

> A combinatorial-indexing variant of CUT&Tag that combines barcoded pA-Tn5 tagmentation (96 wells, first index) with ICELL8 5,184-nanowell PCR (second index) to profile ~40,000 cells per chip at ~$0.11/cell ([[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]).

> [!abstract] 한눈에
> sciCUT&Tag는 barcoded pA-Tn5 tagmentation과 ICELL8 nanowell PCR을 겹쳐 chip 하나에서 약 40,000개 세포의 histone mark를 읽는 combinatorial indexing 방식이다 ([[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]). droplet 기반 scCUT&Tag보다 세포당 비용이 낮고 세포당 unique read가 많다 ([[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]).

## Definition

Workflow: lightly cross-link nuclei → bind to WGA-magnetic beads → bulk primary + secondary antibody → array in 96-well plate with differentially barcoded pA-Tn5 → tagmentation → pool → dispense on ICELL8 at 12–24 cells/nanowell → PCR with second barcode → sequencing. SNP-based collision removal optional via multi-donor mixing.

## Why it matters

- ~8× cost reduction vs droplet-based scCUT&Tag.
- ~2× the unique reads/cell of original scCUT&Tag (2,116 vs 1,110 median reads for H3K27me3 in PBMCs).
- Underlying platform for **MulTI-Tag** (multi-target identification by tagmentation) — multi-epitope per cell.

## Examples

- Mixed-donor PBMC H3K4me1-2-3 and H3K27me3 profiling, with SNP-based collision QC ([[10-Summaries/janssens-2023-scicut-tag]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — Antibody-tethered pA-Tn5 tagmentation of chromatin targets.
> - `concept` [[30-Concepts/combinatorial-indexing|Combinatorial indexing]] — Split-pool barcoding that labels cells without physical isolation.
> - `concept` [[30-Concepts/multi-tag|MulTI-Tag]] — Multi-target identification by tagmentation, built on sciCUT&Tag.
> - `concept` [[30-Concepts/icell8-nanowell|ICELL8 nanowell]] — 5,184-nanowell chip that supplies the second index.
> - `entity` [[20-Entities/steven-henikoff|Steven Henikoff]] — Corresponding author; Henikoff lab developed CUT&Tag.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Single-cell profiling of histone marks.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]
