---
type: concept
title: Cell Type Annotation
aliases: [cell typing, marker genes, label transfer, cell identity]
tags: [annotation, markers, atlases, cell-identity]
created: 2026-08-10
updated: 2026-08-10
---

# Cell Type Annotation

> Assigning biological identity to clusters. Usually done by marker genes; increasingly done jointly across modalities, which raises the question of whether a cell type defined by expression is the same object as one defined by chromatin state.

## Marker-based annotation at scale

68% of genes (17,789 of 26,183) are differentially expressed across major cell types, yielding **2,863 cell-type-specific markers** at >2-fold between first- and second-ranked type, and a median of 20 markers per subtype ([[cao-2019-moca]]). Most were not previously characterized as markers of the respective cell types, and a novel notochord marker (*Tox2*) was confirmed by whole-mount in situ hybridization ([[cao-2019-moca]]).

Annotation quality is uneven: mesenchymal and connective-tissue clusters — the largest populations — were hardest to annotate for lack of known markers ([[cao-2019-moca]]).

## Annotation from the data rather than from priors

- Three of twenty putative tumour cells were reassigned as normal purely on their somatic mutation profiles ([[xu-2012-single-cell-exome-kidney]]).
- Cell types separate on chromatin contact structure alone, with the separating components corresponding to real karyotypic differences ([[ramani-2017-scihi-c]]).
- Neuron subtypes resolve from scHi-C alone after imputation, where earlier methods could not ([[zhang-2022-higashi]]).

## Cross-modal and cross-atlas identity

- Joint definition of cortical cell types from RNA and epigenome profiles ([[welch-2019-liger]]), with the general framing that each modality is a different glimpse into cellular identity ([[welch-2019-liger]]).
- Cross-atlas matching linked 96 adult-atlas cell types to 58 developmental subtypes, each atlas informing the other's anatomy or embryonic origin ([[cao-2019-moca]]).
- Integration must preserve type distinctions while mixing datasets, which is what cell-type LISI measures ([[korsunsky-2019-harmony]]).

## The standing caveat

Cluster resolution determines type count, and definitions are typically operational rather than external ([[cao-2019-moca]]); see [[clustering-algorithms]].

## Related

- [[clustering-algorithms]] · [[multimodal-integration-methods]] · [[batch-effect]] · [[single-cell-multiomics]]

## Added 2026-08-17

Annotation is increasingly **transferred** rather than derived. Three routes ingested 2026-08-14, with a shared risk.

- **Reference mapping** — localise query cells in a frozen annotated embedding, then transfer labels; deliberately annotation-agnostic so labels can be revised without recomputing the embedding ([[10-Summaries/kang-2021-symphony]]).
- **Anchor-based transfer** — the Seurat line, from [[10-Summaries/butler-2018-seurat-cca|CCA alignment]] through [[10-Summaries/hao-2021-seurat-wnn|WNN]] and [[10-Summaries/hao-2024-seurat-v5|bridge integration]].
- **Graph-based classification** — [[10-Summaries/song-2021-scgcn|scGCN]] argues prior methods "extract shared information from individual cells but ignore higher-order relations between cells", and uses a graph convolutional network over the cell graph; benchmarked across 30 datasets spanning tissues, platforms, species, and **molecular layers** (RNA→ATAC).

Cross-modality transfer (RNA→ATAC) is the demanding case because the two share no feature space; the mapping runs through gene-activity scores, each of which imposes assumptions — the weak link [[10-Summaries/hao-2024-seurat-v5|bridge integration]] was later designed to avoid. (synthesis)

**The shared risk**: a transferred label is returned with the same apparent confidence as a directly measured one, and inherits every bias of the source annotation, propagating silently at scale. None of these papers quantifies it. (synthesis)

Deconvolution is the abundance-level analogue for spot data — cell-type proportions rather than per-cell labels ([[10-Summaries/kleshchevnikov-2022-cell2location]]).
