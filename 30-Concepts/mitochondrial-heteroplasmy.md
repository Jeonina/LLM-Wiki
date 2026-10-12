---
type: concept
title: Mitochondrial heteroplasmy
aliases: [mtDNA heteroplasmy, mtDNA mosaicism]
tags: [mitochondria, mtDNA, mosaicism, genetic-drift]
created: 2026-05-12
updated: 2026-10-12
---

# Mitochondrial heteroplasmy

> A cell containing a mixed population of mtDNA molecules — some carrying a variant, some carrying the wild-type allele — at a heteroplasmy fraction (HF) between 0% and 100%. Healthy humans typically carry low-level heteroplasmy at <2% of mtDNA molecules; pathogenic mutations cause disease when they cross a cell-type-specific biochemical threshold.

> [!abstract] 한눈에
> Mitochondrial heteroplasmy는 한 세포 안에 변이 mtDNA와 정상 mtDNA가 섞여 있는 상태이고, 그 비율은 같은 개체 안에서도 세포마다 따로 달라진다 ([[10-Summaries/glynos-2023-mtdna-mosaicism|Glynos 2023]]). 세포 분열과 무관한 relaxed replication이 분열 조직과 비분열 조직 모두에서 이 분산을 키우는 주된 원인이다 ([[10-Summaries/glynos-2023-mtdna-mosaicism|Glynos 2023]]).

## Definition

Each cell has hundreds to thousands of mtDNA copies (vs two for nuclear DNA). The fraction of mtDNA molecules carrying a mutation can vary independently between cells in the same individual.

## Why it matters

- Heteroplasmy levels determine clinical severity in mitochondrial disease.
- mtDNA mutations are heritable through the maternal germ line but undergo a developmental "bottleneck" — small numbers of mtDNA molecules pass to each oocyte, leading to large heteroplasmy variance in offspring.
- mtDNA mutations accumulate with age in somatic tissues, contributing to Parkinson's disease and other late-onset disorders.

## How heteroplasmy variance arises

| Mechanism | What drives variance | Source |
|---|---|---|
| Vegetative segregation | Heteroplasmy variance increasing through cell division | — |
| Relaxed replication | mtDNA destruction-and-resynthesis independent of cell cycle; the dominant driver in both dividing and non-dividing tissues | ([[10-Summaries/glynos-2023-mtdna-mosaicism\|Glynos 2023]]) |

## Measuring per-cell burden

- **Single-cell mtDNA burden metrics** — scmtMPM (depth-normalized mutations per million bp) and scwMSS (heteroplasmy-weighted local-constraint score) quantify per-cell mutational load ([[10-Summaries/hsieh-2026-scmtmpm-scwmss|Hsieh 2026]]).
- **Long reads allow molecule-level phasing** — 17% of mtDNA HiFi reads covered at least 25% of the mitochondrial genome ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).

## Evidence and examples

**Disease mutations**

- MELAS (m.3243A>G), MERRF (m.8344A>G), Leigh syndrome (multiple mtDNA mutations).
- In 818 cells from a MERRF patient line, 8344A>G heteroplasmy spanned 0–100% (median 38%, bulk 44%), and MEF2A/MEF2C activity was anticorrelated with it ([[10-Summaries/ludwig-2020-mtscatac-seq|mtscATAC-seq]]).
- m.5024C>T and m.5019A>G mt-tRNA-Ala mutations in mouse models — single-cell heteroplasmy variance increases from prenatal to P365 ([[10-Summaries/glynos-2023-mtdna-mosaicism|Glynos 2023]]).

**Selection and mutation rate**

- POLG D274A hypermutator cells show ~15× more variants than POLG-wild-type control cells, with pathogenic variants held at sub-threshold VAF by negative selection ([[10-Summaries/hsieh-2026-scmtmpm-scwmss|Hsieh 2026]]).
- In normal human tissues, rare mtDNA point-mutation prevalence (1.4 ± 1.3 × 10⁻⁵ per bp) was ~25-fold higher than nuclear, transition-dominated (89–97%) with strand bias, and rose with age (e.g. 30-fold in colon over 91 years) ([[10-Summaries/hoang-2016-botseqs|BotSeqS]]).
- Unlike nuclear DNA, mtDNA mutation prevalence and spectra were unaffected by smoking or aristolochic-acid exposure ([[10-Summaries/hoang-2016-botseqs|BotSeqS]]).

**Clone-specific heteroplasmy**

- Long-read scWGS found a clone-specific heteroplasmy (chrM:16,218 C>T at 41–67% in three clone-B T cells, absent in clone A and in bulk), confirmed in Illumina data ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/kimura-distribution|Kimura distribution]] — Drift model for allele frequencies, used for mtDNA heteroplasmy distributions.
> - `concept` [[30-Concepts/mitochondrial-lineage-tracing|Mitochondrial lineage tracing]] — Somatic mtDNA variants as natural lineage barcodes.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct lineages within one organism.
> - `entity` [[20-Entities/patrick-chinnery|Patrick Chinnery]] — Mitochondrial-disease researcher; pioneer of single-cell heteroplasmy quantification.

## All sources on this page

> [!info]- 5 summaries cited here
> - [[10-Summaries/glynos-2023-mtdna-mosaicism|Glynos 2023]]
> - [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]
> - [[10-Summaries/hoang-2016-botseqs|Hoang 2016]]
> - [[10-Summaries/hsieh-2026-scmtmpm-scwmss|Hsieh 2026]]
> - [[10-Summaries/ludwig-2020-mtscatac-seq|Lareau & Ludwig 2021]]
