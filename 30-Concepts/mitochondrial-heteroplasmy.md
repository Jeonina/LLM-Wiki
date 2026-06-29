---
type: concept
title: Mitochondrial heteroplasmy
aliases: [mtDNA heteroplasmy, mtDNA mosaicism]
tags: [mitochondria, mtDNA, mosaicism, genetic-drift]
created: 2026-05-12
updated: 2026-05-12
---

# Mitochondrial heteroplasmy

> A cell containing a mixed population of mtDNA molecules — some carrying a variant, some carrying the wild-type allele — at a heteroplasmy fraction (HF) between 0% and 100%. Healthy humans typically carry low-level heteroplasmy at <2% of mtDNA molecules; pathogenic mutations cause disease when they cross a cell-type-specific biochemical threshold.

## Definition

Each cell has hundreds to thousands of mtDNA copies (vs two for nuclear DNA). The fraction of mtDNA molecules carrying a mutation can vary independently between cells in the same individual.

## Why it matters

- Heteroplasmy levels determine clinical severity in mitochondrial disease.
- mtDNA mutations are heritable through the maternal germ line but undergo a developmental "bottleneck" — small numbers of mtDNA molecules pass to each oocyte, leading to large heteroplasmy variance in offspring.
- mtDNA mutations accumulate with age in somatic tissues, contributing to Parkinson's disease and other late-onset disorders.

## Variants and refinements

- **Vegetative segregation**: heteroplasmy variance increasing through cell division.
- **Relaxed replication**: heteroplasmy variance from mtDNA destruction-and-resynthesis independent of cell cycle. [[10-Summaries/glynos-2023-mtdna-mosaicism]] shows this is the dominant driver in both dividing and non-dividing tissues.

## Examples

- m.5024C>T and m.5019A>G mt-tRNA-Ala mutations in mouse models — single-cell heteroplasmy variance increases from prenatal to P365 ([[10-Summaries/glynos-2023-mtdna-mosaicism]]).
- MELAS (m.3243A>G), MERRF (m.8344A>G), Leigh syndrome (multiple mtDNA mutations).
- **Single-cell mtDNA burden metrics** — scmtMPM (depth-normalized mutations per million bp) and scwMSS (heteroplasmy-weighted local-constraint score) introduced by [[10-Summaries/hsieh-2026-scmtmpm-scwmss]] for quantifying per-cell mutational load. POLG D274A hypermutator cells show ~15× more variants than bulk-seq detected, with pathogenic variants held at sub-threshold VAF by negative selection ([[10-Summaries/hsieh-2026-scmtmpm-scwmss]]).

## Related

- [[30-Concepts/kimura-distribution]] · [[40-Topics/somatic-mosaicism]] · [[40-Topics/somatic-mosaicism]] · [[20-Entities/patrick-chinnery]]
