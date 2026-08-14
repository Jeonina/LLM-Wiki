---
type: concept
title: NanoSeq
aliases: [nano-rate sequencing]
tags: [duplex-sequencing, library-prep, somatic-mutation]
created: 2026-05-12
updated: 2026-05-12
---

# NanoSeq

> A duplex-sequencing protocol developed at the Wellcome Sanger Institute that uses bottleneck library prep and BotSeqS-style filtering to achieve very low error rates from small amounts of input DNA. Widely used for somatic mutation rate estimation in normal tissues.

## Definition

NanoSeq uses HpyCH4V restriction digestion (or other bottlenecks) followed by duplex-sequencing library preparation, restricting analysis to high-confidence dual-strand consensus calls.

## Why it matters

NanoSeq has been the workhorse for measuring somatic mutation accumulation rates in normal human tissues (Abascal et al. 2021 Nature). Reports 15–20 SNVs/year accumulation in human neurons ([[10-Summaries/bizzotto-2022-brain-mosaicism-review]]).

## Examples

- One of six methods in the SMaHT benchmark ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]).

## Related

- [[40-Topics/duplex-sequencing]] · [[30-Concepts/codec]] · [[30-Concepts/hidef-seq]] · [[40-Topics/duplex-sequencing]]

## Added 2026-08-13

HiDEF-seq adopts NanoSeq's A-tailing artifact-control approach while **refuting its single-strand calls**: across nine samples run on both, dsDNA burdens and patterns agree, but HiDEF-seq measures 18-fold lower ssDNA call burdens (5-fold for C>T only) with distinct patterns, indicating NanoSeq's ssDNA calls are largely artifactual — as its own developers suspected ([[10-Summaries/liu-2024-hidef-seq]]).

The practical implication: NanoSeq remains sound for **double-strand** mutation burdens and signatures; any prior single-strand claim from duplex-family methods should be re-read against [[10-Summaries/liu-2024-hidef-seq]]. (synthesis)
