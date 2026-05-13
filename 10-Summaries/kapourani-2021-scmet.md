---
type: summary
title: "Kapourani 2021 — scMET: Bayesian modeling of DNA methylation heterogeneity at single-cell resolution"
aliases: ["Kapourani 2021 scMET", "scMET"]
tags: [scMET, scBS-seq, methylation-heterogeneity, beta-binomial, Bayesian, overdispersion, Vallejos-lab, Sanguinetti-lab, Edinburgh]
created: 2026-05-13
updated: 2026-05-13
sources: ["Chantriolnt_2021_GenomeBiology.pdf"]
---

Kapourani, Argelaguet, Sanguinetti and Vallejos (Edinburgh, EMBL-EBI) developed **scMET**, a hierarchical Bayesian framework that quantifies **methylation heterogeneity** — i.e., the residual cell-to-cell variability in methylation level *not* explained by mean methylation rate or technical bias. The model couples a beta-binomial likelihood (modeling over-dispersed CpG counts) with a generalized linear model on feature characteristics (CpG density, etc.), sharing information across cells and genomic features via a hierarchical prior.

Critical capability: scMET decomposes observed variance into technical (sparsity, depth, sequencing error) and biological components, then enables (i) identification of **highly variable features** (HVFs) for unsupervised clustering, (ii) **differential variability testing** between groups of cells (e.g., wild-type vs perturbed), (iii) characterization of epigenetically distinct populations. Validated on two large-scale scBS-seq datasets including multi-omics joint assays.

## Why this matters

scMET fills a niche orthogonal to Melissa and Epiclomal: those tools cluster cells; scMET *quantifies variability itself* as a biological signal. Particularly relevant for mosaicism studies where the question is not "what are the methylation clones" but "where in the genome does methylation vary between cells?" — an essential prerequisite for treating methylation as a mosaicism axis. Anchors §3.3 (methylation heterogeneity), §4 (computational tools), and §6 (limitations — separating technical from biological variance is the central challenge in scBS-seq interpretation).

## Related

- [[10-Summaries/kapourani-2019-melissa]]
- [[10-Summaries/desouza-2020-epiclomal]]
- [[10-Summaries/argelaguet-2019-mofa]]
- [[30-Concepts/methylation-clones-epimutation]]
