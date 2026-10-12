---
type: concept
title: NanoSeq
aliases: [nano-rate sequencing]
tags: [duplex-sequencing, library-prep, somatic-mutation]
created: 2026-05-12
updated: 2026-10-12
---

# NanoSeq

> A duplex-sequencing protocol developed at the Wellcome Sanger Institute that uses bottleneck library prep and BotSeqS-style filtering to achieve very low error rates from small amounts of input DNA. Widely used for somatic mutation rate estimation in normal tissues ([[10-Summaries/abascal-2021-nanoseq|Abascal 2021]]).

> [!abstract] 한눈에
> NanoSeq는 bottleneck library와 양 가닥 consensus로 오류율을 크게 낮춘 duplex sequencing 방법이고, 정상 조직의 체세포 변이 축적 속도를 재는 표준 도구로 쓰여 왔다 ([[10-Summaries/abascal-2021-nanoseq|Abascal 2021]]; [[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]). 양 가닥(dsDNA) 변이 측정은 HiDEF-seq와 일치하지만, 단일 가닥(ssDNA) 호출은 대부분 artifact로 보인다 ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).

## Definition

NanoSeq uses HpyCH4V restriction digestion (or other bottlenecks) followed by duplex-sequencing library preparation, restricting analysis to high-confidence dual-strand consensus calls. It builds on bottleneck-style duplex sequencing (synthesis; see [[10-Summaries/abascal-2021-nanoseq|Abascal 2021]]), introduced by BotSeqS ([[10-Summaries/hoang-2016-botseqs|BotSeqS]]).

## Why it matters

NanoSeq has been the workhorse for measuring somatic mutation accumulation rates in normal human tissues (Abascal et al. 2021 Nature) ([[10-Summaries/abascal-2021-nanoseq|Abascal 2021]]). Reports 15–20 SNVs/year accumulation in human neurons ([[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto 2022]]).

## Protocol variants and ancestor

| Protocol | Fragmentation / design | Genome breadth | Notes | Source |
|---|---|---|---|---|
| BotSeqS (ancestor) | Bottleneck dilution of a PCR-free, adaptor-ligated library so that random double-stranded molecules are read from both strands | ~0.4% of the nuclear genome per library | ≥90% Watson and Crick family concordance; 2.6 × 10⁻¹² per-bp false-positive rate | ([[10-Summaries/hoang-2016-botseqs\|BotSeqS]]) |
| NanoSeq-Hpy | Restriction (HpyCH4V) | ~35% | — | ([[10-Summaries/zhang-2025-smaht-duplex-benchmark\|Zhang 2025]]) |
| NanoSeq-MBN | Sonication + mung bean nuclease | ~94% | Low trinucleotide bias, ~$76 per billion interrogated bp | ([[10-Summaries/zhang-2025-smaht-duplex-benchmark\|Zhang 2025]]) |

## Evidence and examples

- NanoSeq was one of six methods in the SMaHT benchmark, run as both NanoSeq-Hpy and NanoSeq-MBN ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).
- HiDEF-seq adopts NanoSeq's A-tailing artifact-control approach ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).
- Across nine samples run on both NanoSeq and HiDEF-seq, dsDNA burdens and patterns agree, but HiDEF-seq measures 18-fold lower ssDNA call burdens (5-fold for C>T only) with distinct patterns ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).
- SMM-seq borrows NanoSeq's strand-family-size-2 baseline for normalizing mutation frequency ([[10-Summaries/maslov-2022-smm-seq|SMM-seq]]).

## Contested points

- **NanoSeq's single-strand calls.** HiDEF-seq's comparison indicates NanoSeq's ssDNA calls are largely artifactual — as its own developers suspected ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]). The practical implication: NanoSeq remains sound for **double-strand** mutation burdens and signatures; any prior single-strand claim from duplex-family methods should be re-read against HiDEF-seq ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]). (synthesis)
- **Shared error bound.** SMM-seq argues that NanoSeq, Duplex-Seq and BotSeqS share a P(E)² error bound that multi-copy RCA overcomes. No head-to-head comparison on the same DNA is reported ([[10-Summaries/maslov-2022-smm-seq|SMM-seq]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/codec|CODEC]] — Duplex method that reads both strands in a single read pair.
> - `concept` [[30-Concepts/hidef-seq|HiDEF-seq]] — Unamplified single-molecule method that tested NanoSeq's single-strand calls.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Error-corrected sequencing by reading both strands of a molecule.

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/abascal-2021-nanoseq|Abascal 2021]]
> - [[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto & Walsh 2022]]
> - [[10-Summaries/hoang-2016-botseqs|Hoang 2016]]
> - [[10-Summaries/liu-2024-hidef-seq|Liu 2024]]
> - [[10-Summaries/maslov-2022-smm-seq|Maslov 2022]]
> - [[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]
