---
type: summary
title: "Butler et al. 2018 — Integrating single-cell transcriptomic data across different conditions, technologies, and species (Seurat CCA alignment)"
source: "[[00-Sources/papers/Integrating single-cell transcriptomic data across different conditions, technologies, and species]]"
source_kind: paper
author: "Andrew Butler, Paul Hoffman, Peter Smibert, Efthymia Papalexi, Rahul Satija (corresponding)"
published: 2018-04-02
ingested: 2026-08-17
doi: "10.1038/nbt.4096"
journal: "Nature Biotechnology 36:411–420"
tags: [Seurat, CCA, manifold-alignment, integration, cross-species, cross-technology, PBMC, pancreas]
entities: ["[[rahul-satija]]"]
concepts: ["[[batch-effect]]", "[[multimodal-integration-methods]]", "[[dimensionality-reduction]]", "[[cell-type-annotation]]", "[[scrna-seq]]"]
topics: ["[[computational-methods]]", "[[single-cell-multiomics]]"]
---

**Citation:** Butler, Hoffman, Smibert, Papalexi & Satija (2018) — *Integrating single-cell transcriptomic data across different conditions, technologies, and species* — *Nature Biotechnology* 36, 411–420. [DOI](https://doi.org/10.1038/nbt.4096)

# Butler 2018 — Seurat CCA alignment

> The Seurat integration line begins here, and it begins with a borrowed idea: **manifold alignment from computer vision**. Find the gene–gene correlation structure that is *conserved* across datasets using canonical correlation analysis, embed cells in that shared space, then non-linearly warp to fix scale differences. The framing is not "remove the batch effect" but "find what the datasets have in common."

## Key claims

- **Four requirements are stated up front**, and they define what integration must do beyond bulk batch correction: (1) align subpopulations **even if each has a unique response** — the key challenge outside the scope of bulk methods, which assume confounders act uniformly on all cells; (2) allow **changes in cellular density** (subpopulation frequency shifts) between conditions; (3) be robust to **feature-scale changes** from global transcriptional shifts or differing normalisation; (4) require **no pre-established markers** or targeting to defined cell subsets.
- **Five-step workflow**: learn conserved gene-correlation structure via CCA; optionally flag cells poorly described by that shared structure (identifying non-overlapping rare populations); align into a conserved low-dimensional space using non-linear warping robust to density shifts; run integrated downstream analysis (clustering, trajectories); then compare aligned subpopulations to find density or expression changes.
- **The confound it dissolves**: without joint analysis it is difficult to distinguish a change in *cell-type proportion* from a change in *expression within a cell type*, and analysing datasets together naively conflates the two.
- **Three demonstrations spanning the three axes** in the title: 13 aligned PBMC subpopulations resting versus IFN-β-stimulated (condition); hematopoietic progenitors across two profiling technologies (technology); human and mouse pancreatic islet atlases (species).
- **Flagging poorly-aligned cells is a feature, not an error mode** — cells that resist the shared structure may be genuinely dataset-specific populations worth examining separately.
- Scales from hundreds to tens of thousands of cells; shipped in the Seurat R toolkit.

## Methods / evidence

Five sets of published scRNA-seq experiments posing distinct alignment challenges. Validation is by biological interpretability of the aligned subpopulations rather than by a ground-truth metric — appropriate for 2018, before integration benchmarks existed.

## Surprising or load-bearing bits

- **Published the same day, same journal, as [[haghverdi-2018-mnn|MNN correction]].** Two independent solutions to the same problem: MNN corrects in high-dimensional expression space using mutually-nearest cross-batch cells; Seurat aligns in a shared low-dimensional CCA space. The field's two dominant strategies — anchor-based and embedding-based — were born on the same day. (synthesis)
- **"Each subpopulation may have a unique response" is the requirement that separates single-cell integration from bulk batch correction**, and it is why a single global correction vector cannot work. It is also, later, the hardest thing about diagonal integration. (synthesis)
- **The computer-vision provenance is explicit** — the method is motivated by image alignment and registration techniques. Cross-field borrowing recurs throughout this literature: nested effects models from perturbation screens into [[ross-2016-onconem|OncoNEM]], Steiner trees into [[foroughmand-2022-scelestial|Scelestial]], node2vec into [[xiong-2024-scghost|scGHOST]]. (synthesis)
- **This is the ancestor of the anchor framework** that runs through Seurat v3 → [[hao-2021-seurat-wnn|v4 WNN]] → [[hao-2024-seurat-v5|v5 bridge integration]], and of the reference-mapping tools ([[kang-2021-symphony|Symphony]]) built on top of it.

## Entities mentioned

- [[rahul-satija]] — corresponding author; the Seurat line.

## Concepts touched

- [[multimodal-integration-methods]] — CCA-based manifold alignment as the anchor-family founder.
- [[batch-effect]] — reframed from "nuisance to remove" to "shared structure to find".

## Connections to other sources

- Same-day counterpart: [[haghverdi-2018-mnn]].
- Direct descendants: [[hao-2021-seurat-wnn]] (WNN, multimodal), [[hao-2024-seurat-v5]] (bridge integration, dictionary learning), [[stuart-2021-natmethods]] (Signac, chromatin).
- Built on Seurat anchors: [[kang-2021-symphony]]; label-transfer competitor [[song-2021-scgcn]].
- Alternative strategies: [[korsunsky-2019-harmony]] (embedding-space iterative), [[welch-2019-liger]] (integrative NMF).
- Taxonomy and benchmark: [[argelaguet-2021-integration-principles]], [[xiao-2024-multiomics-benchmark]].
- Best practices: [[heumos-2023-best-practices]].

## Open questions

- **CCA can over-align.** Forcing datasets into a shared correlation structure risks erasing genuine biological differences — the concern that becomes acute for diagonal integration ([[argelaguet-2021-integration-principles]]). (synthesis)
- No quantitative metric for over- versus under-correction is offered; that problem waited for the benchmarking literature.
- Cross-species alignment assumes orthologous genes behave comparably, which the paper applies but does not test.

## Related

- [[haghverdi-2018-mnn]] · [[hao-2021-seurat-wnn]] · [[multimodal-integration-methods]] · [[40-Topics/computational-methods]]
