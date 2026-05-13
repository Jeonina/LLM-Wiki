---
type: summary
title: "Jahn 2016 — Tree inference for single-cell data (SCITE)"
aliases: ["Jahn 2016 SCITE", "SCITE", "Beerenwinkel-lab phylogeny"]
tags: [SCITE, tumor-phylogeny, MCMC, allelic-dropout, infinite-sites, Beerenwinkel-lab, ETH-Zurich, founding-method]
created: 2026-05-13
updated: 2026-05-13
sources: ["Katharina_2016_GenomeBiology.pdf"]
---

Jahn, Kuipers and Beerenwinkel (ETH Zurich, SIB) developed **SCITE** (Single-Cell Inference of Tumor Evolution), a stochastic-search algorithm for identifying the evolutionary history of a tumor from noisy, incomplete mutation profiles of single cells. SCITE uses a flexible MCMC sampling scheme that computes the maximum-likelihood mutation history, samples from the posterior distribution, and **simultaneously estimates the error rates** (false-positive, false-negative, and allelic-dropout) of the underlying sequencing experiments.

Key design choices: (i) accommodates the very high allelic-dropout rates of scWGS data (often ≥10% FN rate); (ii) models elevated FP rate inherent to scWGS variant calling; (iii) handles missing data (often 58%+ of sites in early single-nucleus datasets); (iv) reconstructs the **mutation tree** (not just the cell-genealogy tree), defining sub-clones by the mutation profiles inherited along the path from the root. Improved scalability and reconstruction accuracy compared to predecessors (OncoNEM, Sci-Phi).

## Why this matters

A founding paper for scDNA-seq tumor phylogeny inference, alongside OncoNEM and Sci-Phi. SCITE established the now-standard pattern of jointly inferring tree topology AND error parameters from the same noisy data — a critical methodological move given that scWGS error rates are too high and too variable to set as fixed priors. Conceptual ancestor of SCARLET (Satas 2020), B-SCITE, and most later single-cell phylogeny methods. Anchors §4 (phylogenetic methods family) and §5 (cancer-evolution applications). Important context: the Beerenwinkel lab is one of the three main computational hubs (alongside Raphael at Princeton and Marschall/Korbel at EMBL) for single-cell tumor phylogenetics.

## Related

- [[10-Summaries/satas-2020-scarlet]]
- [[10-Summaries/zafar-2017-cellrev]]
- [[10-Summaries/zaccaria-2021-chisel]]
- [[40-Topics/scdna-cancer-applications]]
