---
type: concept
title: Chromatin compartments
aliases: [A/B compartments]
tags: [3D-genome, Hi-C, chromatin]
created: 2026-05-12
updated: 2026-10-12
---

# Chromatin compartments

> Large (~5–10 Mb) genomic blocks that preferentially associate with each other in 3D space: **A compartments** are gene-rich, transcriptionally active, early-replicating and enriched for active histone marks, while **B compartments** are gene-poor, repressed, late-replicating and enriched for heterochromatin ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]; [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

> [!abstract] 한눈에
> Chromatin compartment는 Hi-C contact matrix의 PCA로 정의되는 Mb 단위 영역으로, 활성 영역인 A와 억제 영역인 B가 3차원 공간에서 각자끼리 모인다 ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]). 이제는 단일 세포에서도 측정되며, A/B 이분법은 subcompartment와 같은 compartment 안의 변화를 담기에 너무 거칠다는 근거가 쌓이고 있다 ([[10-Summaries/chakraborty-2022-dchic|dcHiC]]; [[10-Summaries/xiong-2024-scghost|scGHOST]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [3D 유전체 교재](../60-Explainers/3d-genome.html)
<!-- /explainer-links -->

## Definition

Compartments are identified by principal-component analysis on Hi-C contact matrices: A and B correspond to the two directions of the leading contact-matrix eigenvector ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]). In the founding Hi-C paper, normalizing by distance-expected contact reveals a plaid pattern, correlating interaction profiles sharpens it, and PCA on the correlation matrix partitions each chromosome into two compartments with labels consistent genome-wide ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]). Compartments can be further subdivided into subcompartments A1, A2 and B1–B4 ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

## Why it matters

- Compartment A correlates with gene density (ρ = 0.431), expression (ρ = 0.476) and most strongly DNase I sensitivity (ρ = 0.651) ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]).
- Compartment identity correlates with replication timing and chromatin state ([[10-Summaries/chakraborty-2022-dchic|dcHiC]]).
- Compartment switching marks cell-fate transitions: identity switches between cell types in step with each cell type's own accessibility ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]).
- Compartment-level signal contributes to single-cell clustering even without explicit peak calls: off-peak scATAC-seq reads correlate with A-compartment density ([[10-Summaries/fang-2021-snapatac|SnapATAC]]).

## Subcompartments

At 25 kb resolution, A/B compartments split into at least six subcompartments (A1, A2, B1–B4), defined by interchromosomal contact patterns alone ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]). Each has a distinct epigenomic profile ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]):

| Subcompartment | Profile | Source |
|---|---|---|
| B1 | Tracks H3K27me3 | ([[10-Summaries/rao-2014-in-situ-hic\|Rao 2014]]) |
| B2 | Holds 62% of pericentromeric heterochromatin; NAD-enriched | ([[10-Summaries/rao-2014-in-situ-hic\|Rao 2014]]) |
| B3 | Lamina-enriched but NAD-depleted | ([[10-Summaries/rao-2014-in-situ-hic\|Rao 2014]]) |
| B4 | A chr19 KRAB-ZNF cluster | ([[10-Summaries/rao-2014-in-situ-hic\|Rao 2014]]) |

## Measuring compartments

### Bulk and differential calling

- **Differential compartments beyond flips.** dcHiC found that ~26% of significant compartment changes involve no A↔B flip: "strong A to weak A" transitions that show the same monotonic relationships with lamin B1, replication timing and expression as flips do, and that flip-only methods miss by construction ([[10-Summaries/chakraborty-2022-dchic|dcHiC]]).
- **Depth.** dcHiC keeps >80% recall of full-depth differential calls down to 40% downsampling at 100–25 kb; samples differing >2–3× in depth generate substantial false positives; chromosomes 4, 5, 14, 17 and X degrade first at low depth ([[10-Summaries/chakraborty-2022-dchic|dcHiC]]).
- **Resolution.** 10-kb differential analysis is false-positive-prone: median 751 spurious bins in replicate-vs-replicate, versus 2 at 100 kb ([[10-Summaries/chakraborty-2022-dchic|dcHiC]]).
- **Sub-compartment differencing does not replace a statistical test**: 60.5% of all bins show some sub-compartment transition, so specificity would be poor ([[10-Summaries/chakraborty-2022-dchic|dcHiC]]).

### Single-cell methods

| Method | Approach | Key result | Source |
|---|---|---|---|
| Higashi | Per-cell compartments after imputation | Compartment variability correlates with transcriptional variability in 71% of 50 Mb windows | ([[10-Summaries/zhang-2022-higashi\|Higashi]]) |
| Fast-Higashi | Aggregated single-cell A/B values over marker-gene bodies | Annotated scHi-C sub-clusters in developing mouse brain (e.g. interneuron sub-clusters as Vip vs Pvalb/Sst) | ([[10-Summaries/zhang-2022-fast-higashi\|Fast-Higashi]]) |
| scDIAGRAM | Per-cell A/B calls without imputation, by Bayesian 2D change-point detection and normalized-cut partitioning; CpG density used only to orient labels | Under heavy downsampling stays closer to bulk PCA than the CpG-guided scA/B score, which converges to CpG density (pseudo-bulk intersection 0.94 vs 0.825) | ([[10-Summaries/peng-2026-scdiagram\|scDIAGRAM]]) |
| scGHOST | Single-cell subcompartment scores | Separates all five subcompartments, whereas bulk A2 and B1 are not distinguishable (mean P = 0.086) | ([[10-Summaries/xiong-2024-scghost\|scGHOST]]) |
| scSPRITE | Single-cell SPRITE contacts | Detects A/B segregation in ~95% of single mESCs across 224 compartment-switch regions | ([[10-Summaries/arrastia-2022-scsprite\|scSPRITE]]) |
| Droplet Hi-C / Paired Hi-C | Droplet single-cell Hi-C in tissue | Resolves cell-type-specific compartments in cortex and glioblastoma | ([[10-Summaries/chang-2025-droplet-hi-c\|Chang 2025]]) |

### Sequence models

- Orca, trained only on contact maps, learned to recognise active TSS sequences as compartment-A drivers and treats B as the default for extended AT-rich sequence, a hypothesis yet to be tested experimentally ([[10-Summaries/zhou-2022-orca|Orca]]).

## Evidence and examples

- Compartment presence or absence is the discriminator between interphase and mitotic single cells ([[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]).
- Droplet Hi-C found 895 cortex regions with variable compartment scores linked to chromatin state ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).
- Droplet Hi-C found 1,782 switched compartments between MES-like and OPC-like glioblastoma states that associated with differential expression ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).
- With Paired Hi-C, erlotinib-treated GBM39 cells showed 1,066 A→B and 2,796 B→A switches, with expression moving in the matching direction ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).
- In scSPRITE, per-region compartment scores are more variable between cells than chromosome territories (mean 0.03 vs 0.08) ([[10-Summaries/arrastia-2022-scsprite|scSPRITE]]).
- Cells carrying an alternative TAD at chr4 show compartment calls that differ from the ensemble ([[10-Summaries/arrastia-2022-scsprite|scSPRITE]]).
- Compartment variance is higher in AML and embryo cells than in brain or GM12878, and variable loci are enriched for H3K27me3 ([[10-Summaries/peng-2026-scdiagram|scDIAGRAM]]).
- **Variability is where the biology is.** Loci with variable subcompartment assignment show significantly higher H3K27me3 enrichment (P = 1.31 × 10⁻⁴) and host genes with more variable transcription (P = 2.60 × 10⁻²); subcompartment **boundaries** associate even more strongly with transcriptional variability (P = 3.79 × 10⁻⁹) ([[10-Summaries/xiong-2024-scghost|scGHOST]]).

## Contested points

- **Binary A/B is too coarse.** Two independent lines of evidence converged in 2022–2024: within-compartment changes are about a quarter of significant compartment changes at bulk and pseudobulk scale ([[10-Summaries/chakraborty-2022-dchic|dcHiC]]), and single-cell subcompartment scores separate classes that bulk annotation cannot ([[10-Summaries/xiong-2024-scghost|scGHOST]]).
- **Single-cell and bulk subcompartments disagree.** Until that is explained, "scB1" and bulk "B1" should not be treated as the same object ([[10-Summaries/xiong-2024-scghost|scGHOST]]) (synthesis).
- **The direction of the scSPRITE variability score is unclear.** Compartment regions are reported as more variable between cells than chromosome territories, with mean scores of 0.03 vs 0.08 ([[10-Summaries/arrastia-2022-scsprite|scSPRITE]]); the summary does not define the score, so which value means "more variable" should be checked against the paper (synthesis).
- **Orca's compartment-driver hypothesis is untested** experimentally ([[10-Summaries/zhou-2022-orca|Orca]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/topologically-associating-domain|Topologically associating domain]] — Sub-Mb self-interacting domains nested below compartments.
> - `concept` [[30-Concepts/replication-timing|Replication timing]] — Early vs late replication, which tracks A vs B identity.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromatin folding from compartments to loops, in bulk and single cells.

## All sources on this page

> [!info]- 12 summaries cited here
> - [[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]
> - [[10-Summaries/chakraborty-2022-dchic|Chakraborty 2022]]
> - [[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]
> - [[10-Summaries/fang-2021-snapatac|Fang 2021]]
> - [[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]
> - [[10-Summaries/peng-2026-scdiagram|Peng 2026]]
> - [[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]
> - [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]
> - [[10-Summaries/xiong-2024-scghost|Xiong 2024]]
> - [[10-Summaries/zhang-2022-fast-higashi|Zhang 2022]]
> - [[10-Summaries/zhang-2022-higashi|Zhang 2022]]
> - [[10-Summaries/zhou-2022-orca|Orca 2022]]
