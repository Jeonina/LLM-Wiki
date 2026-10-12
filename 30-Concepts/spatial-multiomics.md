---
type: concept
title: Spatial multi-omics
aliases: [spatial omics, spatial transcriptomics, spatial multi-omic]
tags: [spatial, multi-omics, tissue-context]
created: 2026-05-11
updated: 2026-10-12
---

# Spatial multi-omics

> Single-cell multi-omics measurements that preserve **spatial position** within an intact tissue, so that gene expression, chromatin or protein readouts can be mapped back onto the tissue's anatomical structure. Two parallel architectures exist: imaging-based (in situ hybridization or sequencing) and NGS-based (barcoded capture surfaces) ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]; [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).

> [!abstract] 한눈에
> Spatial multi-omics는 조직을 해리하지 않고 위치 정보를 유지한 채 발현·염색질·단백질을 측정하는 방법이며, imaging 기반과 NGS 기반 두 계열이 해상도와 측정 폭을 서로 맞바꾼다 ([[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]). Spatial epigenome assay가 아직 드물어서, 위치가 없는 single-cell 데이터를 공간에 붙이는 계산 방법이 그 빈자리를 메우고 있다 ([[10-Summaries/biancalani-2021-tangram|Tangram]]; [[10-Summaries/debnath-2026-ison|ISON]]).

## Definition

Spatial multi-omics methods fall into two families ([[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]; [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]):

- **Imaging-based** — subcellular resolution and hundreds to thousands of multiplexed transcripts, but a limited transcript count compared with NGS and complex imaging infrastructure.
- **NGS-based** — unbiased (full transcriptome) with a straightforward workflow, but typically ~10–100 μm resolution, i.e. multiple cells per spot until recent advances.

## Why it matters

Dissociation for conventional scRNA-seq destroys spatial relationships, neighbourhood signals and cell–cell communication patterns; spatial multi-omics preserves them for the analysis of:

- tumour microenvironment heterogeneity;
- developmental tissue patterning;
- brain region-specific cell-type distributions;
- immune cell infiltration in pathology.

Three technologies have three complementary failures: sc/snRNA-seq profiles comprehensively but loses position, spatial transcriptomics keeps position at lower resolution and sensitivity, and targeted in-situ methods have both but limited gene throughput ([[10-Summaries/biancalani-2021-tangram|Tangram]]). This trade is the reason spatial data needed a computational layer at all, and it applies unchanged to spatial epigenomics today (synthesis).

## Assay families

| Family | Method | How it works | Source |
|---|---|---|---|
| Imaging | MERFISH, seqFISH+ | Sequential rounds of single-molecule FISH read 100s–1000s of transcripts in situ | ([[10-Summaries/baysoy-2023-multiomics-landscape\|Baysoy 2023]]; [[10-Summaries/vandereyken-2023-scmultiomics-review\|Vandereyken 2023]]) |
| Imaging | In situ sequencing (ISS, FISSEQ) | Sequences transcripts directly within fixed tissue | ([[10-Summaries/baysoy-2023-multiomics-landscape\|Baysoy 2023]]; [[10-Summaries/vandereyken-2023-scmultiomics-review\|Vandereyken 2023]]) |
| NGS | Visium (10x) | Tissue mounted on a slide patterned with positional barcodes; lysed mRNA captured at its location of origin | ([[10-Summaries/baysoy-2023-multiomics-landscape\|Baysoy 2023]]; [[10-Summaries/vandereyken-2023-scmultiomics-review\|Vandereyken 2023]]) |
| NGS | Slide-seq / Slide-seqV2 | Randomly placed barcoded beads with known positions | ([[10-Summaries/baysoy-2023-multiomics-landscape\|Baysoy 2023]]; [[10-Summaries/vandereyken-2023-scmultiomics-review\|Vandereyken 2023]]) |
| NGS | Stereo-seq, DBiT-seq | Higher-resolution variants | (synthesis; not covered in the cited reviews) |
| NGS, methylome + transcriptome | Spatial-DMT | Whole-genome DNA methylation (EM-seq chemistry) and the transcriptome on one tissue section by in situ microfluidic barcoding (50×50 grid, 10–50 μm pixels) | ([[10-Summaries/cardilla-2025-spatial-methylome\|Spatial-DMT]]) |

Other modalities:

- **Spatial protein / metabolite** modalities (CODEX, IMC, MALDI-imaging) parallel the transcriptomic methods.
- **Spatial methylation** and **spatial chromatin accessibility** are emerging.

## Computational bridges to dissociated data

Two 2021–2022 methods define the computational bridge between dissociated and spatial data, and they solve **different** problems ([[10-Summaries/biancalani-2021-tangram|Tangram]]; [[10-Summaries/kleshchevnikov-2022-cell2location|cell2location]]); a later method targets the missing spatial epigenome ([[10-Summaries/debnath-2026-ison|ISON]]).

| Method | Output | Approach | Source |
|---|---|---|---|
| [[10-Summaries/biancalani-2021-tangram\|Tangram]] | Individual cells mapped onto positions | Alignment across five platform types (MERFISH, STARmap, smFISH, Visium, and even histological images) | ([[10-Summaries/biancalani-2021-tangram\|Tangram]]) |
| [[10-Summaries/kleshchevnikov-2022-cell2location\|cell2location]] | Cell-type proportions per location | Bayesian deconvolution that borrows statistical strength across locations, which is what lets it resolve fine subtypes a per-spot method cannot | ([[10-Summaries/kleshchevnikov-2022-cell2location\|cell2location]]) |
| [[10-Summaries/debnath-2026-ison\|ISON]] | Spatial chromatin accessibility, then spatially resolved GRNs | Learns a cross-modality decoder from spatial transcriptomics plus single-cell multiome | ([[10-Summaries/debnath-2026-ison\|ISON]]) |

- **Alignment vs deconvolution is an assay property, not a preference.** When spots contain many cells, proportions are the honest output; as resolution approaches single cells, mapping is (synthesis).
- **Two routes to a missing spatial epigenome assay.** Because SHARE-seq measures RNA and ATAC in the same cell, aligning the RNA to space carries the ATAC with it, and Tangram used this to reveal spatial patterns of chromatin accessibility ([[10-Summaries/biancalani-2021-tangram|Tangram]]); ISON reaches the same goal five years later without a paired spatial assay, by learning a cross-modality decoder ([[10-Summaries/debnath-2026-ison|ISON]]) (synthesis).
- Spatial multiome kits are not commercially available, while spatial transcriptomics and single-cell multiome kits both are; ISON exploits that asymmetry computationally ([[10-Summaries/debnath-2026-ison|ISON]]).
- See also [[reference-atlas-mapping]].

## Evidence and examples

- Spatial-DMT recovers 136,639–281,447 CpGs and 1,890–4,626 genes per pixel ([[10-Summaries/cardilla-2025-spatial-methylome|Spatial-DMT]]).
- cell2location resolved regional **astrocyte subtypes** across thalamus and hypothalamus, a rare **pre-germinal-centre B cell** population in lymph node, and fine immune populations in gut lymphoid follicles ([[10-Summaries/kleshchevnikov-2022-cell2location|cell2location]]).
- Tangram revealed spatial patterns of chromatin accessibility by aligning SHARE-seq RNA to space ([[10-Summaries/biancalani-2021-tangram|Tangram]]).
- Mapping tumour immune infiltration via Visium + CODEX in cancer biopsies.
- Brain region atlases using MERFISH (Allen Brain Cell Atlas).

## Contested points

- **Resolution vs breadth.** Imaging wins on resolution, NGS on breadth; convergence remains incomplete.
- **Cost.** Spatial methods are 5–50× the cost per sample of conventional single-cell.
- **ISON's evaluation is constrained by the same data gap it addresses.** No dataset pairs spatial multiome with sc-multiome from the same tissue, so every benchmark splits one spatial multiome dataset into pseudo-sc-multiome and pseudo-spatial halves, or transfers across timepoints ([[10-Summaries/debnath-2026-ison|ISON]]) (synthesis).
- **A bet against the hardware roadmap.** If spatial epigenome assays commercialise, ISON's motivation weakens ([[10-Summaries/cardilla-2025-spatial-methylome|Spatial-DMT]]; [[10-Summaries/debnath-2026-ison|ISON]]) (synthesis).
- **Ground truth barely exists** for spatial assignment, so accuracy claims across this whole class rest on anatomical plausibility and marker consistency rather than on knowing which cell was really where (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/reference-atlas-mapping|Reference atlas mapping]] — Placing query cells into an annotated reference and transferring labels or unmeasured modalities.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Measuring two or more molecular modalities in the same single cell.

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/baysoy-2023-multiomics-landscape|Baysoy 2023]]
> - [[10-Summaries/biancalani-2021-tangram|Biancalani 2021]]
> - [[10-Summaries/cardilla-2025-spatial-methylome|Lee 2025]]
> - [[10-Summaries/debnath-2026-ison|Debnath 2026]]
> - [[10-Summaries/kleshchevnikov-2022-cell2location|Kleshchevnikov 2022]]
> - [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]
