---
type: concept
title: CALR mutation
aliases: [CALR, calreticulin mutation]
tags: [hematology, MPN, driver-mutation]
created: 2026-05-07
updated: 2026-10-12
---

# CALR mutation

> Recurrent somatic mutation in calreticulin (CALR), one of the three canonical drivers of [[myeloproliferative-neoplasm]] (along with [[jak2-v617f]] and MPL); activates MPL signaling and induces a cell-identity-dependent transcriptional response in hematopoietic progenitors ([[10-Summaries/nam-2019-got|GoT]]).

> [!abstract] 한눈에
> CALR 돌연변이는 MPN의 세 가지 대표 driver 중 하나로, 변이 단백질이 MPL에 결합해 thrombopoietin 없이도 신호를 켠다. GoT로 같은 환자 안의 변이 세포와 정상 세포를 비교하면, 같은 변이가 HSPC에서는 NF-κB 경로를, MkP에서는 UPR을 켜는 식으로 세포 정체성에 따라 다르게 작동한다 ([[10-Summaries/nam-2019-got|GoT]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [혈액암 교재](../60-Explainers/hematopoietic-malignancies.html)
<!-- /explainer-links -->

## Definition

CALR is normally an ER-resident chaperone and Ca²⁺-binding protein. The pathogenic mutations are frameshifts in exon 9 (most commonly type 1, a 52-bp deletion; type 2, a 5-bp insertion) that generate a novel positively-charged C-terminus. The mutant protein traffics to the cell surface and binds the thrombopoietin receptor MPL, activating it constitutively in a thrombopoietin-independent manner ([[10-Summaries/nam-2019-got|GoT]]).

## Why it matters

CALR mutations account for ~25–30% of MPN cases (essential thrombocythemia and primary myelofibrosis). Before [[got]], the transcriptional consequences of CALR mutation in primary HSPCs were inferred indirectly because mutant and wild-type cells in the same patient cannot be sorted by surface markers ([[10-Summaries/nam-2019-got|GoT]]).

This is the canonical example used throughout the wiki of "same mutation, different cell, different transcriptional output" ([[10-Summaries/nam-2019-got|GoT]]).

## Mutation types

| Type | Lesion | Disease association | Source |
|---|---|---|---|
| Type 1 | 52-bp deletion in exon 9 | More strongly associated with myelofibrosis progression | — |
| Type 2 | 5-bp insertion in exon 9 | More associated with essential thrombocythemia | — |

CALR is distinct from [[jak2-v617f]] in its mechanism (direct MPL binding vs constitutive kinase activation) and its consequence (UPR activation due to misfolded chaperone vs cytokine-independent JAK-STAT).

## Cell-identity-dependent output

GoT shows the mutation's transcriptional output is **cell-identity-dependent** ([[10-Summaries/nam-2019-got|GoT]]):

| Cell state | Dominant response | Proposed consequence | Source |
|---|---|---|---|
| Uncommitted HSPCs | NF-κB pathway upregulation (CXCL2, NFKBIA) plus anti-apoptotic genes | HSC self-renewal/outgrowth | ([[10-Summaries/nam-2019-got\|GoT]]) |
| Megakaryocytic progenitors (MkPs) | Unfolded protein response — IRE1-XBP1 splicing, ATF6-mediated chaperone induction (HSPA5/BiP); see [[unfolded-protein-response]] | Increased proliferation, correlated with patient platelet counts | ([[10-Summaries/nam-2019-got\|GoT]]) |
| MkPs in MF (advanced disease) | TGFB1 upregulation | Marrow fibrosis | ([[10-Summaries/nam-2019-got\|GoT]]) |

## Evidence and examples

- Five ET patients (ET01–ET05) profiled with [[got]]: mutant cell frequency higher in MkPs than HSPCs; UPR signature in MkPs ([[10-Summaries/nam-2019-got|GoT]]).
- Four MF patients: mutant cells already enriched in HSPCs; IRE1 activation persists; TGFB1 upregulated in MkPs ([[10-Summaries/nam-2019-got|GoT]]).

## Contested points

- IRE1-XBP1 is proposed as a therapeutic target ([[10-Summaries/nam-2019-got|GoT]]), but in vivo validation in patients has not appeared in the wiki yet.
- The shift from "no HSPC fitness advantage in ET" to "strong HSPC fitness advantage in MF" is observed ([[10-Summaries/nam-2019-got|GoT]]) but not mechanistically explained.

## Related

> [!cards]
> - `concept` [[30-Concepts/jak2-v617f|JAK2 V617F]] — Sister driver mutation with a different mechanism; both converge on JAK-STAT activation downstream.
> - `concept` [[30-Concepts/myeloproliferative-neoplasm|Myeloproliferative neoplasm]] — ET, PV and MF, the diseases CALR drives.
> - `concept` [[30-Concepts/unfolded-protein-response|Unfolded protein response]] — The ER stress response that CALR-mutant MkPs activate.
> - `concept` [[30-Concepts/hematopoietic-differentiation|Hematopoietic differentiation]] — The progenitor hierarchy onto which mutant fitness is mapped.
> - `concept` [[30-Concepts/got|GoT]] — Genotype and transcriptome from the same single cells.
> - `hub` [[40-Topics/hematopoietic-malignancies|Hematopoietic malignancies]] — Cancers and pre-cancerous clonal expansions of blood stem and progenitor cells.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/nam-2019-got|Nam 2019]]
