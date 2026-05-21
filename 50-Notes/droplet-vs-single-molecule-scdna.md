---
type: note
title: "Droplet-scale vs single-molecule scDNA-seq — the breadth/depth tradeoff"
aliases: [droplet vs single-molecule, breadth vs depth scDNA, scDNA platform tradeoffs]
tags: [synthesis, scDNA-seq, single-cell-multiomics, single-molecule-footprinting, methods-tradeoff]
created: 2026-05-19
updated: 2026-05-19
sources: [
  "[[10-Summaries/nam-2019-got]]",
  "[[10-Summaries/izzo-2024-got-cha]]",
  "[[10-Summaries/cortes-lopez-2023-cellstemcell]]",
  "[[10-Summaries/swanson-2025-daf-seq]]",
  "[[10-Summaries/andrewb-2020-science]]",
  "[[10-Summaries/abdulhay-2020-samosa]]",
  "[[10-Summaries/nanda-2024-smrt-tag]]",
  "[[10-Summaries/altemose-2022-dimelo-seq]]",
  "[[10-Summaries/cao-2018-sci-car]]",
  "[[10-Summaries/ma-2020-share-seq]]",
  "[[10-Summaries/pellegrino-2018-tapestri]]",
  "[[10-Summaries/shao-2025-scDNA-mosaicism-review]]",
  "[[10-Summaries/evrony-2021-scDNA-applications-review]]",
  "[[10-Summaries/gawad-2016-scgenome-review]]",
  "[[10-Summaries/baysoy-2023-multiomics-landscape]]"
]
---

# Droplet-scale vs single-molecule scDNA-seq — the breadth/depth tradeoff

> Single-cell DNA sequencing has bifurcated into two architectures that solve different problems. **Droplet/combinatorial platforms** (10x Genomics, Mission Bio Tapestri, sci-CAR, SHARE-seq, GoT/GoT-ChA) scale to 10⁴-10⁶ cells per experiment but read each cell shallowly — typically targeted loci, sparse coverage, no per-fiber resolution ([[10-Summaries/nam-2019-got]]; [[10-Summaries/izzo-2024-got-cha]]; [[10-Summaries/pellegrino-2018-tapestri]]). **Single-molecule long-read platforms** (Fiber-seq, DAF-seq, SAMOSA-Tag, SMRT-Tag, DiMeLo-seq) profile each cell deeply at per-base, per-fiber resolution but are constrained to 10-100 cells per run ([[10-Summaries/andrewb-2020-science]]; [[10-Summaries/swanson-2025-daf-seq]]; [[10-Summaries/abdulhay-2020-samosa]]; [[10-Summaries/nanda-2024-smrt-tag]]). The tradeoff is not a transient engineering problem — it is rooted in the physics of microfluidic compartmentalization vs molecule-by-molecule sequencing ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## The two architectures

### Droplet-scale: breadth at the cost of depth

Droplet platforms encapsulate one cell + one barcoded bead per droplet, lyse, amplify, and pool for sequencing ([[10-Summaries/gawad-2016-scgenome-review]]). Combinatorial-indexing variants (sci-CAR, SHARE-seq) skip the droplet step entirely, using split-pool barcoding to label cells across hundreds of thousands per experiment ([[10-Summaries/cao-2018-sci-car]]; [[10-Summaries/ma-2020-share-seq]]). The defining feature is **scale**: 10⁴-10⁶ cells per run, enough for cell-type-resolved population biology ([[10-Summaries/baysoy-2023-multiomics-landscape]]).

The defining cost is **per-cell depth**. Droplet scDNA-seq typically reads either:
- A handful of targeted loci with high allele recovery (Tapestri ~50-300 amplicons per cell at ~95% recovery, [[10-Summaries/pellegrino-2018-tapestri]]).
- Sparse genome-wide coverage with high allelic dropout (10x CNV at ~0.1× per cell, [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

The droplet architecture **cannot** read per-fiber, per-base accessibility or methylation patterns simultaneously with genotype — the amplification step destroys the original-molecule context ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

### Single-molecule: depth at the cost of breadth

Single-molecule platforms sequence individual native DNA molecules directly, preserving per-base chemical modifications and per-fiber occupancy patterns ([[10-Summaries/andrewb-2020-science]]; [[10-Summaries/swanson-2025-daf-seq]]). The two dominant chemistries:

- **Methyltransferase stenciling** — Fiber-seq (m6A on accessible adenines, [[10-Summaries/andrewb-2020-science]]), SAMOSA (m6A from EcoGII, [[10-Summaries/abdulhay-2020-samosa]]), SMRT-Tag ([[10-Summaries/nanda-2024-smrt-tag]]), DiMeLo-seq (m6A targeted by tethered Dam, [[10-Summaries/altemose-2022-dimelo-seq]]).
- **Cytidine deamination** — DAF-seq (sssDddA deaminates accessible C→U, [[10-Summaries/swanson-2025-daf-seq]]).

PacBio HiFi or Oxford Nanopore reads these modifications directly without conversion, yielding per-fiber, per-base accessibility + sequence simultaneously ([[10-Summaries/andrewb-2020-science]]; [[10-Summaries/swanson-2025-daf-seq]]).

The defining feature is **information density per cell**: each fiber tells you genotype, methylation, and accessibility on the same molecule. The defining cost is **throughput**: scDAF-seq published with 10 cells; SAMOSA-Tag with ~10²; SMRT-Tag with low hundreds ([[10-Summaries/swanson-2025-daf-seq]]; [[10-Summaries/abdulhay-2020-samosa]]; [[10-Summaries/nanda-2024-smrt-tag]]).

## Quantitative comparison

| Property | Droplet (GoT-ChA) | Single-molecule (scDAF-seq) |
|---|---|---|
| Cells per experiment | 10⁵+ ([[10-Summaries/izzo-2024-got-cha]]) | ~10 ([[10-Summaries/swanson-2025-daf-seq]]) |
| Per-cell genome coverage | <1% targeted ([[10-Summaries/izzo-2024-got-cha]]) | ~99% per cell ([[10-Summaries/swanson-2025-daf-seq]]) |
| Per-locus genotyping rate | ~38% (JAK2V617F, [[10-Summaries/izzo-2024-got-cha]]) | ~99% (any locus, [[10-Summaries/swanson-2025-daf-seq]]) |
| Reads per-fiber accessibility? | No | Yes |
| Reads per-fiber methylation? | No (separate assay) | Yes (m6A or 5mC depending on chemistry) |
| Detects haplotype-resolved structure? | No | Yes ([[10-Summaries/swanson-2025-daf-seq]]) |
| Cell-type-resolved population analysis? | Yes — cluster + DE | No — too few cells |
| Cost per cell | Low | High |
| Time per experiment | Hours-days | Days |

The two architectures answer **fundamentally different questions** about the same biology.

## What each architecture is for

### Droplet wins when:

- The biological question is **cell-type frequency or shift** — e.g., does JAK2V617F clonal hematopoiesis enrich a specific HSC subpopulation? Requires 10⁴-10⁵ cells to detect rare populations with statistical power ([[10-Summaries/izzo-2024-got-cha]]).
- The relevant signal is a **few targeted mutations**, not the whole genome — clinical mutation panels (Tapestri, [[10-Summaries/pellegrino-2018-tapestri]]).
- **Cross-modal correlation at population scale** is required — e.g., does a transcriptomic state correlate with chromatin accessibility? sci-CAR/SHARE-seq class ([[10-Summaries/cao-2018-sci-car]]; [[10-Summaries/ma-2020-share-seq]]).
- The system is **heterogeneous** and cell-type composition is the readout — e.g., immune profiling, tumor subclone identification ([[10-Summaries/baysoy-2023-multiomics-landscape]]).

### Single-molecule wins when:

- The question is about **per-fiber chromatin states** — does this allele actuate? Is the H1 locus open on the active vs inactive haplotype? ([[10-Summaries/swanson-2025-daf-seq]]).
- **Repeat-rich or highly variable regions** matter — centromeres, telomeres, rDNAs (only LRS resolves these, [[10-Summaries/andrewb-2020-science]]).
- **The same molecule must yield multiple measurements** — accessibility + sequence + methylation simultaneously, without separate library preps.
- **Allele-specific or haplotype-specific signatures** are the readout — e.g., parental-of-origin imprinting at single-fiber resolution ([[10-Summaries/altemose-2022-dimelo-seq]]).
- **TF footprinting at near-nucleotide resolution** is needed — single-molecule shows binding heterogeneity that bulk averaging smears ([[10-Summaries/doughty-2024-smf-tf]]; [[10-Summaries/pott-2017-elife]]).

## The middle ground (mostly absent)

Few platforms occupy the middle of this tradeoff space:

- **DLP+** — droplet + low-pass WGS, ~10³-10⁴ cells with ~0.1× per-cell coverage, intermediate (but still shallow per-cell, [[10-Summaries/gawad-2016-scgenome-review]]).
- **MeSMLR-seq** — methylation-aware single-molecule, but bulk DNA not single-cell ([[10-Summaries/wang-2019-mesmlr]]).
- **SMAC-seq** — single-molecule accessibility with m6A footprinting; bulk, not single-cell ([[10-Summaries/shipony-2020-smac]]).
- **NanoNOMe** — Nanopore + GpC methyltransferase accessibility; bulk.

The gap between "10 deeply-read single-molecule cells" and "10⁵ shallowly-read droplet cells" is largely unbridged as of 2026. Duplex-Multiome ([[10-Summaries/kriz-2025-duplex-multiome]]) approaches it from the droplet side by adding duplex consensus to 10x Multiome, but does not read per-fiber accessibility.

## Why the gap is persistent

The breadth/depth tradeoff is not a transient engineering problem. Two physical constraints sustain it:

1. **Microfluidic compartmentalization** demands fast, parallel chemistry (PCR, transposition) that destroys original-molecule context. Droplets can carry one cell each but cannot carry the per-fiber state through amplification ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
2. **Single-molecule sequencing** requires individual native molecules to be physically passed through a sequencing engine (PacBio ZMW, Nanopore pore). The per-molecule throughput is intrinsically lower than parallel optical sequencing of amplicons.

The implication: methods that try to scale single-molecule chemistry to droplet-scale cells (e.g., scDAF-seq via plate sorting + PacBio) are bound by ZMW throughput, not by cell-isolation chemistry ([[10-Summaries/swanson-2025-daf-seq]]). PacBio Revio (~25M ZMW) raises the ceiling but does not eliminate the tradeoff.

## The single-cell scientist's choice

For mosaicism research specifically, the choice is usually clear from the biological question:

- **Cell-type-resolved mosaic-mutation burden** in aged tissue → droplet PTA workflows ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]).
- **Per-fiber consequences of a regulatory mutation** (e.g., does an enhancer SNV ablate actuation on the mutant haplotype?) → single-molecule footprinting ([[10-Summaries/swanson-2025-daf-seq]]).
- **Both** — currently impossible in one experiment. Combine droplet for population sampling + single-molecule for follow-up mechanistic depth on selected cells.

For multi-omics specifically, the breadth-vs-depth tension is the **single most important methodological choice point** in the field ([[10-Summaries/baysoy-2023-multiomics-landscape]]). Reviews that recommend "use multi-omics" without specifying which architecture obscure this fundamental tradeoff ([[10-Summaries/baysoy-2023-multiomics-landscape]]; [[10-Summaries/evrony-2021-scDNA-applications-review]]).

## What would close the gap

A method that reads **per-fiber accessibility + sequence + methylation at >10⁴ cells per experiment** would unify the two architectures. Three candidate paths:

1. **High-throughput PacBio Revio scDAF-seq** — current bottleneck is ZMW × cells, not chemistry. Revio's 25M ZMW could plausibly support 10³-10⁴ cells per run if throughput keeps improving (synthesis).
2. **Long-read combinatorial-indexing on Nanopore** — adapt sci-CAR-style barcoding to ONT reads. No published implementation as of 2026.
3. **Droplet single-molecule hybrid** — encapsulate one cell per droplet but skip amplification, instead concentrating native molecules for direct sequencing. Limited by per-cell molecule count (a single mammalian nucleus has ~6 pg DNA; current direct-sequencing requires nanograms).

None of these is currently in published form. The breadth-depth tradeoff is the field's most significant unresolved methodological tension.

## How this synthesis interacts with other wiki notes

- **[[50-Notes/single-cell-duplex-sequencing]]** — duplex closes the *fidelity* dimension at single-cell; this note describes the orthogonal *depth-per-cell* dimension. Both tensions are present in scDNA-seq simultaneously.
- **[[50-Notes/regulatory-layers-overview]]** — single-molecule reads multiple layers per fiber; droplet reads per cell with separate libraries. The architecture choice determines which regulatory questions are tractable.
- **[[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]]** — the synthesis gap is largely a *consequence* of the breadth-depth tradeoff described here. Resolving the breadth-depth tradeoff would resolve the synthesis gap.

## Related

- [[40-Topics/scdna-seq]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/long-read-sequencing]]
- [[30-Concepts/scdna-seq]] · [[30-Concepts/single-molecule-footprinting]] · [[30-Concepts/got]] · [[30-Concepts/got-cha]]
- [[30-Concepts/fiber-seq]] · [[30-Concepts/daf-seq]] · [[30-Concepts/samosa]]
- [[50-Notes/synthesis-targets]] — this note resolves the "Droplet-scale vs single-molecule scDNA-seq" target
