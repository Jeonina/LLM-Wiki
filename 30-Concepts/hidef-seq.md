---
type: concept
title: HiDEF-seq
aliases: [High-Definition Sequencing]
tags: [duplex-sequencing, single-strand, mutation-detection]
created: 2026-05-12
updated: 2026-05-12
---

# HiDEF-seq

> A duplex-sequencing method from the Evrony lab that detects single-strand-resolved mutations with high accuracy. One of the SMaHT-network duplex methods.

## Definition

HiDEF-seq leverages duplex chemistry with optimized library conversion for sensitive somatic mutation detection. Specific implementation details in Park et al. (Evrony lab).

## Why it matters

Specifically designed for somatic mutation profiling in non-cancer tissues with single-strand and double-strand variant resolution.

## Examples

- One of six methods compared in [[10-Summaries/zhang-2025-smaht-duplex-benchmark]].

## Related

- [[40-Topics/duplex-sequencing]] · [[20-Entities/gilad-evrony]] · [[40-Topics/duplex-sequencing]]

## Added 2026-08-13

Founding source ingested 2026-08-13: [[10-Summaries/liu-2024-hidef-seq]].

**What it measures that nothing else does.** Every prior method — single-cell WGS, clonal expansion, microdissection, duplex sequencing — amplifies before reading, which either converts single-strand lesions into double-strand mutations or manufactures artifactual ones ([[10-Summaries/liu-2024-hidef-seq]]). HiDEF-seq sequences unamplified single molecules, so it reads the **precursor** events: single-strand mismatches and cytosine-deamination damage ([[10-Summaries/liu-2024-hidef-seq]]).

**Three engineering moves.** ~32 sequencing passes per strand on median 1.7 kb molecules for per-strand consensus; single-strand nick ligation plus [[30-Concepts/nanoseq|NanoSeq]]-style A-tailing (or a no-A-tailing variant for degraded post-mortem DNA) to eliminate in vitro artifacts; and a pipeline analysing only substitutions, orthogonal to PacBio's dominant indel error mode ([[10-Summaries/liu-2024-hidef-seq]]).

**Fidelity**: <1 error per 3 × 10¹³ bp at ≥5 passes/strand; <1 per 1 × 10¹⁴ bp at ≥20 passes. dsDNA analysis uses the ≥5 threshold (99.8% of molecules retained); ssDNA analysis requires ≥20 ([[10-Summaries/liu-2024-hidef-seq]]).

**Key results**: SBS10ss extracted from *POLE* PPAP samples matches the same samples' dsDNA signatures at cosine 0.97; strand asymmetry (AGA>ATA vs TCT>TAT at 73:10) directly identifies C:dT rather than G:dA misincorporation in vivo; NanoSeq's ssDNA calls are ~18-fold inflated relative to HiDEF-seq ([[10-Summaries/liu-2024-hidef-seq]]).

**Limits**: needs bulk DNA input, not single cells; ~40% genome capture from restriction fragmentation; absolute ssDNA burdens remain uncalibrated because duplex correction is unavailable for single-strand calls ([[10-Summaries/liu-2024-hidef-seq]]).
