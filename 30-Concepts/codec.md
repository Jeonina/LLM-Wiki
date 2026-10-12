---
type: concept
title: CODEC
aliases: [Concatenating Original Duplex for Error Correction]
tags: [duplex-sequencing, library-prep, low-input]
created: 2026-05-12
updated: 2026-10-12
---

# CODEC

> Concatenating Original Duplex for Error Correction — a duplex-sequencing chemistry developed at the Broad Institute (V. Adalsteinsson) that concatenates both strands of a DNA molecule into one read, allowing per-molecule error correction in standard short-read sequencing ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).

> [!abstract] 한눈에
> CODEC은 DNA 이중가닥의 두 가닥을 하나의 read로 이어 붙여 한 read pair만으로 가닥 간 consensus를 만드는 duplex sequencing 화학이다. SMaHT 벤치마크에서 비교된 여섯 방법 중 하나로, end-repair 방식에 따라 breadth가 크게 달랐다 ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).

## Definition

CODEC fuses the two strands of a duplex into a contiguous sequenced fragment, enabling strand-consensus calling from a single read pair. One of the methods evaluated by the SMaHT duplex benchmark ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).

## Why it matters

Lower-cost duplex chemistry; benchmark-comparable accuracy to [[30-Concepts/nanoseq|NanoSeq]] and [[30-Concepts/hidef-seq|HiDEF-seq]] ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).

## Examples

- One of six methods compared in the SMaHT benchmark, in three end-repair versions (restriction-based ~41% breadth; whole-genome DRv1/DRv2 ~98% breadth); ~$126 per billion interrogated bp ([[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/nanoseq|NanoSeq]] — Bottleneck duplex protocol for very low error rates from small DNA inputs.
> - `concept` [[30-Concepts/hidef-seq|HiDEF-seq]] — Duplex method that resolves mutations to a single strand.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Strand-consensus methods for detecting rare somatic mutations.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]
