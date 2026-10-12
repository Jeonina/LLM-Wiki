---
type: concept
title: HiDEF-seq
aliases: [High-Definition Sequencing]
tags: [duplex-sequencing, single-strand, mutation-detection]
created: 2026-05-12
updated: 2026-10-12
---

# HiDEF-seq

> A duplex-sequencing method from the Evrony lab that detects single-strand-resolved mutations with high accuracy, and one of the SMaHT-network duplex methods ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]; [[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).

> [!abstract] 한눈에
> HiDEF-seq는 증폭하지 않은 단일 DNA 분자를 PacBio로 여러 번 읽어 한쪽 가닥에만 있는 mismatch와 손상까지 구분해 내는 duplex 방법이다 ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]). 정확도와 duplex 효율은 가장 높지만 비용도 가장 높고, 아직 단일 세포가 아니라 bulk DNA가 필요하다 ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]; [[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [Duplex sequencing 시뮬레이터](../60-Explainers/duplex-sequencing.html)
<!-- /explainer-links -->

## Definition

HiDEF-seq leverages duplex chemistry with optimized library conversion for sensitive somatic mutation detection; implementation details are in Liu et al. 2024 from the Evrony lab ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]). It sequences unamplified single molecules, so it reads the **precursor** events: single-strand mismatches and cytosine-deamination damage ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).

## Why it matters

- It is designed for somatic mutation profiling with single-strand and double-strand variant resolution ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]), specifically in non-cancer tissues (synthesis).
- Every prior method — single-cell WGS, clonal expansion, microdissection, duplex sequencing — amplifies before reading, which either converts single-strand lesions into double-strand mutations or manufactures artifactual ones ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).

## Method

**Three engineering moves** ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]):

- ~32 sequencing passes per strand on median 1.7 kb molecules, for a per-strand consensus ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).
- Single-strand nick ligation plus [[30-Concepts/nanoseq|NanoSeq]]-style A-tailing (or a no-A-tailing variant for degraded post-mortem DNA) to eliminate in vitro artifacts ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).
- A pipeline analysing only substitutions, orthogonal to PacBio's dominant indel error mode ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).

**Fidelity by pass threshold**

| Passes per strand | Error rate | Used for | Source |
|---|---|---|---|
| ≥5 | <1 error per 3 × 10¹³ bp | dsDNA analysis (99.8% of molecules retained) | ([[10-Summaries/liu-2024-hidef-seq\|Liu 2024]]) |
| ≥20 | <1 error per 1 × 10¹⁴ bp | ssDNA analysis | ([[10-Summaries/liu-2024-hidef-seq\|Liu 2024]]) |

## Evidence and examples

- SBS10ss extracted from *POLE* PPAP samples matches the same samples' dsDNA signatures at cosine 0.97 ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).
- Strand asymmetry (AGA>ATA vs TCT>TAT at 73:10) directly identifies C:dT rather than G:dA misincorporation in vivo ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).
- HiDEF-seq was one of six methods compared in the SMaHT benchmark, which introduced HiDEF-seq v3 (random ~4 kb fragmentation, whole-genome coverage) ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).
- In that benchmark it had the highest duplex efficiency (~64%) but the highest cost (~$220 per billion interrogated bp) ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).

## Contested points

- **Which error rate to quote.** The primary paper estimates <1 error per 3 × 10¹³ bp (≥5 passes) and <1 per 1 × 10¹⁴ bp (≥20 passes) ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]); Shao 2025 quotes <7 × 10⁻¹⁶, which is not in the primary paper's main text ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). Cite the primary-paper values.
- **NanoSeq's single-strand calls look inflated.** NanoSeq's ssDNA calls are ~18-fold inflated relative to HiDEF-seq ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).
- **Bulk input only.** HiDEF-seq needs bulk DNA input, not single cells ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).
- **Partial genome capture.** Restriction fragmentation captures ~40% of the genome ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]); the SMaHT benchmark's v3 uses random fragmentation for whole-genome coverage ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).
- **Uncalibrated ssDNA burdens.** Absolute ssDNA burdens remain uncalibrated because duplex correction is unavailable for single-strand calls ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/nanoseq|NanoSeq]] — Sanger duplex protocol whose A-tailing HiDEF-seq borrows, and whose ssDNA calls it disputes.
> - `entity` [[20-Entities/gilad-evrony|Gilad Evrony]] — Lab head behind HiDEF-seq.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Strand-tagged single-molecule sequencing for low-error somatic mutation calls.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/liu-2024-hidef-seq|Liu 2024]]
> - [[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]
