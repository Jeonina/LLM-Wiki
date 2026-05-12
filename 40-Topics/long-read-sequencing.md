---
type: topic
title: Long-read sequencing
aliases: [PacBio, Oxford Nanopore, long-read]
tags: [sequencing, long-read, third-generation]
created: 2026-05-11
updated: 2026-05-12
---

# Long-read sequencing

> The enabling platform layer beneath several recent breakthroughs in this vault: single-molecule chromatin footprinting ([[fiber-seq]], [[daf-seq]]), direct methylation detection without bisulfite conversion, scDAF-seq chromosome-length consensus reads, and duplex sequencing variants like HiDEF-seq.

## Core concepts

- [[30-Concepts/long-read-sequencing]] — PacBio HiFi and Oxford Nanopore platforms.
- [[30-Concepts/oxford-nanopore]] — ONT platform.
- [[30-Concepts/pacbio]] — PacBio SMRT platform.
- [[30-Concepts/fiber-seq]] — m6A-based single-molecule chromatin footprinting (PacBio).
- [[30-Concepts/daf-seq]] — deaminase-based single-molecule chromatin footprinting (PacBio).
- [[30-Concepts/duplex-sequencing]] — HiDEF-seq, SMM-seq are long-read duplex variants.
- [[30-Concepts/bisulfite-sequencing]] — short-read alternative that long-read methods supplant for methylation.
- [[30-Concepts/samosa]], [[30-Concepts/samosa-tag]], [[30-Concepts/smrt-tag]] — PacBio chromatin-accessibility methods.
- [[30-Concepts/stam-seq]] — plant nanopore chromatin + methylation method.
- [[30-Concepts/nanopore-adaptive-sampling]] — real-time read selection for targeted sequencing.
- [[30-Concepts/highly-repetitive-regions]] — centromeres, telomeres, rDNAs — accessible only with LRS.
- [[30-Concepts/structural-variants]], [[30-Concepts/somagauss-sv]] — somatic SV detection.
- [[30-Concepts/allele-specific-methylation]] — phased methylation via long reads.

## Key entities

- [[20-Entities/fritz-sedlazeck]] — long-read computational genomics.
- [[20-Entities/winston-timp]] — nanopore methylation pioneer.
- [[20-Entities/andrew-b-stergachis]] — Fiber-seq / DAF-seq developer (PacBio).
- [[20-Entities/elliott-g-swanson]] — DAF-seq co-first author.
- [[20-Entities/ana-conesa]] — long-read epigenome review.
- [[20-Entities/vijay-ramani]] — SAMOSA / SMRT-Tag / SAMOSA-Tag developer.
- [[20-Entities/jixian-zhai]] — STAM-seq plant epigenomics.
- [[20-Entities/jifeng-liu]] — nanopore somatic SV in head-and-neck cancer.
- [[20-Entities/dan-xie]] — SCOUT + SomaGauss-SV.

## Sources, by sub-theme

### Long-read methylation analysis

- [[10-Summaries/yilei-2025-naturereviewsgenetics]] — Fu/Sedlazeck/Timp NRG computational long-read methylation analysis.
- [[10-Summaries/profiling-the-epigenome-using-long-read-sequencing]] — Liu/Conesa 2025 NRG broader epigenome review (methylation + accessibility + 3D + transcriptomic LRS).

### Long-read single-molecule chromatin

- [[10-Summaries/elliott-2025-naturebiotechnology]] — DAF-seq / scDAF-seq.
- [[10-Summaries/direct-transposition-of-native-dna-for-sensitive-multimodal-single-molecule-sequencing]] — SMRT-Tag and SAMOSA-Tag (Ramani lab).
- [[10-Summaries/single-molecule-targeted-accessibility-and-methylation-sequencing-of-centromeres-telomeres-and-rdnas-in-arabidopsis]] — STAM-seq, plant HRRs.

### Long-read SV detection

- [[10-Summaries/nanopore-sequencing-unveils-somatic-structural-variations-as-biomarkers-in-laryngeal-squamous-cell-carcinoma-genomes]] — SomaGauss-SV in LSCC.

### Long-read referenced in scDNA-seq context

- [[10-Summaries/diane-2025-naturereviewsgenetics]] — HiDEF-seq and other long-read duplex methods.
- [[10-Summaries/anna-2019-nature]] — Oxford Nanopore validation of GoT for distal loci.

## Synthesized notes

_None yet._

## Open questions

- Cost per Gb at scale — still higher than short-read Illumina; gap closing but not closed.
- Methylation calling accuracy benchmarking across platforms.
- Long-read single-cell methods — emerging but not yet routine; scDAF-seq is currently the most successful single-cell long-read application.
