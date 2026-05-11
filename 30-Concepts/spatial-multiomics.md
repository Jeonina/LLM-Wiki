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

Two families ([[10-Summaries/alev-2023-naturereviewsmolecularcellbiology]], [[10-Summaries/katy-2023-naturereviewsgenetics]]):

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

- [[single-cell-multiomics]]
- [[40-Topics/single-cell-multiomics]]
