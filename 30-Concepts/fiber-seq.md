---
type: concept
title: Fiber-seq
aliases: [fiber-seq]
tags: [single-molecule, chromatin, methyltransferase, footprinting, method]
created: 2026-05-07
updated: 2026-10-12
paper_section: ["3.2.1"]
---

# Fiber-seq

> Single-molecule chromatin footprinting method developed in the [[20-Entities/andrew-b-stergachis|Stergachis lab]] that uses an N6-adenine methyltransferase (m6A) to stencil protein occupancy onto chromatin fibers, then reads the methyl marks with long-read sequencing — predecessor of [[daf-seq]] ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).

> [!abstract] 한눈에
> Fiber-seq는 핵 안에서 m6A methyltransferase로 열린 DNA에 표지를 남기고 long-read sequencing으로 읽어, 수 kb 길이의 한 fiber 위에서 nucleosome과 TF 점유를 동시에 보여 주는 방법이다 ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]). m6A 표지는 증폭 과정에서 지워지기 때문에 bulk에서만 쓸 수 있고, 이 한계를 deamination 기반의 DAF-seq가 풀었다 ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [염색질 구조 교재](../60-Explainers/chromatin-architecture.html)
>
> [Long-read 시퀀싱 교재](../60-Explainers/long-read-sequencing.html)
<!-- /explainer-links -->

## Definition

In nuclei, a non-specific m6A methyltransferase modifies adenines in accessible (TF/nucleosome-free) DNA ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]). Long-read PacBio CCS sequencing reads m6A directly via DNA-polymerase kinetics, so the m6A pattern along an individual fiber is a chromatin footprint at near-nucleotide resolution along multikilobase fragments ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]). Foundational paper: Stergachis et al., *Science* 368, 1449, 2020 ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).

## Why it matters

Stergachis 2020 established four single-molecule chromatin principles that are unobservable in bulk ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]):

1. **All-or-none actuation.** At any DHS, ~81% of overlapping fibers carry the open MAD; the rest are closed. Bulk accessibility is therefore a *frequency of actuation*, not a graded analog signal. TSS-distal DHSs are preferentially closed; promoter DHSs preferentially open ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).
2. **Co-actuation in cis.** Neighbouring DHSs are more likely to be actuated on the *same* fiber than chance, in a distance-dependent way and independently of shared TFs — a physicochemical basis for distal-regulatory-element clustering ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).
3. **Boundary nucleosome positioning.** Well-positioned nucleosome arrays around DHSs exist *only* on actuated fibers; sequence does not encode the position, regulatory actuation imposes it ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).
4. **Single-molecule TF footprinting.** Within actuated MADs, m6A is punctuated by short TF-footprint gaps ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).

## Operating point (Stergachis 2020)

- **Enzymes screened:** five nonspecific m6A-MTases, including Hia5, EcoGII and Hin1523; all marked accessible DNA quantitatively ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).
- **AdMTase-seq** (short-read m6A-IP) confirms quantitative tracking of DNase-seq accessibility ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).
- **Fiber-seq output:** average fiber length 10.9 kb, max ~30 kb; ~43× coverage per DHS; nearly all fibers carry m6A. Two MAD classes — ~272 bp (DHS-coincident) and ~67 bp (linker regions) ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).
- Validated on both *Drosophila* S2 cells and human K562 cells ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).

## Variants and refinements

| Variant | Chemistry / readout | What it adds | Source |
|---|---|---|---|
| AdMTase-seq | Short-read m6A-IP | Bulk-only short-read version | ([[10-Summaries/andrewb-2020-science\|Stergachis 2020]]) |
| Fiber-seq | m6A, long-read PacBio CCS | Multikilobase per-fiber resolution | ([[10-Summaries/andrewb-2020-science\|Stergachis 2020]]) |
| Targeted Fiber-seq | Fiber-seq plus in-gel CRISPR–Cas9 excision of 100–250 kb loci | Median 10-fold enrichment; at least 5 samples multiplexed per SMRT cell | ([[10-Summaries/bohaczuk-2024-targeted-fiberseq\|Bohaczuk 2024]]) |
| [[stam-seq\|STAM-seq]] | Fiber-seq-style m6A stenciling | Adapted to *Arabidopsis* centromeres / telomeres / rDNA | ([[10-Summaries/mo-2023-stam-seq\|Mo 2023]]) |
| [[samosa\|SAMOSA]], [[samosa-tag\|SAMOSA-Tag]], [[smrt-tag\|SMRT-Tag]] | Methylation-based footprinting | Adjacent applications (targeted, repeat-mapping, multimodal) | — |
| [[daf-seq\|DAF-seq]] | Cytidine deamination | Direct successor; single-cell-compatible | ([[10-Summaries/swanson-2025-daf-seq\|DAF-seq]]) |

**Structural ceiling — why Fiber-seq is bulk-only.** Methylation marks are erased during DNA amplification, which keeps methyltransferase footprinting a bulk assay ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]); this holds for any amplification (PCR, MDA, PTA, LIANTI), and a single cell yields ≤1–2 fibers per locus with no way to amplify up to sequencing depth (synthesis). [[daf-seq]] solves this five years later by replacing methylation with cytidine deamination — sequence changes that *do* survive amplification ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

## Evidence and examples

- All-or-none actuation rates at TSS-distal DHSs in *Drosophila* S2 cells track DNase-seq cleavage density tightly (Fig. 3) ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).
- For CTCF in K562, **most actuated fibers overlapping CTCF-bound elements lack a CTCF footprint** (accessible but TF-vacant); elements with a higher fraction of CTCF-footprinted fibers participate in significantly more RAD21 ChIA-PET long-range interactions (Fig. 5) ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).
- The chr17:19447245–19447246 CC>TT somatic CTCF-ablating variant in COLO829T melanoma was originally analysed via Fiber-seq before DAF-seq took over for the BL/T mixture ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

## Contested points

- The bulk-only nature follows from amplification erasing m6A marks; it is a structural limit rather than a contested point (synthesis).
- m6A base-calling accuracy depends on long-read base-caller models; Stergachis 2020 used PacBio CCS resequencing ≥10× per fiber to mitigate this ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).
- Internal nucleosome-bound regions are inferred from m6A *absence* — a non-trivial assumption that base-flipping is uniformly inhibited by nucleosomes; the paper validates this against deproteinized DNA controls ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/daf-seq|DAF-seq]] — Direct successor; deaminase marks that survive amplification and allow single-cell fibers.
> - `concept` [[30-Concepts/single-molecule-footprinting|Single-molecule footprinting]] — Assays that mark accessible DNA on individual fibers and read the marks with long reads.
> - `concept` [[30-Concepts/chromatin-actuation|Chromatin actuation]] — A regulatory element being simultaneously open and bound on one fiber.
> - `concept` [[30-Concepts/stam-seq|STAM-seq]] — Long-read accessibility and methylation in plants using 6mA labelling.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA packaging varies across fibers, haplotypes and cells.

## All sources on this page

> [!info]- 4 summaries cited here
> - [[10-Summaries/andrewb-2020-science|Stergachis 2020]]
> - [[10-Summaries/bohaczuk-2024-targeted-fiberseq|Bohaczuk 2024]]
> - [[10-Summaries/mo-2023-stam-seq|Mo 2023]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
