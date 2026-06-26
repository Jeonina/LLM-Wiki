---
type: summary
title: "Chi et al. 2026 — Single-cell mapping of regulatory DNA–protein interactions (D&D-seq)"
source: "[[00-Sources/papers/Single-cell mapping of regulatory DNA-protein interactions]]"
source_kind: paper
author: "Wei-Yu Chi, Sang-Ho Yoon, ..., Franco Izzo, Dan A. Landau, Ivan Raimondi (corresponding)"
published: 2026
ingested: 2026-06-26
doi: "10.1016/j.cell.2026.05.014"
journal: "Cell"
tags: [single-cell, DNA-protein-interaction, transcription-factor, CTCF, base-editor, multiomics, method]
entities: ["[[20-Entities/dan-a-landau]]", "[[20-Entities/franco-izzo]]", "[[20-Entities/landau-lab]]"]
concepts: ["[[30-Concepts/dd-seq]]", "[[30-Concepts/got-cha]]", "[[30-Concepts/transcription-factor-motif]]", "[[30-Concepts/chromatin-accessibility]]"]
topics: ["[[40-Topics/single-cell-multiomics]]", "[[40-Topics/chromatin-architecture]]"]
---

**Citation:** Chi et al. (2026) — *Single-cell mapping of regulatory DNA–protein interactions* — *Cell*. [DOI](https://doi.org/10.1016/j.cell.2026.05.014)

# Chi 2026 — D&D-seq

> D&D-seq (docking and deamination followed by sequencing) is a single-cell immuno-tethering method that records where a chosen DNA-binding protein sits on the genome by fusing an antibody-binding nanobody to a cytosine deaminase (DddA), which stencils protein-bound sites as C→U (read as C→T) edits. Because the edit is written into the DNA sequence itself, D&D-seq slots into standard single-cell genome, accessibility, and multi-omic workflows — adding a **DNA–protein interaction / transcription-factor-binding axis** that scATAC (which only reports openness) cannot resolve, and uniquely capturing binding in *inactive/heterochromatic* compartments.

## Key claims

- A split nb-DddA enzyme (N-terminal nanobody fusion + separately supplied C-terminal peptide) is catalytically inactive until reconstituted, avoiding nonspecific deamination; it preferentially edits cytosines in TpC (and CpC) context at protein-bound sites.
- In bulk K562 cells, nb-DddA targeting CTCF, GATA1, or GATA2 produces a bimodal deamination footprint centered on HOCOMOCO/ENCODE binding sites, with de novo motif recovery matching the targeted factor — i.e., the signal is binding-specific, not accessibility-driven.
- Coupling D&D-seq with **PTA-based whole-genome sequencing** captured 2,045 CTCF peaks *outside* open chromatin, including 196 inaccessible peaks overlapping H3K9me3/H3K27me3 heterochromatin — binding events invisible to ATAC.
- Integrated into the 10x scATAC-seq workflow (scD&D-seq), it maps TF binding per cell: CA46/K562 mixing showed cell-level specificity, ~57% FRiP for CTCF (vs ~14% for uliCUT&RUN), and **higher motif specificity than scCUT&Tag**, whose peaks are confounded by open-chromatin bleed-through.
- scD&D-seq CTCF + matched scATAC fed into the C.Origami deep-learning pipeline reconstructs Hi-C-like 3D contact maps from single-cell data — linking the TF-binding axis to 3D genome prediction.
- **D&D-GoT-ChA** (D&D-seq + GoT-ChA targeted genotyping) profiled an *IDH2^R140Q* clonal-hematopoiesis patient (VAF 0.15): genotyped 33% of 15,807 cells, found mutant cells enriched in the CD8 T compartment (FACS+nanopore validated), and showed **primary IDH2-mutant T cells have disrupted CTCF binding vs wild-type** — a same-cell mutation → DNA-protein-interaction consequence.

## Methods / evidence

Method paper with layered validation: bulk benchmarking against ENCODE ChIP-seq, single-cell mixing controls, head-to-head vs uliCUT&RUN and scCUT&Tag (FRiP, motif dominance, cross-specificity), a logistic-regression on-target peak classifier (AUC 0.84 bulk, generalizing to scD&D AUC 0.73–0.89), and a primary-tissue clinical application (PBMCs, CHIP patient). Also profiled the chromatin remodeler p300 (broader, more diffuse footprints), demonstrating the assay extends beyond sequence-specific TFs. Limitations are intrinsic to the chemistry: sparse edits per cell (needs pseudobulk/metacell aggregation, ≥250 cells for robust footprints), moderate single-cell GATA1 sensitivity, and TpC sequence-context bias.

## Surprising or load-bearing bits

- The headline for the review: D&D-seq adds a **sixth regulatory axis — direct DNA–protein occupancy / TF binding** — to the accessibility/methylation/histone/3D/physical set, and it is the first to read TF binding in *closed* chromatin at single-cell scale. Accessibility tells you a region is open; D&D tells you *who is actually bound*, even when it's closed.
- D&D-GoT-ChA is a same-cell **genotype → TF-binding** assay from the same lab that built GoT and GoT-ChA — completing a trajectory: GoT (genotype+RNA) → GoT-ChA (genotype+accessibility) → D&D-GoT-ChA (genotype+TF-occupancy).
- Writing the readout *into the DNA sequence* (like DAF-seq's deamination trick) is what makes it composable with WGS and multi-omics — same design logic as DAF-seq, applied to protein binding instead of accessibility.

## Entities mentioned

- [[20-Entities/dan-a-landau]] — senior author; extends the lab's genotype-phenotype co-capture program to DNA-protein interactions.
- [[20-Entities/franco-izzo]] — co-author; bridges from GoT-ChA to D&D-GoT-ChA.
- [[20-Entities/landau-lab]] — New York Genome Center / Weill Cornell; method origin.

## Concepts touched

- [[30-Concepts/dd-seq]] — defines this method.
- [[30-Concepts/got-cha]] — D&D-seq composes with GoT-ChA to give genotype + TF binding (D&D-GoT-ChA).
- [[30-Concepts/transcription-factor-motif]] — the binding readout is validated by de novo motif recovery.
- [[30-Concepts/chromatin-accessibility]] — D&D distinguishes "open" from "actually bound"; captures binding in closed chromatin that ATAC misses.

## Connections to other sources

- Extends [[10-Summaries/izzo-2024-got-cha]] — same lab; D&D-GoT-ChA adds a TF-binding layer onto the GoT-ChA genotype+accessibility platform.
- Shares the "write the epigenetic readout into the DNA sequence via deamination" design with [[10-Summaries/swanson-2025-daf-seq]] (DAF-seq stencils accessibility; D&D-seq stencils protein occupancy).
- Provides the empirical basis for a sixth axis in [[50-Notes/regulatory-layers-overview]] and a new direction in [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]].

## Open questions

- Per-cell edit sparsity forces pseudobulk/metacell aggregation — true single-cell-resolution TF binding (not cluster-level) is not yet achieved.
- Throughput/economics of the WGS-coupled (PTA) genome-wide mode for cohort-scale studies are not established.
- Does mutation-disrupted CTCF binding (IDH2 case) generalize across drivers and loci, or is it locus/factor-specific? One patient, one factor.
