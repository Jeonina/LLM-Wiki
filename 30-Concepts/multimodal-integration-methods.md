---
type: concept
title: Multimodal integration methods
aliases: [multi-omics integration, multimodal integration, cross-modality integration]
tags: [computational, integration, multiomics, machine-learning]
created: 2026-05-19
updated: 2026-10-12
paper_section: ["4.3"]
---

# Multimodal integration methods

> Computational methods that combine several single-cell omics modalities, measured on the same cells (paired) or on separate cell populations (unpaired), into one low-dimensional representation. They fall into three families, matrix factorization, manifold alignment and deep generative models ([[10-Summaries/wang-2023-multimodal-review|Wang 2023]]), and three topologies, horizontal, vertical and diagonal ([[10-Summaries/bi-2024-multiomics-review|Bi & Weng 2024]]).

> [!abstract] 한눈에
> Multimodal integration은 여러 single-cell 데이터를 하나의 저차원 공간으로 합치는 계산 방법이며, 무엇을 anchor로 삼는지(feature, cell, 또는 없음)가 방법의 가정과 실패 양상을 정한다 ([[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]). Matrix factorization, anchor 기반 방법, deep generative model에 이어 최근에는 foundation model까지 RNA–ATAC 통합에서 경쟁하고 있다 ([[10-Summaries/wang-2023-multimodal-review|Wang 2023]]; [[10-Summaries/liu-2025-scarf|SCARF]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [분석 도구 교재](../60-Explainers/computational-methods.html)
<!-- /explainer-links -->

## Definition

Integration takes datasets that differ in modality, in cells, or in both, and places them in a shared space ([[10-Summaries/wang-2023-multimodal-review|Wang 2023]]). Under the Argelaguet taxonomy the **anchor determines the assumptions**: *horizontal* integration anchors on features (batch correction), *vertical* on cells (matched multimodal), *diagonal* applies when no anchor exists in high-dimensional space, and *mosaic* when different modalities are measured on different cells from the same sample, leaving entire matrices missing ([[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]; [[10-Summaries/bi-2024-multiomics-review|Bi & Weng 2024]]). For same-cell assays see [[30-Concepts/joint-single-cell-multi-omics|joint single-cell multi-omics]].

## Why it matters

Single-cell integration has to do things bulk batch correction cannot: align subpopulations even when **each has a unique response**, tolerate **shifts in subpopulation frequency**, be robust to feature-scale changes, and need no pre-established markers ([[10-Summaries/butler-2018-seurat-cca|Butler 2018]]). Bulk methods (limma, ComBat, RUVseq, svaseq) assume confounders act uniformly on all cells and that **population composition is identical across batches**; when that fails the batch coefficient absorbs real biology, and "the results might potentially be worse than if no correction were performed" ([[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]).

## Integration topologies

| Topology | Data shape | Anchor | Main difficulty | Source |
|---|---|---|---|---|
| Horizontal (unpaired) | Same modality, different cell populations | Shared genomic features | Batch correction | ([[10-Summaries/bi-2024-multiomics-review\|Bi & Weng 2024]]; [[10-Summaries/wang-2023-multimodal-review\|Wang 2023]]; [[10-Summaries/argelaguet-2021-integration-principles\|Argelaguet 2021]]) |
| Vertical (paired) | Different modalities, same cells | The cell | *Alignment* of within-cell features | ([[10-Summaries/bi-2024-multiomics-review\|Bi & Weng 2024]]; [[10-Summaries/argelaguet-2021-integration-principles\|Argelaguet 2021]]) |
| Diagonal (unpaired) | Different modalities, different cells | None in high-dimensional space | The hardest case, because batch correction risks erasing biology | ([[10-Summaries/bi-2024-multiomics-review\|Bi & Weng 2024]]; [[10-Summaries/argelaguet-2021-integration-principles\|Argelaguet 2021]]) |
| Mosaic | Different modalities on different cells from the same sample | Partial | Entire matrices missing | ([[10-Summaries/argelaguet-2021-integration-principles\|Argelaguet 2021]]) |

A second, six-setup taxonomy distinguishes one sample (1S), across samples (+S), across experiments (+X+S), multiple modalities in the same cell (+M1C), different modalities in different cells (+M+C) and a full reference (+all) ([[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]). See [[reference-atlas-mapping]] for the asymmetric case, where the reference is frozen.

## Method families

| Family | Methods | How it works | Source |
|---|---|---|---|
| Matrix factorization | MOFA ([[10-Summaries/argelaguet-2018-mofa\|MOFA]]), MOFA+ ([[10-Summaries/argelaguet-2020-mofa-plus\|MOFA+]]), LIGER ([[10-Summaries/welch-2019-liger\|LIGER]]), ISON ([[10-Summaries/debnath-2026-ison\|ISON]]) | Extract latent factors per modality; struggle at high dimensionality | ([[10-Summaries/argelaguet-2020-mofa-plus\|MOFA+]]; [[10-Summaries/wang-2023-multimodal-review\|Wang 2023]]) |
| Anchor / nearest-neighbour and manifold alignment | MNN ([[10-Summaries/haghverdi-2018-mnn\|MNN]]), Seurat CCA ([[10-Summaries/butler-2018-seurat-cca\|Butler 2018]]), WNN ([[10-Summaries/hao-2021-seurat-wnn\|Hao 2021]]), bridge integration ([[10-Summaries/hao-2024-seurat-v5\|Hao 2024]]), Tangram, Cell2location | CCA, MNN and WNN are all in Seurat; anchors are mutually nearest cells or shared low-dimensional axes | ([[10-Summaries/stuart-2021-natmethods\|Stuart 2021]]; [[10-Summaries/wang-2023-multimodal-review\|Wang 2023]]) |
| Embedding-space iterative | Harmony ([[10-Summaries/korsunsky-2019-harmony\|Harmony]]) | Corrects only the embedding and leaves expression untouched | ([[10-Summaries/korsunsky-2019-harmony\|Harmony]]) |
| Deep generative | totalVI ([[10-Summaries/gayoso-2021-totalvi\|totalVI]]), sciPENN ([[10-Summaries/lakkis-2022-scipenn\|sciPENN]]), scMVP, MultiVI ([[10-Summaries/ashuach-2023-multivi\|MultiVI]]), Cobolt ([[10-Summaries/gong-2021-cobolt\|Cobolt]]), scJoint, GLUE ([[10-Summaries/cao-2022-glue\|GLUE]]), Symphony | Shared latent space learned by a generative network | ([[10-Summaries/wang-2023-multimodal-review\|Wang 2023]]) |
| Graph neural network | scGCN ([[10-Summaries/song-2021-scgcn\|scGCN]]) | Graph convolutional label transfer | ([[10-Summaries/song-2021-scgcn\|scGCN]]) |
| Supervised cross-modality prediction | snDrop-seq + scTHS-seq integration ([[10-Summaries/lake-2018-brain-snrna-scths\|Lake 2018]]) | Gradient-boosting models predict accessibility from expression and the reverse, applied down a transcriptome-derived dendrogram; an early diagonal method with its failure boundary reported | ([[10-Summaries/lake-2018-brain-snrna-scths\|Lake 2018]]) |
| Foundation models | SCARF ([[10-Summaries/liu-2025-scarf\|SCARF]]), scMomer ([[10-Summaries/liu-2025-scmomer\|scMomer]]), CLM-X ([[10-Summaries/li-2026-clm-x\|CLM-X]]) | Pretrained on millions of cells; SCARF uses a contrastive alignment loss on 2.7 M paired 10x Multiome cells, CLM-X a multiway Transformer | ([[10-Summaries/liu-2025-scarf\|SCARF]]; [[10-Summaries/li-2026-clm-x\|CLM-X]]) |

### Factor analysis: MOFA and its successors

- The factor-analysis branch originates with MOFA (*Molecular Systems Biology* 2018), a Bayesian group factor analysis model that decomposes each modality as Yᵐ = ZWᵐᵀ + εᵐ with shared factors Z and sparse per-modality weights ([[10-Summaries/argelaguet-2018-mofa|MOFA]]).
- MOFA reports the variance each factor explains in each modality, so shared and modality-specific axes can be told apart ([[10-Summaries/argelaguet-2018-mofa|MOFA]]); MOFA+ is its scalable successor ([[10-Summaries/argelaguet-2020-mofa-plus|MOFA+]]).
- ISON's linear KL-NMF model carries a Laplacian spatial-smoothness prior and modality-specific batch-correction vectors ([[10-Summaries/debnath-2026-ison|ISON]]).

### Anchors, bridges and per-cell weights

- MNN and Seurat CCA alignment appeared in the same issue of *Nature Biotechnology* on 2 April 2018 and solve the same problem from opposite directions: MNN corrects in high-dimensional expression space via mutually nearest cross-batch cells, while Seurat aligns in a shared low-dimensional CCA space ([[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]; [[10-Summaries/butler-2018-seurat-cca|Butler 2018]]). The field's two dominant strategies were born the same day. (synthesis)
- **Per-cell modality weighting**: concatenation implicitly weights by feature count and choosing a "primary" modality biases the analysis, whereas WNN *learns the relative utility of each data type in each cell* ([[10-Summaries/hao-2021-seurat-wnn|Hao 2021]]).
- **Bridge integration** removes the gene-activity assumption by treating each cell of a multiomic dataset as a dictionary atom, learning the cross-modality relationship instead of assuming it ([[10-Summaries/hao-2024-seurat-v5|Hao 2024]]).
- In [[30-Concepts/spatial-multiomics|spatial]] terms, ISON is **diagonal integration with a physical anchor**: different modalities and different cells, bridged by a shared latent space and constrained by spatial adjacency ([[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]; [[10-Summaries/debnath-2026-ison|ISON]]). (synthesis)

## Evidence and examples

**Factor models**

- In simulations, GFA and iCluster tended to infer redundant factors and recovered shared-factor activity less accurately than MOFA; on the 200-patient CLL data MOFA trained in 25 min versus 34 h for GFA and 5–6 days for iCluster ([[10-Summaries/argelaguet-2018-mofa|MOFA]]).
- On scM&T-seq data, MOFA's continuous factors recovered a naive → primed → differentiated trajectory that the clustering methods SNF and iCluster could not, as they only separated subpopulations ([[10-Summaries/argelaguet-2018-mofa|MOFA]]).
- MOFA on matched RNA, H3K4me1 and H3K27me3 from OneCell CUT&Tag separated a multiomic basal factor from an epigenome-only factor: an H3K4me1 signature in a basal subset, enriched for Zfx, Trp63 and Tcfap2c motifs and undetectable at the RNA level ([[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]).

**Anchor methods**

- WNN was tested on RNA+ATAC (11,351 10x Multiome PBMCs), where it beat either modality alone ([[10-Summaries/hao-2021-seurat-wnn|Hao 2021]]).
- About 50 bridge cells per cell type suffice for bridge integration, and prediction confidence drops sharply (0.907 → 0.514) when a cell type is missing from the bridge ([[10-Summaries/hao-2024-seurat-v5|Hao 2024]]).
- For scCUT&Tag, WNN integration with matched scRNA-seq is the dominant route to cell-type annotation (sn-m6A-CT, NTT-seq, nano-CT, scCUT&Tag-pro), and ChromHMM/scChromHMM are described as the only promising approaches for combining multiple marks within one dataset ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).

**Spatial inference**

- In ISON, the linear KL-NMF model consistently beat a contrastive joint VAE on both datasets and both metrics (peak-wise PCC 0.23 vs 0.09, and 0.15 vs 0.07) ([[10-Summaries/debnath-2026-ison|ISON]]).
- ISON also outperformed MOFA, CCA+KNN, Tangram, RCTD, SPAGE and GIMVI at predicting spatial chromatin accessibility from spatial transcriptomics plus sc-multiome ([[10-Summaries/debnath-2026-ison|ISON]]).
- Joint expression + accessibility modelling can **distinguish TFs within the same family**, which motif-based accessibility methods structurally cannot do because paralogues share motifs ([[10-Summaries/debnath-2026-ison|ISON]]).

**Foundation models**

- SCARF reported the lowest FOSCTTM on 10x PBMC against GLUE, Seurat, Harmony, LIGER, uniPort and scVI ([[10-Summaries/liu-2025-scarf|SCARF]]).
- After fine-tuning on 3,233 human brain multiome cells, scMomer's RNA→ATAC translation gave pseudo-bulk accessibility PCC 0.981, against 0.333 for scButterfly ([[10-Summaries/liu-2025-scmomer|scMomer]]).
- CLM-X reached an overall fusion score of 0.730 on seven multiome datasets under the Hu et al. 2024 benchmark protocol, narrowly ahead of MultiVI (ARI 0.658 vs 0.622) ([[10-Summaries/li-2026-clm-x|CLM-X]]).

## Contested points

- **Named failure modes**: overcorrection (merging non-matching subpopulations when no shared biological axis exists); latent-space integration distorting the high-dimensional observations so marker detection becomes problematic; and biological variability that tracks batch being inseparable from it ([[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]).
- **Sequence context is a systematic confounder** in epigenomic association: GC content raises apparent accessibility and lowers apparent methylation, so nulls should be built from features with matched sequence context, as chromVAR does ([[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]).
- **Feature-count imbalance** lets the modality with more features dominate a joint latent space, the problem WNN reweighting exists to solve ([[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]).
- **Diagonal integration usually rests on the gene-activity assumption**, which is known to fail in early development, where gene-body methylation and accessibility do not predict expression ([[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]).
- **Measurement linkage** (e.g., copy number raising expression) is flagged as unaddressed for same-cell modalities ([[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]).
- **WNN may obscure native chromatin variation** when used to annotate scCUT&Tag ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).
- **Linear models can beat deep generative ones.** ISON's KL-NMF result is a counterexample to the deep-generative default; its spatial prior and batch vectors are structure a VAE would have to learn from data (synthesis).
- **WNN on sparse pairs.** How per-cell weighting behaves on still sparser pairs such as RNA+methylation is untested (synthesis).
- **Correcting expression versus correcting embeddings** is an unresolved trade: MNN returns corrected expression values usable for differential testing, while Harmony corrects only the embedding ([[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]; [[10-Summaries/korsunsky-2019-harmony|Harmony]]). Neither the risk nor the benefit has been quantified (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/joint-single-cell-multi-omics|Joint single-cell multi-omics]] — Measuring two or more modalities in the same cell, rather than integrating them computationally.
> - `concept` [[30-Concepts/reference-atlas-mapping|Reference atlas mapping]] — Placing query cells into a frozen annotated reference and transferring labels or modalities.
> - `concept` [[30-Concepts/spatial-multiomics|Spatial multi-omics]] — Multi-omics readouts that keep each cell's position in intact tissue.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Methods that measure several molecular modalities in the same single cell.

## All sources on this page

> [!info]- 26 summaries cited here
> - [[10-Summaries/argelaguet-2018-mofa|Argelaguet 2018]]
> - [[10-Summaries/argelaguet-2020-mofa-plus|Argelaguet 2020]]
> - [[10-Summaries/argelaguet-2021-integration-principles|Argelaguet 2021]]
> - [[10-Summaries/ashuach-2023-multivi|Ashuach 2023]]
> - [[10-Summaries/bi-2024-multiomics-review|Bi & Weng 2024]]
> - [[10-Summaries/butler-2018-seurat-cca|Butler 2018]]
> - [[10-Summaries/cao-2022-glue|Cao 2022]]
> - [[10-Summaries/debnath-2026-ison|Debnath 2026]]
> - [[10-Summaries/gayoso-2021-totalvi|Gayoso 2021]]
> - [[10-Summaries/gong-2021-cobolt|Gong 2021]]
> - [[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]
> - [[10-Summaries/hao-2021-seurat-wnn|Hao 2021]]
> - [[10-Summaries/hao-2024-seurat-v5|Hao 2024]]
> - [[10-Summaries/korsunsky-2019-harmony|Korsunsky 2019]]
> - [[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]
> - [[10-Summaries/lake-2018-brain-snrna-scths|Lake 2018]]
> - [[10-Summaries/lakkis-2022-scipenn|Lakkis 2022]]
> - [[10-Summaries/li-2026-clm-x|CLM-X 2026]]
> - [[10-Summaries/liu-2025-scarf|SCARF 2025]]
> - [[10-Summaries/liu-2025-scmomer|scMomer 2025]]
> - [[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]
> - [[10-Summaries/song-2021-scgcn|Song 2021]]
> - [[10-Summaries/stuart-2021-natmethods|Stuart 2021]]
> - [[10-Summaries/wang-2023-multimodal-review|Wang 2023]]
> - [[10-Summaries/welch-2019-liger|Welch 2019]]
> - [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]
