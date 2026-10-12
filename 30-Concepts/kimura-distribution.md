---
type: concept
title: Kimura distribution
aliases: [Kimura genetic drift distribution]
tags: [population-genetics, genetic-drift, mtDNA, statistics]
created: 2026-05-12
updated: 2026-10-12
---

# Kimura distribution

> A two-parameter probability distribution introduced by Motoo Kimura describing allele frequencies in a population subject to genetic drift. Used to model mtDNA heteroplasmy distributions across a population of cells, where each cell is treated as a "population" of mtDNA molecules.

> [!abstract] 한눈에
> Kimura distribution은 genetic drift만 작용할 때 집단 안 allele 빈도가 어떻게 퍼지는지를 나타내는 분포로, 세포 하나를 mtDNA 분자의 집단으로 보고 heteroplasmy 분포에 적용한다. 생쥐 세포 수천 개의 mt-tRNA-Ala 돌연변이 heteroplasmy가 모든 발달 시점에서 이 분포에 맞아, selection보다 drift가 주된 힘으로 해석되었다 ([[10-Summaries/glynos-2023-mtdna-mosaicism|Glynos 2023]]).

## Definition

The Kimura distribution has parameters *p₀* (initial allele frequency) and *b* (segregation parameter, ≈ 1 − V′(h) where V′(h) is normalized variance). For a starting heteroplasmy p₀ and a level of genetic drift parameterized by b, the distribution predicts the steady-state allele-frequency distribution across cells.

## Why it matters

Fitting single-cell mtDNA heteroplasmy data to a Kimura distribution allows quantitative testing of whether observed variance is consistent with **random genetic drift alone** (no selection) or whether selective forces are at work.

## Examples

- Two pathogenic mt-tRNA-Ala mutations (m.5024C>T, m.5019A>G) — heteroplasmy distributions across thousands of mouse cells fit Kimura distributions at every developmental time point, indicating **drift, not selection**, is the dominant force ([[10-Summaries/glynos-2023-mtdna-mosaicism|Glynos 2023]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/mitochondrial-heteroplasmy|Mitochondrial heteroplasmy]] — A cell's mixed population of variant and wild-type mtDNA, the quantity the distribution models.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one organism.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/glynos-2023-mtdna-mosaicism|Glynos 2023]]
