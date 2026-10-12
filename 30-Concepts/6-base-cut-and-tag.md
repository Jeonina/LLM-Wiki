---
type: concept
title: 6-base-CUT&Tag
aliases: [6B-C&T, biomodal 6-base CUT&Tag]
tags: [CUT&Tag, methylation, 5mC, 5hmC, histone-modifications, biomodal]
created: 2026-05-12
updated: 2026-10-12
---

# 6-base-CUT&Tag

> A bulk method that profiles **G/A/T/C + 5mC + 5hmC** at the DNA fragments tethered to a specific histone modification by CUT&Tag. Uses biomodal's enzymatic 6-base-seq conversion chemistry on hairpin-tagmented DNA ([[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]).

> [!abstract] 한눈에
> 6-base-CUT&Tag는 CUT&Tag로 특정 histone 표지에 묶인 DNA 조각만 골라 염기서열과 5mC·5hmC를 함께 읽는 bulk 방법이다. 전장 유전체 6-base-seq로는 너무 작은 분획이라 보이지 않던 enhancer 상태별 5mC/5hmC 차이를 드러낸다 ([[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]).

## Definition

Workflow: antibody-directed pA-Tn5 tagmentation with a uracil-containing hairpin mosaic-end adapter (ME2U) → USER digestion → 6-base-seq enzymatic conversion (biomodal duet evoC kit) → Illumina paired-end sequencing. Scar sequences from the digested hairpin identify valid double-tagmented (circularized) molecules ([[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]).

## Why it matters

Reveals 5mC and 5hmC distributions at **specific** chromatin states (active vs primed vs poised enhancers) at the fragment level — invisible to whole-genome 6-base-seq because the relevant histone-mark fraction is too small ([[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]).

## Examples

- mESCs: primed enhancers (H3K4me1-only) have highest 5mC (~13%) and 5hmC (~4%); active and poised enhancers have lower modifications. H3K4me1-derived 5mC/5hmC signatures classify enhancer functional states ([[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — Antibody-tethered pA-Tn5 tagmentation, the targeting step here.
> - `concept` [[30-Concepts/5hmc|5hmC]] — The oxidized cytosine read alongside 5mC.
> - `entity` [[20-Entities/biomodal|biomodal]] — Maker of the 6-base-seq conversion chemistry.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation biology and methylome methods.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone marks and how they are profiled.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]
