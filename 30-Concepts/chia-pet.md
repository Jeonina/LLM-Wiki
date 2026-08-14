---
type: concept
title: ChIA-PET
aliases: [Chromatin Interaction Analysis with Paired-End Tag sequencing, HiChIP, PLAC-seq, protein-anchored interaction mapping]
tags: [3D-genome, ChIP, proximity-ligation, enhancer-promoter, CTCF, RNAPII]
created: 2026-08-13
updated: 2026-08-13
---

# ChIA-PET

> **Chromatin Interaction Analysis with Paired-End Tag sequencing** — chromatin immunoprecipitation combined with proximity ligation, so that only interactions involving a chosen protein are recovered.

## Definition

ChIA-PET closes a gap on both sides of it. ChIP-chip, ChIP-PET, and [[chip-seq|ChIP-seq]] locate a factor's binding sites but cannot name the target gene of a distal site, nor say whether the site is functional. 3C is low-throughput; 4C and 5C cannot map interacting regions at high resolution genome-wide ([[10-Summaries/li-2014-chia-pet]]). ChIA-PET is unbiased, genome-wide, high-throughput, and de novo ([[10-Summaries/li-2014-chia-pet]]).

Against [[lieberman-aiden-2009-hic|Hi-C]], the trade is scope for resolution and interpretability: ChIA-PET gives higher resolution *associated with a protein of interest*, plus TF binding sites and interactions from one assay ([[10-Summaries/li-2014-chia-pet]]).

The protocol is described in three co-equal parts — wet lab, data analysis, and experimental verification ([[10-Summaries/li-2014-chia-pet]]).

## What it established

- **Three interaction classes**: enhancer–promoter, enhancer–enhancer, promoter–promoter ([[10-Summaries/li-2014-chia-pet]]).
- **>40% of enhancers do not regulate their nearest promoter** — the empirical premise for why enhancer-to-gene assignment requires contact data rather than a proximity heuristic ([[10-Summaries/li-2014-chia-pet]]).
- **Chromatin interaction networks are scale-free and hierarchical**, organised into function-enriched "chromatin communities" ([[10-Summaries/li-2014-chia-pet]]).
- Applied across ER-α, RNA polymerase II, CTCF and SMC1A in human MCF7, cancer cells, T cells, and mouse ESCs, NPCs, and B cells ([[10-Summaries/li-2014-chia-pet]]).

## The single-cell asymmetry

Protein-anchored interaction mapping has **no single-cell member**, because immunoprecipitation requires many cells. Its descendants — PLAC-seq and HiChIP — therefore appear in the single-cell literature not as assays but as the **reference truth** against which single-cell loop callers are scored ([[10-Summaries/yu-2021-snaphic]]). The single-cell 3D field traded the functional handle for per-cell resolution: [[single-cell-hi-c|scHi-C]] is protein-agnostic and is the only 3D modality available at single-cell scale. (synthesis)

This mirrors the ChIP-to-[[cut-and-tag|CUT&Tag]] transition in the histone field, where a low-input tethering chemistry replaced immunoprecipitation and *did* reach single cells ([[10-Summaries/kaya-okur-2019-cut-and-tag]]) — no equivalent chemistry has yet rescued protein-anchored *interaction* mapping. (synthesis)

## Related

- [[chromatin-loop]] · [[chip-seq]] · [[single-cell-hi-c]] · [[cis-regulatory-element]] · [[cut-and-tag]] · [[40-Topics/3d-genome]] · [[40-Topics/chromatin-architecture]]
