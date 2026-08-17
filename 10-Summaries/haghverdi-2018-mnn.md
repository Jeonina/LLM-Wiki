---
type: summary
title: "Haghverdi et al. 2018 — Batch effects in single-cell RNA-sequencing data are corrected by matching mutual nearest neighbors (MNN)"
source: "[[00-Sources/papers/Batch effects in single-cell RNA-sequencing data are corrected by matching mutual nearest neighbors]]"
source_kind: paper
author: "Laleh Haghverdi, Aaron T. L. Lun, Michael D. Morgan, John C. Marioni (corresponding)"
published: 2018-04-02
ingested: 2026-08-17
doi: "10.1038/nbt.4091"
journal: "Nature Biotechnology 36:421–427"
tags: [MNN, batch-correction, mutual-nearest-neighbors, ComBat, limma, composition-assumption, Human-Cell-Atlas]
entities: []
concepts: ["[[batch-effect]]", "[[multimodal-integration-methods]]", "[[dimensionality-reduction]]", "[[cell-type-annotation]]"]
topics: ["[[computational-methods]]", "[[single-cell-multiomics]]"]
---

**Citation:** Haghverdi, Lun, Morgan & Marioni (2018) — *Batch effects in single-cell RNA-sequencing data are corrected by matching mutual nearest neighbors* — *Nature Biotechnology* 36, 421–427. [DOI](https://doi.org/10.1038/nbt.4091)

# Haghverdi 2018 — MNN correction

> Bulk batch-correction methods carry an assumption that is **false for single-cell data**: that population composition is identical across batches. When it is not — and it never is, because dissociation, culture and sorting all shift cell-type abundance — the estimated batch coefficient absorbs real biology, and "the results might potentially be worse than if no correction were performed." MNN replaces the assumption with a much weaker one: **only a subset of the population needs to be shared**.

## Key claims

- **The composition assumption is the flaw, stated precisely.** limma's `removeBatchEffect` and ComBat fit a linear model with a batch blocking term and zero out its coefficient; RUVseq and svaseq identify unknown factors and regress them out. All were designed for bulk, where composition is fixed. In scRNA-seq the abundance of each cell type varies between batches even when the same types are present, so "the estimated coefficients for the batch blocking factors are not purely technical but contain a nonzero biological component."
- **Mutual nearest neighbours define the anchor.** Cells that are each other's nearest neighbours across batches are inferred to be the same cell type; the expression difference within an MNN pair estimates the batch effect, and averaging across many pairs sharpens it into a correction vector.
- **Overlap is discovered, not assumed.** The method automatically identifies which subpopulations are shared and uses only those for correction — so batch-specific cell types do not distort the estimate.
- **Landmark/projection approaches fail on novel cell types.** The alternative strategy of projecting new data onto reference landmarks breaks when the new batch contains cell types outside the reference's transcriptional space — they get projected somewhere arbitrary.
- **Scales to droplet data.** Demonstrated on multiple droplet-based scRNA-seq datasets with large cell numbers.
- **The Human Cell Atlas is the motivating context**: large projects must generate data at different times, by different operators, with different dissociation protocols, library chemistries and sequencers — batch effects are structural, not accidental.

## Methods / evidence

Simulated and real scRNA-seq datasets spanning different biological systems and technologies, benchmarked against linear-model methods; scalability demonstrated on multiple droplet datasets.

Weight: the conceptual argument — that composition-invariance is the wrong assumption — is stronger and more durable than any specific benchmark, and it reframed the whole batch-correction subfield.

## Surprising or load-bearing bits

- **"Correction can be worse than no correction"** is the sentence that changed practice. It converted batch correction from a routine preprocessing step into a modelling decision with a failure mode. (synthesis)
- **Published the same day as [[butler-2018-seurat-cca|Seurat CCA integration]]**, in the same journal, solving the same problem from a different direction — MNN works in the original high-dimensional expression space, Seurat works in a shared low-dimensional space found by canonical correlation analysis. The two papers together define the start of the modern integration literature. (synthesis)
- **The MNN pair is the ancestor of the "anchor."** Seurat v3 renamed and generalised the idea; [[hao-2024-seurat-v5|Seurat v5]] bridge integration and [[kang-2021-symphony|Symphony]]'s reference mapping are both descendants of the same intuition — find provably corresponding cells, then use their difference as the correction. (synthesis)
- **Correcting in expression space, not embedding space**, is a distinguishing property with practical consequences: MNN returns corrected expression values usable for differential expression, whereas [[korsunsky-2019-harmony|Harmony]] corrects only the embedding and leaves expression untouched.

## Concepts touched

- [[batch-effect]] — the composition-invariance critique and the MNN alternative; this is the founding source for the concept in its single-cell form.
- [[multimodal-integration-methods]] — MNN pairs as the earliest form of cross-dataset anchoring.

## Connections to other sources

- Same-day counterpart solving the same problem via CCA: [[butler-2018-seurat-cca]].
- Descendants of the anchor idea: [[hao-2021-seurat-wnn]], [[hao-2024-seurat-v5]], [[kang-2021-symphony]].
- Embedding-space alternative: [[korsunsky-2019-harmony]]; matrix-factorisation alternative [[welch-2019-liger]].
- Integration taxonomy that places all of these: [[argelaguet-2021-integration-principles]]; benchmark [[xiao-2024-multiomics-benchmark]].
- Deep generative successors: [[ashuach-2023-multivi]], [[cao-2022-glue]], [[gayoso-2021-totalvi]].
- Best-practice context: [[heumos-2023-best-practices]].

## Open questions

- **MNN pairs can be wrong** when two distinct cell types are each other's nearest cross-batch neighbours because their true counterparts are absent — the paper's shared-subset requirement mitigates but does not eliminate this. (synthesis)
- Order-dependence when correcting more than two batches sequentially is a known practical issue not addressed here.
- The trade between correcting expression (usable downstream, riskier) and correcting embeddings only (safer, less usable) is never resolved in the literature. (synthesis)

## Related

- [[butler-2018-seurat-cca]] · [[korsunsky-2019-harmony]] · [[batch-effect]] · [[40-Topics/computational-methods]]
