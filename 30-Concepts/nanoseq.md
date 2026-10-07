---
type: concept
title: NanoSeq
aliases: [nano-rate sequencing]
tags: [duplex-sequencing, library-prep, somatic-mutation]
created: 2026-05-12
updated: 2026-10-07
---

# NanoSeq

> A duplex-sequencing protocol developed at the Wellcome Sanger Institute that uses bottleneck library prep and BotSeqS-style filtering to achieve very low error rates from small amounts of input DNA. Widely used for somatic mutation rate estimation in normal tissues.

## Definition

NanoSeq uses HpyCH4V restriction digestion (or other bottlenecks) followed by duplex-sequencing library preparation, restricting analysis to high-confidence dual-strand consensus calls.

## Why it matters

NanoSeq has been the workhorse for measuring somatic mutation accumulation rates in normal human tissues (Abascal et al. 2021 Nature). Reports 15–20 SNVs/year accumulation in human neurons ([[10-Summaries/bizzotto-2022-brain-mosaicism-review]]).

## Examples

- One of six methods in the SMaHT benchmark, run as restriction NanoSeq-Hpy (~35% genome breadth) and sonication + mung bean nuclease NanoSeq-MBN (~94% breadth, low trinucleotide bias, ~$76 per billion interrogated bp) ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]).

## Added 2026-10-07

BotSeqS introduced bottleneck dilution of a PCR-free, adaptor-ligated library so that random double-stranded molecules are read from both strands; with ≥90% Watson and Crick family concordance it reached a 2.6 × 10⁻¹² per-bp false-positive rate but covered only ~0.4% of the nuclear genome per library [[10-Summaries/hoang-2016-botseqs]]. NanoSeq builds on bottleneck-style duplex sequencing (synthesis; see [[10-Summaries/abascal-2021-nanoseq]]).

SMM-seq borrows NanoSeq's strand-family-size-2 baseline for normalizing mutation frequency, and argues that NanoSeq, Duplex-Seq and BotSeqS share a P(E)² error bound that multi-copy RCA overcomes. No head-to-head comparison on the same DNA is reported ([[10-Summaries/maslov-2022-smm-seq]]).


## Related

- [[40-Topics/duplex-sequencing]] · [[30-Concepts/codec]] · [[30-Concepts/hidef-seq]] · [[40-Topics/duplex-sequencing]]

## Added 2026-08-13

HiDEF-seq adopts NanoSeq's A-tailing artifact-control approach while **refuting its single-strand calls**: across nine samples run on both, dsDNA burdens and patterns agree, but HiDEF-seq measures 18-fold lower ssDNA call burdens (5-fold for C>T only) with distinct patterns, indicating NanoSeq's ssDNA calls are largely artifactual — as its own developers suspected ([[10-Summaries/liu-2024-hidef-seq]]).

The practical implication: NanoSeq remains sound for **double-strand** mutation burdens and signatures; any prior single-strand claim from duplex-family methods should be re-read against [[10-Summaries/liu-2024-hidef-seq]]. (synthesis)
