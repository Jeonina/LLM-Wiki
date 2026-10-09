---
type: concept
title: Chromatin compartments
aliases: [A/B compartments]
tags: [3D-genome, Hi-C, chromatin]
created: 2026-05-12
updated: 2026-10-08
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


## Added 2026-10-07

Cell-type-specific compartments can be resolved from single-cell Hi-C in tissue. Droplet Hi-C found 895 cortex regions with variable compartment scores linked to chromatin state, and 1,782 switched compartments between MES-like and OPC-like glioblastoma states that associated with differential expression ([[10-Summaries/chang-2025-droplet-hi-c]]). With Paired Hi-C, erlotinib-treated GBM39 cells showed 1,066 A→B and 2,796 B→A switches, with expression moving in the matching direction ([[10-Summaries/chang-2025-droplet-hi-c]]).

scSPRITE detects A/B compartment segregation in ~95% of single mESCs across 224 compartment-switch regions. Per-region scores are more variable between cells than chromosome territories (mean 0.03 vs 0.08) ([[10-Summaries/arrastia-2022-scsprite]]). Cells carrying an alternative TAD at chr4 show compartment calls that differ from the ensemble ([[10-Summaries/arrastia-2022-scsprite]]).

Aggregated single-cell A/B values over marker-gene bodies were used to annotate scHi-C sub-clusters (e.g. interneuron sub-clusters as Vip vs Pvalb/Sst) in developing mouse brain ([[10-Summaries/zhang-2022-fast-higashi]]).

**Single-cell compartments without imputation.** scDIAGRAM calls A/B compartments per cell by Bayesian 2D change-point detection and normalized-cut partitioning, using CpG density only to orient labels ([[10-Summaries/peng-2026-scdiagram]]). Under heavy downsampling the CpG-guided scA/B score converges to CpG density, whereas scDIAGRAM stays closer to bulk PCA (pseudo-bulk intersection 0.94 vs 0.825) ([[10-Summaries/peng-2026-scdiagram]]). Compartment variance is higher in AML and embryo cells than in brain or GM12878, and variable loci are enriched for H3K27me3 ([[10-Summaries/peng-2026-scdiagram]]).

At 25 kb resolution, A/B compartments split into at least six subcompartments (A1, A2, B1–B4), defined by interchromosomal contact patterns alone ([[10-Summaries/rao-2014-in-situ-hic]]). Each has a distinct epigenomic profile: B1 tracks H3K27me3, B2 holds 62% of pericentromeric heterochromatin and is NAD-enriched, B3 is lamina-enriched but NAD-depleted, and B4 is a chr19 KRAB-ZNF cluster ([[10-Summaries/rao-2014-in-situ-hic]]).


## Added 2026-10-08 — sequence models & foundation models

- Orca, trained only on contact maps, learned to recognise active TSS sequences as compartment-A drivers and treats B as the default for extended AT-rich sequence, a hypothesis yet to be tested experimentally ([[10-Summaries/zhou-2022-orca]])

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
