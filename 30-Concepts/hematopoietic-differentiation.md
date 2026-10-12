---
type: concept
title: Hematopoietic differentiation hierarchy
aliases: [hematopoiesis, HSPC hierarchy, hematopoietic differentiation]
tags: [hematology, stem-cells, differentiation]
created: 2026-05-07
updated: 2026-10-12
---

# Hematopoietic differentiation hierarchy

> The branching topology by which hematopoietic stem cells (HSCs) generate all blood lineages: HSCs → multipotent progenitors → lineage-committed progenitors → mature cells. The native scaffold against which somatic mutations like [[calr-mutation]] and [[jak2-v617f]] reshape clonal differentiation ([[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

> [!abstract] 한눈에
> 조혈 분화 계층은 HSC에서 다능성 전구세포와 계통 특이 전구세포를 거쳐 성숙 혈액세포로 갈라지는 구조이고, GoT와 GoT–ChA는 genotype을 이 분화 지도 위에 투영해 mutant 세포가 어디에 쌓이는지 보여 준다 ([[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]). Lineage barcode 연구는 이 계층을 뚜렷한 단계보다 연속적인 priming으로 본다 ([[10-Summaries/weinreb-2020-larry|LARRY]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [클론성 조혈 교재](../60-Explainers/clonal-hematopoiesis.html)
>
> [혈액암 교재](../60-Explainers/hematopoietic-malignancies.html)
<!-- /explainer-links -->

## Definition

In CD34⁺ progenitor analyses (the cohort type used in both [[10-Summaries/nam-2019-got|Nam 2019]] and [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]), the canonical clusters are:

| Cluster | Meaning |
|---|---|
| HSPC | Hematopoietic stem and progenitor cells; further subdivided into HSC, HSC_LY (lymphoid-biased), HSC_MY (myeloid-biased) |
| LMPP | Lymphoid-myeloid pluripotent progenitors |
| CMP / GMP | Common myeloid / granulocyte–monocyte progenitors |
| MEP | Megakaryocytic–erythroid progenitors |
| EP | Erythroid progenitors (often resolved into EP1/EP2/EP3 by pseudotime) |
| MkP | Megakaryocytic progenitors |
| NP | Neutrophil progenitors |
| CLP | Common lymphoid progenitors |
| PreB / B / T / NK | Lymphoid commitments |

These are recovered de novo from scRNA-seq and scATAC-seq clustering and serve as the analytic backbone for mapping mutant-cell distributions ([[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Why it matters

Both [[10-Summaries/nam-2019-got|Nam 2019]] and [[10-Summaries/izzo-2024-got-cha|Izzo 2024]] make their key claims by **projecting genotypes onto the differentiation map** and asking where the mutated cells accumulate or shift. The hierarchy itself — recovered from healthy CD34⁺ cells — defines the "native differentiation tree" that mutated clones perturb.

## Refinements of the hierarchy

- **MkP heterogeneity**: HSC^low MkP^high vs HSC^high MkP^low subsets within the MkP cluster differ in mutant cell frequency and proliferation ([[10-Summaries/nam-2019-got|Nam 2019]]).
- **Pseudotime ordering** captures progressive commitment within branches (e.g. erythroid pseudotime quantiles) ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- **A structured continuum**: expressed-barcode state–fate maps showed haematopoietic priming as a structured continuum with two monocyte routes (GMP-like and MDP-like) ([[10-Summaries/weinreb-2020-larry|LARRY]]).
- **Regulatory topics**: GFETM topics on Buenrostro 2018 haematopoiesis link IRF1/IRF2 motifs to MEP-enriched topics, CTCF to topics enriched in CLP, MEP and monocytes, and ETV2/5/6 to a monocyte topic ([[10-Summaries/fan-2026-gfetm|GFETM]]).

## Evidence and examples

**Mutant clones on the map**

- CALR-mutant cells in ET enrich progressively along myeloid differentiation, peaking in MkPs ([[10-Summaries/nam-2019-got|Nam 2019]]).
- JAK2V617F-mutant cells distribute toward erythroid–megakaryocytic and granulocyte–monocyte progenitors and away from CLPs/lymphoid clusters ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- Ruxolitinib abolishes the cell-intrinsic TF-motif differences between mutant and wild-type HSCs without removing the clone ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- 38,290 CD34⁺ cells from 5 ET patients, t-SNE clustered into HSPC / IMP / MEP / MkP / NP / EP / E-B-M / M-D / PreB ([[10-Summaries/nam-2019-got|Nam 2019]]).
- 150,643 cells from 21 MPN samples, integrated UMAP with HSC / HSCMY / HSCLY / LMPP / CMP / GMP / MEP / EP1-3 / MkP / CLP / B / T / NK ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

**Native clonal behaviour**

- Native-context clonal barcoding (DARLIN) found low-level HSC migration between bones: ~5% of HSC clones shared across bones 4 months after adult labelling (~12% after 1 year), higher for MPPs (~14%) and myeloid progenitors (~40%) ([[10-Summaries/li-2023-darlin|DARLIN]]).
- Haematopoiesis was predominantly local even when labelled at E17.0 ([[10-Summaries/li-2023-darlin|DARLIN]]).
- Megakaryocyte-biased HSCs were already present when labelled at E17.0 ([[10-Summaries/li-2023-darlin|DARLIN]]).

## Contested points

- The "hierarchy" framing is itself a simplification — single-cell data show continuous lineage priming rather than discrete commitments. The hierarchy is preserved here as the analytic vocabulary the cited papers use. The LARRY state–fate maps, which show a structured continuum ([[10-Summaries/weinreb-2020-larry|LARRY]]), fit the continuum reading (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/calr-mutation|CALR mutation]] — MPN driver whose mutant cells peak in MkPs.
> - `concept` [[30-Concepts/jak2-v617f|JAK2 V617F]] — MPN driver that skews progenitors away from lymphoid clusters.
> - `concept` [[30-Concepts/myeloproliferative-neoplasm|Myeloproliferative neoplasm]] — The blood cancers in which these hierarchies were mapped.
> - `concept` [[30-Concepts/got|GoT]] — Genotype-to-transcriptome method that projects genotypes onto the hierarchy.
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Genotype-to-chromatin successor of GoT.
> - `hub` [[40-Topics/hematopoietic-malignancies|Hematopoietic malignancies]] — Blood cancers studied with single-cell genotyping.

## All sources on this page

> [!info]- 5 summaries cited here
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/li-2023-darlin|Li 2023]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
> - [[10-Summaries/weinreb-2020-larry|Weinreb 2020]]
