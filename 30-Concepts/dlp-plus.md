---
type: concept
title: DLP+ (DNA Transposition Single-cell Library Preparation)
aliases: [DLP+, DLP-plus]
tags: [scWGA, Tn5, microfluidics, high-throughput, method]
created: 2026-05-11
updated: 2026-05-11
---

# DLP+ (DNA Transposition Single-cell Library Preparation)

> Tn5-based [[scwga]] method implemented in a microfluidic format that trades per-cell coverage for very high cell throughput (>10,000 cells per run). Used for large-scale single-cell CNV / chromosomal phylogenetics where many cells are more informative than deep per-cell coverage.

## Definition

DLP+ uses Tn5 transposase to tagment nuclear DNA, inserting Illumina-compatible adapters directly into the genome of single cells in microfluidic compartments ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). The tagmented fragments are then PCR-amplified. Imaging-based microscopy QC provides real-time ploidy and quality checks. Outputs very low per-cell coverage but covers thousands of cells.

Typical metrics: coverage very low per cell, MAPD moderate, allelic balance typically captures one allele (low per-cell depth), >10,000 cells per run, ~21 h, not commercially available.

## Why it matters

For CNV-centric questions at scale — clonal evolution in tumors, chromosomal mosaicism in development, large-cohort aneuploidy screening — DLP+ delivers far more cells than PTA or MDA can per run. Each cell contributes shallow but uniform CNV information; in aggregate the dataset enables sub-megabase phylogenetic resolution and detection of rare clonal subpopulations.

Tn5-based tagmentation has a useful side-effect: **specific overlap patterns of tagmentation events can be used to distinguish allelic states of each genomic region**, providing additional validation for depth-based CNV calls beyond what MDA or PTA can offer ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Variants and refinements

- Closely related Tn5-based scWGA methods: LIANTI (linear amplification via transposon insertion).
- [[meta-cs]] is the duplex-sequencing variant of Tn5-based scWGA.

## Contested points

- Per-cell coverage so low that SNV detection is unreliable — DLP+ is essentially a CNV-only platform.
- Tn5 tagmentation biases (preferred insertion sites) can affect uniformity at fine scale, though the high cell throughput averages this out for population-level conclusions.

## Examples

- Large-scale single-cell CNV phylogenetics in breast cancer and other solid tumors.
- Detection of chromosomal mosaicism patterns across thousands of cells per sample.

## Related

- [[scwga]]
- [[meta-cs]] — Tn5-based duplex-sequencing sibling method.
- [[scdna-seq]]
- [[40-Topics/whole-genome-amplification]]
