---
type: summary
title: "Bartosovic 2023 — Multimodal chromatin profiling using nanobody-based single-cell CUT&Tag (nano-CT)"
source: "[[00-Sources/papers/Multimodal chromatin profiling using nanobody-based single-cell CUT&Tag]]"
aliases: [Bartosovic 2023, nano-CT, Marek 2023, nanobody-CUT-and-Tag]
tags: [scCUT&Tag, nano-CT, single-cell-chromatin, multimodal, multi-omics, brain, method]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Bartosovic et al. (2023) — *Multimodal chromatin profiling using nanobody-based single-cell CUT&Tag (nano-CT)* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-022-01535-4)

# Bartosovic et al. 2023 — nano-CT

> Marek Bartosovic, **Gonçalo Castelo-Branco\***. *Nature Biotechnology* **41**, 794–805 (June 2023). DOI: 10.1038/s41587-022-01535-4. Karolinska Institutet.

## Thesis

**nano-CT (nanobody-Tn5 fusion-based single-cell CUT&Tag)** simultaneously maps **up to three epigenomic modalities** at single-cell resolution per nucleus by using **nanobody-Tn5 fusion proteins** specific to either mouse-IgG or rabbit-IgG primary antibodies. Compatible with 25,000–200,000 cell input, with significantly higher sensitivity and fragments-per-cell than [[marek-2021-naturebiotechnology|conventional scCUT&Tag]]. Applied to juvenile mouse brain: simultaneous profiling of chromatin accessibility + H3K27ac + H3K27me3 reveals more cell types than unimodal scCUT&Tag, infers chromatin velocity in oligodendrocyte lineage, and deconvolutes two sequential waves of H3K27me3 repression during oligodendrocyte progression.

## Mechanism

1. **Two nano-Tn5 fusion proteins**: one with nanobody anti-mouse-IgG (ms-Tn5) loaded with MeA/Me-Rev oligos; one with nanobody anti-rabbit-IgG (rb-Tn5) loaded with different barcoded oligos.
2. Both primary antibodies (mouse + rabbit) incubated simultaneously with cells → both nanobody-Tn5s bind to their respective primary antibodies in one pot.
3. Secondary antibody step is **omitted** (nanobodies directly bind primary antibodies) → simpler workflow, fewer washes, higher recovery.
4. Tagmentation step deposits modality-specific barcoded adapters at each antibody-bound chromatin region.
5. **Optional 3rd modality**: pre-treatment with non-fused barcoded ATAC Tn5 before nano-CT step → accessibility + 2 histone marks in same cell.
6. 10x Genomics Chromium for single-cell barcoding + library prep.

## Key claims

- **Higher fragments per cell than scCUT&Tag** (median 6,123–14,496 for nano-CT vs 1,832–6,510 for scCUT&Tag at same cell input).
- Better cell-type deconvolution: 5,157 dual-modality cells across 12 clusters vs scCUT&Tag's ~similar count but fewer fine-grained types.
- **Chromatin velocity**: ATAC vs H3K27ac dynamics in oligodendrocyte lineage reveal genes where accessibility precedes activation; analog of RNA velocity but at chromatin layer.
- **Two sequential H3K27me3 repression waves** during oligodendrocyte differentiation — gene modules previously bivalent become permanently silenced in sequential order.
- Identified fine-grained cell types missed by unimodal scCUT&Tag: more sub-clusters in astrocytes (4) and vascular leptomeningeal cells (3).

## Surprising / load-bearing for the review

- **The current high-water mark of single-cell histone-modification multimodality** for §3.4 of the review. nano-CT joins [[scchix-seq]] (two marks via computational deconvolution) and [[multi-tag]] (multiple antibody-conjugated Tn5s) as ways to get >1 chromatin mark per cell.
- The **chromatin velocity** concept from nano-CT is analogous to [[chromatin-velocity]] in single-cell ATAC+RNA assays, but now multi-modal at chromatin-only level.
- For §4.6 joint-assay coverage, nano-CT is the cleanest 3-modality chromatin-only joint assay (ATAC + 2 histone marks) — complements the DNA-anchored joint assays.

## Entities / concepts touched

[[cut-and-tag]] · [[multi-tag]] · [[scchix-seq]] · [[scicut-tag]] · [[chromatin-velocity]] · [[single-cell-multiomics]] · [[40-Topics/histone-modifications]] · [[40-Topics/chromatin-architecture]] · [[40-Topics/single-cell-multiomics]]

## Related summaries

- [[marek-2021-naturebiotechnology]] — Bartosovic 2021 scCUT&Tag, predecessor.
- [[10-Summaries/abdulhay-2020-samosa]] — SMRT-Tag, complementary single-molecule multimodal chromatin.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-022-01535-4) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/36536148/)

---
**Source:** [DOI](https://doi.org/10.1038/s41587-022-01535-4) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/36536148/)
