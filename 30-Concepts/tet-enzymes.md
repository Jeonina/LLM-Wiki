---
type: concept
title: TET enzymes
aliases: [TET, TET1, TET2, TET3, ten-eleven translocation]
tags: [epigenetics, methylation, enzymes, demethylation]
created: 2026-05-11
updated: 2026-10-12
---

# TET enzymes

> Ten-eleven translocation (TET) dioxygenases — **TET1**, **TET2**, **TET3** — that oxidize 5-methylcytosine (5mC) to 5-hydroxymethylcytosine (5hmC), the first step in active demethylation ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]). TET2 loss-of-function is among the most common drivers of [[40-Topics/clonal-hematopoiesis]] and myeloid neoplasia.

> [!abstract] 한눈에
> TET 효소는 5mC를 5hmC, 5fC, 5caC로 차례로 산화하고, TDG와 base excision repair가 이를 이어받아 능동적 탈메틸화를 완성한다 ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]). bisulfite sequencing은 이렇게 만들어진 5hmC를 메틸화된 C로 읽기 때문에 두 수식이 섞여 보인다 ([[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]).

## Definition

TET enzymes use molecular oxygen and α-ketoglutarate to iteratively oxidize 5mC → 5hmC → 5-formylcytosine → 5-carboxylcytosine. Thymine DNA glycosylase (TDG) recognizes the oxidized intermediates and triggers base excision repair, completing **active demethylation** ([[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]).

## Why it matters

- Active demethylation mechanism — distinct from passive (replication-without-DNMT1) demethylation; see [[dnmt]] for the opposing methylation enzymes.
- TET2 loss is a major clonal hematopoiesis driver, predisposing to MPN, MDS, AML and to cardiovascular disease.
- IDH1/IDH2 mutations produce 2-hydroxyglutarate, which inhibits TET enzymes — a major mechanism in glioma and AML.

## Family members

| Member | Role | Source |
|---|---|---|
| TET1 | Preferentially binds [[cpg-island\|CpG island]] promoters in embryonic stem cells; the binding pattern is independent of methylation status (binds unmethylated CpG islands). TET dioxygenases, with deaminases and BER enzymes, may act as proofreading enzymes coupled to promoter/enhancer complexes that prevent aberrant hypermethylation | ([[10-Summaries/smith-2013-methylation-development\|Smith & Meissner 2013]]) |
| TET2 | Mutated in ~15% of AML and ~20% of CMML; the second most common driver of clonal hematopoiesis after DNMT3A | — |
| TET3 | Dynamically active during zygotic reprogramming | — |

## Evidence and examples

- TET2 mutation in CHIP (clonal hematopoiesis of indeterminate potential) → elevated risk of MPN/MDS/AML and atherosclerosis.
- IDH1 R132H glioma → 2-HG accumulation → TET inhibition → CIMP (CpG island methylator phenotype).
- Following the discovery that TET enzymes generate 5hmC, the same lab showed that bisulfite sequencing reads TET-generated 5hmC as methylated C and that its bisulfite adduct impairs PCR ([[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]).

## Contested points

- Whether 5hmC is purely an intermediate or functional in its own right; 5hmC may be a functional mark, especially in brain — distinct from 5mC.

## Related

> [!cards]
> - `concept` [[30-Concepts/dnmt|DNMT]] — Opposing methylation enzymes that write 5mC.
> - `concept` [[30-Concepts/cpg-island|CpG island]] — CpG-dense promoter regions that TET1 preferentially binds.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC biology and the methods that measure it.
> - `hub` [[40-Topics/clonal-hematopoiesis|Clonal hematopoiesis]] — Age-related clonal expansion driven by DNMT3A, TET2 and other mutations.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/huang-2010-5hmc-bisulfite|Huang 2010]]
> - [[10-Summaries/smith-2013-methylation-development|Smith & Meissner 2013]]
