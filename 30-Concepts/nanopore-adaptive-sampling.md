---
type: concept
title: Nanopore adaptive sampling
aliases: [ReadFish, ReadUntil]
tags: [long-read, ONT, targeted-sequencing]
created: 2026-05-12
updated: 2026-10-12
---

# Nanopore adaptive sampling

> A real-time read-selection feature of Oxford Nanopore sequencers that compares the first few hundred bases of each emerging read to a target reference, then **rejects unwanted reads** by reversing the pore voltage so the molecule is ejected. The pore is then available for the next molecule.

> [!abstract] 한눈에
> Adaptive sampling은 nanopore가 읽는 중인 read의 앞부분을 표적 서열과 비교해 필요 없는 분자를 즉시 내보내는 기능으로, capture나 PCR 없이 원하는 영역만 농축한다. Capture probe를 설계하기 어려운 반복 영역에 특히 유용해서, STAM-seq는 이를 식물의 반복 영역(HRR) 연구에 썼다 ([[10-Summaries/mo-2023-stam-seq|STAM-seq]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [Long-read 시퀀싱 교재](../60-Explainers/long-read-sequencing.html)
<!-- /explainer-links -->

## Definition

Implemented via tools like ReadFish, ReadUntil, and ONT's native Dorado. Targeted regions are typically specified as a BED file or list of contigs.

## Why it matters

- Targeted sequencing without library-prep capture: enriches for regions of interest without PCR or hybridization.
- Particularly useful for highly repetitive regions where capture probes can't be uniquely designed.

## Examples

- STAM-seq uses adaptive sampling for plant HRRs ([[10-Summaries/mo-2023-stam-seq|STAM-seq]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/oxford-nanopore|Oxford Nanopore Technologies]] — The long-read platform that provides adaptive sampling.
> - `concept` [[30-Concepts/highly-repetitive-regions|Highly repetitive regions (HRRs)]] — Centromeres, telomeres and rDNA that short reads cannot map uniquely.
> - `concept` [[30-Concepts/stam-seq|STAM-seq]] — Nanopore accessibility and methylation assay that uses adaptive sampling.
> - `hub` [[40-Topics/long-read-sequencing|Long-read sequencing]] — Long-read platforms and what they measure.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/mo-2023-stam-seq|Mo 2023]]
