---
type: summary
title: "Swanson et al. 2025 — DAF-seq: single-cell diploid chromatin fiber architectures"
source: "[[00-Sources/papers/Elliott_2025_NatureBiotechnology]]"
source_kind: paper
author: "Elliott G. Swanson, Yizi Mao, ... Andrew B. Stergachis (corresponding)"
published: 2025-10-20
ingested: 2026-05-07
doi: "10.1038/s41587-025-02914-3"
journal: "Nature Biotechnology"
tags: [single-cell, single-molecule, chromatin, deaminase, footprinting, DAF-seq, fiber-seq]
entities:
  - "[[20-Entities/elliott-g-swanson]]"
  - "[[20-Entities/andrew-b-stergachis]]"
concepts:
  - "[[30-Concepts/daf-seq]]"
  - "[[30-Concepts/single-molecule-footprinting]]"
  - "[[30-Concepts/fiber-seq]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/chromatin-actuation]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[40-Topics/chromatin-architecture]]"
---

# Swanson et al. 2025 — DAF-seq: single-cell diploid chromatin fiber architectures

> Thesis: existing single-molecule chromatin footprinting methods (Fiber-seq, methyltransferase stenciling) cannot survive DNA amplification — methylation marks are erased — so they are stuck as bulk assays covering ~0.001% of a single cell's genome. Replace methyl marks with **C→T deaminations**, which are sequence changes that *do* survive amplification. Result: **DAF-seq** maps single-molecule, near-nucleotide-resolution protein occupancy across nearly entire chromosomes from a single cell, with simultaneous DNA sequence and chromatin readout from the same fibers.

## Key claims

- **SsDddA (a DddA variant from *Simiaoa sunii*) is a near-ideal chromatin stenciler**: dsDNA-active cytidine deaminase, 99.8% deamination of free dsDNA, minimal sequence bias, deaminates accessible cytidines in nuclei while sparing nucleosome- and CTCF-protected ones. Optimal: 4 μM, 10 min. Median deamination 73–82% in accessible promoters vs 2.3–2.6% in protected footprints.
- **Targeted DAF-seq** sequences chosen loci to >25,000× single-molecule depth. ChIP-seq-grade single-nucleotide TF occupancy and **TF co-occupancy** can be quantified directly from the deamination pattern. Applied to NAPA promoter: 11 binding elements; element-1/element-2 cooperative interaction is 180,000× stronger than element-2's protein–DNA interaction alone (thermodynamic / Boltzmann formalism).
- **Synchronous genotype + chromatin readout from the same molecule.** Top vs bottom strand can be distinguished by C→T vs G→A pattern, enabling haplotype phasing from a single C/T heterozygous variant. Demonstrated on UBA1 (X-inactivation), SLC39A4 (eQTL), and a 1.5% VAF mosaic CC→TT variant in COLO829 BL/T mixture that ablates a CTCF site.
- **scDAF-seq**: single-cell variant. SsDddA-treat permeabilized cells → FACS → primary template-directed amplification (PTA, ResolveServices) → PacBio long-read sequencing.
  - **Up to 99% of mappable genome** covered per cell, 27–80% haplotype-phased (using parental short reads).
  - Each unique SsDddA deamination pattern serves as a UMI to deduplicate PCR amplicons and to merge overlapping reads from the same haplotype-strand into **consensus reads with N50 up to 34.5 kb** and >5,600 reads >100 kb in the deepest cell.
  - Haplotype switch error rate 2.4–3.3%.
- **Pervasive chromatin plasticity within and between cells:**
  - Two cells differ in ~63% of regulatory-element actuation states.
  - Two haplotypes within the same cell differ in ~61% — i.e. cell-to-cell trans-environment differences contribute only marginally.
  - Highly accessible / highly expressed elements are more consistent (~9–16% disagreement).
- **Co-actuation along the same fiber is distance-dependent, mirroring cohesin-mediated loops** (~100 kb domains). This is the first chromosome-length single-molecule confirmation of preferential same-fiber co-actuation; bulk Fiber-seq could only suggest it.

## Methods / evidence

Recombinant SsDddA expressed in bacteria. Mass-spec for activity. Long-read PacBio sequencing for deamination patterns. PTA from ResolveServices for whole-genome amplification of single cells (preserves the deamination pattern as a strand-specific UMI). 12 single cells sequenced, 4 deeply benchmarked. Bulk comparators: Fiber-seq, scATAC-seq, ATAC-seq, DNase-seq, ChIP-seq.

The strongest engineering claim — **"deamination marks survive amplification, methylation marks don't"** — is the lever that turns single-molecule chromatin assays from bulk-only to single-cell. Everything else follows from that.

## Surprising or load-bearing bits

- **Plasticity is mostly intra-cellular, not inter-cellular.** ~61% haplotype-vs-haplotype within the same cell, ~63% between cells — almost the same number. That kills the "cells differ because they are in different states / have different trans-factors" story for regulatory-element actuation; differences are stochastic at the fiber level even within one nucleus.
- **The deamination pattern as a UMI** is a clever side-effect of the chemistry: the combinatorial space of C→T positions on a 5 kb fiber is so large that it doubles as a unique molecular identifier without explicit barcoding.
- **scDAF-seq covers ~99% of the genome per cell** — vs ~0.01% for prior single-cell single-molecule chromatin assays. This is a four-orders-of-magnitude jump in single-cell coverage.
- **TF cooperativity quantified via thermodynamic ΔG.** Treating fiber occupancy patterns as Boltzmann-distributed states lets you compute interaction free energies between TFs from raw read counts. The 180,000× cooperative coefficient at NAPA element 1/2 is a striking number that bulk assays could never have produced.
- **Distinguishes deaminations from germline variants** by single-strand specificity (C→T from top, G→A from bottom). Same-read, same-cell genotype + chromatin readout — analogous to [[30-Concepts/got-cha]]'s goal but at single-nucleotide / single-molecule precision rather than droplet single-cell scale.

## Entities mentioned

- [[20-Entities/elliott-g-swanson]] — co-first author; UW Genome Sciences (Stergachis lab).
- [[20-Entities/andrew-b-stergachis]] — corresponding/senior author; UW Medical Genetics; group's previous Fiber-seq work is the methodological ancestor.

## Concepts touched

- [[30-Concepts/daf-seq]] — defined here.
- [[30-Concepts/single-molecule-footprinting]] — DAF-seq is the first amplifiable single-molecule footprinting method.
- [[30-Concepts/fiber-seq]] — methodological ancestor (m6A methyltransferase stenciling); DAF-seq's contribution is replacing the marks with sequence changes that survive amplification.
- [[30-Concepts/chromatin-accessibility]] — measured at single-molecule, single-nucleotide resolution.
- [[30-Concepts/chromatin-actuation]] — the paper's term for an element being in the "open" / TF-occupied state on a specific fiber. Made measurable per-fiber, per-haplotype, per-cell.

## Connections to other sources

- **Methodologically parallel to** [[10-Summaries/franco-2024-nature]] (GoT–ChA): both link DNA sequence to chromatin in single cells. GoT–ChA wins on cell number (10⁵ cells, droplet) but reads only Tn5 accessibility at low locus resolution; DAF-seq wins on resolution (single-nucleotide, single-molecule, ~99% genome per cell) but at much lower cell throughput (~10 cells deeply sequenced).
- **Conceptually downstream of** [[10-Summaries/anna-2019-nature]]'s framing — that linking sequence to functional readout in the same cell is the right unit of analysis — but in a chromatin/biophysics rather than transcriptomics/disease context.

## Open questions

- **Cell throughput vs depth.** scDAF-seq sequenced ~12 cells. Can the method scale to hundreds or thousands without losing the consensus-read benefit of PTA + deamination-UMI?
- **Cost.** Each deeply sequenced cell consumed ~91–133 Gb of PacBio. The economics of scaling to cohort-sized experiments are unclear.
- **Why is intra-cell haplotype divergence (61%) almost equal to inter-cell divergence (63%)?** The paper notes this but doesn't have a mechanism — is regulatory element actuation closer to a stochastic per-fiber event than to a programmed per-cell state?
- **Generalization beyond GM24385/GM12878.** All scDAF-seq cells profiled are lymphoblastoid. Primary tissue scDAF-seq is not demonstrated.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-025-02914-3)
