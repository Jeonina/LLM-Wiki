---
type: concept
title: SomaGauss-SV
aliases: []
tags: [structural-variants, nanopore, somatic, software, cancer]
created: 2026-05-12
updated: 2026-10-12
---

# SomaGauss-SV

> A somatic structural-variant detection workflow for paired tumor-vs-normal nanopore long-read data (Liu et al. 2025). Balances precision and recall across SV types (deletions, insertions, duplications, inversions, translocations) ([[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]).

> [!abstract] 한눈에
> SomaGauss-SV는 tumor와 normal을 짝지은 nanopore long-read 데이터에서 체세포 structural variant를 찾는 workflow다. 15쌍의 후두 편평세포암 시료에 적용해 흡연 강도와 somatic deletion 부담 사이의 상관을 보고했다 ([[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]).

## Definition

Designed for high-sensitivity detection of cancer-driven structural variation. Benchmarked against five paired tumor cell-line datasets. Applied to 15 paired laryngeal SCC tumor-blood samples to discover deletion-burden ↔ smoking intensity correlation and a high-frequency repeat-expansion ([[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]).

## Examples

- Laryngeal SCC SV landscape and biomarkers ([[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/structural-variants|Structural variants]] — Large genomic rearrangements: deletions, insertions, duplications, inversions, translocations.
> - `concept` [[30-Concepts/oxford-nanopore|Oxford Nanopore]] — Long-read platform that threads native molecules through nanopores.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — Technologies that read kilobase-to-megabase single molecules.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]
