---
title: Index
description: Catalog of every page in the wiki. Updated on every ingest and lint pass.
updated: 2026-05-13
---

# Index

This is the navigable catalog of the wiki. The maintainer (Claude) updates it on every ingest. Each entry: `- [[slug]] — one-line description`.

## Summaries

### Methods reviews (scDNA-seq / multi-omics / chromatin / methylation)

- [[10-Summaries/diane-2025-naturereviewsgenetics]] — Shao et al. 2025: keystone scDNA-seq review; current state of the field.
- [[10-Summaries/charles-2016-naturereviewsgenetics]] — Gawad/Quake 2016: foundational scDNA-seq review.
- [[10-Summaries/gilad-2021-annualreviewofgenomicsandhumangenetics]] — Evrony et al. 2021: applications-and-capabilities framework.
- [[10-Summaries/alev-2023-naturereviewsmolecularcellbiology]] — Baysoy/Fan/Satija 2023: multi-omics technological landscape.
- [[10-Summaries/katy-2023-naturereviewsgenetics]] — Vandereyken/Voet 2023: single-cell and spatial multi-omics methods.
- [[10-Summaries/lukas-2023-naturereviewsgenetics]] — Heumos/Theis 2023: best practices for single-cell analysis.
- [[10-Summaries/sandy-2019-naturereviewsgenetics]] — Klemm/Greenleaf 2019: chromatin accessibility canonical review.
- [[10-Summaries/zachary-2013-naturereviewsgenetics]] — Smith/Meissner 2013: DNA methylation in mammalian development.
- [[10-Summaries/yilei-2025-naturereviewsgenetics]] — Fu/Timp/Sedlazeck 2025: computational long-read methylation analysis.
- [[10-Summaries/profiling-the-epigenome-using-long-read-sequencing]] — Liu/Conesa 2025: comprehensive long-read epigenomics review.
- [[10-Summaries/navigating-the-3d-genome-at-single-cell-resolution-techniques-computation-and-mechanistic-landscapes]] — Hong/Dao 2025: single-cell 3D-genome review.
- [[10-Summaries/dna-methylation-an-epigenetic-mark-of-cellular-memory-experimental-molecular-medicine]] — Kim/Costello 2017: DNA methylation as epigenetic memory.

### Mosaicism reviews

- [[10-Summaries/lars-2017-naturereviewsgenetics]] — Forsberg/Dumanski 2017: mosaicism in health and disease.
- [[10-Summaries/ian-2015-trendsingenetics]] — Campbell/Lupski 2015: developmental timing of mutations.
- [[10-Summaries/bizzotto-2022-brain-mosaicism]] (= Bizzotto & Walsh 2022): brain mosaicism and lineage tracing.

### Primary methods papers (multi-omics + genotyping)

- [[10-Summaries/anna-2019-nature]] — Nam et al. 2019: GoT method paper; CALR-mutated MPN.
- [[10-Summaries/franco-2024-nature]] — Izzo et al. 2024: GoT–ChA method paper; JAK2V617F MPN.
- [[10-Summaries/elliott-2025-naturebiotechnology]] — Swanson et al. 2025: DAF-seq / scDAF-seq.
- [[10-Summaries/accurate-single-cell-genotyping-utilizing-information-from-the-local-genome-territory]] — Tu et al. 2021: SCOUT single-cell variant caller.
- [[10-Summaries/andrewb-2020-science]] — Stergachis et al. 2020: Fiber-seq, the foundational m6A-MTase chromatin stenciling paper.

### Primary methods papers (joint DNA + epigenome + RNA assays)

- [[10-Summaries/g-t-seq-parallel-sequencing-of-single-cell-genomes-and-transcriptomes]] — Macaulay 2015: G&T-seq, separation-based scDNA + scRNA.
- [[10-Summaries/integrated-genome-and-transcriptome-sequencing-of-the-same-cell]] — Dey 2015: DR-seq, one-pot scDNA + scRNA alternative.
- [[10-Summaries/single-cell-triple-omics-sequencing-reveals-genetic-epigenetic-and-transcriptomic-heterogeneity-in-hepatocellular-carcinomas]] — Hou 2016: scTrio-seq, CNV + methylation + RNA triple-omics.
- [[10-Summaries/scnmt-seq-enables-joint-profiling-of-chromatin-accessibility-dna-methylation-and-transcription-in-single-cells]] — Clark 2018: scNMT-seq, accessibility + methylation + RNA triple-omics.
- [[10-Summaries/joint-profiling-of-chromatin-accessibility-and-gene-expression-in-thousands-of-single-cells]] — Cao 2018: sci-CAR, scATAC + scRNA at thousands of cells.
- [[10-Summaries/share-seq-reveals-chromatin-potential-nature-reviews-genetics]] — Ma 2020 (NRG perspective): SHARE-seq, chromatin potential.
- [[10-Summaries/andrewc-2020-science]] — Payne 2021: IGS, in-situ genome sequencing with 3D spatial coordinates.

### Histone-modification foundational reviews

- [[10-Summaries/andrew-2011-cellresearch]] — Bannister & Kouzarides 2011: regulation of chromatin by histone modifications (foundational review).

## Notes (synthesized findings)

- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — **STATUS UPDATE 2026-05-13**: the methodological gap is closed by [[10-Summaries/andrea-2025-biorxiv|Duplex-Multiome]] (Kriz 2025 bioRxiv, Walsh + Lee labs). The note now articulates a **conceptual** novelty claim: jointly measuring mutation + epi + RNA at single-cell scale is possible; what's missing is the DNA-centric locus-state framework to interpret what those measurements mean. The planned review's contribution shifts from method-gap-identification to framework-articulation.

### Duplex sequencing

- [[10-Summaries/detecting-ultralow-frequency-mutations-by-duplex-sequencing]] — Kennedy/Loeb 2014: founding DS protocol.
- [[10-Summaries/a-universal-duplex-sequencing-approach-for-accurate-detection-of-somatic-mutations]] — Nandi/Alexandrov 2025: UDSeq at ~2.5×10⁻⁹/bp from 100 pg.
- [[10-Summaries/benchmarking-of-duplex-sequencing-approaches-to-reveal-somatic-mutation-landscapes]] — Zhang/Coorens 2025: SMaHT cross-method benchmark.

### Somatic mosaicism (primary papers)

- [[10-Summaries/a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis]] — Luquette/Walsh 2025: PTA + DS validation on 102 nuclei from lung/colon.
- [[10-Summaries/high-throughput-single-cell-analysis-reveals-progressive-mitochondrial-dna-mosaicism-throughout-life]] — Glynos/Chinnery 2023: mouse mtDNA heteroplasmy variance through life.
- [[10-Summaries/single-cell-mosaicism-analysis-reveals-cell-type-specific-somatic-mutational-burden-in-alzheimer-s-dementia]] — Kousi/Kellis 2022: cell-type-specific AD somatic mutation burden.
- [[10-Summaries/nanopore-sequencing-unveils-somatic-structural-variations-as-biomarkers-in-laryngeal-squamous-cell-carcinoma-genomes]] — Liu et al. 2025: SomaGauss-SV in LSCC, smoking × deletion correlation.
- [[10-Summaries/taejeong-2018-science]] — Bae 2018: 200–400 SNVs/cell in fetal-brain progenitors; mutation-spectrum shift CpG-deamination → oxidative damage from pre-gastrulation to neurogenesis.
- [[10-Summaries/taejeong-2022-science]] — Bae 2022: 131-brain BSMN cohort; aging-associated hypermutability; ASD enhancer MEIS-motif enrichment.
- [[10-Summaries/eran-2025-neuron]] — Mukamel 2025: snmC-seq atlas-scale (415K mouse brain cells) detects aneuploidy; chr16 trisomy 13× enriched; cell-type-specific enrichment in OPCs/Pons.
- [[10-Summaries/lodato-2015-science]] — Lodato 2015: foundational scWGS of 36 cortical neurons; nested lineage trees from somatic SNVs; transcription-associated damage.
- [[10-Summaries/mcconnell-2017-science]] — McConnell 2017: founding BSMN review; consortium-scale plan for cataloging brain somatic mutations in neurotypical and disease cohorts.
- [[10-Summaries/lodato-2018-science]] — Lodato 2018: LiRA pipeline; "genosenium" — neurons accumulate sSNVs linearly with age; CS/XP accelerate; 3 NMF signatures (A clock-like, B DG-specific, C repair-deficient).
- [[10-Summaries/miller-2022-nature]] — Miller 2022: 319 neurons from AD/control PFC + hippocampus; AD-specific excess sSNVs; oxidative-damage Signature C; transcription-coupled NER bias.
- [[10-Summaries/coorens-2021-nature]] — Coorens 2021: 511 LCM-WGS samples from 3 adults; asymmetric zygote contribution (60:40–93:7); 301-crypt patches; spatial embryonic patterning.
- [[10-Summaries/lee-six-2018-nature]] — Lee-Six 2018: 140 HSPC colonies from one 59yo man; HSC pool size 50K–200K; first in-vivo human HSC population estimate (Sanger).
- [[10-Summaries/cagan-2022-nature]] — Cagan 2022: 208 intestinal crypts across 16 mammalian species; mutation rate × lifespan = constant end-of-life burden; resolves Peto's paradox direction (Sanger).
- [[10-Summaries/mckenna-2016-science]] — McKenna 2016 **GESTALT**: founding CRISPR combinatorial-barcode lineage tracing; zebrafish proof-of-principle (Shendure lab).
- [[10-Summaries/kim-2018-cell]] — Kim 2018: TNBC chemoresistance — scDNA + scRNA on 20 patients; resistant genotypes pre-existing, resistant transcriptomes acquired (Navin lab).
- [[10-Summaries/frankell-2019-natgenet]] — Frankell 2019: 551-EAC bulk-cohort WGS; 77 driver genes; OCCAMS Consortium. Bulk-cohort counterpoint to single-cell cancer work.
- [[10-Summaries/falconer-2012-natmethods]] — Falconer 2012 **Strand-seq**: founding directional-DNA single-cell method; SCE at 23bp resolution; structural-variant axis (Lansdorp lab).
- [[10-Summaries/cusanovich-2015-science]] — Cusanovich 2015 **sci-ATAC-seq**: combinatorial-indexing scATAC-seq; first plate-based (non-droplet) scATAC method (Shendure lab).
- [[10-Summaries/rotem-2015-natbiotech]] — Rotem 2015 **Drop-ChIP**: founding scChIP-seq method via microfluidic droplets; chromatin-state subpopulations in mES (Bernstein lab).
- [[10-Summaries/schubeler-2015-nature]] — Schübeler 2015: canonical DNA-methylation function review; methylation as consequence rather than instruction of regulatory state.
- [[10-Summaries/nam-2022-natgenet]] — Nam 2022: GoT + scMethylome on DNMT3A-R882 clonal hematopoiesis; PRC2-target hypomethylation as mechanistic link (Landau lab).
- [[10-Summaries/doughty-2024-nature]] — Doughty 2024: single-molecule footprinting on engineered enhancer-promoter constructs; TF cooperativity emerges from nucleosome eviction by activation domains (Greenleaf/Bintu).
- [[10-Summaries/lee-2019-natmethods]] — Lee 2019 **sn-m3C-seq**: founding joint single-nucleus methylome + 3C; 4,238 human PFC nuclei; 14 cortical cell types (Ecker / Dixon labs). High-priority §3.5 anchor.
- [[10-Summaries/macaulay-2014-plosgenet]] — Macaulay & Voet 2014: scWGA methods review; canonical pre-PTA-era reference.
- [[10-Summaries/derop-2024-natbiotech]] — De Rop 2024: **PUMATAC** + systematic benchmarking of 8 scATAC-seq protocols across 47 experiments (Aerts + Heyn labs).
- [[10-Summaries/lahnemann-2021-natcomm]] — Lähnemann 2021 **ProSolo**: joint single-cell + bulk SNV caller with explicit FDR control for MDA data.
- [[10-Summaries/yuan-2022-natmethods]] — Yuan & Kelley 2022 **scBasset**: sequence-based CNN for scATAC; auROC 0.73–0.76 on held-out peaks.
- [[10-Summaries/zafar-2016-natmethods]] — Zafar 2016 **Monovar**: first single-cell-aware SNV caller (Navin / Chen / Nakhleh labs).
- [[10-Summaries/zafar-2017-genomebiol]] — Zafar 2017 **SiFit**: finite-sites tumor phylogeny inference from scDNA-seq.
- [[10-Summaries/cui-2024-natmethods]] — Cui 2024 **scGPT**: transformer-based single-cell foundation model pretrained on 33M cells.
- [[10-Summaries/vijg-2020-cell]] — Vijg & Dong 2020: somatic mutation × aging Cell Perspective; LOY framing.
- [[10-Summaries/gong-2021-genomebiol]] — Gong 2021 **Cobolt**: multimodal VAE for joint + single-modality scRNA + scATAC integration.
- [[10-Summaries/bersaglieri-2019-cells]] — Bersaglieri 2019: nucleolar genome organization review; NAD/heterochromatin compartment.
- [[10-Summaries/tan-2018-science]] — Tan 2018 **Dip-C**: haplotype-resolved diploid single-cell 3D genome; ~1M contacts/cell via META; 96% imputation accuracy (Xie lab).
- [[10-Summaries/smallwood-2014-natmethods]] — Smallwood 2014 **scBS-seq**: founding genome-wide single-cell bisulfite method; 48.4% CpGs per cell (Reik/Kelsey labs).
- [[10-Summaries/gonzalez-pena-2021-pnas]] — Gonzalez-Pena 2021 **PTA**: primary template-directed amplification; >95% genome coverage uniformly; current scWGA SOTA (Gawad lab).
- [[10-Summaries/zhao-2022-nature]] — Zhao 2022 **slide-DNA-seq**: spatial scDNA-seq in tissues; clone-specific CNV mapped in space; cancer (Chen/Buenrostro labs).
- [[10-Summaries/pott-2017-elife]] — Pott 2017 **scNOMe-seq**: single-cell joint methylation + accessibility + nucleosome phasing via GpC-MTase footprinting.
- [[10-Summaries/angermueller-2017-genomebiol]] — Angermueller 2017 **DeepCpG**: deep-learning imputation of single-cell methylation; CpG + DNA + Joint modules (Stegle/Reik labs).
- [[10-Summaries/garvin-2015-natmethods]] — Garvin 2015 **Ginkgo**: web platform for single-cell CNV analysis (Wigler/Schatz labs).
- [[10-Summaries/cao-2018-science]] — Cao 2018 **sci-CAR**: founding joint scATAC + scRNA via combinatorial indexing; A549 + adult mouse kidney (Shendure lab).
- [[10-Summaries/lim-2020-cancercell]] — Lim/Lin/Navin 2020: cancer + single-cell genomics review; technology landscape + clinical translation (Navin lab).
- [[10-Summaries/nishioka-2019-molpsych]] — Nishioka 2019: brain somatic mutations × psychiatric research review (Iwamoto/Kato, RIKEN).
- [[10-Summaries/chen-2025-methyltree]] — Chen 2025 **MethylTree**: methylation-epimutation lineage tracing from sparse scBS-seq; ~100% accuracy at 5% coverage (Wang lab, Westlake).

### Single-cell chromatin profiling (ultra-low-input)

- [[10-Summaries/sarah-2019-cell]] — Hainer 2019 *Cell*: uliCUT&RUN profiles TFs (CTCF, OCT4, SOX2, NANOG, BRG1) from 10–50 cells, single cells, and blastocysts.
- [[10-Summaries/marek-2021-naturebiotechnology]] — Bartosovic 2021: scCUT&Tag in mouse CNS via 10x droplet platform.
- [[10-Summaries/marek-2023-naturebiotechnology]] — Bartosovic 2023: nano-CT, three-modality (ATAC + 2 histone marks) per nucleus via nanobody-Tn5 fusions.

### scWGA chemistry foundational papers (§3.1)

- [[10-Summaries/chenghang-2012-science]] — Zong 2012 *Science*: MALBAC foundational paper (Xie lab); 93% genome coverage / 76% SNV detection from one SW480 cell.
- [[10-Summaries/chongyi-2017-science]] — Chen 2017 *Science*: LIANTI (Xie lab); linear amplification via Tn5+T7, 97% coverage, 17% ADO, micro-CNV detection.

### Single-cell methylome foundational + atlas-scale (§3.3)

- [[10-Summaries/hongshan-2013-genomeresearch]] — Guo/Tang 2013: scRRBS, foundational single-cell methylome method.
- [[10-Summaries/chongyuan-2018-naturecommunications]] — Luo/Ecker 2018: snmC-seq2 — improved chemistry behind BICCN mouse brain atlas.
- [[10-Summaries/liu-2023-nature]] — Liu/Ecker 2023: snmC-seq3 + snm3C-seq whole-mouse-brain atlas; 301K methylomes + 176K joint methylome+3D; 4,673 cell groups; 2.6M DMRs.
- [[10-Summaries/argelaguet-2019-nature]] — Argelaguet 2019: scNMT-seq applied to mouse gastrulation; MOFA decomposition; asymmetric epigenetic logic of mesendoderm vs ectoderm.
- [[10-Summaries/scherer-2025-nature]] — Scherer/Rodríguez-Fraticelli/Velten 2025: EPI-Clone (scTAM-seq); transgene-free methylation-based lineage tracing; static vs dynamic CpGs; 230K cells across mouse + human hematopoiesis.

### Joint-assay (further primary methods, §4.6)

- [[10-Summaries/caleb-2021-naturebiotechnology]] — Lareau 2021: mtscATAC-seq, mtDNA genotyping + chromatin per cell at thousands of cells.
- [[10-Summaries/cortes-lopez-2023-cellstemcell]] — Cortés-López 2023: **GoT-Splice** — four-modality joint assay (genotype + short-read scRNA + long-read isoform + CITE-seq protein); SF3B1-mutant MDS / clonal hematopoiesis.

### Lineage tracing (epigenetic clock, §4.5)

- [[10-Summaries/federico-2019-nature]] — Gaiti 2019 *Nature*: epimutation as molecular clock in CLL; 2,652 cells; SF3B1 subclone reconstruction (Landau lab).

### Duplex sequencing (additional methods)

- [[10-Summaries/federico-2021-nature]] — Abascal 2021 *Nature*: NanoSeq; <5 errors/billion bp; post-mitotic neurons accumulate mutations at constant rate (Sanger).

### Structural variant single-cell analysis

- [[10-Summaries/hyobin-2023-naturebiotechnology]] — Jeong 2023 *Nat Biotechnol*: scNOVA — Strand-seq + haplotype-aware nucleosome occupancy for SV functional analysis (Korbel lab); CLL and T-ALL clinical applications.

### Computational tools (§4.3)

- [[10-Summaries/jeffrey-2021-naturegenetics]] — Granja 2021: ArchR scATAC analysis software, 1.2M cells in 8h (Greenleaf lab).
- [[10-Summaries/stuart-2021-natmethods]] — Stuart/Satija 2021: **Signac** — Seurat-compatible single-cell chromatin toolkit; ChromatinAssay class; scales to 700K cells.
- [[10-Summaries/luquette-2019-natcomm]] — Luquette/Park 2019: **SCAN-SNV** — spatial allele-balance model for MDA single-cell SNV calling; >3× FDR reduction vs Monovar/SCcaller.

### Gap-closing methods (synthesis-note anchors, 2025)

- [[10-Summaries/andrea-2025-biorxiv]] — **Kriz/Walsh/Lee 2025 *bioRxiv* (preprint)**: **Duplex-Multiome** — duplex consensus + snATAC + snRNA-seq in the same nucleus; 51,400 brain nuclei; **first joint genome-wide SNV + chromatin + RNA at single-nucleus scale**. Closes the central methodological gap articulated in [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]].

### DNA methylation methods (single-cell + joint)

- [[10-Summaries/sctem-seq-single-cell-analysis-of-transposable-element-methylation-to-link-global-epigenetic-heterogeneity-with-transcriptional-programs]] — Hunt/Lee 2022: scTEM-seq (SINE Alu surrogate for global methylation).
- [[10-Summaries/simultaneous-single-cell-analysis-of-5mc-and-5hmc-with-simple-seq]] — Bai/Yi 2024: SIMPLE-seq joint 5mC+5hmC.
- [[10-Summaries/high-throughput-single-cell-dna-methylation-and-chromatin-accessibility-co-profiling-with-splicool-seq]] — Shen/Fan 2026: SpliCOOL-seq methylation + accessibility.
- [[10-Summaries/sequencing-dna-methylation-and-hydroxymethylation-at-co-occurring-chromatin-features]] — Tavares/Balasubramanian 2026: 6-base-CUT&Tag (5mC + 5hmC at histone marks).
- [[10-Summaries/single-cell-multi-omic-detection-of-dna-methylation-and-histone-modifications-reconstructs-the-dynamics-of-epigenomic-maintenance]] — Geisenberger/van Oudenaarden 2025: scEpi²-seq histone+5mC.

### Single-cell ATAC-seq tooling

- [[10-Summaries/chromvar-inferring-transcription-factor-associated-accessibility-from-single-cell-epigenomic-data]] — Schep/Greenleaf 2017: chromVAR TF motif aggregation.
- [[10-Summaries/cistopic-cis-regulatory-topic-modeling-on-single-cell-atac-seq-data]] — Bravo/Aerts 2019: cisTopic LDA topic modeling.
- [[10-Summaries/comprehensive-analysis-of-single-cell-atac-seq-data-with-snapatac]] — Fang/Ren 2021: SnapATAC peak-free clustering to 1M cells.
- [[10-Summaries/episcanpy-integrated-single-cell-epigenomic-analysis]] — Danese/Theis 2021: EpiScanpy scanpy-based unified framework.
- [[10-Summaries/unsupervised-clustering-and-epigenetic-classification-of-single-cells]] — Zamanighomi/Wong 2018: scABC weighted k-medoids.
- [[10-Summaries/high-throughput-chromatin-accessibility-profiling-at-single-cell-resolution]] — Mezger/Greenleaf 2018: µATAC-seq on ICELL8 nanowell.
- [[10-Summaries/scatac-seq-generates-more-accurate-and-complete-regulatory-maps-than-bulk-atac-seq]] — Gur/Hughes 2025: pseudo-bulk scATAC vs bulk ATAC comparison.

### Histone modifications (single-cell + prediction)

- [[10-Summaries/single-cell-chromatin-immunocleavage-sequencing-scchic-seq-to-profile-histone-modification]] — Ku/Zhao 2019: scChIC-seq.
- [[10-Summaries/scchix-seq-infers-dynamic-relationships-between-histone-modifications-in-single-cells]] — Yeung/van Oudenaarden 2023: scChIX-seq two-mark deconvolution.
- [[10-Summaries/scalable-single-cell-profiling-of-chromatin-modifications-with-scicut-tag]] — Janssens/Henikoff 2023: sciCUT&Tag at 40k cells/chip.
- [[10-Summaries/deephistone-a-deep-learning-approach-to-predicting-histone-modifications]] — Yin/Jiang 2019: CNN prediction of 7 histone marks.

### 3D genome (single-cell)

- [[10-Summaries/harmonizing-single-cell-3d-genome-data-with-stark-and-scnucleome]] — Jiang/Wu 2026: STARK unified pipeline + scNucleome atlas.

### Long-read chromatin / methylation methods

- [[10-Summaries/direct-transposition-of-native-dna-for-sensitive-multimodal-single-molecule-sequencing]] — Nanda/Ramani 2024: SMRT-Tag and SAMOSA-Tag (PacBio low-input).
- [[10-Summaries/single-molecule-targeted-accessibility-and-methylation-sequencing-of-centromeres-telomeres-and-rdnas-in-arabidopsis]] — Mo/Zhai 2023: STAM-seq plant HRR epigenomics.

### Batch 12 founding-method + tools (2026-05-13)

- [[10-Summaries/nagano-2013-nature]] — Nagano et al. 2013: founding single-cell Hi-C.
- [[10-Summaries/schmitt-2012-pnas]] — Schmitt/Loeb 2012: founding Duplex Sequencing.
- [[10-Summaries/ma-2020-cell]] — Ma/Buenrostro 2020: SHARE-seq joint scATAC+scRNA.
- [[10-Summaries/jin-2015-nature]] — Jin/Zhao 2015: scDNase-seq founding paper.
- [[10-Summaries/clark-2018-scnmt]] — Clark/Reik 2018: scNMT-seq founding triple-omics.
- [[10-Summaries/ashuach-2023-multivi]] — Ashuach/Yosef 2023: MultiVI deep generative multimodal integration.
- [[10-Summaries/zhang-2024-snapatac2]] — Zhang/Ren 2024: SnapATAC2 scalable single-cell omics tool.
- [[10-Summaries/shipony-2020-smac]] — Shipony/Greenleaf 2020: SMAC-seq single-molecule accessibility.
- [[10-Summaries/miller-2022-maester]] — Miller/van Galen 2022: MAESTER mtDNA from scRNA-seq.
- [[10-Summaries/dou-2020-mosaicforecast]] — Dou/Park 2020: MosaicForecast read-phasing mosaic caller.
- [[10-Summaries/dou-2023-monopogen]] — Dou/Chen 2024: Monopogen LD-aware SNV caller from any single-cell modality.
- [[10-Summaries/ha-2023-natmethods]] — Ha/Kim 2023: comprehensive mosaic-variant-caller benchmark.

### Batch 13 founding methods + cancer + computational (2026-05-13)

- [[10-Summaries/debourcy-2014-plosone]] — de Bourcy/Quake 2014: quantitative WGA-chemistry benchmark.
- [[10-Summaries/buenrostro-2015-nature]] — Buenrostro/Greenleaf 2015: founding Fluidigm scATAC-seq + regulatory variation.
- [[10-Summaries/sanders-2020-sctrip]] — Sanders/Korbel 2020: scTRIP Strand-seq SV calling.
- [[10-Summaries/zaccaria-2021-chisel]] — Zaccaria/Raphael 2021: CHISEL allele/haplotype-specific CNV.
- [[10-Summaries/yang-2023-deepmosaic]] — Yang/Gleeson 2023: DeepMosaic CNN mosaic-variant caller.
- [[10-Summaries/xiao-2025-epitrace]] — Xiao/Zhang 2025: EpiTrace clock-like ATAC mitotic age.
- [[10-Summaries/cao-2022-glue]] — Cao/Gao 2022: GLUE graph-linked unpaired multi-omics integration.
- [[10-Summaries/lee-2020-nanonome]] — Lee/Timp 2020: nanoNOMe nanopore joint methylation+accessibility.
- [[10-Summaries/dong-2017-sccaller]] — Dong/Vijg 2017: SCcaller + SCMDA scWGS variant caller.
- [[10-Summaries/bae-2023-codec]] — Bae/Adalsteinsson 2023: CODEC concatenated single-duplex sequencing.
- [[10-Summaries/pellegrino-2018-tapestri]] — Pellegrino/Eastburn 2018: founding Tapestri droplet scDNA in AML.
- [[10-Summaries/kaufmann-2022-medicc2]] — Kaufmann/Schwarz 2022: MEDICC2 WGD-aware CN phylogeny.

### Batch 14 computational tools + tumor phylogeny + mosaic chromatin (2026-05-13)

- [[10-Summaries/huang-2017-mosaichunter]] — Huang/Wei 2017: founding unpaired mosaic-SNM caller.
- [[10-Summaries/desouza-2020-epiclomal]] — de Souza/Shah 2020: Epiclomal probabilistic methylation clustering.
- [[10-Summaries/kapourani-2019-melissa]] — Kapourani/Sanguinetti 2019: Melissa Bayesian methylation imputation.
- [[10-Summaries/kapourani-2021-scmet]] — Kapourani/Vallejos 2021: scMET methylation-heterogeneity quantification.
- [[10-Summaries/peter-2024-brain-fiberseq]] — Peter/Akbarian 2024: Fiber-seq adapted for FACS-sorted human brain nuclei.
- [[10-Summaries/satas-2020-scarlet]] — Satas/Raphael 2020: SCARLET phylogeny with CN-constrained SNV losses.
- [[10-Summaries/jahn-2016-scite]] — Jahn/Beerenwinkel 2016: SCITE founding tumor-phylogeny inference.
- [[10-Summaries/bohaczuk-2024-targeted-fiberseq]] — Bohaczuk/Stergachis 2024: targeted Fiber-seq for mosaic-variant chromatin impact.
- [[10-Summaries/mallory-2020-cna-review]] — Mallory/Nakhleh 2020: scDNA CNA-detection methods review.
- [[10-Summaries/hsieh-2026-mtdna-mosaicism]] — Hsieh/Ludwig 2026: scmtMPM + scwMSS mtDNA mosaicism metrics on POLG line.
- [[10-Summaries/wang-2019-mesmlr]] — Wang/Au 2019: MeSMLR-seq foundational single-molecule Nanopore footprinting in yeast.

### Batch 15 bioinformatics tools + reviews + benchmarks (2026-05-13)

- [[10-Summaries/lu-2024-cnaphylogeny-review]] — Lu 2025: CNA-based cancer phylogenetic-inference review.
- [[10-Summaries/krueger-2011-bismark]] — Krueger/Andrews 2011: founding Bismark bisulfite aligner + methylation caller.
- [[10-Summaries/garrison-2023-bsmn-data]] — Garrison/BSMN 2023: BSMN consortium genomic-data resources descriptor.
- [[10-Summaries/valecha-2022-scsnv-review]] — Valecha/Posada 2022: scDNA SNV-calling review.
- [[10-Summaries/luo-2024-scatac-benchmark]] — Luo/von Meyenn 2024: scATAC computational-methods benchmark.
- [[10-Summaries/iqbal-2023-methylome-review]] — Iqbal/Zhou 2023: scDNA methylome computational-methods review.
- [[10-Summaries/sun-2025-scmitomut]] — Sun/Perié 2025: scMitoMut beta-binomial mtDNA calling.
- [[10-Summaries/xiao-2024-multiomics-benchmark]] — Xiao/Wei 2024: multi-omics integration benchmark (12 methods).
- [[10-Summaries/zafar-2016-monovar]] — Zafar/Nakhleh 2016: Monovar founding scDNA SNV caller.
- [[10-Summaries/zafar-2017-sifit]] — Zafar/Nakhleh 2017: SiFit finite-sites tumor phylogeny.
- [[10-Summaries/gong-2021-cobolt]] — Gong/Purdom 2021: Cobolt MVAE multimodal integration.

### Batch 16 multiome + scATAC founding + cancer + brain mosaicism (2026-05-13)

- [[10-Summaries/kriz-2025-duplex-multiome]] — Kriz/Walsh/Lee 2025: Duplex-Multiome strand-tagged sSNV + snATAC + snRNA in brain.
- [[10-Summaries/rotem-2015-drop-chip]] — Rotem/Bernstein/Weitz 2015: Drop-ChIP founding single-cell ChIP-seq.
- [[10-Summaries/doughty-2024-smf-tf]] — Doughty/Greenleaf/Bintu 2024: SMF links TF binding to gene expression.
- [[10-Summaries/kim-2018-tnbc-chemoresistance]] — Kim/Navin 2018: TNBC chemoresistance scDNA + scRNA longitudinal.
- [[10-Summaries/luo-2018-snmc-seq2]] — Luo/Ecker 2018: snmC-seq2 improved scWGBS protocol.
- [[10-Summaries/frankell-2019-eac-landscape]] — Frankell/Fitzgerald 2019: OCCAMS 551-EAC driver landscape.
- [[10-Summaries/cusanovich-2015-sciatac]] — Cusanovich/Shendure 2015: sci-ATAC-seq founding combinatorial-indexing scATAC.
- [[10-Summaries/schubeler-2015-methylation-review]] — Schübeler 2015: review of DNA methylation function/information content.
- [[10-Summaries/mukamel-2025-aneuploidy-brain]] — Mukamel/Ecker 2025: cell-type-specific chr16 trisomy in mouse brain from snmC-seq.
- [[10-Summaries/yuan-2022-scbasset]] — Yuan/Kelley 2022: scBasset deep-CNN sequence model for scATAC.
- [[10-Summaries/liu-2023-mouse-brain-methylome-3d]] — Liu/Ecker 2023: 301k-methylome + 176k snm3C-seq adult mouse brain atlas.
- [[10-Summaries/lee-six-2018-hsc-dynamics]] — Lee-Six/Campbell 2018: HSC dynamics from 140-colony WGS phylogeny.

### Batch 17 multimodal founding + reviews + GoT family + DAF-seq (2026-05-13)

- [[10-Summaries/macaulay-2015-gt-seq]] — Macaulay/Voet 2015: G&T-seq founding parallel scDNA+scRNA.
- [[10-Summaries/argelaguet-2020-mofa-plus]] — Argelaguet/Stegle 2020: MOFA+ scalable multimodal factor analysis.
- [[10-Summaries/baysoy-2023-multiomics-landscape]] — Baysoy/Fan/Satija 2023: NRMCB review of single-cell multi-omics landscape.
- [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — Shao/Walsh 2025: NRG review of scDNA-seq for somatic mosaicism (competitor review).
- [[10-Summaries/fu-2025-longread-methylation]] — Fu/Timp/Sedlazeck 2025: long-read methylation computational analysis review.
- [[10-Summaries/heumos-2023-best-practices]] — Heumos/Theis 2023: NRG best-practices for single-cell analysis across modalities.
- [[10-Summaries/vandereyken-2023-scmultiomics-review]] — Vandereyken/Voet 2023: NRG review of single-cell + spatial multi-omics methods.
- [[10-Summaries/nam-2019-got]] — Nam/Landau 2019: GoT founding genotyping + scRNA-seq.
- [[10-Summaries/izzo-2024-got-cha]] — Izzo/Landau 2024: GoT-ChA genotyping + scATAC-seq.
- [[10-Summaries/swanson-2025-daf-seq]] — Swanson/Stergachis 2025: DAF-seq deaminase-based single-cell diploid chromatin fiber sequencing.
- [[10-Summaries/gawad-2016-scgenome-review]] — Gawad/Quake 2016: NRG scDNA-seq state-of-the-science review.

### Batch 18 founding scDNA + SMF expansion + reviews + triple-omics (2026-05-13)

- [[10-Summaries/evrony-2021-scDNA-applications-review]] — Evrony/Hinch/Luo 2021: ARGHG scDNA-seq applications review (fidelity/co-presence/phenotypic-association framework).
- [[10-Summaries/campbell-2015-mosaicism-review]] — Campbell/Lupski 2015: TiG mosaicism review focused on developmental timing and transmission.
- [[10-Summaries/forsberg-2017-mosaicism-review]] — Forsberg/Gisselsson/Dumanski 2017: NRG post-zygotic variation review + mLOY.
- [[10-Summaries/navin-2011-sns-tumor-evolution]] — Navin/Wigler 2011: founding single-nucleus sequencing of tumor evolution.
- [[10-Summaries/altemose-2022-dimelo-seq]] — Altemose/Streets/Straight 2022: DiMeLo-seq long-read antibody-directed protein-DNA mapping.
- [[10-Summaries/abdulhay-2020-samosa]] — Abdulhay/Ramani 2020: SAMOSA single-molecule oligonucleosome footprinting.
- [[10-Summaries/ghorbani-2019-comp-epigenetics]] — Ghorbani 2019: generic computational epigenetics overview (low-priority).
- [[10-Summaries/wang-2020-scope]] — Wang/Jiang 2020: SCOPE scDNA-seq CNV normalization + ploidy estimation.
- [[10-Summaries/he-2024-foodie]] — He/Xie 2024: FOODIE deaminase-based single-cell/single-molecule TF footprinting.
- [[10-Summaries/nichols-2022-scimet-v2]] — Nichols/Adey 2022: sciMETv2 high-throughput scDNA methylation via combinatorial indexing.
- [[10-Summaries/klemm-2019-chromatin-accessibility-review]] — Klemm/Greenleaf 2019: NRG chromatin accessibility review.
- [[10-Summaries/dey-2015-dr-seq]] — Dey/van Oudenaarden 2015: DR-seq founding no-separation parallel scDNA+scRNA.
- [[10-Summaries/hou-2016-sctrio-seq]] — Hou/Tang 2016: scTrio-seq founding single-cell triple-omics (genome+methylome+transcriptome).
- [[10-Summaries/smith-2013-methylation-development]] — Smith/Meissner 2013: NRG DNA methylation in mammalian development review.

### Batch 19 markdown sources (31 papers, 2026-05-13)

- [[10-Summaries/luquette-2025-smaht-pta]] — Luquette/Coorens/Walsh/Park/Abyzov 2025: SMaHT PTA-based scDNA on lung+colon 102 nuclei.
- [[10-Summaries/nandi-2025-udseq]] — Nandi/Alexandrov 2025: UDSeq universal duplex sequencing protocol.
- [[10-Summaries/tu-2021-scout]] — Tu/Xie 2021: SCOUT single-cell genotyper using local genome territory.
- [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] — Zhang/Coorens 2025: SMaHT 6-platform duplex sequencing benchmark.
- [[10-Summaries/schep-2017-chromvar]] — Schep/Greenleaf 2017: chromVAR TF-motif scATAC analysis.
- [[10-Summaries/bravo-2019-cistopic]] — Bravo González-Blas/Aerts 2019: cisTopic LDA-based scATAC clustering.
- [[10-Summaries/fang-2021-snapatac]] — Fang/Ren 2021: SnapATAC Nyström-method scATAC at million-cell scale.
- [[10-Summaries/yin-2019-deephistone]] — Yin/Jiang 2019: DeepHistone CNN-based histone-modification prediction.
- [[10-Summaries/kennedy-2014-duplex-protocol]] — Kennedy/Loeb 2014: Nature Protocols duplex sequencing.
- [[10-Summaries/nanda-2024-smrt-tag]] — Nanda/Ramani 2024: SMRT-Tag and SAMOSA-Tag low-input PacBio.
- [[10-Summaries/kim-2017-dna-methylation-memory]] — Kim/Costello 2017: DNA methylation as cellular memory review.
- [[10-Summaries/danese-2021-episcanpy]] — Danese/Theis 2021: EpiScanpy unified scATAC + scDNA-methylation analysis.
- [[10-Summaries/bizzotto-2022-brain-mosaicism-nrn]] — Bizzotto/Walsh 2022: NRN brain mosaicism review.
- [[10-Summaries/jiang-2026-stark-scnucleome]] — Jiang/Wu 2026: STARK + scNucleome sc3DG-seq benchmark.
- [[10-Summaries/mezger-2018-uatac]] — Mezger/Klemm/Greenleaf 2018: µATAC-seq nanowell-based scATAC.
- [[10-Summaries/glynos-2023-mtdna-mosaicism]] — Glynos/Chinnery 2023: high-throughput single-cell mtDNA heteroplasmy.
- [[10-Summaries/shen-2025-splicool-seq]] — Shen/Fan 2025: SpliCOOL-seq scDNA methylation + accessibility.
- [[10-Summaries/liu-2025-somagauss-lscc]] — Liu 2025: SomaGauss-SV nanopore somatic SV in LSCC.
- [[10-Summaries/hong-2025-sc3d-genome-review]] — Hong/Dao 2025: sc3D-genome review.
- [[10-Summaries/liu-2025-longread-epigenome-review]] — Liu/Conesa 2025: long-read epigenome review.
- [[10-Summaries/janssens-2023-scicut-tag]] — Janssens/Henikoff 2023: sciCUT&Tag combinatorial-indexing chromatin profiling.
- [[10-Summaries/gur-2025-scatac-vs-bulk]] — Gur/Hughes 2025: scATAC vs bulk ATAC comparison.
- [[10-Summaries/yeung-2023-scchix-seq]] — Yeung/van Oudenaarden 2023: scChIX-seq joint two-histone-mark single-cell.
- [[10-Summaries/hunt-2022-sctem-seq]] — Hunt/Lee 2022: scTEM-seq transposable element methylation as global proxy.
- [[10-Summaries/tavares-2026-6base-cuttag]] — Tavares/Balasubramanian 2026: 6-base-CUT&Tag 5mC + 5hmC at histone features.
- [[10-Summaries/bai-2024-simple-seq]] — Bai/Yi 2024: SIMPLE-seq single-cell joint 5mC + 5hmC.
- [[10-Summaries/ku-2019-scchic-seq]] — Ku/Zhao 2019: scChIC-seq MNase-based single-cell histone modification.
- [[10-Summaries/kousi-2022-ad-mosaicism]] — Kousi/Kellis 2022: Alzheimer cell-type-specific scDNA mosaicism.
- [[10-Summaries/geisenberger-2025-scepi2-seq]] — Geisenberger/van Oudenaarden 2025: scEpi²-seq joint histone + methylation.
- [[10-Summaries/mo-2023-stam-seq]] — Mo/Zhai 2023: STAM-seq nanopore adaptive-sampling Arabidopsis HRR.
- [[10-Summaries/zamanighomi-2018-scabc]] — Zamanighomi/Wong 2018: scABC weighted K-medoids scATAC clustering.

### Wiki seed

- [[10-Summaries/example-llm-wiki]] — paraphrase of Andrej Karpathy's LLM Wiki proposal.

## Entities

### scDNA-seq, mosaicism, lineage tracing

- [[20-Entities/diane-d-shao]] — Boston Children's; keystone 2025 review first author.
- [[20-Entities/christopher-walsh]] — Walsh lab; human brain mosaicism program (SMaHT lead).
- [[20-Entities/sara-bizzotto]] — Walsh lab postdoc; brain mosaicism review first author.
- [[20-Entities/charles-gawad]] — St Jude; foundational 2016 review first author.
- [[20-Entities/stephen-quake]] — Stanford; microfluidic single-cell genomics pioneer.
- [[20-Entities/gilad-evrony]] — NYU; applications-framework architect; HiDEF-seq.
- [[20-Entities/lars-forsberg]] — Uppsala; mosaicism in health and disease.
- [[20-Entities/james-lupski]] — Baylor; clinical genetics of mosaicism.
- [[20-Entities/lovelace-luquette]] — Park lab; SMaHT comprehensive scDNA-seq paper.
- [[20-Entities/alexej-abyzov]] — Mayo Clinic; SMaHT scDNA-seq.
- [[20-Entities/peter-park]] — HMS; SMaHT bioinformatics.
- [[20-Entities/flora-vaccarino]] — Yale; SMaHT co-senior.
- [[20-Entities/smaht-network]] — NIH consortium for somatic mosaicism atlas.

### Duplex sequencing

- [[20-Entities/lawrence-loeb]] — UW; original Duplex Sequencing inventor.
- [[20-Entities/scott-kennedy]] — first author of the founding DS paper.
- [[20-Entities/ludmil-alexandrov]] — UCSD; mutational signatures; UDSeq.
- [[20-Entities/joseph-gleeson]] — UCSD; brain mosaicism (UDSeq co-author).
- [[20-Entities/tim-coorens]] — Sanger/Broad; SMaHT duplex-seq benchmark co-lead.

### mtDNA heteroplasmy

- [[20-Entities/patrick-chinnery]] — Cambridge; single-cell mtDNA biology.
- [[20-Entities/james-stewart]] — Max Planck; pathogenic mtDNA mouse models.

### Neurodegeneration

- [[20-Entities/manolis-kellis]] — MIT/Broad; AD single-cell mosaicism.
- [[20-Entities/li-huei-tsai]] — MIT Picower; AD biology.

### Multi-omics methods

- [[20-Entities/anna-s-nam]] — Weill Cornell; first author of GoT.
- [[20-Entities/franco-izzo]] — first author of GoT–ChA.
- [[20-Entities/dan-a-landau]] — senior author of GoT and GoT–ChA.
- [[20-Entities/landau-lab]] — NYGC/Weill Cornell group.
- [[20-Entities/thierry-voet]] — KU Leuven; G&T-seq co-developer.
- [[20-Entities/rong-fan]] — Yale; multi-omics landscape review.
- [[20-Entities/rahul-satija]] — NYGC; Seurat developer.
- [[20-Entities/fabian-theis]] — Helmholtz Munich; EpiScanpy, best practices.
- [[20-Entities/maria-colome-tatche]] — Helmholtz Munich; EpiScanpy.
- [[20-Entities/alexander-van-oudenaarden]] — Hubrecht; sortChIC, scChIX, scEpi².

### Methylation chemistry

- [[20-Entities/alexander-meissner]] — Harvard/Broad; methylation development.
- [[20-Entities/fritz-sedlazeck]] — Baylor; long-read methylation.
- [[20-Entities/winston-timp]] — Johns Hopkins; nanopore methylation.
- [[20-Entities/chun-xiao-song]] — Oxford; TAPS chemistry inventor.
- [[20-Entities/chengqi-yi]] — Peking U; SIMPLE-seq, hmC-CATCH.
- [[20-Entities/heather-lee]] — Newcastle Australia; scTEM-seq.
- [[20-Entities/xiaoying-fan]] — GIBH; SpliCOOL-seq.
- [[20-Entities/joseph-costello]] — UCSF; glioma methylation, EPICUP.
- [[20-Entities/shankar-balasubramanian]] — Cambridge / biomodal; 6-base sequencing.
- [[20-Entities/biomodal]] — biotech; evoC kit for 6-base sequencing.

### Single-cell chromatin (ATAC + histone)

- [[20-Entities/william-greenleaf]] — Stanford; ATAC-seq, chromVAR, µATAC.
- [[20-Entities/jason-buenrostro]] — Harvard; chromVAR, hematopoiesis scATAC.
- [[20-Entities/sandy-klemm]] — µATAC-seq co-developer.
- [[20-Entities/stein-aerts]] — VIB-KU Leuven; cisTopic, SCENIC.
- [[20-Entities/bing-ren]] — UCSD; SnapATAC, brain atlas.
- [[20-Entities/wing-hung-wong]] — Stanford; scABC biostatistics.
- [[20-Entities/jim-hughes]] — Oxford; Capture-C, scATAC vs bulk comparison.
- [[20-Entities/keji-zhao]] — NIH; scChIC-seq.
- [[20-Entities/steven-henikoff]] — Fred Hutch; CUT&Tag/CUT&RUN, sciCUT&Tag.
- [[20-Entities/jake-yeung]] — first author of scChIX-seq.
- [[20-Entities/rui-jiang]] — Tsinghua; DeepHistone.

### Long-read chromatin / 3D-genome

- [[20-Entities/elliott-g-swanson]] — UW; DAF-seq co-first author.
- [[20-Entities/andrew-b-stergachis]] — UW; DAF-seq senior; Fiber-seq developer.
- [[20-Entities/ana-conesa]] — CSIC; long-read epigenome review.
- [[20-Entities/vijay-ramani]] — UCSF/Gladstone; SAMOSA, SMRT-Tag, SAMOSA-Tag.
- [[20-Entities/jixian-zhai]] — SUSTech; STAM-seq plant epigenomics.
- [[20-Entities/jifeng-liu]] — head-and-neck cancer nanopore SV.
- [[20-Entities/dan-xie]] — Sichuan U; SCOUT, SomaGauss-SV.
- [[20-Entities/fuying-dao]] — sc 3D-genome review.
- [[20-Entities/hua-jun-wu]] — Peking U; STARK, scNucleome.

### Other

- [[20-Entities/andrej-karpathy]] — proposed the LLM Wiki pattern.

## Concepts

### scDNA-seq methods + variant calling

- [[30-Concepts/scdna-seq]] — umbrella for single-cell DNA sequencing.
- [[30-Concepts/scwga]] — single-cell whole-genome amplification.
- [[30-Concepts/mda]] — multiple displacement amplification (Φ29).
- [[30-Concepts/pta]] — primary template amplification; current gold standard.
- [[30-Concepts/malbac]] — hybrid PCR/isothermal scWGA.
- [[30-Concepts/dop-pcr]] — earliest PCR-based scWGA.
- [[30-Concepts/dlp-plus]] — Tn5-based high-throughput scWGA.
- [[30-Concepts/meta-cs]] — Tn5-based single-cell duplex.
- [[30-Concepts/scdna-capabilities-framework]] — Evrony fidelity/co-presence/phenotypic-association framework.
- [[30-Concepts/scout-variant-caller]] — local-territory single-cell variant caller.
- [[30-Concepts/monovar]] — multi-cell-pooled single-cell SNV caller.
- [[30-Concepts/sccaller]] — bulk-anchored single-cell SNV caller.
- [[30-Concepts/allele-dropout]] — scWGA failure mode.

### Duplex sequencing

- [[30-Concepts/duplex-sequencing]] — strand-paired single-molecule error correction.
- [[30-Concepts/umi-molecular-barcoding]] — degenerate-tag adapters.
- [[30-Concepts/mutational-signatures]] — 96-channel SBS context patterns.
- [[30-Concepts/codec]] — Broad duplex chemistry.
- [[30-Concepts/nanoseq]] — Sanger duplex chemistry.
- [[30-Concepts/hidef-seq]] — Evrony duplex chemistry.

### Multi-omic methods

- [[30-Concepts/got]] — droplet single-cell genotype + transcriptome.
- [[30-Concepts/circularization-got]] — GoT extension for distal loci.
- [[30-Concepts/got-cha]] — droplet single-cell genotype + chromatin accessibility.
- [[30-Concepts/daf-seq]] — single-molecule chromatin + DNA via deaminase footprinting.
- [[30-Concepts/fiber-seq]] — bulk single-molecule chromatin via m6A stenciling.
- [[30-Concepts/single-molecule-footprinting]] — method class.
- [[30-Concepts/dogma-seq]] — chromatin + RNA + protein.
- [[30-Concepts/cite-seq]] — scRNA + surface protein via antibody-derived tags.
- [[30-Concepts/gt-seq]] — physical-separation scDNA + scRNA (G&T-seq).
- [[30-Concepts/single-cell-multiomics]] — umbrella concept.
- [[30-Concepts/spatial-multiomics]] — spatially-resolved multi-omic methods.
- [[30-Concepts/combinatorial-indexing]] — split-pool barcoding.

### scATAC-seq + chromatin accessibility

- [[30-Concepts/atac-seq]] — Tn5-based accessibility assay.
- [[30-Concepts/scatac-seq]] — single-cell version.
- [[30-Concepts/dnase-seq]] — original DNase I accessibility assay.
- [[30-Concepts/chromatin-accessibility]] — open vs closed DNA.
- [[30-Concepts/chromatin-actuation]] — per-fiber open+bound state.
- [[30-Concepts/cis-regulatory-element]] — enhancer/promoter/insulator.
- [[30-Concepts/enhancer-states]] — active/primed/poised.
- [[30-Concepts/tn5-tagmentation]] — Tn5 cut+adapter-ligation.
- [[30-Concepts/chromvar]] — TF motif aggregation for sparse scATAC.
- [[30-Concepts/cistopic]] — LDA topic modeling for scATAC.
- [[30-Concepts/snapatac]] — peak-free 5-kb-bin Jaccard clustering.
- [[30-Concepts/episcanpy]] — scanpy-based unified epigenomics framework.
- [[30-Concepts/scabc]] — weighted k-medoids clustering.
- [[30-Concepts/micro-atac-seq]] — ICELL8-nanowell scATAC-seq.
- [[30-Concepts/transcription-factor-motif]] — PWM definition.
- [[30-Concepts/de-novo-motif-discovery]] — algorithmic motif inference.
- [[30-Concepts/pseudo-bulk]] — per-cluster aggregation of single cells.
- [[30-Concepts/scanpy]] / [[30-Concepts/anndata]] — Python scRNA framework.
- [[30-Concepts/icell8-nanowell]] — Takara 5,184-well platform.
- [[30-Concepts/jaccard-similarity]] / [[30-Concepts/nystrom-method]] / [[30-Concepts/k-medoids]] / [[30-Concepts/latent-dirichlet-allocation]] — algorithm primitives.

### Histone modifications

- [[30-Concepts/histone-modifications]] — H3K4me3 / H3K4me1 / H3K27ac / H3K27me3 / H3K9me3 / H3K36me3.
- [[30-Concepts/chip-seq]] — bulk ChIP-seq.
- [[30-Concepts/cut-and-run]] — antibody-tethered MNase + release.
- [[30-Concepts/cut-and-tag]] — antibody-tethered pA-Tn5.
- [[30-Concepts/chic-seq]] — original chromatin immunocleavage.
- [[30-Concepts/sortchic]] — FACS-integrated single-cell ChIC.
- [[30-Concepts/scchic-seq]] — single-cell ChIC.
- [[30-Concepts/scchix-seq]] — two histone marks per cell via deconvolution.
- [[30-Concepts/scicut-tag]] — combinatorial-indexing CUT&Tag.
- [[30-Concepts/multi-tag]] — multi-epitope CUT&Tag.
- [[30-Concepts/scepi2-seq]] — histone + 5mC + nucleosome positioning.
- [[30-Concepts/6-base-cut-and-tag]] — histone + 5mC + 5hmC per fragment.
- [[30-Concepts/chromatin-velocity]] — multi-mark single-cell dynamics.
- [[30-Concepts/deephistone]] — CNN prediction of histone marks.
- [[30-Concepts/convolutional-neural-network]] — CNN basics.
- [[30-Concepts/replication-timing]] — temporal chromatin organization.

### DNA methylation

- [[30-Concepts/dna-methylation]] — 5mC and related modifications.
- [[30-Concepts/cpg-island]] — unmethylated promoter features.
- [[30-Concepts/dnmt]] — DNA methyltransferase enzymes.
- [[30-Concepts/tet-enzymes]] — active demethylation pathway.
- [[30-Concepts/uhrf1]] — DNMT1 maintenance cofactor.
- [[30-Concepts/5hmc]] — oxidative intermediate / stable mark.
- [[30-Concepts/bisulfite-sequencing]] — standard short-read methylation assay.
- [[30-Concepts/scbs-seq]] — single-cell bisulfite sequencing.
- [[30-Concepts/taps]] — TET + borane bisulfite-free 5mC chemistry.
- [[30-Concepts/nome-seq]] — GpC methyltransferase for accessibility.
- [[30-Concepts/sctem-seq]] — SINE Alu single-cell global methylation.
- [[30-Concepts/simple-seq]] — single-cell 5mC + 5hmC joint.
- [[30-Concepts/splicool-seq]] — single-cell 5mC + accessibility.
- [[30-Concepts/transposable-elements]] — TEs silenced by methylation.
- [[30-Concepts/viral-mimicry]] — TE expression triggers innate immunity.
- [[30-Concepts/decitabine]] — DNMT-trapping hypomethylating agent.
- [[30-Concepts/epigenetic-memory]] — heritable methylation states.
- [[30-Concepts/epigenetic-aging]] — methylation clocks (Horvath, scAge).
- [[30-Concepts/cancer-of-unknown-primary]] — EPICUP methylation classifier.

### Long-read sequencing

- [[30-Concepts/long-read-sequencing]] — PacBio + ONT direct modification detection.
- [[30-Concepts/oxford-nanopore]] — ONT nanopore platform.
- [[30-Concepts/pacbio]] — PacBio SMRT platform.
- [[30-Concepts/samosa]] — EcoGII + PacBio chromatin (bulk).
- [[30-Concepts/samosa-tag]] — SAMOSA + tagmentation (low-input).
- [[30-Concepts/smrt-tag]] — low-input PacBio library prep.
- [[30-Concepts/stam-seq]] — plant nanopore chromatin + methylation.
- [[30-Concepts/nanopore-adaptive-sampling]] — real-time read selection.
- [[30-Concepts/highly-repetitive-regions]] — centromeres, telomeres, rDNAs.
- [[30-Concepts/structural-variants]] — large genomic rearrangements.
- [[30-Concepts/somagauss-sv]] — nanopore somatic SV caller.
- [[30-Concepts/allele-specific-methylation]] — phased methylation.

### 3D genome

- [[30-Concepts/3d-genome]] — nuclear chromatin organization.
- [[30-Concepts/single-cell-hi-c]] — sc3DG-seq method family.
- [[30-Concepts/topologically-associating-domain]] — TADs.
- [[30-Concepts/chromatin-compartments]] — A/B compartments.
- [[30-Concepts/sc-sprite]] — sonication-based multi-way single-cell contacts.
- [[30-Concepts/dip-c]] — diploid haplotype-phased Hi-C.
- [[30-Concepts/stark]] — unified sc3DG-seq pipeline.
- [[30-Concepts/sscce]] — single-cell structural quality metric.
- [[30-Concepts/empty-cells-algorithm]] — sc3DG-seq barcode filtering.

### Mosaicism / disease biology

- [[30-Concepts/somatic-mosaicism]] — mosaic somatic variation.
- [[30-Concepts/post-zygotic-variation]] — broader umbrella term.
- [[30-Concepts/microchimerism]] — foreign cells in host.
- [[30-Concepts/developmental-mutation-timing]] — timing→tissue-distribution geometry.
- [[30-Concepts/gonadal-mosaicism]] — germline mosaicism; recurrence risk.
- [[30-Concepts/clonal-hematopoiesis]] — mosaic HSC clones in blood.
- [[30-Concepts/lineage-tracing]] — endogenous mutations as lineage barcodes.
- [[30-Concepts/mitochondrial-heteroplasmy]] — mtDNA mosaicism in cells.
- [[30-Concepts/mitochondrial-lineage-tracing]] — mtDNA mutations as lineage barcodes.
- [[30-Concepts/kimura-distribution]] — drift-model distribution for heteroplasmy.
- [[30-Concepts/calr-mutation]] — MPN driver mutation.
- [[30-Concepts/jak2-v617f]] — most common MPN driver.
- [[30-Concepts/myeloproliferative-neoplasm]] — disease class.
- [[30-Concepts/unfolded-protein-response]] — CALR-mutation transcriptional output.
- [[30-Concepts/hematopoietic-differentiation]] — HSPC hierarchy.
- [[30-Concepts/focal-cortical-dysplasia]] — mTOR-pathway mosaic disease.
- [[30-Concepts/mtor-pathway]] — growth-signaling pathway.
- [[30-Concepts/autism-spectrum-disorder]] — mosaicism-contributing neurodevelopmental disorder.
- [[30-Concepts/alzheimers-disease]] — neurodegeneration with mosaic-mutation contribution.
- [[30-Concepts/laryngeal-squamous-cell-carcinoma]] — smoking-driven cancer.
- [[30-Concepts/lung-adenocarcinoma]] — NSCLC subtype.

### Wiki / meta

- [[30-Concepts/llm-wiki]] — LLM-as-maintainer wiki pattern.
- [[30-Concepts/three-layer-architecture]] — sources / wiki / schema.
- [[30-Concepts/compounding-artifact]] — value-compounding knowledge.
- [[30-Concepts/maintenance-asymmetry]] — humans defer cross-references; LLMs don't.
- [[30-Concepts/ingest-workflow]] — per-source procedure.

## Topics

- [[40-Topics/scdna-seq]] — single-cell DNA sequencing (umbrella).
- [[40-Topics/somatic-mosaicism]] — mosaicism biology and disease.
- [[40-Topics/whole-genome-amplification]] — scWGA methods.
- [[40-Topics/duplex-sequencing]] — ultra-accurate sequencing for low-VAF variants.
- [[40-Topics/dna-methylation]] — methylation biology and measurement.
- [[40-Topics/long-read-sequencing]] — PacBio and ONT enabling platform.
- [[40-Topics/single-cell-multiomics]] — methods measuring ≥2 modalities per cell.
- [[40-Topics/single-cell-atac-seq]] — chromatin accessibility at single-cell resolution.
- [[40-Topics/histone-modifications]] — histone-mark profiling.
- [[40-Topics/3d-genome]] — chromatin architecture.
- [[40-Topics/chromatin-architecture]] — single-cell and single-molecule chromatin.
- [[40-Topics/hematopoietic-malignancies]] — MPN and related.
- [[40-Topics/llm-tooling-patterns]] — LLM design patterns.
- [[40-Topics/knowledge-management]] — knowledge capture and refinement.

## Notes

_Empty — promote one once a query or synthesis pulls together ≥3 sources/pages._

Promising synthesis targets:
- **Single-cell duplex sequencing** — the major open methodological frontier; current methods are either single-cell (scWGA-based, loses strand identity) or duplex (bulk-only). Combining the two is the next frontier.
- **MNase-based vs Tn5-based single-cell chromatin profiling** — tradeoffs in nucleosome-positioning fidelity vs throughput.
- **Droplet-scale vs single-molecule scDNA-seq** — could pull together GoT/GoT–ChA/DAF-seq + Diane 2025 + Gilad 2021 + Charles 2016.
- **The PTA inflection point** — comparison of pre-2020 MDA-era applications with current PTA-enabled work.
- **DNA-methylation-based cancer-of-origin classifiers** — EPICUP, brain-tumor MNP, AML methylation classifiers.

## Open questions

_Tensions and gaps surfaced during ingest or lint. Resolve, then move out._

### Duplex sequencing

- **Single-cell + duplex** — duplex needs both strands; scWGA loses strand identity. Holy grail of mosaicism detection.
- Mutation-rate concordance across duplex platforms (SMaHT benchmark) — does it hold for brain, aging muscle, FFPE samples?
- UDSeq vs the SMaHT-benchmarked methods — no cross-comparison yet.

### scDNA-seq methods

- Where does scDAF-seq's per-cell ~99% coverage / ~10-cell throughput win over GoT–ChA's ~38% genotyping / 10⁵-cell throughput?
- Throughput vs depth: DLP+ (>10⁴ cells low coverage) vs PTA (384 cells, ~95% coverage). Right operating point per question?
- Why is intra-cell haplotype actuation divergence (~61%) nearly equal to inter-cell divergence (~63%)?

### Mosaicism biology

- Tissue-specific mosaic mutation rates beyond skin/intestine/brain.
- **Smoking × somatic SV** burden mechanism in head-and-neck cancer.
- Causality of cell-type-specific somatic mutation burden in AD.
- IRE1-XBP1 as a therapeutic target in CALR-mutant MPN.
- mtDNA heteroplasmy drop at P6 in mouse — mechanism unclear.

### Methylation / chromatin

- 5mC vs 5hmC functional distinction — most measurements still conflate.
- **Causal vs consequential**: does methylation-loss-driven viral mimicry require additional gating factors (e.g., SETDB1, TF availability)?
- Methylation calling accuracy benchmarking across long-read platforms.
- Single-cell long-read methylation — emerging but not routine.
- Decitabine vs azacitidine: distinct demethylation patterns, mechanistic basis unknown.

### 3D genome

- TAD/loop **causality** — drive expression or follow it?
- Per-cell 3D resolution still ~1 Mb; gap to bulk Hi-C ~kb.
- Sonication-based methods (scSPRITE) capture more contacts; will they generalize?

### Wiki

- Does flat-file + `index.md` navigation scale to ~150 pages?
- Practical contradiction-resolution policy beyond flagging.
- Measuring whether the wiki is actually compounding vs accumulating.
