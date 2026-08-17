---
type: summary
title: "Yuan & Duren 2024 — Inferring gene regulatory networks from single-cell multiome data using atlas-scale external data (LINGER)"
source: "[[00-Sources/papers/Inferring gene regulatory networks from single-cell multiome data using atlas-scale external data]]"
source_kind: paper
author: "Qiuyue Yuan, Zhana Duren (corresponding)"
published: 2024-04-12
ingested: 2026-08-17
doi: "10.1038/s41587-024-02182-7"
journal: "Nature Biotechnology 43:247–257"
tags: [LINGER, gene-regulatory-network, lifelong-learning, manifold-regularization, TF-activity, GWAS, PECA, SCENIC-plus]
entities: ["[[zhana-duren]]"]
concepts: ["[[gene-regulatory-network]]", "[[cis-regulatory-element]]", "[[transcription-factor-motif]]", "[[multimodal-integration-methods]]", "[[joint-single-cell-multi-omics]]", "[[chromatin-accessibility]]"]
topics: ["[[single-cell-multiomics]]", "[[computational-methods]]", "[[single-cell-atac-seq]]"]
---

**Citation:** Yuan & Duren (2024) — *Inferring gene regulatory networks from single-cell multiome data using atlas-scale external data* — *Nature Biotechnology* 43, 247–257. [DOI](https://doi.org/10.1038/s41587-024-02182-7)

# Yuan 2024 — LINGER

> GRN inference has a data problem disguised as a modelling problem: single-cell data supplies many *cells* but few **independent** data points, while the model has enormous numbers of parameters. LINGER's answer is **lifelong learning** — pre-load knowledge from atlas-scale external **bulk** data across diverse cellular contexts, then adapt to the single-cell multiome at hand. Reported gain: a **fourfold to sevenfold relative increase in accuracy**.

## Key claims

- **The field's accuracy baseline was dismal.** The paper states plainly that inferred GRN accuracy assessed against experimental data had been "only marginally better than random prediction." That is the bar LINGER is measured against.
- **Three persistent challenges are named**: learning a complex mechanism from limited *independent* data points (most single cells are not independent); incorporating prior knowledge such as motif matching into non-linear models; and the poor accuracy just described.
- **Three corresponding contributions**: lifelong learning to import atlas-scale bulk knowledge; **manifold regularisation** to inject TF–RE motif-matching priors into a neural model; and TF-activity estimation from expression alone.
- **Co-expression methods cannot give direction or causality.** WGCNA, ARACNe and GENIE3 infer TF–target links from covariation, producing **undirected** edges — you cannot tell TF_A→TF_B from TF_B→TF_A — and co-expression is correlation, not causal regulation.
- **Motif-based footprinting cannot separate within-family TFs** that share a motif. This is the same limitation [[debnath-2026-ison|ISON]] later addresses from the same group by bringing expression into the model.
- **Three network levels, three edge types.** Output is a cell-population GRN, cell-type-specific GRNs, and cell-level GRNs; each contains *trans*-regulation (TF–TG), *cis*-regulation (RE–TG), and TF binding (TF–RE). TF self-regulation is explicitly excluded as unmodellable without extra data.
- **TF activity from bulk or single-cell expression alone**, once the GRN is learned from a reference multiome — which turns the vast existing archive of expression-only case-control studies into a source of driver-regulator hypotheses.
- **GWAS interpretation is the headline application**: the inferred regulatory landscape enables improved interpretation of disease-associated variants and genes.

## Methods / evidence

Benchmarked against existing GRN methods with accuracy assessed against experimental data; applied to GWAS variant interpretation and to case-control driver-regulator identification.

Weight: "fourfold to sevenfold relative increase" over a near-random baseline still leaves the absolute accuracy an open question — a relative improvement on a weak baseline is the honest reading, and the paper's own framing of the field's accuracy problem invites it. (synthesis)

## Surprising or load-bearing bits

- **"Most single cells are not independent" is the underappreciated statistical point.** Thousands of cells from one donor, one tissue, one state provide far less information than the cell count suggests — the effective sample size is closer to the number of distinct states than to the number of cells. This applies well beyond GRN inference, to every single-cell method that treats cells as replicates (including [[yu-2021-snaphic|SnapHiC]] and [[park-2026-mintsc|MINTsC]] in the 3D-genome world). (synthesis)
- **Bulk data as prior knowledge, not as a competitor.** The bulk-versus-single-cell framing that runs through this field is inverted here: bulk's cell-type heterogeneity is a liability for direct inference but an asset as a pre-training corpus spanning contexts no single experiment covers. (synthesis)
- **Manifold regularisation as the mechanism for injecting priors into neural models** is a transferable technique — the general problem of "how do I make a deep model respect known biology" recurs everywhere.
- **The within-family TF problem is a recurring blind spot.** Motif-based accessibility methods ([[schep-2017-chromvar|chromVAR]] and successors) structurally cannot resolve paralogues; only bringing expression in does. Both LINGER and [[debnath-2026-ison|ISON]] make this argument, from the same lab.
- **PECA is the bulk ancestor** — the same group's earlier statistical model fitting target-gene expression from TF expression and RE accessibility across cell-type panels. LINGER is PECA's knowledge, transferred.

## Entities mentioned

- [[zhana-duren]] — corresponding author; also [[debnath-2026-ison|ISON]], which uses LINGER for spatially resolved GRN reconstruction.

## Concepts touched

- [[gene-regulatory-network]] — three-level GRNs with three edge types; lifelong learning from bulk.
- [[transcription-factor-motif]] — motif matching as manifold regularisation rather than as a hard filter.

## Connections to other sources

- Direct downstream use by the same group: [[debnath-2026-ison]].
- Contemporary multiome GRN method: [[bravo-2023-scenicplus]]; perturbation-oriented [[kamimoto-2023-celloracle]]; peak–gene linking [[pliner-2018-cicero]].
- Motif-activity methods it critiques: [[schep-2017-chromvar]], and accessibility frameworks [[granja-2021-archr]], [[zhang-2024-snapatac2]], [[bravo-2019-cistopic]].
- Multiome assays that supply its input: [[ma-2020-cell]] (SHARE-seq), [[cao-2018-sci-car]], [[clark-2018-scnmt-seq]].
- Integration context: [[argelaguet-2021-integration-principles]], [[xiao-2024-multiomics-benchmark]], [[hao-2021-seurat-wnn]].
- GWAS-to-gene assignment from a different data type: [[yu-2021-snaphic]], [[park-2026-mintsc]].

## Open questions

- **Absolute accuracy remains unclear** — a 4–7× improvement over near-random is a real gain whose ceiling is unstated.
- Lifelong learning imports bulk knowledge, and therefore bulk biases; whether pre-training on contexts unlike the target tissue helps or hurts is not characterised. (synthesis)
- TF self-regulation is excluded, which removes a common and biologically important motif class.
- Cell-level GRNs are produced but their reliability at that resolution is not separately validated.

## Related

- [[debnath-2026-ison]] · [[bravo-2023-scenicplus]] · [[gene-regulatory-network]] · [[40-Topics/single-cell-multiomics]]
