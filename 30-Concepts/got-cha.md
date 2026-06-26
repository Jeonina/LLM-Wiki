---
type: concept
title: GoT–ChA (Genotyping of Targeted loci with single-cell Chromatin Accessibility)
aliases: [GoT-ChA, GoTChA]
tags: [single-cell, scATAC-seq, genotyping, gDNA, chromatin, method]
created: 2026-05-07
updated: 2026-05-07
---

# GoT–ChA (Genotyping of Targeted loci with single-cell Chromatin Accessibility)

> Droplet-based single-cell method that captures somatic genotype and chromatin accessibility from the same nucleus by amplifying the mutation locus directly from genomic DNA inside 10x scATAC-seq droplets — bypassing the expression-level and transcript-distance limitations of [[got]].

## Definition

GoT–ChA modifies 10x Genomics scATAC-seq by adding two custom **GoT–ChA primers** to the cell-barcoding PCR mixture before droplet generation ([[10-Summaries/izzo-2024-got-cha]]). Inside each droplet, the primers anneal to the mutation-containing genomic locus. A linear amplification step is followed by exponential amplification, producing barcoded amplicons that carry both the cell barcode (CBC) and the genotype-encoding sequence. The amplicon library is processed alongside the scATAC-seq library; an R package handles GoT–ChA → scATAC integration end-to-end.

Genotype capture **does not require target-site tagmentation** — amplicons inherit the capture sequence from the cell-barcoding chemistry — so genotyping efficiency is independent of locus accessibility.

## Why it matters

GoT–ChA solves the two biggest limitations of [[got]] in one architectural change: switching the genotype source from cDNA (one-or-more copies, expression-dependent) to **genomic DNA (always exactly two copies per diploid nucleus, expression-independent)**. The practical consequence is a **~4× jump in single-cell genotyping rate** for low-expression drivers like JAK2 (~38% with GoT–ChA vs ~7–10% with cDNA-based methods).

It also opens the chromatin readout — a richer functional layer than RNA for tracking how somatic mutations rewire regulatory programs. The pro-inflammatory chromatin priming of JAK2V617F-mutant HSCs visible in [[10-Summaries/izzo-2024-got-cha]] could not be measured with [[got]].

## Variants and refinements

- **Single-target GoT–ChA** ([[10-Summaries/izzo-2024-got-cha]]) — TP53 R248, JAK2 V617, NRAS Q61, TP53 M133, FOXO1 S22 each validated.
- **Multiplexed GoT–ChA** ([[10-Summaries/izzo-2024-got-cha]]) — up to 4 targets simultaneously; per-cell genotyping for individual loci ranges 56–73%.
- **GoT–ChA + DOGMA-seq integration** ([[10-Summaries/izzo-2024-got-cha]]) — using mitochondrial variant + cell-surface protein bridges, GoT–ChA can be imputation-extended onto DOGMA-seq, giving genotype + chromatin + RNA + surface protein in single cells.
- **D&D-GoT-ChA** ([[10-Summaries/chi-2026-dd-seq]]) — composes GoT–ChA with [[dd-seq|D&D-seq]] to add a same-cell **transcription-factor-binding** readout; applied to an IDH2^R140Q CHIP patient, it showed mutant T cells have disrupted CTCF binding vs wild-type — a same-cell genotype → DNA-protein-interaction consequence.

## Contested points

- Multiplexing efficiency drops with target count; per-locus genotyping rates fall from ~64% (single) to ~58–73% (multiplex). The paper does not characterize how this scales beyond 4 targets.
- DOGMA integration is **imputation-based**, not direct co-capture — generalization to systems without informative mitochondrial variants or surface proteins is unclear ([[10-Summaries/izzo-2024-got-cha]] open question).

## Examples

- 21 JAK2V617F MF samples, 150,643 cells → 38.1% genotyping rate, revealing cell-intrinsic NF-κB / TGF-β chromatin priming in mutant HSCs and a profibrotic chromatin signature in mutant MkPs ([[10-Summaries/izzo-2024-got-cha]]).
- JAK2V617F clonal hematopoiesis sample: STAT motif accessibility increase visible *before* overt MPN — pre-clinical chromatin signature.

## Related

- [[got]] — direct predecessor; same lab, same 10x platform, RNA → chromatin and cDNA → gDNA.
- [[circularization-got]] — workaround in the GoT framework that GoT–ChA supersedes.
- [[chromatin-accessibility]]
- [[jak2-v617f]]
- [[dogma-seq]]
- [[dd-seq]] — D&D-GoT-ChA extension (genotype + TF binding)
- [[40-Topics/single-cell-multiomics]]
- [[20-Entities/franco-izzo]]
- [[20-Entities/landau-lab]]
