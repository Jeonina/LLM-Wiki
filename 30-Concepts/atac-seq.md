---
type: concept
title: ATAC-seq
aliases: [Assay for Transposase-Accessible Chromatin sequencing, scATAC-seq]
tags: [chromatin, accessibility, Tn5, single-cell, method]
created: 2026-05-11
updated: 2026-05-11
---

# ATAC-seq

> Assay for Transposase-Accessible Chromatin using sequencing. Uses hyperactive Tn5 transposase to insert Illumina sequencing adapters into accessible chromatin regions in a single step. Reduced input requirement to ~500 cells (vs millions for DNase-seq), enabling clinical-sample, single-cell, and droplet-scale chromatin profiling.

## Definition

Tn5 transposase preferentially inserts adapters into accessible (nucleosome-free or sparsely-nucleosome-bound) DNA. After PCR amplification of the tagmented fragments, sequencing reads pile up at accessible regions, producing peak calls similar to DNase-seq ([[10-Summaries/sandy-2019-naturereviewsgenetics]]).

ATAC-seq is highly correlated with double-cut DNase-seq (r > 0.8) and single-cut DNase-seq (r > 0.75), though it can differ at fine-scale TF footprinting due to Tn5 sequence biases.

## Why it matters

- **500-cell input requirement** democratized chromatin profiling vs DNase-seq's million-cell requirement.
- **Single-cell extension (scATAC-seq)** enables per-cell chromatin profiling on droplet platforms (10x Genomics).
- **Base layer for genotype + chromatin multi-omics**: [[got-cha]] uses 10x scATAC-seq as its base with custom primers for gDNA genotyping.
- **Now standard** for most chromatin accessibility experiments — DNase-seq is rarely used.

## Variants and refinements

- **Omni-ATAC** — improved protocol with reduced mitochondrial contamination.
- **scATAC-seq** — droplet single-cell variant.
- **dscATAC-seq, sci-ATAC-seq** — combinatorial-indexing variants for very high cell throughput.
- **CUT&Tag** — Tn5-based but targeted via antibody, profiling specific TF or histone modification binding.

## Contested points

- Tn5 sequence bias at TF footprinting scale.
- Mitochondrial DNA contamination has been a recurring artifact; protocols (Omni-ATAC) address this.

## Examples

- The [[got-cha]] platform builds on 10x scATAC-seq.
- ENCODE-scale ATAC-seq atlases across hundreds of tissues and cell types.

## Related

- [[chromatin-accessibility]]
- [[dnase-seq]]
- [[got-cha]]
- [[40-Topics/chromatin-architecture]]
