---
type: concept
title: UMI / molecular barcoding
aliases: [unique molecular identifier, molecular tag, degenerate barcode]
tags: [sequencing, error-correction, library-prep]
created: 2026-05-12
updated: 2026-10-07
---

# UMI (Unique Molecular Identifier)

> A short random DNA sequence ligated to each individual molecule during library preparation so that, after PCR amplification, reads can be grouped by molecular origin and consensus-called to remove polymerase and sequencing errors.

## Definition

A 6–24-nt degenerate oligo, often paired between adapter ends so each duplex DNA fragment gets a complementary pair of tags. After PCR, reads sharing the same UMI pair come from the same original molecule and can be collapsed to a consensus sequence (or, for [[40-Topics/duplex-sequencing]], compared between strands to call mutations only when both strands agree).

## Why it matters

UMIs make NGS quantitative (counts reflect input molecules, not PCR duplicates) and dramatically reduce false-positive variant calls. Foundational to duplex sequencing and to scRNA-seq where droplet-barcoded UMIs distinguish per-cell expression.

**Caveat — UMI saturation is sublinear.** [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]] showed across 15 scRNA-seq protocols that the best-fit relationship between input mRNA molecules and counted UMIs has an exponent of ~0.8, not 1.0 — i.e. UMI counts undercount at high expression. Plausible causes include collision (UMI re-use when complexity is low — 4-nt UMI ⇒ only 256 codes) and template-switching artifacts; longer UMIs (10 nt → ~1M codes) mitigate but do not eliminate this (synthesis). For quantitative claims at high expression, the residual amplification bias matters.

## Examples

- 12-nt random tag in Kennedy 2014 ([[10-Summaries/kennedy-2014-duplex-protocol]])
- Combinatorial split-pool barcoding in [[10-Summaries/bai-2024-simple-seq]] and [[10-Summaries/shen-2026-splicool-seq]]
- 8-nt random UMI on every Drop-seq bead primer for PCR-duplicate collapse in droplet scRNA-seq ([[10-Summaries/macosko-2015-drop-seq]])

## Added 2026-10-07

Random shear-point coordinates can serve as endogenous molecular barcodes: BotSeqS groups reads into Watson and Crick families by fragment ends after bottleneck dilution, without synthetic UMIs [[10-Summaries/hoang-2016-botseqs]].

In SMM-seq a 6-nt UMI sits in the stem of a hairpin adapter. It identifies both the fragment's UMI family and its two strand families, and reads from each strand family (≥7 required) must agree before a variant is called ([[10-Summaries/maslov-2022-smm-seq]]).


Single-strand UMI consensus removes ~99% of sequencing errors but cannot remove first-round PCR errors at damaged bases (15-fold G→T and 11-fold C→T excess), which is why complementary double-stranded tags are needed ([[10-Summaries/schmitt-2012-pnas]]).

## Related

- [[40-Topics/duplex-sequencing]] · [[30-Concepts/combinatorial-indexing]] · [[40-Topics/duplex-sequencing]]
- [[30-Concepts/drop-seq]] · [[30-Concepts/scrna-seq]] — UMI is now standard in droplet scRNA-seq
- [[10-Summaries/svensson-2017-power-analysis]] — quantifies UMI saturation (exponent ~0.8)
