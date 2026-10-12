---
type: topic
title: Single-cell multi-omics
aliases: [single-cell multiomics, sc-multiomics, multimodal omics]
tags: [single-cell, methods, multiomics, multi-omics]
created: 2026-05-07
updated: 2026-10-12
paper_section: ["4.3"]
---

# Single-cell multi-omics

> Methods that measure two or more molecular modalities (DNA sequence, RNA, chromatin accessibility, surface protein, methylation, …) in the same single cell, enabling joint analysis that uncoupled single-modality assays cannot. Most modality pairs, and some triples, are now technically feasible, and computational integration has become the main bottleneck ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]; [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).

> [!abstract] 한눈에
> 한 세포에서 DNA, RNA, chromatin, methylation, 단백질 가운데 두 층 이상을 함께 읽는 방법은 이제 대부분의 조합이 가능하고, 남은 병목은 데이터 통합이다 ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]; [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]). droplet 플랫폼은 세포 수를, single-molecule·plate 기반 플랫폼은 세포당 깊이를 얻는 대신 다른 쪽을 내준다 ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]; [[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

## Key points

- **Integration, not measurement, is the bottleneck.** Most modality pairs and some triples can now be co-measured ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]; [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).
- **Breadth and depth trade off.** Droplet platforms scale to 10⁵+ cells but profile each modality coarsely; single-molecule and plate-based platforms profile deeply at far lower cell number ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]; [[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).
- **The coupling mechanism sets the throughput ceiling.** When analytes are uncoupled (physical separation, preamplification-and-split, differential barcoding, combinatorial indexing) predicts each method's scale and explains why genome + transcriptome lags epigenome + transcriptome ([[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).
- **Co-measurement can overturn single-layer inference.** DNTR-seq showed *MYC* and *TCF7L2* largely unaffected by copy number despite strong structural imbalance, so CNV→expression cannot be assumed ([[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).
- **A growing genre predicts modalities that were never measured.** RNA→protein, RNA→space and RNA→spatial chromatin are each solved by several mechanisms, but only one returns an uncertainty estimate ([[10-Summaries/lakkis-2022-scipenn|sciPENN]]; [[10-Summaries/debnath-2026-ison|ISON]]). (synthesis)

## Start here

> [!cards]
> - `note` [[50-Notes/joint-assays-by-layer-pair|Joint assays by layer pair]] — Joint single-cell assays organised by the layer pair they bridge, genotype-anchored first, ending on Duplex-Multiome.
> - `concept` [[30-Concepts/gt-seq|G&T-seq]] — Physical-separation scDNA + scRNA; the first joint DNA + RNA assay.
> - `concept` [[30-Concepts/got|GoT]] — Single-cell genotype + transcriptome on droplet 10x scRNA-seq.
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Single-cell genotype + chromatin accessibility on droplet 10x scATAC-seq, via gDNA capture.
> - `concept` [[30-Concepts/daf-seq|DAF-seq]] — Single-cell, single-molecule chromatin + DNA sequence via deaminase footprinting.
> - `concept` [[30-Concepts/spatial-multiomics|Spatial multi-omics]] — Spatially resolved multi-omic measurements.

## How the field is organised

Several taxonomies anchor the method landscape:

- **By modality pair** ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]; [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]):
  - scRNA + scATAC (10x Multiome, SHARE-seq) ([[10-Summaries/ma-2020-share-seq|Ma 2020]]).
  - scRNA + surface protein (CITE-seq, REAP-seq) — see [[cite-seq|CITE-seq]] ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]).
  - scDNA + scRNA (G&T-seq, DR-seq, SIDR-seq, DNTR-seq) ([[10-Summaries/macaulay-2015-gt-seq|Macaulay 2015]]; [[10-Summaries/dey-2015-dr-seq|Dey 2015]]).
  - scRNA + methylome (scM&T-seq, snmCT-seq) ([[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).
  - CRISPR-perturbed scRNA (Perturb-seq, CROP-seq) ([[10-Summaries/bi-2024-multiomics-review|Bi & Weng 2024]]).
  - scATAC + scRNA + protein (DOGMA-seq) — see [[dogma-seq|DOGMA-seq]] ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).
  - scDNA + scATAC + RNA + protein (GoT–ChA + DOGMA-seq via imputation) ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).
- **By when modalities are uncoupled**: before library prep by physical separation (G&T-seq, SIDR-seq) ([[10-Summaries/macaulay-2015-gt-seq|Macaulay 2015]]); during library prep by joint barcoding ([[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]); after library prep by diagonal computational integration ([[10-Summaries/wang-2023-multimodal-review|Wang 2023]]). The finer split — physical separation, preamplification-and-split, seq-split by differential barcoding, combinatorial indexing — predicts each method's throughput ceiling ([[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).
- **By throughput vs depth**: one-cell-at-a-time deep assays vs droplet or combinatorial-indexing scalable assays, with histone modifications, proteome and spatial named as the 2020 gaps ([[10-Summaries/zhu-2020-multimodal-power-of-many|Zhu 2020]]).
- **By computational anchor**: horizontal / vertical / diagonal / mosaic ([[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]), with bridge integration removing the gene-activity assumption diagonal methods otherwise require ([[10-Summaries/hao-2024-seurat-v5|Seurat v5]]).
- **By integration topology and protein lineage**: horizontal / vertical / diagonal, and NGS-based vs mass-spectrometry-based protein quantification, with the CRISPR-perturbation dual-modal family covered explicitly ([[10-Summaries/bi-2024-multiomics-review|Bi & Weng 2024]]).

## Why it matters

- The same cell answers several questions at once: what is this cell's genotype, and what does it express ([[10-Summaries/nam-2019-got|Nam 2019]])?
- Joint assays provide the **phenotypic association** capability of the [[scdna-capabilities-framework|scDNA capabilities framework]] (synthesis).
- Cell-type atlases (Human Cell Atlas) and disease atlases are increasingly multi-omic by default ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]).
- Some findings exist only because genome and transcriptome were read in the same cells: ~16% of *OCT4*-edited human embryo cells carried unintended edits — LOH beyond the on-target locus plus chromosome-6 segmental changes ([[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).

## Genotype-anchored joint assays

Assays that read DNA sequence or copy number together with another layer in the same cell.

| Assay | Year | Layers measured | Chemistry | Note |
|---|---|---|---|---|
| [[gt-seq\|G&T-seq]] | 2015 | Genome + transcriptome | Physical separation of DNA and RNA | First joint DNA + RNA assay; trisomy-11 subclone in HCC38-BL ([[10-Summaries/macaulay-2015-gt-seq\|Macaulay 2015]]); step-by-step protocol ([[10-Summaries/macaulay-2016-gt-seq-protocol\|Macaulay 2016]]) |
| [[30-Concepts/dr-seq\|DR-seq]] | 2015 | Genome + transcriptome | One-pot, quasilinear | CNVs drive expression variability ([[10-Summaries/dey-2015-dr-seq\|Dey 2015]]) |
| DNTR-seq | — | Genome + transcriptome | — | Dosage compensation: *MYC* and *TCF7L2* largely unaffected by copy number ([[10-Summaries/vandereyken-2023-scmultiomics-review\|Vandereyken 2023]]) |
| [[30-Concepts/sctrio-seq\|scTrio-seq]] | 2016 | CNV + methylome + transcriptome | Mild cytoplasmic lysis; nucleus and mRNA separated | CNVs drive expression but not methylation; HCC subpopulations; closest precedent for DNA-anchored mutation + epigenome + transcriptome ([[10-Summaries/hou-2016-sctrio-seq\|Hou 2016]]) |
| [[30-Concepts/got\|GoT]] | 2019 | Targeted genotype + transcriptome | Amplicon from cDNA on droplet 10x scRNA-seq | CALR-mutated MPN ([[10-Summaries/nam-2019-got\|Nam 2019]]); [[30-Concepts/circularization-got\|circularization GoT]] extends it to distal mutation loci |
| [[30-Concepts/resolveome\|ResolveOME]] | 2023 | Genome-wide genotype + full transcriptome | PTA | AML quizartinib resistance (FLT3 + AXL) and breast cancer *PIK3CA* ([[10-Summaries/marks-2023-resolveome\|Marks 2023]]) |
| [[30-Concepts/got-cha\|GoT–ChA]] | 2024 | Targeted genotype + chromatin accessibility | gDNA capture on droplet 10x scATAC-seq | JAK2V617F MPN; cell-intrinsic chromatin priming of HSCs; integrated with [[30-Concepts/dogma-seq\|DOGMA-seq]] by imputation ([[10-Summaries/izzo-2024-got-cha\|GoT–ChA]]) |
| wellDA-seq | 2024 | Genome-wide copy number + chromatin accessibility | Two sequential, differently barcoded Tn5 tagmentations in nanowells | Subclonal CNAs reshape accessibility in cis: ~80% of differential chromatin-hub bins lie on subclonal CNA bins in breast tumours (preprint) ([[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]]) |
| [[daf-seq\|DAF-seq / scDAF-seq]] | 2025 | Single-molecule chromatin + DNA sequence | Deaminase footprinting | Chromosome-length single-cell, single-molecule chromatin maps ([[10-Summaries/swanson-2025-daf-seq\|DAF-seq]]) |
| [[30-Concepts/defnd-seq\|DEFND-seq]] | 2025 | Whole genome + RNA | Nucleosome depletion on stock 10x Multiome | Glioblastoma CNV/SNV-to-expression links ([[10-Summaries/olsen-2025-defnd-seq\|Olsen 2025]]) |
| [[30-Concepts/sdr-seq\|SDR-seq]] | 2025 | Targeted DNA + RNA (≤480 loci + genes) | Droplet, Tapestri | ~90% allele recovery, low allelic dropout, per-cell zygosity; B-cell lymphoma clonal and variant phenotyping ([[10-Summaries/lindenhofer-2025-sdr-seq\|Lindenhofer 2025]]) |
| SPLONGGET | 2025 | Genotype + accessibility + transcriptome | Long-read, modified 10x Multiome | CD19 escape in B-ALL (preprint) ([[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]) |
| [[30-Concepts/dd-seq\|D&D-seq / D&D-GoT-ChA]] | 2026 | TF binding (+ genotype + accessibility when composed with GoT–ChA) | Nanobody-deaminase footprinting | CTCF binding in closed chromatin; IDH2-mutant T cells show disrupted CTCF binding ([[10-Summaries/chi-2026-dd-seq\|Chi 2026]]) |
| SCARCE | 2026 | Targeted DNA genotype + ADT surface protein | Tapestri | Finds cell-type-specific somatic variants, e.g. *DDX3X* drivers in CD4−CD8− T cells in refractory coeliac disease ([[10-Summaries/gillman-2026-scarce\|SCARCE]]) |

DAF-seq is the single-cell descendant of bulk [[30-Concepts/fiber-seq|Fiber-seq]] (methyltransferase stenciling); both belong to the [[30-Concepts/single-molecule-footprinting|single-molecule footprinting]] class ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

## Chromatin, methylation and histone combinations

Assays that pair epigenomic layers with each other or with RNA, without a genotype anchor. [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] is the common readout layer, with [[30-Concepts/chromatin-actuation|chromatin actuation]] as its single-molecule refinement.

| Assay | Year | Layers measured | Chemistry | Note |
|---|---|---|---|---|
| [[30-Concepts/sci-car\|sci-CAR]] | 2018 | Accessibility + RNA | Combinatorial indexing | Thousands of cells ([[10-Summaries/cao-2018-sci-car\|Cao 2018]]) |
| [[30-Concepts/share-seq\|SHARE-seq]] | 2020 | Accessibility + RNA | Split-pool barcoding | Tens of thousands of cells; introduces the chromatin-potential framework ([[10-Summaries/ma-2020-cell\|Ma 2020]]; [[10-Summaries/ma-2020-share-seq\|Ma 2020 perspective]]) |
| [[30-Concepts/scnmt-seq\|scNMT-seq]] | 2018 | Methylation + accessibility + RNA | GpC methyltransferase (NOMe) + bisulfite, after DNA/RNA separation | First triple-omics; methylation–accessibility coupling strengthens along differentiation ([[10-Summaries/clark-2018-scnmt-seq\|Clark 2018]]) |
| Camellia-seq | 2023 | Lineage barcodes + RNA + CpG methylation + GpC accessibility | GpC methylation for accessibility | DNA methylation, not expression or accessibility, carries clonal memory in self-renewing HSCs ([[10-Summaries/li-2023-darlin\|Li 2023]]) |
| [[30-Concepts/simple-seq\|SIMPLE-seq]] | 2024 | 5mC + 5hmC | Bisulfite-free chemical labelling; combinatorial indexing | Joint 5mC + 5hmC at base resolution ([[10-Summaries/bai-2024-simple-seq\|Bai 2024]]) |
| sciMET+ATAC | 2025 | Methylome + accessibility | Sequential (double) tagmentation | Variant of sciMETv3 ([[10-Summaries/nichols-2025-scimetv3\|Nichols 2025]]) |
| [[30-Concepts/splicool-seq\|SpliCOOL-seq]] | 2026 | 5mC + accessibility (GpC) | Split-pool barcoding | High throughput ([[10-Summaries/shen-2026-splicool-seq\|Shen 2026]]) |
| [[30-Concepts/scepi2-seq\|scEpi²-seq]] | 2025 | Histone mark + 5mC | sortChIC + TAPS | ([[10-Summaries/geisenberger-2025-scepi2-seq\|Geisenberger 2025]]) |
| [[30-Concepts/6-base-cut-and-tag\|6-base-CUT&Tag]] | 2026 | Histone mark + 5mC + 5hmC, per fragment (bulk) | CUT&Tag + 6-base enzymatic conversion | ([[10-Summaries/tavares-2026-6-base-cut-tag\|Tavares 2026]]) |
| [[30-Concepts/scchix-seq\|scChIX-seq]] | 2023 | Two histone marks | Two antibodies + computational deconvolution | ([[10-Summaries/yeung-2023-scchix-seq\|Yeung 2023]]) |
| [[30-Concepts/scicut-tag\|sciCUT&Tag]] | 2023 | Histone mark | Combinatorial-indexing CUT&Tag | Multi-epitope extension in [[30-Concepts/multi-tag\|MulTI-Tag]] ([[10-Summaries/janssens-2023-scicut-tag\|Janssens 2023]]) |
| scCUT&Tag-pro | 2022 | Histone mark + 173 surface proteins | CUT&Tag + ADT | Protein as the integration currency: six separately measured marks harmonised and interpolated per cell, though not co-measured ([[10-Summaries/zhang-2022-sccut-tag-pro\|Zhang 2022]]) |
| OneCell CUT&Tag | 2026 | Histone mark + full-length RNA + surface markers | One cell per well | From ≥1 cell; epigenome/RNA identity discordance and asynchronous remodelling in mammary transdifferentiation ([[10-Summaries/schwager-2026-onecell-cut-tag\|Schwager 2026]]) |
| Paired Hi-C | 2025 | Single-nucleus Hi-C + RNA | 10x Multiome kit | ([[10-Summaries/chang-2025-droplet-hi-c\|Droplet Hi-C]]) |

Other findings:

- **GpC-methyltransferase accessibility gives higher promoter coverage than ATAC** and distinguishes truly closed from unsampled, because every read reports ([[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).
- **Different layers, different answers on CNV coupling.** scTrio-seq found that CNVs do not perturb local DNA methylation, while wellDA-seq reports that subclonal CNAs reshape chromatin accessibility in cis ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]; [[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]). Different epigenetic layers, so not a contradiction (synthesis).
- **Co-measurement as validation.** MINTsC validates chromatin contacts using DNA methylation partial correlations from the same sn-m3C-seq cells — an argument only available in joint assays, and the sharpest demonstration in the corpus that co-measurement pays off analytically rather than only descriptively ([[10-Summaries/park-2026-mintsc|MINTsC]]). (synthesis)
- A layer-by-layer protocol catalog, including the single-cell proteome methods this wiki otherwise lacks ([[10-Summaries/lim-2024-single-cell-omics-review|Lim 2024]]).

## Spatial and long-read

- **Spatial multi-omics** preserves tissue context, by imaging (MERFISH, seqFISH, in situ) or by NGS (Visium, Slide-seq) ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]; [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]). See [[spatial-multiomics|spatial multi-omics]].
- **In situ genome sequencing.** [[30-Concepts/igs|IGS]] sequences DNA inside intact fixed cells, giving 3D-resolved single-cell genomes ([[10-Summaries/andrewc-2020-science|Payne 2021]]).
- **Long-read multi-modal chromatin.** SAMOSA footprints oligonucleosomes on single long molecules (bulk); the tagmentation variant [[30-Concepts/samosa-tag|SAMOSA-Tag]] is a later paper ([[10-Summaries/abdulhay-2020-samosa|Abdulhay 2020]]). [[30-Concepts/smrt-tag|SMRT-Tag]] is the related long-read tagmentation method.
- **Spatial chromatin without a spatial multiome kit.** ISON addresses a gap that is commercial rather than conceptual: spatial multiome kits do not exist, while spatial transcriptomics and single-cell multiome kits do. It learns a shared embedding across the two, decodes spatial RNA through the multiome's ATAC decoder to infer spatial accessibility, then reconstructs spatially resolved GRNs ([[10-Summaries/debnath-2026-ison|ISON]]). The **linear KL-NMF model beat a contrastive VAE** consistently, and the *inferred* accessibility recovered eQTL- and Hi-C-supported regulatory links **better than the directly measured** spatial ATAC ([[10-Summaries/debnath-2026-ison|ISON]]).

## Integration methods

The corpus covers the full genealogy, from the 2018 origin to reference mapping. MNN and Seurat CCA appeared in the same journal issue on the same day with opposite strategies ([[10-Summaries/haghverdi-2018-mnn|MNN]]; [[10-Summaries/butler-2018-seurat-cca|Seurat CCA]]). Multi-omic QC and integration recommendations are collected in [[10-Summaries/heumos-2023-best-practices|Heumos 2023]], and an integration-tool taxonomy (matrix factorisation vs manifold alignment vs deep generative) in [[10-Summaries/wang-2023-multimodal-review|Wang 2023]].

| Tool | Year | Strategy | Note |
|---|---|---|---|
| [[10-Summaries/haghverdi-2018-mnn\|MNN]] | 2018 | Mutual nearest neighbours | Origin of the field ([[10-Summaries/haghverdi-2018-mnn\|MNN]]) |
| [[10-Summaries/butler-2018-seurat-cca\|Seurat CCA]] | 2018 | Canonical correlation alignment | Origin of the field ([[10-Summaries/butler-2018-seurat-cca\|Seurat CCA]]) |
| [[10-Summaries/argelaguet-2018-mofa\|MOFA]] | 2018 | Sparse Bayesian factor analysis across omics layers | CLL cohort (N = 200) and scM&T-seq mESC (87 cells) applications ([[10-Summaries/argelaguet-2018-mofa\|MOFA]]) |
| [[10-Summaries/korsunsky-2019-harmony\|Harmony]] | 2019 | Embedding correction | Multi-covariate support; LISI metric pair ([[10-Summaries/korsunsky-2019-harmony\|Harmony]]) |
| [[10-Summaries/welch-2019-liger\|LIGER]] | 2019 | Factorisation into shared and dataset-specific factors | Differences between datasets stay legible ([[10-Summaries/welch-2019-liger\|LIGER]]) |
| [[10-Summaries/hao-2021-seurat-wnn\|Seurat WNN]] | 2021 | Paired (vertical); per-cell modality weights | The WNN reference the corpus previously lacked ([[10-Summaries/hao-2021-seurat-wnn\|Seurat WNN]]) |
| [[10-Summaries/gayoso-2021-totalvi\|totalVI]] | 2021 | Paired (vertical); deep generative | Protein background model ([[10-Summaries/gayoso-2021-totalvi\|totalVI]]) |
| [[10-Summaries/kang-2021-symphony\|Symphony]] | 2021 | Reference mapping | RNA→protein by reference mapping; see [[30-Concepts/reference-atlas-mapping]] ([[10-Summaries/kang-2021-symphony\|Symphony]]) |
| [[10-Summaries/song-2021-scgcn\|scGCN]] | 2021 | Reference mapping, graph convolution | ([[10-Summaries/song-2021-scgcn\|scGCN]]) |
| [[10-Summaries/biancalani-2021-tangram\|Tangram]] | 2021 | Spatial alignment | RNA→space; with paired SHARE-seq input it carries chromatin into space ([[10-Summaries/biancalani-2021-tangram\|Tangram]]) |
| [[10-Summaries/lakkis-2022-scipenn\|sciPENN]] | 2022 | Deep learning, [[30-Concepts/cite-seq\|CITE-seq]] at scale | Partially overlapping antibody panels; uncertainty quantification ([[10-Summaries/lakkis-2022-scipenn\|sciPENN]]) |
| [[10-Summaries/kleshchevnikov-2022-cell2location\|cell2location]] | 2022 | Spatial deconvolution | RNA→space ([[10-Summaries/kleshchevnikov-2022-cell2location\|cell2location]]) |
| [[10-Summaries/zhang-2022-higashi\|Higashi]] | 2022 | Joint modelling | A co-assayed modality is a prediction target rather than an input ([[10-Summaries/zhang-2022-higashi\|Higashi]]) |
| [[10-Summaries/hao-2024-seurat-v5\|Seurat v5]] | 2024 | Bridge integration | Removes the gene-activity assumption of diagonal methods ([[10-Summaries/hao-2024-seurat-v5\|Seurat v5]]) |
| [[10-Summaries/debnath-2026-ison\|ISON]] | 2026 | Shared embedding + learned ATAC decoder | RNA→spatial chromatin ([[10-Summaries/debnath-2026-ison\|ISON]]) |

**Predicting a modality you never measured.** Five instances, five mechanisms — RNA→protein by reference mapping ([[10-Summaries/kang-2021-symphony|Symphony]]) or deep learning ([[10-Summaries/lakkis-2022-scipenn|sciPENN]]); RNA→space by alignment ([[10-Summaries/biancalani-2021-tangram|Tangram]]) or deconvolution ([[10-Summaries/kleshchevnikov-2022-cell2location|cell2location]]); RNA→spatial chromatin via a paired assay ([[10-Summaries/biancalani-2021-tangram|Tangram]]) or a learned decoder ([[10-Summaries/debnath-2026-ison|ISON]]). The shared premise is that a reference substitutes for an experiment; the shared risk is that only one of them returns an uncertainty estimate. (synthesis)

## Regulatory networks from joint accessibility and expression

- [[10-Summaries/pliner-2018-cicero|Cicero]] links elements to genes by co-accessibility ([[10-Summaries/pliner-2018-cicero|Cicero]]).
- [[10-Summaries/kamimoto-2023-celloracle|CellOracle]] uses the resulting network as a simulation operator for in-silico TF perturbation ([[10-Summaries/kamimoto-2023-celloracle|CellOracle]]).
- [[10-Summaries/bravo-2023-scenicplus|SCENIC+]] infers enhancer-driven regulons and reports that only 49% of enhancers regulate their most proximal gene ([[10-Summaries/bravo-2023-scenicplus|SCENIC+]]).
- [[10-Summaries/yuan-2024-linger|LINGER]] infers regulatory networks from single-cell multiome data ([[10-Summaries/yuan-2024-linger|LINGER]]).

## Reviews

- [[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]] — Baysoy/Fan/Satija technological landscape.
- [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]] — Vandereyken/Voet methods and applications, including spatial.
- [[10-Summaries/heumos-2023-best-practices|Heumos 2023]] — Heumos/Theis best-practices analysis recommendations.
- [[10-Summaries/wang-2023-multimodal-review|Wang 2023]] — Wang/Jin methods catalog and integration-tool taxonomy.
- [[10-Summaries/bi-2024-multiomics-review|Bi & Weng 2024]] — methods catalog by integration topology and protein-quantification lineage.
- [[10-Summaries/zhu-2020-multimodal-power-of-many|Zhu 2020]] — throughput-vs-depth taxonomy and the 2020 gaps.
- [[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]] — computational principles of integration.
- [[10-Summaries/lim-2024-single-cell-omics-review|Lim 2024]] — layer-by-layer protocol catalog.

## People and groups

- [[20-Entities/dan-a-landau]] and the [[20-Entities/landau-lab]] — the GoT → circularization GoT → GoT–ChA methods program.
- [[20-Entities/franco-izzo]] — first author of GoT–ChA; co-author on the original GoT and on D&D-seq.
- [[20-Entities/anna-s-nam]] — first author of the original GoT paper.
- [[20-Entities/jay-a-a-west]] — corresponding author of ResolveOME; BioSkryb / PTA commercialisation.
- [[20-Entities/elliott-g-swanson]] — co-first author of DAF-seq.
- [[20-Entities/andrew-b-stergachis]] — senior author of DAF-seq and developer of Fiber-seq.
- [[20-Entities/thierry-voet]] — KU Leuven; G&T-seq co-developer.
- [[20-Entities/rong-fan]] — Yale; spatial multi-omics.
- [[20-Entities/rahul-satija]] — NYGC; Seurat integration toolkit.
- [[20-Entities/fabian-theis]] — Helmholtz Munich; best-practices recommendations.
- [[20-Entities/alexander-van-oudenaarden]] — sortChIC, scChIX-seq, scEpi²-seq.
- [[20-Entities/chengqi-yi]] — SIMPLE-seq.
- [[20-Entities/xiaoying-fan]] — SpliCOOL-seq.
- [[20-Entities/shankar-balasubramanian]] — 6-base-CUT&Tag.
- [[20-Entities/steven-henikoff]] — sciCUT&Tag, MulTI-Tag.
- [[20-Entities/vijay-ramani]] — SMRT-Tag, SAMOSA-Tag.

## Open questions

- **Cost per cell.** Multi-omic methods are substantially more expensive than unimodal assays at equal cell number ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]).
- **Benchmarking diagonal integration.** Integration accuracy across diagonal (different cells, different modalities) approaches is hard to benchmark ([[10-Summaries/wang-2023-multimodal-review|Wang 2023]]).
- Where does scDAF-seq's per-cell ~99% genome coverage at ~10-cell throughput become more useful than GoT–ChA's ~38% genotyping at 10⁵-cell throughput, and which experimental questions sit on each side of that line ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]; [[10-Summaries/izzo-2024-got-cha|GoT–ChA]])? (synthesis)
- The first genotype-anchored sources (GoT, GoT–ChA, DAF-seq) all use within-patient wild-type cells as comparators, or within-cell haplotypes for DAF-seq ([[10-Summaries/nam-2019-got|Nam 2019]]; [[10-Summaries/izzo-2024-got-cha|GoT–ChA]]; [[10-Summaries/swanson-2025-daf-seq|DAF-seq]]). Are there single-cell multi-omic questions where this design does not apply? (synthesis)
- Imputation-based integration (GoT–ChA + DOGMA-seq via mitochondrial variants and surface proteins) works in MPN; how well does it generalise ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]])? (synthesis)
- Bulk Fiber-seq → single-cell DAF-seq closed a major gap for chromatin. Is there an analogous "single-molecule, per-fiber" extension waiting to be built for [[got|GoT]] and [[got-cha|GoT–ChA]]? (synthesis)
- Only one of the modality-prediction methods returns an uncertainty estimate, so predicted modalities are hard to weigh against measured ones ([[10-Summaries/lakkis-2022-scipenn|sciPENN]]). (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Genome-wide chromatin accessibility in individual cells via Tn5.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — Aligners, callers, imputers, integrators and network-inference frameworks.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC at CpG dinucleotides, the most stable epigenetic mark.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Post-translational histone marks that demarcate chromatin states.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Compartments, TADs and loops inside the nucleus.
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Technologies that interrogate the DNA of single cells.

## All sources on this page

> [!info]- 59 summaries cited here
> - [[10-Summaries/abdulhay-2020-samosa|Abdulhay 2020]]
> - [[10-Summaries/andrewc-2020-science|Payne 2021]]
> - [[10-Summaries/argelaguet-2018-mofa|Argelaguet 2018]]
> - [[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]
> - [[10-Summaries/bai-2024-simple-seq|Bai 2024]]
> - [[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]
> - [[10-Summaries/bi-2024-multiomics-review|Bi & Weng 2024]]
> - [[10-Summaries/biancalani-2021-tangram|Biancalani 2021]]
> - [[10-Summaries/bravo-2023-scenicplus|Bravo 2023]]
> - [[10-Summaries/butler-2018-seurat-cca|Butler 2018]]
> - [[10-Summaries/cao-2018-sci-car|Cao 2018]]
> - [[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]
> - [[10-Summaries/chi-2026-dd-seq|Chi 2026]]
> - [[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]
> - [[10-Summaries/debnath-2026-ison|Debnath 2026]]
> - [[10-Summaries/dey-2015-dr-seq|Dey 2015]]
> - [[10-Summaries/gayoso-2021-totalvi|Gayoso 2021]]
> - [[10-Summaries/geisenberger-2025-scepi2-seq|Geisenberger 2025]]
> - [[10-Summaries/gillman-2026-scarce|Gillman 2026]]
> - [[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]
> - [[10-Summaries/hao-2021-seurat-wnn|Hao 2021]]
> - [[10-Summaries/hao-2024-seurat-v5|Hao 2024]]
> - [[10-Summaries/heumos-2023-best-practices|Heumos 2023]]
> - [[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/janssens-2023-scicut-tag|Janssens 2023]]
> - [[10-Summaries/kamimoto-2023-celloracle|Kamimoto 2023]]
> - [[10-Summaries/kang-2021-symphony|Kang 2021]]
> - [[10-Summaries/kleshchevnikov-2022-cell2location|Kleshchevnikov 2022]]
> - [[10-Summaries/korsunsky-2019-harmony|Korsunsky 2019]]
> - [[10-Summaries/lakkis-2022-scipenn|Lakkis 2022]]
> - [[10-Summaries/li-2023-darlin|Li 2023]]
> - [[10-Summaries/lim-2024-single-cell-omics-review|Lim 2024]]
> - [[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]
> - [[10-Summaries/ma-2020-cell|Ma 2020]]
> - [[10-Summaries/ma-2020-share-seq|Ma 2020]]
> - [[10-Summaries/macaulay-2015-gt-seq|Macaulay 2015]]
> - [[10-Summaries/macaulay-2016-gt-seq-protocol|Macaulay 2016]]
> - [[10-Summaries/marks-2023-resolveome|Marks 2023]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
> - [[10-Summaries/nichols-2025-scimetv3|Nichols 2025]]
> - [[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/park-2026-mintsc|Park 2026]]
> - [[10-Summaries/pliner-2018-cicero|Pliner 2018]]
> - [[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]
> - [[10-Summaries/shen-2026-splicool-seq|Shen 2026]]
> - [[10-Summaries/song-2021-scgcn|Song 2021]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
> - [[10-Summaries/tavares-2026-6-base-cut-tag|Tavares 2026]]
> - [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]
> - [[10-Summaries/wang-2023-multimodal-review|Wang 2023]]
> - [[10-Summaries/wang-2024-wellda-seq|Wang 2024]]
> - [[10-Summaries/welch-2019-liger|Welch 2019]]
> - [[10-Summaries/yeung-2023-scchix-seq|Yeung 2023]]
> - [[10-Summaries/yuan-2024-linger|Yuan & Duren 2024]]
> - [[10-Summaries/zhang-2022-higashi|Zhang 2022]]
> - [[10-Summaries/zhang-2022-sccut-tag-pro|Zhang 2022]]
> - [[10-Summaries/zhu-2020-multimodal-power-of-many|Zhu]]
