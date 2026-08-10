---
type: summary
title: "Argelaguet, Cuomo, Stegle & Marioni 2021 — Computational principles and challenges in single-cell data integration"
source: "[[00-Sources/papers/Computational principles and challenges in single-cell data integration]]"
source_kind: paper
author: "Ricard Argelaguet, Anna S. E. Cuomo, Oliver Stegle, John C. Marioni (corresponding)"
published: 2021-05-03
ingested: 2026-08-10
doi: "10.1038/s41587-021-00895-7"
journal: "Nature Biotechnology (Review)"
tags: [data-integration, anchors, horizontal-vertical-diagonal, mosaic-integration, transfer-learning, batch-correction, taxonomy, review]
entities: ["[[oliver-stegle]]"]
concepts: ["[[multimodal-integration-methods]]", "[[joint-single-cell-multi-omics]]", "[[scnmt-seq]]", "[[chromvar]]", "[[spatial-multiomics]]", "[[cite-seq]]"]
topics: ["[[single-cell-multiomics]]"]
---

**Citation:** Argelaguet, Cuomo, Stegle & Marioni (2021) — *Computational principles and challenges in single-cell data integration* — *Nature Biotechnology* 39, 1202–1215. [DOI](https://doi.org/10.1038/s41587-021-00895-7)

# Argelaguet 2021 — the anchor taxonomy

> "Data integration" had come to mean everything from batch correction to eQTL mapping. This review imposes one organizing question — **what is the anchor linking the datasets?** — and derives from it a taxonomy (horizontal / vertical / diagonal / mosaic) that determines which assumptions you are making and therefore which methods are legitimate.

## Key claims

- **The anchor determines everything.** Three primary regimes:
  - **Horizontal** — features are the anchor, across unmatched experiments of the same type. This is batch correction.
  - **Vertical** — cells (or groups of cells) are the anchor, in matched multimodal experiments.
  - **Diagonal** — *no anchor exists* in the high-dimensional space; different modalities profiled in different cells.
- **Horizontal**: bulk methods (limma, ComBat) fail because they implicitly assume identical or known cell-type composition across batches, which is violated even between biological replicates. Single-cell methods (MNN, Seurat v3, LIGER, Harmony, BBKNN, scVI, conos, Scanorama) all use nonlinear or locally-linear strategies. Shared failure modes: **overcorrection** (forcibly merging non-matching subpopulations when no shared biological axis exists — a good method should detect this and refuse); integration performed in latent space **distorts the high-dimensional observations**, so downstream marker detection and differential expression become problematic; and when biological variability tracks batch (e.g. a developmental time course that cannot be randomized), the two are not separable.
- **Vertical splits into local and global.** Local = supervised feature-pair association (eQTL mapping, methylation-to-expression), typically regression, usually restricted to *cis* windows to keep multiple testing and interpretation tractable, with **linear mixed models** handling relatedness, population structure and repeated cells per donor.
- **The confounding warning for epigenetic association is the practically important one**: ATAC peaks with high GC show higher accessibility, and high-CpG-density regions show low methylation, so sequence context is a systematic confounder. [[chromvar|chromVAR]]'s solution — build a per-feature null from randomly selected features with *matched sequence context* — is offered as the template. Modality-wide confounders (global methylation level differing by cell type) should enter as covariates, as PCA/PEER factors do in eQTL work.
- **Global** vertical integration uses matrix factorization: CCA (Seurat), [[argelaguet-2020-mofa-plus|MOFA]], JIVE, PLS, MCIA, iNMF. MOFA generalizes CCA to arbitrary modality counts and, via structured sparsity priors, separates **shared** from **modality-private** variation. WNN (Seurat v4) extends nearest-neighbor graphs instead.
- Four practical challenges for factorization models, each concrete: heterogeneous statistical properties across modalities (counts vs binary CpG calls) require combining likelihoods; **feature-count imbalance** (dozens of antibodies vs thousands of genes) lets the larger modality dominate the latent space; solution quality is hard to assess — variance explained helps, but robustness should be checked by bootstrapping or downsampling; and linearity buys interpretability at the cost of explanatory power, with VAEs the nonlinear alternative at the cost of interpretability.
- **Diagonal is the hard one.** It requires assuming a latent manifold is preserved across modalities. Common workarounds reduce it to an easier problem: aggregate cells into shared cell types (vertical, but assumes the cell-type definition and loses single-cell resolution) or link features one-to-one (horizontal, e.g. gene-body accessibility ↔ expression). The linkage assumption "can fail in scenarios where such linkages are incomplete and when the relationship between the molecular layers is complex" — **explicitly, early embryonic development, where gene-body methylation and accessibility do not predict expression.** MATCHER, MMD-MA, SCIM, UnionCom attempt genuine manifold alignment.
- **Mosaic integration** — the fourth regime, and the one the review argues will become ubiquitous: different modalities profiled on different cell populations from the same sample, giving entirely missing data matrices where some pairs are anchored by cells, some by features, some by neither. Sequential rounds of the three basic operations work but are order- and feature-selection-dependent; multitask learning with uncertainty propagation is the proposed proper solution.
- **Transfer learning** reframes reference atlases: extract a compressed representation of the reference rather than loading it alongside the query. Anchor is still features, but the relationship is hierarchical rather than symmetric.
- Time and space are treated as further integration dimensions: dynamic time warping for aligning trajectories that tick at different rates across species (Kanton et al. found human-specific programs precisely where trajectories *failed* to align); SpatialDE and SVCA for spatial variance decomposition, the latter with an explicit cell–cell interaction component.

## Methods / evidence

A conceptual review with method and benchmark-dataset tables, from authors who build these tools (MOFA, scNMT-seq). Its value is definitional rather than evidentiary — but the definitions are load-bearing, because they make the assumptions of each method class explicit and therefore checkable.

## Surprising or load-bearing bits

- **Diagonal integration is the regime most single-cell epigenomics actually lives in, and the review says it is the hardest and least validatable.** Most of this wiki's modalities — scATAC, scBS, scCUT&Tag, single-cell Hi-C — are generated in separate cells from the transcriptome. Every claim of the form "we integrated our scATAC with published scRNA" is a diagonal integration resting on the assumption that a shared manifold exists, and "there is no guarantee that their latent manifolds can in fact be aligned."
- The early-development counterexample is the sharpest caution in the review: the gene-activity-score heuristic — accessibility or gene-body methylation as a proxy for expression, used by essentially every scATAC pipeline — **is known to fail** in exactly the systems where multi-omics is most wanted.
- **Sequence-context confounding** is a specific, actionable warning for epigenomic association testing that is widely ignored: GC content drives both accessibility and methylation, so any naive correlation between them is partly sequence composition.
- Feature-count imbalance means that in a CITE-seq or scCUT&Tag-pro-style design, the modality with more features silently dominates the joint embedding unless explicitly reweighted — the problem WNN exists to solve.
- Overcorrection as a *named* failure mode with a stated ideal behavior ("an optimal method should be able to detect this and prevent merging") is a benchmark criterion most integration papers do not report.
- Mosaic integration describes the actual structure of this wiki's corpus: dozens of modalities, each measured in different cells, sharing samples but not cells.

## Entities mentioned

- [[oliver-stegle]] — co-author; MOFA, scNMT-seq analysis, LMM-based association methods.
- Ricard Argelaguet — first author; [[argelaguet-2020-mofa-plus|MOFA+]] and [[clark-2018-scnmt-seq|scNMT-seq]].

## Concepts touched

- [[multimodal-integration-methods]] — the anchor taxonomy is the organizing frame for this page.
- [[joint-single-cell-multi-omics]] — vertical integration is what joint assays buy you, and this explains precisely what that is worth.
- [[chromvar]] — cited as the model for sequence-context-matched null construction.

## Connections to other sources

- Assay-side counterpart to [[zhu-2020-multimodal-power-of-many]]: that paper taxonomizes the experiments, this one taxonomizes the analyses.
- Methods discussed and bookmarked here: [[argelaguet-2020-mofa-plus|MOFA+]], [[korsunsky-2019-harmony|Harmony]], [[welch-2019-liger|LIGER]], [[hao-2024-seurat-v5|Seurat/WNN]], [[cao-2022-glue|GLUE]], [[ashuach-2023-multivi|MultiVI]], [[gong-2021-cobolt|Cobolt]].
- Benchmarked empirically in [[xiao-2024-multiomics-benchmark]] and [[luo-2024-scatac-benchmark]].
- The mosaic problem is exactly what [[zhang-2022-sccut-tag-pro]] solves via shared protein anchors.
- Practice-level companion: [[heumos-2023-best-practices]].

## Open questions

- No source in this corpus **validates** a diagonal integration against ground truth for an epigenomic modality — the review proposes matched multimodal assays as the gold standard for exactly this, and that benchmark is the gap.
- Mosaic integration methods with proper uncertainty propagation are proposed, not delivered; whether any exists now is unaddressed here.
- The genotype–epigenome anchor (somatic mutation ↔ chromatin state) is absent from the taxonomy entirely — see [[mosaicism-and-epigenome-the-synthesis-gap]].

## Related

- [[multimodal-integration-methods]] · [[zhu-2020-multimodal-power-of-many]] · [[argelaguet-2020-mofa-plus]] · [[single-cell-multiomics]]
