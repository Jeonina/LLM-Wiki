---
type: summary
title: "Kousi et al. 2022 — Cell-type-specific somatic mutation burden in Alzheimer's disease"
source: "[[00-Sources/papers/Single-cell mosaicism analysis reveals cell-type-specific somatic mutational burden in Alzheimer's Dementia]]"
source_kind: paper
author: "Maria Kousi, Carles Boix, Yongjin P. Park, Hansruedi Mathys, Samuel Sledzieski, Zhuyu Peng, David A. Bennett, Li-Huei Tsai, Manolis Kellis (corresponding)"
published: 2022-04-22
ingested: 2026-05-12
doi: "10.1101/2022.04.21.489103"
journal: "bioRxiv (preprint)"
tags: [Alzheimer-disease, somatic-mosaicism, single-cell, brain, neurodegeneration, ROSMAP, Kellis-lab]
entities:
  - "[[20-Entities/manolis-kellis]]"
  - "[[20-Entities/li-huei-tsai]]"
  - "[[20-Entities/david-bennett]]"
  - "[[20-Entities/maria-kousi]]"
concepts:
  - "[[30-Concepts/somatic-mosaicism]]"
  - "[[30-Concepts/alzheimers-disease]]"
  - "[[30-Concepts/post-zygotic-variation]]"
  - "[[30-Concepts/clonal-hematopoiesis]]"
topics:
  - "[[40-Topics/somatic-mosaicism]]"
  - "[[40-Topics/scdna-seq]]"
---

# Kousi et al. 2022 — Cell-type-specific somatic mutation burden in Alzheimer's disease

> Thesis: Alzheimer's-affected human brains carry **a cell-type-specific increase in somatic mutational burden** detectable by single-cell mosaicism analysis on cells profiled within the ROSMAP cohort. Inherited APP/PSEN1/PSEN2 mutations explain only a small fraction of AD risk; this work asks whether post-zygotic somatic mutations contribute to the much larger sporadic and late-onset burden — and finds that they do, in a cell-type-resolved way.

## Key claims

- Single-cell mosaicism analysis across brain cell types from ROSMAP AD vs control donors detects **cell-type-specific differential somatic mutation burdens**. Different cell types (neurons, glia, microglia) carry different burdens, with AD-status-correlated differences.
- The framing positions somatic mosaicism as an additional **non-Mendelian contribution to AD risk**, complementing inherited variation captured in GWAS (CLU, PICALM, APOE, etc.) and the rare familial APP/PSEN mutations.
- ROSMAP multi-omic data (DNA, RNA, ATAC, methylation across the same donors) is the substrate. Earlier Mathys 2019 *Nature* and Miller 2022 *Nature* single-cell studies of AD brain established the cell-type framework this paper extends.

## Methods / evidence

Pre-print on bioRxiv; the clipping captures the abstract and reference list. Analysis combines ROSMAP single-cell DNA mosaicism with single-cell transcriptomics of the same cohort. Cell types inferred from transcriptomic markers; somatic variants called per cell type; burden compared by AD case-control status.

## Surprising or load-bearing bits

- This is a **post-zygotic complement** to the heritable-variant story dominating AD genetics for two decades. If validated, somatic mosaicism may explain why APOE-ε4-noncarriers also develop AD: cell-type-restricted hits accumulate over a lifetime.
- The cell-type resolution is the key methodological move: bulk-tissue measurements can't distinguish "more burden in microglia" from "more burden in neurons" — and these have very different mechanistic implications.

## Connections to other sources

- Sits at the intersection of [[10-Summaries/bizzotto-2022-brain-mosaicism]] (mosaicism in brain) and the broader scDNA-seq methods landscape in [[10-Summaries/diane-2025-naturereviewsgenetics]].
- Extends Lodato et al. 2018 *Science* findings of age- and disease-associated neuronal mutation accumulation.
- Methodological dependence on PTA-class scWGA places it in the post-2019 generation of single-cell genomics, alongside [[10-Summaries/a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis]].

## Open questions

- The clipping captured by web-archive heavily weights the reference list over the methods/results sections. To extract specific burden estimates (e.g., per-cell SNV counts in AD microglia), need to read the PDF.
- Preprint; peer review still pending.

---
**Source:** [DOI](https://doi.org/10.1101/2022.04.21.489103)
## Related

- [[40-Topics/somatic-mosaicism]] · [[30-Concepts/alzheimers-disease]] · [[20-Entities/manolis-kellis]]
