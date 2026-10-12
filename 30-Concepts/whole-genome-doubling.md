---
type: concept
title: "Whole-Genome Doubling"
aliases: []
tags: []
created: 2026-10-07
updated: 2026-10-12
sources: ["[[10-Summaries/kaufmann-2022-medicc2]]", "[[10-Summaries/mcpherson-2025-ongoing-wgd]]"]
---

# Whole-Genome Doubling

> Whole-genome doubling (WGD) is the duplication of an entire chromosome complement in a cell lineage, found in more than 30% of solid cancers and linked to metastasis, drug resistance and poor outcomes ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).

> [!abstract] 한눈에
> WGD는 한 세포 계통에서 염색체 한 벌 전체가 복제되는 사건이고, single-cell WGS로 보면 한 종양 안에서도 계속 일어나는 과정이다 ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]). 다만 두 배가 된 세포는 read-depth 비율이 그대로라서 copy-number profile만으로는 잡기 어렵고, fragment overlap이나 read density로 절대 ploidy를 추정하는 방법들이 서로 다른 성능을 보고한다 ([[10-Summaries/wesley-2026-songbird|Songbird]]; [[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]; [[10-Summaries/schneider-2024-scabsolute|scAbsolute]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [종양 계통수 시뮬레이터](../60-Explainers/cancer-clonal-evolution.html)
>
> [암 연구의 scDNA-seq 교재](../60-Explainers/scdna-cancer-applications.html)
<!-- /explainer-links -->

## Definition

In single-cell WGS, WGD can be called per cell from allele-specific copy number: a cell with more than half its genome at two or more copies of the major allele (FM2 > 0.5) has undergone at least one WGD, and FM3 > 0.5 marks at least two ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).

## Why it matters

- WGD is an ongoing process rather than a single event: 40 of 41 high-grade serous ovarian cancer patients carried coexisting WGD multiplicities ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- WGD cells show higher ploidy-adjusted rates of chromosome and arm losses and gains, and WGD-high tumours have a 3.3-fold higher rate of cGAS-positive ruptured micronuclei ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]) — see [[chromosomal-instability]].
- Despite more chromosomal instability, WGD-high tumours show STING1 repression and reduced interferon signalling ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- Pseudo-triploid HGSOC karyotypes are inferred to arise from WGD plus pre- and post-WGD losses rather than incremental gains ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).

## Modelling WGD histories

- Truncal, parallel, subclonal and unexpanded WGD histories were distinguished by SNV-based timing (doubleTime) in 39 patients ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- WGD-aware copy-number phylogenies model doubling explicitly ([[10-Summaries/kaufmann-2022-medicc2|MEDICC2]]).
- CNRein models WGD as one of its CNA actions, doubling all copy numbers ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]).

## Detecting WGD in single cells

Read-depth-ratio callers cannot detect WGD, because a doubled cell has the same depth ratios between regions as an undoubled one ([[10-Summaries/wesley-2026-songbird|Songbird]]). Methods differ in which signal they use to recover absolute ploidy:

| Signal | Example | How it works | Blind spot | Source |
|---|---|---|---|---|
| Allele-specific copy number | FM2/FM3 thresholds | Fraction of the genome at ≥2 (or ≥3) copies of the major allele | — | ([[10-Summaries/mcpherson-2025-ongoing-wgd\|McPherson 2025]]) |
| B-allele frequency | CHISEL | Needs mutations to accumulate on different alleles | Cannot detect a recent WGD with no later copy-number change; balanced doublings carry no allelic imbalance and can be missed | ([[10-Summaries/schneider-2024-scabsolute\|scAbsolute]]; [[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]]) |
| Fragment geometry | [[10-Summaries/wesley-2026-songbird\|Songbird]] | In amplification-free Tn5 libraries, fragments overlapping a reference fragment can come only from the other n − 1 copies, so overlap density over upstream density approaches (n − 1)/n; within each breakpoint-defined subclone, cells near a 1:2 ploidy ratio to the rest are flagged as WGD | — | ([[10-Summaries/wesley-2026-songbird\|Songbird]]) |
| Fragment overlap rate | [[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]] | In direct-tagmentation scWGS, the rate of fragment overlap rises with copy number | — | ([[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]]) |
| Read density | [[10-Summaries/schneider-2024-scabsolute\|scAbsolute]] | Overlapping unique reads are capped by the number of physical DNA copies, so read density at a given read depth separates G1 cells from G2, WGD or multiplet cells; works from read density alone in amplification-free, paired-end DLP/ACT-type data | Cannot tell G2 from WGD cells without extra information such as Geminin staining | ([[10-Summaries/schneider-2024-scabsolute\|scAbsolute]]) |

## Evidence and examples

- 40 of 41 HGSOC patients carried coexisting WGD multiplicities ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- Songbird's median ploidy was accurate up to 6 on a [[dlp-plus|DLP+]] hTERT/HEK293T ladder, and only Songbird and ASCENT called the 2× hTERT wells correctly ([[10-Summaries/wesley-2026-songbird|Songbird]]).
- ASCENT used fragment overlap to flag S-phase, G2M and multiplet HCT116 cells at P < 1%, while scAbsolute missed 89% of G2M cells ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]).
- scAbsolute reached 97% G1 vs 6N–12N accuracy in PEO1 multiplets ([[10-Summaries/schneider-2024-scabsolute|scAbsolute]]).

## Open questions

- **Callers can disagree on whether WGD happened at all.** On DLP+ ovarian cancer OV2295, Alleloscope called no WGD while CNRein, SIGNALS and CHISEL called WGD in many cells ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]). Truncal-SNV VAFs peaked at 1/3 and 2/3 in {2,1} regions for the WGD-calling methods but near 1/2 for Alleloscope, which supports WGD ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]).
- Whether STING1 repression precedes WGD is untested ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- Perfectly doubled cells are hard to distinguish from their non-doubled counterparts in single-cell copy-number data, so 2×WGD frequency may be underestimated (synthesis).
- Fragment-overlap ploidy estimation needs no SNPs or copy-number variation, so it can in principle call perfectly doubled cells. Songbird recovered doubled diploid genomes (2× hTERT wells), but its WGD module has not yet been tested in tumours with mixed WGD multiplicities ([[10-Summaries/wesley-2026-songbird|Songbird]]; (synthesis)).
- scAbsolute addresses this for amplification-free, paired-end data. Overlapping unique reads are capped by the number of physical DNA copies, so read density at a given read depth separates G1 cells from G2, WGD or multiplet cells that look the same in copy-number profiles: 97% G1 vs 6N–12N accuracy in PEO1 multiplets ([[10-Summaries/schneider-2024-scabsolute]]). It still cannot tell G2 from WGD cells without extra information such as Geminin staining ([[10-Summaries/schneider-2024-scabsolute]]).
- **Disagreement over scAbsolute's G2/WGD detection.** Its authors report 97% accuracy separating G1 cells from 6N–12N multiplets in PEO1 ([[10-Summaries/schneider-2024-scabsolute]]). The ASCENT authors report that scAbsolute missed 89% of G2M cells in sorted HCT116 ([[10-Summaries/kolbeinsdottir-2025-ascent]]), and the Songbird ploidy ladder found it tended to call 2× and 3× hTERT wells diploid ([[10-Summaries/wesley-2026-songbird]]). The competing benchmarks ran scAbsolute outside its original setup (e.g. GRCh38 at 1 Mb in the ASCENT run), so whether this is a method limit or a regime mismatch is unresolved (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/copy-number-variation|Copy number variation]] — Gains and losses of genomic segments; why absolute ploidy is underdetermined.
> - `concept` [[30-Concepts/chromosomal-instability|Chromosomal instability]] — The rate of mis-segregation, as opposed to aneuploidy, the resulting state.
> - `concept` [[30-Concepts/dlp-plus|DLP+]] — High-throughput Tn5 scWGS for large-scale single-cell CNV and chromosomal phylogenetics.
> - `hub` [[40-Topics/cancer-clonal-evolution|Cancer clonal evolution]] — Somatic mutation and clonal selection reconstructed from bulk and single-cell DNA.

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/ivanovic-2025-cnrein|Ivanovic & El-Kebir 2025]]
> - [[10-Summaries/kaufmann-2022-medicc2|Kaufmann 2022]]
> - [[10-Summaries/kolbeinsdottir-2025-ascent|Kolbeinsdottir 2025]]
> - [[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]
> - [[10-Summaries/schneider-2024-scabsolute|Schneider 2024]]
> - [[10-Summaries/wesley-2026-songbird|Wesley 2026]]
