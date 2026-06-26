---
type: concept
title: "D&D-seq (docking and deamination followed by sequencing)"
aliases: [D&D-seq, DD-seq, docking and deamination, scD&D-seq, D&D-GoT-ChA]
tags: [single-cell, DNA-protein-interaction, transcription-factor, base-editor, CTCF, method]
created: 2026-06-26
updated: 2026-06-26
---

# D&D-seq (docking and deamination followed by sequencing)

> A single-cell immuno-tethering method that records where a DNA-binding protein is bound on the genome by fusing an antibody-binding nanobody to a cytosine deaminase (DddA), which writes C→U (read as C→T) edits into protein-bound sites — adding a direct **DNA–protein interaction / transcription-factor-binding** readout to single-cell genome and multi-omic workflows ([[10-Summaries/chi-2026-dd-seq]]).

## Definition

D&D-seq couples a secondary nanobody (which binds an antibody against the protein of interest) to the double-stranded-DNA cytosine deaminase DddA ([[10-Summaries/chi-2026-dd-seq]]). The enzyme is split: an inactive nanobody-DddA_NT fusion is reconstituted only when the separately supplied C-terminal peptide and Zn²⁺ are added, preventing nonspecific deamination ([[10-Summaries/chi-2026-dd-seq]]). At antibody-bound genomic sites the reconstituted enzyme stencils cytosines (TpC/CpC context) as C→U, surviving amplification as C→T sequence changes that mark binding footprints ([[10-Summaries/chi-2026-dd-seq]]). Because the readout is written into the DNA sequence, it integrates with scATAC-seq, PTA-based WGS, and combinatorial-barcoding multi-omic protocols ([[10-Summaries/chi-2026-dd-seq]]).

## Why it matters

Chromatin accessibility ([[chromatin-accessibility]]) tells you a region is *open*; D&D-seq tells you *which protein is actually bound there* — a distinction scATAC cannot make ([[10-Summaries/chi-2026-dd-seq]]). Uniquely, by coupling to whole-genome sequencing it captures binding in **inactive/heterochromatic compartments** (CTCF peaks overlapping H3K9me3/H3K27me3) that accessibility assays miss entirely ([[10-Summaries/chi-2026-dd-seq]]). In benchmarking it achieved higher motif specificity than scCUT&Tag, whose peaks are confounded by open-chromatin bleed-through (~57% vs ~14% FRiP against uliCUT&RUN for CTCF) ([[10-Summaries/chi-2026-dd-seq]]). For the wiki's regulatory-layers framing it supplies a distinct sixth axis — TF/DNA-protein occupancy — see [[50-Notes/regulatory-layers-overview]] (synthesis).

## Variants and refinements

- **Bulk D&D-seq** ([[10-Summaries/chi-2026-dd-seq]]) — CTCF/GATA1/GATA2/SP1/p300 targets in K562; validated against ENCODE ChIP-seq.
- **D&D-seq + WGS (PTA)** ([[10-Summaries/chi-2026-dd-seq]]) — genome-wide binding including non-accessible chromatin.
- **scD&D-seq** ([[10-Summaries/chi-2026-dd-seq]]) — integrated into 10x scATAC-seq; per-cell binding (pseudobulk/metacell aggregation, ≥250 cells for robust footprints).
- **D&D-GoT-ChA** ([[10-Summaries/chi-2026-dd-seq]]) — composed with [[got-cha]] genotyping for same-cell **genotype + TF binding**; applied to an IDH2^R140Q CHIP patient, showing mutant T cells have disrupted CTCF binding.

## Contested points

- Per-cell edit sparsity means true single-cell-resolution binding is not yet achieved — interpretation is cluster/pseudobulk-level ([[10-Summaries/chi-2026-dd-seq]]).
- TpC sequence-context bias and moderate single-cell GATA1 sensitivity limit uniform applicability across factors ([[10-Summaries/chi-2026-dd-seq]]).

## Examples

- IDH2^R140Q clonal hematopoiesis: 33% of 15,807 cells genotyped, mutant cells enriched in CD8 T compartment, mutant T cells show disrupted CTCF binding vs wild-type ([[10-Summaries/chi-2026-dd-seq]]).
- scD&D CTCF + scATAC fed to the C.Origami pipeline reconstructs Hi-C-like 3D contact maps from single-cell input ([[10-Summaries/chi-2026-dd-seq]]).

## Related

- [[got-cha]] — composes with D&D-seq as D&D-GoT-ChA (genotype + TF binding)
- [[daf-seq]] — shares the "stencil epigenetic state into DNA via deamination" design (accessibility vs protein occupancy)
- [[chromatin-accessibility]] — D&D distinguishes bound from merely open
- [[transcription-factor-motif]] — binding validated by de novo motif recovery
- [[cut-and-tag]] — antibody-tethered alternative D&D-seq outperforms on specificity
- [[3d-genome]] — scD&D CTCF enables single-cell 3D structure prediction
- [[40-Topics/single-cell-multiomics]]
- [[40-Topics/chromatin-architecture]]
- [[20-Entities/landau-lab]]
