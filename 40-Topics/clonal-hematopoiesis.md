---
type: topic
title: Clonal hematopoiesis
aliases: [CH, CHIP, clonal hematopoiesis of indeterminate potential, MPN]
tags: [clonal-hematopoiesis, MPN, JAK2, DNMT3A, TET2, CALR, hematology, mosaicism, mutation, aging]
created: 2026-05-19
updated: 2026-10-12
paper_section: ["5.3"]
---

# Clonal hematopoiesis

> Age-related mosaic expansion of a hematopoietic stem cell (HSC) clone carrying a recurrent somatic driver mutation (DNMT3A, TET2, JAK2 V617F, CALR, ASXL1), detectable in peripheral blood by sequencing; it confers elevated risk of cardiovascular disease and hematologic malignancy and is a precursor state to overt MPN / MDS / AML. It is the single-cell genomics field's most tractable mosaicism disease model ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]; [[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]).

> [!abstract] 한눈에
> 클론성 조혈은 나이가 들면서 DNMT3A, TET2, JAK2 V617F 같은 driver 변이를 가진 HSC 클론이 혈액 안에서 늘어나는 상태이며, 혈액암과 심혈관 질환 위험을 높인다 ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]). GoT 계열 single-cell 방법은 같은 세포에서 genotype과 transcriptome 또는 chromatin accessibility를 함께 읽어, 변이 세포가 질병이 드러나기 전부터 어떻게 달라지는지 보여 준다 ([[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Key points

- **CHIP is defined by a VAF threshold.** It is a leukemia-driver mutation at ≥2% VAF without overt hematologic disease ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]).
- **DNMT3A and TET2 are the two most frequent drivers.** Both are loss-of-function mutations in DNA-methylation enzymes ([[10-Summaries/kapadia-2024-stem-cell-aging|Kapadia 2024]]).
- **CH raises both cancer and cardiovascular risk.** It raises the risk of progression to MDS / AML and is an independent risk factor for atherosclerosis ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]), recently extended to HFpEF and stroke ([[10-Summaries/hilal-2026-cardiac-somatic-review|Hilal 2026]]).
- **Single-cell genotyping shows priming before disease.** GoT-ChA found cell-intrinsic chromatin priming in a JAK2V617F CH sample before overt MPN ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- **Many putative CH drivers are noncoding.** A UK Biobank scan found 35 novel putative drivers, 32 of them noncoding ([[10-Summaries/weinstock-2025-ch-noncoding-drivers|Weinstock 2025]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/got|GoT]] — Links somatic genotype to the single-cell transcriptome in 10x droplets.
> - `concept` [[30-Concepts/got-cha|GoT-ChA]] — Captures genotype and chromatin accessibility from the same nucleus.
> - `concept` [[30-Concepts/jak2-v617f|JAK2 V617F]] — The most common MPN driver and a precursor lesion in CH.
> - `concept` [[30-Concepts/myeloproliferative-neoplasm|Myeloproliferative neoplasm]] — ET, PV and MF, driven by JAK2, CALR or MPL mutations.
> - `concept` [[30-Concepts/hematopoietic-differentiation|Hematopoietic differentiation]] — The HSC-to-mature-cell hierarchy that driver mutations reshape.

## Definition and clinical categories

A subset of mature blood cells shares a somatic mutation traceable to a common HSC ancestor, typically detected at ≥2% variant allele frequency (VAF) for canonical drivers ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]). CH is common with age ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]; [[10-Summaries/kapadia-2024-stem-cell-aging|Kapadia 2024]]).

| Category | Definition | Source |
|---|---|---|
| CHIP (clonal hematopoiesis of indeterminate potential) | Clinical term: ≥2% VAF of a leukemia-driver mutation without overt hematologic disease | ([[10-Summaries/forsberg-2017-mosaicism-review\|Forsberg 2017]]) |
| CCUS (clonal cytopenia of undetermined significance) | CHIP plus cytopenias | ([[10-Summaries/forsberg-2017-mosaicism-review\|Forsberg 2017]]) |
| Pre-leukemic clonal expansion | Precedes overt AML/MDS by years | ([[10-Summaries/forsberg-2017-mosaicism-review\|Forsberg 2017]]) |

## Drivers

| Driver | Mechanism | Note |
|---|---|---|
| DNMT3A | Methyltransferase loss-of-function | The most frequent CHIP driver ([[10-Summaries/kapadia-2024-stem-cell-aging\|Kapadia 2024]]); R882 hypomethylation profiled in CH ([[10-Summaries/nam-2022-natgenet\|Nam 2022]]); R882H clones expand in elderly individuals over decades ([[10-Summaries/forsberg-2017-mosaicism-review\|Forsberg 2017]]; [[10-Summaries/nam-2022-natgenet\|Nam 2022]]) |
| TET2 | Demethylation-enzyme loss-of-function | The second of the two most frequent drivers ([[10-Summaries/kapadia-2024-stem-cell-aging\|Kapadia 2024]]) |
| ASXL1, JAK2 V617F, SF3B1, TP53, CALR and others | — | Other common drivers ([[10-Summaries/forsberg-2017-mosaicism-review\|Forsberg 2017]]; [[10-Summaries/nam-2019-got\|Nam 2019]]) |
| Noncoding drivers (e.g. TERT promoter) | — | An age-association scan of ~490K UK Biobank blood genomes found 35 novel putative CH drivers, 32 of them noncoding, including a TERT promoter mutation with fitness similar to splicing-factor CH; non-canonical mutations carried on average 47% of CH's liability-scale disease variance ([[10-Summaries/weinstock-2025-ch-noncoding-drivers\|Weinstock 2025]]) |

Related enzyme concepts: [[30-Concepts/dnmt]] · [[30-Concepts/tet-enzymes]]; MPN driver concepts: [[30-Concepts/jak2-v617f]] · [[30-Concepts/calr-mutation]].

## Why it matters

- **Cancer risk.** Elevated risk of progression to MDS / AML ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]).
- **Cardiovascular risk.** An independent risk factor for atherosclerosis, mechanistically via an inflammatory monocyte/macrophage phenotype ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]); recently extended to HFpEF and stroke ([[10-Summaries/hilal-2026-cardiac-somatic-review|Hilal 2026]]).
- **Precursor state for MPN.** Drivers include JAK2 V617F; GoT-ChA profiled a JAK2V617F CH sample and showed cell-intrinsic chromatin priming *before* overt MPN ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Methods that resolve genotype and phenotype in CH

| Method | Readout paired with genotype | Application | Source |
|---|---|---|---|
| [[30-Concepts/got\|GoT]] (Genotyping of Transcriptomes) | Transcriptome | CALR-mutated MPN | ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| [[30-Concepts/got-cha\|GoT-ChA]] | Chromatin accessibility | JAK2V617F MPN; pre-disease chromatin priming in JAK2V617F CH | ([[10-Summaries/izzo-2024-got-cha\|Izzo 2024]]) |
| GoT-Splice | Gene expression, long-read isoforms and surface protein | Splicing-factor-mutant CH | ([[10-Summaries/cortes-lopez-2023-cellstemcell\|Cortés-López 2023]]) |

## Clonal structure of normal hematopoiesis

- **HSC clonal dynamics.** Somatic mutations in WGS of single-HSPC-derived colonies from one 59-year-old donor were used to infer HSC population dynamics, with a stable pool of 50,000–200,000 actively contributing stem cells by adolescence ([[10-Summaries/lee-six-2018-hsc-dynamics|Lee-Six 2018]]).
- **mtDNA clone tracing.** mtDNA tracing of 7,474 bone-marrow HSPCs and 8,591 blood cells from one healthy 47-year-old donor resolved 257 clones, 92% holding <1% of cells, with no detectable lineage bias ([[10-Summaries/ludwig-2020-mtscatac-seq|Lareau 2021]]).

## Open questions

- The right threshold (VAF, gene set) for clinical action ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]).
- Whether CHIP-associated cardiovascular risk is causal or mediated by shared risk factors ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]); causality is still being established, with recent extension to HFpEF and stroke ([[10-Summaries/hilal-2026-cardiac-somatic-review|Hilal 2026]]).
- IRE1-XBP1 as a therapeutic target in CALR-mutant CH — clinical validation pending ([[10-Summaries/nam-2019-got|Nam 2019]]).
- Whether JAK2V617F chromatin priming is causal for clonal expansion or downstream of it ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- If most putative CH drivers are noncoding ([[10-Summaries/weinstock-2025-ch-noncoding-drivers|Weinstock 2025]]), CHIP definitions built on a canonical coding gene set may miss clones. (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/hematopoietic-malignancies|Hematopoietic malignancies]] — Cancers and pre-cancerous clonal expansions of blood stem and progenitor cells.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one body.

## All sources on this page

> [!info]- 10 summaries cited here
> - [[10-Summaries/cortes-lopez-2023-cellstemcell|Cortés-López 2023]]
> - [[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]
> - [[10-Summaries/hilal-2026-cardiac-somatic-review|Hilal 2026]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/kapadia-2024-stem-cell-aging|Kapadia & Goodell 2024]]
> - [[10-Summaries/lee-six-2018-hsc-dynamics|Lee-Six 2018]]
> - [[10-Summaries/ludwig-2020-mtscatac-seq|Lareau & Ludwig 2021]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
> - [[10-Summaries/nam-2022-natgenet|Nam 2022]]
> - [[10-Summaries/weinstock-2025-ch-noncoding-drivers|Weinstock 2025]]
