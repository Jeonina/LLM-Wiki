---
type: concept
title: Long-read sequencing
aliases: [PacBio, Oxford Nanopore, ONT, HiFi]
tags: [sequencing, long-read, third-generation]
created: 2026-05-11
updated: 2026-05-11
---

# Long-read sequencing

> Sequencing technologies that read DNA molecules of kilobases to hundreds of kilobases in single contiguous reads. Two dominant platforms — **PacBio HiFi** (circular consensus, high accuracy) and **Oxford Nanopore (ONT)** — enable direct detection of base modifications, phasing across long-range variants, and assembly across repeats that short-read sequencing cannot resolve.

## Definition

**PacBio HiFi (SMRT sequencing)**: a polymerase incorporates fluorescent nucleotides at the bottom of a zero-mode waveguide; pulse-width and inter-pulse duration during incorporation are altered by base modifications. Circular consensus sequencing (CCS) of the same molecule produces high-accuracy long reads (>99.9%).

**Oxford Nanopore**: DNA threads through a protein nanopore; electrolytic current changes are interpreted by HMMs / CNNs to call bases — including modified bases that produce distinct current signatures.

## Why it matters

- **No base conversion required** for methylation detection — sidesteps the three-base alignment problem of [[bisulfite-sequencing]].
- **Direct detection of multiple modifications**: 5mC, 5hmC, 6mA, 4mC.
- **Phasing across long distances**: structural variants, repeat expansions, imprinted regions become tractable.
- **Single-molecule resolution** without amplification: native DNA is read directly, preserving any per-molecule information ([[10-Summaries/fu-2025-longread-methylation]]).
- **Enabling platform for** [[fiber-seq]] (m6A footprinting via PacBio) and [[daf-seq]] (deaminase footprinting via PacBio + PTA).

## Variants and refinements

- **PacBio Revio** — current high-throughput HiFi platform.
- **ONT PromethION** — high-throughput nanopore platform; supports R10.4.1+ chemistry with higher accuracy.
- **Methylation callers**: Remora, primrose (Pac); Megalodon, DeepMod (ONT).

## Contested points

- Cost per Gb still higher than short-read Illumina at scale.
- Per-platform methylation calling accuracy varies; benchmarking lags chemistry development.

## Examples

- [[10-Summaries/swanson-2025-daf-seq]] uses PacBio HiFi to read DAF-seq deamination patterns at >25,000× depth on targeted loci.
- HiDEF-seq achieves ~7 × 10⁻¹⁶ error rate via PacBio circular consensus duplex sequencing.

## Related

- [[bisulfite-sequencing]]
- [[30-Concepts/dna-methylation]]
- [[30-Concepts/duplex-sequencing]]
- [[fiber-seq]]
- [[daf-seq]]
- [[40-Topics/long-read-sequencing]]
