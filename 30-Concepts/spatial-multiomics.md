---
type: concept
title: Spatial multi-omics
aliases: [spatial omics, spatial transcriptomics, spatial multi-omic]
tags: [spatial, multi-omics, tissue-context]
created: 2026-05-11
updated: 2026-05-11
---

# Spatial multi-omics

> Single-cell multi-omics measurements that preserve **spatial position** within an intact tissue, so that gene expression / chromatin / protein readouts can be mapped back onto the tissue's anatomical structure. Two parallel architectures: imaging-based (in situ hybridization or sequencing) and NGS-based (barcoded capture surfaces).

## Definition

Two families ([[10-Summaries/baysoy-2023-multiomics-landscape]], [[10-Summaries/vandereyken-2023-scmultiomics-review]]):

**Imaging-based**:
- **MERFISH, seqFISH+** — sequential rounds of single-molecule FISH read 100s–1000s of transcripts in situ.
- **In situ sequencing (ISS, FISSEQ)** — sequence transcripts directly within fixed tissue.
- Pros: subcellular resolution, multiplex hundreds to thousands of transcripts.
- Cons: limited transcript count compared to NGS; complex imaging infrastructure.

**NGS-based**:
- **Visium (10x)** — tissue mounted on a slide patterned with positional barcodes; lysed mRNA captured at its location of origin.
- **Slide-seq / Slide-seqV2** — randomly placed barcoded beads with known positions.
- **Stereo-seq, DBiT-seq** — higher-resolution variants.
- Pros: unbiased (full transcriptome), straightforward workflow.
- Cons: typically ~10–100 μm resolution (multiple cells per spot until recent advances).

## Why it matters

Tissue context matters: dissociation for conventional scRNA-seq destroys spatial relationships, neighborhood signals, and cell-cell communication patterns. Spatial multi-omics preserves these for analysis of:

- Tumor microenvironment heterogeneity.
- Developmental tissue patterning.
- Brain region-specific cell type distributions.
- Immune cell infiltration in pathology.

## Variants and refinements

- **Spatial protein / metabolite** modalities (CODEX, IMC, MALDI-imaging) parallel the transcriptomic methods.
- **Spatial methylation** and **spatial chromatin accessibility** are emerging.

## Contested points

- Resolution gap between imaging and NGS approaches — imaging wins on resolution, NGS on breadth. Convergence remains incomplete.
- Cost: spatial methods are 5–50× the cost per sample of conventional single-cell.

## Examples

- Mapping tumor immune infiltration via Visium + CODEX in cancer biopsies.
- Brain region atlases using MERFISH (Allen Brain Cell Atlas).

## Related

- [[40-Topics/single-cell-multiomics]]
- [[40-Topics/single-cell-multiomics]]

## Added 2026-08-13

Spatial multiome kits are not commercially available, while spatial transcriptomics and single-cell multiome kits both are — an asymmetry that ISON exploits computationally, inferring spatial chromatin accessibility and then spatially resolved GRNs from the two available data types ([[10-Summaries/debnath-2026-ison]]).

**The evaluation is constrained by the same data gap it addresses**: no dataset pairs spatial multiome with sc-multiome from the same tissue, so every benchmark splits one spatial multiome dataset into pseudo-sc-multiome and pseudo-spatial halves, or transfers across timepoints ([[10-Summaries/debnath-2026-ison]]). (synthesis)

The method is a bet against the hardware roadmap: if spatial epigenome assays commercialise, the motivation weakens ([[10-Summaries/cardilla-2025-spatial-methylome]]; [[10-Summaries/debnath-2026-ison]]). (synthesis)

## Added 2026-08-17

Two 2021–2022 methods define the computational bridge between dissociated and spatial data, and they solve **different** problems.

**Three technologies, three complementary failures** ([[10-Summaries/biancalani-2021-tangram]]): sc/snRNA-seq profiles comprehensively but loses position; spatial transcriptomics keeps position at lower resolution and sensitivity; targeted in-situ methods have both but limited gene throughput. This trade is the reason spatial data needed a computational layer at all — and it applies unchanged to spatial epigenomics today. (synthesis)

**Alignment vs deconvolution is an assay property, not a preference.** [[10-Summaries/biancalani-2021-tangram|Tangram]] maps *individual cells* onto positions across five platform types (MERFISH, STARmap, smFISH, Visium, and even histological images). [[10-Summaries/kleshchevnikov-2022-cell2location|cell2location]] estimates *cell-type proportions* per location by Bayesian deconvolution, borrowing statistical strength across locations — which is what lets it resolve fine subtypes a per-spot method cannot. When spots contain many cells, proportions are the honest output; as resolution approaches single cells, mapping is. (synthesis)

cell2location's results show what "fine-grained" buys: regional **astrocyte subtypes** across thalamus and hypothalamus, a rare **pre-germinal-centre B cell** population in lymph node, and fine immune populations in gut lymphoid follicles ([[10-Summaries/kleshchevnikov-2022-cell2location]]).

**Spatial chromatin accessibility by propagation, in 2021.** Because SHARE-seq measures RNA and ATAC in the same cell, aligning the RNA to space carries the ATAC with it — Tangram used this to reveal spatial patterns of chromatin accessibility ([[10-Summaries/biancalani-2021-tangram]]). [[10-Summaries/debnath-2026-ison|ISON]] reaches the same goal five years later without a paired spatial assay, by learning a cross-modality decoder. Two routes to substituting computation for a missing spatial epigenome assay. (synthesis)

**Ground truth barely exists** for spatial assignment, so accuracy claims across this whole class rest on anatomical plausibility and marker consistency rather than on knowing which cell was really where. (synthesis) See also [[reference-atlas-mapping]].
