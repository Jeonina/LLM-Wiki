---
type: concept
title: Epigenetic aging
aliases: [methylation clock, Horvath clock, scAge]
tags: [aging, methylation, biomarker, single-cell]
created: 2026-05-12
updated: 2026-05-12
---

# Epigenetic aging

> The use of DNA methylation patterns at specific CpG sites to predict chronological or biological age. Horvath's multi-tissue clock (2013) was the original; later clocks (DNAm PhenoAge, GrimAge, PCPhenoAge) and the single-cell scAge framework extend the approach.

## Definition

A methylation clock is a weighted linear combination of methylation β-values at a small set of CpG sites (~300–500 for Horvath's clock). The weights are learned from arrays profiling cohorts of varying ages.

## Why it matters

- Predicts chronological age with median error <4 years across tissues.
- "Epigenetic age acceleration" (predicted > chronological) correlates with all-cause mortality, cancer risk, and disease incidence.
- **scAge** ([[10-Summaries/shen-2026-splicool-seq]]) extends to single cells: tumor subclones show accelerated epigenetic aging compared to surrounding normal cells.

## Related

- [[40-Topics/dna-methylation]] · [[30-Concepts/epigenetic-memory]] · [[40-Topics/dna-methylation]]
