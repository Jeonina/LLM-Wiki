---
type: concept
title: scChIC-seq
aliases: [single-cell chromatin immunocleavage]
tags: [histone-modifications, single-cell, MNase, Zhao-lab]
created: 2026-05-12
updated: 2026-10-12
---

# scChIC-seq

> A single-cell histone-modification profiling method that uses an antibody-MNase fusion (covalent or pA-MNase + Ab complex) to cut chromatin at target sites, then **selectively PCR-amplifies the small target fragments** for sequencing ([[10-Summaries/ku-2019-scchic-seq|Ku 2019]]).

> [!abstract] 한눈에
> scChIC-seq는 antibody에 묶인 MNase로 histone mark 위치를 자르고 작은 target 조각만 선택적으로 PCR 증폭해, ChIP 없이 single cell의 histone modification을 읽는 방법이다 ([[10-Summaries/ku-2019-scchic-seq|Ku 2019]]). 한 번에 약 285개 세포만 다룰 수 있어 처리량이 낮다 ([[10-Summaries/ku-2019-scchic-seq|Ku 2019]]).

## Definition

Workflow: fix cells → bind antibody-MNase conjugate (or pA-MNase + Ab) → MNase digestion (Ca²⁺-triggered) → adaptor ligation → selective PCR amplification of short (target) fragments → size selection → sequencing.

## Why it matters

- Single-cell histone-modification profiling without ChIP. Avoids losses from immunoprecipitation ([[10-Summaries/ku-2019-scchic-seq|Ku 2019]]).
- Works with formaldehyde fixation (unlike CUT&RUN), and supports either covalent Ab-MNase or pA-MNase strategies ([[10-Summaries/ku-2019-scchic-seq|Ku 2019]]).
- Established the feasibility of single-cell chromatin-state profiling. Throughput ~285 cells/experiment ([[10-Summaries/ku-2019-scchic-seq|Ku 2019]]).

## Evidence and examples

- Human WBCs profiled for H3K4me3 → identifies T cells, B cells, NK cells, monocytes by chromatin state alone ([[10-Summaries/ku-2019-scchic-seq|Ku 2019]]).
- CoBATCH reported markedly more non-duplicated reads per cell, a higher mapping rate and less read redundancy than scChIC-seq, with slightly higher FRiP for scChIC-seq ([[10-Summaries/wang-2019-cobatch|CoBATCH]]).

## Contested points

- **The CoBATCH comparison is not like-for-like.** It set CoBATCH H3K27ac in 2,161 ESCs against scChIC-seq H3K4me3 in 281 white blood cells, and FRiP was computed differently in the two studies ([[10-Summaries/wang-2019-cobatch|CoBATCH]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/chic-seq|ChIC]] — The original 2004 antibody-tethered MNase method; ancestor of scChIC-seq.
> - `concept` [[30-Concepts/cut-and-run|CUT&RUN]] — pA-MNase tethered by antibody, with Ca²⁺-triggered release of target fragments.
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — pA-Tn5 tethered to histone-mark-bound chromatin.
> - `concept` [[30-Concepts/sortchic|sortChIC]] — pA-MNase plus FACS sorting into 384-well plates.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone-tail marks that demarcate chromatin states.
> - `entity` [[20-Entities/keji-zhao|Keji Zhao]] — NIH / NHLBI; a developer of scChIC-seq.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/ku-2019-scchic-seq|Ku 2019]]
> - [[10-Summaries/wang-2019-cobatch|Wang 2019]]
