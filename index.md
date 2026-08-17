---
title: LLM Wiki — scDNA-seq & Single-Cell Epigenomics
description: A living knowledge base on single-cell DNA sequencing, somatic mosaicism, and adjacent epigenomics.
updated: 2026-08-14
---

# LLM Wiki

A living knowledge base on **single-cell DNA sequencing**, **somatic mosaicism**, and **single-cell epigenomics** — built and maintained with the help of an LLM, following [Andrej Karpathy's LLM Wiki pattern](10-Summaries/example-llm-wiki).

> This wiki synthesizes ~296 papers spanning scDNA-seq methods, chromatin profiling, DNA methylation, multi-omics assays, and computational tools. Start from a topic below, or browse the full catalog.

The central motivation: there is no DNA-centric locus-state framework that jointly interprets mutation + epigenome + RNA at single-cell scale. The wiki tracks the methods that get us closer to one — see [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|the synthesis gap note]] for the framing.

---

## Core Topics

### Single-Cell DNA Sequencing

The foundation: how to sequence a genome from one cell. Covers whole-genome amplification chemistries (MDA → MALBAC → LIANTI → **PTA**), variant calling, and error correction.

**Start here →** [[40-Topics/scdna-seq]] · [[30-Concepts/scwga]] · [[30-Concepts/pta]]
**Key review →** [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao et al. 2025 (NRG)]]
**Foundational →** [[10-Summaries/gawad-2016-scgenome-review|Gawad & Quake 2016]] · [[10-Summaries/dean-2002-mda|Dean 2002 (MDA founding paper)]] · [[10-Summaries/telenius-1992-dop-pcr|Telenius 1992 (DOP-PCR)]]
**Amplification-free →** [[10-Summaries/laks-2019-dlp-plus|Laks 2019 (DLP+)]] · **Bulk baseline →** [[10-Summaries/mckenna-2010-gatk|McKenna 2010 (GATK)]]
**WGA benchmarks →** [[10-Summaries/hou-2015-wga-comparison|Hou 2015 (7 kits)]] · [[10-Summaries/huang-2015-scwga-review|Huang/Xie 2015 (8-axis framework)]] · [[30-Concepts/scwga-chemistries]]
**Input-copy lever →** [[10-Summaries/wang-2014-nuc-seq|Wang 2014 (nuc-seq, G2/M nuclei)]] · **Targeted at scale →** [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014 (1,479 ALL cells)]]
**Assembly →** [[30-Concepts/single-cell-genome-assembly]] · [[10-Summaries/chitsaz-2011-velvet-sc|Velvet-SC]] · [[10-Summaries/peng-2012-idba-ud|IDBA-UD]] · [[10-Summaries/bankevich-2012-spades|SPAdes]]

---

### Somatic Mosaicism & Lineage Tracing

Post-zygotic mutations as both disease drivers and natural lineage barcodes. From brain mosaicism to clonal hematopoiesis, from Peto's paradox to aging.

**Start here →** [[40-Topics/somatic-mosaicism]] · [[30-Concepts/lineage-tracing]] · [[40-Topics/clonal-hematopoiesis]] · [[40-Topics/single-cell-lineage-tracing]]
**Key papers →** [[10-Summaries/lodato-2015-science|Lodato 2015]] · [[10-Summaries/coorens-2021-nature|Coorens 2021]] · [[10-Summaries/cagan-2022-nature|Cagan 2022]]
**Lineage-tracing reviews (NRG 2026) →** [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli & Parreno (technologies)]] · [[10-Summaries/wang-2026-multimodal-lineage-computational|Wang, He & Hu (computational)]]
**Tree inference →** [[30-Concepts/phylogenetic-inference]] · [[10-Summaries/ross-2016-onconem|OncoNEM]] · [[10-Summaries/el-kebir-2018-sphyr|SPhyR]] · [[10-Summaries/singer-2018-sciphi|SCIΦ]] · [[10-Summaries/foroughmand-2022-scelestial|Scelestial]]
**CRISPR recorders →** [[10-Summaries/gong-2022-dclear|DCLEAR]] · [[10-Summaries/sashittal-2023-startle|Startle]] · [[10-Summaries/chu-2025-laml|LAML (time-resolved)]] · [[10-Summaries/seidel-2026-sciphy|SciPhy]]
**Endogenous clocks →** [[10-Summaries/kwok-2022-mquad|MQuad (mtDNA)]] · [[10-Summaries/shahryary-2020-alphabeta|AlphaBeta]] · [[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]]
**Tracing concepts →** [[30-Concepts/crispr-lineage-recording]] · [[30-Concepts/phylogenetic-inference]] · [[30-Concepts/mitochondrial-lineage-tracing]] · [[30-Concepts/methylation-clones-epimutation]]
**Brain focus →** [[10-Summaries/bae-2017-pregastrulation-mutations|Bae 2018]] · [[10-Summaries/taejeong-2022-science|Bae 2022]] · [[10-Summaries/miller-2022-nature|Miller 2022 (AD)]]
**Reviews →** [[10-Summaries/forsberg-2017-mosaicism-review|Forsberg/Dumanski 2017 NRG]] · [[10-Summaries/hilal-2026-cardiac-somatic-review|Hilal 2026 (cardiac)]] · [[10-Summaries/hsieh-2026-scmtmpm-scwmss|Hsieh 2026 (mtDNA burden metrics)]]
**Stem cell aging →** [[10-Summaries/kapadia-2024-stem-cell-aging|Kapadia & Goodell 2024]]
**Rate revisions →** [[10-Summaries/luquette-2021-scan2|SCAN2 (Luquette 2021) — 15 SNVs/yr + first indel rate]]
**Upstream of mutation →** [[30-Concepts/hidef-seq]] · [[10-Summaries/liu-2024-hidef-seq|HiDEF-seq (Liu 2024) — single-strand mismatch & damage signatures]]

---

### Chromatin Accessibility (scATAC-seq)

Measuring open chromatin at single-cell resolution. Includes founding methods, computational tools, and histone modification profiling.

**Start here →** [[30-Concepts/scatac-seq]] · [[30-Concepts/chromatin-accessibility]] · [[30-Concepts/cut-and-tag]]
**Founding methods →** [[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]] · [[10-Summaries/cusanovich-2015-sciatac|Cusanovich 2015 (sci-ATAC)]]
**Tools →** [[30-Concepts/chromvar]] · [[30-Concepts/cistopic]] · [[30-Concepts/snapatac]] · [[10-Summaries/granja-2021-archr|ArchR]]
**Imputation / denoising →** [[30-Concepts/scatac-imputation]] · [[10-Summaries/li-2021-scopen|scOpen (NMF)]] · [[10-Summaries/xiong-2019-scale|SCALE (VAE+GMM)]]
**Enhancer state →** [[10-Summaries/creyghton-2010-h3k27ac-enhancers|Creyghton 2010 (H3K27ac active/poised partition)]] · [[10-Summaries/heinz-2010-homer|Heinz 2010 (priming + HOMER)]] · [[30-Concepts/enhancer-states]]
**Reference & tooling →** [[10-Summaries/roadmap-2015-111-epigenomes|Roadmap 2015 (127 epigenomes)]] · [[10-Summaries/mclean-2010-great|GREAT]] · [[10-Summaries/zhang-2021-chromap|Chromap]] · [[10-Summaries/traag-2019-leiden|Leiden]] · [[10-Summaries/mcinnes-2018-umap|UMAP]]

---

### DNA Methylation

From bisulfite sequencing to single-cell methylomes, 5hmC detection, and methylation-based lineage tracing (EPI-Clone, MethylTree).

**Start here →** [[40-Topics/dna-methylation]] · [[30-Concepts/bisulfite-sequencing]] · [[30-Concepts/scbs-seq]]
**Function & 5hmC →** [[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012 (context-dependence)]] · [[10-Summaries/tahiliani-2009-tet1-5hmc|Tahiliani 2009 (5hmC)]] · [[10-Summaries/chen-2025-sctaps-sccaps-plus|scTAPS/scCAPS+]] · [[10-Summaries/kremer-2024-methscan|MethSCAn]]
**Foundational →** [[10-Summaries/smallwood-2014-natmethods|Smallwood 2014 (scBS-seq)]] · [[10-Summaries/schubeler-2015-methylation-review|Schübeler 2015]]
**Lineage tracing →** [[10-Summaries/scherer-2025-nature|EPI-Clone (Scherer 2025)]] · [[10-Summaries/chen-2025-methyltree|MethylTree (Chen 2025)]]
**Cell typing by mCH →** [[10-Summaries/luo-2017-snmc-seq|Luo 2017 (snmC-seq)]] · [[10-Summaries/luo-2018-snmc-seq2|snmC-seq2]]
**Protocols →** [[10-Summaries/clark-2017-scbs-seq-protocol|scBS-seq / PBAT (~50% CpG)]] · [[10-Summaries/guo-2015-scrrbs-protocol|scRRBS one-tube (~70% CGIs)]]
**Throughput →** [[10-Summaries/mulqueen-2018-sci-met|sci-MET (combinatorial indexing)]] · [[10-Summaries/zhang-2023-drop-bs|Drop-BS (droplets, 10k cells)]]

---

### Single-Cell Transcriptomics (scRNA-seq foundations)

The transcriptomic axis underlying every multi-omics method. Why bulk RNA-seq averages away cell-type biology, and how scRNA-seq recovers it.

**Start here →** [[30-Concepts/scrna-seq]] · [[30-Concepts/drop-seq]] · [[30-Concepts/umi-molecular-barcoding]]
**Founding →** [[10-Summaries/tang-2009-scrna-seq|Tang 2009 (first scRNA-seq)]] · [[10-Summaries/macosko-2015-drop-seq|Drop-seq (Macosko 2015)]]
**Benchmark →** [[10-Summaries/svensson-2017-power-analysis|Svensson 2017 power analysis]]

---

### Multi-Omics Joint Assays

Methods that read two or more modalities from the same cell: genotype + transcriptome (GoT), genotype + chromatin (GoT-ChA), triple-omics, and beyond.

**Start here →** [[40-Topics/single-cell-multiomics]] · [[30-Concepts/got]] · [[30-Concepts/got-cha]]
**GoT family →** [[10-Summaries/nam-2019-got|Nam 2019]] · [[10-Summaries/izzo-2024-got-cha|Izzo 2024]] · [[10-Summaries/cortes-lopez-2023-cellstemcell|GoT-Splice]] · [[10-Summaries/chi-2026-dd-seq|D&D-GoT-ChA (Chi 2026)]]
**DNA + Epigenome →** [[10-Summaries/swanson-2025-daf-seq|DAF-seq]] · [[10-Summaries/kriz-2025-duplex-multiome|Duplex-Multiome]]
**Genotype + TF binding →** [[30-Concepts/dd-seq]] · [[10-Summaries/chi-2026-dd-seq|D&D-seq (Chi 2026, DNA–protein interaction axis)]]
**Scalable DNA + RNA →** [[30-Concepts/defnd-seq]] · [[10-Summaries/olsen-2025-defnd-seq|DEFND-seq (whole-genome)]] · [[30-Concepts/sdr-seq]] · [[10-Summaries/lindenhofer-2025-sdr-seq|SDR-seq (targeted, low ADO)]] · [[30-Concepts/resolveome]] · [[10-Summaries/marks-2023-resolveome|ResolveOME (PTA genome + RNA)]]
**Integration origins →** [[10-Summaries/haghverdi-2018-mnn|MNN]] · [[10-Summaries/butler-2018-seurat-cca|Seurat CCA]] (same journal issue, 2 Apr 2018) · [[30-Concepts/multimodal-integration-methods]]
**Paired-modality →** [[10-Summaries/hao-2021-seurat-wnn|WNN (Seurat v4)]] · [[10-Summaries/gayoso-2021-totalvi|totalVI]] · [[10-Summaries/lakkis-2022-scipenn|sciPENN]]
**Reference mapping →** [[30-Concepts/reference-atlas-mapping]] · [[10-Summaries/kang-2021-symphony|Symphony]] · [[10-Summaries/song-2021-scgcn|scGCN]]
**Spatial inference →** [[10-Summaries/biancalani-2021-tangram|Tangram]] · [[10-Summaries/kleshchevnikov-2022-cell2location|cell2location]] · [[10-Summaries/debnath-2026-ison|ISON]] · [[30-Concepts/spatial-multiomics]]
**Regulatory networks →** [[10-Summaries/yuan-2024-linger|LINGER]] · [[30-Concepts/gene-regulatory-network]]
**Reviews →** [[10-Summaries/wang-2023-multimodal-review|Wang & Jin 2023 methods+integration]] · [[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]] · [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]] · [[10-Summaries/bi-2024-multiomics-review|Bi & Weng 2024 (integration topology + protein lineages)]]

---

### Long-Read & Single-Molecule Methods

PacBio and Nanopore approaches that capture chromatin state, methylation, and structural variants on native DNA molecules.

**Start here →** [[40-Topics/long-read-sequencing]] · [[30-Concepts/fiber-seq]] · [[30-Concepts/daf-seq]]
**Key papers →** [[10-Summaries/andrewb-2020-science|Fiber-seq (Stergachis 2020)]] · [[10-Summaries/altemose-2022-dimelo-seq|DiMeLo-seq]] · [[10-Summaries/nanda-2024-smrt-tag|SMRT-Tag]]

---

### 3D Genome at Single-Cell Resolution

Chromatin conformation capture (Hi-C) adapted for single cells, haplotype-resolved structures, computational harmonization, and **nuclear-lamina spatial positioning** as a third measurement axis.

**Start here →** [[40-Topics/3d-genome]] · [[30-Concepts/single-cell-hi-c]] · [[30-Concepts/dip-c]] · [[30-Concepts/nuclear-lamina]] · [[30-Concepts/lamina-associated-domains]] · [[30-Concepts/damid]]
**Founding →** [[10-Summaries/nagano-2013-nature|Nagano 2013]] · [[10-Summaries/tan-2018-science|Dip-C (Tan 2018)]]
**Lamina lineage →** [[10-Summaries/van-steensel-2017-lads-review|LADs review (van Steensel & Belmont 2017)]] · [[10-Summaries/rooijers-2019-scdamt-seq|scDam&T-seq (Rooijers 2019)]] · [[10-Summaries/de-luca-2021-scdamid-protocol|scDamID protocol (de Luca & Kind 2021)]]
**Feature callers →** [[30-Concepts/chromatin-loop]] · [[10-Summaries/yu-2021-snaphic|SnapHiC (loops)]] · [[10-Summaries/xiong-2024-scghost|scGHOST (subcompartments)]] · [[30-Concepts/multi-way-chromatin-interaction]] · [[10-Summaries/park-2026-mintsc|MINTsC (multi-way)]]
**Differential compartments →** [[10-Summaries/chakraborty-2022-dchic|dcHiC (Chakraborty 2022)]] · [[30-Concepts/chromatin-compartments]]
**Protein-anchored branch →** [[30-Concepts/chia-pet]] · [[10-Summaries/li-2014-chia-pet|Li & Ruan 2014 (ChIA-PET)]]
**Heterogeneity metric →** [[10-Summaries/mali-2025-conformational-heterogeneity|C.H. metric (Mali 2025)]]
**Biophysical / LLPS →** [[10-Summaries/gibson-2019-chromatin-llps|Gibson 2019]] · [[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]] · [[10-Summaries/daugird-2024-viscoelastic-chromatin|Daugird 2024]] · [[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]

---

### Duplex Sequencing

Ultra-accurate error correction by reading both strands of a DNA molecule. Essential for detecting rare somatic variants.

**Start here →** [[40-Topics/duplex-sequencing]] · [[30-Concepts/nanoseq]] · [[30-Concepts/codec]]
**Founding →** [[10-Summaries/schmitt-2012-pnas|Schmitt & Loeb 2012]] · [[10-Summaries/kennedy-2014-duplex-protocol|Kennedy 2014]]
**Benchmark →** [[10-Summaries/zhang-2025-smaht-duplex-benchmark|SMaHT Benchmark (Zhang 2025)]]
**Beyond duplex →** [[10-Summaries/liu-2024-hidef-seq|HiDEF-seq (Liu 2024)]] — unamplified single molecules reach the single-strand lesions duplex methods destroy; finds NanoSeq ssDNA calls ~18× inflated

---

## Browse the wiki

| | |
|---|---|
| [[10-Summaries/index\|Papers]] | All ~299 paper summaries, organized by topic |
| [[20-Entities/index\|People & labs]] | Researchers, labs, consortia |
| [[30-Concepts/index\|Concepts]] | Definitions: methods, terms, ideas |
| [[40-Topics/index\|Topics]] | Broad themes that gather concepts and papers |
| [[50-Notes/index\|Notes]] | Cross-source syntheses, organized by layer |

---

## Synthesis & open threads

- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|Mosaicism × Epigenome: The Synthesis Gap]] — the central conceptual note; updated 2026-05-13 after Duplex-Multiome closes the method gap.
- [[50-Notes/regulatory-layers-overview|Regulatory layers — five (or six) axes of epigenome interpretation]] — entry point mapping accessibility / methylation / histone marks / DNA-protein (TF) binding / 3D genome (+ structural-physical) to concept pages and assays.
- [[50-Notes/joint-assays-by-layer-pair|Joint single-cell assays, by layer-pair]] — methodological-integration catalog: which assay bridges which layer-pair, genotype-anchored first, climaxing on Duplex-Multiome.
- [[50-Notes/computational-framework-structure|Computational framework — structuring the review's main section]] — draft scaffold: invert the 5-layer frame, organize computation by task ending in integration; includes the task × layer matrix.
- [[50-Notes/single-cell-duplex-sequencing|Single-cell duplex — the methodological frontier closes]] — synthesis of the 2025 inflection: PTA + duplex validation ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]) and same-molecule Duplex-Multiome ([[10-Summaries/kriz-2025-duplex-multiome]]).
- [[50-Notes/droplet-vs-single-molecule-scdna|Droplet vs single-molecule — the breadth/depth tradeoff]] — why 10⁵-cell droplet platforms and ~10-cell single-molecule platforms answer different biological questions, and why the gap is sustained by physics rather than engineering.
- [[50-Notes/pta-inflection-point|The PTA inflection point]] — how the 2021 Primary Template-Directed Amplification chemistry shifted scDNA-seq from "needs bioinformatic correction" to "cohort-scale routine". Frames the BSMN/SMaHT/Duplex-Multiome era as PTA-enabled.
- [[50-Notes/mnase-vs-tn5-chromatin|MNase vs Tn5 — two chemistries for single-cell histone profiling]] — when to pick scChIC-family (MNase) vs CUT&Tag-family (Tn5) chemistry, indexed by which secondary measurement (methylation, accessibility, RNA, multi-mark) the experiment needs.
- [[50-Notes/methylation-cancer-origin-classifiers|Methylation cancer-of-origin classifiers]] — clinical-grade epigenetic memory. EPICUP (CUP), Heidelberg MNP (brain tumors), AML classifiers. Why methylation succeeds where other epigenetic marks struggle.
- [[50-Notes/open-questions]] — tensions and gaps surfaced during ingest, by domain
- [[50-Notes/synthesis-targets]] — clusters of papers ripe for a written synthesis

---

## How this wiki works

Three layers, never mixed:

1. **Sources** (`00-Sources/`) — immutable raw inputs (papers, articles, data). Read-only.
2. **Wiki** (`10-Summaries/`, `20-Entities/`, `30-Concepts/`, `40-Topics/`, `50-Notes/`) — distillation, linked into a graph.
3. **Schema** (CLAUDE + `90-Meta/templates/`) — the conventions the maintainer follows.

The maintainer reads each new source in full, writes a summary, and **touches 5–15 other pages** per ingest to weave it into the graph. See the ingest log for a chronological record.

---

*This wiki is a personal research tool. Papers are summarized by an LLM; always verify against the original sources. Last updated 2026-08-14.*
