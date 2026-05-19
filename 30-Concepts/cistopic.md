---
type: concept
title: cisTopic
aliases: [LDA-based scATAC clustering]
tags: [scATAC-seq, topic-modeling, LDA, Aerts-lab, software]
created: 2026-05-12
updated: 2026-05-12
---

# cisTopic

> An R/Bioconductor package by the Aerts lab that applies Latent Dirichlet Allocation (LDA) with collapsed Gibbs sampling to scATAC-seq, co-optimizing the clustering of cells and the clustering of regulatory regions into "cis-regulatory topics."

## Definition

Input: binary cell × region accessibility matrix. LDA derives two distributions: region-topic (which regions belong to which topic) and topic-cell (how each cell's accessibility maps to topics). Topics can be interpreted as combinatorial regulatory programs.

## Why it matters

- Resolves temporal heterogeneity that chromVAR averages away (e.g., GATA-mediated regulation at HSC vs intermediate vs MEP stages, each a distinct topic).
- Naturally handles sparsity via topic aggregation.
- Topic regions enrich for TF motifs that correspond to cell-type master regulators.

## Examples

- Hematopoietic differentiation, brain cell types (cortical excitatory layers, glia), SOX10-knockdown dynamics in melanoma ([[10-Summaries/bravo-2019-cistopic]]).

## Related

- [[30-Concepts/latent-dirichlet-allocation]] · [[30-Concepts/scatac-seq]] · [[30-Concepts/chromvar]] · [[30-Concepts/snapatac]] · [[40-Topics/single-cell-atac-seq]] · [[20-Entities/stein-aerts]]
