---
type: concept
title: Read Alignment
aliases: [read mapping, sequence alignment, BWT alignment]
tags: [alignment, BWA, SAM, BAM, infrastructure]
created: 2026-08-10
updated: 2026-08-10
---

# Read Alignment

> Placing sequencing reads onto a reference genome — the step every assay in this wiki passes through, and the one whose output format determines what downstream tools can exist.

## Definition

Two dominant paradigms. **BWT/FM-index search** builds a Burrows–Wheeler transform of the reference and searches it backwards, counting exact occurrences of a length-*m* query in *O*(*m*) time independent of genome size ([[li-2009-bwa]]). **Seed-and-extend hashing** finds short exact seeds then extends by dynamic programming; BWA-MEM, the version most pipelines actually run, belongs to this class rather than to the backtracking algorithm of the original BWA paper ([[li-2009-bwa]]).

Alignments are emitted in **SAM**, a TAB-delimited format with 11 mandatory fields plus extensible `TAG:TYPE:VALUE` pairs, and its compressed binary equivalent **BAM** ([[li-2009-samtools]]).

## Why it matters

- **Repeat collapsing** is why BWT alignment is fast — exact repeats occupy one path in the prefix trie — and simultaneously why multi-mapping is unresolvable ([[li-2009-bwa]]). See [[mappability]].
- **Format standardization decoupled alignment from analysis**, which is why the tool ecosystem is modular at all ([[li-2009-samtools]]).
- **Sub-1 GB index memory** makes thousands of small per-cell alignment jobs practical, which is the shape of shallow single-cell WGS workloads ([[li-2009-bwa]], [[zahn-2017-dlp]]).
- **The `RG` read-group tag**, designed for sequencing-centre bookkeeping, is the slot single-cell pipelines repurpose to carry cell identity through merged BAMs ([[li-2009-samtools]]).

## Assay-specific complications

- **Proximity-ligation reads are chimeric by construction**, so a plain aligner discards informative pairs; Hi-C pipelines add two-step mapping or chimeric rescue ([[servant-2015-hicpro]]).
- **Adapter contamination and polyG tails** degrade mappability if not trimmed first ([[chen-2018-fastp]]); WGA-derived adaptor contamination produces measurably low mappability ([[zahn-2017-dlp]]).
- **Allele-specific analysis** requires an N-masked reference and phased SNPs, and recovers only ~6% of valid interactions even with 2.2 million phased sites ([[servant-2015-hicpro]]).
- Chromatin assays benefit from purpose-built fast aligners ([[zhang-2021-chromap]]).

## Related

- [[mappability]] · [[duplicate-marking]] · [[quality-control-metrics]] · [[computational-methods]]
