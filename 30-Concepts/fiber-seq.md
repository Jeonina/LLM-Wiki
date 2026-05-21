---
type: concept
title: Fiber-seq
aliases: [fiber-seq]
tags: [single-molecule, chromatin, methyltransferase, footprinting, method]
created: 2026-05-07
updated: 2026-05-07
---

# Fiber-seq

> Single-molecule chromatin footprinting method developed in the [[20-Entities/andrew-b-stergachis|Stergachis lab]] that uses an N6-adenine methyltransferase (m6A) to stencil protein occupancy onto chromatin fibers, then reads the methyl marks with long-read sequencing — predecessor of [[daf-seq]].

## Definition

In nuclei, a non-specific m6A methyltransferase modifies adenines in accessible (TF/nucleosome-free) DNA. Long-read PacBio CCS sequencing reads m6A directly via DNA-polymerase kinetics, so the m6A pattern along an individual fiber is a chromatin footprint at near-nucleotide resolution along multikilobase fragments. Foundational paper: [[10-Summaries/andrewb-2020-science]] (Stergachis et al., *Science* 368, 1449, 2020).

## Operating point (Stergachis 2020)

- **Enzymes screened**: five nonspecific m6A-MTases — Hia5, EcoGII, Btr192IV, EcoGI, Hin1523. Hia5 is the most efficient and is the default.
- **AdMTase-seq** (short-read m6A-IP) confirms quantitative tracking of DNase-seq accessibility (Hia5 vs DNase-seq R² = 0.84).
- **Fiber-seq output**: average fiber length 10.9 kb, max ~30 kb; ~43× coverage per DHS; 99.7% of fibers carry m6A. Two MAD classes — ~272 bp (DHS-coincident) and ~67 bp (linker regions).
- Validated on both *Drosophila* S2 cells and human K562 cells.

## Why it matters (primary findings)

The Stergachis 2020 paper established four single-molecule chromatin principles unobservable in bulk:

1. **All-or-none actuation**: at any DHS, ~81% of overlapping fibers carry the open MAD; the rest are closed. Bulk accessibility is therefore a *frequency of actuation*, not a graded analog signal. TSS-distal DHSs are preferentially closed; promoter DHSs preferentially open.
2. **Co-actuation in cis**: neighboring DHSs are more likely to be actuated on the *same* fiber than chance, in a distance-dependent way and independently of shared TFs. A physicochemical basis for distal-regulatory-element clustering.
3. **Boundary nucleosome positioning**: well-positioned nucleosome arrays around DHSs exist *only* on actuated fibers. Sequence does not encode the position; regulatory actuation imposes it.
4. **Single-molecule TF footprinting**: within actuated MADs, m6A is punctuated by short TF-footprint gaps. For CTCF in K562, only **30%** of accessible CTCF-bound elements (per bulk ChIP) actually carry a CTCF footprint on any given fiber; bound elements participate in significantly more RAD21 ChIA-PET long-range interactions.

## Structural ceiling — why Fiber-seq is bulk-only

m6A marks are erased during any DNA amplification (PCR, MDA, PTA, LIANTI). A single cell yields ≤1–2 fibers per locus, with no way to amplify up to sequencing depth. This is the limitation that [[daf-seq]] solves five years later by replacing methylation with cytidine deamination — sequence changes that *do* survive amplification.

## Variants and refinements

- **AdMTase-seq** ([[10-Summaries/andrewb-2020-science]]) — short-read m6A-IP version, bulk only.
- **Fiber-seq** ([[10-Summaries/andrewb-2020-science]]) — long-read PacBio CCS version giving multikilobase per-fiber resolution.
- **[[stam-seq]]** ([[10-Summaries/mo-2023-stam-seq]]) — Fiber-seq-style m6A stenciling adapted to *Arabidopsis* centromeres / telomeres / rDNA.
- **[[samosa]]**, **[[samosa-tag]]**, **[[smrt-tag]]** — methylation-based footprinting variants for adjacent applications (targeted, repeat-mapping, multimodal).
- **[[daf-seq]]** ([[10-Summaries/swanson-2025-daf-seq]]) — direct successor; deamination-based, single-cell-compatible.

## Contested points

- Bulk-only nature is acknowledged in the original paper, not contested.
- m6A base-calling accuracy depends on long-read base-caller models; Stergachis 2020 used PacBio CCS resequencing ≥10× per fiber to mitigate.
- Internal nucleosome-bound regions are inferred from m6A *absence* — a non-trivial assumption that base-flipping is uniformly inhibited by nucleosomes (the paper validates this against deproteinized DNA controls).

## Examples

- All-or-none actuation rates at TSS-distal DHSs in *Drosophila* S2 cells track DNase-seq cleavage density tightly ([[10-Summaries/andrewb-2020-science]] Fig. 3).
- 30% / 70% bound / accessible-unbound CTCF site partitioning in K562 cells, with bound-fraction predicting long-range loop participation ([[10-Summaries/andrewb-2020-science]] Fig. 5).
- The chr.17:19447245–19447246 CC>TT somatic CTCF-ablating variant in COLO829T melanoma was originally analyzed via Fiber-seq before DAF-seq took over for the BL/T mixture ([[10-Summaries/swanson-2025-daf-seq]]).

## Related

- [[daf-seq]] — direct successor; replaces methylation marks with deaminations.
- [[single-molecule-footprinting]]
- [[chromatin-actuation]]
- [[20-Entities/andrew-b-stergachis]]
- [[40-Topics/chromatin-architecture]]
