---
type: summary
title: "Hao et al. 2021 — Integrated analysis of multimodal single-cell data (Seurat v4 / weighted nearest neighbor)"
source: "[[00-Sources/papers/Integrated analysis of multimodal single-cell data]]"
source_kind: paper
author: "Yuhan Hao, Stephanie Hao, Erica Andersen-Nissen, William M. Mauck, … Tim Stuart, Peter Smibert, Rahul Satija (corresponding)"
published: 2021-06-24
ingested: 2026-08-17
doi: "10.1016/j.cell.2021.04.048"
journal: "Cell 184:3573–3587.e29"
tags: [WNN, Seurat-v4, CITE-seq, multimodal-reference, reference-mapping, PBMC-atlas, vaccination, COVID-19]
entities: ["[[rahul-satija]]"]
concepts: ["[[multimodal-integration-methods]]", "[[cite-seq]]", "[[cell-type-annotation]]", "[[dimensionality-reduction]]", "[[batch-effect]]", "[[joint-single-cell-multi-omics]]"]
topics: ["[[single-cell-multiomics]]", "[[computational-methods]]"]
---

**Citation:** Hao et al. (2021) — *Integrated analysis of multimodal single-cell data* — *Cell* 184, 3573–3587.e29. [DOI](https://doi.org/10.1016/j.cell.2021.04.048)

# Hao 2021 — Seurat v4 / WNN

> When two modalities are measured in the same cell, how much should each one count? WNN's answer is: **learn it per cell**. Rather than concatenating modalities or picking one, weighted nearest neighbor analysis infers, for every individual cell, the relative utility of each data type — because a T cell's identity may be better resolved by surface protein while a progenitor's is better resolved by RNA.

## Key claims

- **The weight is per cell, and unsupervised.** WNN "learns the relative utility of each data type in each cell." This is the conceptual core: modality informativeness is not a global property of the assay but a local property of the cell state being resolved.
- **A 211,000-cell CITE-seq PBMC reference atlas** with panels extending to **228 antibodies** — at the time far beyond typical CITE-seq panel sizes.
- **Multimodal analysis resolves states single-modality analysis cannot**, and this is demonstrated rather than asserted: previously unreported lymphoid subpopulations were identified and validated.
- **Reference-based mapping of query datasets onto the multimodal atlas** — the workflow that made "map to a reference" a routine operation rather than a research project.
- **Applied to interpret immune responses to vaccination and to COVID-19**, i.e. the atlas is built to be used, not only to exist.
- The stated ambition is definitional: to "look beyond the transcriptome toward a unified and multimodal definition of cellular identity."

## Methods / evidence

CITE-seq on 211,000 PBMCs with up to 228 antibodies; WNN applied to build the reference; novel lymphoid populations identified and experimentally validated; query datasets from vaccination and COVID-19 cohorts mapped onto the reference.

Weight: the scale and the validation of new populations are the strongest evidence. The method is demonstrated primarily on RNA+protein; its behaviour on RNA+ATAC (where modality informativeness differs much more sharply) is a separate question.

## Surprising or load-bearing bits

- **Per-cell modality weighting is the honest answer to a question most integration methods dodge.** Concatenation implicitly weights by feature count; picking a "primary" modality biases the analysis; WNN measures. The [[argelaguet-2021-integration-principles|integration taxonomy]] calls this vertical integration, and WNN is its canonical implementation. (synthesis)
- **This is the paper the wiki previously lacked.** [[stuart-2021-natmethods|Stuart 2021]] is Signac (chromatin), not WNN; the WNN reference was missing from the corpus until now. Any manuscript sentence citing "Seurat WNN" needs *this* citation. (synthesis)
- **Reference atlases changed the unit of analysis.** Before this, every study defined cell types from scratch; after, mapping to a shared reference became the default — which is also what makes [[kang-2021-symphony|Symphony]]'s "map in seconds without the raw reference" problem worth solving. (synthesis)
- **228 antibodies is a scale at which post-hoc contextualisation stops working.** With a handful of markers you can cluster on RNA and look at protein afterwards; with 228 you need joint modelling — the same argument [[gayoso-2021-totalvi|totalVI]] makes.
- **Author overlap with the whole Satija line** (Stuart, Smibert, Butler, Hoffman) makes this the middle term of a single continuous programme: [[butler-2018-seurat-cca|CCA alignment 2018]] → anchors v3 → **WNN v4 2021** → [[hao-2024-seurat-v5|bridge integration v5 2024]].

## Entities mentioned

- [[rahul-satija]] — corresponding author; the Seurat programme.

## Concepts touched

- [[multimodal-integration-methods]] — WNN as the canonical vertical (paired) integration method.
- [[cite-seq]] — the assay this was built for, at 228-antibody scale.
- [[cell-type-annotation]] — reference mapping as the annotation mechanism.

## Connections to other sources

- The Seurat lineage: [[butler-2018-seurat-cca]] → this → [[hao-2024-seurat-v5]]; chromatin arm [[stuart-2021-natmethods]].
- Probabilistic alternative for the same CITE-seq problem: [[gayoso-2021-totalvi]]; faster deep-learning alternative [[lakkis-2022-scipenn]] (which criticises Seurat 4 as computationally expensive and unable to merge partially-overlapping protein panels).
- Reference-mapping successor built on Seurat-style embeddings: [[kang-2021-symphony]].
- Taxonomy placing WNN as vertical integration: [[argelaguet-2021-integration-principles]]; benchmark [[xiao-2024-multiomics-benchmark]].
- Other paired-modality assays WNN is applied to: [[ma-2020-cell]] (SHARE-seq), [[clark-2018-scnmt-seq]], [[izzo-2024-got-cha]].
- Batch-correction ancestors: [[haghverdi-2018-mnn]], [[korsunsky-2019-harmony]].
- Best practices: [[heumos-2023-best-practices]].

## Open questions

- **Does per-cell weighting behave well when one modality is far sparser?** RNA+protein are both relatively dense; RNA+ATAC or RNA+methylation are not, and the weighting could collapse onto the dense modality. Not tested here. (synthesis)
- Reference atlases embed the reference's biases; mapping a query onto a PBMC atlas built from healthy donors may distort disease states — the vaccination/COVID applications probe this but do not resolve it.
- Computational cost is flagged as a weakness by later methods ([[lakkis-2022-scipenn]]).

## Related

- [[butler-2018-seurat-cca]] · [[hao-2024-seurat-v5]] · [[gayoso-2021-totalvi]] · [[multimodal-integration-methods]]
