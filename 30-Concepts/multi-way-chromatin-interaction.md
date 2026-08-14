---
type: concept
title: Multi-way chromatin interaction
aliases: [multi-way interactions, higher-order chromatin contacts, chromatin clique, multi-contact]
tags: [3D-genome, multi-way, clique, SPRITE, GAM, Pore-C, epistasis]
created: 2026-08-13
updated: 2026-08-13
---

# Multi-way chromatin interaction

> Three or more genomic loci in simultaneous contact **within the same nucleus** — as opposed to three pairwise contacts that may have occurred in three different cells.

## Definition

Bulk Hi-C cannot express this question. Aggregation across millions of nuclei destroys the co-occurrence information that distinguishes "A–B, B–C and A–C each happen somewhere in the population" from "A, B and C are together in one nucleus" ([[10-Summaries/park-2026-mintsc]]). The distinction matters because disease-linked genes are frequently regulated by **multiple distal enhancers acting in combination**, and >90% of GWAS variants are noncoding and dispersed over long distances ([[10-Summaries/park-2026-mintsc]]).

## Two routes to measurement

**Dedicated assays.** GAM, ChIA-drop, SPRITE ([[sc-sprite]]), Tri-C, multi-contact 4C, COLA, and Pore-C all capture multi-way contacts directly. Their limitation is scope: they are established mainly in cell lines and mESCs, not complex tissue ([[10-Summaries/park-2026-mintsc]]). Long-read scNanoHi-C demonstrated multi-way capture in single cells via concatemers, but cellular heterogeneity and noise make such events inconsistently observable across cells ([[10-Summaries/park-2026-mintsc]]).

**Inference from scHi-C.** [[single-cell-hi-c|scHi-C]] is abundant for tissue — notably the NIH BRAIN Initiative brain datasets — and can be re-read as a **multilayer network**: each cell is a layer, loci are nodes, contacts are edges, and a multi-way interaction is a **clique** ([[10-Summaries/park-2026-mintsc]]). Despite sparsity and ligation limits, scHi-C contains abundant cliques of order 3–6; higher orders remain out of reach ([[10-Summaries/park-2026-mintsc]]).

## The spurious-clique problem

Aggregating pairwise contacts across cells can assemble a clique whose edges never co-occurred in any single nucleus. [[10-Summaries/park-2026-mintsc|MINTsC]] guards against this with a pre-filter admitting only cliques fully observed in at least *c* cells and an optional edge co-occurrence post-filter; a simulation with deliberately planted spurious cliques held empirical FDR at 5% ([[10-Summaries/park-2026-mintsc]]). Independent imaging validation put per-cell false-positive rate at ≤3% against a 150-nm DNA seqFISH+ gold standard, and ~8% empirical FDR against scMicro-C 3D reconstructions ([[10-Summaries/park-2026-mintsc]]).

## Why it matters beyond structure

The strongest application is statistical rather than architectural: multi-way interactions supply a **prior that collapses the multiple-testing burden for epistatic SNP effects**. Rather than testing all *cis* SNP pairs for a gene, test only the pairs that share a nucleus-level contact with its promoter. Applied to ROS/MAP Alzheimer's cortex expression data, 321 (gene, SNP₁, SNP₂) tuples from 39 genes showed significantly stronger interaction effects than permuted — including *DKK3* (amyloid-β pathology) and *CPLX2* (synaptic plasticity), where each SNP alone has a weak effect ([[10-Summaries/park-2026-mintsc]]).

Genes participating in multi-way interactions are also more highly expressed across most prefrontal cortex cell types (Wilcoxon P ≤ 0.003) ([[10-Summaries/park-2026-mintsc]]).

## Open questions

- Cliques above order ~6 are undetectable — a ligation and sparsity ceiling, not a statistical one ([[10-Summaries/park-2026-mintsc]]).
- Detection requires a homogeneous cell group; each cell is treated as an independent sample of one context's true contact matrix, and uncertainty in cluster assignment is not currently propagated ([[10-Summaries/park-2026-mintsc]]).
- Multi-way interactions are reported per cell type, so their cell-to-cell variability — the thing the single-cell formulation ought to enable — is not measured. (synthesis)

## Related

- [[single-cell-hi-c]] · [[chromatin-loop]] · [[sc-sprite]] · [[gene-regulatory-network]] · [[40-Topics/3d-genome]]
