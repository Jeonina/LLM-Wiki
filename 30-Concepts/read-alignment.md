---
type: concept
title: Read Alignment
aliases: [read mapping, sequence alignment, BWT alignment]
tags: [alignment, BWA, SAM, BAM, infrastructure]
created: 2026-08-10
updated: 2026-10-12
---

# Read Alignment

> Placing sequencing reads onto a reference genome — the step every assay in this wiki passes through, and the one whose output format determines what downstream tools can exist ([[10-Summaries/li-2009-bwa|BWA]]; [[10-Summaries/li-2009-samtools|Li 2009]]).

> [!abstract] 한눈에
> Read alignment는 sequencing read를 reference genome 위에 놓는 단계로, BWT/FM-index 검색과 seed-and-extend 두 방식이 주류이고 결과는 SAM/BAM 형식으로 나온다 ([[10-Summaries/li-2009-bwa|BWA]]; [[10-Summaries/li-2009-samtools|Li 2009]]). Hi-C의 chimeric read나 WGA adaptor 오염처럼 assay마다 정렬을 어렵게 만드는 요인이 따로 있다 ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]; [[10-Summaries/zahn-2017-dlp|Zahn 2017]]).

## Definition

Alignments are emitted in **SAM**, a TAB-delimited format with 11 mandatory fields plus extensible `TAG:TYPE:VALUE` pairs, and its compressed binary equivalent **BAM** ([[10-Summaries/li-2009-samtools|Li 2009]]).

## Why it matters

- **Repeat collapsing** is why BWT alignment is fast — exact repeats occupy one path in the prefix trie — and simultaneously why multi-mapping is unresolvable ([[10-Summaries/li-2009-bwa|BWA]]). See [[mappability]].
- **Format standardization decoupled alignment from analysis**, which is why the tool ecosystem is modular at all ([[10-Summaries/li-2009-samtools|Li 2009]]).
- **Sub-1 GB index memory** makes thousands of small per-cell alignment jobs practical, which is the shape of shallow single-cell WGS workloads ([[10-Summaries/li-2009-bwa|BWA]]; [[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- **The `RG` read-group tag**, designed for sequencing-centre bookkeeping, is the slot single-cell pipelines repurpose to carry cell identity through merged BAMs ([[10-Summaries/li-2009-samtools|Li 2009]]).
- **Variant-call accuracy depends on the upstream aligner.** VarScan accepted BLAT, Newbler, cross_match, Bowtie and Novoalign output and shipped recommended parameters for each, because, in the authors' words, sensitivity and specificity depend on alignment accuracy ([[10-Summaries/koboldt-2009-varscan|VarScan]]).

## Alignment paradigms

| Paradigm | How it works | Note | Source |
|---|---|---|---|
| BWT/FM-index search | Builds a Burrows–Wheeler transform of the reference and searches it backwards | Counts exact occurrences of a length-*m* query in *O*(*m*) time independent of genome size | ([[10-Summaries/li-2009-bwa\|BWA]]) |
| Seed-and-extend hashing | Finds short exact seeds, then extends by dynamic programming | BWA-MEM, the version most pipelines actually run, belongs to this class rather than to the backtracking algorithm of the original BWA paper | ([[10-Summaries/li-2009-bwa\|BWA]]) |
| Purpose-built chromatin aligners | — | Chromatin assays benefit from purpose-built fast aligners | ([[10-Summaries/zhang-2021-chromap\|Chromap]]) |

## Assay-specific complications

- **Proximity-ligation reads are chimeric by construction**, so a plain aligner discards informative pairs; Hi-C pipelines add two-step mapping or chimeric rescue ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]).
- **Ligation-junction multimapping is an aligner-induced artifact** in chromatin-conformation reads ([[10-Summaries/galasso-2026-map3c|map3C]]).
- **Adapter contamination and polyG tails** degrade mappability if not trimmed first ([[10-Summaries/chen-2018-fastp|fastp]]); WGA-derived adaptor contamination produces measurably low mappability ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- **Allele-specific analysis** requires an N-masked reference and phased SNPs ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]).
- **Aligned reads as model input.** STRAND takes aligned reads (BAM) rather than called variants as language-model input, arguing this avoids variant-calling bias ([[10-Summaries/ayanian-2025-strand|STRAND]]).

## Evidence and examples

- 26–30% of soft-clipped alignments multimapped in example LiMCA and snm3C-seq cells ([[10-Summaries/galasso-2026-map3c|map3C]]).
- Allele-specific Hi-C recovers only ~6% of valid interactions even with 2.2 million phased sites ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/mappability|Mappability]] — Whether a read from a position can be assigned back to it uniquely.
> - `concept` [[30-Concepts/duplicate-marking|Duplicate marking]] — Identifying reads that are PCR copies of the same template.
> - `concept` [[30-Concepts/quality-control-metrics|Quality-control metrics]] — Per-library and per-cell statistics that decide which data enter an analysis.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — The tool layer: aligners, formats, callers, imputers and integrators.

## All sources on this page

> [!info]- 9 summaries cited here
> - [[10-Summaries/ayanian-2025-strand|STRAND 2025]]
> - [[10-Summaries/chen-2018-fastp|Chen 2018]]
> - [[10-Summaries/galasso-2026-map3c|Galasso 2026]]
> - [[10-Summaries/koboldt-2009-varscan|Koboldt 2009]]
> - [[10-Summaries/li-2009-bwa|Li & Durbin 2009]]
> - [[10-Summaries/li-2009-samtools|Li 2009]]
> - [[10-Summaries/servant-2015-hicpro|Servant 2015]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
> - [[10-Summaries/zhang-2021-chromap|Zhang 2021]]
