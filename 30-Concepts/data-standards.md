---
type: concept
title: Data Standards
aliases: [file formats, SAM, BAM, cooler, interoperability]
tags: [formats, standards, HDF5, interoperability, 4D-Nucleome]
created: 2026-08-10
updated: 2026-08-10
---

# Data Standards

> Shared file formats are what make a modular tool ecosystem possible. Every "pipeline" in this wiki is really a sequence of tools agreeing on an interface.

## The two that matter most here

**SAM/BAM.** A generic alignment format with 11 mandatory fields plus extensible tags, designed to support all sequencing platforms and aligners, with a binary equivalent compressed by **BGZF** — a zlib-compatible block library allowing fast random access into a compressed file ([[li-2009-samtools]]). Coordinate sorting plus UCSC-binning-and-linear indexing retrieves any region, usually in a single seek ([[li-2009-samtools]]). The stated aim — separating alignment from downstream analyses to enable a generic, modular approach — is why every tool downstream can exist ([[li-2009-samtools]]).

**Cooler.** A sparse, self-describing HDF5 format for genomically labeled arrays: a bin table, a pixel table of non-zero elements referencing it, and a chromosome table, with only the upper triangle stored for symmetric matrices ([[abdennur-2020-cooler]]). Adopted as a standard by the NIH 4D Nucleome Consortium ([[abdennur-2020-cooler]]).

## Why HDF5 over a custom binary layout

Custom Hi-C binary formats organize data efficiently and permit random access, but their **strict byte layouts make them inflexible** for new data types, metadata or additional information ([[abdennur-2020-cooler]]). HDF5 is hierarchical and self-describing, so a format can absorb new columns without a spec revision — derived signals such as balancing weights and compartment eigenvectors travel with the matrix rather than in separate files ([[abdennur-2020-cooler]]).

## Design decisions with downstream consequences

- **Multi-resolution files (`.mcool`)** precompute zoom levels, which is what makes interactive multiscale browsing feasible ([[abdennur-2020-cooler]], [[kerpedjiev-2018-higlass]]).
- **Column-oriented tables** allow cheap column addition and better compression, at the cost of no random row insertion — accepted because raw datasets are write-once ([[abdennur-2020-cooler]]).
- **The `RG` tag** in SAM, meant for sequencing-centre bookkeeping, became the carrier for per-cell identity in merged single-cell BAMs ([[li-2009-samtools]]).

## Open tension

Two Hi-C standards coexist — cooler and Juicer's `.hic` ([[durand-2016-juicer]]) — so format conversion remains a routine step and tool compatibility a practical constraint ([[abdennur-2020-cooler]]).

## Related

- [[read-alignment]] · [[hi-c-normalization]] · [[anndata]] · [[computational-methods]]
