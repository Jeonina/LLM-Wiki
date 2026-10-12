---
type: concept
title: ATAC-seq
aliases: [Assay for Transposase-Accessible Chromatin sequencing, scATAC-seq]
tags: [chromatin, accessibility, Tn5, single-cell, method]
created: 2026-05-11
updated: 2026-10-12
---

# ATAC-seq

> Assay for Transposase-Accessible Chromatin using sequencing. Uses hyperactive Tn5 transposase to insert Illumina sequencing adapters into accessible chromatin regions in a single step ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]). Reduced input requirement to ~500 cells (vs millions for DNase-seq), enabling clinical-sample, single-cell, and droplet-scale chromatin profiling ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]).

> [!abstract] 한눈에
> ATAC-seq는 Tn5 transposase가 열린 chromatin에 adapter를 끼워 넣는 성질을 이용해 한 단계로 accessibility를 측정하는 방법이며, 약 500개 세포면 충분해서 DNase-seq를 대체하고 single-cell로 확장되었다 ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]; [[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]). Tn5 서열 편향과 세포당 sparsity는 여전히 한계로 남는다 ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

## Definition

Tn5 transposase preferentially inserts adapters into accessible (nucleosome-free or sparsely-nucleosome-bound) DNA. After PCR amplification of the tagmented fragments, sequencing reads pile up at accessible regions, producing peak calls similar to DNase-seq ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]; [[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]). See [[chromatin-accessibility]] and [[dnase-seq]].

ATAC-seq produces accessibility profiles similar to DNase-seq, though it can differ at fine-scale TF footprinting due to Tn5 sequence biases ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]).

## Why it matters

- **500-cell input requirement** democratized chromatin profiling vs DNase-seq's million-cell requirement ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]).
- **Single-cell extension (scATAC-seq)** enables per-cell chromatin profiling, first via plate-based ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]) and combinatorial-indexing ([[10-Summaries/cusanovich-2015-sciatac|Cusanovich 2015]]) approaches; later commercialized on droplet platforms (10x Genomics).
- **Base layer for genotype + chromatin multi-omics**: [[got-cha]] uses 10x scATAC-seq as its base with custom primers for gDNA genotyping ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).
- **Now standard** for most chromatin accessibility experiments — DNase-seq is rarely used (synthesis based on [[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]).

## Variants and refinements

| Variant | What changes | Source |
|---|---|---|
| Omni-ATAC | Improved protocol with reduced mitochondrial contamination | (synthesis; reduced-mito ATAC variants discussed in [[10-Summaries/klemm-2019-chromatin-accessibility-review\|Klemm 2019]]) |
| scATAC-seq | Single-cell variant, founded on the Fluidigm C1 programmable microfluidics platform | ([[10-Summaries/buenrostro-2015-nature\|Buenrostro 2015]]) |
| dscATAC-seq, sci-ATAC-seq | Combinatorial-indexing variants for very high cell throughput | ([[10-Summaries/cusanovich-2015-sciatac\|Cusanovich 2015]]) |
| sci-CAR | Combinatorial-indexing scATAC + scRNA | ([[10-Summaries/cao-2018-sci-car\|sci-CAR]]) |
| SHARE-seq | Split-pool scATAC + scRNA at tens of thousands of cells | ([[10-Summaries/ma-2020-share-seq\|SHARE-seq]]) |
| [[30-Concepts/cut-and-tag\|CUT&Tag]] | Tn5-based but targeted via antibody, profiling specific TF or histone modification binding | (synthesis) |

## Evidence and examples

- scATAC-seq reveals principles of regulatory variation (trans-factor and cis-element drivers of cell-to-cell accessibility variance) across GM12878, K562, H1-ESC and other cell lines ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]).
- Chromatin potential — accessibility precedes transcription in differentiating keratinocytes ([[10-Summaries/ma-2020-share-seq|SHARE-seq]]).
- The [[got-cha]] platform builds on 10x scATAC-seq ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]).
- **As model input.** In EPInformer, ATAC-seq alone as the enhancer-activity input predicted CAGE expression nearly as well as DNase + H3K27ac (r = 0.843 vs 0.867 in K562), so ATAC-only cell types can be modelled ([[10-Summaries/lin-2026-epinformer|EPInformer]]).
- scBasset trains sequence-based CNN models on scATAC data ([[10-Summaries/yuan-2022-scbasset|scBasset]]).

## Contested points

- Tn5 sequence bias at TF footprinting scale ([[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]; resolved at single-molecule level by [[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).
- Mitochondrial DNA contamination has been a recurring artifact; protocols (Omni-ATAC) address this (synthesis).
- scATAC-seq under-calls accessibility vs single-molecule methods due to per-cell sparsity ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — The property ATAC-seq measures.
> - `concept` [[30-Concepts/dnase-seq|DNase-seq]] — The original genome-scale accessibility assay that ATAC-seq largely replaced.
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Somatic genotype and chromatin accessibility from the same nucleus, built on 10x scATAC-seq.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Per-cell accessibility methods and their analysis.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA packaging varies across fibers, haplotypes and cells.
> - `note` [[50-Notes/regulatory-layers-overview|Regulatory layers overview]] — The five molecular axes used to read regulatory DNA.

## All sources on this page

> [!info]- 9 summaries cited here
> - [[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]
> - [[10-Summaries/cao-2018-sci-car|Cao 2018]]
> - [[10-Summaries/cusanovich-2015-sciatac|Cusanovich 2015]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/klemm-2019-chromatin-accessibility-review|Klemm 2019]]
> - [[10-Summaries/lin-2026-epinformer|EPInformer 2026]]
> - [[10-Summaries/ma-2020-share-seq|Ma 2020]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
> - [[10-Summaries/yuan-2022-scbasset|Yuan & Kelley 2022]]
