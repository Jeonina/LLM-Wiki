---
type: concept
title: Gene Regulatory Network
aliases: [GRN, eGRN, regulon, eRegulon, network inference]
tags: [GRN, transcription-factors, enhancers, network-inference, perturbation]
created: 2026-08-10
updated: 2026-08-10
---

# Gene Regulatory Network

> The set of transcription-factor-to-target relationships that specify a cell's identity. Inferring one from single-cell data means solving two problems at once: which elements a TF acts through, and which of the possible edges are active in a given cell state.

## Directionality from sequence, activity from expression

Coexpression alone cannot establish causality (synthesis). Both current frameworks solve this by deriving edge direction from genomic sequence and using expression only to select active edges:

- A **base GRN** from scATAC peaks classified into promoters and enhancers (using a TSS database plus co-accessibility, [[pliner-2018-cicero]]) and scanned for TF-binding motifs, followed by cluster-wise regularized linear regression on scRNA-seq with Bayesian/bagging pruning ([[kamimoto-2023-celloracle]]).
- **eRegulons** — a TF with its target enhancers *and* genes — from topics and differentially accessible regions as enhancer candidates, motif enrichment against a 32,765-motif collection, and GRNBoost2 importance scoring with direction of regulation from linear correlation ([[bravo-2023-scenicplus]]).

Benchmarked against ChIP-seq ground truth, network inference reaches AUROC 0.66–0.85 with promoter-only base networks and 0.73–0.91 with scATAC-derived ones ([[kamimoto-2023-celloracle]]).

## Why the enhancer layer matters

Only **49% of enhancers are predicted to regulate their most proximal gene** ([[bravo-2023-scenicplus]]) — the quantitative case against nearest-gene assignment. Representing target regions also makes TF **cooperativity** directly computable: top cell-type-specific TFs largely co-bind shared enhancers, which is not seen for TFs specific to different cell types ([[bravo-2023-scenicplus]]).

## Networks as operators, not descriptions

Propagating a **shift** in expression rather than an absolute value lets the network act as a linear operator on a perturbation, converting a static structure into an in-silico knockout simulator trained only on unperturbed data ([[kamimoto-2023-celloracle]]). Systematic screening ranked TFs such that **85% of the top 30 are reported regulators** of myeloid differentiation ([[kamimoto-2023-celloracle]]), and prospective prediction of a *noto* loss-of-function phenotype in zebrafish was experimentally validated ([[kamimoto-2023-celloracle]]).

The strongest argument for network reasoning: *Gata1*'s mild phenotype in early granulocyte differentiation is recovered by the network but **cannot be inferred from its low expression there** ([[kamimoto-2023-celloracle]]).

## Open questions

- Binding is not regulation — predicted enhancer-gene links are validated against TF-binding ChIP-seq, not against functional perturbation of the enhancer ([[bravo-2023-scenicplus]]).
- Motif-based assignment cannot distinguish family members sharing a motif ([[bravo-2023-scenicplus]]).
- A substantial minority of inferred edges are wrong at reported AUROCs, and how that error propagates through iterative signal propagation is uncharacterized ([[kamimoto-2023-celloracle]]).

## Related

- [[cis-regulatory-element]] · [[enhancer-states]] · [[transcription-factor-motif]] · [[computational-methods]]

## Added 2026-08-17

[[10-Summaries/yuan-2024-linger|LINGER]] reframes GRN inference as a **data** problem rather than a modelling one: single-cell data supplies many cells but few *independent* data points, while the model has enormous numbers of parameters. Its fix is **lifelong learning** — pre-load knowledge from atlas-scale external **bulk** data across diverse contexts, then adapt to the multiome at hand — plus **manifold regularisation** to inject TF–RE motif priors into a non-linear model ([[10-Summaries/yuan-2024-linger]]).

Reported gain: a **fourfold to sevenfold relative increase** in accuracy — against a field the paper itself describes as having been "only marginally better than random prediction" ([[10-Summaries/yuan-2024-linger]]). A relative improvement on a weak baseline is the honest reading. (synthesis)

**Two structural limitations of prior approaches, named precisely** ([[10-Summaries/yuan-2024-linger]]): co-expression methods (WGCNA, ARACNe, GENIE3) produce **undirected** edges — TF_A–TF_B cannot be oriented — and correlation is not causal regulation. Motif-based footprinting **cannot distinguish within-family TFs** that share a motif; only bringing expression into the model breaks the tie, an argument the same group repeats for spatial data in [[10-Summaries/debnath-2026-ison]].

Output is three network levels (cell-population, cell-type-specific, cell-level) each with three edge types — *trans* (TF–TG), *cis* (RE–TG), TF-binding (TF–RE). TF self-regulation is explicitly excluded as unmodellable without additional data ([[10-Summaries/yuan-2024-linger]]).

**"Most single cells are not independent"** is the underappreciated point, and it generalises: thousands of cells from one donor, tissue and state carry far less information than the cell count suggests. The same caution applies to every method that treats cells as statistical replicates, including [[10-Summaries/yu-2021-snaphic|SnapHiC]] and [[10-Summaries/park-2026-mintsc|MINTsC]]. (synthesis)
