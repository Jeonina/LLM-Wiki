---
type: concept
title: Lineage tracing
aliases: [cell lineage tracing, lineage reconstruction]
tags: [development, lineage, single-cell]
created: 2026-05-11
updated: 2026-05-11
---

# Lineage tracing

> Reconstruction of the developmental ancestry of cells in a tissue — which cells descend from which progenitor, and when each lineage diverged. In humans, where engineered markers cannot be used, **endogenous somatic mutations** that accumulate at ~2–4 per cell division serve as natural lineage barcodes recoverable by [[scdna-seq]].

## Definition

Two strategies:

1. **Engineered markers** (model organisms): fluorescent reporters, Cre recombinase, CRISPR-introduced scarring (GESTALT, scGESTALT, ScarTrace). Powerful but require genetic manipulation — not applicable to humans.
2. **Endogenous mutation accumulation** (humans + model organisms): natural somatic SNVs and structural variants accumulating at known rates serve as cellular barcodes. Detected post-hoc by single-cell genome sequencing ([[10-Summaries/shao-2025-scDNA-mosaicism-review]], [[10-Summaries/evrony-2021-scDNA-applications-review]]).

For endogenous mutation-based tracing in humans, the workflow typically:
- Performs [[scwga]] (often [[pta]]) + scWGS on a sample of cells.
- Identifies lineage-informative variants (those shared among subsets of cells).
- Genotypes those variants in a larger panel of cells via targeted sequencing.
- Reconstructs a phylogenetic tree.

## Why it matters

Lineage tracing answers questions inaccessible to bulk sequencing:

- When did the progenitors of brain region X diverge from region Y?
- Which adult tissue cells descend from which embryonic clone?
- What is the clonal architecture of a tumor and how did it evolve?

In humans specifically, [[lineage-tracing]] using endogenous mutations is one of the major motivations for [[scdna-seq]] advancement.

## Variants and refinements

- **Targeted sequencing of lineage-informative loci** — cheaper, allows thousands of cells (e.g., leukemia lineage studies cited in [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- **Whole-genome reconstruction** — slower but unbiased; preferred when lineage markers are unknown a priori.
- **Combined with single-cell phenotype** (scRNA-seq, surface protein) to map lineage onto cell type — the "phenotypic association" capability in [[10-Summaries/evrony-2021-scDNA-applications-review]].

## Contested points

- Lineage trees from low-coverage scWGA suffer from missing-data artifacts that distort topology. Jaccard distance (binary) is favored by Quake group; model-based clustering with EM is an alternative.
- The mutation rate per division is itself uncertain by ~2× across tissues.

## Examples

- Mapping human cortical neuron lineage with PTA-based scWGS to track the timing of brain region divergence ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- Leukemia clonal evolution by targeted sequencing of driver loci in thousands of cells.
- Identifying inhibitory vs excitatory neuron progenitor divergence in development ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Related

- [[scdna-seq]]
- [[somatic-mosaicism]]
- [[scwga]]
- [[pta]]
- [[scdna-capabilities-framework]]
- [[40-Topics/scdna-seq]]
