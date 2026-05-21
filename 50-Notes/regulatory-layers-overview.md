---
type: note
title: "Regulatory layers — the four (or five) axes of epigenome interpretation"
aliases: [regulatory layers, epigenome layers, regulatory axes, four regulatory layers]
tags: [synthesis, epigenome, regulation, overview, entry-point]
created: 2026-05-19
updated: 2026-05-19
sources: [
  "[[10-Summaries/clark-2018-scnmt-seq]]",
  "[[10-Summaries/hou-2016-sctrio-seq]]",
  "[[10-Summaries/swanson-2025-daf-seq]]",
  "[[10-Summaries/izzo-2024-got-cha]]",
  "[[10-Summaries/baysoy-2023-multiomics-landscape]]",
  "[[10-Summaries/vandereyken-2023-scmultiomics-review]]"
]
---

# Regulatory layers — the four (or five) axes of epigenome interpretation

> When asking "what does this region of DNA do, and is it active in this cell?", the field reads four molecular axes — **accessibility, DNA methylation, histone modifications, 3D genome organization** — plus a fifth structural/physical axis (lamina position, phase separation, mechanics) that gates which of the four are even possible at a given locus. This page is an entry point that maps each layer to its concept pages, single-cell assays, and cross-layer dependencies. (synthesis)

## The four molecular layers

### 1. Chromatin accessibility (open chromatin)

**What it measures.** Whether DNA is free of nucleosomes and available for TF binding and transcription machinery. The most direct readout of "is this region usable right now?" ([[30-Concepts/chromatin-accessibility]]).

**Bulk assays.** [[30-Concepts/dnase-seq]] (DNase I), MNase-seq, FAIRE-seq, [[30-Concepts/atac-seq]] (Tn5 transposase — current standard).

**Single-cell assays.** scATAC-seq is the workhorse; [[30-Concepts/daf-seq]] and [[30-Concepts/fiber-seq]] provide single-molecule per-fiber accessibility via methyltransferase/deaminase stenciling; [[30-Concepts/got-cha]] couples accessibility to targeted genotype calls.

**Interpretive role.** Accessibility is the layer most directly tied to **cell-type identity** at regulatory elements (enhancers, promoters). It's the first thing you'd want to know about a mosaic mutation's locus.

### 2. DNA methylation

**What it measures.** Covalent modifications of cytosine bases — primarily 5mC (and 5hmC as an intermediate / signaling mark). At CpG islands in promoters: typically silencing. At gene bodies and enhancers: more nuanced ([[30-Concepts/dna-methylation]], [[30-Concepts/cpg-island]], [[30-Concepts/5hmc]]).

**Bulk assays.** [[30-Concepts/bisulfite-sequencing|Bisulfite-seq]] (WGBS), reduced-representation BS-seq, EM-seq, oxBS-seq for 5hmC.

**Single-cell assays.** scBS-seq, scNMT-seq ([[30-Concepts/scnmt-seq]]) for joint methylation + accessibility + RNA, [[30-Concepts/simple-seq]] for joint 5mC + 5hmC, [[30-Concepts/splicool-seq]] for 5mC + accessibility at scale.

**Interpretive role.** Methylation encodes **stable cell-state memory** ([[30-Concepts/epigenetic-memory]], [[30-Concepts/epigenetic-aging]]). It's slower-changing than accessibility — a mutation in a methylated CpG can have inherited consequences across cell divisions.

### 3. Histone modifications

**What it measures.** Post-translational modifications on histone tails (H3K4me3 = active promoter, H3K27ac = active enhancer, H3K27me3 = polycomb-repressed, H3K9me3 = heterochromatin, etc.) that recruit/repel chromatin machinery ([[30-Concepts/histone-modifications]], [[30-Concepts/enhancer-states]]).

**Bulk assays.** [[30-Concepts/chip-seq]] (antibody pull-down + seq); [[30-Concepts/cut-and-run]] and [[30-Concepts/cut-and-tag]] (tethered enzyme, lower-input modern replacements).

**Single-cell assays.** scCUT&Tag, [[30-Concepts/chic-seq]], [[30-Concepts/scicut-tag]] (combinatorial-indexing), [[30-Concepts/multi-tag]] (multi-epitope), [[30-Concepts/scchix-seq]] (two histone marks per cell via deconvolution), [[30-Concepts/6-base-cut-and-tag]] (histone + 5mC + 5hmC per fragment).

**Interpretive role.** Histone marks give the **functional annotation** of a region — accessibility tells you it's open, but H3K27ac vs H3K27me3 tells you whether it's a poised enhancer or a polycomb domain. Marks are not independent of accessibility; they're a higher-resolution interpretation of it.

### 4. 3D genome organization

**What it measures.** How chromatin folds in 3D — A/B compartments (active vs inactive megabase domains), TADs (topologically associating domains), and CTCF/cohesin loops connecting enhancers to promoters across linear distance ([[30-Concepts/3d-genome]], [[30-Concepts/chromatin-compartments]]).

**Bulk assays.** Hi-C, Micro-C, ChIA-PET, [[30-Concepts/damid]] (lamina contacts).

**Single-cell assays.** scHi-C, [[30-Concepts/dip-c]] (diploid resolution), [[30-Concepts/igs]] (in-situ genome sequencing — preserves spatial coordinates).

**Interpretive role.** 3D organization explains **which enhancer regulates which gene**. Two regulatory elements at the same linear distance can have very different effects depending on whether they're in the same TAD. A mutation in an enhancer can only act on genes its TAD allows it to contact.

## The fifth axis: structural/physical

This sits adjacent to "3D genome" but is conceptually distinct: it's about **where in the nucleus** a locus lives and **what physical environment** it's embedded in, not whether two loci touch.

- **Lamina association** ([[30-Concepts/lamina-associated-domains]]) — LADs are gene-poor, heterochromatic, late-replicating regions tethered to the nuclear periphery. Mutually exclusive with active transcription in most cases.
- **Phase separation** ([[30-Concepts/chromatin-phase-separation]]) — heterochromatin (HP1-mediated) and active condensates (Pol II/Mediator-mediated) behave as distinct liquid-like phases, sorting loci by biophysical compatibility.
- **Mechanical properties** ([[30-Concepts/chromatin-mechanical-properties]]) — chromatin stiffness, density, and force response constrain accessibility and replication.

**Interpretive role.** This layer **gates** the four molecular layers. A locus in a LAD is by definition closed, methylated, and H3K9me3-marked — you don't measure those independently, you measure the physical state once and it predicts the rest. The wiki is still developing this axis; see [[40-Topics/chromatin-architecture]].

## Why "four layers" is a useful framing

Each layer captures a different *kind* of regulatory information:

| Layer | Temporal scale | Heritability across divisions | What it tells you |
|---|---|---|---|
| Accessibility | Minutes–hours | Low (re-established) | Is this region usable *now*? |
| Methylation | Hours–days, often lifetimes | High (semi-conservative copying) | What is this region's *memory*? |
| Histone marks | Variable (some seconds, some persistent) | Moderate (some marks copied) | What is this region's *function*? |
| 3D genome | Stable across cell cycle | Moderate | Which other regions does this *talk to*? |

This is why **scNMT-seq** ([[10-Summaries/clark-2018-scnmt-seq]]) was a landmark: by reading accessibility + methylation in the same cell, it showed the **coupling between the two layers strengthens along differentiation** — a finding that would have been impossible with either layer alone.

## Cross-layer dependencies (synthesis)

The four layers are not independent. A partial dependency map:

- **Accessibility ↔ Methylation.** CpG methylation at promoters tends to close chromatin; conversely, accessible regions are usually hypomethylated. scNMT-seq quantifies this coupling per cell.
- **Accessibility ↔ Histone marks.** Active marks (H3K4me3, H3K27ac) overlap accessible regions; repressive marks (H3K9me3, H3K27me3) overlap closed regions. CUT&Tag + ATAC at the same locus distinguishes "open + active" from "open + poised".
- **3D ↔ all three molecular layers.** Compartment A = accessible + unmethylated + active marks. Compartment B = closed + methylated + repressive marks. TAD boundaries co-localize with CTCF binding and accessible chromatin.
- **Physical axis ↔ all four.** LADs predict closed + methylated + H3K9me3 + Compartment B simultaneously. This is why "where in the nucleus" is often more parsimonious than measuring four marks.

The implication for mosaicism interpretation ([[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]]): you don't need to measure all four layers to know a region's regulatory state. Measuring one or two well-chosen layers often suffices, because the others are predictable from them. **Duplex-Multiome** (point mutations + accessibility + RNA per nucleus) reads exactly the minimal informative set for cell-type × locus-state inference.

## Single-cell methods, organized by which layers they read

See [[40-Topics/single-cell-multiomics]] for the full catalog. Quick map:

| Method | Layers read |
|---|---|
| scATAC, [[30-Concepts/daf-seq]], [[30-Concepts/got-cha]] | Accessibility (+ genotype for GoT-ChA, DAF-seq) |
| scBS-seq, [[30-Concepts/simple-seq]] | Methylation (5mC, + 5hmC for SIMPLE) |
| scCUT&Tag, [[30-Concepts/scchix-seq]] | Histone marks |
| scHi-C, [[30-Concepts/dip-c]], [[30-Concepts/igs]] | 3D genome |
| [[30-Concepts/scnmt-seq]] | Accessibility + methylation + RNA |
| [[30-Concepts/sctrio-seq]] | CNV + methylation + RNA |
| [[30-Concepts/splicool-seq]] | Methylation + accessibility |
| [[30-Concepts/scepi2-seq]] | Methylation + histone mark |
| [[30-Concepts/6-base-cut-and-tag]] | Methylation + 5hmC + histone mark (bulk fragment-level) |

No published single-cell method reads all four molecular layers simultaneously. The closest are triple-omics platforms (scNMT-seq, scTrio-seq).

## Open questions

- Is the fifth axis (structural/physical) really separable, or is it just the macroscopic phenotype of the four molecular layers acting together? See [[30-Concepts/chromatin-phase-separation]] for the case it *is* primary.
- For mosaicism: which layer is most informative when you can only measure one? Accessibility (current Duplex-Multiome answer) or methylation (stable memory of cell history)?
- 3D genome is conspicuously absent from the single-cell joint-with-genotype assay landscape. Why? Coverage requirements are higher; [[30-Concepts/dip-c]] and [[30-Concepts/igs]] don't yet pair with point-mutation calling.

## Related

- [[40-Topics/chromatin-architecture]] — gathers accessibility, 3D, structural pages
- [[40-Topics/dna-methylation]]
- [[40-Topics/histone-modifications]]
- [[40-Topics/3d-genome]]
- [[40-Topics/single-cell-multiomics]] — methods that read multiple layers
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — applies this framing to somatic mosaicism interpretation
- [[50-Notes/synthesis-targets]]
