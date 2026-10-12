---
type: concept
title: Multi-way chromatin interaction
aliases: [multi-way interactions, higher-order chromatin contacts, chromatin clique, multi-contact]
tags: [3D-genome, multi-way, clique, SPRITE, GAM, Pore-C, epistasis]
created: 2026-08-13
updated: 2026-10-12
---

# Multi-way chromatin interaction

> Three or more genomic loci in simultaneous contact **within the same nucleus**, as opposed to three pairwise contacts that may have occurred in three different cells ([[10-Summaries/park-2026-mintsc|MINTsC]]).

> [!abstract] 한눈에
> Multi-way chromatin interaction은 세 개 이상의 locus가 한 핵 안에서 동시에 접촉하는 현상이며, 수백만 개 핵을 합친 bulk Hi-C로는 pairwise 접촉의 합과 구별할 수 없다 ([[10-Summaries/park-2026-mintsc|MINTsC]]). 전용 assay로 직접 잡거나 single-cell Hi-C에서 clique로 추론하는데, ligation 기반 assay와 barcoding 기반 assay는 서로 다른 물리적 거리를 본다 ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]; [[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]).

## Definition

Bulk Hi-C cannot express this question: aggregation across millions of nuclei destroys the co-occurrence information that distinguishes "A–B, B–C and A–C each happen somewhere in the population" from "A, B and C are together in one nucleus" ([[10-Summaries/park-2026-mintsc|MINTsC]]). In a network view of [[single-cell-hi-c|scHi-C]], each cell is a layer, loci are nodes, contacts are edges, and a multi-way interaction is a **clique** ([[10-Summaries/park-2026-mintsc|MINTsC]]).

## Why it matters

- Disease-linked genes are frequently regulated by **multiple distal enhancers acting in combination**, and >90% of GWAS variants are noncoding and dispersed over long distances ([[10-Summaries/park-2026-mintsc|MINTsC]]).
- The strongest application is statistical rather than architectural: multi-way interactions supply a **prior that collapses the multiple-testing burden for epistatic SNP effects**. Rather than testing all *cis* SNP pairs for a gene, one tests only the pairs that share a nucleus-level contact with its promoter ([[10-Summaries/park-2026-mintsc|MINTsC]]).

## Routes to measurement

| Route | Examples | How multi-way contacts are read | Scope and limits | Source |
|---|---|---|---|---|
| Dedicated assays | GAM, ChIA-drop, SPRITE ([[sc-sprite]]), Tri-C, multi-contact 4C, COLA, Pore-C | Capture multi-way contacts directly | Established mainly in cell lines and mESCs, not complex tissue | ([[10-Summaries/park-2026-mintsc\|MINTsC]]) |
| Single-cell complex barcoding | [[10-Summaries/arrastia-2022-scsprite\|scSPRITE]] | Split-pool barcodes tag whole complexes, so a four-fragment complex yields six contacts rather than at most two by proximity ligation; the maximum grows quadratically with complex size | A cluster of n reads is counted as n-choose-2 contacts | ([[10-Summaries/arrastia-2022-scsprite\|Arrastia 2022]]) |
| Long-read single-cell Hi-C | [[10-Summaries/li-2023-scnanohi-c\|scNanoHi-C]] | Concatemers carry several ligated fragments in one read | Cellular heterogeneity and noise make such events inconsistently observable across cells | ([[10-Summaries/park-2026-mintsc\|MINTsC]]; [[10-Summaries/li-2023-scnanohi-c\|scNanoHi-C]]) |
| Short-read single-cell Hi-C | [[10-Summaries/chang-2025-droplet-hi-c\|Droplet Hi-C]] | `pairtools parse2` rescues complex ligation events; a read pair is multi-way if it touches ≥3 unique 10 kb bins, and a bin is a hub when its per-cell-type frequency has Z > 1.96 | — | ([[10-Summaries/chang-2025-droplet-hi-c\|Chang 2025]]) |
| Clique inference from scHi-C | [[10-Summaries/park-2026-mintsc\|MINTsC]] | Re-reads pairwise scHi-C as a multilayer network and calls cliques | scHi-C is abundant for tissue, notably the NIH BRAIN Initiative brain datasets; despite sparsity and ligation limits it holds abundant cliques of order 3–6, but higher orders remain out of reach | ([[10-Summaries/park-2026-mintsc\|MINTsC]]) |

### The spurious-clique problem

- Aggregating pairwise contacts across cells can assemble a clique whose edges never co-occurred in any single nucleus ([[10-Summaries/park-2026-mintsc|MINTsC]]).
- MINTsC guards against this with a pre-filter admitting only cliques fully observed in at least *c* cells and an optional edge co-occurrence post-filter ([[10-Summaries/park-2026-mintsc|MINTsC]]).

## Evidence and examples

**Detection accuracy**

- A simulation with deliberately planted spurious cliques held MINTsC's empirical FDR at 5% ([[10-Summaries/park-2026-mintsc|MINTsC]]).
- Independent imaging validation put the per-cell false-positive rate at ≤3% against a 150-nm DNA seqFISH+ gold standard, and the empirical FDR at ~8% against scMicro-C 3D reconstructions ([[10-Summaries/park-2026-mintsc|MINTsC]]).

**Physical scale of different assays**

- With matched sequencing volume in mESC, ~70% of scSPRITE reads fall in >10-way clusters (trans ratio 54%), whereas in scNanoHi-C such clusters are negligible (trans 11%) ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).
- scNanoHi-C multi-way contacts decay with distance like pairwise Hi-C, i.e. they sample the ~200-nm 3C contact radius ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).

**Regulatory hubs**

- In Droplet Hi-C, about 5% of bins were hubs, mostly cell-type specific and enriched at super-enhancers and marker genes ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).
- In GM12878, single scNanoHi-C concatemers linked 1,097 promoter bins to ≥2 ABC-predicted enhancer bins, and 917 enhancer–promoter "synergies" were called, ~20% of them inter-chromosomal ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).
- Genes participating in multi-way interactions are more highly expressed across most prefrontal cortex cell types (Wilcoxon P ≤ 0.003) ([[10-Summaries/park-2026-mintsc|MINTsC]]).

**Epistasis**

- Applied to ROS/MAP Alzheimer's cortex expression data, 321 (gene, SNP₁, SNP₂) tuples from 39 genes showed significantly stronger interaction effects than permuted, including *DKK3* (amyloid-β pathology) and *CPLX2* (synaptic plasticity), where each SNP alone has a weak effect ([[10-Summaries/park-2026-mintsc|MINTsC]]).

## Open questions

- Cliques above order ~6 are undetectable, a ligation and sparsity ceiling rather than a statistical one ([[10-Summaries/park-2026-mintsc|MINTsC]]).
- Detection requires a homogeneous cell group; each cell is treated as an independent sample of one context's true contact matrix, and uncertainty in cluster assignment is not currently propagated ([[10-Summaries/park-2026-mintsc|MINTsC]]).
- Multi-way interactions are reported per cell type, so their cell-to-cell variability, the thing the single-cell formulation ought to enable, is not measured. (synthesis)
- Because SPRITE-type assays count a cluster of n reads as n-choose-2 contacts, their contact counts are not like-for-like with ligation-based counts ([[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]; synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — Methods that profile genome-wide chromatin contacts at single-cell resolution.
> - `concept` [[30-Concepts/sc-sprite|scSPRITE]] — Split-pool barcoding that captures multi-way contacts in single cells without ligation.
> - `concept` [[30-Concepts/chromatin-loop|Chromatin loop]] — A focal point-to-point contact enriched above its local background.
> - `concept` [[30-Concepts/gene-regulatory-network|Gene regulatory network]] — TF-to-target relationships that specify a cell's identity.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Compartments, TADs, loops and their single-cell measurement.

## All sources on this page

> [!info]- 4 summaries cited here
> - [[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]
> - [[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]
> - [[10-Summaries/li-2023-scnanohi-c|Li 2023]]
> - [[10-Summaries/park-2026-mintsc|Park 2026]]
