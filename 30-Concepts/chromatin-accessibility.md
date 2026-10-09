---
type: concept
title: Chromatin accessibility
aliases: [open chromatin, chromatin openness, accessibility]
tags: [chromatin, regulation]
created: 2026-05-07
updated: 2026-10-08
---

# Chromatin accessibility

> Whether a region of DNA is "open" (free of nucleosomes, available for TF binding and transcription machinery) or "closed" (wrapped in nucleosomes / heterochromatin) — a regulatory readout that varies by cell type ([[10-Summaries/buenrostro-2015-nature]]), cell state, and (per [[10-Summaries/swanson-2025-daf-seq|DAF-seq]]) per fiber within a cell.

## Definition

The operational definition depends on the assay. ATAC-seq / DNase-seq measure accessibility as susceptibility to Tn5 transposase or DNase I cleavage in *bulk*, producing peaks where many cells have open chromatin at that locus ([[10-Summaries/buenrostro-2015-nature]]). Single-cell ATAC-seq (scATAC-seq) generalizes to a per-cell binary or count matrix per peak ([[10-Summaries/buenrostro-2015-nature]]; [[10-Summaries/cusanovich-2015-sciatac]]). Single-molecule footprinting ([[10-Summaries/andrewb-2020-science|Fiber-seq]]; [[10-Summaries/swanson-2025-daf-seq|DAF-seq]]) refines further to a per-fiber occupancy pattern, distinguishing nucleosome-protected from TF-protected from fully-accessible bases.

## Why it matters

Accessibility is the most upstream measurable consequence of regulatory state. Mutations that do not change DNA sequence in coding regions can still drive disease by altering accessibility — see the [[jak2-v617f]] cell-intrinsic chromatin priming finding in [[10-Summaries/izzo-2024-got-cha]] and the rs2280838 SLC39A4 nucleosome-positioning eQTL in [[10-Summaries/swanson-2025-daf-seq]].

In single-cell genomics, accessibility complements RNA: it captures regulatory potential before transcription, and it captures it for non-coding regions that scRNA-seq does not see ([[10-Summaries/cao-2018-sci-car]]; [[10-Summaries/ma-2020-share-seq]]).

## Variants and refinements

- **Bulk ATAC-seq / DNase-seq** — population-averaged accessibility peaks ([[10-Summaries/buenrostro-2015-nature]]).
- **Single-cell ATAC-seq** — per-cell peak occupancy; powers cell-type identification and differential accessibility analysis ([[10-Summaries/buenrostro-2015-nature]]; [[10-Summaries/cusanovich-2015-sciatac]]). The base layer of [[got-cha]] ([[10-Summaries/izzo-2024-got-cha]]).
- **Single-molecule footprinting** ([[daf-seq]], [[fiber-seq]]) — per-fiber, per-base accessibility plus protein occupancy patterns; resolves what bulk and single-cell assays smear together ([[10-Summaries/andrewb-2020-science]]; [[10-Summaries/swanson-2025-daf-seq]]).
- **[[chromatin-actuation]]** — DAF-seq's term for an element being in the "open + bound" state on a specific fiber; a per-fiber refinement of accessibility ([[10-Summaries/swanson-2025-daf-seq]]).
- **TF-associated accessibility deviation** — chromVAR aggregates scATAC peaks by TF motif to extract motif-level accessibility signal from sparse single-cell data ([[10-Summaries/schep-2017-chromvar]]).

## Contested points

- Tn5-based assays under-call accessibility at GC-rich regions and have well-known tagmentation biases (synthesis — Tn5 sequence preference is broadly acknowledged in scATAC tooling, e.g. [[10-Summaries/schep-2017-chromvar]]); long-read footprinting methods do not share these biases but have their own — m6A methyltransferase sequence preference for Fiber-seq ([[10-Summaries/andrewb-2020-science]]), whereas DAF-seq's SsDddA deaminase is reported to have minimal sequence bias ([[10-Summaries/swanson-2025-daf-seq]]).
- "Accessible peak" calls in scATAC-seq are often binarized at thresholds that hide quantitative differences observed in single-molecule data ([[10-Summaries/swanson-2025-daf-seq]] vs [[10-Summaries/buenrostro-2015-nature]]).
- ~61% intra-cell haplotype divergence in actuation state ≈ ~63% inter-cell divergence ([[10-Summaries/swanson-2025-daf-seq]]) — suggests per-fiber stochasticity rather than per-cell programs.

## Examples

- JAK2V617F-mutant HSCs show increased accessibility at NF-κB target genes (TRAPPC9), TGF-β receptor BMPR1B, and matrix-remodeling MMP15 ([[10-Summaries/izzo-2024-got-cha]]).
- The SLC39A4 eQTL locus is resolved per haplotype by same-molecule genotype + chromatin readout ([[10-Summaries/swanson-2025-daf-seq]]).
- Chromatin potential — accessibility precedes transcription during differentiation, predicting cell-fate decisions in keratinocytes ([[10-Summaries/ma-2020-share-seq]]).

## Added 2026-10-07

Differential accessibility in scATAC-seq is statistically fragile: in a replicate-vs-replicate null, a Wilcoxon test called 6,761 regions and a Signac-style GLM 910, whereas PeakVI's posterior-sampling test called none ([[10-Summaries/ashuach-2022-peakvi]]). scaDA instead models peaks as zero-inflated negative binomial and tests mean, prevalence and dispersion jointly, arguing cell types differ in accessibility distributions, not only means ([[10-Summaries/zhao-2024-scada]]). BROCKMAN found reads outside called peaks grouped K562 samples better than reads inside peaks ([[10-Summaries/de-boer-2018-brockman]]).


Before interferon stimulation, ISREs are accessible and carry narrow IRF9 footprints with no expression, so accessibility can be decoupled from transcriptional activity ([[10-Summaries/doughty-2024-smf-tf]]). At the DM1 SIX5 promoter, accessibility falls on expanded haplotypes while CpG methylation does not change ([[10-Summaries/bohaczuk-2024-targeted-fiberseq]]).

## Added 2026-10-08 — sequence models & foundation models

- Basset showed that DNA sequence alone predicts cell-type DHS status across 164 ENCODE/Roadmap cell types (mean AUC 0.895), although cell-specific sites are harder (AUC 0.858) ([[10-Summaries/kelley-2016-basset]])
- NTv3 reaches Pearson r 0.753 (HepG2) and 0.755 (IMR-90) on shared DNase experiments against 0.704 and 0.717 for ChromBPNet, predicting accessibility at base resolution from up to 1 Mb of context ([[10-Summaries/boshar-2025-ntv3]]).
- On the BEND benchmark with frozen embeddings, a 7B Transformer–Mamba2 hybrid reached AUROC 0.84 for chromatin accessibility, 0.79 for histone modification and 0.93 for CpG methylation ([[10-Summaries/ma-2025-hybridna]]).
- On DeepSEA, a 192-kb-context dense-attention DNA language model matched or slightly beat earlier models on DNase-hypersensitivity prediction (median AUC 0.934) but fell behind on histone marks (0.839 vs 0.863 for HyenaDNA) ([[10-Summaries/vishniakov-2025-gene42]]).
- On ChromBPNet's caQTL, dsQTL and SPI1 bQTL benchmarks across ancestries, the multimodal AlphaGenome beat the accessibility-specialist ChromBPNet (e.g. Pearson r = 0.74 with African-ancestry caQTL effect sizes) ([[10-Summaries/avsec-2026-alphagenome]])

## Related

- [[chromatin-actuation]]
- [[fiber-seq]]
- [[daf-seq]]
- [[got-cha]]
- [[single-molecule-footprinting]]
- [[40-Topics/chromatin-architecture]]
- [[50-Notes/regulatory-layers-overview]] — accessibility as one of the four molecular regulatory layers
