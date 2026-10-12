---
type: concept
title: Cell Type Annotation
aliases: [cell typing, marker genes, label transfer, cell identity]
tags: [annotation, markers, atlases, cell-identity]
created: 2026-08-10
updated: 2026-10-12
---

# Cell Type Annotation

> Assigning biological identity to clusters. Usually done by marker genes; increasingly done jointly across modalities, which raises the question of whether a cell type defined by expression is the same object as one defined by chromatin state ([[10-Summaries/cao-2019-moca|Cao 2019]]; [[10-Summaries/welch-2019-liger|LIGER]]).

> [!abstract] 한눈에
> Cell type annotation은 cluster에 생물학적 정체성을 붙이는 일로, 전통적으로 marker gene에 기대지만 점점 reference에서 label을 옮겨 오는 방식과 여러 modality를 함께 쓰는 방식으로 바뀌고 있다 ([[10-Summaries/cao-2019-moca|Cao 2019]]; [[10-Summaries/kang-2021-symphony|Symphony]]; [[10-Summaries/welch-2019-liger|LIGER]]). 다만 cell type의 정의는 대개 cluster 해상도에 따른 조작적 정의라서, 옮겨 온 label도 원래 annotation의 편향을 그대로 물려받는다 ([[10-Summaries/cao-2019-moca|Cao 2019]]).

## Definition

Annotation assigns biological identity to clusters, usually by marker genes ([[10-Summaries/cao-2019-moca|Cao 2019]]). Cluster resolution determines type count, and definitions are typically operational rather than external ([[10-Summaries/cao-2019-moca|Cao 2019]]); see [[30-Concepts/clustering-algorithms|clustering algorithms]]. Each modality is a different glimpse into cellular identity, so cell types can also be defined jointly from RNA and epigenome profiles ([[10-Summaries/welch-2019-liger|LIGER]]).

## Why it matters

- Integration must preserve type distinctions while mixing datasets, which is what cell-type LISI measures ([[10-Summaries/korsunsky-2019-harmony|Harmony]]); see [[30-Concepts/batch-effect|batch effect]].
- Annotation granularity sets which somatic mutations SComatic can detect: mutations acquired before two annotated types diverged appear in both and are discarded as germline, so finer annotations restrict calls to later mutations ([[10-Summaries/muyas-2024-scomatic|SComatic]]).
- Annotation is increasingly **transferred** rather than derived ([[10-Summaries/kang-2021-symphony|Symphony]]; [[10-Summaries/hao-2024-seurat-v5|Hao 2024]]; [[10-Summaries/song-2021-scgcn|scGCN]]).

## Approaches

### Deriving labels from the data

| Approach | Example | What it uses | Source |
|---|---|---|---|
| Marker genes at atlas scale | [[10-Summaries/cao-2019-moca\|MOCA]] | Differentially expressed cell-type-specific markers | ([[10-Summaries/cao-2019-moca\|Cao 2019]]) |
| Somatic mutation profiles | [[10-Summaries/xu-2012-single-cell-exome-kidney\|Xu 2012]] | Single-cell exome SNVs, used to reassign putative tumour cells as normal | ([[10-Summaries/xu-2012-single-cell-exome-kidney\|Xu 2012]]) |
| Chromatin contact structure | [[10-Summaries/ramani-2017-scihi-c\|sciHi-C]], [[10-Summaries/zhang-2022-higashi\|Higashi]] | scHi-C alone, with imputation in Higashi | ([[10-Summaries/ramani-2017-scihi-c\|Ramani 2017]]; [[10-Summaries/zhang-2022-higashi\|Higashi]]) |
| Similarity to bulk reference profiles | [[10-Summaries/ji-2017-scrat\|SCRAT]] | Aggregated scATAC/scDNase signals compared with a pre-compiled panel of ENCODE bulk DNase-seq profiles | ([[10-Summaries/ji-2017-scrat\|SCRAT]]) |
| De novo scATAC annotation | [[10-Summaries/ashuach-2022-peakvi\|PeakVI]] | Cluster-marker differential accessibility plus gene-signature enrichment | ([[10-Summaries/ashuach-2022-peakvi\|PeakVI]]) |
| Joint multimodal definition | [[10-Summaries/welch-2019-liger\|LIGER]] | Cortical cell types defined jointly from RNA and epigenome profiles | ([[10-Summaries/welch-2019-liger\|LIGER]]) |

### Transferring labels

| Approach | Example | How it works | Source |
|---|---|---|---|
| Reference mapping | [[10-Summaries/kang-2021-symphony\|Symphony]]; [[10-Summaries/ashuach-2022-peakvi\|PeakVI]] (scArches-style) | Localise query cells in a frozen annotated embedding, then transfer labels; deliberately annotation-agnostic so labels can be revised without recomputing the embedding | ([[10-Summaries/kang-2021-symphony\|Symphony]]; [[10-Summaries/ashuach-2022-peakvi\|PeakVI]]) |
| Anchor-based transfer | The Seurat line: [[10-Summaries/butler-2018-seurat-cca\|CCA alignment]], [[10-Summaries/hao-2021-seurat-wnn\|WNN]], [[10-Summaries/hao-2024-seurat-v5\|bridge integration]] | Corresponding cells across datasets anchor the transfer | ([[10-Summaries/butler-2018-seurat-cca\|Butler 2018]]; [[10-Summaries/hao-2021-seurat-wnn\|Hao 2021]]; [[10-Summaries/hao-2024-seurat-v5\|Hao 2024]]) |
| Graph-based classification | [[10-Summaries/song-2021-scgcn\|scGCN]] | A graph convolutional network over the cell graph; argues prior methods "extract shared information from individual cells but ignore higher-order relations between cells" | ([[10-Summaries/song-2021-scgcn\|scGCN]]) |
| Foundation-model annotators | [[10-Summaries/chen-2025-epiagent\|EpiAgent]], [[10-Summaries/liu-2025-clm-access\|CLM-access]], [[10-Summaries/liu-2025-scarf\|SCARF]], [[10-Summaries/liu-2025-scmomer\|scMomer]], [[10-Summaries/li-2026-clm-x\|CLM-X]], [[10-Summaries/yu-2026-scdynomics\|scDynOmics]] | Zero-shot annotators, fine-tuning, or probes and heads on frozen embeddings | ([[10-Summaries/chen-2025-epiagent\|EpiAgent]]; [[10-Summaries/liu-2025-clm-access\|CLM-access]]; [[10-Summaries/liu-2025-scarf\|SCARF]]; [[10-Summaries/liu-2025-scmomer\|scMomer]]; [[10-Summaries/li-2026-clm-x\|CLM-X]]; [[10-Summaries/yu-2026-scdynomics\|scDynOmics]]) |
| Deconvolution | [[10-Summaries/kleshchevnikov-2022-cell2location\|cell2location]] | The abundance-level analogue for spot data — cell-type proportions rather than per-cell labels | ([[10-Summaries/kleshchevnikov-2022-cell2location\|cell2location]]) |

## Evidence and examples

**Marker-based annotation at scale**

- 68% of genes (17,789 of 26,183) are differentially expressed across major cell types, yielding **2,863 cell-type-specific markers** at >2-fold between first- and second-ranked type, and a median of 20 markers per subtype ([[10-Summaries/cao-2019-moca|Cao 2019]]).
- Most were not previously characterized as markers of the respective cell types, and a novel notochord marker (*Tox2*) was confirmed by whole-mount in situ hybridization ([[10-Summaries/cao-2019-moca|Cao 2019]]).
- Annotation quality is uneven: mesenchymal and connective-tissue clusters — the largest populations — were hardest to annotate for lack of known markers ([[10-Summaries/cao-2019-moca|Cao 2019]]).
- Cross-atlas matching linked 96 fetal (E14.5) cell types of the Mouse Cell Atlas to 58 MOCA developmental subtypes, each atlas informing the other's anatomy or embryonic origin ([[10-Summaries/cao-2019-moca|Cao 2019]]).

**Annotation from non-expression data**

- Three of twenty putative tumour cells were reassigned as normal purely on their somatic mutation profiles ([[10-Summaries/xu-2012-single-cell-exome-kidney|Xu 2012]]).
- Cell types separate on chromatin contact structure alone, with the separating components corresponding to real karyotypic differences ([[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]).
- Neuron subtypes resolve from scHi-C alone after imputation, where earlier methods could not ([[10-Summaries/zhang-2022-higashi|Higashi]]).

**Transfer and foundation-model benchmarks**

- scGCN was benchmarked across 30 datasets spanning tissues, platforms, species and **molecular layers** (RNA→ATAC) ([[10-Summaries/song-2021-scgcn|scGCN]]).
- EpiAgent's zero-shot annotators reach accuracy above 0.88 (brain) and 0.95 (non-brain) on held-out datasets ([[10-Summaries/chen-2025-epiagent|EpiAgent]]).
- Fine-tuned CLM-access reached macro-F1 0.544 and 0.674 on two ~70k-cell scATAC datasets, against 0.361/0.547 for scATAnno and 0.343/0.396 for Cellcano ([[10-Summaries/liu-2025-clm-access|CLM-access]]).
- A logistic-regression probe on frozen SCARF embeddings trained on 10% of BMMC cells reached >0.75 accuracy, macro F1, recall and precision on the other 90%, beating scFoundation ([[10-Summaries/liu-2025-scarf|SCARF]]).
- With an MLP head on mostly frozen embeddings, scMomer reached 0.808 accuracy and 0.703 F1 on Zheng68K, against 0.768 and 0.647 for its scBERT backbone ([[10-Summaries/liu-2025-scmomer|scMomer]]).
- A gated RNA/ATAC fusion head on CLM-X reached macro F1 88.24% on four 10x PBMC multiome sets, against 85.44% for Seurat WNN and 67.45% for CLM-X ATAC-only ([[10-Summaries/li-2026-clm-x|CLM-X]]).
- On mouse gastrulation, multiome-pretrained scDynOmics fine-tuned on spliced/unspliced RNA reached 0.82 median 10-fold accuracy, against 0.78 without pretraining and 0.82 for a tuned scANVI ([[10-Summaries/yu-2026-scdynomics|scDynOmics]]).

## Contested points

- **Is an expression-defined type the same object as a chromatin-defined one?** Joint annotation across modalities raises this question rather than settling it ([[10-Summaries/welch-2019-liger|LIGER]]).
- **Operational definitions.** Cluster resolution determines type count, and definitions are typically operational rather than external ([[10-Summaries/cao-2019-moca|Cao 2019]]).
- **Cross-modality transfer (RNA→ATAC) is the demanding case** because the two share no feature space; the mapping runs through gene-activity scores, each of which imposes assumptions — the weak link [[10-Summaries/hao-2024-seurat-v5|bridge integration]] was later designed to avoid (synthesis).
- **The shared risk of transfer.** A transferred label is returned with the same apparent confidence as a directly measured one, and inherits every bias of the source annotation, propagating silently at scale; none of the transfer papers quantifies it (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/clustering-algorithms|Clustering algorithms]] — Partitioning cells into groups; the step that produces the clusters being annotated.
> - `concept` [[30-Concepts/multimodal-integration-methods|Multimodal integration methods]] — Combining modalities into one representation, the basis of joint annotation.
> - `concept` [[30-Concepts/batch-effect|Batch effect]] — Technical variation that integration must remove without erasing type distinctions.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Measuring two or more modalities in the same cell.

## All sources on this page

> [!info]- 21 summaries cited here
> - [[10-Summaries/ashuach-2022-peakvi|Ashuach 2022]]
> - [[10-Summaries/butler-2018-seurat-cca|Butler 2018]]
> - [[10-Summaries/cao-2019-moca|Cao 2019]]
> - [[10-Summaries/chen-2025-epiagent|Chen 2025]]
> - [[10-Summaries/hao-2021-seurat-wnn|Hao 2021]]
> - [[10-Summaries/hao-2024-seurat-v5|Hao 2024]]
> - [[10-Summaries/ji-2017-scrat|Ji 2017]]
> - [[10-Summaries/kang-2021-symphony|Kang 2021]]
> - [[10-Summaries/kleshchevnikov-2022-cell2location|Kleshchevnikov 2022]]
> - [[10-Summaries/korsunsky-2019-harmony|Korsunsky 2019]]
> - [[10-Summaries/li-2026-clm-x|CLM-X 2026]]
> - [[10-Summaries/liu-2025-clm-access|CLM-access 2025]]
> - [[10-Summaries/liu-2025-scarf|SCARF 2025]]
> - [[10-Summaries/liu-2025-scmomer|scMomer 2025]]
> - [[10-Summaries/muyas-2024-scomatic|Muyas 2024]]
> - [[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]
> - [[10-Summaries/song-2021-scgcn|Song 2021]]
> - [[10-Summaries/welch-2019-liger|Welch 2019]]
> - [[10-Summaries/xu-2012-single-cell-exome-kidney|Xu 2012]]
> - [[10-Summaries/yu-2026-scdynomics|scDynOmics 2026]]
> - [[10-Summaries/zhang-2022-higashi|Zhang 2022]]
