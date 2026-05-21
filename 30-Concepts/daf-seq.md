---
type: concept
title: DAF-seq (Deaminase-Assisted single-molecule chromatin Fiber sequencing)
aliases: [DAF-seq, scDAF-seq]
tags: [single-molecule, single-cell, chromatin, deaminase, footprinting, method]
created: 2026-05-07
updated: 2026-05-07
---

# DAF-seq (Deaminase-Assisted single-molecule chromatin Fiber sequencing)

> Single-molecule chromatin footprinting method that uses the dsDNA cytidine deaminase **SsDddA** to stencil protein occupancy as C→T sequence changes — which, unlike methylation marks, **survive DNA amplification** and so enable single-cell extension (scDAF-seq) covering up to 99% of an individual cell's genome.

## Definition

SsDddA (a *Simiaoa sunii* DddA variant, expressed in *E. coli*) deaminates accessible cytidines in nuclei to uridine; subsequent PCR or whole-genome amplification converts these to thymidine, producing C→T changes on the top strand and G→A changes on the bottom strand of accessible DNA ([[10-Summaries/swanson-2025-daf-seq]]). Nucleosome- and TF-protected DNA escapes deamination, so the deamination pattern along a fiber is a **near-nucleotide-resolution footprint of protein occupancy**.

Two operational modes:

- **Targeted DAF-seq** — amplify chosen loci to >25,000× single-molecule depth; resolves TF cooperativity, haplotype-specific actuation, and low-VAF mosaic variant impact.
- **scDAF-seq** — sort SsDddA-treated single cells by FACS, perform primary template-directed amplification (PTA), sequence on PacBio. Each unique deamination pattern serves as a per-fiber UMI, enabling consensus-read assembly with N50 up to 34.5 kb across ~99% of mappable autosomal genome per cell.

## Why it matters

Prior single-molecule chromatin footprinting methods (notably [[fiber-seq]] and other methyltransferase stencilers) lose their marks during DNA amplification. They are stuck as bulk assays covering ~0.001% of a single cell's genome. Deamination produces *sequence* changes, not modifications, so it survives any amplification chemistry — the load-bearing change that makes single-cell single-molecule chromatin profiling possible at chromosome scale.

It also yields **synchronous DNA sequence + chromatin readout from the same fiber**: top vs bottom strand can be distinguished by C→T vs G→A pattern, so haplotype phasing from a single C/T heterozygous variant works directly. The same single fiber gives genotype + chromatin state — a different solution to the same single-cell genotype-phenotype linking problem that [[got]] and [[got-cha]] address with droplet barcoding.

## Variants and refinements

- **Targeted DAF-seq** ([[10-Summaries/swanson-2025-daf-seq]]) — bulk single-molecule with PCR enrichment; up to 230,000× enrichment over genome-wide.
- **scDAF-seq** ([[10-Summaries/swanson-2025-daf-seq]]) — single-cell variant; FACS + PTA + PacBio.
- Reaction conditions: 4 μM SsDddA, 10 min, optimal across NAPA / WASF1 promoter benchmarks.

## Contested points

- **Cell throughput.** scDAF-seq sequenced 12 cells (deeply benchmarked: 4). Whether the method scales to hundreds/thousands of cells is unclear.
- **Cost.** Each deeply sequenced cell consumed ~91–133 Gb of PacBio HiFi data — economics of cohort-scale studies are not established.
- Generalization to primary tissue is not yet demonstrated; all scDAF-seq cells profiled are GM24385 lymphoblastoid.

## Examples

- **NAPA promoter cooperativity**: thermodynamic analysis identified a 180,000× cooperative binding interaction between elements 1 and 2 (USF1/2 + NFY-A) ([[10-Summaries/swanson-2025-daf-seq]]).
- **SLC39A4 eQTL mechanism**: rs2280838-T haplotype increases liver expression by altering nucleosome positioning over the promoter — visible as a chromatin epiallele only at single-molecule resolution.
- **Low-VAF mosaic variant**: a 1.5% VAF CC→TT mutation in COLO829 BL/T mixture ablates a CTCF binding element, with chromatin loss visible only on the variant reads.
- **Pervasive plasticity**: between-cell regulatory-element actuation differs by ~63%; haplotype-vs-haplotype within the same cell differs by ~61%.

## Related

- [[fiber-seq]] — methodological ancestor; methyltransferase-based stenciling.
- [[single-molecule-footprinting]]
- [[chromatin-actuation]]
- [[chromatin-accessibility]]
- [[got-cha]] — droplet-scale alternative for linking sequence to chromatin in single cells.
- [[20-Entities/elliott-g-swanson]]
- [[20-Entities/andrew-b-stergachis]]
- [[40-Topics/chromatin-architecture]]
