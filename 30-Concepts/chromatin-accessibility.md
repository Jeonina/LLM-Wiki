---
type: concept
title: Chromatin accessibility
aliases: [open chromatin, chromatin openness, accessibility]
tags: [chromatin, regulation]
created: 2026-05-07
updated: 2026-10-12
---

# Chromatin accessibility

> Whether a region of DNA is "open" (free of nucleosomes, available for TF binding and transcription machinery) or "closed" (wrapped in nucleosomes or heterochromatin) — a regulatory readout that varies by cell type ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]), cell state, and per fiber within a cell ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

> [!abstract] 한눈에
> Chromatin accessibility는 DNA 구간이 nucleosome에서 벗어나 TF와 전사 기구가 닿을 수 있는 상태인지를 나타내며, 세포 유형과 상태에 따라 달라지고 같은 세포 안에서도 fiber마다 다르다 ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]; [[10-Summaries/swanson-2025-daf-seq|DAF-seq]]). 측정 방법이 bulk peak에서 단일 세포, 단일 분자 footprint로 내려갈수록 정의도 세밀해지지만, scATAC-seq의 differential accessibility 검정은 통계적으로 취약하다 ([[10-Summaries/ashuach-2022-peakvi|PeakVI]]).

## Definition

The operational definition depends on the assay. ATAC-seq and DNase-seq measure accessibility as susceptibility to Tn5 transposase or DNase I cleavage in *bulk*, producing peaks where many cells have open chromatin at that locus ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]). Single-cell ATAC-seq (scATAC-seq) generalizes this to a per-cell binary or count matrix per peak ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]; [[10-Summaries/cusanovich-2015-sciatac|Cusanovich 2015]]). Single-molecule footprinting refines it further to a per-fiber occupancy pattern, distinguishing nucleosome-protected from TF-protected from fully accessible bases ([[10-Summaries/andrewb-2020-science|Fiber-seq]]; [[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

## Why it matters

- Accessibility is the most upstream measurable consequence of regulatory state (synthesis).
- Mutations that do not change coding sequence can still drive disease by altering accessibility: see the [[jak2-v617f]] cell-intrinsic chromatin priming finding ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]) and the rs2280838 SLC39A4 nucleosome-positioning eQTL ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).
- In single-cell genomics, accessibility complements RNA: it captures regulatory potential before transcription, and it captures it for non-coding regions that scRNA-seq does not see ([[10-Summaries/cao-2018-sci-car|sci-CAR]]; [[10-Summaries/ma-2020-share-seq|SHARE-seq]]).

## Assays and readouts

| Readout | Examples | What it resolves | Source |
|---|---|---|---|
| Bulk ATAC-seq / DNase-seq | — | Population-averaged accessibility peaks | ([[10-Summaries/buenrostro-2015-nature\|Buenrostro 2015]]) |
| Single-cell ATAC-seq | scATAC-seq, sci-ATAC-seq; the base layer of [[got-cha]] | Per-cell peak occupancy; powers cell-type identification and differential accessibility analysis | ([[10-Summaries/buenrostro-2015-nature\|Buenrostro 2015]]; [[10-Summaries/cusanovich-2015-sciatac\|Cusanovich 2015]]; [[10-Summaries/izzo-2024-got-cha\|Izzo 2024]]) |
| Single-molecule footprinting ([[single-molecule-footprinting]]) | [[fiber-seq]], [[daf-seq]] | Per-fiber, per-base accessibility plus protein-occupancy patterns; resolves what bulk and single-cell assays smear together | ([[10-Summaries/andrewb-2020-science\|Fiber-seq]]; [[10-Summaries/swanson-2025-daf-seq\|DAF-seq]]) |
| [[chromatin-actuation]] | DAF-seq | DAF-seq's term for an element in the "open + bound" state on a specific fiber; a per-fiber refinement of accessibility | ([[10-Summaries/swanson-2025-daf-seq\|DAF-seq]]) |

## Analysis approaches

### Single-cell accessibility statistics

- **TF-associated accessibility deviation.** chromVAR aggregates scATAC peaks by TF motif to extract motif-level accessibility signal from sparse single-cell data ([[10-Summaries/schep-2017-chromvar|chromVAR]]).
- **Differential accessibility is statistically fragile.** In a replicate-vs-replicate null, a Wilcoxon test called 6,761 regions and a Signac-style GLM 910, whereas PeakVI's posterior-sampling test called none ([[10-Summaries/ashuach-2022-peakvi|PeakVI]]).
- **Distributional testing.** scaDA models peaks as zero-inflated negative binomial and tests mean, prevalence and dispersion jointly, arguing that cell types differ in accessibility distributions, not only in means ([[10-Summaries/zhao-2024-scada|scaDA]]).
- **Reads outside peaks carry signal.** BROCKMAN found that reads outside called peaks grouped K562 samples better than reads inside peaks ([[10-Summaries/de-boer-2018-brockman|BROCKMAN]]).

### Sequence models that predict accessibility

| Model | Setting | Result | Source |
|---|---|---|---|
| Basset | DNA sequence alone, 164 ENCODE/Roadmap cell types, cell-type DHS status | Mean AUC 0.895; cell-specific sites harder (AUC 0.858) | ([[10-Summaries/kelley-2016-basset\|Basset]]) |
| NTv3 | Base-resolution accessibility from up to 1 Mb of context, shared DNase experiments | Pearson r 0.753 (HepG2) and 0.755 (IMR-90), against 0.704 and 0.717 for ChromBPNet | ([[10-Summaries/boshar-2025-ntv3\|NTv3]]) |
| HybriDNA (7B Transformer–Mamba2 hybrid) | BEND benchmark, frozen embeddings | AUROC 0.84 for chromatin accessibility, 0.79 for histone modification, 0.93 for CpG methylation | ([[10-Summaries/ma-2025-hybridna\|HybriDNA]]) |
| Gene42 (192-kb-context dense-attention DNA language model) | DeepSEA | Matched or slightly beat earlier models on DNase-hypersensitivity prediction (median AUC 0.934) but fell behind on histone marks (0.839 vs 0.863 for HyenaDNA) | ([[10-Summaries/vishniakov-2025-gene42\|Gene42]]) |
| AlphaGenome (multimodal) | ChromBPNet's caQTL, dsQTL and SPI1 bQTL benchmarks across ancestries | Beat the accessibility-specialist ChromBPNet (e.g. Pearson r = 0.74 with African-ancestry caQTL effect sizes) | ([[10-Summaries/avsec-2026-alphagenome\|AlphaGenome]]) |

## Evidence and examples

- JAK2V617F-mutant HSCs show increased accessibility at NF-κB target genes (TRAPPC9), the TGF-β receptor BMPR1B, and matrix-remodelling MMP15 ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- The SLC39A4 eQTL locus is resolved per haplotype by a same-molecule genotype and chromatin readout ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).
- Chromatin potential: accessibility precedes transcription during differentiation and predicts cell-fate decisions in keratinocytes ([[10-Summaries/ma-2020-share-seq|SHARE-seq]]).
- Before interferon stimulation, ISREs are accessible and carry narrow IRF9 footprints with no expression, so accessibility can be decoupled from transcriptional activity ([[10-Summaries/doughty-2024-smf-tf|Doughty 2024]]).
- At the DM1 SIX5 promoter, accessibility falls on expanded haplotypes while CpG methylation does not change ([[10-Summaries/bohaczuk-2024-targeted-fiberseq|Bohaczuk 2024]]).

## Contested points

- **Assay biases.** Tn5-based assays under-call accessibility at GC-rich regions and have well-known tagmentation biases (synthesis — Tn5 sequence preference is broadly acknowledged in scATAC tooling, e.g. [[10-Summaries/schep-2017-chromvar|chromVAR]]). Long-read footprinting methods do not share these biases but have their own: m6A methyltransferase sequence preference for Fiber-seq ([[10-Summaries/andrewb-2020-science|Fiber-seq]]), whereas DAF-seq's SsDddA deaminase is reported to have minimal sequence bias ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).
- **Binarized peaks hide quantitative differences.** "Accessible peak" calls in scATAC-seq are often binarized at thresholds that hide quantitative differences observed in single-molecule data ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]] vs [[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]).
- **Per-fiber stochasticity vs per-cell programs.** About 61% intra-cell haplotype divergence in actuation state is close to the ~63% inter-cell divergence ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]), which suggests per-fiber stochasticity rather than per-cell programs.
- **Accessibility is not activity.** Accessible, footprinted ISREs without expression ([[10-Summaries/doughty-2024-smf-tf|Doughty 2024]]) and keratinocyte chromatin potential ([[10-Summaries/ma-2020-share-seq|SHARE-seq]]) both show accessibility running ahead of transcription, so treating accessibility as a proxy for activity needs care (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromatin-actuation|Chromatin actuation]] — An element simultaneously open and bound on one fiber.
> - `concept` [[30-Concepts/single-molecule-footprinting|Single-molecule footprinting]] — Per-fiber maps of nucleosomes, TF occupancy and accessibility.
> - `concept` [[30-Concepts/fiber-seq|Fiber-seq]] — m6A methyltransferase footprinting read by long-read sequencing.
> - `concept` [[30-Concepts/daf-seq|DAF-seq]] — Deaminase footprinting that survives amplification, enabling single-cell fibers.
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Somatic genotype plus scATAC from the same nucleus.
> - `concept` [[30-Concepts/jak2-v617f|JAK2 V617F]] — Driver mutation with cell-intrinsic chromatin priming in HSCs.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA is packaged along chromosomes and how that varies across fibers, haplotypes and cells.
> - `note` [[50-Notes/regulatory-layers-overview|Regulatory layers overview]] — Accessibility as one of the four molecular regulatory layers.

## All sources on this page

> [!info]- 18 summaries cited here
> - [[10-Summaries/andrewb-2020-science|Stergachis 2020]]
> - [[10-Summaries/ashuach-2022-peakvi|Ashuach 2022]]
> - [[10-Summaries/avsec-2026-alphagenome|AlphaGenome 2026]]
> - [[10-Summaries/bohaczuk-2024-targeted-fiberseq|Bohaczuk 2024]]
> - [[10-Summaries/boshar-2025-ntv3|NTv3 2025]]
> - [[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]
> - [[10-Summaries/cao-2018-sci-car|Cao 2018]]
> - [[10-Summaries/cusanovich-2015-sciatac|Cusanovich 2015]]
> - [[10-Summaries/de-boer-2018-brockman|de Boer & Regev 2018]]
> - [[10-Summaries/doughty-2024-smf-tf|Doughty 2024]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/kelley-2016-basset|Basset 2016]]
> - [[10-Summaries/ma-2020-share-seq|Ma 2020]]
> - [[10-Summaries/ma-2025-hybridna|HybriDNA 2025]]
> - [[10-Summaries/schep-2017-chromvar|Schep 2017]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
> - [[10-Summaries/vishniakov-2025-gene42|Gene42 2025]]
> - [[10-Summaries/zhao-2024-scada|Zhao 2024]]
