---
type: concept
title: Hematopoietic differentiation hierarchy
aliases: [hematopoiesis, HSPC hierarchy, hematopoietic differentiation]
tags: [hematology, stem-cells, differentiation]
created: 2026-05-07
updated: 2026-05-07
---

# Hematopoietic differentiation hierarchy

> The branching topology by which hematopoietic stem cells (HSCs) generate all blood lineages: HSCs → multipotent progenitors → lineage-committed progenitors → mature cells. The native scaffold against which somatic mutations like [[calr-mutation]] and [[jak2-v617f]] reshape clonal differentiation.

## Definition

In CD34⁺ progenitor analyses (the cohort type used in both [[10-Summaries/nam-2019-got]] and [[10-Summaries/izzo-2024-got-cha]]), the canonical clusters are:

- **HSPC** — hematopoietic stem and progenitor cells; further subdivided into HSC, HSC_LY (lymphoid-biased), HSC_MY (myeloid-biased).
- **LMPP** — lymphoid-myeloid pluripotent progenitors.
- **CMP / GMP** — common myeloid / granulocyte–monocyte progenitors.
- **MEP** — megakaryocytic–erythroid progenitors.
- **EP** — erythroid progenitors (often resolved into EP1/EP2/EP3 by pseudotime).
- **MkP** — megakaryocytic progenitors.
- **NP** — neutrophil progenitors.
- **CLP** — common lymphoid progenitors.
- **PreB / B / T / NK** — lymphoid commitments.

These are recovered de novo from scRNA-seq and scATAC-seq clustering and serve as the analytic backbone for mapping mutant-cell distributions.

## Why it matters

Both [[10-Summaries/nam-2019-got]] and [[10-Summaries/izzo-2024-got-cha]] make their key claims by **projecting genotypes onto the differentiation map** and asking where the mutated cells accumulate or shift:

- CALR-mutant cells in ET enrich progressively along myeloid differentiation, peaking in MkPs ([[10-Summaries/nam-2019-got]]).
- JAK2V617F-mutant cells distribute toward erythroid–megakaryocytic and granulocyte–monocyte progenitors and away from CLPs/lymphoid clusters; ruxolitinib re-evens this distribution without removing the clone ([[10-Summaries/izzo-2024-got-cha]]).

The hierarchy itself — recovered from healthy CD34⁺ cells — defines the "native differentiation tree" that mutated clones perturb.

## Variants and refinements

- **MkP heterogeneity** ([[10-Summaries/nam-2019-got]]): HSC^low MkP^high vs HSC^high MkP^low subsets within the MkP cluster differ in mutant cell frequency and proliferation.
- **Pseudotime ordering** captures progressive commitment within branches (e.g. erythroid pseudotime quantiles in [[10-Summaries/izzo-2024-got-cha]]).

## Contested points

- The "hierarchy" framing is itself a simplification — single-cell data show continuous lineage priming rather than discrete commitments. The hierarchy is preserved here as the analytic vocabulary the cited papers use.

## Examples

- 18,722 CD34⁺ cells from 5 ET patients, t-SNE clustered into HSPC / IMP / MEP / MkP / NP / EP / E-B-M / M-D / PreB ([[10-Summaries/nam-2019-got]]).
- 150,643 cells from 21 MPN samples, integrated UMAP with HSC / HSCMY / HSCLY / LMPP / CMP / GMP / MEP / EP1-3 / MkP / CLP / B / T / NK ([[10-Summaries/izzo-2024-got-cha]]).

## Related

- [[calr-mutation]]
- [[jak2-v617f]]
- [[myeloproliferative-neoplasm]]
- [[got]]
- [[got-cha]]
- [[40-Topics/hematopoietic-malignancies]]
