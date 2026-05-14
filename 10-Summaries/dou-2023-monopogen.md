---
type: summary
title: "Dou 2023 — Single-nucleotide variant calling in single-cell sequencing data with Monopogen"
aliases: ["Monopogen", "Dou 2023", "Dou Monopogen"]
tags: [Monopogen, scSNV-calling, LD-refinement, scRNA-seq, snRNA-seq, scATAC-seq, scDNA-seq, KenChen-lab, MDAnderson]
created: 2026-05-13
updated: 2026-05-13
sources: ["Jinzhuang_2023_NatureBiotechnology.pdf"]
---

Dou, Tan, Kock, Wang, Cheng, Tan, Han, Hon, Park, Shin, Jin, Wang, Chen, Ding, Prabhakar, Navin, Chen and Chen (MD Anderson, GIS Singapore, BCM) developed **Monopogen**, a computational tool that calls single-nucleotide variants from single-cell sequencing data of *any* modality — scRNA-seq, snRNA-seq, scATAC-seq, sci-ATAC-seq, scDNA-seq. The core idea is to overcome the uneven coverage, allelic dropout, and high sequencing-error rates of single-cell data by leveraging **linkage disequilibrium (LD) from external population reference panels** (e.g., 1000 Genomes phase 3).

Two-tier strategy: (i) **germline SNV calling**: refine genotype likelihoods via LD from the population reference, yielding 100K–3M germline SNVs at ~95% accuracy per sample; (ii) **putative somatic SNV calling**: detect somatic variants by identifying alleles that *cosegregate* with germline haplotypes at the cell-population level (i.e., LD pattern matches genome-wide population except for a subpopulation of cells that gained the somatic allele). The somatic SNVs feed into clonal-lineage tracing via Monovar.

Applied to retina snRNA-seq, colon sci-ATAC-seq, and TNBC scDNA-seq with matched-WGS validation. Recall: 21% for retina snRNA at 95%+ accuracy, beating Samtools/GATK/FreeBayes/Strelka2 (11–20% recall, <73% accuracy). Detected ~100 new SNVs not in 1KG3 panel with 35% overall accuracy (86% for clusters with ≥90% concordance).

## Why this matters

A modality-agnostic variant caller that brings genotype information into transcriptome and accessibility datasets without requiring scWGS. Critical for our review's argument that population-LD-aware genotype inference is a viable route around the high cost of scWGS — but with limitations (recall is modest, somatic-SNV detection depends on cosegregation with germline LD which fails for very small clones). Anchors §4 (variant calling) and §5 (clonal hematopoiesis, ancestry-aware analysis).

---
**Source:** [DOI](https://doi.org/10.1038/s41587-023-01873-x) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37592035/)

## Related

- [[10-Summaries/zafar-2016-monovar]]
- [[10-Summaries/luquette-2019-natcomm]]
- [[10-Summaries/dou-2020-mosaicforecast]]
- [[40-Topics/mosaic-variant-calling]]
