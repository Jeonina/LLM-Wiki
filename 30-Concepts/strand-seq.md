---
type: concept
title: Strand-seq
aliases: [strand sequencing, BrdU-strand-seq]
tags: [scDNA-seq, structural-variants, haplotype, sister-chromatid]
created: 2026-05-19
updated: 2026-05-19
---

# Strand-seq

> Single-cell DNA sequencing method that distinguishes parental Watson and Crick strands by selectively sequencing one (BrdU-labeled) strand per chromosome per cell ([[10-Summaries/falconer-2012-natmethods]]). Enables high-resolution detection of structural variants, sister-chromatid exchanges, and haplotype phasing in single cells.

## Method

Cells are grown for one division in BrdU-containing medium, then BrdU-labeled strands are selectively nicked. Sequencing of the surviving (parental) strand gives a per-cell strand inheritance pattern that reveals which chromatid each homolog inherited.

## Applications

- Detection of inversions, translocations, and sister-chromatid exchanges at single-cell resolution ([[10-Summaries/sanders-2020-sctrip]]).
- Haplotype-resolved genome assembly.
- Genome stability assays.

## Related

- [[30-Concepts/scdna-seq]] · [[30-Concepts/structural-variants]]
- [[40-Topics/scdna-seq]]
