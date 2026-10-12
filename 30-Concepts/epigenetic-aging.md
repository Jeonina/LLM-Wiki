---
type: concept
title: Epigenetic aging
aliases: [methylation clock, Horvath clock, scAge]
tags: [aging, methylation, biomarker, single-cell]
created: 2026-05-12
updated: 2026-10-12
---

# Epigenetic aging

> The use of DNA methylation patterns at specific CpG sites to predict chronological or biological age. Horvath's multi-tissue clock (2013) was the original; later clocks (DNAm PhenoAge, GrimAge, PCPhenoAge) and the single-cell scAge framework ([[10-Summaries/shen-2026-splicool-seq|SpliCOOL-seq]]) extend the approach.

> [!abstract] 한눈에
> Epigenetic aging은 특정 CpG의 methylation 수준으로 나이를 예측하는 methylation clock 접근이고, single-cell에서는 tumor subclone이 주변 정상 세포보다 빠르게 늙는 것으로 나타났다 ([[10-Summaries/shen-2026-splicool-seq|SpliCOOL-seq]]). 최근에는 CpGPT, MethylGPT 같은 methylation foundation model도 clock을 만들거나 나이를 예측한다 ([[10-Summaries/delimacamillo-2024-cpgpt|CpGPT]]; [[10-Summaries/ying-2024-methylgpt|MethylGPT]]).

## Definition

A methylation clock is a weighted linear combination of methylation β-values at a small set of CpG sites (~300–500 for Horvath's clock). The weights are learned from arrays profiling cohorts of varying ages.

## Why it matters

- Predicts chronological age with median error <4 years across tissues.
- "Epigenetic age acceleration" (predicted > chronological) correlates with all-cause mortality, cancer risk, and disease incidence.
- Applied to single cells, it links epigenetic aging clocks to cancer progression: tumor subclones show accelerated epigenetic aging compared to surrounding normal cells ([[10-Summaries/shen-2026-splicool-seq|SpliCOOL-seq]]).

## Approaches

| Approach | Example | What it shows | Source |
|---|---|---|---|
| Array-based linear clock | Horvath multi-tissue clock; DNAm PhenoAge, GrimAge, PCPhenoAge | Weighted CpG β-values predict chronological or biological age | — |
| Single-cell clock | scAge framework, applied in [[10-Summaries/shen-2026-splicool-seq\|SpliCOOL-seq]] | Per-cell epigenetic age; tumor subclones age faster than surrounding normal cells | ([[10-Summaries/shen-2026-splicool-seq\|SpliCOOL-seq]]) |
| Foundation-model-derived clock | CpGPTGrimAge3 ([[10-Summaries/delimacamillo-2024-cpgpt\|CpGPT]]) | Built from CpGPT-predicted plasma-protein proxies plus GrimAge2 proxies | ([[10-Summaries/delimacamillo-2024-cpgpt\|CpGPT]]) |
| Fine-tuned methylation foundation model | [[10-Summaries/ying-2024-methylgpt\|MethylGPT]] | Multi-tissue age prediction robust to missing CpGs | ([[10-Summaries/ying-2024-methylgpt\|MethylGPT]]) |

## Evidence and examples

- CpGPTGrimAge3 ranked in the top two clocks in 30 of 34 mortality and disease comparisons across four cohorts ([[10-Summaries/delimacamillo-2024-cpgpt|CpGPT]]).
- Fine-tuned MethylGPT predicted multi-tissue age with a median absolute error of 4.45 years, stayed stable with up to 70% of CpGs missing, and showed different attention patterns for young and old samples ([[10-Summaries/ying-2024-methylgpt|MethylGPT]]).
- In SpliCOOL-seq, tumor subclones showed accelerated epigenetic aging compared to surrounding normal cells ([[10-Summaries/shen-2026-splicool-seq|SpliCOOL-seq]]).

## Contested points

- **Drift versus mutation as the driver of aging.** A sequence-to-function analysis of colonic-crypt somatic mutations found predicted per-gene expression effects orders of magnitude below the young-vs-old aging program, and the author argues that colonic transcriptional aging is better explained by epigenetic drift than by accumulated SNVs and short indels ([[10-Summaries/fischbach-2026-alphagenome-aging|Fischbach 2026]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/epigenetic-memory|Epigenetic memory]] — Mitotically heritable record of past cell states in methylation and chromatin.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation chemistry, assays and single-cell readouts.

## All sources on this page

> [!info]- 4 summaries cited here
> - [[10-Summaries/delimacamillo-2024-cpgpt|CpGPT 2024]]
> - [[10-Summaries/fischbach-2026-alphagenome-aging|Fischbach 2026]]
> - [[10-Summaries/shen-2026-splicool-seq|Shen 2026]]
> - [[10-Summaries/ying-2024-methylgpt|MethylGPT 2024]]
