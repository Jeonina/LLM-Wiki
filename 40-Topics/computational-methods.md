---
type: topic
title: Computational Methods
aliases: [bioinformatics tooling, analysis pipelines, computational infrastructure]
tags: [pipelines, algorithms, tools, infrastructure]
created: 2026-08-10
updated: 2026-08-10
---

# Computational Methods

> The tool layer of this wiki: the aligners, formats, callers, imputers, integrators and network-inference frameworks that turn raw single-cell and epigenomic sequencing into interpretable results. Assay pages describe what was measured; these describe what was done to it.

## Why this is a topic

Method choice is not neutral. Seven TAD callers disagree on the same contact matrix ([[kerpedjiev-2018-higlass]]); two Hi-C pipelines with identical input produce maps correlating at 0.83, not 1.0 ([[servant-2015-hicpro]]); a ChIP-seq peak caller run on CUT&RUN data emits up to ~900 peaks for a factor that is not expressed ([[meers-2019-seacr]]). Conclusions in this corpus are conditional on tooling, and this page exists so that dependency stays visible.

## The stack

**Preprocessing and alignment.** QC, adapter and polyG trimming, UMI handling in a single pass ([[chen-2018-fastp]]); BWT-based read alignment ([[li-2009-bwa]]); the SAM/BAM format and toolkit that decoupled alignment from every downstream analysis ([[li-2009-samtools]]); chromatin-optimized fast alignment ([[zhang-2021-chromap]]).

**Variant and copy-number calling.** Germline/somatic SNV calling infrastructure ([[mckenna-2010-gatk]]); single-cell CNV by HMM over mappability-variable bins ([[bakker-2016-aneufinder]]), by circular binary segmentation ([[garvin-2015-natmethods]]) and by Poisson-latent-factor modelling ([[wang-2020-scope]]); CNV inferred from transcriptomes ([[tickle-2019-infercnv]], [[gao-2021-copykat]]); mutational-process decomposition ([[alexandrov-2013-mutational-signatures]]).

**Chromatin and peak calling.** Empirical fragment-shift modelling with dynamic local background ([[zhang-2008-macs]]); model-free thresholding for low-background in-situ assays ([[meers-2019-seacr]]); motif and peak toolkit ([[heinz-2010-homer]]); region-to-gene functional annotation ([[mclean-2010-great]]); single-cell methylation segmentation ([[kremer-2024-methscan]]).

**Hi-C pipelines, storage and visualization.** Read-to-normalized-matrix processing with ICE and allele-specific modes ([[servant-2015-hicpro]]); the Juicer toolchain ([[durand-2016-juicer]]); the sparse HDF5 cooler format adopted by 4D Nucleome ([[abdennur-2020-cooler]]); composable linked-view browsing ([[kerpedjiev-2018-higlass]]).

**Single-cell Hi-C imputation.** Convolution plus random walk with top-20% selection to defeat coverage bias ([[zhou-2019-schicluster]]); hypergraph representation learning that borrows across cells and integrates co-assayed modalities ([[zhang-2022-higashi]]).

**Embedding, clustering, integration.** Dimensionality reduction ([[mcinnes-2018-umap]]); community detection with connectivity guarantees ([[traag-2019-leiden]]); batch correction in embedding space across multiple covariates ([[korsunsky-2019-harmony]]); factorization into shared and dataset-specific factors ([[welch-2019-liger]]); anchor- and bridge-based integration ([[hao-2024-seurat-v5]]); the conceptual taxonomy ([[argelaguet-2021-integration-principles]]).

**Trajectory and lineage.** Graph abstraction reconciling clustering with trajectory inference ([[wolf-2019-paga]]); atlas-scale trajectory inference ([[cao-2019-moca]]); phylogenies from CRISPR lineage recorders ([[jones-2020-cassiopeia]]); lineage from copy number under minimal event distance ([[wang-2021-medalt]]); lineage from endogenous mtDNA variants ([[ludwig-2019-mtdna-lineage-tracing]]).

**Regulatory network inference.** Element-to-gene linkage from co-accessibility ([[pliner-2018-cicero]]); networks used as simulation operators for in-silico perturbation ([[kamimoto-2023-celloracle]]); enhancer-driven regulons from joint accessibility and expression ([[bravo-2023-scenicplus]]).

## Cross-cutting tensions

- **Sparsity squares in two dimensions.** 5–10% linear genome coverage becomes 0.25–1% of possible contacts in a Hi-C matrix ([[zhou-2019-schicluster]]), which is the quantitative form of the *n*²-resolution rule ([[lieberman-aiden-2009-hic]]).
- **Coverage bias can dominate biological signal** in single-cell clustering, and is not removable by simply dropping the first principal component ([[zhou-2019-schicluster]]).
- **Imputation that enables clustering also suppresses the variability being measured** — an unresolved trade in both scHi-C imputation frameworks ([[zhou-2019-schicluster]], [[zhang-2022-higashi]]).
- **Duplicate-removal semantics depend on library chemistry**: coordinate-based deduplication is only valid when fragmentation precedes amplification ([[zahn-2017-dlp]], [[li-2009-samtools]]).
- **Compute cost is a real selection pressure**: 500,000 cells integrate in 7.2 GB ([[korsunsky-2019-harmony]]) while enhancer-GRN inference can require 461 GB ([[bravo-2023-scenicplus]]).

## Related

- [[3d-genome]] · [[single-cell-multiomics]] · [[cancer-clonal-evolution]] · [[scdna-seq]]

## Added 2026-08-13

The 2026-08-13 ingest adds a historical layer the corpus was missing: [[30-Concepts/single-cell-genome-assembly|single-cell genome assembly]] ([[10-Summaries/chitsaz-2011-velvet-sc]], [[10-Summaries/peng-2012-idba-ud]], [[10-Summaries/bankevich-2012-spades]]), where MDA's coverage pathology was first met with algorithms rather than better chemistry.

The transferable statistical lesson is the **abundance inversion**: under uneven coverage, incorrect *k*-mers in high-depth regions can outnumber correct *k*-mers in low-depth regions, so no global multiplicity threshold works ([[10-Summaries/peng-2012-idba-ud]]). The same inversion, in a different data type, is what single-cell variant callers negotiate as allelic imbalance ([[10-Summaries/dong-2017-sccaller]]; [[10-Summaries/luquette-2019-natcomm]]). (synthesis)

New tools this session: SCAN2 ([[10-Summaries/luquette-2021-scan2]]), SnapHiC ([[10-Summaries/yu-2021-snaphic]]), scGHOST ([[10-Summaries/xiong-2024-scghost]]), MINTsC ([[10-Summaries/park-2026-mintsc]]), dcHiC ([[10-Summaries/chakraborty-2022-dchic]]), ISON ([[10-Summaries/debnath-2026-ison]]).
