---
type: summary
title: "Zhang et al. 2022 — Characterizing cellular heterogeneity in chromatin state with scCUT&Tag-pro"
source: "[[00-Sources/papers/Characterizing cellular heterogeneity in chromatin state with scCUT&Tag-pro]]"
source_kind: paper
author: "Bingjie Zhang, Avi Srivastava, Eleni Mimitou, Tim Stuart, Ivan Raimondi, Yuhan Hao, Peter Smibert, Rahul Satija (corresponding)"
published: 2022-03-24
ingested: 2026-08-10
doi: "10.1038/s41587-022-01250-0"
journal: "Nature Biotechnology"
tags: [scCUT&Tag-pro, scChromHMM, multimodal, surface-protein, ADT, chromatin-state, regulatory-priming, WNN, reference-mapping]
entities: ["[[rahul-satija]]"]
concepts: ["[[cut-and-tag]]", "[[cite-seq]]", "[[multimodal-integration-methods]]", "[[joint-single-cell-multi-omics]]", "[[chromvar]]", "[[enhancer-states]]", "[[pseudo-bulk]]"]
topics: ["[[histone-modifications]]", "[[single-cell-multiomics]]"]
---

**Citation:** Zhang et al. (2022) — *Characterizing cellular heterogeneity in chromatin state with scCUT&Tag-pro* — *Nature Biotechnology* 40, 1220–1230. [DOI](https://doi.org/10.1038/s41587-022-01250-0)

# Zhang 2022 — scCUT&Tag-pro and scChromHMM

> Two problems, one solution. scCUT&Tag is sparse, and it measures **one mark per cell** while chromatin *state* is by definition combinatorial. Adding a 173-antibody surface-protein readout to each cell gives a dense, shared coordinate system; anchoring six separate single-mark experiments through that protein space yields interpolated per-cell profiles for all six marks, which a single-cell extension of ChromHMM then segments into states.

## Key claims

- **scCUT&Tag-pro**: CUT&Tag on whole cells (not nuclei) with simultaneous ADT capture. Cells stained with oligo-conjugated antibodies → monovalent Fab blocks pAG binding to them → light 0.1% formaldehyde fixation → isotonic lysis. **Removing digitonin from all buffers eliminated cell clumping** without hurting tagmentation. Compatible with the 10x scATAC kit and with cell hashing.
- 64,876 cells across six histone modifications (H3K4me1/2/3, H3K27ac, H3K27me3, H3K9me3) plus 173 TotalSeq-A antibodies.
- Sensitivity is comparable to nuclei-based scCUT&Tag: 501 mean unique fragments/cell for H3K27me3 vs 802 in [[wu-2021-sccut-tag|Wu et al.]] Pseudobulk **saturates between 500 and 1,000 cells**, and cell-type specificity survives downsampling to **300 cells per pseudobulk profile**.
- Chromatin-only clustering finds major immune lineages but "did not recapitulate the high-resolution identification of cell states as observed in scRNA-seq or CITE-seq." The protein modality adds CD4/CD8 exclusivity, CD14/CD16 monocyte split, MAIT cells. WNN clustering on both modalities is what recovers granular identity.
- Reference mapping to a 161,764-cell / 228-protein CITE-seq PBMC reference transfers annotations at three resolutions and harmonizes **nine modalities** (CITE-seq RNA + protein, ASAP-seq accessibility, six scCUT&Tag-pro marks) into one manifold with a shared pseudotime.
- **The bulk-tool failure that motivates scChromHMM**: ChromHMM's Baum–Welch step works fine on pseudobulk (12 interpretable states), but its final assignments are **granularity-dependent** — 16.4% of windows called enhancers in level-1 CD8 T cells are enhancers in *no* level-2 T cell subset. Conditioning on a fixed discrete label set is detrimental for continuous systems.
- **scChromHMM**: anchor-based interpolation produces 20,000 single-cell profiles each carrying all six marks plus accessibility, RNA and protein; the forward–backward algorithm is then run per cell with the pseudobulk-derived emission/transition probabilities, returning a posterior distribution over 12 states per 200 bp window per cell. Interpolation validates at R = 0.95 vs measured pseudobulk and R = 0.98 across independent runs. scChromHMM regions show **stronger** histone-mark and RNAPII enrichment than pseudobulk ChromHMM regions; heterochromatic calls overlap RepeatMasker elements 76.3%.
- CD8 T cell maturation remodels **14,585 windows** of repressive state, sharpest at the naive→memory transition. TBX21-motif windows gain active-state probability along the trajectory; LEF1-motif windows lose it.
- **The regulatory-priming result.** Cell identity is encoded in repressive-state probabilities at TSSs *even after removing the 3,000 most variable transcriptome genes*. Of 1,597 monocyte-specific repressive-state TSS shifts, only **257 (16.1%)** have a matching transcriptional shift; the other 1,340 genes are expressed at or near zero in all cell types (median <0.5 TPM). 81% of those show no differential expression in high-quality **bulk** total RNA-seq either, so it is not an scRNA-seq dropout artifact. Meta-analysis at those TSSs: H3K27me3 enriched, H3K4me3/me2 weakly enriched, H3K27ac absent — a poised signature.

## Methods / evidence

The interpolation step is the paper's load-bearing and most contestable move, and the authors bound it carefully: concordance with held-out measured profiles, reproducibility across independent interpolation runs, per-cell-type clustering of interpolated vs measured pseudobulk, and an explicit statement of what it cannot do — "interpolated modality predictions cannot capture stochastic technical or biological variation or be used to detect associations between multiple histone modifications within the same cell."

That caveat matters: scChromHMM's per-cell states are per-*cell-state* states rendered at single-cell resolution, not measurements of combinatorial marks in one nucleus.

## Surprising or load-bearing bits

- **Regulatory priming is the finding to carry.** Cell-type-specific repressive chromatin at genes that are silent everywhere means chromatin encodes *potential*, not just current output — a layer of identity invisible to any transcriptome method, bulk or single-cell. It is the strongest argument in this corpus for why epigenome measurement is not redundant with RNA.
- The granularity-dependence of ChromHMM generalizes: **any bulk tool applied to pseudobulk inherits the analyst's choice of cluster resolution as a hidden parameter.** Reported as a concrete 16.4% discordance.
- Protein as the integration currency is a deliberate alternative to RNA. Paired-Tag and CoTECH use transcriptome; this uses immunophenotype, which is denser per cell and better defined for immune systems — the authors say so explicitly. Both are "megaomic" strategies for the same gap.
- Whole cells rather than nuclei is what makes surface-protein capture possible — inherited from ASAP-seq's fixation/permeabilization optimizations.
- Six marks in one cell is stated as **not currently feasible experimentally**, especially for marks with overlapping localization. This paper is a computational workaround, and it says so.

## Entities mentioned

- [[rahul-satija]] — corresponding author; Seurat/WNN/Azimuth lineage.
- Peter Smibert, Eleni Mimitou — CITE-seq/ASAP-seq chemistry.

## Concepts touched

- [[cite-seq]] — the ADT strategy transplanted onto chromatin profiling.
- [[multimodal-integration-methods]] — anchor-based transfer used as *modality imputation*, not just batch correction.
- [[enhancer-states]] — 12 states recovered de novo from single-cell-derived pseudobulk.

## Connections to other sources

- Builds on [[kaya-okur-2019-cut-and-tag]] and re-analyzes [[wu-2021-sccut-tag]] as a query dataset, resolving its broad clusters into granular subsets (88% classified at level 1, 73% at level 2).
- WNN and anchor transfer come from [[hao-2024-seurat-v5]] / Seurat v4 lineage; [[stuart-2021-natmethods|Signac]] is the sibling tool.
- Fulfils the histone-modification gap named in [[zhu-2020-multimodal-power-of-many]].
- True simultaneous multi-mark measurement — what this paper simulates — is attempted by [[gopalan-2022-multi-cut-and-tag]] and [[yeung-2023-scchix-seq]].
- ChromHMM's bulk parent is [[roadmap-2015-111-epigenomes]].

## Open questions

- Because interpolation averages across cells in similar states, **genuine per-cell combinatorial mark co-occurrence remains unmeasured** — the bivalency question from [[bernstein-2006-bivalent-chromatin]] and [[rothbart-2014-histone-dna-language]] is untouched by this approach.
- Whether primed loci are actually induced later, or the signature is inert, is stated as a hypothesis; bone-marrow developmental profiling is proposed but not done.
- Method is immune-system-shaped: it needs a dense, well-annotated surface-protein reference. Transfer to tissues without one is unaddressed.

## Related

- [[wu-2021-sccut-tag]] · [[cite-seq]] · [[kaya-okur-2019-cut-and-tag]] · [[single-cell-multiomics]]
