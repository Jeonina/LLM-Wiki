---
type: concept
title: Multimodal integration methods
aliases: [multi-omics integration, multimodal integration, cross-modality integration]
tags: [computational, integration, multiomics, machine-learning]
created: 2026-05-19
updated: 2026-10-08
paper_section: ["4.3"]
---

# Multimodal integration methods

> Computational methods for combining multiple single-cell omics modalities — paired (measured on the same cells) or unpaired (separate cell populations) — into a unified low-dimensional representation. Three method families ([[10-Summaries/wang-2023-multimodal-review]]): matrix factorization, manifold alignment, and deep generative models. Three integration *topologies* per the Argelaguet taxonomy ([[10-Summaries/bi-2024-multiomics-review]]): horizontal (same modality, different cells, anchored on genomic features), vertical (different modalities, same cell, anchored on the cell), and diagonal (different modalities, different cells, no anchor).

## Method families

- **Matrix factorization** — MOFA / MOFA+ ([[10-Summaries/argelaguet-2020-mofa-plus]]), LIGER. Extract latent factors per modality; struggle at high dimensionality.
- **Manifold alignment / anchoring** — CCA, MNN, WNN (all in Seurat per [[10-Summaries/stuart-2021-natmethods]]), Tangram, Cell2location.
- **Deep generative models** — totalVI, sciPENN, scMVP, MultiVI ([[10-Summaries/ashuach-2023-multivi]]), Cobolt ([[10-Summaries/gong-2021-cobolt]]), scJoint, GLUE ([[10-Summaries/cao-2022-glue]]), Symphony.

## Paired vs unpaired (= vertical vs horizontal/diagonal)

- **Paired / vertical**: cells measured by both modalities; problem is *alignment* of within-cell features ([[10-Summaries/bi-2024-multiomics-review]]).
- **Unpaired / horizontal**: same modality across cell populations, anchored on shared genomic features ([[10-Summaries/bi-2024-multiomics-review]]; [[10-Summaries/wang-2023-multimodal-review]]).
- **Unpaired / diagonal**: different modalities and different cells, no anchor — the hardest case because batch correction risks erasing biology ([[10-Summaries/bi-2024-multiomics-review]]).

## The anchor taxonomy

- **The anchor determines the assumptions.** *Horizontal* integration anchors on features (batch correction); *vertical* on cells (matched multimodal); *diagonal* when no anchor exists in high-dimensional space; *mosaic* when different modalities are measured on different cells from the same sample, leaving entire matrices missing ([[10-Summaries/argelaguet-2021-integration-principles]]).
- **Named failure modes**: overcorrection (merging non-matching subpopulations when no shared biological axis exists); latent-space integration distorting the high-dimensional observations so marker detection becomes problematic; and biological variability that tracks batch being inseparable from it ([[10-Summaries/argelaguet-2021-integration-principles]]).
- **Sequence context is a systematic confounder** in epigenomic association: GC content raises apparent accessibility and lowers apparent methylation, so nulls should be built from features with matched sequence context, as chromVAR does ([[10-Summaries/argelaguet-2021-integration-principles]]).
- **Feature-count imbalance** lets the modality with more features dominate a joint latent space — the problem WNN reweighting exists to solve ([[10-Summaries/argelaguet-2021-integration-principles]]).
- **Diagonal integration usually rests on the gene-activity assumption**, which is known to fail in early development where gene-body methylation and accessibility do not predict expression ([[10-Summaries/argelaguet-2021-integration-principles]]).
- **Bridge integration removes that assumption** by treating each cell of a multiomic dataset as a dictionary atom, learning the cross-modality relationship instead of assuming it; ~50 bridge cells per cell type suffice, and prediction confidence drops sharply (0.907 → 0.514) when a cell type is missing from the bridge ([[10-Summaries/hao-2024-seurat-v5]]).

## Added 2026-10-07

A six-setup taxonomy of single-cell integration distinguishes one sample (1S), across samples (+S), across experiments (+X+S), multiple modalities in the same cell (+M1C), different modalities in different cells (+M+C) and a full reference (+all) ([[10-Summaries/lahnemann-2020-grand-challenges]]). It flags "measurement linkage" — e.g., copy number raising expression — as unaddressed for same-cell modalities ([[10-Summaries/lahnemann-2020-grand-challenges]]).

The factor-analysis branch originates with MOFA (Molecular Systems Biology 2018), a Bayesian group factor analysis model that decomposes each modality as Yᵐ = ZWᵐᵀ + εᵐ with shared factors Z and sparse per-modality weights, and reports the variance each factor explains in each modality so shared and modality-specific axes can be told apart ([[10-Summaries/argelaguet-2018-mofa]]); MOFA+ is its scalable successor ([[10-Summaries/argelaguet-2020-mofa-plus]]).

MOFA on matched RNA, H3K4me1 and H3K27me3 from OneCell CUT&Tag separated a multiomic basal factor from an epigenome-only factor. The epigenome-only factor is an H3K4me1 signature in a basal subset, enriched for Zfx, Trp63 and Tcfap2c motifs and undetectable at the RNA level ([[10-Summaries/schwager-2026-onecell-cut-tag]]).

For scCUT&Tag, WNN integration with matched scRNA-seq is the dominant route to cell-type annotation (sn-m6A-CT, NTT-seq, nano-CT, scCUT&Tag-pro), but it may obscure native chromatin variation, and ChromHMM/scChromHMM are described as the only promising approaches for combining multiple marks within one dataset ([[10-Summaries/wu-2026-sccut-tag-review]]).

MOFA's own benchmarks set it against earlier multi-omics latent-variable models: in simulations GFA and iCluster tended to infer redundant factors and recovered shared-factor activity less accurately, and on the 200-patient CLL data MOFA trained in 25 min versus 34 h for GFA and 5–6 days for iCluster ([[10-Summaries/argelaguet-2018-mofa]]). On scM&T-seq data, MOFA's continuous factors recovered a naive → primed → differentiated trajectory that the clustering methods SNF and iCluster could not, as they only separated subpopulations ([[10-Summaries/argelaguet-2018-mofa]]).

## Added 2026-10-08 — sequence models & foundation models

- Foundation-model approaches now compete on RNA–ATAC integration: SCARF, pretrained on 2.7 M paired 10x Multiome cells with a contrastive alignment loss, reported the lowest FOSCTTM on 10x PBMC against GLUE, Seurat, Harmony, LIGER, uniPort and scVI ([[10-Summaries/liu-2025-scarf]])
- After fine-tuning on 3,233 human brain multiome cells, scMomer's RNA→ATAC translation gave pseudo-bulk accessibility PCC 0.981, against 0.333 for scButterfly ([[10-Summaries/liu-2025-scmomer]])
- CLM-X, a multiway-Transformer foundation model, reached an overall fusion score of 0.730 on seven multiome datasets under the Hu et al. 2024 benchmark protocol, narrowly ahead of MultiVI (ARI 0.658 vs 0.622) ([[10-Summaries/li-2026-clm-x]])

## Related

- [[40-Topics/single-cell-multiomics]] · [[30-Concepts/joint-single-cell-multi-omics]]
- [[10-Summaries/argelaguet-2021-integration-principles]] · [[10-Summaries/hao-2024-seurat-v5]] · [[10-Summaries/lake-2018-brain-snrna-scths]]

## Added 2026-08-13

A useful counterexample to the deep-generative default: in ISON, the **linear KL-NMF model consistently beat a contrastive joint VAE** on both datasets and both metrics (peak-wise PCC 0.23 vs 0.09, and 0.15 vs 0.07) ([[10-Summaries/debnath-2026-ison]]). The NMF variant carries a Laplacian spatial-smoothness prior and modality-specific batch-correction vectors — structure a VAE would have to learn from data. (synthesis)

ISON also outperformed MOFA, CCA+KNN, Tangram, RCTD, SPAGE and GIMVI at predicting spatial chromatin accessibility from spatial transcriptomics plus sc-multiome ([[10-Summaries/debnath-2026-ison]]).

In [[30-Concepts/spatial-multiomics|spatial]] terms this is **diagonal integration with a physical anchor** — different modalities, different cells, bridged by a shared latent space and constrained by spatial adjacency ([[10-Summaries/argelaguet-2021-integration-principles]]; [[10-Summaries/debnath-2026-ison]]). (synthesis)

One capability is specific to joint expression + accessibility modelling: **distinguishing TFs within the same family**, which motif-based accessibility methods structurally cannot do because paralogues share motifs ([[10-Summaries/debnath-2026-ison]]).

## Added 2026-08-17

The modern integration literature has a birthday: **2 April 2018**, when [[10-Summaries/haghverdi-2018-mnn|MNN correction]] and [[10-Summaries/butler-2018-seurat-cca|Seurat CCA alignment]] appeared in the same issue of *Nature Biotechnology*, solving the same problem from opposite directions — MNN corrects in high-dimensional expression space via mutually-nearest cross-batch cells; Seurat aligns in a shared low-dimensional CCA space. The field's two dominant strategies were born the same day. (synthesis)

**What single-cell integration must do that bulk batch correction cannot** ([[10-Summaries/butler-2018-seurat-cca]]): align subpopulations even when **each has a unique response**; tolerate **shifts in subpopulation frequency**; be robust to feature-scale changes; and require no pre-established markers. Bulk methods (limma, ComBat, RUVseq, svaseq) assume confounders act uniformly on all cells and that **population composition is identical across batches** — false in practice, and when it fails the batch coefficient absorbs real biology so that "the results might potentially be worse than if no correction were performed" ([[10-Summaries/haghverdi-2018-mnn]]).

**Method families now represented in the corpus:**

| Family | Methods |
|---|---|
| Anchor / nearest-neighbour | [[10-Summaries/haghverdi-2018-mnn]], [[10-Summaries/butler-2018-seurat-cca]], [[10-Summaries/hao-2021-seurat-wnn]], [[10-Summaries/hao-2024-seurat-v5]] |
| Embedding-space iterative | [[10-Summaries/korsunsky-2019-harmony]] |
| Matrix factorisation | [[10-Summaries/welch-2019-liger]], [[10-Summaries/argelaguet-2020-mofa-plus]], [[10-Summaries/debnath-2026-ison]] |
| Deep generative | [[10-Summaries/gayoso-2021-totalvi]], [[10-Summaries/ashuach-2023-multivi]], [[10-Summaries/cao-2022-glue]], [[10-Summaries/lakkis-2022-scipenn]] |
| Graph neural network | [[10-Summaries/song-2021-scgcn]] |

**Per-cell modality weighting** is the honest answer to a question most methods dodge — concatenation implicitly weights by feature count and choosing a "primary" modality biases the analysis, whereas WNN *learns the relative utility of each data type in each cell* ([[10-Summaries/hao-2021-seurat-wnn]]). It was also tested on RNA+ATAC (11,351 10x Multiome PBMCs), where WNN beat either modality alone ([[10-Summaries/hao-2021-seurat-wnn]]); how it behaves on still sparser pairs such as RNA+methylation is untested. (synthesis)

**Correcting expression versus correcting embeddings** is an unresolved trade: MNN returns corrected expression values usable for differential testing; Harmony corrects only the embedding and leaves expression untouched. Neither the risk nor the benefit has been quantified. (synthesis)

See [[reference-atlas-mapping]] for the asymmetric case, where the reference is frozen.
