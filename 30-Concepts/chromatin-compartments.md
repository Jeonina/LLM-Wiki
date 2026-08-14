---
type: concept
title: Chromatin compartments
aliases: [A/B compartments]
tags: [3D-genome, Hi-C, chromatin]
created: 2026-05-12
updated: 2026-08-10
---

# Chromatin compartments

> Large (~5–10 Mb) genomic blocks that preferentially associate with each other in 3D space. **A compartments** are gene-rich, transcriptionally active, early-replicating, and enriched for active histone marks. **B compartments** are gene-poor, repressed, late-replicating, and enriched for heterochromatin.

## Definition

Identified by principal-component analysis on Hi-C contact matrices. A and B compartments correspond to the two principal directions of the contact-matrix eigenvector. They can be further subdivided into A1, A2, B1–B4.

## Why it matters

- Compartment identity correlates with replication timing and chromatin state.
- Compartment switching marks cell-fate transitions.
- SnapATAC ([[10-Summaries/fang-2021-snapatac]]) shows that off-peak scATAC-seq reads correlate with A-compartment density — meaning compartment-level signal contributes to single-cell clustering even without explicit peak calls.

## Added 2026-08-10

[[10-Summaries/lieberman-aiden-2009-hic]] is the founding source: normalizing by distance-expected contact reveals a plaid pattern, correlating interaction profiles sharpens it, and PCA on the correlation matrix partitions each chromosome into two compartments with labels consistent genome-wide. Compartment A correlates with gene density (ρ = 0.431), expression (ρ = 0.476) and most strongly DNase I sensitivity (ρ = 0.651), and compartment identity switches between cell types in step with that cell type's own accessibility.

Compartments are now measurable per cell after imputation, with variability that correlates with transcriptional variability in 71% of 50 Mb windows ([[10-Summaries/zhang-2022-higashi]]); their presence or absence is also the discriminator between interphase and mitotic single cells ([[10-Summaries/ramani-2017-scihi-c]]).


## Related

- [[40-Topics/3d-genome]] · [[30-Concepts/topologically-associating-domain]] · [[30-Concepts/replication-timing]] · [[40-Topics/3d-genome]]

## Added 2026-08-13

Two independent lines of evidence converged in 2022–2024 that **binary A/B is too coarse**.

At bulk and pseudobulk scale, [[10-Summaries/chakraborty-2022-dchic|dcHiC]] found that **~26% of significant compartment changes involve no A↔B flip** — "strong A to weak A" transitions that show the same monotonic relationships with lamin B1, replication timing, and expression as flips do, and that flip-only methods miss by construction ([[10-Summaries/chakraborty-2022-dchic]]).

At single-cell scale, [[10-Summaries/xiong-2024-scghost|scGHOST]] found that single-cell subcompartment scores separate all five subcompartments, whereas bulk A2 and B1 are not distinguishable (mean P = 0.086) — the single-cell annotation is finer than the bulk one it was matched to ([[10-Summaries/xiong-2024-scghost]]).

**Variability is where the biology is.** Loci with variable subcompartment assignment show significantly higher H3K27me3 enrichment (P = 1.31 × 10⁻⁴) and host genes with more variable transcription (P = 2.60 × 10⁻²); subcompartment **boundaries** associate even more strongly with transcriptional variability (P = 3.79 × 10⁻⁹) ([[10-Summaries/xiong-2024-scghost]]).

**Operational limits from dcHiC** worth reusing: >80% recall of full-depth differential calls down to 40% downsampling at 100–25 kb; 10-kb differential analysis is false-positive-prone (median 751 spurious bins in replicate-vs-replicate, versus 2 at 100 kb); samples differing >2–3× in depth generate substantial false positives; chromosomes 4, 5, 14, 17 and X degrade first at low depth ([[10-Summaries/chakraborty-2022-dchic]]).

**Sub-compartment differencing does not replace a statistical test**: 60.5% of all bins show some sub-compartment transition, so specificity would be poor ([[10-Summaries/chakraborty-2022-dchic]]).

Unresolved: single-cell and bulk subcompartments disagree, and until that is explained "scB1" and bulk "B1" should not be treated as the same object ([[10-Summaries/xiong-2024-scghost]]). (synthesis)
