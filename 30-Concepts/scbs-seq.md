---
type: concept
title: scBS-seq
aliases: [single-cell bisulfite sequencing, single-cell whole-genome bisulfite sequencing]
tags: [methylation, single-cell, bisulfite, genome-wide]
created: 2026-05-12
updated: 2026-10-12
---

# scBS-seq

> Single-cell bisulfite sequencing: genome-wide CpG methylation per cell from bisulfite conversion, with sparse coverage (~10–40% of CpGs detected per cell at ~20M reads) because bisulfite-induced DNA degradation limits library complexity (synthesis; method: [[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]).

> [!abstract] 한눈에
> scBS-seq는 bisulfite 변환 뒤에 adaptor를 붙이는 PBAT 순서 덕분에 단일 세포에서 genome-wide CpG methylation을 읽을 수 있게 된 방법이다 ([[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]). 세포당 coverage가 희소해서 tile 평균, DMR 검정, imputation 같은 전처리 선택이 결과를 크게 바꾼다 ([[10-Summaries/kremer-2024-methscan|MethSCAn]]; [[10-Summaries/zhou-2024-scdmv|scDMV]]).

## Definition

scBS-seq is the founding method for single-cell methylomics (Smallwood et al. 2014, [[10-Summaries/smallwood-2014-natmethods|Smallwood 2014]]); its step-by-step protocol is [[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]. For the functions of the mark itself, see [[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]].

- **PBAT is the enabling inversion.** In conventional bisulfite sequencing, adaptor-tagged molecules are bisulfite-treated and most are destroyed; PBAT uses bisulfite to do both the conversion and the fragmentation, tagging afterwards ([[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]). Protocol topology, not chemistry, is what set the input floor (synthesis).
- **Five rounds of random priming with intermediate heat denaturation** are the single-cell modification — five chances to capture each locus, and multiple copies per fragment so purification does not collapse complexity ([[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]).
- Random hexamers are recommended over tetramers (yield) or nonamers (trimming burden) ([[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]).

## Why it matters

- It is the foundational method for single-cell methylomics ([[10-Summaries/smallwood-2014-natmethods|Smallwood 2014]]).
- It is cost-prohibitive at atlas scale, which motivates alternatives such as [[30-Concepts/sctem-seq]] (TE-targeted), sci-MET (combinatorial indexing) and TAPS-based methods (synthesis).

## Variants and descendants

| Method | Design | Coverage per cell | Source |
|---|---|---|---|
| scBS-seq | PBAT with five rounds of random priming | Up to ~50% of CpGs per single mouse cell — the highest per-cell coverage of any single-cell methylation method in the corpus | ([[10-Summaries/clark-2017-scbs-seq-protocol\|Clark 2017]]) |
| scWGBS | No-pre-amplification sibling: cells bisulfite-treated after lysis, post-bisulfite library steps in one tube | Median 1.4 M CpGs from 4.6 M reads per human single cell | ([[10-Summaries/farlik-2015-scwgbs\|Farlik 2015]]) |
| scDEEP-mC | PBAT descendant: cells sorted directly into bisulfite reagent (no post-conversion cleanup), seven rounds of base-composition-matched random priming, directional second-strand priming | ~30% of CpGs at 20 M reads per cell | ([[10-Summaries/spix-2025-scdeep-mc\|scDEEP-mC]]) |
| sci-MET | Combinatorial indexing | ~1% | ([[10-Summaries/mulqueen-2018-sci-met\|sci-MET]]; [[10-Summaries/clark-2017-scbs-seq-protocol\|Clark 2017]]) |
| Drop-BS | Droplet-based bisulfite sequencing | Sparse, at the opposite end of the design axis from scBS-seq | ([[10-Summaries/zhang-2023-drop-bs\|Drop-BS]]; [[10-Summaries/clark-2017-scbs-seq-protocol\|Clark 2017]]) |
| Bisulfite-free (scTAPS/scCAPS+) | TAPS-based chemistry | — | ([[10-Summaries/chen-2025-sctaps-sccaps-plus\|Chen 2025]]) |

- Farlik 2015 positions scWGBS for many cells at low coverage, scRRBS for CpG islands, and scPBAT for deep single-cell coverage ([[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]).

## Preprocessing is not neutral

- **Tile-averaging dilutes signal.** The standard 100 kb-tile-and-average recipe drowns small variably methylated regions in uninformative CpGs, and sparse per-cell coverage means different cells are represented by reads at *different positions* within a tile ([[10-Summaries/kremer-2024-methscan|MethSCAn]]).
- **Read-position-aware quantitation.** Compare each cell to a kernel-smoothed cross-cell average at the CpGs it actually observed, and average the signed residuals with shrinkage ([[10-Summaries/kremer-2024-methscan|MethSCAn]]).
- **DMR detection for scBS did not exist before 2024**; sliding-window *t* statistics with permutation-based FDR now make it possible ([[10-Summaries/kremer-2024-methscan|MethSCAn]]).
- **Zero–one inflation.** Regional per-cell methylation rates concentrate at exactly 0 or 1, which scDMV models with a zero–one inflated beta for DMR testing ([[10-Summaries/zhou-2024-scdmv|scDMV]]).
- **Imputation** is the other response to sparsity ([[10-Summaries/zhao-2025-mambacpg|MambaCpG]]).
- **Single-CpG modelling.** scDNAm-GPT models scWGBS data at single-CpG resolution instead of 100-kb or 5-kb bins ([[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]).

## Evidence and examples

- Whole methylomes of rare cell types are reconstructed by merging <20 cells ([[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]).
- A bulk WGBS benchmark found the post-bisulfite (PBAT) design that underlies scBS-seq to be the least biased library strategy, with amplification-free PBAT showing no significant CG-dinucleotide coverage deviation ([[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]).
- scDEEP-mC has the highest sequencing efficiency among reprocessed public scWGBS methods ([[10-Summaries/spix-2025-scdeep-mc|scDEEP-mC]]).
- 63,421 de novo variably methylated regions (VMRs) match the cell-typing performance of 339,815 ENCODE cCREs and outperform an equal-sized cCRE subset ([[10-Summaries/kremer-2024-methscan|MethSCAn]]).
- VMR methylation predicts expression better than promoter methylation ([[10-Summaries/kremer-2024-methscan|MethSCAn]]).
- In an embryo scBS-seq dataset, regional per-cell rates of exactly 0 or 1 made up over 0.9 combined ([[10-Summaries/zhou-2024-scdmv|scDMV]]).
- In scDMV's simulations, the bulk caller methylpy flagged 999 of 1,000 null regions at P ≤ 0.01 without an effect-size cutoff ([[10-Summaries/zhou-2024-scdmv|scDMV]]).
- MambaCpG reports AUC 91.42–94.20 on scBS-seq and snmC-seq datasets of 20–780 cells ([[10-Summaries/zhao-2025-mambacpg|MambaCpG]]).
- scDNAm-GPT reports 80.5–87.1% cell-type accuracy on four datasets unseen in pretraining ([[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]).
- Most public site-level imputation benchmarks still rest on early scBS-seq data (e.g. 12–20-cell mESC/oocyte sets) ([[10-Summaries/liang-2026-scmeth-imputation-benchmark|Liang 2026]]).

## Contested points

- **5mC and 5hmC are confounded.** All bisulfite-based single-cell methylomes report 5mC+5hmC combined — a 22% confound in hippocampal neurons ([[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]).
- **Amplification still biases values.** Amplified post-BS libraries (ampPBAT) still altered local CG methylation values ([[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]), a caution for heavily amplified single-cell libraries (synthesis).
- **The protocol's own analysis advice was superseded.** Clark 2017 recommends sliding-window averaging for cross-cell comparison ([[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]); tile-averaging dilutes signal and VMR-based discovery replaces it ([[10-Summaries/kremer-2024-methscan|MethSCAn]]) (synthesis).
- **Per-cell coverage figures differ.** The lead's ~10–40% at ~20M reads, Clark 2017's up to ~50% per mouse cell, and scDEEP-mC's ~30% at 20 M reads come from different cell types, depths and pipelines, so they are not directly comparable (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/bisulfite-sequencing|Bisulfite sequencing]] — The conversion chemistry scBS-seq adapts to single cells.
> - `concept` [[30-Concepts/taps|TAPS]] — Bisulfite-free, TET-assisted 5mC sequencing.
> - `concept` [[30-Concepts/sctem-seq|scTEM-seq]] — Low-cost, transposable-element-targeted single-cell methylation.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation biology and the single-cell methylome methods.

## All sources on this page

> [!info]- 14 summaries cited here
> - [[10-Summaries/chen-2025-sctaps-sccaps-plus|Chen 2025]]
> - [[10-Summaries/clark-2017-scbs-seq-protocol|Clark 2017]]
> - [[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]
> - [[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]]
> - [[10-Summaries/kremer-2024-methscan|Kremer 2024]]
> - [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT 2025]]
> - [[10-Summaries/liang-2026-scmeth-imputation-benchmark|Liang 2026]]
> - [[10-Summaries/mulqueen-2018-sci-met|Mulqueen 2018]]
> - [[10-Summaries/olova-2018-wgbs-library-bias|Olova 2018]]
> - [[10-Summaries/smallwood-2014-natmethods|Smallwood 2014]]
> - [[10-Summaries/spix-2025-scdeep-mc|Spix 2025]]
> - [[10-Summaries/zhang-2023-drop-bs|Zhang 2023]]
> - [[10-Summaries/zhao-2025-mambacpg|Zhao 2025]]
> - [[10-Summaries/zhou-2024-scdmv|Zhou 2024]]
