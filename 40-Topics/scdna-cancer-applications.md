---
type: topic
title: scDNA-seq in cancer applications
aliases: [cancer scDNA-seq, single-cell oncology, tumor scDNA]
tags: [cancer, scDNA-seq, clonal-evolution, intratumor-heterogeneity]
created: 2026-05-19
updated: 2026-10-12
paper_section: ["5.1"]
---

# scDNA-seq in cancer applications

> Single-cell DNA sequencing in cancer research and clinical applications — intratumor heterogeneity, chemoresistance evolution, metastatic clonal lineage, copy-number phylogeny, and emerging clinical translation ([[10-Summaries/lim-2020-cancercell|Lim 2020]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

> [!abstract] 한눈에
> 종양을 세포 단위로 읽으면 클론 구성과 진화 순서, 항암제 내성이 원래 있던 것인지 새로 생긴 것인지를 가를 수 있다 ([[10-Summaries/navin-2011-sns-tumor-evolution|Navin 2011]]; [[10-Summaries/kim-2018-tnbc-chemoresistance|Kim 2018]]). 최근 copy-number 도구는 절대값과 allele·haplotype 단위, WGD까지 다루게 됐지만 ([[10-Summaries/wesley-2026-songbird|Songbird]]; [[10-Summaries/ivanovic-2025-cnrein|CNRein]]), 임상 적용은 아직 비용과 재현성에 막혀 있다 ([[10-Summaries/lim-2020-cancercell|Lim 2020]]).

## Key points

- **Copy-number change and point mutation follow different tempos.** In breast cancer, CNAs were punctuated while SNVs accumulated gradually, with a 13.3× mutation rate in the TNBC ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]); single-nucleus CNV profiles first exposed intratumor heterogeneity ([[10-Summaries/navin-2011-sns-tumor-evolution|Navin 2011]]).
- **Chemoresistance can be pre-existing or acquired.** Longitudinal scDNA + scRNA in TNBC separated the two ([[10-Summaries/kim-2018-tnbc-chemoresistance|Kim 2018]]).
- **WGD is ongoing in high-grade serous ovarian cancer.** DLP+ scWGS of 41 HGSOC patients found ongoing WGD, divergent cells, micronuclei and immune phenotypes ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- **Copy-number callers now target absolute, allele- or haplotype-specific and WGD-aware states.** ([[10-Summaries/wesley-2026-songbird|Songbird]]; [[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]; [[10-Summaries/ivanovic-2025-cnrein|CNRein]]; [[10-Summaries/zaccaria-2021-chisel|CHISEL]]).
- **Same-cell genome + chromatin links CNAs to regulatory change.** About 82% of subclonal chromatin-hub changes were in cis with CNAs, and CNAs inferred from ATAC alone were unreliable (median R = 0.47) ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/intratumor-heterogeneity|Intratumor heterogeneity]] — Genetic and phenotypic variation between cells within one tumour.
> - `concept` [[30-Concepts/copy-number-variation|Copy-number variation]] — Gains and losses of genomic segments; the most tractable single-cell readout.
> - `concept` [[30-Concepts/whole-genome-doubling|Whole-genome doubling]] — Duplication of the whole chromosome complement in a cell lineage.
> - `concept` [[30-Concepts/phylogenetic-inference|Phylogenetic inference]] — Reconstructing a cell-division tree from heritable markers.
> - `concept` [[30-Concepts/cancer-of-unknown-primary|Cancer of unknown primary]] — A cancer diagnosed by metastasis without an identifiable primary tumour.
> - `note` [[50-Notes/methylation-cancer-origin-classifiers|Methylation cancer-of-origin classifiers]] — Methylation as a clinical tissue-of-origin tool.

## Tumour studies

Single-cell studies of clonal structure, resistance and evolution in specific cancers, with one bulk landscape for contrast.

| Study | System | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/navin-2011-sns-tumor-evolution\|Navin 2011]] | Breast | Single-nucleus sequencing, CNV | Intratumor heterogeneity ([[10-Summaries/navin-2011-sns-tumor-evolution\|Navin 2011]]) |
| [[10-Summaries/wang-2014-nuc-seq\|Wang 2014]] | Breast | nuc-seq | Punctuated CNAs vs gradual SNVs; 13.3× TNBC mutation rate ([[10-Summaries/wang-2014-nuc-seq\|Wang 2014]]) |
| [[10-Summaries/gawad-2014-all-clonal-origins\|Gawad 2014]] | Childhood ALL | Single-cell targeted genotyping | Codominant clones in 5/6 patients; deletions before SNVs; late *KRAS* ([[10-Summaries/gawad-2014-all-clonal-origins\|Gawad 2014]]) |
| [[10-Summaries/kim-2018-tnbc-chemoresistance\|Kim 2018]] | TNBC | Longitudinal scDNA + scRNA through neoadjuvant chemotherapy | Pre-existing vs acquired resistance ([[10-Summaries/kim-2018-tnbc-chemoresistance\|Kim 2018]]) |
| [[10-Summaries/pellegrino-2018-tapestri\|Pellegrino 2018]] | AML | Tapestri targeted droplet panels | High-throughput targeted scDNA-seq ([[10-Summaries/pellegrino-2018-tapestri\|Tapestri]]) |
| [[10-Summaries/frankell-2019-eac-landscape\|Frankell 2019]] | Esophageal adenocarcinoma | Bulk, 551 tumours | Genomic landscape of EAC ([[10-Summaries/frankell-2019-eac-landscape\|Frankell 2019]]) |
| [[10-Summaries/mcpherson-2025-ongoing-wgd\|McPherson 2025]] | HGSOC, 41 patients | DLP+ scWGS | Ongoing WGD, divergent cells, micronuclei and immune phenotypes ([[10-Summaries/mcpherson-2025-ongoing-wgd\|McPherson 2025]]) |

## Copy-number calling and phylogeny

Copy-number phylogeny is one of the core cancer uses of scDNA-seq ([[10-Summaries/zaccaria-2021-chisel|CHISEL]]; [[10-Summaries/kaufmann-2022-medicc2|MEDICC2]]).

| Tool | Year | Input data | What it adds |
|---|---|---|---|
| [[10-Summaries/zaccaria-2021-chisel\|CHISEL]] | 2021 | Low-coverage scDNA-seq | Allele- and haplotype-specific copy numbers ([[10-Summaries/zaccaria-2021-chisel\|CHISEL]]) |
| [[10-Summaries/kaufmann-2022-medicc2\|MEDICC2]] | 2022 | Copy-number profiles | WGD-aware copy-number phylogenies ([[10-Summaries/kaufmann-2022-medicc2\|MEDICC2]]) |
| [[10-Summaries/kuipers-2025-scicone\|SCICoNE]] | 2025 | DLP and 10x single-cell CNV breast cancer data | Copy-number calling and CNA history ([[10-Summaries/kuipers-2025-scicone\|SCICoNE]]) |
| [[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]] | 2025 | Direct-tagmentation scWGS | Absolute and allele-specific CN; applied to a paediatric B-ALL, an ACT breast cancer (single-end reads) and an FFPE DCIS prepared with ARC-well ([[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]]) |
| [[10-Summaries/ivanovic-2025-cnrein\|CNRein]] | 2025 | DLP+ ovarian (OV2295), 10x breast (S0), matched 10x/ACT breast (TN3) | Haplotype-specific CN calling ([[10-Summaries/ivanovic-2025-cnrein\|CNRein]]) |
| [[10-Summaries/wesley-2026-songbird\|Songbird]] | 2026 | DLP+ and other Tn5 scWGS | Absolute, WGD-sensitive copy number; tested on an hTERT/HEK ploidy ladder and the CAM277 esophageal adenocarcinoma organoid ([[10-Summaries/wesley-2026-songbird\|Songbird]]) |

## Multimodal and spatial readouts

| Method | Year | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]] | 2024 (bioRxiv preprint) | Same-cell scDNA + scATAC; 2 normal breasts, 9 ER+ tumours | LumHR-derived ancestral clones; ~82% of subclonal chromatin-hub changes in cis with CNAs; ATAC-inferred CNAs unreliable (median R = 0.47) ([[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]]) |
| [[10-Summaries/pancikova-2025-splongget\|SPLONGGET]] | 2025 (preprint) | Genome-inclusive 10x Multiome on Nanopore, paediatric B-ALL | 3,800 single-cell CN profiles plus targeted per-cell genotyping ([[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]) |
| [[10-Summaries/zhao-2022-nature\|slide-DNA-seq]] | 2022 | Spatial genomics in tissue | Spatial and multimodal study of clonal heterogeneity ([[10-Summaries/zhao-2022-nature\|Zhao 2022]]) |

## Clinical translation and cancer predisposition

- **Cancer of unknown primary** is a target application ([[30-Concepts/cancer-of-unknown-primary]]).
- **Clinical translation** — circulating tumor cells and MRD detection ([[10-Summaries/lim-2020-cancercell|Lim 2020]]), tissue-of-origin classifiers ([[50-Notes/methylation-cancer-origin-classifiers]]).
- **Inherited predisposition.** HiDEF-seq profiles 17 samples across 8 inherited cancer predisposition syndromes and finds elevated single-strand mismatch burdens in *POLE* PPAP (2.6-fold) and CMMRD (1.6-fold), plus distinct patterns in tumours deficient in **both** mismatch repair and polymerase proofreading ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).

## Reviews

- [[10-Summaries/lim-2020-cancercell|Lim, Lin & Navin 2020]] — single-cell genomics in cancer research and medicine.
- [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]] — scDNA-seq for somatic mosaicism (*Nat Rev Genet*).
- [[10-Summaries/lu-2024-cnaphylogeny-review|Lu 2024]] — CNA-based cancer phylogenetics.
- [[10-Summaries/mallory-2020-cna-review|Mallory 2020]] — CNA detection from scDNA-seq.

## Open questions

- Clinical-grade scDNA-seq workflows — cost and reproducibility are still barriers ([[10-Summaries/lim-2020-cancercell|Lim 2020]]).
- Integration with clinical sequencing — bulk panels vs scDNA tradeoffs.
- Liquid biopsy with single-cell resolution.

## Related

> [!cards]
> - `hub` [[40-Topics/cancer-clonal-evolution|Cancer clonal evolution]] — Somatic mutation and clonal selection shaping tumour heterogeneity, treatment response and metastasis.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one body.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — Technologies that interrogate the DNA of single cells.

## All sources on this page

> [!info]- 21 summaries cited here
> - [[10-Summaries/frankell-2019-eac-landscape|Frankell 2019]]
> - [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]
> - [[10-Summaries/ivanovic-2025-cnrein|Ivanovic & El-Kebir 2025]]
> - [[10-Summaries/kaufmann-2022-medicc2|Kaufmann 2022]]
> - [[10-Summaries/kim-2018-tnbc-chemoresistance|Kim 2018]]
> - [[10-Summaries/kolbeinsdottir-2025-ascent|Kolbeinsdottir 2025]]
> - [[10-Summaries/kuipers-2025-scicone|Kuipers 2025]]
> - [[10-Summaries/lim-2020-cancercell|Lim & Navin 2020]]
> - [[10-Summaries/liu-2024-hidef-seq|Liu 2024]]
> - [[10-Summaries/lu-2024-cnaphylogeny-review|Lu 2024]]
> - [[10-Summaries/mallory-2020-cna-review|Mallory 2020]]
> - [[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]
> - [[10-Summaries/navin-2011-sns-tumor-evolution|Navin 2011]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/pellegrino-2018-tapestri|Pellegrino 2018]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/wang-2014-nuc-seq|Wang 2014]]
> - [[10-Summaries/wang-2024-wellda-seq|Wang 2024]]
> - [[10-Summaries/wesley-2026-songbird|Wesley 2026]]
> - [[10-Summaries/zaccaria-2021-chisel|Zaccaria 2021]]
> - [[10-Summaries/zhao-2022-nature|Zhao 2022]]
