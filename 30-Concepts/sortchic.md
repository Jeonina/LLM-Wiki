---
type: concept
title: sortChIC
aliases: [FACS-sorted ChIC]
tags: [histone-modifications, single-cell, MNase, FACS, van-Oudenaarden-lab]
created: 2026-05-12
updated: 2026-10-12
---

# sortChIC

> A single-cell histone-modification profiling method from the van Oudenaarden lab that combines pA-MNase + antibody binding with FACS sorting into 384-well plates. Designed for integration with cell-cycle reporters (FUCCI) and fluorescent labels ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).

> [!abstract] 한눈에
> sortChIC은 항체에 pA-MNase를 붙여 histone mark 위치를 자르고, 세포를 FACS로 plate에 하나씩 분류해 형광 정보까지 함께 남기는 single-cell histone 방법이다. 같은 depth에서 OneCell CUT&Tag와 비슷한 read 수와 FrIP를 보였지만 여전히 10,000개 이상의 input 세포가 필요하다 ([[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]).

## Definition

Workflow: bind antibody to histone mark in suspension → recruit pA-MNase → FACS sort single cells into plates (capturing fluorescence metadata) → MNase activation → adaptor ligation → IVT/PCR ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).

## Why it matters

- FACS compatibility enables integration with cell-cycle reporters (FUCCI), CellTrace dyes (intestinal anteroposterior axis labeling), and other fluorescent metadata that droplet platforms cannot capture ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).
- Substrate for [[30-Concepts/scchix-seq]] (two marks per cell) and [[30-Concepts/scepi2-seq]] (mark + 5mC per cell; [[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).

## Examples

- Mouse intestine epithelial vs immune lineage profiling with anteroposterior CellTrace labeling ([[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]).
- In a depth-equalized benchmark on MDA-MB-468 H3K27me3 (38,716 reads/cell), sortChIC gave 20,581 median unique reads/cell and FrIP 0.79, close to OneCell CUT&Tag (26,008; 0.77) and well above scChIP-seq (5,722) and 10x droplet scCUT&Tag (5,156). sortChIC still requires ≥10,000 input cells ([[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/chic-seq|ChIC-seq]] — The original antibody-tethered MNase cleavage method.
> - `concept` [[30-Concepts/scchic-seq|scChIC-seq]] — Single-cell histone profiling with an antibody–MNase complex.
> - `concept` [[30-Concepts/scchix-seq|scChIX-seq]] — Two marks per cell during sortChIC, deconvolved computationally.
> - `concept` [[30-Concepts/scepi2-seq|scEpi²-seq]] — Histone mark, 5mC and nucleosome positioning from one cell.
> - `entity` [[20-Entities/alexander-van-oudenaarden|Alexander van Oudenaarden]] — Hubrecht Institute; developer of sortChIC and its descendants.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone PTMs and how single-cell methods read them.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]
> - [[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]
