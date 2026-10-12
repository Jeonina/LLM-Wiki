---
type: concept
title: SMRT-Tag
aliases: [single-molecule real-time sequencing by tagmentation]
tags: [PacBio, tagmentation, low-input, Ramani-lab]
created: 2026-05-12
updated: 2026-10-12
---

# SMRT-Tag

> A low-input PacBio HiFi library-preparation method (Nanda et al. 2024) that uses Tn5 transposition with hairpin PacBio adapters to make exonuclease-resistant circular molecules from as little as 40 ng of DNA (~7,000 cells) ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).

> [!abstract] 한눈에
> SMRT-Tag는 hairpin PacBio adapter를 실은 Tn5로 DNA를 tagmentation해 40 ng(약 7,000세포)만으로 PacBio HiFi library를 만드는 방법이다. 필요한 DNA 양을 90–99% 줄이면서도 variant calling과 CpG methylation 정확도는 ligation 기반 PacBio와 비슷하다 ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).

## Definition

Tn5 with hairpin-loaded adapters tagments native DNA at low concentrations to generate ≥1 kb fragments. Gap repair (Phusion + Taq ligase or T4 + Ampligase) seals the 9-nt Tn5 gaps; exonuclease digestion enriches circularized molecules for PacBio sequencing ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).

## Why it matters

- ~90–99% reduction in PacBio DNA input requirements ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).
- Comparable variant-calling and CpG-methylation accuracy to ligation-based PacBio at matched coverage ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).
- Enables clinical-biopsy-scale PacBio sequencing ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).

## Examples

- HG002 trio variant calling; CpG methylation against bisulfite reference ([[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/samosa-tag|SAMOSA-Tag]] — SMRT-Tag plus in-nucleus EcoGII footprinting for single-fiber accessibility.
> - `concept` [[30-Concepts/samosa|SAMOSA]] — EcoGII footprinting of oligonucleosomes on PacBio.
> - `concept` [[30-Concepts/pacbio|PacBio]] — Long-read platform based on single-molecule real-time observation.
> - `concept` [[30-Concepts/tn5-tagmentation|Tn5 tagmentation]] — Simultaneous fragmentation and adapter insertion by Tn5.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — Technologies that read kilobase-to-megabase single molecules.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]
