---
type: concept
title: GoT–ChA (Genotyping of Targeted loci with single-cell Chromatin Accessibility)
aliases: [GoT-ChA, GoTChA]
tags: [single-cell, scATAC-seq, genotyping, gDNA, chromatin, method]
created: 2026-05-07
updated: 2026-10-12
---

# GoT–ChA (Genotyping of Targeted loci with single-cell Chromatin Accessibility)

> Droplet-based single-cell method that captures somatic genotype and chromatin accessibility from the same nucleus by amplifying the mutation locus directly from genomic DNA inside 10x scATAC-seq droplets — bypassing the expression-level and transcript-distance limitations of [[got]] ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

> [!abstract] 한눈에
> GoT–ChA는 10x scATAC-seq droplet 안에서 mutation locus를 genomic DNA로부터 직접 증폭해, 같은 핵에서 somatic genotype과 chromatin accessibility를 함께 읽는 방법이다 ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]). Genotype 출처를 cDNA에서 gDNA로 바꾼 덕분에 JAK2처럼 발현이 낮은 driver의 genotyping rate가 약 4배 올랐다 ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Definition

GoT–ChA modifies 10x Genomics scATAC-seq by adding two custom **GoT–ChA primers** to the cell-barcoding PCR mixture before droplet generation ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]). Inside each droplet, the primers anneal to the mutation-containing genomic locus. A linear amplification step is followed by exponential amplification, producing barcoded amplicons that carry both the cell barcode (CBC) and the genotype-encoding sequence. The amplicon library is processed alongside the scATAC-seq library; an R package handles GoT–ChA → scATAC integration end-to-end ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

Genotype capture **does not require target-site tagmentation** — amplicons inherit the capture sequence from the cell-barcoding chemistry — so genotyping efficiency is independent of locus accessibility ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Why it matters

- GoT–ChA solves the two biggest limitations of [[got]] in one architectural change: switching the genotype source from cDNA (one-or-more copies, expression-dependent) to **genomic DNA (always exactly two copies per diploid nucleus, expression-independent)** ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- The practical consequence is a **~4× jump in single-cell genotyping rate** for low-expression drivers like JAK2 (~38% with GoT–ChA vs ~7–10% with cDNA-based methods) ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- It also opens the chromatin readout — a richer functional layer than RNA for tracking how somatic mutations rewire regulatory programs. The pro-inflammatory chromatin priming of JAK2V617F-mutant HSCs could not be measured with [[got]] ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Variants and refinements

| Variant | Added readout | What was shown | Source |
|---|---|---|---|
| Single-target GoT–ChA | Genotype + chromatin accessibility | TP53 R248, JAK2 V617, NRAS Q61, TP53 M133 each validated | ([[10-Summaries/izzo-2024-got-cha\|Izzo 2024]]) |
| Multiplexed GoT–ChA | Up to 4 targets simultaneously | Per-locus genotyping rates ~58–73% in multiplex, against ~64% single-target | ([[10-Summaries/izzo-2024-got-cha\|Izzo 2024]]) |
| GoT–ChA + [[dogma-seq]] integration | RNA + surface protein, by imputation | Mitochondrial variant + cell-surface protein bridges extend GoT–ChA onto DOGMA-seq, giving genotype + chromatin + RNA + surface protein in single cells | ([[10-Summaries/izzo-2024-got-cha\|Izzo 2024]]) |
| D&D-GoT-ChA | Same-cell transcription-factor binding, via [[dd-seq\|D&D-seq]] | In an IDH2^R140Q CHIP patient, mutant T cells had disrupted CTCF binding vs wild-type — a same-cell genotype → DNA-protein-interaction consequence | ([[10-Summaries/chi-2026-dd-seq\|Chi 2026]]) |

## Evidence and examples

- 21 JAK2V617F MF samples, 150,643 cells → 38.1% genotyping rate ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- In those samples, mutant HSCs showed cell-intrinsic NF-κB / TGF-β chromatin priming and mutant MkPs a profibrotic chromatin signature ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- JAK2V617F clonal hematopoiesis sample: STAT motif accessibility increase visible *before* overt MPN — pre-clinical chromatin signature.

## Contested points

- Multiplexing efficiency drops with target count; per-locus genotyping rates fall from ~64% (single) to ~58–73% (multiplex). The paper does not characterize how this scales beyond 4 targets.
- DOGMA integration is **imputation-based**, not direct co-capture — generalization to systems without informative mitochondrial variants or surface proteins is unclear ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]] open question).

## Related

> [!cards]
> - `concept` [[30-Concepts/got|GoT]] — Direct predecessor; same lab, same 10x platform, RNA → chromatin and cDNA → gDNA.
> - `concept` [[30-Concepts/circularization-got|Circularization GoT]] — Workaround in the GoT framework that GoT–ChA supersedes.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — The regulatory readout GoT–ChA pairs with genotype.
> - `concept` [[30-Concepts/jak2-v617f|JAK2 V617F]] — The MPN driver used to benchmark GoT–ChA.
> - `concept` [[30-Concepts/dogma-seq|DOGMA-seq]] — Multiome assay GoT–ChA is imputed onto.
> - `concept` [[30-Concepts/dd-seq|D&D-seq]] — D&D-GoT-ChA extension (genotype + TF binding).
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Joint measurement of several layers in one cell.
> - `entity` [[20-Entities/franco-izzo|Franco Izzo]] — First author of GoT–ChA.
> - `entity` [[20-Entities/landau-lab|Landau lab]] — Lab that developed GoT and GoT–ChA.

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/chi-2026-dd-seq|Chi 2026]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
