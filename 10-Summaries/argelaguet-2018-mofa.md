---
type: summary
title: "Argelaguet et al. 2018 — Multi-Omics Factor Analysis: a framework for unsupervised integration of multi-omics data sets"
source: "[[00-Sources/papers/Multi‐Omics Factor Analysis—a framework for unsupervised integration of multi‐omics data sets - Molecular Systems Biology]]"
source_kind: paper
author: "Ricard Argelaguet, Britta Velten, Damien Arnol, Sascha Dietrich, Thorsten Zenz, John C Marioni, Florian Buettner, Wolfgang Huber, Oliver Stegle"
published: 2018-06-20
ingested: 2026-10-07
doi: "10.15252/msb.20178124"
journal: "Molecular Systems Biology 14(6):MSB178124"
tags: [MOFA, factor-analysis, multi-omics-integration, unsupervised, clipping-incomplete]
entities: ["[[oliver-stegle]]"]
concepts: ["[[multimodal-integration-methods]]", "[[dimensionality-reduction]]", "[[joint-single-cell-multi-omics]]"]
topics: ["[[single-cell-multiomics]]", "[[computational-methods]]"]
---

**Citation:** Argelaguet et al. (2018) — *Multi‐Omics Factor Analysis—a framework for unsupervised integration of multi‐omics data sets* — *Molecular Systems Biology* 14(6):MSB178124. [DOI](https://doi.org/10.15252/msb.20178124)

# Argelaguet 2018 — MOFA

> **Source caveat:** the clipping in `00-Sources/` contains only the article's truncated abstract (in frontmatter), the reference list and author affiliations — **no main text, results or methods**. This summary therefore records only what the clipping supports. The abstract fragment frames the problem: multi-omics studies promise better characterisation of biological processes across molecular layers, but methods for unsupervised integration of such data are needed. The paper introduces MOFA (Multi-Omics Factor Analysis), the method later extended as MOFA+ ([[argelaguet-2020-mofa-plus]]).

## Key claims

- From the clipping: MOFA is presented as a framework for **unsupervised integration of multi-omics data sets** (title and abstract fragment).
- According to the wiki's MOFA+ summary (not this clipping), MOFA is a Bayesian group factor analysis framework that recovers latent factors explaining shared and modality-specific variation across views, and MOFA+ later added stochastic variational inference and multi-group sparsity priors ([[argelaguet-2020-mofa-plus]]).
- No quantitative results can be stated from this source.

## Methods / evidence

Not available in the clipping. The reference list cites, among others, group factor analysis (Klami et al. 2015; Virtanen et al. 2012; Bunte et al. 2016), variational inference reviews, chronic lymphocytic leukaemia (CLL) drug-perturbation data (Dietrich et al. 2018) and single-cell multi-omics assays (scNMT-seq, G&T-seq, parallel scM&T-seq), suggesting — but not establishing — the methodological lineage and application datasets. (synthesis)

Weight: **low as a source** for anything beyond bibliographic identity. A full-text re-clip is needed before this page can support factual claims.

## Surprising or load-bearing bits

- The load-bearing role of this paper in the wiki is as the **origin of the MOFA family** of linear, sample-space integration models, which [[argelaguet-2020-mofa-plus]] scales up and which [[argelaguet-2021-integration-principles]] places within the broader integration landscape. (synthesis)

## Concepts touched

- [[multimodal-integration-methods]] — founding paper of the factor-analysis branch.
- [[dimensionality-reduction]] — latent factors as the shared low-dimensional representation (per the MOFA+ summary).

## Connections to other sources

- Successor: [[argelaguet-2020-mofa-plus]]; review by the same group: [[argelaguet-2021-integration-principles]].
- Single-cell multi-omics assays cited in its references and summarised in the wiki: [[clark-2018-scnmt-seq]], [[macaulay-2015-gt-seq]]; later application to mouse gastrulation multi-omics: [[argelaguet-2019-nature]]. (synthesis)
- Contrasting integration families: [[welch-2019-liger]], [[hao-2021-seurat-wnn]], [[cao-2022-glue]], [[ashuach-2023-multivi]].

## Open questions

- Re-clip the full text to capture the model, CLL application and single-cell (scMT) application, then update this page.

## Related

- [[argelaguet-2020-mofa-plus]] · [[multimodal-integration-methods]] · [[40-Topics/single-cell-multiomics]]
