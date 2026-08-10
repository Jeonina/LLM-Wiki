---
type: summary
title: "Welch et al. 2019 — Single-cell multi-omic integration compares and contrasts features of brain cell identity (LIGER)"
source: "[[00-Sources/papers/Single-Cell Multi-omic Integration Compares and Contrasts Features of Brain Cell Identity]]"
source_kind: paper
author: "Joshua D. Welch, Velina Kozareva, Ashley Ferreira, Charles Vanderburg, Carly Martin, Evan Z. Macosko (corresponding)"
published: 2019-06-13
ingested: 2026-08-10
doi: "10.1016/j.cell.2019.05.006"
journal: "Cell"
tags: [LIGER, iNMF, metagene-factors, integration, brain, bed-nucleus, substantia-nigra, spatial, epigenome]
entities: ["[[evan-macosko]]", "[[joshua-welch]]"]
concepts: ["[[multimodal-integration-methods]]", "[[batch-effect]]", "[[dimensionality-reduction]]", "[[cell-type-annotation]]", "[[dna-methylation]]", "[[chromatin-accessibility]]"]
topics: ["[[single-cell-multiomics]]", "[[computational-methods]]"]
---

> ⚠️ **Source caveat.** The clipping in `00-Sources/` captured the article front matter — title, journal metadata, highlights, keywords and the opening of the introduction — but not the Results or Methods. The claims below are limited to what the source actually states; quantitative results (factor counts, cell numbers, benchmark comparisons) are **not** available from this source and are deliberately not asserted here. Re-clip the full text before extending this page.

**Citation:** Welch et al. (2019) — *Single-cell multi-omic integration compares and contrasts features of brain cell identity* — *Cell* 177, 1873–1887.e17. [DOI](https://doi.org/10.1016/j.cell.2019.05.006)

# Welch 2019 — LIGER

> Integration by **matrix factorization into shared and dataset-specific metagene factors**. Where [[korsunsky-2019-harmony|Harmony]] corrects an embedding toward a common space and [[hao-2024-seurat-v5|Seurat]] transfers labels across anchor pairs, LIGER's integrative non-negative matrix factorization keeps *both* halves — the factors cells share across datasets and the factors specific to each — so the analysis can **compare and contrast** rather than only merge.

## Key claims

*(Per the source caveat above, these are the paper's stated contributions as given in its highlights and introduction.)*

- **Shared and dataset-specific metagene factors enable single-cell data integration** — the methodological claim, and the design that distinguishes LIGER from correction-based approaches.
- **LIGER reveals inter-individual differences** in cells of the bed nucleus of the stria terminalis and the substantia nigra.
- **Integration of *in situ* and dissociated scRNA-seq maps cell types in space** — cross-modality integration where one modality carries spatial position and the other carries transcriptome depth.
- **Joint definition of cortical cell types from single-cell RNA and epigenome profiles** — cell identity defined across expression and epigenomic measurement rather than within one.
- Framing from the introduction: mammalian brain function depends on coordinated activity of highly specialized cell types; scRNA-seq has been applied across regions, perturbations and species, and new technologies now measure DNA methylation, chromatin accessibility and *in situ* expression in thousands to millions of cells. **Each experimental context and measurement modality provides a different glimpse into cellular identity** — so defining a cell type requires integrating diverse measurements from multiple experiments and biological contexts.
- Published in the same *Cell* issue as Stuart et al.'s Seurat v3 anchor-based integration, with an accompanying commentary — the two approaches arrived as an explicit pair.

## Methods / evidence

Not available from this source clipping. The source records the study design at the level of its four highlighted results (bed nucleus and substantia nigra inter-individual analysis, spatial-plus-dissociated integration, and joint RNA-plus-epigenome cortical typing) without the supporting quantitative detail.

## Surprising or load-bearing bits

- **Keeping dataset-specific factors is the conceptual difference, and it is a different research question.** A correction method's success criterion is that datasets become indistinguishable; LIGER's is that what differs between them remains legible and interpretable as factors. For comparing individuals, species or modalities — as opposed to pooling replicates — those are not interchangeable goals. The "compares and contrasts" in the title is the argument.
- **Inter-individual differences as a target, not a nuisance.** Most integration work treats donor as a covariate to remove ([[korsunsky-2019-harmony|Harmony]] corrects across 36 donors); here individual variation in brain nuclei is the finding. The same algorithmic machinery serves both aims depending on which factors you read.
- **Joint RNA-plus-epigenome cell typing** is the concrete instance of the general question in [[argelaguet-2021-integration-principles]] and [[zhu-2020-multimodal-power-of-many]]: whether cell type defined by expression coincides with cell type defined by chromatin state. That two modalities can be factorized into shared factors at all is a substantive claim about cell identity.
- The paper's own framing — each modality is "a different glimpse into cellular identity" — is the cleanest one-line statement in this corpus of why multi-omics exists, and it sets up the anchor taxonomy used across [[single-cell-multiomics]].

## Entities mentioned

- [[evan-macosko]] — corresponding author; Drop-seq and the Broad's brain single-cell program.
- [[joshua-welch]] — first author; LIGER's continued development.

## Concepts touched

- [[multimodal-integration-methods]] — LIGER is the factorization branch (integrative NMF), alongside embedding correction and anchor transfer.
- [[cell-type-annotation]] — cell type defined jointly across modalities rather than within one.

## Connections to other sources

- Published alongside and directly comparable to Seurat v3 anchors, whose lineage continues in [[hao-2024-seurat-v5]]; the embedding-correction alternative is [[korsunsky-2019-harmony]].
- Conceptual framing: [[argelaguet-2021-integration-principles]], [[zhu-2020-multimodal-power-of-many]], [[lim-2024-single-cell-omics-review]].
- Brain multi-omic context: [[lake-2018-brain-snrna-scths]]; spatial context: [[vandereyken-2023-spatial-multiomics]].

## Open questions

- **This page is incomplete pending a full-text clipping** — the factorization details, benchmarks against contemporaries, and the substance of the inter-individual and spatial findings are not in the source.
- The general open question the paper's design raises: whether "dataset-specific factor" is biology or technical artefact is decided by interpretation, not by the algorithm, and the source does not state how that decision is made.

## Related

- [[multimodal-integration-methods]] · [[korsunsky-2019-harmony]] · [[argelaguet-2021-integration-principles]] · [[single-cell-multiomics]]
