---
title: Concepts
description: Definitions, methods, and theoretical ideas referenced across the wiki.
updated: 2026-05-13
---

# Concepts

Each entry links to its definition page. Grouped by domain.

## scDNA-seq methods + variant calling

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

## Duplex sequencing

- [[30-Concepts/duplex-sequencing]] — strand-paired single-molecule error correction.
- [[30-Concepts/umi-molecular-barcoding]] — degenerate-tag adapters.
- [[30-Concepts/mutational-signatures]] — 96-channel SBS context patterns.
- [[30-Concepts/codec]] — Broad duplex chemistry.
- [[30-Concepts/nanoseq]] — Sanger duplex chemistry.
- [[30-Concepts/hidef-seq]] — Evrony duplex chemistry.

## Multi-omic methods

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

## scATAC-seq + chromatin accessibility

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

## Histone modifications

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

## DNA methylation

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

## Long-read sequencing

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

## 3D genome

- [[30-Concepts/3d-genome]] — nuclear chromatin organization.
- [[30-Concepts/single-cell-hi-c]] — sc3DG-seq method family.
- [[30-Concepts/topologically-associating-domain]] — TADs.
- [[30-Concepts/chromatin-compartments]] — A/B compartments.
- [[30-Concepts/sc-sprite]] — sonication-based multi-way single-cell contacts.
- [[30-Concepts/dip-c]] — diploid haplotype-phased Hi-C.
- [[30-Concepts/stark]] — unified sc3DG-seq pipeline.
- [[30-Concepts/sscce]] — single-cell structural quality metric.
- [[30-Concepts/empty-cells-algorithm]] — sc3DG-seq barcode filtering.

## Mosaicism / disease biology

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

## Wiki / meta

- [[30-Concepts/llm-wiki]] — LLM-as-maintainer wiki pattern.
- [[30-Concepts/three-layer-architecture]] — sources / wiki / schema.
- [[30-Concepts/compounding-artifact]] — value-compounding knowledge.
- [[30-Concepts/maintenance-asymmetry]] — humans defer cross-references; LLMs don't.
- [[30-Concepts/ingest-workflow]] — per-source procedure.
