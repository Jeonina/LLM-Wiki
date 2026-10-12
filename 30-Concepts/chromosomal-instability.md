---
type: concept
title: Chromosomal Instability
aliases: [CIN, ongoing aneuploidy, karyotype heterogeneity, aneuploidy]
tags: [CIN, aneuploidy, cancer, spindle-assembly-checkpoint, karyotype]
created: 2026-08-10
updated: 2026-10-12
---

# Chromosomal Instability

> The *rate* at which cells mis-segregate chromosomes — distinct from aneuploidy, which is the resulting *state*; bulk assays measure the state, and only single-cell karyotyping measures the rate ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]).

> [!abstract] 한눈에
> CIN은 염색체를 잘못 분리하는 속도이고, aneuploidy는 그 결과로 남은 상태다. bulk 핵형이 clonal해 보여도 single-cell로 보면 세포 절반 이상이 고유한 핵형을 가질 수 있어서, CIN은 single-cell 핵형 분석으로만 잴 수 있다 ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]; [[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [종양 계통수 시뮬레이터](../60-Explainers/cancer-clonal-evolution.html)
<!-- /explainer-links -->

## Definition

Chromosomal instability is the rate at which cells mis-segregate chromosomes; aneuploidy is the resulting state ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]). The two are easily confused because a tumour can look karyotypically clonal in bulk while individual cells keep changing ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]).

Truncating the spindle-assembly-checkpoint kinase *Mps1* causes mitotic abnormalities in virtually every division, yet the resulting *p53*-null T-ALLs showed highly similar karyotypes by array CGH — recurrent gains of chromosomes 4, 9, 14 and 15 — implying clonal selection ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]). Single-cell sequencing resolved the paradox: the pooled profile is clonal while 56% of individual cells carry a unique karyotype ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]).

Ongoing instability and a clonal-looking karyotype are therefore compatible: selection drives cells toward favourable chromosome combinations while mis-segregation keeps generating variants around that attractor (synthesis, following [[10-Summaries/bakker-2016-aneufinder|AneuFinder]]).

## Why it matters

- More than two out of three cancers are aneuploid, despite aneuploidy causing physiological stress and growth defects in untransformed cells ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]).
- Genetic and phenotypic plasticity from aneuploidy evolution underlies treatment resistance and recurrence ([[10-Summaries/wang-2021-medalt|MEDALT]]).
- Somatic mosaicism including copy-number change occurs in pathologically normal tissue such as blood and oesophagus, so distinguishing pathogenic from normal variation is a general problem, not a cancer-only one ([[10-Summaries/wang-2021-medalt|MEDALT]]).
- Because CIN makes cancer-cell ploidy vary, per-cell ploidy must be estimated before copy-number calling, phylogenetics or SNV analysis ([[10-Summaries/schneider-2024-scabsolute|scAbsolute]]); see [[copy-number-variation]].

## Measuring it

| Measure | What it captures | Source |
|---|---|---|
| Heterogeneity score plus aneuploidy score | Number of cells with distinct copy-number profiles, alongside divergence from euploidy; together they turn CIN into a per-tumour quantity | ([[10-Summaries/bakker-2016-aneufinder\|AneuFinder]]) |
| Cell-specific CNAs on phylogenies | Recent, unshared copy-number events per cell | ([[10-Summaries/mcpherson-2025-ongoing-wgd\|McPherson 2025]]) |
| Highly divergent "hopeful monster" cells | Cells far from any clone's karyotype | ([[10-Summaries/mcpherson-2025-ongoing-wgd\|McPherson 2025]]) |
| cGAS-positive ruptured micronuclei | A cellular footprint of mis-segregation | ([[10-Summaries/mcpherson-2025-ongoing-wgd\|McPherson 2025]]) |
| Recurrent CNAs in parallel lineages of a CNA tree | The same locus altered independently more than once | ([[10-Summaries/kuipers-2025-scicone\|SCICoNE]]) |
| Per-cell absolute ploidy | The baseline that every downstream copy-number call depends on | ([[10-Summaries/schneider-2024-scabsolute\|scAbsolute]]) |

## Evidence and examples

- Human paediatric B-ALL samples show measurably different grades of karyotype heterogeneity, i.e. CIN rates differ between malignancies ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]).
- Clonal dynamics across passages show minor clones vanishing and dominant clones diversifying between serial xenograft passages ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- Single-cell WGS of 30,260 HGSOC tumour genomes measured CIN three ways — cell-specific CNAs on phylogenies, hopeful-monster cells (38/41 patients, mean 2.6% of cells) and cGAS-positive ruptured micronuclei — and all were elevated after whole-genome doubling ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- Ploidy-adjusted chromosome and arm losses were 2.6- and 2.4-fold higher in WGD-high 1×WGD cells than in WGD-low 0×WGD cells ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- The CIN → cGAS-STING → interferon link held in WGD-low tumours but was decoupled in WGD-high tumours, which repressed STING1 ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- In a 260-cell TNBC xenograft CNA tree, *AKT1* was amplified repeatedly and *NTRK3* and *TBX3* were each deleted in two parallel lineages; the authors read this as chromosomal instability and as a reason for phylogenetic models to allow recurrent CNAs ([[10-Summaries/kuipers-2025-scicone|SCICoNE]]).
- scAbsolute estimates per-cell ploidy from shallow scDNA-seq alone, with a 5% mean wrong-ploidy rate on ACT breast-cancer data versus 11% (CHISEL), 16% (HMMCopy) and 27% (Ginkgo) ([[10-Summaries/schneider-2024-scabsolute|scAbsolute]]).

## Open questions

- **Does karyotype heterogeneity predict outcome?** This is proposed but not shown — the human data establish differing CIN rates without outcome data ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/copy-number-variation|Copy number variation]] — Gains and losses of genomic segments, the state CIN produces.
> - `concept` [[30-Concepts/intratumor-heterogeneity|Intratumor heterogeneity]] — Variation between cells within one tumour.
> - `hub` [[40-Topics/cancer-clonal-evolution|Cancer clonal evolution]] — Somatic mutation and clonal selection reconstructed from bulk and single-cell DNA.
> - `hub` [[40-Topics/scdna-cancer-applications|scDNA cancer applications]] — What single-cell DNA sequencing has shown in cancer.

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/bakker-2016-aneufinder|Bakker 2016]]
> - [[10-Summaries/kuipers-2025-scicone|Kuipers 2025]]
> - [[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]
> - [[10-Summaries/schneider-2024-scabsolute|Schneider 2024]]
> - [[10-Summaries/wang-2021-medalt|Wang 2021]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
