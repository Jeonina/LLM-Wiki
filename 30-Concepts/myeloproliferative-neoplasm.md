---
type: concept
title: Myeloproliferative neoplasm (MPN)
aliases: [MPN, myeloproliferative neoplasms]
tags: [hematology, malignancy, clonal-hematopoiesis]
created: 2026-05-07
updated: 2026-10-12
---

# Myeloproliferative neoplasm (MPN)

> Group of clonal hematological diseases — essential thrombocythemia (ET), polycythemia vera (PV), and primary myelofibrosis (MF) — driven by somatic mutations in JAK2, CALR, or MPL that cause overproduction of mature myeloid lineages and progressive marrow dysfunction.

> [!abstract] 한눈에
> MPN은 JAK2·CALR·MPL 체세포 변이로 생기는 클론성 골수 질환(ET, PV, MF)이고, 같은 환자 안에 변이 세포와 정상 세포가 섞여 있어 single-cell genotyping으로 한 변이의 효과를 내부 대조군과 비교하기 좋은 모델이다 ([[10-Summaries/nam-2019-got|Nam 2019]]). 같은 변이라도 progenitor 유형에 따라 전사 결과가 다르고, 질환이 드러나기 전부터 chromatin priming이 나타난다 ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [클론성 조혈 교재](../60-Explainers/clonal-hematopoiesis.html)
>
> [혈액암 교재](../60-Explainers/hematopoietic-malignancies.html)
<!-- /explainer-links -->

## Definition

MPNs originate in [[hematopoietic-differentiation|hematopoietic stem cells]] and are diagnosed by lineage-specific cytoses (platelets in ET, red cells in PV, fibrosis with cytopenia in MF) plus a driver mutation. The three canonical drivers ([[jak2-v617f]], [[calr-mutation]], MPL W515) are largely mutually exclusive and converge on JAK-STAT activation.

A subset of patients evolve PV → MF or ET → MF; a smaller fraction transform to acute myeloid leukemia.

## Why it matters

MPN is a tractable model for studying **how a single somatic mutation perturbs human hematopoiesis** because:

- The mutations are stable, well-characterized, and present in a substantial mutated-cell fraction;
- Bone marrow CD34⁺ samples are clinically obtainable;
- Mutated and wild-type cells coexist in the same patient — the **internal-control design** that makes [[got]] and [[got-cha]] uniquely powerful here ([[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Disease subtypes and states

| Subtype / state | Hallmark | Single-cell finding | Source |
|---|---|---|---|
| Essential thrombocythemia (ET) | Elevated platelets | CALR-mutant fitness advantage grows with myeloid differentiation | ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| Polycythemia vera (PV) | Elevated red cells; mostly JAK2V617F | — | — |
| Primary myelofibrosis (MF) | Bone-marrow fibrosis, cytopenias | Mutant cells already enriched in HSPCs; MkPs upregulate TGFB1 | ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| JAK2V617F clonal hematopoiesis | Pre-disease state | Chromatin priming already detectable | ([[10-Summaries/izzo-2024-got-cha\|Izzo 2024]]) |
| Triple mutants | Co-occurring CALR + NFE2 + SF3B1 | Dissectable via multiplexed [[got]] | ([[10-Summaries/nam-2019-got\|Nam 2019]]) |

## Evidence and examples

**Mutation effects resolved in single cells**

- The same mutation produces **different transcriptional outputs in different progenitor cell types** ([[10-Summaries/nam-2019-got|Nam 2019]]).
- The same mutation produces **cell-intrinsic chromatin priming** that is visible *before* overt disease ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- SComatic applied to scRNA-seq of CD34+ cells from five MPN patients detected ~0.12 mutations/Mb per haploid genome, 96% attributed to SBS5/SBS40, with burden correlating with age (r = 0.79, P = 0.09) ([[10-Summaries/muyas-2024-scomatic|SComatic]]).

**Cohorts**

- ET01–ET05 (5 patients), MF01–MF04, MF05 multi-mutant ([[10-Summaries/nam-2019-got|Nam 2019]]).
- 21 samples from 18 JAK2V617F MF patients (12 untreated, including three longitudinal PV→MF samples from one patient; 6 ruxolitinib-treated) plus 1 JAK2V617F clonal hematopoiesis sample ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Contested points

- Why CALR fitness advantage is differentiation-dependent in ET but already strong at the HSPC level in MF is observed but unexplained ([[10-Summaries/nam-2019-got|Nam 2019]]).
- Whether ruxolitinib's failure to eliminate the JAK2V617F clone — despite reversing the chromatin TF-motif phenotype — argues for combination therapy targeting the cell-intrinsic chromatin program directly ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/calr-mutation|CALR mutation]] — Driver mutation whose effect depends on progenitor identity.
> - `concept` [[30-Concepts/jak2-v617f|JAK2 V617F]] — The most common MPN driver.
> - `concept` [[30-Concepts/hematopoietic-differentiation|Hematopoietic differentiation hierarchy]] — The stem-to-progenitor hierarchy that MPN mutations perturb.
> - `concept` [[30-Concepts/unfolded-protein-response|Unfolded protein response (UPR)]] — Stress pathway activated in CALR-mutant progenitors.
> - `concept` [[30-Concepts/got|GoT]] — Genotyping of transcriptomes in single cells.
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Genotyping with single-cell chromatin accessibility.
> - `hub` [[40-Topics/hematopoietic-malignancies|Hematopoietic malignancies]] — Blood cancers and their single-cell genetics.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/muyas-2024-scomatic|Muyas 2024]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
