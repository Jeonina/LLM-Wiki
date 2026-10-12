---
type: concept
title: DNMT (DNA methyltransferases)
aliases: [DNA methyltransferase, DNMT1, DNMT3A, DNMT3B]
tags: [epigenetics, methylation, enzymes]
created: 2026-05-11
updated: 2026-10-12
---

# DNMT (DNA methyltransferases)

> The enzyme family that catalyzes addition of methyl groups to the C5 of cytosine: in mammals **DNMT1** maintains methylation through S phase, and **DNMT3A** and **DNMT3B** establish new patterns de novo; loss of any is lethal ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]).

> [!abstract] 한눈에
> DNMT는 cytosine의 C5에 methyl기를 붙이는 효소군으로, DNMT1은 복제 때 hemimethylated DNA를 인식해 기존 패턴을 유지하고 DNMT3A/3B는 발생 과정에서 새 패턴을 만든다 ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]). DNMT3A 기능 상실 돌연변이는 clonal hematopoiesis와 AML의 반복적 driver다.

## Definition

DNA methyltransferases add a methyl group to the C5 of cytosine. Mammals have three catalytic members: **DNMT1** (maintenance — propagates methylation through S phase) and **DNMT3A** and **DNMT3B** (de novo — establish new methylation patterns during development) ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]).

## Why it matters

- Maintenance fidelity is essential — without DNMT1, methylation patterns are diluted at each cell division.
- Loss of any DNMT is lethal in mice — early gestational or postnatal, depending on the enzyme ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]).
- DNMT3A loss-of-function mutations are recurrent drivers of [[40-Topics/clonal-hematopoiesis]] and AML.
- DNMT inhibitors (5-azacytidine, decitabine) are approved for MDS and AML.

## Family members

| Enzyme | Role | Mechanism and notes | Source |
|---|---|---|---|
| DNMT1 | Maintenance | Constitutively expressed in dividing cells and recruited to replication forks by PCNA and UHRF1. UHRF1 binds hemimethylated DNA via its SRA domain, orienting DNMT1 to methylate the nascent strand opposite a previously methylated cytosine. DNMT1 is **structurally dependent on a hemimethylated substrate**: its low affinity and catalytic activity at unmethylated DNA limit its de novo activity, preventing spurious gain of methylation | ([[10-Summaries/smith-2013-methylation-development\|Smith & Meissner 2013]]) |
| DNMT3A | De novo | Required for establishing methylation patterns during embryogenesis and germ cell development; R882H is the most common DNMT3A mutation in AML | ([[10-Summaries/smith-2013-methylation-development\|Smith & Meissner 2013]]) |
| DNMT3B | De novo | Required for establishing methylation patterns during embryogenesis and germ cell development | ([[10-Summaries/smith-2013-methylation-development\|Smith & Meissner 2013]]) |
| DNMT3L | Regulatory paralog | No catalytic activity | — |

The opposing demethylation pathway runs through the [[tet-enzymes|TET enzymes]].

## Evidence and examples

- DNMT3A R882H is a clonal-hematopoiesis-driving mutation.
- Decitabine treatment of MDS is pharmacologic DNMT inhibition.

## Contested points

- DNMT3A vs DNMT3B specificity in different developmental contexts.

## Related

> [!cards]
> - `concept` [[30-Concepts/cpg-island|CpG island]] — Short CpG-dense regions at the promoters of most housekeeping and developmental genes.
> - `concept` [[30-Concepts/tet-enzymes|TET enzymes]] — Dioxygenases that oxidize 5mC; the opposing demethylation pathway.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5-methylcytosine, predominantly at CpG, and how it is measured.
> - `hub` [[40-Topics/clonal-hematopoiesis|Clonal hematopoiesis]] — Age-related expansion of a blood stem-cell clone carrying a driver mutation.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]
