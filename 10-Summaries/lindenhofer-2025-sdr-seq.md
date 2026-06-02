---
type: summary
title: "Lindenhofer et al. 2025 — SDR-seq: targeted joint single-cell DNA–RNA sequencing"
source: "[[00-Sources/papers/Functional phenotyping of genomic variants using joint multiomic single-cell DNA–RNA sequencing]]"
source_kind: paper
author: "Dominik Lindenhofer, Julia R. Bauman, John A. Hawkins, Donnacha Fitzgerald, Umut Yildiz, Haeyeon Jung, Anastasiia Korosteleva, Mikael Marttinen, Moritz Kueblbeck, Judith B. Zaugg, Kyung-Min Noh, Sascha Dietrich, Wolfgang Huber, Oliver Stegle, Lars M. Steinmetz (corresponding)"
published: 2025-09-01
ingested: 2026-06-02
doi: "10.1038/s41592-025-02805-0"
journal: "Nature Methods"
tags: [single-cell-multiomics, DNA-RNA-coassay, Tapestri, variant-phenotyping, eQTL, base-editing, prime-editing, B-cell-lymphoma, Steinmetz-lab]
entities:
  - "[[20-Entities/lars-steinmetz]]"
  - "[[20-Entities/oliver-stegle]]"
concepts:
  - "[[30-Concepts/sdr-seq]]"
  - "[[30-Concepts/joint-single-cell-multi-omics]]"
  - "[[30-Concepts/allele-dropout]]"
  - "[[30-Concepts/single-cell-variant-calling]]"
  - "[[30-Concepts/cis-regulatory-element]]"
concepts_secondary:
  - "[[30-Concepts/umi-molecular-barcoding]]"
  - "[[30-Concepts/got]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[40-Topics/scdna-cancer-applications]]"
---

**Citation:** Lindenhofer et al. (2025) — *Functional phenotyping of genomic variants using joint multiomic single-cell DNA–RNA sequencing* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-025-02805-0)

# Lindenhofer et al. 2025 — SDR-seq

> Thesis: Most disease variants are noncoding, and existing droplet DNA+RNA co-assays are too sparse (>96% allelic dropout) to call variant zygosity per cell. **SDR-seq** (single-cell DNA–RNA sequencing) performs in-situ reverse transcription in fixed cells, then a *targeted multiplexed PCR in Tapestri droplets* over up to 480 combined gDNA loci + genes — giving ~90% allele recovery (ADO <10%) so coding *and* noncoding variants can be linked to gene-expression changes in the same cell, at thousands-of-cells scale.

## Key claims

- Targeted, tagmentation-independent design beats whole-genome droplet co-assays: existing methods have ADO >96% (can't determine zygosity); SDR-seq detects ~90% of alleles, comparable to targeted Tapestri scDNA (ADO <10%) and ~100× higher cell throughput than PTA-based plate methods.
- Glyoxal fixation outperforms PFA for in-situ RT (no nucleic-acid crosslinking → better RNA detection); custom poly(dT) RT primers add UMI + sample barcode + capture sequence; distinct R2/R2N overhangs let gDNA and RNA libraries be sequenced separately and optimally.
- Scales cleanly: 120/240/480-target panels give highly correlated, panel-size-independent detection; covers up to 42.8 kb gDNA/cell; gDNA detection is independent of chromatin state (OEG vs NOEG, H3K4me3/H3K27ac/DNase) and RNA detection independent of expression level (except lowly expressed genes); cross-contamination low (gDNA <0.16%, RNA 0.8–1.6%).
- Sensitivity to expression change shown across CRISPRi (strong knockdown), prime editing and base editing (subtle eQTL installation), and natural somatic variants — detecting variants at ~0.15% frequency and resolving that *combinations* of 3′UTR variants in *POU5F1* have different expression effects than single variants.
- Primary B-cell lymphoma (2 FL + 1 GCB-DLBCL, 3,600–8,400 cells/sample): variant-based clustering reveals clonal structure; clones differ in dark-zone/light-zone proportions, implying clonal evolution and differentiation are largely separate processes. **Cells with higher mutational burden show elevated B-cell-receptor signaling and tumorigenic, antiapoptotic expression**; *BCL2* and Ig variable-region variants enriched in the light zone.

## Methods / evidence

Tapestri (Mission Bio) droplets; analysis via SDRranger (github.com/hawkjo/SDRranger) for barcode/UMI processing, GATK HaplotypeCaller for variant calling, MAST for differential expression, Seurat for clustering. Patent filed (PCT/US2024/029950); Steinmetz cofounder of Sophia Genetics/LevitasBio/Recombia.

## Surprising or load-bearing bits

- The core trade-off vs DEFND-seq: SDR-seq sacrifices genome-wide breadth for *targeted depth* — enabling confident single-cell zygosity, which whole-genome droplet methods cannot deliver. Directly assessing a variant beats approximating it with CRISPRi (eQTLs near the TSS behave like CRISPRi; distal ones don't).
- Editing efficiency, not the readout, was the limiting factor for interpreting many eQTLs — a candid statement that the bottleneck is precision genome editing, not measurement.
- Decoupling of clonal genetic evolution from B-cell maturation state is a conceptual result enabled only by reading genotype + state jointly.

## Entities mentioned

- [[20-Entities/lars-steinmetz]] — corresponding (EMBL/Stanford).
- [[20-Entities/oliver-stegle]] — co-author; statistical genomics.
- Wolfgang Huber, Judith Zaugg, Sascha Dietrich — EMBL/Heidelberg co-authors.

## Concepts touched

- [[30-Concepts/sdr-seq]] — method defined here.
- [[30-Concepts/joint-single-cell-multi-omics]] — targeted, low-ADO droplet DNA+RNA.
- [[30-Concepts/allele-dropout]] — the metric SDR-seq is built to beat.

## Connections to other sources

- Complement/contrast to [[10-Summaries/olsen-2025-defnd-seq]] (DEFND-seq, whole-genome high-ADO) — SDR-seq explicitly cites it as a sparse alternative.
- Built on the [[10-Summaries/pellegrino-2018-tapestri]] (Tapestri) droplet scDNA platform.
- Extends genotype-to-phenotype logic of [[10-Summaries/nam-2019-got]] (GoT, mutations in mRNA) to direct gDNA readout including noncoding loci.
- Future direction (mtDNA targeting for clonal tracing) connects to [[10-Summaries/ludwig-2020-mtscatac-seq]] and [[10-Summaries/miller-2022-maester]].

## Open questions

- Whole-transcriptome readout failed (template-switch attempts) — currently targeted RNA only.
- Interpretation limited by low precision-editing efficiency; better pegRNA/base-editor tools needed.

---
**Source:** [DOI](https://doi.org/10.1038/s41592-025-02805-0)
## Related

- [[40-Topics/single-cell-multiomics]] · [[30-Concepts/sdr-seq]] · [[30-Concepts/joint-single-cell-multi-omics]] · [[20-Entities/lars-steinmetz]] · [[20-Entities/oliver-stegle]]
