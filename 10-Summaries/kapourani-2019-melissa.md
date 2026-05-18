---
type: summary
title: "Kapourani 2019 — Melissa: Bayesian clustering and imputation of single-cell methylomes"
source: "[[00-Sources/papers/Melissa_ Bayesian clustering and imputation of single-cell methylomes]]"
aliases: ["Kapourani 2019 Melissa", "Melissa", "MEthyLation Inference for Single cell Analysis"]
tags: [Melissa, scBS-seq, Bayesian-clustering, imputation, methylation, Sanguinetti-lab, Edinburgh]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/Melissa_ Bayesian clustering and imputation of single-cell methylomes]]"
---

**Citation:** Kapourani et al. (2019) — *Melissa: Bayesian clustering and imputation of single-cell methylomes* — *Genome Biology*. [DOI](https://doi.org/10.1186/s13059-019-1665-8)

Kapourani and Sanguinetti (Edinburgh) developed **Melissa** (MEthyLation Inference for Single cell Analysis), a Bayesian hierarchical method that jointly learns smooth methylation profiles over genomic regions of interest and clusters cells based on those profiles. The model fits a generalized-linear basis-function regression to each region's CpG observations per cell, with a Dirichlet-mixture prior providing the cell-clustering. Variational Bayes estimation gives both per-cell cluster membership and imputed methylation profiles for unobserved CpGs.

Key methodological idea: **local CpG correlations are informative for imputation** — the smoothness regularization within each region lets the model fill in sparse data using neighboring observed CpGs in the same cell, while the shared Dirichlet prior lets cells in the same cluster reinforce each other. Benchmarked on simulated and real scBS-seq data, Melissa achieves state-of-the-art imputation accuracy *and* biologically meaningful clustering.

## Why this matters

Companion to Epiclomal (de Souza 2020) in the §4 methylation-clustering tool family, with a different statistical philosophy: Melissa models smooth profiles per region; Epiclomal models discrete CpG calls. Both address the central scBS-seq pain point — 80–95% missing CpGs per cell. Methodological lineage continued by scMET (Kapourani 2021) which generalizes to heterogeneity quantification. Anchors §3.3 (methylation analysis) and §4 (computational methods for sparse epigenome data).

---
**Source:** [DOI](https://doi.org/10.1186/s13059-019-1665-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/30898142/)

---
**Source:** [DOI](https://doi.org/10.1186/s13059-019-1665-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/30898142/)

## Related

- [[10-Summaries/desouza-2020-epiclomal]]
- [[10-Summaries/kapourani-2021-scmet]]
- [[10-Summaries/angermueller-2017-genomebiol]]
- [[30-Concepts/methylation-imputation]]
