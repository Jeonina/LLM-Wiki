---
type: concept
title: ICELL8 nanowell platform
aliases: [Takara ICELL8, SMARTer ICELL8]
tags: [single-cell, nanowell, platform, Takara, throughput]
created: 2026-05-12
updated: 2026-10-12
---

# ICELL8 nanowell platform

> A Takara Bio commercial single-cell dispensing platform with a 5,184-nanowell chip and integrated fluorescence imaging. Cells are loaded under Poisson statistics, imaged for QC, and addressable reagents are dispensed nanoliter-volumes per well ([[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]).

> [!abstract] 한눈에
> ICELL8은 5,184개 nanowell chip에 세포를 넣고 형광 영상으로 각 well을 확인한 뒤 well마다 시약을 나눠 넣는 Takara Bio의 single-cell 플랫폼이다 ([[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]). µATAC-seq, sciCUT&Tag, wellDA-seq가 이 chip을 쓴다 ([[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]; [[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).

## Why it matters

- Fluorescence imaging enables live single-cell QC before sequencing — unlike droplet platforms.
- Supports chromatin profiling methods (µATAC-seq, sciCUT&Tag), single-cell RNA-seq, and multi-omic protocols.
- 5,184 wells per chip × multiplexed loading → 10⁴ cells per chip.

## Examples

- [[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]] (µATAC-seq), [[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]] (sciCUT&Tag).
- wellDA-seq uses the 5,184-nanowell ICELL8 chip with DAPI imaging to keep only single-nucleus wells (1,200-2,600 per chip), then lyses each nucleus with protease in the well so that a second Tn5 can tagment chromatin-free DNA for whole-genome copy number alongside the first Tn5's ATAC library ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]). The authors argue this compartmentalisation is what allows full chromatin removal while keeping each cell's DNA together ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/micro-atac-seq|µATAC-seq]] — Single-cell ATAC-seq run on the ICELL8 nanowell chip.
> - `concept` [[30-Concepts/scicut-tag|sciCUT&Tag]] — Combinatorially indexed CUT&Tag dispensed on ICELL8.
> - `concept` [[30-Concepts/combinatorial-indexing|Combinatorial indexing]] — Split-pool barcoding that multiplies cells per chip.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]
> - [[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]
> - [[10-Summaries/wang-2024-wellda-seq|Wang 2024]]
