---
type: summary
title: "Bartosovic 2021 — Single-cell CUT&Tag profiles histone modifications and transcription factors in complex tissues"
aliases: [Bartosovic 2021, scCUT&Tag, Marek 2021]
tags: [scCUT&Tag, single-cell-chromatin, histone-modifications, brain, oligodendrocyte, method]
created: 2026-05-12
updated: 2026-05-12
sources: ["00-Sources/papers/Marek_2021_NatureBiotechnology.pdf"]
---

**Citation:** Bartosovic et al. (2021) — *Single-cell CUT&Tag profiles histone modifications and transcription factors in complex tissues* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-021-00869-9)

# Bartosovic et al. 2021 — scCUT&Tag in complex tissues

> Marek Bartosovic, Mukund Kabbe, **Gonçalo Castelo-Branco\***. *Nature Biotechnology* **39**, 825–835 (July 2021). DOI: 10.1038/s41587-021-00869-9. Karolinska Institutet.

## Thesis

Combined the **CUT&Tag** chromatin-profiling chemistry (Henikoff lab) with the **10x Genomics droplet scATAC-seq platform** to produce **scCUT&Tag** — droplet-based single-cell histone modification + TF profiling in tens of thousands of cells. Applied to mouse central nervous system (cortex, oligodendrocyte lineage) to profile H3K4me3, H3K27ac, H3K36me3, H3K27me3 (active and repressive marks) plus Olig2 and Rad21 TFs. Resolved cell types from chromatin marks alone, mapped enhancer-promoter connectivity, identified H3K4me3 spreading and promoter bivalency.

## Mechanism

1. Cells/nuclei + 1% BSA in buffers to reduce nuclei clumping.
2. **Antibody-directed tagmentation** (CUT&Tag): protein A-Tn5 fusion guided by antibody against histone modification, performs in situ tagmentation only at antibody-bound chromatin.
3. **10x Genomics Chromium** scATAC-seq v1/v1.1 platform processes tagmented nuclei → barcoded single-cell libraries.
4. Per-cell median 597–568 unique fragments for H3K27me3 in 4,872/3,873 cells from cell-line mixtures.
5. Applied to mouse postnatal P15 / P21–P25 brain with sorted GFP+/− cells (Sox10-Cre lineage label).

## Key claims

- Resolves **cell types from chromatin profile alone** in cell-line mixtures (mESC, NIH/3T3, Oli-neu) and mouse CNS.
- Captures the **oligodendrocyte differentiation trajectory** at chromatin level: H3K4me3, H3K27me3, H3K27ac, H3K36me3 reorganize during P15 → P25 myelination onset.
- **Olig2 single-cell binding profile** shows lineage-specific occupancy patterns; **Rad21 (cohesin)** profile complements TAD mapping.
- Public web resource: [mouse-brain-cutandtag.cells.ucsc.edu](https://mouse-brain-cutandtag.cells.ucsc.edu/).

## Surprising / load-bearing for the review

- **One of the first droplet-platform scCUT&Tag implementations** for complex tissue (the other being Wu 2021 *Nat Biotechnol* with iCell8 nanowell). Together they establish the droplet/nanowell axis for scaling single-cell histone profiling.
- For the planned review's **§3.4 (Chromatin State)**, scCUT&Tag sits alongside [[scicut-tag|sciCUT&Tag]] (Henikoff lab, combinatorial-indexing scaling), [[scchic-seq]] (Zhao lab, MNase-based), and [[scchix-seq]] (van Oudenaarden lab, two marks per cell).
- The follow-up [[marek-2023-naturebiotechnology|Bartosovic 2023 nano-CT]] extends this to three modalities per cell.

## Entities / concepts touched

[[cut-and-tag]] · [[scchic-seq]] · [[scicut-tag]] · [[multi-tag]] · [[histone-modifications]] · [[scatac-seq]] · [[40-Topics/histone-modifications]] · [[40-Topics/chromatin-architecture]]

## Related summaries

- [[marek-2023-naturebiotechnology]] — Bartosovic 2023, nano-CT three-modality successor.
- [[scalable-single-cell-profiling-of-chromatin-modifications-with-scicut-tag]] — Janssens/Henikoff sciCUT&Tag.
- [[scchix-seq-infers-dynamic-relationships-between-histone-modifications-in-single-cells]] — scChIX-seq two-mark deconvolution.
