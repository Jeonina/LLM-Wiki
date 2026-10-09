---
type: concept
title: Epigenetic aging
aliases: [methylation clock, Horvath clock, scAge]
tags: [aging, methylation, biomarker, single-cell]
created: 2026-05-12
updated: 2026-10-09
---

# Epigenetic aging

> The use of DNA methylation patterns at specific CpG sites to predict chronological or biological age. Horvath's multi-tissue clock (2013) was the original; later clocks (DNAm PhenoAge, GrimAge, PCPhenoAge) and the single-cell scAge framework extend the approach.

## Definition

A methylation clock is a weighted linear combination of methylation β-values at a small set of CpG sites (~300–500 for Horvath's clock). The weights are learned from arrays profiling cohorts of varying ages.

## Why it matters

- Predicts chronological age with median error <4 years across tissues.
- "Epigenetic age acceleration" (predicted > chronological) correlates with all-cause mortality, cancer risk, and disease incidence.
- **scAge** ([[10-Summaries/shen-2026-splicool-seq]]) extends to single cells: tumor subclones show accelerated epigenetic aging compared to surrounding normal cells.

## Added 2026-10-08 — sequence models & foundation models

- CpGPTGrimAge3, built from CpGPT-predicted plasma-protein proxies plus GrimAge2 proxies, ranked in the top two clocks in 30 of 34 mortality and disease comparisons across four cohorts ([[10-Summaries/delimacamillo-2024-cpgpt]]).
- Fine-tuned MethylGPT predicted multi-tissue age with a median absolute error of 4.45 years, stayed stable with up to 70% of CpGs missing, and showed different attention patterns for young and old samples ([[10-Summaries/ying-2024-methylgpt]]).

## Added 2026-10-09 — foundation-model gap evidence

- A sequence-to-function analysis of colonic-crypt somatic mutations found predicted per-gene expression effects orders of magnitude below the young-vs-old aging program, and the author argues that colonic transcriptional aging is better explained by epigenetic drift than by accumulated SNVs and short indels ([[10-Summaries/fischbach-2026-alphagenome-aging]])

## Related

- [[40-Topics/dna-methylation]] · [[30-Concepts/epigenetic-memory]] · [[40-Topics/dna-methylation]]
