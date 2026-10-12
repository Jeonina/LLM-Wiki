---
type: summary
title: "Weber et al. 2023 — MosaiCatcher v2: a single-cell structural variations detection and analysis reference framework based on Strand-seq"
source: "[[00-Sources/papers/MosaiCatcher v2- a single-cell structural variations detection and analysis reference framework based on Strand-seq.pdf]]"
source_quality: full
source_sha256: "bbce84ba8542e17e8d9ae56ec0e8a90d6edd4a7861ef68a075fbfa2dba2cd58b"
source_kind: paper
author: "Thomas Weber, Marco Raffaele Cosenza, Jan Korbel (corresponding)"
published: 2023-10-18
ingested: 2026-10-12
updated: 2026-10-12
doi: "10.1093/bioinformatics/btad633"
journal: "Bioinformatics 39(11):btad633 (Applications Note)"
aliases: ["Weber 2023", "MosaiCatcher v2", "MosaiCatcher", "mosaicatcher-pipeline"]
tags: [MosaiCatcher, Strand-seq, structural-variants, single-cell-SV-calling, Snakemake, workflow, ashleys-qc, ArbiGent, scNOVA, haplotype-phasing, Korbel-lab, EMBL]
entities: []
concepts: ["[[30-Concepts/strand-seq]]", "[[30-Concepts/structural-variants]]", "[[30-Concepts/copy-number-variation]]", "[[30-Concepts/single-cell-variant-calling]]"]
topics: ["[[40-Topics/scdna-seq]]", "[[40-Topics/computational-methods]]"]
---

**Citation:** Weber, Cosenza & Korbel (2023) — *MosaiCatcher v2: a single-cell structural variations detection and analysis reference framework based on Strand-seq* — *Bioinformatics* 39(11):btad633. [DOI](https://doi.org/10.1093/bioinformatics/btad633)

# Weber 2023 — MosaiCatcher v2

> MosaiCatcher v2 is a Snakemake workflow from the Korbel lab (EMBL Heidelberg) that turns raw Strand-seq FASTQ files into haplotype-phased single-cell structural variant (SV) calls, genotypes and functional readouts in one run. The original MosaiCatcher (the computational side of scTRIP, [[10-Summaries/sanders-2020-sctrip]]) needed manual preprocessing and manual selection of good libraries. Version 2 adds automatic library QC (ashleys-qc), data-dependent checkpoints, a multistep read-count normalization, SV genotyping (ArbiGent), nucleosome-occupancy functional analysis (scNOVA, [[10-Summaries/hyobin-2023-naturebiotechnology]]), and shareable HTML reports. The paper is a software note: it presents features and a re-analysis of four previously published cell lines, not a new benchmark.

## Key claims

- **End-to-end processing.** The ML-based ashleys-qc tool is now built in and selects high-quality libraries automatically, so the pipeline runs from FASTQ to single-cell SV calls and plots. Manual library flagging by an expert in a Jupyter notebook remains as an option. The core can still run alone from aligned Strand-seq BAM files.
- **Data-dependent checkpoints.** Snakemake checkpoints recompute the execution graph from intermediate results. The first filters low-quality libraries (ashleys-qc predictions plus mapping-quality and coverage-bias checks). The second computes average chromosomal ploidy across all libraries and phases heterozygous SNPs only on chromosomes that are at least diploid.
- **Multistep normalization.** Read counts go through library-size normalization, GC correction and variance-stabilizing transformation (VST). The authors say this gives more readable Strand-seq karyotype plots and better SV and copy-number calling in atypical or noisy libraries.
- **Reference genomes.** The QC/assembly sub-workflow supports hg19, hg38, T2T-CHM13 and mouse mm10.
- **ArbiGent SV genotyping.** Uses Strand-seq phasing to genotype inversions and any other SV with at least 500 bp of uniquely mappable sequence. It adds fine-scale depth normalization, phase harmonization between datasets and population-level QC metrics.
- **scNOVA integration.** Strand-seq reads also carry nucleosome-occupancy information. scNOVA uses it to link SVs to functional effects in the same cell, and v2 launches it with one command.
- **Reports.** Shareable static HTML reports hold QC (FASTQC, Strand-seq count plots, GC analysis, excluded cells) and SV-call plots at different stringencies. The pipeline also writes a UCSC custom track and an IGV XML session with per-cell Watson/Crick counts and SV calls.
- **Demonstration.** Four cell lines from the original MosaiCatcher paper (RPE1-WT, RPE-BM510, RPE-C7, NA20509 LCL) were reprocessed in one run against T2T-CHM13 with automatic ashleys-qc selection. A second run genotyped 10 copy-number-imbalanced SVs previously validated by WGS: all were detected, with no false positives or false negatives. A "virtual mixture" of 26 RPE-BM510 and 70 RPE1-WT cells was used to show subclone detection followed by scNOVA comparison of nucleosome occupancy between subclones.

## Methods / evidence

Software engineering plus re-analysis of published data. The pipeline runs under conda or a versioned Docker container, has GitHub Actions CI/CD tests, and follows the snakemake-workflow-catalog "standardized usage" guidelines. Code: github.com/friendsofstrandseq/mosaicatcher-pipeline. Input data and the example report are on Zenodo (records 7696695, 7697329, 8005968). The normalization methods, genotyping set (Supplementary Table S4) and subclone figures are in the Supplementary Material, which this summary did not see.

## Limitations

**Authors' own:**
- SV breakpoint resolution is 100 kb because reads are binned for SV analysis (stated for the MosaiCatcher framework, citing Sanders 2020).
- Workflow components "are not necessarily robust to variation in the input"; the checkpoints are the authors' fix for this, not a removal of it.

**Reviewer notes:**
- The validation is small: 10 SVs in four cell lines already analysed by the same group. No comparison with other Strand-seq or scDNA SV callers is reported. (synthesis)
- The "virtual mixture" is an in-silico pool of cells from two lines, which tests clone separation only between known, distinct genotypes. (synthesis)
- The claims of better calling after normalization and of higher efficiency are qualitative in the main text; no runtime or accuracy numbers are given. (synthesis)

## Surprising or load-bearing bits

- Strand-seq is one assay with several readouts: depth, strand direction and haplotype phase for SVs, plus nucleosome occupancy for function. v2 is the first package that runs all of them from one command.
- The pipeline now treats T2T-CHM13 as a supported reference, which matters for SVs in regions missing from hg38.
- J.O.K. declares a patent application (EP 19169090) on using Strand-seq to find SVs in cancer genomes.

## Entities mentioned

- Jan Korbel (EMBL Heidelberg / DKFZ) — corresponding author; no entity page yet.

## Concepts touched

- [[30-Concepts/strand-seq]] — reference processing workflow for the method.
- [[30-Concepts/structural-variants]] — haplotype-phased single-cell SV calling, including balanced inversions, and SV genotyping.
- [[30-Concepts/copy-number-variation]] — normalization targets better copy-number calling.
- [[30-Concepts/single-cell-variant-calling]] — an SV-oriented counterpart to the SNV/CNV callers listed there.

## Connections to other sources

- Extends [[10-Summaries/sanders-2020-sctrip]]: v2 of the MosaiCatcher framework that scTRIP introduced, reprocessing the same four cell lines.
- Integrates [[10-Summaries/hyobin-2023-naturebiotechnology]] (scNOVA) as a downstream module.
- Builds on the Strand-seq method of [[10-Summaries/falconer-2012-natmethods]].

## Open questions

- How does v2 perform on primary tissue or tumour samples, as opposed to cell lines?
- Does the normalization change SV call sets relative to v1 on the same data? The main text does not say.

## Related

- [[30-Concepts/strand-seq]] · [[30-Concepts/structural-variants]] · [[40-Topics/scdna-seq]] · [[40-Topics/computational-methods]]
- [[10-Summaries/sanders-2020-sctrip]] · [[10-Summaries/hyobin-2023-naturebiotechnology]] · [[10-Summaries/falconer-2012-natmethods]]
