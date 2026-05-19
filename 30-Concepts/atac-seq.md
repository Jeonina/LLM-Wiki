---
type: concept
title: ATAC-seq
aliases: [Assay for Transposase-Accessible Chromatin sequencing, scATAC-seq]
tags: [chromatin, accessibility, Tn5, single-cell, method]
created: 2026-05-11
updated: 2026-05-19
---

# ATAC-seq

> Assay for Transposase-Accessible Chromatin using sequencing. Uses hyperactive Tn5 transposase to insert Illumina sequencing adapters into accessible chromatin regions in a single step ([[10-Summaries/buenrostro-2015-nature]]). Reduced input requirement to ~500 cells (vs millions for DNase-seq), enabling clinical-sample, single-cell, and droplet-scale chromatin profiling ([[10-Summaries/buenrostro-2015-nature]]).

## Definition

Tn5 transposase preferentially inserts adapters into accessible (nucleosome-free or sparsely-nucleosome-bound) DNA. After PCR amplification of the tagmented fragments, sequencing reads pile up at accessible regions, producing peak calls similar to DNase-seq ([[10-Summaries/sandy-2019-naturereviewsgenetics]]; [[10-Summaries/buenrostro-2015-nature]]).

ATAC-seq is highly correlated with double-cut DNase-seq (r > 0.8) and single-cut DNase-seq (r > 0.75), though it can differ at fine-scale TF footprinting due to Tn5 sequence biases ([[10-Summaries/sandy-2019-naturereviewsgenetics]]).

## Why it matters

- **500-cell input requirement** democratized chromatin profiling vs DNase-seq's million-cell requirement ([[10-Summaries/buenrostro-2015-nature]]).
- **Single-cell extension (scATAC-seq)** enables per-cell chromatin profiling, first via plate-based ([[10-Summaries/buenrostro-2015-nature]]) and combinatorial-indexing ([[10-Summaries/cusanovich-2015-science]]) approaches; later commercialized on droplet platforms (10x Genomics).
- **Base layer for genotype + chromatin multi-omics**: [[got-cha]] uses 10x scATAC-seq as its base with custom primers for gDNA genotyping ([[10-Summaries/franco-2024-nature]]).
- **Now standard** for most chromatin accessibility experiments — DNase-seq is rarely used (synthesis based on [[10-Summaries/klemm-2019-chromatin-accessibility-review]]).

## Variants and refinements

- **Omni-ATAC** — improved protocol with reduced mitochondrial contamination (synthesis; reduced-mito ATAC variants discussed in [[10-Summaries/klemm-2019-chromatin-accessibility-review]]).
- **scATAC-seq** — droplet single-cell variant ([[10-Summaries/buenrostro-2015-nature]]).
- **dscATAC-seq, sci-ATAC-seq** — combinatorial-indexing variants for very high cell throughput ([[10-Summaries/cusanovich-2015-science]]).
- **sci-CAR** — combinatorial-indexing scATAC + scRNA ([[10-Summaries/cao-2018-sci-car]]).
- **SHARE-seq** — split-pool scATAC + scRNA at tens of thousands of cells ([[10-Summaries/ma-2020-share-seq]]).
- **CUT&Tag** — Tn5-based but targeted via antibody, profiling specific TF or histone modification binding (synthesis; see [[30-Concepts/cut-and-tag]]).

## Contested points

- Tn5 sequence bias at TF footprinting scale ([[10-Summaries/sandy-2019-naturereviewsgenetics]]; resolved at single-molecule level by [[10-Summaries/elliott-2025-naturebiotechnology]]).
- Mitochondrial DNA contamination has been a recurring artifact; protocols (Omni-ATAC) address this ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]).
- scATAC-seq under-calls accessibility vs single-molecule methods due to per-cell sparsity ([[10-Summaries/elliott-2025-naturebiotechnology]]).

## Examples

- The [[got-cha]] platform builds on 10x scATAC-seq ([[10-Summaries/franco-2024-nature]]).
- scATAC-seq reveals chromatin accessibility principles across hematopoietic cell types ([[10-Summaries/buenrostro-2015-nature]]).
- Chromatin potential — accessibility precedes transcription in differentiating keratinocytes ([[10-Summaries/ma-2020-share-seq]]).

## Related

- [[chromatin-accessibility]]
- [[dnase-seq]]
- [[got-cha]]
- [[10-Summaries/yuan-2022-scbasset]] — sequence-based CNN models on scATAC data
- [[40-Topics/chromatin-architecture]]
- [[40-Topics/single-cell-atac-seq]]
- [[50-Notes/regulatory-layers-overview]]
