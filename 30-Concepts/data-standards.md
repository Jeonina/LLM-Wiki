---
type: concept
title: Data Standards
aliases: [file formats, SAM, BAM, cooler, interoperability]
tags: [formats, standards, HDF5, interoperability, 4D-Nucleome]
created: 2026-08-10
updated: 2026-10-12
---

# Data Standards

> Shared file formats are what make a modular tool ecosystem possible. Every "pipeline" in this wiki is really a sequence of tools agreeing on an interface ([[10-Summaries/li-2009-samtools|SAMtools]]; [[10-Summaries/abdennur-2020-cooler|cooler]]).

> [!abstract] 한눈에
> SAM/BAM과 cooler 같은 공통 파일 형식이 있어야 정렬·호출·시각화 도구를 따로 만들어 이어 붙일 수 있다 ([[10-Summaries/li-2009-samtools|SAMtools]]; [[10-Summaries/abdennur-2020-cooler|cooler]]). Hi-C에서는 cooler와 Juicer의 `.hic`가 함께 쓰여 형식 변환이 여전히 일상적인 단계다 ([[10-Summaries/abdennur-2020-cooler|cooler]]; [[10-Summaries/durand-2016-juicer|Juicer]]).

## Definition

A data standard here is a shared file format with a published layout, so that one tool's output is another tool's input. The stated aim of SAM — separating alignment from downstream analyses to enable a generic, modular approach — is why every tool downstream can exist ([[10-Summaries/li-2009-samtools|SAMtools]]).

## Why it matters

Custom Hi-C binary formats organize data efficiently and permit random access, but their **strict byte layouts make them inflexible** for new data types, metadata or additional information ([[10-Summaries/abdennur-2020-cooler|cooler]]). A self-describing standard lets a format absorb new information without a spec revision ([[10-Summaries/abdennur-2020-cooler|cooler]]).

## The two that matter most here

| Format | Data | Structure | Key design | Source |
|---|---|---|---|---|
| SAM/BAM | Read alignments | 11 mandatory fields plus extensible tags; binary equivalent compressed by **BGZF**, a zlib-compatible block library allowing fast random access into a compressed file | Designed to support all sequencing platforms and aligners; coordinate sorting plus UCSC-binning-and-linear indexing retrieves any region, usually in a single seek | ([[10-Summaries/li-2009-samtools\|SAMtools]]) |
| Cooler | Genomically labeled arrays (Hi-C matrices) | Sparse, self-describing HDF5: a bin table, a pixel table of non-zero elements referencing it, and a chromosome table | Only the upper triangle stored for symmetric matrices; adopted as a standard by the NIH 4D Nucleome Consortium | ([[10-Summaries/abdennur-2020-cooler\|cooler]]) |

**Why HDF5 over a custom binary layout.** HDF5 is hierarchical and self-describing, so a format can absorb new columns without a spec revision — derived signals such as balancing weights and compartment eigenvectors travel with the matrix rather than in separate files ([[10-Summaries/abdennur-2020-cooler|cooler]]).

## Evidence and examples

Design decisions with downstream consequences:

- **Multi-resolution files (`.mcool`)** precompute zoom levels, which is what makes interactive multiscale browsing feasible ([[10-Summaries/abdennur-2020-cooler|cooler]]; [[10-Summaries/kerpedjiev-2018-higlass|HiGlass]]).
- **Column-oriented tables** allow cheap column addition and better compression, at the cost of no random row insertion — accepted because raw datasets are write-once ([[10-Summaries/abdennur-2020-cooler|cooler]]).
- **The `RG` tag** in SAM, meant for sequencing-centre bookkeeping, became the carrier for per-cell identity in merged single-cell BAMs ([[10-Summaries/li-2009-samtools|SAMtools]]).

## Contested points

- Two Hi-C standards coexist — cooler and Juicer's `.hic` ([[10-Summaries/durand-2016-juicer|Juicer]]) — so format conversion remains a routine step and tool compatibility a practical constraint ([[10-Summaries/abdennur-2020-cooler|cooler]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/read-alignment|Read alignment]] — The step whose output SAM/BAM standardises.
> - `concept` [[30-Concepts/hi-c-normalization|Hi-C normalization]] — Balancing weights that travel inside cooler files.
> - `concept` [[30-Concepts/anndata|AnnData]] — The analogous container standard for single-cell matrices.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — The tool layer: aligners, callers, imputers and integrators.

## All sources on this page

> [!info]- 4 summaries cited here
> - [[10-Summaries/abdennur-2020-cooler|Abdennur & Mirny 2020]]
> - [[10-Summaries/durand-2016-juicer|Durand 2016]]
> - [[10-Summaries/kerpedjiev-2018-higlass|Kerpedjiev 2018]]
> - [[10-Summaries/li-2009-samtools|Li 2009]]
