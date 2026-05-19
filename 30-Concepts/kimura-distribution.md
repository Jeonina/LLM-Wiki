---
type: concept
title: Kimura distribution
aliases: [Kimura genetic drift distribution]
tags: [population-genetics, genetic-drift, mtDNA, statistics]
created: 2026-05-12
updated: 2026-05-12
---

# Kimura distribution

> A two-parameter probability distribution introduced by Motoo Kimura describing allele frequencies in a population subject to genetic drift. Used to model mtDNA heteroplasmy distributions across a population of cells, where each cell is treated as a "population" of mtDNA molecules.

## Definition

The Kimura distribution has parameters *p₀* (initial allele frequency) and *b* (segregation parameter, ≈ 1 − V′(h) where V′(h) is normalized variance). For a starting heteroplasmy p₀ and a level of genetic drift parameterized by b, the distribution predicts the steady-state allele-frequency distribution across cells.

## Why it matters

Fitting single-cell mtDNA heteroplasmy data to a Kimura distribution allows quantitative testing of whether observed variance is consistent with **random genetic drift alone** (no selection) or whether selective forces are at work.

## Examples

- Two pathogenic mt-tRNA-Ala mutations (m.5024C>T, m.5019A>G) — heteroplasmy distributions across thousands of mouse cells fit Kimura distributions at every developmental time point, indicating **drift, not selection**, is the dominant force ([[10-Summaries/glynos-2023-mtdna-mosaicism]]).

## Related

- [[30-Concepts/mitochondrial-heteroplasmy]] · [[30-Concepts/somatic-mosaicism]]
