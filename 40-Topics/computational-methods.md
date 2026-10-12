---
type: topic
title: Computational Methods
aliases: [bioinformatics tooling, analysis pipelines, computational infrastructure]
tags: [pipelines, algorithms, tools, infrastructure]
created: 2026-08-10
updated: 2026-10-12
paper_section: ["4.2"]
---

# Computational Methods

> The tool layer of this wiki: the aligners, formats, callers, imputers, integrators and network-inference frameworks that turn raw single-cell and epigenomic sequencing into interpretable results. Assay pages describe what was measured; these describe what was done to it.

> [!abstract] 한눈에
> 같은 데이터라도 어떤 도구를 쓰느냐에 따라 결론이 달라진다. Hi-C pipeline 두 개는 같은 입력에서 0.83의 상관만 보이고, CUT&RUN에 ChIP-seq peak caller를 쓰면 발현되지 않는 인자에서도 peak가 수백 개 나온다 ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]; [[10-Summaries/meers-2019-seacr|SEACR]]). single-cell 데이터에서는 sparsity, coverage bias, imputation이 측정하려는 변이를 지우는 문제, 계산 비용이 도구 선택을 좌우한다 ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]; [[10-Summaries/bravo-2023-scenicplus|SCENIC+]]).

## Key points

- **Method choice is not neutral.** Seven TAD callers disagree on the same contact matrix ([[10-Summaries/kerpedjiev-2018-higlass|HiGlass]]), and two Hi-C pipelines given identical input produce maps correlating at 0.83, not 1.0 ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]).
- **Sparsity squares in two dimensions.** 5–10% linear genome coverage becomes 0.25–1% of possible contacts in a single-cell Hi-C matrix ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).
- **Imputation that enables clustering also suppresses the variability being measured**, an unresolved trade in both scHi-C imputation frameworks ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]; [[10-Summaries/zhang-2022-higashi|Higashi]]).
- **In phylogenetics, tree inference and error correction are the same problem**, reached independently in 2018 at the read level ([[10-Summaries/singer-2018-sciphi|SCIΦ]]) and the genotype-matrix level ([[10-Summaries/el-kebir-2018-sphyr|SPhyR]]).
- **Compute cost is a real selection pressure**: 500,000 cells integrate in 7.2 GB ([[10-Summaries/korsunsky-2019-harmony|Harmony]]) while enhancer-GRN inference can require 461 GB ([[10-Summaries/bravo-2023-scenicplus|SCENIC+]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/phylogenetic-inference|Phylogenetic inference]] — Reconstructing a cell-division tree from heritable markers, synthetic or natural.
> - `concept` [[30-Concepts/crispr-lineage-recording|CRISPR lineage recording]] — Synthetic recorders whose accumulated Cas9 edits encode a cell-division phylogeny.
> - `concept` [[30-Concepts/multimodal-integration-methods|Multimodal integration methods]] — Combining paired or unpaired single-cell modalities into one representation.
> - `concept` [[30-Concepts/reference-atlas-mapping|Reference atlas mapping]] — Placing query cells into an annotated reference and transferring labels or modalities.
> - `concept` [[30-Concepts/single-cell-genome-assembly|Single-cell genome assembly]] — De novo assembly from one amplified cell, with no reference genome.

## Why method choice matters

Method choice is not neutral. Seven TAD callers disagree on the same contact matrix ([[10-Summaries/kerpedjiev-2018-higlass|HiGlass]]); two Hi-C pipelines with identical input produce maps correlating at 0.83, not 1.0 ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]); a ChIP-seq peak caller run on CUT&RUN data emits up to ~900 peaks for a factor that is not expressed ([[10-Summaries/meers-2019-seacr|SEACR]]). Conclusions in this corpus are conditional on tooling, and this page exists so that dependency stays visible.

## Preprocessing, alignment and formats

| Tool | Year | Role | Note |
|---|---|---|---|
| [[10-Summaries/chen-2018-fastp\|fastp]] | 2018 | FASTQ preprocessing | QC, adapter and polyG trimming, UMI handling in a single pass ([[10-Summaries/chen-2018-fastp\|fastp]]) |
| [[10-Summaries/li-2009-bwa\|BWA]] | 2009 | Read alignment | BWT-based alignment ([[10-Summaries/li-2009-bwa\|BWA]]) |
| [[10-Summaries/li-2009-samtools\|SAMtools]] | 2009 | Format and toolkit | The SAM/BAM format that decoupled alignment from every downstream analysis ([[10-Summaries/li-2009-samtools\|SAMtools]]) |
| [[10-Summaries/zhang-2021-chromap\|Chromap]] | 2021 | Read alignment | Chromatin-optimized fast alignment ([[10-Summaries/zhang-2021-chromap\|Chromap]]) |

## Variant and structural-variant calling

| Tool | Year | Input | Approach | Note |
|---|---|---|---|---|
| [[10-Summaries/mckenna-2010-gatk\|GATK]] | 2010 | Bulk | Germline/somatic SNV calling infrastructure | ([[10-Summaries/mckenna-2010-gatk\|GATK]]) |
| [[10-Summaries/koboldt-2009-varscan\|VarScan]] | 2009 | Bulk | Aligner-independent heuristic SNP/indel caller (Perl/C) | ([[10-Summaries/koboldt-2009-varscan\|VarScan]]) |
| [[10-Summaries/cibulskis-2013-mutect\|MuTect]] | 2013 | Bulk tumour | Somatic SNV caller | Virtual-tumour benchmarking approach ([[10-Summaries/cibulskis-2013-mutect\|MuTect]]) |
| [[10-Summaries/chen-2009-breakdancer\|BreakDancer]] | 2009 | Bulk read pairs | Poisson/Fisher-pooled read-pair SV detection | Plus a KS-test small-indel module ([[10-Summaries/chen-2009-breakdancer\|BreakDancer]]) |
| [[10-Summaries/dong-2017-sccaller\|SCcaller]] | 2017 | Single-cell WGA | SNV calling under allelic imbalance | ([[10-Summaries/dong-2017-sccaller\|SCcaller]]) |
| [[10-Summaries/luquette-2019-natcomm\|SCAN-SNV]] | 2019 | Single-cell WGA | SNV calling under allelic imbalance | ([[10-Summaries/luquette-2019-natcomm\|SCAN-SNV]]) |
| [[10-Summaries/luquette-2022-neuron-scan2-indels\|SCAN2]] | 2022 | Single-cell WGA (PTA, MDA) | Somatic SNV and indel detection | ([[10-Summaries/luquette-2022-neuron-scan2-indels\|SCAN2]]) |
| [[10-Summaries/weber-2023-mosaicatcher-v2\|MosaiCatcher v2]] | 2023 | Strand-seq | Snakemake, FASTQ to haplotype-phased single-cell SV calls | Data-dependent checkpoints, ML-based library QC, normalization by library size, GC correction and VST; conda environments in a versioned Docker container, tested by CI ([[10-Summaries/weber-2023-mosaicatcher-v2\|MosaiCatcher v2]]) |

Independent comparisons such as the mosaic-variant benchmark ([[10-Summaries/ha-2023-natmethods|Ha 2023]]) deserve more weight than tool papers that benchmark themselves (synthesis).

## Copy-number calling and mutational processes

| Tool | Year | Input | Approach | Note |
|---|---|---|---|---|
| [[10-Summaries/bakker-2016-aneufinder\|AneuFinder]] | 2016 | scDNA-seq | HMM over mappability-variable bins | ([[10-Summaries/bakker-2016-aneufinder\|AneuFinder]]) |
| [[10-Summaries/garvin-2015-natmethods\|Ginkgo]] | 2015 | scDNA-seq | Circular binary segmentation | ([[10-Summaries/garvin-2015-natmethods\|Ginkgo]]) |
| [[10-Summaries/wang-2020-scope\|SCOPE]] | 2020 | scDNA-seq | Poisson latent-factor model | ([[10-Summaries/wang-2020-scope\|SCOPE]]) |
| [[10-Summaries/tickle-2019-infercnv\|inferCNV]] | 2019 | scRNA-seq | CNV inferred from transcriptomes | ([[10-Summaries/tickle-2019-infercnv\|inferCNV]]) |
| [[10-Summaries/gao-2021-copykat\|CopyKAT]] | 2021 | scRNA-seq | CNV inferred from transcriptomes | ([[10-Summaries/gao-2021-copykat\|CopyKAT]]) |
| [[10-Summaries/kuipers-2025-scicone\|SCICoNE]] | 2025 | Shallow scWGS | Dirichlet-multinomial MCMC over CNA trees | Cross-cell breakpoint detection ([[10-Summaries/kuipers-2025-scicone\|SCICoNE]]) |
| [[10-Summaries/zhao-2025-hiscanner\|HiScanner]] | 2025 | High-coverage scWGS | Multi-cell BIC segmentation (BICseq2); KS-test LOH-aware BAF | Allele-specific; bin size set from allelic-dropout size; ViScanner browser ([[10-Summaries/zhao-2025-hiscanner\|HiScanner]]) |
| [[10-Summaries/schneider-2024-scabsolute\|scAbsolute]] | 2024 | Shallow scDNA-seq | Constrained DPGMM ploidy fitting plus read-density correction | Replication-time cycling activity for S-phase detection ([[10-Summaries/schneider-2024-scabsolute\|scAbsolute]]) |
| [[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]] | 2025 | 0.01×–0.1× tagmentation scWGS | Snakemake; high-resolution mpcf/LLR segmentation; absolute ploidy from fragment overlap; per-clone haplotyping with no reference sample, then MEDICC2 | Scored above scAbsolute, Alleloscope and CHISEL on one B-ALL ([[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]]) |
| [[10-Summaries/ivanovic-2025-cnrein\|CNRein]] | 2025 | scDNA-seq | CNN generative model of CNA trajectories trained by policy-gradient RL | Regularizes haplotype-specific copy-number calls; PyTorch, CPU-only ([[10-Summaries/ivanovic-2025-cnrein\|CNRein]]) |

Mutational-process decomposition of passenger mutations comes from mutational signatures ([[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]).

## Single-cell genome assembly

[[30-Concepts/single-cell-genome-assembly|Single-cell genome assembly]] is the historical layer where MDA's coverage pathology was first met with algorithms rather than better chemistry ([[10-Summaries/chitsaz-2011-velvet-sc|Velvet-SC]]; [[10-Summaries/peng-2012-idba-ud|IDBA-UD]]; [[10-Summaries/bankevich-2012-spades|SPAdes]]).

- **Abundance inversion.** Under uneven coverage, incorrect *k*-mers in high-depth regions can outnumber correct *k*-mers in low-depth regions, so no global multiplicity threshold works ([[10-Summaries/peng-2012-idba-ud|IDBA-UD]]).
- **The same inversion in another data type** is what single-cell variant callers negotiate as allelic imbalance ([[10-Summaries/dong-2017-sccaller|SCcaller]]; [[10-Summaries/luquette-2019-natcomm|SCAN-SNV]]). (synthesis)

## Chromatin, peaks and methylation

| Tool | Year | Data | Approach | Note |
|---|---|---|---|---|
| [[10-Summaries/zhang-2008-macs\|MACS]] | 2008 | ChIP-seq | Empirical fragment-shift modelling with dynamic local background | ([[10-Summaries/zhang-2008-macs\|MACS]]) |
| [[10-Summaries/meers-2019-seacr\|SEACR]] | 2019 | CUT&RUN | Model-free thresholding for low-background in-situ assays | ([[10-Summaries/meers-2019-seacr\|SEACR]]) |
| [[10-Summaries/heinz-2010-homer\|HOMER]] | 2010 | Peaks | Motif and peak toolkit | ([[10-Summaries/heinz-2010-homer\|HOMER]]) |
| [[10-Summaries/mclean-2010-great\|GREAT]] | 2010 | Regions | Region-to-gene functional annotation | ([[10-Summaries/mclean-2010-great\|GREAT]]) |
| [[10-Summaries/hu-2026-patty\|PATTY]] | 2026 | CUT&Tag (bulk and single-cell) | ML correction of Tn5 open-chromatin bias | ([[10-Summaries/hu-2026-patty\|PATTY]]) |
| [[10-Summaries/tang-2024-sccase\|scCASE]] | 2024 | scATAC-seq | Interpretable NMF-based imputation with a learned cell-similarity matrix | ([[10-Summaries/tang-2024-sccase\|scCASE]]) |
| [[10-Summaries/kremer-2024-methscan\|MethSCAn]] | 2024 | Single-cell bisulfite | Single-cell methylation segmentation | ([[10-Summaries/kremer-2024-methscan\|MethSCAn]]) |
| [[10-Summaries/farlik-2015-scwgbs\|Farlik 2015]] | 2015 | scWGBS | Region-set residual aggregation for sparse single-cell methylomes | ([[10-Summaries/farlik-2015-scwgbs\|Farlik 2015]]) |
| [[10-Summaries/zhou-2024-scdmv\|scDMV]] | 2024 | Single-cell methylation | Single-cell DMR testing | ([[10-Summaries/zhou-2024-scdmv\|scDMV]]) |

Two benchmarks cover this layer:

- **scDNAm imputation.** Random-split evaluation leaks information, and accuracy is limited by entropy ([[10-Summaries/liang-2026-scmeth-imputation-benchmark|Liang 2026]]).
- **Single-cell histone PTM pipelines.** A >10,000-run benchmark of matrix construction, feature/cell selection and embedding ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).

## Hi-C pipelines, storage and single-cell 3D genome

| Tool | Year | Role | Note |
|---|---|---|---|
| [[10-Summaries/servant-2015-hicpro\|HiC-Pro]] | 2015 | Reads to normalized matrix | ICE and allele-specific modes ([[10-Summaries/servant-2015-hicpro\|HiC-Pro]]) |
| [[10-Summaries/durand-2016-juicer\|Juicer]] | 2016 | Processing toolchain | ([[10-Summaries/durand-2016-juicer\|Juicer]]) |
| [[10-Summaries/abdennur-2020-cooler\|cooler]] | 2020 | Storage format | Sparse HDF5 format adopted by 4D Nucleome ([[10-Summaries/abdennur-2020-cooler\|cooler]]) |
| [[10-Summaries/kerpedjiev-2018-higlass\|HiGlass]] | 2018 | Visualization | Composable linked-view browsing ([[10-Summaries/kerpedjiev-2018-higlass\|HiGlass]]) |
| [[10-Summaries/zhou-2019-schicluster\|scHiCluster]] | 2019 | scHi-C imputation | Convolution plus random walk with top-20% selection to defeat coverage bias ([[10-Summaries/zhou-2019-schicluster\|scHiCluster]]) |
| [[10-Summaries/zhang-2022-higashi\|Higashi]] | 2022 | scHi-C imputation | Hypergraph representation learning that borrows across cells and integrates co-assayed modalities ([[10-Summaries/zhang-2022-higashi\|Higashi]]) |
| [[10-Summaries/zheng-2022-bandnorm-scvi-3d\|BandNorm / scVI-3D]] | 2022 | scHi-C normalization and de-noising | BandNorm normalization, ZINB-VAE de-noising and an 8-method benchmark ([[10-Summaries/zheng-2022-bandnorm-scvi-3d\|BandNorm / scVI-3D]]) |
| [[10-Summaries/yu-2021-snaphic\|SnapHiC]] | 2021 | scHi-C loop calling | ([[10-Summaries/yu-2021-snaphic\|SnapHiC]]) |
| [[10-Summaries/xiong-2024-scghost\|scGHOST]] | 2024 | scHi-C subcompartments | ([[10-Summaries/xiong-2024-scghost\|scGHOST]]) |
| [[10-Summaries/peng-2026-scdiagram\|scDIAGRAM]] | 2026 | scHi-C compartments | Change-point plus normalized-cut compartment calling ([[10-Summaries/peng-2026-scdiagram\|scDIAGRAM]]) |
| [[10-Summaries/park-2026-mintsc\|MINTsC]] | 2026 | Multi-way interactions from single cells | ([[10-Summaries/park-2026-mintsc\|MINTsC]]) |
| [[10-Summaries/chakraborty-2022-dchic\|dcHiC]] | 2022 | Differential compartments | Across multiple Hi-C datasets ([[10-Summaries/chakraborty-2022-dchic\|dcHiC]]) |

A catalogue of scHi-C software finds single-tool gaps for loops, differential contacts, pseudotime and simulation ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]).

## Embedding, clustering and integration

See [[30-Concepts/multimodal-integration-methods]] and [[30-Concepts/reference-atlas-mapping]]. The integration field starts on 2 April 2018 with two papers in the same journal issue ([[10-Summaries/haghverdi-2018-mnn|MNN]]; [[10-Summaries/butler-2018-seurat-cca|Seurat CCA]]).

| Tool | Year | Approach | Note |
|---|---|---|---|
| [[10-Summaries/mcinnes-2018-umap\|UMAP]] | 2018 | Dimensionality reduction | ([[10-Summaries/mcinnes-2018-umap\|UMAP]]) |
| [[10-Summaries/traag-2019-leiden\|Leiden]] | 2019 | Community detection | Connectivity guarantees ([[10-Summaries/traag-2019-leiden\|Leiden]]) |
| [[10-Summaries/haghverdi-2018-mnn\|MNN]] | 2018 | Batch correction | ([[10-Summaries/haghverdi-2018-mnn\|MNN]]) |
| [[10-Summaries/butler-2018-seurat-cca\|Seurat CCA]] | 2018 | Cross-condition integration | ([[10-Summaries/butler-2018-seurat-cca\|Seurat CCA]]) |
| [[10-Summaries/korsunsky-2019-harmony\|Harmony]] | 2019 | Batch correction in embedding space across multiple covariates | 500,000 cells in 7.2 GB ([[10-Summaries/korsunsky-2019-harmony\|Harmony]]) |
| [[10-Summaries/welch-2019-liger\|LIGER]] | 2019 | Factorization into shared and dataset-specific factors | ([[10-Summaries/welch-2019-liger\|LIGER]]) |
| [[10-Summaries/argelaguet-2018-mofa\|MOFA]] | 2018 | Sparse Bayesian group factor analysis | Native handling of missing assays and non-Gaussian data; origin of the MOFA/MOFA+ family ([[10-Summaries/argelaguet-2018-mofa\|MOFA]]) |
| [[10-Summaries/hao-2024-seurat-v5\|Seurat v5]] | 2024 | Anchor- and bridge-based integration | ([[10-Summaries/hao-2024-seurat-v5\|Seurat v5]]) |
| [[10-Summaries/debnath-2026-ison\|ISON]] | 2026 | Spatial chromatin accessibility inferred by integrating spatial transcriptomics | ([[10-Summaries/debnath-2026-ison\|ISON]]) |
| [[10-Summaries/fan-2026-gfetm\|GFETM]] | 2026 | Embedded topic model jointly trained with a genome foundation model | Transferable, sequence-informed scATAC-seq modelling; parity with scBasset on clustering, gains on unseen cells/peaks and transfer (bioRxiv v3 full text) ([[10-Summaries/fan-2026-gfetm\|GFETM]]) |

- **Conceptual taxonomy** of integration principles and challenges ([[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]).
- **Independent benchmark** of multi-omics integration across scRNA and scATAC ([[10-Summaries/xiao-2024-multiomics-benchmark|Xiao 2024]]).
- **Sequence and foundation models** have their own hub, [[40-Topics/sequence-models-and-foundation-models]], covering 64 sequence-to-function models, DNA language models and single-cell epigenome/multimodal foundation models; GFETM is one of the first to put a DNA language model inside a scATAC model ([[10-Summaries/fan-2026-gfetm|GFETM]]).

## Trajectory, lineage and phylogenetics

See [[30-Concepts/phylogenetic-inference]] and [[30-Concepts/crispr-lineage-recording]].

| Tool | Year | Input | Approach | Note |
|---|---|---|---|---|
| [[10-Summaries/wolf-2019-paga\|PAGA]] | 2019 | scRNA-seq | Graph abstraction | Reconciles clustering with trajectory inference ([[10-Summaries/wolf-2019-paga\|PAGA]]) |
| [[10-Summaries/cao-2019-moca\|MOCA]] | 2019 | scRNA-seq | Atlas-scale trajectory inference | ([[10-Summaries/cao-2019-moca\|MOCA]]) |
| [[10-Summaries/jones-2020-cassiopeia\|Cassiopeia]] | 2020 | CRISPR lineage recorders | Phylogeny reconstruction | ([[10-Summaries/jones-2020-cassiopeia\|Cassiopeia]]) |
| [[10-Summaries/gong-2022-dclear\|DCLEAR]] | 2022 | CRISPR barcodes | Distance-based reconstruction | Allen Institute DREAM Challenge ([[10-Summaries/gong-2022-dclear\|DCLEAR]]) |
| [[10-Summaries/chu-2025-laml\|LAML]] | 2025 | Lineage data with mixed-type missing data | Maximum likelihood, time-scaled trees | Imputation inside the objective; heritable missing data treated as signal ([[10-Summaries/chu-2025-laml\|LAML]]) |
| [[10-Summaries/ludwig-2019-mtdna-lineage-tracing\|Ludwig 2019]] | 2019 | Endogenous mtDNA variants | Lineage tracing | ([[10-Summaries/ludwig-2019-mtdna-lineage-tracing\|Ludwig 2019]]) |
| [[10-Summaries/wang-2021-medalt\|MEDALT]] | 2021 | Copy number | Minimal event distance | ([[10-Summaries/wang-2021-medalt\|MEDALT]]) |
| [[10-Summaries/singer-2018-sciphi\|SCIΦ]] | 2018 | Reads | Joint mutation calling and tree | Error correction at the read level ([[10-Summaries/singer-2018-sciphi\|SCIΦ]]) |
| [[10-Summaries/el-kebir-2018-sphyr\|SPhyR]] | 2018 | Genotype matrix | Tree under loss and errors | Error correction at the genotype-matrix level ([[10-Summaries/el-kebir-2018-sphyr\|SPhyR]]) |
| [[10-Summaries/foroughmand-2022-scelestial\|Scelestial]] | 2022 | SNV | Lineage tree inference | Imputation inside the objective ([[10-Summaries/foroughmand-2022-scelestial\|Scelestial]]) |
| [[10-Summaries/kang-2022-sieve\|SIEVE]] | 2022 | scDNA-seq | BEAST 2 statistical phylogenetics | ([[10-Summaries/kang-2022-sieve\|SIEVE]]) |
| [[10-Summaries/kozlov-2022-cellphy\|CellPhy]] | 2022 | SNV genotypes | GT16 genotype substitution model + scWGA error model in RAxML-NG | ([[10-Summaries/kozlov-2022-cellphy\|CellPhy]]) |

The transferable ideas from these phylogenetics papers (synthesis):

- Tree inference and error correction are the same problem, reached independently in 2018 at the read level ([[10-Summaries/singer-2018-sciphi|SCIΦ]]) and the genotype-matrix level ([[10-Summaries/el-kebir-2018-sphyr|SPhyR]]).
- Imputation belongs inside the objective rather than before it ([[10-Summaries/foroughmand-2022-scelestial|Scelestial]]; [[10-Summaries/chu-2025-laml|LAML]]).
- Missing data can carry signal when it is heritable ([[10-Summaries/chu-2025-laml|LAML]]).

## Regulatory network inference

| Tool | Year | Input | Approach | Note |
|---|---|---|---|---|
| [[10-Summaries/pliner-2018-cicero\|Cicero]] | 2018 | scATAC-seq | Element-to-gene linkage from co-accessibility | ([[10-Summaries/pliner-2018-cicero\|Cicero]]) |
| [[10-Summaries/kamimoto-2023-celloracle\|CellOracle]] | 2023 | — | Networks used as simulation operators | In-silico perturbation ([[10-Summaries/kamimoto-2023-celloracle\|CellOracle]]) |
| [[10-Summaries/bravo-2023-scenicplus\|SCENIC+]] | 2023 | Joint accessibility and expression | Enhancer-driven regulons | Can require 461 GB ([[10-Summaries/bravo-2023-scenicplus\|SCENIC+]]) |
| [[10-Summaries/yuan-2024-linger\|LINGER]] | 2024 | Single-cell multiome | GRN inference | Effective sample size is far below the cell count ([[10-Summaries/yuan-2024-linger\|LINGER]]) |

## Cross-cutting tensions

- **Sparsity squares in two dimensions.** 5–10% linear genome coverage becomes 0.25–1% of possible contacts in a Hi-C matrix ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]), which is the quantitative form of the *n*²-resolution rule ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]).
- **Coverage bias can dominate biological signal** in single-cell clustering, and is not removable by simply dropping the first principal component ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).
- **Imputation that enables clustering also suppresses the variability being measured**, an unresolved trade in both scHi-C imputation frameworks ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]; [[10-Summaries/zhang-2022-higashi|Higashi]]).
- **Duplicate-removal semantics depend on library chemistry**: coordinate-based deduplication is only valid when fragmentation precedes amplification ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]; [[10-Summaries/li-2009-samtools|SAMtools]]).
- **Compute cost is a real selection pressure**: 500,000 cells integrate in 7.2 GB ([[10-Summaries/korsunsky-2019-harmony|Harmony]]) while enhancer-GRN inference can require 461 GB ([[10-Summaries/bravo-2023-scenicplus|SCENIC+]]).
- **Most single cells are not independent**, so the effective sample size is far below the cell count ([[10-Summaries/yuan-2024-linger|LINGER]]); this applies to every method that treats cells as replicates, including the 3D-genome callers SnapHiC and MINTsC ([[10-Summaries/yu-2021-snaphic|SnapHiC]]; [[10-Summaries/park-2026-mintsc|MINTsC]]). (synthesis)
- **Nearly every tool paper here benchmarks itself.** The exceptions worth weighting more heavily are the Allen Institute DREAM Challenge ([[10-Summaries/gong-2022-dclear|DCLEAR]]) and independent comparisons ([[10-Summaries/ha-2023-natmethods|Ha 2023]]; [[10-Summaries/xiao-2024-multiomics-benchmark|Xiao 2024]]). (synthesis)

## Reviews and agendas

- [[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]] — community agenda of 11 single-cell data-science challenges, including scDNA variant calling, phylogenetic scaling and benchmarking/simulation gaps.
- [[10-Summaries/dautle-2025-schic-review|Dautle 2025]] — catalogue of scHi-C software and its single-tool gaps.
- [[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]] — computational principles and challenges of single-cell data integration.

## Open questions

- How much biological variability do scHi-C imputation frameworks remove while making clustering possible ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]; [[10-Summaries/zhang-2022-higashi|Higashi]])?
- Do single-cell callers that treat cells as independent replicates (e.g. SnapHiC, MINTsC) overstate significance, given that the effective sample size is far below the cell count ([[10-Summaries/yuan-2024-linger|LINGER]]; [[10-Summaries/yu-2021-snaphic|SnapHiC]]; [[10-Summaries/park-2026-mintsc|MINTsC]])? (synthesis)
- Most tool papers benchmark themselves; which tools hold up in independent comparisons ([[10-Summaries/gong-2022-dclear|DCLEAR]]; [[10-Summaries/ha-2023-natmethods|Ha 2023]]; [[10-Summaries/xiao-2024-multiomics-benchmark|Xiao 2024]])? (synthesis)
- Since seven TAD callers disagree on one matrix and two Hi-C pipelines correlate at 0.83, which downstream conclusions survive a change of tool ([[10-Summaries/kerpedjiev-2018-higlass|HiGlass]]; [[10-Summaries/servant-2015-hicpro|HiC-Pro]])? (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Technologies that interrogate the DNA of single cells, by amplification or by single-molecule reads.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Compartments, TADs and loops of DNA in the nucleus.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Measuring two or more modalities in the same cell.
> - `hub` [[40-Topics/cancer-clonal-evolution|Cancer clonal evolution]] — Somatic mutation and clonal selection reconstructed as tumour phylogenies.
> - `hub` [[40-Topics/sequence-models-and-foundation-models|Sequence models and foundation models]] — Sequence-to-function models, DNA language models and single-cell foundation models.

## All sources on this page

> [!info]- 82 summaries cited here
> - [[10-Summaries/abdennur-2020-cooler|Abdennur & Mirny 2020]]
> - [[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]
> - [[10-Summaries/argelaguet-2018-mofa|Argelaguet 2018]]
> - [[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]
> - [[10-Summaries/bakker-2016-aneufinder|Bakker 2016]]
> - [[10-Summaries/bankevich-2012-spades|Bankevich 2012]]
> - [[10-Summaries/bravo-2023-scenicplus|Bravo 2023]]
> - [[10-Summaries/butler-2018-seurat-cca|Butler 2018]]
> - [[10-Summaries/cao-2019-moca|Cao 2019]]
> - [[10-Summaries/chakraborty-2022-dchic|Chakraborty 2022]]
> - [[10-Summaries/chen-2009-breakdancer|Chen 2009]]
> - [[10-Summaries/chen-2018-fastp|Chen 2018]]
> - [[10-Summaries/chitsaz-2011-velvet-sc|Chitsaz 2011]]
> - [[10-Summaries/chu-2025-laml|Chu 2025]]
> - [[10-Summaries/cibulskis-2013-mutect|Cibulskis 2013]]
> - [[10-Summaries/dautle-2025-schic-review|Dautle 2025]]
> - [[10-Summaries/debnath-2026-ison|Debnath 2026]]
> - [[10-Summaries/dong-2017-sccaller|Dong 2017]]
> - [[10-Summaries/durand-2016-juicer|Durand 2016]]
> - [[10-Summaries/el-kebir-2018-sphyr|El-Kebir 2018]]
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
> - [[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]
> - [[10-Summaries/foroughmand-2022-scelestial|Foroughmand-Araabi 2022]]
> - [[10-Summaries/gao-2021-copykat|Gao 2021]]
> - [[10-Summaries/garvin-2015-natmethods|Garvin 2015]]
> - [[10-Summaries/gong-2022-dclear|Gong 2022]]
> - [[10-Summaries/ha-2023-natmethods|Ha 2023]]
> - [[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]
> - [[10-Summaries/hao-2024-seurat-v5|Hao 2024]]
> - [[10-Summaries/heinz-2010-homer|Heinz 2010]]
> - [[10-Summaries/hu-2026-patty|Hu 2026]]
> - [[10-Summaries/ivanovic-2025-cnrein|Ivanovic & El-Kebir 2025]]
> - [[10-Summaries/jones-2020-cassiopeia|Jones 2020]]
> - [[10-Summaries/kamimoto-2023-celloracle|Kamimoto 2023]]
> - [[10-Summaries/kang-2022-sieve|Kang 2022]]
> - [[10-Summaries/kerpedjiev-2018-higlass|Kerpedjiev 2018]]
> - [[10-Summaries/koboldt-2009-varscan|Koboldt 2009]]
> - [[10-Summaries/kolbeinsdottir-2025-ascent|Kolbeinsdottir 2025]]
> - [[10-Summaries/korsunsky-2019-harmony|Korsunsky 2019]]
> - [[10-Summaries/kozlov-2022-cellphy|Kozlov 2022]]
> - [[10-Summaries/kremer-2024-methscan|Kremer 2024]]
> - [[10-Summaries/kuipers-2025-scicone|Kuipers 2025]]
> - [[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]
> - [[10-Summaries/li-2009-bwa|Li & Durbin 2009]]
> - [[10-Summaries/li-2009-samtools|Li 2009]]
> - [[10-Summaries/liang-2026-scmeth-imputation-benchmark|Liang 2026]]
> - [[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]
> - [[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]
> - [[10-Summaries/luquette-2019-natcomm|Luquette 2019]]
> - [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]
> - [[10-Summaries/mcinnes-2018-umap|McInnes 2018]]
> - [[10-Summaries/mckenna-2010-gatk|McKenna 2010]]
> - [[10-Summaries/mclean-2010-great|McLean 2010]]
> - [[10-Summaries/meers-2019-seacr|Meers 2019]]
> - [[10-Summaries/park-2026-mintsc|Park 2026]]
> - [[10-Summaries/peng-2012-idba-ud|Peng 2012]]
> - [[10-Summaries/peng-2026-scdiagram|Peng 2026]]
> - [[10-Summaries/pliner-2018-cicero|Pliner 2018]]
> - [[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]
> - [[10-Summaries/schneider-2024-scabsolute|Schneider 2024]]
> - [[10-Summaries/servant-2015-hicpro|Servant 2015]]
> - [[10-Summaries/singer-2018-sciphi|Singer 2018]]
> - [[10-Summaries/tang-2024-sccase|Tang 2024]]
> - [[10-Summaries/tickle-2019-infercnv|Tickle 2019]]
> - [[10-Summaries/traag-2019-leiden|Traag 2019]]
> - [[10-Summaries/wang-2020-scope|Wang 2020]]
> - [[10-Summaries/wang-2021-medalt|Wang 2021]]
> - [[10-Summaries/weber-2023-mosaicatcher-v2|Weber 2023]]
> - [[10-Summaries/welch-2019-liger|Welch 2019]]
> - [[10-Summaries/wolf-2019-paga|Wolf 2019]]
> - [[10-Summaries/xiao-2024-multiomics-benchmark|Xiao 2024]]
> - [[10-Summaries/xiong-2024-scghost|Xiong 2024]]
> - [[10-Summaries/yu-2021-snaphic|Yu 2021]]
> - [[10-Summaries/yuan-2024-linger|Yuan & Duren 2024]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
> - [[10-Summaries/zhang-2008-macs|Zhang 2008]]
> - [[10-Summaries/zhang-2021-chromap|Zhang 2021]]
> - [[10-Summaries/zhang-2022-higashi|Zhang 2022]]
> - [[10-Summaries/zhao-2025-hiscanner|Zhao 2025]]
> - [[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]
> - [[10-Summaries/zhou-2019-schicluster|Zhou 2019]]
> - [[10-Summaries/zhou-2024-scdmv|Zhou 2024]]
