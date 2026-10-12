---
type: concept
title: SAMOSA-Tag
aliases: [SAMOSA by tagmentation]
tags: [PacBio, chromatin-accessibility, single-fiber, EcoGII, Ramani-lab]
created: 2026-05-12
updated: 2026-10-12
---

# SAMOSA-Tag

> A low-input single-molecule chromatin-accessibility method (Nanda et al. 2024) combining in-nucleus EcoGII methyltransferase footprinting (6mA marks accessible regions) with SMRT-Tag library preparation. Detects sequence + 5mC (CpG) + 6mA (accessibility) on the same PacBio fiber from 30k–50k nuclei ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).

> [!abstract] 한눈에
> SAMOSA-Tag는 핵 안에서 EcoGII로 accessible DNA에 6mA를 표시한 뒤 SMRT-Tag로 library를 만들어, 같은 PacBio fiber에서 서열·CpG 5mC·accessibility를 함께 읽는 방법이다 ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]). 3–5만 개 핵이면 충분해 prostate cancer PDX 같은 임상 시료에도 적용되었다 ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).

## Definition

In-nucleus EcoGII methylation → SMRT-Tag tagmentation → PacBio HiFi sequencing ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]). PacBio polymerase kinetics distinguish endogenous 5mC from exogenous 6mA, enabling multi-modal single-fiber readout.

## Why it matters

- Brings the [[30-Concepts/samosa]] single-molecule chromatin assay within reach of clinical samples (PDXs, biopsies) ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).
- Resolves single-fiber CTCF binding and nucleosome positioning at the same loci where CpG methylation is also measured ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).
- Applied to prostate-cancer PDXs to reveal metastasis-associated global chromatin disorganization invisible to bulk ATAC-seq ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/samosa|SAMOSA]] — The parent single-molecule EcoGII footprinting assay.
> - `concept` [[30-Concepts/smrt-tag|SMRT-Tag]] — Tn5-based low-input PacBio HiFi library preparation.
> - `concept` [[30-Concepts/fiber-seq|Fiber-seq]] — m6A stencilling of protein occupancy on chromatin fibers.
> - `concept` [[30-Concepts/single-molecule-footprinting|Single-molecule footprinting]] — The class of per-fiber accessibility assays read by long reads.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — PacBio HiFi and ONT reads of kilobases or longer.
> - `entity` [[20-Entities/vijay-ramani|Vijay Ramani]] — Developer of SAMOSA, SMRT-Tag and SAMOSA-Tag.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]
