---
type: summary
title: "Argelaguet 2020 — MOFA+: statistical framework for comprehensive integration of multi-modal single-cell data"
source: "[[00-Sources/papers/MOFA+_ a statistical framework for comprehensive integration of multi-modal single-cell data]]"
aliases: ["Argelaguet 2020 MOFA+", "MOFA+", "Multi-Omics Factor Analysis v2"]
tags: [MOFA+, factor-analysis, multimodal-integration, stochastic-variational-inference, Marioni-lab, Stegle-lab, EBI]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/MOFA+_ a statistical framework for comprehensive integration of multi-modal single-cell data]]"
---

**Citation:** Argelaguet et al. (2020) — *MOFA+: statistical framework for comprehensive integration of multi-modal single-cell data* — *Genome Biology*. [DOI](https://doi.org/10.1186/s13059-020-02015-1)

Argelaguet, Arnol, Bredikhin, Deloro, Velten, Marioni, Stegle (EBI + EMBL Heidelberg) developed **MOFA+**, a scalable extension of Multi-Omics Factor Analysis (MOFA). MOFA itself was a Bayesian Group Factor Analysis framework recovering latent factors that explain shared and modality-specific variation across views. MOFA+ adds: (i) **stochastic variational inference on GPUs** — enabling analysis of millions of cells, addressing MOFA's scalability ceiling; (ii) **structured sparsity priors** for multiple sample groups (batches, donors, conditions), enabling joint modeling across sample groups and data modalities. Inputs are multiple matrices grouped into views (modalities) and grouped along the sample axis. Outputs are interpretable latent factors with weights identifying modality-feature contributions. Contrasts with Seurat-v3/LIGER which align datasets via common features; MOFA+ instead integrates modalities via a common **sample** space.

## Why this matters

Established factor-analysis-based multimodal integration as a scalable alternative to deep-learning approaches (Cobolt, MultiVI, GLUE). Anchors §4 (multimodal integration tool family) — typically cited alongside Seurat-WNN, Cobolt, GLUE, MultiVI as the "MOFA family" of integration methods. Still widely used for scNMT-seq, CITE-seq, and other multimodal-scDNA analyses. Important historical anchor for the linear-Bayesian branch of multimodal integration.

---
**Source:** [DOI](https://doi.org/10.1186/s13059-020-02015-1) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32393329/)

## Related

- [[10-Summaries/gong-2021-cobolt]]
- [[10-Summaries/ashuach-2023-multivi]]
- [[10-Summaries/cao-2022-glue]]
- [[10-Summaries/clark-2018-scnmt]]
- [[30-Concepts/multimodal-integration-methods]]
