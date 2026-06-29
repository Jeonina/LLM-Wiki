---
type: summary
title: "Liu & Conesa 2025 — Profiling the epigenome using long-read sequencing (review)"
source: "[[00-Sources/papers/Profiling the epigenome using long-read sequencing]]"
source_kind: paper
author: "Tianyuan Liu, Ana Conesa (corresponding)"
published: 2025-01-08
ingested: 2026-05-12
doi: "10.1038/s41588-024-02038-5"
journal: "Nature Genetics"
tags: [review, long-read-sequencing, epigenome, ONT, PacBio, methylation, chromatin-accessibility, Fiber-seq]
entities:
  - "[[20-Entities/ana-conesa]]"
  - "tianyuan liu"
concepts:
  - "[[40-Topics/long-read-sequencing]]"
  - "[[30-Concepts/oxford-nanopore]]"
  - "[[30-Concepts/pacbio]]"
  - "[[40-Topics/dna-methylation]]"
  - "[[30-Concepts/fiber-seq]]"
  - "[[30-Concepts/nome-seq]]"
  - "[[30-Concepts/allele-specific-methylation]]"
topics:
  - "[[40-Topics/long-read-sequencing]]"
  - "[[40-Topics/dna-methylation]]"
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Liu et al. (2025) — *Profiling the epigenome using long-read sequencing (review)* — *Nature Genetics*. [DOI](https://doi.org/10.1038/s41588-024-02038-5)

# Liu & Conesa 2025 — Profiling the epigenome using long-read sequencing

> Thesis: ONT and PacBio long-read sequencing have transformed epigenomics by (a) directly detecting DNA methylation without bisulfite chemistry, (b) operating on PCR-free single-molecule native DNA so amplification doesn't erase modifications, (c) generating reads long enough for haplotype phasing and highly-repetitive-region mapping, and (d) enabling **co-detection of multiple epigenetic events on the same chromatin fiber**. This review covers methylation detection, chromatin-accessibility methods, protein–DNA interaction profiling, and integration with transcriptomic LRS.

## Key claims

- **Direct methylation detection**: ONT measures ionic current "squiggles" perturbed by methylated bases; PacBio measures kinetic interpulse distance and pulse width. Both have advanced to deep-learning callers (Dorado/Remora for ONT; Fibertools/Primrose for PacBio). Recent benchmarks show comparable methylation accuracy. Multiple modifications detectable (5mC, 5hmC, 6mA, 4mC).
- **Allele-specific methylation (ASM)**: long reads span haplotype blocks, enabling phased methylation calls. Recent deCODE genetics work identified ASM-QTLs as drivers of expression variability in cis-regulatory regions and hematological traits.
- **Chromatin accessibility via methyltransferase footprinting**: exogenous methyltransferases (M.CviPI for GpC, EcoGII for 6mA, DddA-derivatives for cytosine deamination) mark open regions; LRS reads the marks at single-molecule resolution. **Fiber-seq** (EcoGII + PacBio), **nanoNOMe**, **SMAC-seq**, **SAMOSA** (M.CviPI + PacBio), **STAM-seq** (Arabidopsis-adapted), **DAF-seq** (DddA, amplifiable).
- **Methylation in highly repetitive regions** (HRRs) — centromeres, telomeres, rDNA arrays — is accessible only with long reads. Telomere-to-telomere CHM13 assembly enabled by LRS allowed first complete methylation maps of centromeres.
- **3D genome and protein–DNA**: long-read Pore-C, scNanoHi-C, Fiber-seq with CTCF/RNAPII profiling. Single-molecule co-detection of chromatin features in one read.
- **Multi-omics with transcriptomic LRS**: pairing direct RNA sequencing (alternative isoforms, m6A, nascent transcription, translating ribosome profiles) with epigenomic LRS data on the same samples opens integrative analyses of regulation.

## Methods / evidence

Authoritative review. Covers technology evolution (PacBio HiFi $35/Gb; ONT R10.4.1), bioinformatics pipelines (Nanopolish → Megalodon → Dorado/Remora), and biological applications (development, cancer, repetitive-region biology). Discusses challenges: training set generation, k-mer-specific accuracy, polymerase/pore updates requiring model retraining.

## Surprising or load-bearing bits

- The **PCR-free / single-molecule / multimodal** combination is unique to LRS — short-read methods need amplification (erases marks) and only see one event per read.
- The framing that **HRRs are an LRS-exclusive frontier** is load-bearing: centromeres, telomeres, rDNAs, and segmental duplications cannot be uniquely mapped with short reads, so methylation/accessibility maps there were essentially unknown until LRS.
- Bisulfite-free chemistries (TAPS, EM-seq, UBS-seq) reduce DNA damage but introduce conversion-efficiency tradeoffs — methylation detection method choice is non-trivial.

## Connections to other sources

- Extends [[10-Summaries/fu-2025-longread-methylation]] (Fu/Sedlazeck/Timp 2025 long-read methylation review, NRG) on the methylation side. The two reviews complement: NRG focuses on methylation chemistry; this NG paper covers the broader chromatin-accessibility / multi-omics use of LRS.
- Direct methodological link to [[10-Summaries/swanson-2025-daf-seq]] (DAF-seq, single-cell deaminase footprinting) and [[10-Summaries/abdulhay-2020-samosa]] (SMRT-Tag / SAMOSA-Tag).
- STAM-seq application in plants is in [[10-Summaries/mo-2023-stam-seq]] — exemplifies the LRS-HRR advantage.

## Open questions

- The accuracy ceiling for non-CpG methylation contexts (6mA, 4mC) remains lower than for 5mC; new training datasets with synthetic k-mer-balanced controls are still needed.
- Cost and throughput of LRS are improving but still trail Illumina by ~10× for genome-wide bulk applications.

---
**Source:** [DOI](https://doi.org/10.1038/s41588-024-02038-5)
## Related

- [[40-Topics/long-read-sequencing]] · [[30-Concepts/oxford-nanopore]] · [[30-Concepts/pacbio]] · [[30-Concepts/fiber-seq]] · [[20-Entities/ana-conesa]]
