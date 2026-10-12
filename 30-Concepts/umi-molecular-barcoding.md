---
type: concept
title: UMI / molecular barcoding
aliases: [unique molecular identifier, molecular tag, degenerate barcode]
tags: [sequencing, error-correction, library-prep]
created: 2026-05-12
updated: 2026-10-12
---

# UMI (Unique Molecular Identifier)

> A short random DNA sequence ligated to each individual molecule during library preparation so that, after PCR amplification, reads can be grouped by molecular origin and consensus-called to remove polymerase and sequencing errors ([[10-Summaries/kennedy-2014-duplex-protocol|Kennedy 2014]]).

> [!abstract] 한눈에
> UMI는 증폭 전 각 분자에 붙이는 짧은 무작위 서열로, 같은 분자에서 나온 read를 묶어 consensus를 내고 PCR 중복을 걸러 낸다. 단일 가닥 consensus만으로는 첫 PCR 단계의 손상 염기 오류가 남기 때문에 duplex sequencing은 두 가닥에 상보적인 tag를 붙이며 ([[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]), scRNA-seq에서 UMI 수는 입력 분자 수에 선형으로 늘지 않는다 ([[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [Duplex sequencing 시뮬레이터](../60-Explainers/duplex-sequencing.html)
<!-- /explainer-links -->

## Definition

A 6–24-nt degenerate oligo, often paired between adapter ends so each duplex DNA fragment gets a complementary pair of tags. After PCR, reads sharing the same UMI pair come from the same original molecule and can be collapsed to a consensus sequence (or, for [[40-Topics/duplex-sequencing]], compared between strands to call mutations only when both strands agree).

## Why it matters

- UMIs make NGS quantitative (counts reflect input molecules, not PCR duplicates) and dramatically reduce false-positive variant calls.
- They are foundational to duplex sequencing and to scRNA-seq, where droplet-barcoded UMIs distinguish per-cell expression.

## Barcoding strategies

| Strategy | Example | Tag design | Source |
|---|---|---|---|
| Random duplex tag | [[10-Summaries/kennedy-2014-duplex-protocol\|Kennedy 2014]] | 12-nt random tag | ([[10-Summaries/kennedy-2014-duplex-protocol\|Kennedy 2014]]) |
| Complementary double-stranded tags | [[10-Summaries/schmitt-2012-pnas\|Schmitt 2012]] | Tags on both strands, needed because single-strand consensus leaves first-round PCR errors | ([[10-Summaries/schmitt-2012-pnas\|Schmitt 2012]]) |
| UMI in a hairpin-adapter stem | [[10-Summaries/maslov-2022-smm-seq\|SMM-seq]] | 6-nt UMI that identifies both the fragment's UMI family and its two strand families | ([[10-Summaries/maslov-2022-smm-seq\|SMM-seq]]) |
| Endogenous shear-point barcodes | [[10-Summaries/hoang-2016-botseqs\|BotSeqS]] | Random fragment-end coordinates after bottleneck dilution, no synthetic UMIs | ([[10-Summaries/hoang-2016-botseqs\|BotSeqS]]) |
| Bead-primer UMI in droplets | [[10-Summaries/macosko-2015-drop-seq\|Drop-seq]] | 8-nt random UMI on every bead primer, for PCR-duplicate collapse | ([[10-Summaries/macosko-2015-drop-seq\|Drop-seq]]) |
| Combinatorial split-pool barcoding | [[10-Summaries/bai-2024-simple-seq\|SIMPLE-seq]]; [[10-Summaries/shen-2026-splicool-seq\|SpliCOOL-seq]] | Split-pool barcode combinations (see [[30-Concepts/combinatorial-indexing]]) | ([[10-Summaries/bai-2024-simple-seq\|SIMPLE-seq]]; [[10-Summaries/shen-2026-splicool-seq\|SpliCOOL-seq]]) |

## Evidence and examples

- Single-strand UMI consensus removes ~99% of sequencing errors but cannot remove first-round PCR errors at damaged bases (15-fold G→T and 11-fold C→T excess), which is why complementary double-stranded tags are needed ([[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]).
- In SMM-seq, reads from each strand family (≥7 required) must agree before a variant is called ([[10-Summaries/maslov-2022-smm-seq|SMM-seq]]).
- BotSeqS groups reads into Watson and Crick families by fragment ends after bottleneck dilution, without synthetic UMIs ([[10-Summaries/hoang-2016-botseqs|BotSeqS]]).
- Across 15 scRNA-seq protocols, the best-fit relationship between input mRNA molecules and counted UMIs has an exponent of ~0.8, not 1.0 ([[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]).

## Contested points

- **UMI saturation is sublinear.** The ~0.8 exponent means UMI counts undercount at high expression ([[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]). Plausible causes include collision (UMI re-use when complexity is low — 4-nt UMI ⇒ only 256 codes) and template-switching artifacts; longer UMIs (10 nt → ~1M codes) mitigate but do not eliminate this (synthesis). For quantitative claims at high expression, the residual amplification bias matters (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/combinatorial-indexing|Combinatorial indexing]] — Split-pool barcoding that gives each cell a unique barcode combination.
> - `concept` [[30-Concepts/drop-seq|Drop-seq]] — Droplet scRNA-seq with barcoded beads; UMI is now standard in droplet scRNA-seq.
> - `concept` [[30-Concepts/scrna-seq|scRNA-seq]] — Per-cell expression profiling, where UMIs count input molecules.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Tags both strands of each molecule with complementary UMIs and calls mutations only when both agree.

## All sources on this page

> [!info]- 8 summaries cited here
> - [[10-Summaries/bai-2024-simple-seq|Bai 2024]]
> - [[10-Summaries/hoang-2016-botseqs|Hoang 2016]]
> - [[10-Summaries/kennedy-2014-duplex-protocol|Kennedy 2014]]
> - [[10-Summaries/macosko-2015-drop-seq|Macosko 2015]]
> - [[10-Summaries/maslov-2022-smm-seq|Maslov 2022]]
> - [[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]
> - [[10-Summaries/shen-2026-splicool-seq|Shen 2026]]
> - [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]]
