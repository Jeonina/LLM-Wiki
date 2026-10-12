---
type: concept
title: SCcaller
aliases: []
tags: [single-cell, variant-calling, software]
created: 2026-05-12
updated: 2026-10-12
---

# SCcaller

> A single-cell SNV caller (Dong et al. 2017) that uses information from adjacent **bulk-sample-derived heterozygous SNVs** to calibrate allele-dropout corrections in a target cell. Requires matched bulk data ([[10-Summaries/dong-2017-sccaller|Dong 2017]]).

> [!abstract] 한눈에
> SCcaller는 주변의 heterozygous germline SNP로 그 구간의 allele 증폭 편향을 추정해, single cell의 SNV 후보를 보정하는 variant caller다 ([[10-Summaries/dong-2017-sccaller|Dong 2017]]). matched bulk가 없거나 세포가 bulk와 다른 minor clone에 속하면 쓰기 어렵다.

## Definition

Local heterozygous SNVs (from bulk) anchor the expected allele-balance pattern; deviations at candidate single-cell loci are scored against this anchor.

## Why it matters

- Improves on Monovar's independent-locus assumption by exploiting local linkage.
- Limited when matched bulk is unavailable or when the cell belongs to a minor clone whose heterozygous pattern differs from bulk.

## Related

> [!cards]
> - `concept` [[30-Concepts/scout-variant-caller|SCOUT]] — Single-cell SNV caller borrowing information from adjacent loci.
> - `concept` [[30-Concepts/monovar|Monovar]] — Multi-cell SNV caller that assumes independent loci.
> - `concept` [[30-Concepts/allele-dropout|Allele dropout]] — One allele fails to amplify, so a heterozygous site looks homozygous.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — Technologies that interrogate the DNA of single cells.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/dong-2017-sccaller|Dong 2017]]
