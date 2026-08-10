---
type: summary
title: "Kamimoto et al. 2023 — Dissecting cell identity via network inference and in silico gene perturbation (CellOracle)"
source: "[[00-Sources/papers/Dissecting cell identity via network inference and in silico gene perturbation]]"
source_kind: paper
author: "Kenji Kamimoto, Blerta Stringa, Christy M. Hoffmann, Kunal Jindal, Lilianna Solnica-Krezel, Samantha A. Morris (corresponding)"
published: 2023-02-08
ingested: 2026-08-10
doi: "10.1038/s41586-022-05688-9"
journal: "Nature"
tags: [CellOracle, GRN, in-silico-perturbation, transcription-factors, haematopoiesis, zebrafish, noto, lhx1a, signal-propagation]
entities: ["[[samantha-morris]]"]
concepts: ["[[gene-regulatory-network]]", "[[transcription-factor-motif]]", "[[scatac-seq]]", "[[cis-regulatory-element]]", "[[trajectory-inference]]", "[[multimodal-integration-methods]]"]
topics: ["[[computational-methods]]", "[[single-cell-lineage-tracing]]", "[[single-cell-multiomics]]"]
---

**Citation:** Kamimoto et al. (2023) — *Dissecting cell identity via network inference and in silico gene perturbation* — *Nature* 614, 742–751. [DOI](https://doi.org/10.1038/s41586-022-05688-9)

# Kamimoto 2023 — CellOracle

> Build cluster-specific gene-regulatory networks from multi-omic data, then **use the network as a function**: propagate a simulated transcription-factor knockout through it, compare the resulting expression shift to each cell's neighbours, and render the result as a **vector field of cell-identity transitions** on the embedding. Trained entirely on unperturbed wild-type data.

## Key claims

- **The gap addressed.** scRNA-seq with pooled CRISPR screens is powerful but unavailable in many biological contexts; computational simulators mostly require experimental perturbation data for training; deep-learning models are black boxes that obscure the regulatory mechanism; and existing GRN work focuses on static network structure, leaving open how a static network governs a dynamic process.
- **Four simulation steps**: (1) build cell-type/state-specific GRN configurations by cluster-wise regularized linear regression on multi-omic data; (2) propagate the **shift** in expression — not the absolute value — from TF to targets, iterating to capture broad downstream effects; (3) estimate cell-identity transition probability by comparing that shift against local neighbours' expression; (4) convert to a weighted local average vector. The multi-dimensional shift is deliberately reduced to a **2D vector**, because the goal is to model changes in *identity*, not to predict absolute expression, and the reduction is more robust to noise.
- **Two-stage GRN inference.** A **base GRN** comes from sequence: scATAC-seq peaks classified into promoters and enhancers using a TSS database and **[[pliner-2018-cicero|Cicero]]** co-accessibility, then scanned for TF-binding motifs. Because directionality comes from motifs and sequence rather than from expression, the second stage can use a simple **regularized linear model** on scRNA-seq to select active edges, with a Bayesian/bagging strategy pruning weak connections. Clustering before fitting is what keeps the linear assumption defensible.
- Base GRNs are prebuilt from a mouse scATAC atlas and as promoter-only versions for **ten commonly studied species**, so scATAC data is not required per sample.
- **Benchmarked against a ChIP-seq ground truth** of 1,298 datasets covering 80 regulatory factors across five tissues: **AUROC 0.66–0.85 with promoter base GRNs and 0.73–0.91 with scATAC base GRNs**.
- **The perturbation score** compares the perturbation vector's direction to the natural differentiation vector: negative means the knockout blocks or delays differentiation, positive means it promotes it.
- **Haematopoiesis validation.** On a 2,730-cell myeloid atlas with 24 clusters, *Spi1* (PU.1) knockout gave positive scores for MEPs and negative for GMPs, with *Gata1* exactly inverted — recapitulating the canonical lineage switch, including a mild *Gata1* phenotype in early granulocyte differentiation that **could not be inferred from *Gata1*'s low expression there**. Eight further TFs reproduced their reported knockout phenotypes; *Cebpa*, *Cebpe* and *Tal1* simulations matched experimental knockout cell distributions via a Markov random-walk simulation.
- **Systematic screening**: perturbing all 90 qualifying TFs and ranking by summed negative perturbation score, **85% of the top 30 are reported regulators of myeloid differentiation**, with ME-lineage, GM-lineage and dual-role factors separating in the expected regions of the scatter plot.
- **A new prediction, experimentally validated.** Across a 38,731-cell zebrafish embryogenesis atlas, 232 active TFs were perturbed. *noto* ranked top by degree centrality in axial mesoderm; its simulated loss reproduced the known loss of notochord and enhanced somite differentiation **and predicted a previously unreported enhanced prechordal plate phenotype**, which was then experimentally validated. The axial mesoderm regulator **lhx1a** was also identified.

## Methods / evidence

Three validation tiers: recapitulation of textbook TF biology, quantitative agreement with existing experimental knockout scRNA-seq data (*Cebpa*, *Cebpe*, *Tal1*), and prospective prediction followed by wet-lab confirmation in zebrafish. Plus an independent ChIP-seq-derived ground truth for the network-inference step alone, separating GRN quality from simulation quality — with null/randomized model analysis and hyperparameter evaluation.

## Surprising or load-bearing bits

- **Propagating a shift rather than an absolute value is the whole trick.** It lets the network act as a linear operator on a perturbation, which is why a simple regularized linear model suffices and why the result stays interpretable. Deep models predicting absolute expression give up both.
- **Deliberately limiting output to a 2D identity vector is a restraint worth noting.** The method could report predicted expression changes; it doesn't, because the identity question is answerable more robustly than the expression question. Choosing to predict less in order to predict reliably is unusual and is why the perturbation scores are trustworthy enough to screen with.
- **The *Gata1*-in-granulocytes result is the strongest argument for network-based reasoning.** A TF expressed at low level in a cell type can still matter there, and no expression-threshold or marker-based method can see that. Only propagating through connectivity recovers it.
- **Directionality from sequence, activity from expression** is a clean division of labour and the reason CellOracle avoids the causality-from-correlation problem that dogs coexpression-based GRN inference. It also makes [[pliner-2018-cicero|Cicero]] load-bearing infrastructure rather than a convenience.
- **The honest failure is reported**: CellOracle did not detect the known depletion of erythroid progenitors after *Spi1* knockout, attributed to **proliferation changes the method does not model**. A vector field over identity space cannot represent cells being made or dying — a structural limitation, not a tuning issue.
- **The authors also warn against their own summary statistic**: *Elf1*'s negative score in both lineages obscures its role, and only inspecting the vector field recovered the reported phenotype. The scalar is for screening; the vector is for interpretation.

## Entities mentioned

- [[samantha-morris]] — corresponding author; cell-identity and reprogramming program.

## Concepts touched

- [[gene-regulatory-network]] — cluster-specific directed networks used as simulation operators, not as static descriptions.
- [[transcription-factor-motif]] — context-dependent TF function quantified per cell state.

## Connections to other sources

- Depends on [[pliner-2018-cicero]] for enhancer/promoter classification; benchmarked against in [[bravo-2023-scenicplus]].
- Input atlases and trajectories: [[cao-2019-moca]], [[wolf-2019-paga]].
- Accessibility data source: [[cusanovich-2015-sciatac]]; motif/annotation tooling: [[heinz-2010-homer]].
- Multi-omic integration framing: [[argelaguet-2021-integration-principles]], [[zhu-2020-multimodal-power-of-many]].

## Open questions

- **Proliferation and cell death are outside the model**, and the *Spi1* miss shows this produces real false negatives. Any phenotype mediated by differential expansion rather than fate change is invisible.
- The linear-model assumption is defended by pre-clustering, but the paper does not establish how fine the clustering must be for it to hold, or what happens when a cluster spans a genuinely non-linear regulatory regime.
- GRN inference AUROC of 0.66–0.91 means a substantial minority of edges are wrong; how that error propagates through iterative signal propagation is not characterized.

## Related

- [[gene-regulatory-network]] · [[pliner-2018-cicero]] · [[bravo-2023-scenicplus]] · [[computational-methods]]
