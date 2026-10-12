---
type: concept
title: SCOUT (Single Cell Genotyper Utilizing Information from Local Genome Territory)
aliases: [SCOUT]
tags: [single-cell, variant-calling, scWGA, software]
created: 2026-05-12
updated: 2026-10-12
---

# SCOUT

> A single-cell SNV caller (Tu et al. 2021) that classifies each candidate locus into homozygous, heterozygous, intermediate, or low-major-allele states using a four-component multinomial model that borrows information from **adjacent loci within the same cell** (local-territory smoothing).

> [!abstract] 한눈에
> SCOUT는 같은 세포 안 인접 locus 정보를 빌려 각 후보 SNV의 genotype 상태를 네 가지 중 하나로 분류하는 single-cell SNV caller다 ([[10-Summaries/tu-2021-scout-genotyper|SCOUT]]). 외부 bulk 데이터 없이 동작하므로 소수 clone 변이나 희귀 변이에 쓸 수 있다 ([[10-Summaries/tu-2021-scout-genotyper|SCOUT]]).

## Definition

For each candidate SNV at locus *s*, SCOUT estimates the multinomial allele-success probability *p* and the latent genotype *Z_s* ∈ {0,1,2,3} by fitting a model that pools information from neighboring SNVs (30 kb window) with exponentially decaying weights.

## Why it matters

- Independent of external bulk data — important for minor-clone variants or rare mutations not in bulk reference.
- 2–77.5% F1 improvement over GATK, SCcaller, Monovar.
- 400% faster than alternative single-cell callers.

## Examples

- [[10-Summaries/tu-2021-scout-genotyper]].

## Related

> [!cards]
> - `concept` [[30-Concepts/monovar|Monovar]] — Single-cell SNV caller that pools evidence across cells.
> - `concept` [[30-Concepts/sccaller|SCcaller]] — Single-cell SNV caller that exploits local linkage instead of independent loci.
> - `concept` [[30-Concepts/allele-dropout|Allele dropout]] — Loss of one allele during amplification, a core error source in single-cell SNV calling.
> - `concept` [[30-Concepts/scwga|scWGA]] — Single-cell whole-genome amplification, the source of the data SCOUT genotypes.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — The single-cell DNA sequencing field as a whole.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/tu-2021-scout-genotyper|Tu 2021]]
