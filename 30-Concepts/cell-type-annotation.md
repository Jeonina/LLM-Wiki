---
type: concept
title: Cell Type Annotation
aliases: [cell typing, marker genes, label transfer, cell identity]
tags: [annotation, markers, atlases, cell-identity]
created: 2026-08-10
updated: 2026-10-08
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
- Cross-atlas matching linked 96 fetal (E14.5) cell types of the Mouse Cell Atlas to 58 MOCA developmental subtypes, each atlas informing the other's anatomy or embryonic origin ([[cao-2019-moca]]).
- Integration must preserve type distinctions while mixing datasets, which is what cell-type LISI measures ([[korsunsky-2019-harmony]]).

## The standing caveat

Cluster resolution determines type count, and definitions are typically operational rather than external ([[cao-2019-moca]]); see [[clustering-algorithms]].

## Added 2026-10-07

In SComatic, the granularity of cell-type annotation sets which somatic mutations are detectable: mutations acquired before two annotated types diverged appear in both and are discarded as germline, so finer annotations restrict calls to later mutations ([[10-Summaries/muyas-2024-scomatic]]).

An early regulome approach labelled single cells by similarity of aggregated scATAC/scDNase signals to a pre-compiled panel of ENCODE bulk DNase-seq profiles (SCRAT) [[10-Summaries/ji-2017-scrat]].

For scATAC-seq, PeakVI supports both scArches-style reference mapping and de novo annotation via cluster-marker differential accessibility plus gene-signature enrichment ([[10-Summaries/ashuach-2022-peakvi]]). EpiAgent's zero-shot annotators reach accuracy above 0.88 (brain) and 0.95 (non-brain) on held-out datasets ([[10-Summaries/chen-2025-epiagent]]).


## Added 2026-10-08 — sequence models & foundation models

- Fine-tuned CLM-access reached macro-F1 0.544 and 0.674 on two ~70k-cell scATAC datasets, against 0.361/0.547 for scATAnno and 0.343/0.396 for Cellcano ([[10-Summaries/liu-2025-clm-access]]).
- A logistic-regression probe on frozen SCARF embeddings trained on 10% of BMMC cells reached >0.75 accuracy, macro F1, recall and precision on the other 90%, beating scFoundation ([[10-Summaries/liu-2025-scarf]])
- With an MLP head on mostly frozen embeddings, scMomer reached 0.808 accuracy and 0.703 F1 on Zheng68K, against 0.768 and 0.647 for its scBERT backbone ([[10-Summaries/liu-2025-scmomer]])
- A gated RNA/ATAC fusion head on CLM-X reached macro F1 88.24% on four 10x PBMC multiome sets, against 85.44% for Seurat WNN and 67.45% for CLM-X ATAC-only ([[10-Summaries/li-2026-clm-x]])
- On mouse gastrulation, multiome-pretrained scDynOmics fine-tuned on spliced/unspliced RNA reached 0.82 median 10-fold accuracy, against 0.78 without pretraining and 0.82 for a tuned scANVI ([[10-Summaries/yu-2026-scdynomics]])

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
