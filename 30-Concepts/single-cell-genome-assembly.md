---
type: concept
title: Single-cell genome assembly
aliases: [de novo single-cell assembly, SPAdes, Velvet-SC, IDBA-UD, E+V-SC]
tags: [assembly, de-Bruijn-graph, MDA, uneven-coverage, chimera, metagenomics, uncultivated-bacteria]
created: 2026-08-13
updated: 2026-10-07
---

# Single-cell genome assembly

> De novo reconstruction of a genome from the reads of one amplified cell. Distinct from every other analysis in this wiki in that it has **no reference genome** — which is exactly why it was the first place [[mda|MDA]]'s coverage pathology had to be solved computationally.

## Why it is a separate problem

Standard de Bruijn assemblers prune sequencing errors by discarding low-multiplicity *k*-mers, which assumes near-uniform coverage. Single-cell MDA data violates that assumption catastrophically. In multicell *E. coli* most positions sit at 450–800× with only 0.1% below 450×; in single-cell *E. coli*, **5% of positions have <10× and 11% have <30×** — and ~30× is the usual minimum for gap-free assembly ([[10-Summaries/chitsaz-2011-velvet-sc]]). Worse, the multiplicity ordering inverts: **incorrect *k*-mers in high-depth regions can outnumber correct *k*-mers in low-depth regions**, so no single global threshold works ([[10-Summaries/peng-2012-idba-ud]]).

A second MDA artifact compounds it: **chimeras** formed during φ29's branching amplification join non-contiguous sequences, producing both chimeric reads and chimeric read-pairs ([[10-Summaries/chitsaz-2011-velvet-sc]]). Chimeras are also why single-cell [[structural-variants|structural variants]] resist detection generally ([[10-Summaries/huang-2015-scwga-review]]).

## Three solutions, 2011–2012

| Tool | Core fix | Read pairs | Chimeras |
|---|---|---|---|
| Velvet-SC / E+V-SC ([[10-Summaries/chitsaz-2011-velvet-sc]]) | Progressively increasing coverage cutoff, coupled to EULER-SR error correction | Discarded deliberately, to avoid misassembly from chimeric pairs | Quantified (2% of *E. coli*, 0.5% of *S. aureus* read pairs) but not removed |
| IDBA-UD ([[10-Summaries/peng-2012-idba-ud]]) | Multiple depth-relative thresholds; iterative *k* from k_min to k_max carrying contigs forward as reads; local assembly with paired-end info | Used for local assembly of low-depth short repeats | Not addressed |
| SPAdes ([[10-Summaries/bankevich-2012-spades]]) | Paired de Bruijn graph + *k*-bimer adjustment; multisized de Bruijn graph; Hammer error correction | Used fully — the stated improvement over E+V-SC | Explicit detection and removal stage |

Two SPAdes authors coauthored E+V-SC and stated the reason for rebuilding rather than patching: *"one needs to change algorithmic design (rather than just modify existing tools) to fully utilize the potential of SCS"* ([[10-Summaries/bankevich-2012-spades]]). SPAdes is the one of the three that remained in routine use. (synthesis)

## What it delivered

Single *E. coli* and *S. aureus* cells yield **>91% of genes within contigs**, against 95% from a multicell *E. coli* assembly ([[10-Summaries/chitsaz-2011-velvet-sc]]). The motivating application is uncultivated organisms — most microbes cannot be cultured — and the demonstration was a genome from a single cell of the marine SAR324 Deltaproteobacteria clade, with metabolic reconstruction indicating an aerobic, motile, chemotaxic organism ([[10-Summaries/chitsaz-2011-velvet-sc]]). Metagenomics is gene-centric and structurally cannot say which genes co-occur in one organism; single-cell assembly can ([[10-Summaries/chitsaz-2011-velvet-sc]]).



## The generalisable lesson

This is the earliest place in the corpus where WGA's problems are named as **computational rather than experimental** ([[10-Summaries/chitsaz-2011-velvet-sc]]) — a claim that recurs almost verbatim a decade later in the mosaic-variant-calling literature ([[10-Summaries/lahnemann-2021-natcomm]]; [[10-Summaries/ha-2023-natmethods]]). And the abundance-inversion problem it identifies reappears, in a different data type, as the allelic-imbalance problem that single-cell variant callers solve ([[10-Summaries/dong-2017-sccaller]]; [[10-Summaries/luquette-2019-natcomm]]). (synthesis)

Bacterial single-cell genomics matured years before human single-cell variant calling because gene *presence* is far more robust to dropout than base-level genotype. (synthesis)

## Added 2026-10-07

Single-cell Hi-C can scaffold single-cell draft assemblies. Using SALSA2, 20 scWGS cells plus 12 scNanoHi-C cells reached NG50 2.49 Mb, versus 1.34 Mb for 30 scWGS cells alone (HG002) ([[10-Summaries/li-2023-scnanohi-c]]).

Partial de novo assembly of human single-cell genomes has been shown from HiFi reads after a self-BLAST chimera filter: hifiasm primary assemblies of 598.3 Mb and 454.1 Mb (~19% and 15% of the reference), contig N50 of 35–42 kb, ~40 Mb of haplotype-alternative contigs, and 12.8% complete BUSCO genes in the best cell ([[10-Summaries/hard-2023-long-read-scwgs]]).


## Related

- [[mda]] · [[scwga]] · [[scwga-chemistries]] · [[structural-variants]] · [[highly-repetitive-regions]] · [[40-Topics/whole-genome-amplification]]
