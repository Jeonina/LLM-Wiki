---
type: topic
title: Brain somatic mosaicism
aliases: [neuronal mosaicism, brain mosaicism, BSMN]
tags: [brain, mosaicism, neurons, Walsh-lab, BSMN, Alzheimers, autism]
created: 2026-05-19
updated: 2026-10-12
paper_section: ["5.2"]
---

# Brain somatic mosaicism

> Somatic mutations accumulating in human neurons and other brain cells throughout life. Fetal-progenitor SNVs (~200–400/cell) plus age-related accumulation produce a distinct mosaicism profile per neuron. Implicated in normal aging, Alzheimer's disease, autism, and brain tumors ([[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto 2022]]; [[10-Summaries/lodato-2017-aging-neurons|Lodato 2018]]).

> [!abstract] 한눈에
> 뉴런은 발생기에 생긴 SNV 위에 나이에 따라 체세포 변이를 계속 쌓으며, 축적 속도 추정치는 증폭 화학이 좋아질수록 낮아져 PTA와 duplex 계열에서 연 16개 안팎으로 모였다 ([[10-Summaries/lodato-2017-aging-neurons|Lodato 2018]]; [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]). 속도와 클론 구조는 세포 유형마다 달라 oligodendrocyte가 excitatory neuron보다 빠르게 변이를 쌓는다 ([[10-Summaries/kriz-2025-duplex-multiome|Kriz 2025]]).

## Key points

- **Neurons accumulate somatic SNVs with age.** In 159 MDA single neurons, ~23 sSNVs/year in PFC and ~40/year in DG, with a replication-independent clocklike signature ([[10-Summaries/lodato-2017-aging-neurons|Lodato 2018]]).
- **Better chemistry gave lower rates.** SCAN2 on 52 PTA neurons revised the rate to 16.5 SNVs/year ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]), META-CS found ~16 SNVs/year ([[10-Summaries/xing-2021-meta-cs|Xing 2021]]), and HiDEF-seq measured ssDNA call burdens ~13-fold lower than Meta-CS ([[10-Summaries/liu-2024-hidef-seq|Liu 2024]]).
- **Rates differ by cell type.** Duplex-Multiome estimates 15.05 ± 3.15 sSNVs/year in excitatory neurons and 32.34 ± 2.39 in oligodendrocytes ([[10-Summaries/kriz-2025-duplex-multiome|Kriz 2025]]).
- **Copy-number changes follow cell type.** 3.1% of 65 PTA brain cells were aneuploid; neurons carry mostly private losses while oligodendrocytes carry clonal gains ([[10-Summaries/zhao-2025-hiscanner|Zhao 2025]]).
- **Disease links are cell-type-specific.** Alzheimer's disease shows cell-type-specific mosaicism ([[10-Summaries/kousi-2022-ad-mosaicism|Kousi 2022]]), and hypermutable aging brains may harbour glioma precursors ([[10-Summaries/taejeong-2022-science|Bae 2022]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/developmental-mutation-timing|Developmental mutation timing]] — When a post-zygotic mutation arises sets how much of the body carries it.
> - `concept` [[30-Concepts/pta|PTA]] — Primary template amplification, the scWGA chemistry behind the revised neuronal rates.
> - `concept` [[30-Concepts/mutational-signatures|Mutational signatures]] — Trinucleotide-context patterns that reflect specific mutagenic processes.
> - `note` [[50-Notes/single-cell-duplex-sequencing|Single-cell duplex sequencing]] — How strand-paired error correction reached single cells.
> - `note` [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|Mosaicism × epigenome]] — The gap between somatic mutation and single-cell epigenome, and how Duplex-Multiome addressed it.

## Somatic SNV and indel rates

Rate estimates by assay, from MDA single neurons to bulk duplex sequencing.

| Study | System | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/bae-2017-pregastrulation-mutations\|Bae 2018]] | Fetal brain progenitors | Mosaic SNVs at pregastrulation vs neurogenesis | Different mutation rates at the two stages; fetal brain progenitor SNVs ([[10-Summaries/bae-2017-pregastrulation-mutations\|Bae 2018]]) |
| [[10-Summaries/lodato-2017-aging-neurons\|Lodato 2018]] | 159 single neurons | MDA scWGS | ~23 sSNVs/year in PFC, ~40/year in DG; ~2.3–2.5-fold excess in Cockayne syndrome and xeroderma pigmentosum; replication-independent clocklike signature; coins "genosenium" ([[10-Summaries/lodato-2017-aging-neurons\|Lodato 2018]]) |
| [[10-Summaries/xing-2021-meta-cs\|Xing 2021]] | 32 PFC neurons, 3 donors (19/49/76 y) | META-CS | ~16 SNVs/year, lower than earlier estimates; ssDNA G>T damage calls rise in the oldest brain ([[10-Summaries/xing-2021-meta-cs\|Xing 2021]]) |
| [[10-Summaries/luquette-2022-neuron-scan2-indels\|Luquette 2022]] | 52 single neurons | PTA + SCAN2 | 16.5 sSNVs/year and a genome-wide indel rate of ~3/year (≥3); enrichment in neuronal enhancers and promoters; indels may matter more for gene function than SNVs ([[10-Summaries/luquette-2022-neuron-scan2-indels\|Luquette 2022]]) |
| [[10-Summaries/liu-2024-hidef-seq\|Liu 2024]] | Cortical neurons among 134 samples | HiDEF-seq | ssDNA call burdens ~13-fold lower than Meta-CS single-cell duplex sequencing, indicating amplification-based single-strand estimates are inflated ([[10-Summaries/liu-2024-hidef-seq\|Liu 2024]]) |
| [[10-Summaries/kriz-2025-duplex-multiome\|Kriz 2025]] | Brain nuclei by cell type | Duplex-Multiome | 15.05 ± 3.15 sSNVs/year in excitatory neurons, 32.34 ± 2.39 in oligodendrocytes; astrocytes faster than microglia, upper-layer faster than deep-layer neurons; low-VAF clonal sSNVs more frequent in glia than neurons (P = 0.036) ([[10-Summaries/kriz-2025-duplex-multiome\|Kriz 2025]]) |
| [[10-Summaries/zhang-2025-smaht-duplex-benchmark\|Zhang 2025]] | Brain homogenates | Bulk duplex sequencing, several methods | ~18.6 somatic SNVs per cell per year averaged across methods ([[10-Summaries/zhang-2025-smaht-duplex-benchmark\|Zhang 2025]]) |

## Copy number and aneuploidy

- **Human brain CNAs.** HiScanner on 65 PTA cells from 11 brains: 3.1% aneuploid, 614 mostly sub-3 Mb CNAs; neurons carry mostly private losses (5% clonal), oligodendrocytes carry clonal gains; cnLOH only in neurons; no clear age trend ([[10-Summaries/zhao-2025-hiscanner|Zhao 2025]]).
- **Mouse brain aneuploidy atlas.** Mukamel 2025 maps cell-type-specific aneuploidy in the mouse brain ([[10-Summaries/mukamel-2025-aneuploidy-brain|Mukamel 2025]]).

## Disease and clonal expansion

- **Glioma precursors.** Analysis of 131 human brains finds aging-associated hypermutability, read as possible glioma precursors ([[10-Summaries/taejeong-2022-science|Bae 2022]]).
- **Alzheimer's disease, by cell type.** Cell-type-specific somatic mutation burden in AD ([[10-Summaries/kousi-2022-ad-mosaicism|Kousi 2022]]).
- **Alzheimer's disease, single neurons.** Somatic genomic changes in single AD neurons ([[10-Summaries/miller-2022-nature|Miller 2022]]).

## Consortia and reviews

- **BSMN.** The Brain Somatic Mosaicism Network is an NIH program; [[10-Summaries/mcconnell-2017-science|McConnell 2017]] is its framing paper, and [[10-Summaries/garrison-2023-bsmn-data|Garrison 2023]] describes its data resource (ASD, schizophrenia, bipolar, FCD and Tourette cohorts).
- **SMaHT.** [[20-Entities/smaht-network]] — Somatic Mosaicism Across Human Tissues.
- **Review.** [[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto & Walsh 2022]] — *Nature Reviews Neuroscience* review of mosaicism in the human brain.

## Epigenomic annotation of brain cell types

- **Methylation taxonomy.** snmC-seq supplies the methylation-based neuronal cell-type taxonomy (16 mouse / 21 human clusters) ([[10-Summaries/luo-2017-snmc-seq|Luo 2017]]) that the 3D-genome brain studies use as their annotation ([[10-Summaries/yu-2021-snaphic|SnapHiC]]; [[10-Summaries/xiong-2024-scghost|scGHOST]]; [[10-Summaries/park-2026-mintsc|MINTsC]]).

## Open questions

- Neuronal SNV rates span ~16 to ~23 per year in PFC across MDA, META-CS, PTA and duplex assays, and bulk duplex gives ~18.6 per cell; how much of the spread is chemistry and how much is cell-type mix is unresolved ([[10-Summaries/lodato-2017-aging-neurons|Lodato 2018]]; [[10-Summaries/xing-2021-meta-cs|Xing 2021]]; [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]; [[10-Summaries/kriz-2025-duplex-multiome|Kriz 2025]]; [[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]). (synthesis)
- Single-strand damage calls depend on the assay: META-CS calls rise in the oldest brain, while HiDEF-seq measures burdens ~13-fold lower than Meta-CS ([[10-Summaries/xing-2021-meta-cs|Xing 2021]]; [[10-Summaries/liu-2024-hidef-seq|Liu 2024]]). (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one body.
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Technologies that interrogate the DNA of single cells, by scWGA or by strand-paired single-molecule reads.

## All sources on this page

> [!info]- 19 summaries cited here
> - [[10-Summaries/bae-2017-pregastrulation-mutations|Bae 2018]]
> - [[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto & Walsh 2022]]
> - [[10-Summaries/garrison-2023-bsmn-data|Garrison 2023]]
> - [[10-Summaries/kousi-2022-ad-mosaicism|Kousi 2022]]
> - [[10-Summaries/kriz-2025-duplex-multiome|Kriz 2025]]
> - [[10-Summaries/liu-2024-hidef-seq|Liu 2024]]
> - [[10-Summaries/lodato-2017-aging-neurons|Lodato 2018]]
> - [[10-Summaries/luo-2017-snmc-seq|Luo 2017]]
> - [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]
> - [[10-Summaries/mcconnell-2017-science|McConnell 2017]]
> - [[10-Summaries/miller-2022-nature|Miller 2022]]
> - [[10-Summaries/mukamel-2025-aneuploidy-brain|Mukamel 2025]]
> - [[10-Summaries/park-2026-mintsc|Park 2026]]
> - [[10-Summaries/taejeong-2022-science|Bae 2022]]
> - [[10-Summaries/xing-2021-meta-cs|Xing 2021]]
> - [[10-Summaries/xiong-2024-scghost|Xiong 2024]]
> - [[10-Summaries/yu-2021-snaphic|Yu 2021]]
> - [[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]
> - [[10-Summaries/zhao-2025-hiscanner|Zhao 2025]]
