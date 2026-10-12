---
type: concept
title: Mappability
aliases: [multi-mapping, uniquely mappable regions, alignability]
tags: [alignment, repeats, bias, QC]
created: 2026-08-10
updated: 2026-10-12
---

# Mappability

> Whether a read originating from a given genomic position can be assigned back to that position uniquely. Low-mappability regions receive systematically depressed read counts regardless of their true copy number or signal ([[10-Summaries/li-2009-bwa|BWA]]; [[10-Summaries/bakker-2016-aneufinder|AneuFinder]]).

> [!abstract] 한눈에
> Mappability는 read가 유래한 위치로 유일하게 되돌아가 정렬될 수 있는지를 뜻하며, sample이 아니라 reference와 read 길이의 성질이다 ([[10-Summaries/li-2009-bwa|BWA]]). CNV caller, peak caller, sparse-data caller가 각자 방식으로 보정하지만 반복이 많은 영역은 short read로는 여전히 사각지대로 남는다 ([[10-Summaries/eichler-2007-completing-sv-map|Eichler 2007]]).

## Definition

Exact repeats collapse onto a single path during BWT-based search, so a read matching many locations is cheap to detect and impossible to place ([[10-Summaries/li-2009-bwa|BWA]]). Mappability is therefore a property of the reference and read length, not of the sample ([[10-Summaries/li-2009-bwa|BWA]]).

## Why it matters

Every downstream caller that counts reads inherits the bias, so each class of tool needs its own way of handling it (synthesis).

## How methods handle it

| Setting | Handling | Source |
|---|---|---|
| Copy-number calling | Variable-size bins chosen so each has comparable expected read count under mappability — averaging ~1 Mb — are what make an HMM emission model valid | ([[10-Summaries/bakker-2016-aneufinder\|AneuFinder]]) |
| Peak calling | A dynamic local λ estimated in 1/5/10 kb windows absorbs mappability bias along with copy number and chromatin structure | ([[10-Summaries/zhang-2008-macs\|MACS]]) |
| Sparse-data peak calling | SEACR discards signal blocks overlapping a threshold-passing IgG block, precisely to remove spurious peaks arising from multi-mapping at repeats | ([[10-Summaries/meers-2019-seacr\|SEACR]]) |
| Long-read accessibility | Long reads rescue low-mappability regions that short-read ATAC-seq largely misses | ([[10-Summaries/li-2025-scnanoatac-seq2\|scNanoATAC-seq2]]) |

## Evidence and examples

- **Library chemistry can destroy it.** WGA4-amplified single cells suffer low mappability from adaptor contamination, wasting a large fraction of reads ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- **Repeat-rich regions remain a structural blind spot** for short-read approaches generally ([[10-Summaries/eichler-2007-completing-sv-map|Eichler 2007]]).
- **Long reads recover repeated regulatory elements.** scNanoATAC-seq2 recovers an intronic CRE in every Zscan4 paralog, and accessibility of individual Tcstv paralogs and LTRs ([[10-Summaries/li-2025-scnanoatac-seq2|scNanoATAC-seq2]]).

## Open questions

- Highly repetitive and segmentally duplicated regions are the parts of the genome where somatic variation is least characterized, and no method in this corpus resolves them with short reads; see [[highly-repetitive-regions]] (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/read-alignment|Read alignment]] — Placing reads onto a reference genome; the step that defines mappability.
> - `concept` [[30-Concepts/highly-repetitive-regions|Highly repetitive regions]] — Centromeres, telomeres, rDNA and segmental duplications that short reads cannot map uniquely.
> - `concept` [[30-Concepts/copy-number-variation|Copy number variation]] — Read-depth calling that must correct for mappability.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — Aligners, callers and other tools that turn raw reads into results.

## All sources on this page

> [!info]- 7 summaries cited here
> - [[10-Summaries/bakker-2016-aneufinder|Bakker 2016]]
> - [[10-Summaries/eichler-2007-completing-sv-map|Eichler 2007]]
> - [[10-Summaries/li-2009-bwa|Li & Durbin 2009]]
> - [[10-Summaries/li-2025-scnanoatac-seq2|Li 2025]]
> - [[10-Summaries/meers-2019-seacr|Meers 2019]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
> - [[10-Summaries/zhang-2008-macs|Zhang 2008]]
