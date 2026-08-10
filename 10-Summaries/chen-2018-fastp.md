---
type: summary
title: "Chen et al. 2018 — fastp: an ultra-fast all-in-one FASTQ preprocessor"
source: "[[00-Sources/papers/fastp_ an ultra-fast all-in-one FASTQ preprocessor]]"
source_kind: paper
author: "Shifu Chen, Yanqing Zhou, Yaru Chen, Jia Gu"
published: 2018-09-08
ingested: 2026-08-10
doi: "10.1093/bioinformatics/bty560"
journal: "Bioinformatics"
tags: [fastp, QC, adapter-trimming, preprocessing, UMI, polyG, single-pass, multithreading]
entities: []
concepts: ["[[quality-control-metrics]]", "[[umi-molecular-barcoding]]", "[[read-alignment]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[computational-methods]]", "[[scdna-seq]]"]
---

**Citation:** Chen et al. (2018) — *fastp: an ultra-fast all-in-one FASTQ preprocessor* — *Bioinformatics* 34, i884–i890. [DOI](https://doi.org/10.1093/bioinformatics/bty560)

# Chen 2018 — fastp

> The conventional FASTQ preprocessing stack — FASTQC for QC, Cutadapt for adapters, Trimmomatic for pruning — reads and writes the data three times, in three languages, mostly single-threaded. fastp collapses all of it into **one C++ multi-threaded pass** over the file, and runs **2–5× faster than any one of the tools it replaces** while doing more.

## Key claims

- **Single-scan, all-in-one**: quality profiling, adapter trimming, quality filtering, per-read quality pruning, base correction, and report generation from one pass over the FASTQ.
- Implementation: reads are batched in packs of **N = 1000**, each pack consumed by one thread from a pool; every thread keeps an independent statistics context (per-cycle quality, per-cycle base content, adapter results, k-mer counts) which are merged at the end. Written in C/C++, against the Java (FASTQC, Trimmomatic) and Python (Cutadapt, AfterQC) tools it replaces.
- **Automatic adapter detection** for single-end and paired-end Illumina data, by building nucleotide trees forward and backward from sorted adapter seeds and following dominant-child paths.
- **Base correction from paired-end overlap** — inherited from the same authors' AfterQC — corrects mismatched bases in the overlapping region of a read pair, which fastp presents as producing *better* clean data than trimming alone rather than merely faster data.
- **Features the older stack lacks**: UMI preprocessing, per-read **polyG tail trimming** (the NovaSeq/NextSeq two-colour chemistry artefact where absent signal is called as G), and output splitting.
- Reports are HTML and JSON, with **pre-filter and post-filter statistics side by side on one page** so the effect of preprocessing is directly visible.
- Explicit motivating use case: **ctDNA / liquid biopsy**, where mutations sit at ultra-low allele frequency and preprocessing errors convert directly into false positives and false negatives.
- Basic support for long reads (PacBio, Nanopore) in addition to short-read SE/PE data.

## Methods / evidence

This is a tool paper; the evidence is a runtime comparison against Trimmomatic and Cutadapt showing the 2–5× advantage, plus feature-coverage comparison against FASTQC + Cutadapt + Trimmomatic + AfterQC. The design rationale — I/O cost from repeated reading and loading, and the speed ceiling of high-level languages — is stated directly and is the paper's actual argument.

## Surprising or load-bearing bits

- **PolyG trimming is the feature most people need without knowing it.** On two-colour chemistry instruments (NextSeq, NovaSeq), no signal is read as G, so low-quality read ends accumulate spurious poly-G tails. Untrimmed, they either fail to align or align spuriously to G-rich regions. This is a **platform artefact, not a library artefact**, so it affects every assay run on those instruments — which by 2018 was most of them.
- **The ultra-low-allele-frequency framing transfers directly to single-cell work.** A single-cell library also asks for confident calls from very few supporting molecules; the ctDNA argument that preprocessing errors dominate the false-positive rate applies verbatim to per-cell variant calling ([[xu-2012-single-cell-exome-kidney]], [[gonzalez-pena-2021-pnas]]).
- **Overlap-based base correction is quiet extra sensitivity**: for paired-end reads with overlapping inserts, disagreements between mates are resolvable by quality, correcting errors rather than discarding reads. For low-input libraries where every molecule counts, keeping a corrected read beats trimming it.
- The **UMI handling** matters because UMIs are the other answer to the duplicate-versus-independent-molecule problem that [[zahn-2017-dlp|DLP]] solves chemically and [[li-2009-samtools|SAMtools]] approximates by coordinate.
- Nothing here is conceptually novel — the contribution is engineering. That is exactly why it displaced the older stack: pipeline tools compete on throughput and on how many separate steps they remove.

## Concepts touched

- [[quality-control-metrics]] — pre/post-filter reporting as the standard QC artefact.
- [[umi-molecular-barcoding]] — UMI extraction as a preprocessing-stage operation.

## Connections to other sources

- Feeds [[li-2009-bwa]] and [[zhang-2021-chromap]]; upstream of [[li-2009-samtools]] and [[mckenna-2010-gatk]].
- Pipelines that assume clean FASTQ input: [[servant-2015-hicpro]], [[durand-2016-juicer]].
- The low-allele-frequency detection problem it is designed for: [[gonzalez-pena-2021-pnas]], [[allele-dropout]].

## Open questions

- The speed comparison is against tools chosen by the authors at their default settings; no independent benchmark is included, and accuracy of trimming decisions (as opposed to speed) is asserted rather than systematically measured against a ground-truth set.
- Automatic adapter detection is heuristic (dominant-child tree traversal) with no reported false-detection rate — worth pinning adapters explicitly for unusual library chemistries.

## Related

- [[quality-control-metrics]] · [[li-2009-bwa]] · [[li-2009-samtools]] · [[computational-methods]]
