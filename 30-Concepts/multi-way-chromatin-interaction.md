---
type: concept
title: Multi-way chromatin interaction
aliases: [multi-way interactions, higher-order chromatin contacts, chromatin clique, multi-contact]
tags: [3D-genome, multi-way, clique, SPRITE, GAM, Pore-C, epistasis]
created: 2026-08-13
updated: 2026-10-07
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

## Added 2026-10-07

Short-read single-cell Hi-C can also recover multi-way contacts. Droplet Hi-C used `pairtools parse2` to rescue complex ligation events, counted a read pair as multi-way if it touched ≥3 unique 10 kb bins, and called a bin a hub when its per-cell-type frequency had Z > 1.96 ([[10-Summaries/chang-2025-droplet-hi-c]]). About 5% of bins were hubs, mostly cell-type specific and enriched at super-enhancers and marker genes ([[10-Summaries/chang-2025-droplet-hi-c]]).

The single-cell case for multi-way capture is combinatorial: a DNA fragment can be ligated only once per allele, so a four-fragment complex yields at most two pairwise contacts by proximity ligation but six by complex barcoding, and the maximum grows quadratically with complex size ([[10-Summaries/arrastia-2022-scsprite]]). Because a cluster of n reads is counted as n-choose-2 contacts, SPRITE-type contact counts are not like-for-like with ligation-based counts (synthesis).

Ligation-based and ligation-free multi-way assays sample different physical scales. With matched sequencing volume in mESC, ~70% of scSPRITE reads fall in >10-way clusters (trans ratio 54%). In scNanoHi-C such clusters are negligible (trans 11%), and its multi-way contacts decay with distance like pairwise Hi-C, i.e. the ~200-nm 3C contact radius ([[10-Summaries/li-2023-scnanohi-c]]). In GM12878, scNanoHi-C single concatemers linked 1,097 promoter bins to ≥2 ABC-predicted enhancer bins, and 917 enhancer–promoter 'synergies' were called, ~20% of them inter-chromosomal ([[10-Summaries/li-2023-scnanohi-c]]).


## Related

- [[single-cell-hi-c]] · [[chromatin-loop]] · [[sc-sprite]] · [[gene-regulatory-network]] · [[40-Topics/3d-genome]]
