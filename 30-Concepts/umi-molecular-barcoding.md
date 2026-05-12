---
type: concept
title: UMI / molecular barcoding
aliases: [unique molecular identifier, molecular tag, degenerate barcode]
tags: [sequencing, error-correction, library-prep]
created: 2026-05-12
updated: 2026-05-12
---

# UMI (Unique Molecular Identifier)

> A short random DNA sequence ligated to each individual molecule during library preparation so that, after PCR amplification, reads can be grouped by molecular origin and consensus-called to remove polymerase and sequencing errors.

## Definition

A 6–24-nt degenerate oligo, often paired between adapter ends so each duplex DNA fragment gets a complementary pair of tags. After PCR, reads sharing the same UMI pair come from the same original molecule and can be collapsed to a consensus sequence (or, for [[30-Concepts/duplex-sequencing]], compared between strands to call mutations only when both strands agree).

## Why it matters

UMIs make NGS quantitative (counts reflect input molecules, not PCR duplicates) and dramatically reduce false-positive variant calls. Foundational to duplex sequencing and to scRNA-seq where droplet-barcoded UMIs distinguish per-cell expression.

## Examples

- 12-nt random tag in Kennedy 2014 ([[10-Summaries/detecting-ultralow-frequency-mutations-by-duplex-sequencing]])
- Combinatorial split-pool barcoding in [[10-Summaries/simultaneous-single-cell-analysis-of-5mc-and-5hmc-with-simple-seq]] and [[10-Summaries/high-throughput-single-cell-dna-methylation-and-chromatin-accessibility-co-profiling-with-splicool-seq]]
- 8-nt SMRT-Tag barcode in [[10-Summaries/direct-transposition-of-native-dna-for-sensitive-multimodal-single-molecule-sequencing]]

## Related

- [[30-Concepts/duplex-sequencing]] · [[30-Concepts/combinatorial-indexing]] · [[40-Topics/duplex-sequencing]]
