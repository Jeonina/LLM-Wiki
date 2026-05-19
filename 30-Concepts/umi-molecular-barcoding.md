---
type: concept
title: UMI / molecular barcoding
aliases: [unique molecular identifier, molecular tag, degenerate barcode]
tags: [sequencing, error-correction, library-prep]
created: 2026-05-12
updated: 2026-05-14
---

# UMI (Unique Molecular Identifier)

> A short random DNA sequence ligated to each individual molecule during library preparation so that, after PCR amplification, reads can be grouped by molecular origin and consensus-called to remove polymerase and sequencing errors.

## Definition

A 6–24-nt degenerate oligo, often paired between adapter ends so each duplex DNA fragment gets a complementary pair of tags. After PCR, reads sharing the same UMI pair come from the same original molecule and can be collapsed to a consensus sequence (or, for [[30-Concepts/duplex-sequencing]], compared between strands to call mutations only when both strands agree).

## Why it matters

UMIs make NGS quantitative (counts reflect input molecules, not PCR duplicates) and dramatically reduce false-positive variant calls. Foundational to duplex sequencing and to scRNA-seq where droplet-barcoded UMIs distinguish per-cell expression.

**Caveat — UMI saturation is sublinear.** [[10-Summaries/svensson-2017-power-analysis|Svensson 2017]] showed across 15 scRNA-seq protocols that the best-fit relationship between input mRNA molecules and counted UMIs has an exponent of ~0.8, not 1.0 — i.e. UMI counts undercount at high expression. Causes: collision (UMI re-use when complexity is low — 4-nt UMI ⇒ only 256 codes), and template-switching artifacts. Longer UMIs (10 nt → ~1M codes) mitigate but do not eliminate this. For quantitative claims at high expression, the residual amplification bias matters.

## Examples

- 12-nt random tag in Kennedy 2014 ([[10-Summaries/kennedy-2014-duplex-protocol]])
- Combinatorial split-pool barcoding in [[10-Summaries/bai-2024-simple-seq]] and [[10-Summaries/shen-2026-splicool-seq]]
- 8-nt SMRT-Tag barcode in [[10-Summaries/abdulhay-2020-samosa]]
- 8-nt random UMI on every Drop-seq bead primer for PCR-duplicate collapse in droplet scRNA-seq ([[10-Summaries/macosko-2015-drop-seq]])

## Related

- [[30-Concepts/duplex-sequencing]] · [[30-Concepts/combinatorial-indexing]] · [[40-Topics/duplex-sequencing]]
- [[30-Concepts/drop-seq]] · [[30-Concepts/scrna-seq]] — UMI is now standard in droplet scRNA-seq
- [[10-Summaries/svensson-2017-power-analysis]] — quantifies UMI saturation (exponent ~0.8)
