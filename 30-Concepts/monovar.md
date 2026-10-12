---
type: concept
title: Monovar
aliases: []
tags: [single-cell, variant-calling, software]
created: 2026-05-12
updated: 2026-10-12
---

# Monovar

> A single-cell SNV caller (Zafar et al. 2016) that integrates base count information across multiple cells to correct for uneven allele coverage caused by scWGA amplification bias. Assumes independent loci ([[10-Summaries/zafar-2016-monovar|Monovar]]).

> [!abstract] 한눈에
> Monovar는 여러 세포의 base count를 함께 써서 scWGA 증폭 편향과 allele dropout을 보정하는 초기 single-cell SNV caller이다 ([[10-Summaries/zafar-2016-monovar|Monovar]]). 이후 benchmark에서는 precision은 비슷하지만 recall이 크게 낮았다 ([[10-Summaries/kang-2022-sieve|SIEVE]]).

## Definition

Monovar treats each locus as independently sampled across all cells in the dataset; this multi-cell pooling helps calibrate genotype likelihoods when individual cells suffer amplification dropout ([[10-Summaries/zafar-2016-monovar|Monovar]]).

## Why it matters

- One of the first single-cell SNV callers; reference benchmark for newer methods like SCcaller and SCOUT ([[10-Summaries/zafar-2016-monovar|Monovar]]).
- Fails when minor clones or rare variants make multi-cell pooling unreliable.
- In SIEVE's benchmarks Monovar had precision comparable to SIEVE but much lower recall, more missing entries and more (likely false) double-mutant calls, and its F1 dropped in proportion to the amount of CNA sites included ([[10-Summaries/kang-2022-sieve|SIEVE]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/scout-variant-caller|SCOUT]] — Single-cell SNV caller using a four-component multinomial genotype model.
> - `concept` [[30-Concepts/sccaller|SCcaller]] — Single-cell SNV caller that calibrates allele dropout from nearby bulk heterozygous SNVs.
> - `concept` [[30-Concepts/scwga|scWGA]] — Single-cell whole-genome amplification, the source of the biases Monovar models.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — Technologies that interrogate the DNA of single cells.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/kang-2022-sieve|Kang 2022]]
> - [[10-Summaries/zafar-2016-monovar|Zafar 2016]]
