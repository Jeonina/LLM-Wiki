---
type: concept
title: Chromosomal Instability
aliases: [CIN, ongoing aneuploidy, karyotype heterogeneity, aneuploidy]
tags: [CIN, aneuploidy, cancer, spindle-assembly-checkpoint, karyotype]
created: 2026-08-10
updated: 2026-10-07
---

# Chromosomal Instability

> The *rate* at which cells mis-segregate chromosomes — distinct from aneuploidy, which is the resulting *state*. Bulk assays measure the state; only single-cell karyotyping measures the rate.

## The distinction, demonstrated

Truncating the spindle-assembly-checkpoint kinase *Mps1* causes mitotic abnormalities in virtually every division, yet the resulting *p53*-null T-ALLs showed **highly similar karyotypes by array CGH** — recurrent gains of chromosomes 4, 9, 14 and 15 — implying clonal selection ([[bakker-2016-aneufinder]]). Single-cell sequencing resolved the paradox: the pooled profile is clonal while **56% of individual cells carry a unique karyotype** ([[bakker-2016-aneufinder]]).

Ongoing instability and a clonal-looking karyotype are therefore compatible: selection drives cells toward favourable chromosome combinations while mis-segregation keeps generating variants around that attractor (synthesis, following [[bakker-2016-aneufinder]]).

## Measuring it

A **heterogeneity score** (number of cells with distinct copy-number profiles) alongside an **aneuploidy score** (divergence from euploidy) turns CIN into a per-tumour quantity ([[bakker-2016-aneufinder]]). Human paediatric B-ALL samples show measurably different grades of karyotype heterogeneity, i.e. CIN rates differ between malignancies ([[bakker-2016-aneufinder]]).

## Why it matters

- More than two out of three cancers are aneuploid, despite aneuploidy causing physiological stress and growth defects in untransformed cells ([[bakker-2016-aneufinder]]).
- Genetic and phenotypic plasticity from aneuploidy evolution underlies treatment resistance and recurrence ([[wang-2021-medalt]]).
- Clonal dynamics across passages show minor clones vanishing and dominant clones diversifying between serial xenograft passages ([[zahn-2017-dlp]]).
- Somatic mosaicism including copy-number change occurs in pathologically normal tissue such as blood and esophagus, so distinguishing pathogenic from normal variation is a general problem, not a cancer-only one ([[wang-2021-medalt]]).

## Open questions

Whether karyotype heterogeneity predicts treatment outcome is proposed but not shown — the human data establish differing CIN rates without outcome data ([[bakker-2016-aneufinder]]).

## Added 2026-10-07

Single-cell WGS of 30,260 HGSOC tumour genomes measured CIN three ways — cell-specific CNAs on phylogenies, highly divergent 'hopeful monster' cells (38/41 patients, mean 2.6% of cells) and cGAS-positive ruptured micronuclei — all elevated after whole-genome doubling ([[10-Summaries/mcpherson-2025-ongoing-wgd]]). Ploidy-adjusted chromosome and arm losses were 2.6- and 2.4-fold higher in WGD-high 1×WGD cells than in WGD-low 0×WGD cells ([[10-Summaries/mcpherson-2025-ongoing-wgd]]). The CIN to cGAS-STING to interferon link held in WGD-low tumours but was decoupled in WGD-high tumours, which repressed STING1 ([[10-Summaries/mcpherson-2025-ongoing-wgd]]).

In a 260-cell TNBC xenograft CNA tree, *AKT1* was amplified repeatedly and *NTRK3* and *TBX3* were each deleted in two parallel lineages. The authors read this as chromosomal instability and as a reason for phylogenetic models to allow recurrent CNAs ([[10-Summaries/kuipers-2025-scicone]]).


## Related

- [[copy-number-variation]] · [[intratumor-heterogeneity]] · [[cancer-clonal-evolution]] · [[scdna-cancer-applications]]
