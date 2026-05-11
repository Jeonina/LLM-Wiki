---
type: topic
title: Long-read sequencing
aliases: [PacBio, Oxford Nanopore, long-read]
tags: [sequencing, long-read, third-generation]
created: 2026-05-11
updated: 2026-05-11
---

# Long-read sequencing

> The enabling platform layer beneath several recent breakthroughs in this vault: single-molecule chromatin footprinting ([[fiber-seq]], [[daf-seq]]), direct methylation detection without bisulfite conversion, scDAF-seq chromosome-length consensus reads, and duplex sequencing variants like HiDEF-seq.

## Core concepts

- [[30-Concepts/long-read-sequencing]] — PacBio HiFi and Oxford Nanopore platforms.
- [[30-Concepts/fiber-seq]] — m6A-based single-molecule chromatin footprinting (PacBio).
- [[30-Concepts/daf-seq]] — deaminase-based single-molecule chromatin footprinting (PacBio).
- [[30-Concepts/duplex-sequencing]] — HiDEF-seq, SMM-seq are long-read duplex variants.
- [[30-Concepts/bisulfite-sequencing]] — short-read alternative that long-read methods supplant for methylation.

## Key entities

- [[20-Entities/fritz-sedlazeck]] — long-read computational genomics.
- [[20-Entities/winston-timp]] — nanopore methylation pioneer.
- [[20-Entities/andrew-b-stergachis]] — Fiber-seq / DAF-seq developer (PacBio).
- [[20-Entities/elliott-g-swanson]] — DAF-seq co-first author.

## Sources, by sub-theme

### Long-read methylation analysis

- [[10-Summaries/yilei-2025-naturereviewsgenetics]] — computational analysis of long-read methylation data.

### Long-read single-molecule chromatin

- [[10-Summaries/elliott-2025-naturebiotechnology]] — DAF-seq / scDAF-seq.

### Long-read referenced in scDNA-seq context

- [[10-Summaries/diane-2025-naturereviewsgenetics]] — HiDEF-seq and other long-read duplex methods.
- [[10-Summaries/anna-2019-nature]] — Oxford Nanopore validation of GoT for distal loci.

## Synthesized notes

_None yet._

## Open questions

- Cost per Gb at scale — still higher than short-read Illumina; gap closing but not closed.
- Methylation calling accuracy benchmarking across platforms.
- Long-read single-cell methods — emerging but not yet routine; scDAF-seq is currently the most successful single-cell long-read application.
