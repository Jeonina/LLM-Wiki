---
type: concept
title: Mitochondrial heteroplasmy
aliases: [mtDNA heteroplasmy, mtDNA mosaicism]
tags: [mitochondria, mtDNA, mosaicism, genetic-drift]
created: 2026-05-12
updated: 2026-10-07
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
- **Single-cell mtDNA burden metrics** — scmtMPM (depth-normalized mutations per million bp) and scwMSS (heteroplasmy-weighted local-constraint score) introduced by [[10-Summaries/hsieh-2026-scmtmpm-scwmss]] for quantifying per-cell mutational load. POLG D274A hypermutator cells show ~15× more variants than POLG-wild-type control cells, with pathogenic variants held at sub-threshold VAF by negative selection ([[10-Summaries/hsieh-2026-scmtmpm-scwmss]]).

## Added 2026-10-07

In normal human tissues, rare mtDNA point-mutation prevalence (1.4 ± 1.3 × 10⁻⁵ per bp) was ~25-fold higher than nuclear, transition-dominated (89–97%) with strand bias, and rose with age (e.g. 30-fold in colon over 91 years); unlike nuclear DNA, mtDNA prevalence and spectra were unaffected by smoking or aristolochic-acid exposure [[10-Summaries/hoang-2016-botseqs]].

Long-read scWGS found a clone-specific heteroplasmy (chrM:16,218 C>T at 41–67% in three clone-B T cells, absent in clone A and in bulk), confirmed in Illumina data. 17% of mtDNA HiFi reads covered at least 25% of the mitochondrial genome, which makes phasing possible at the molecule level ([[10-Summaries/hard-2023-long-read-scwgs]]).


## Related

- [[30-Concepts/kimura-distribution]] · [[40-Topics/somatic-mosaicism]] · [[20-Entities/patrick-chinnery]]
