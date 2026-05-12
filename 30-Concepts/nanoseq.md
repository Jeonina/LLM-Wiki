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

NanoSeq has been the workhorse for measuring somatic mutation accumulation rates in normal human tissues (Abascal et al. 2021 Nature). Reports 15–20 SNVs/year accumulation in human neurons ([[10-Summaries/bizzotto-2022-brain-mosaicism]]).

## Examples

- One of six methods in the SMaHT benchmark ([[10-Summaries/benchmarking-of-duplex-sequencing-approaches-to-reveal-somatic-mutation-landscapes]]).

## Related

- [[30-Concepts/duplex-sequencing]] · [[30-Concepts/codec]] · [[30-Concepts/hidef-seq]] · [[40-Topics/duplex-sequencing]]
