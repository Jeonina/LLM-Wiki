---
type: concept
title: Batch Effect
aliases: [batch correction, dataset integration, technical variation]
tags: [integration, batch, LISI, Harmony, meta-analysis]
created: 2026-08-10
updated: 2026-10-12
---

# Batch Effect

> Systematic variation attributable to when, where, by whom or on what platform data were generated. In single-cell work biological and technical differences are interspersed, so joint analysis across studies requires explicit correction ([[10-Summaries/korsunsky-2019-harmony|Harmony]]).

> [!abstract] 한눈에
> Batch effect는 데이터를 언제, 어디서, 어떤 플랫폼으로 만들었는지에서 생기는 체계적 변동이고, single-cell에서는 batch마다 세포 구성이 달라 bulk식 선형 보정이 생물학적 신호까지 지울 수 있다 ([[10-Summaries/korsunsky-2019-harmony|Harmony]]; [[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]). 그래서 MNN·Harmony·anchor 계열처럼 batch 사이에 대응하는 세포를 찾아 그 차이로 보정하는 방법이 표준이 되었다 ([[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]; [[10-Summaries/hao-2024-seurat-v5|Hao 2024]]).

## Definition

A batch effect is systematic variation attributable to when, where, by whom or on what platform data were generated ([[10-Summaries/korsunsky-2019-harmony|Harmony]]). At atlas scale it is structural rather than accidental: large projects must generate data at different times, by different operators, with different dissociation protocols, chemistries and sequencers ([[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]).

## Why it matters

- In single-cell work biological and technical differences are interspersed, so joint analysis across studies requires explicit correction ([[10-Summaries/korsunsky-2019-harmony|Harmony]]).
- Bulk-style correction assumes population composition is identical across batches — true enough for bulk, false for single cell, because dissociation, culture and sorting all shift cell-type abundance ([[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]).
- When composition differs, "the estimated coefficients for the batch blocking factors are not purely technical but contain a nonzero biological component", and correction "might potentially be worse than if no correction were performed" ([[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]).

## Correction strategies

| Strategy | Example | Mechanism and assumption | Source |
|---|---|---|---|
| Linear model with a batch blocking term | limma `removeBatchEffect`, ComBat | Fit a batch term and zero its coefficient; assumes identical composition across batches | ([[10-Summaries/haghverdi-2018-mnn\|Haghverdi 2018]]) |
| Regress out unknown factors | RUVseq, svaseq | Identify unknown factors and regress them out; same composition assumption | ([[10-Summaries/haghverdi-2018-mnn\|Haghverdi 2018]]) |
| Mutual nearest neighbours | [[10-Summaries/haghverdi-2018-mnn\|MNN]] | Only a *subset* of the population need be shared; cells that are mutually nearest neighbours across batches are taken to be the same type, and their expression difference, averaged over many pairs, estimates the batch effect. Overlap is discovered rather than assumed, so batch-specific cell types do not distort the estimate | ([[10-Summaries/haghverdi-2018-mnn\|Haghverdi 2018]]) |
| Correct the shared embedding | [[10-Summaries/korsunsky-2019-harmony\|Harmony]] | Soft-cluster cells with an information-theoretic penalty on clusters dominated by one dataset, compute per-cluster linear corrections from each dataset's centroid, and give every cell a cluster-weighted correction — cell-type-specific, because a protocol rarely affects all cell types equally | ([[10-Summaries/korsunsky-2019-harmony\|Harmony]]) |
| Shared and dataset-specific factors | [[10-Summaries/welch-2019-liger\|LIGER]] | Factorize and keep both halves, so differences remain legible rather than removed | ([[10-Summaries/welch-2019-liger\|LIGER]]) |
| Anchor and bridge transfer | [[10-Summaries/hao-2024-seurat-v5\|Seurat v5]], [[10-Summaries/kang-2021-symphony\|Symphony]] | Anchor and bridge transfer across modalities ([[10-Summaries/hao-2024-seurat-v5\|Hao 2024]]); see [[30-Concepts/multimodal-integration-methods\|multimodal integration methods]] | ([[10-Summaries/hao-2024-seurat-v5\|Hao 2024]]) |
| Explicit removal inside a model | [[10-Summaries/zhang-2022-higashi\|Higashi]] | A dedicated mechanism, e.g. when one batch has lower sequencing depth | ([[10-Summaries/zhang-2022-higashi\|Higashi]]) |
| Implicit mitigation by sequence | [[10-Summaries/tayyebi-2024-cellspace\|CellSpace]], [[10-Summaries/fan-2026-gfetm\|GFETM]] | CellSpace mixes donors without a batch covariate by updating cell embeddings from k-mer content rather than peak identity; GFETM attributes its scalability to batch-agnostic embeddings | ([[10-Summaries/tayyebi-2024-cellspace\|CellSpace]]; [[10-Summaries/fan-2026-gfetm\|GFETM]]) |
| Optional correction module | [[10-Summaries/tang-2024-sccase\|scCASE]] | An optional extension that corrects protocol batch effects in scATAC data | ([[10-Summaries/tang-2024-sccase\|scCASE]]) |

The MNN pair is the **ancestor of the "anchor"**: Seurat v3 generalised it, and [[10-Summaries/hao-2024-seurat-v5|bridge integration]] and [[10-Summaries/kang-2021-symphony|Symphony]] are both descendants of the same intuition — find provably corresponding cells, then use their difference as the correction (synthesis).

## Measuring success

- LISI computes the local inverse Simpson's index in each cell's neighbourhood twice — **iLISI** on dataset labels (higher = better mixing) and **cLISI** on cell-type labels (should stay at 1) ([[10-Summaries/korsunsky-2019-harmony|Harmony]]).
- This formalizes the trade that perfect mixing is achievable by merging everything and perfect accuracy by not integrating at all ([[10-Summaries/korsunsky-2019-harmony|Harmony]]).
- Benchmarks in this wiki also score kBET, batch ASW, ARI, NMI, cASW and graph connectivity ([[10-Summaries/tang-2024-sccase|scCASE]]; [[10-Summaries/fan-2026-gfetm|GFETM]]; [[10-Summaries/wu-2025-epifoundation|EpiFoundation]]).

## Evidence and examples

**Multiple covariates**

- Real designs confound technology *and* donor *and* tissue; correcting jointly over 36 donors and five platforms reached technology iLISI 2.17 and donor iLISI 5.05 at >98% cell-type accuracy, where single-variable methods could not ([[10-Summaries/korsunsky-2019-harmony|Harmony]]).

**Single-cell Hi-C**

- Coverage heterogeneity is the leading factor driving scHi-C clustering results, ahead of biology, and is not removable by simply dropping the first principal component ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).
- For band-normalized scHi-C (Lee2019, 5 libraries), Harmony removed batch effects and slightly sharpened neuronal sub-type separation; SVA worsened results, dropping the batch-correlated PC did not remove the bias, and Seurat regression introduced new biases in other clusters ([[10-Summaries/zheng-2022-bandnorm-scvi-3d|BandNorm]]).

**scATAC-seq**

- On HSPC data CellSpace beat ArchR itLSI on batch score (tie on biological score), though batch-corrected PeakVI beat it overall on a large haematopoietic dataset ([[10-Summaries/tayyebi-2024-cellspace|CellSpace]]).
- FFPE versus fresh scATAC data show a residual batch effect even when cell-type signals agree ([[10-Summaries/yadav-2025-scffpe-atac|scFFPE-ATAC]]).
- On a mouse-brain dataset mixing 10X and snATAC, scCASE's batch extension improved kBET and batch ASW and merged L2/3 IT cells from both batches into one cluster ([[10-Summaries/tang-2024-sccase|scCASE]]).
- On Buenrostro 2018, GFETM without any batch term had the highest ARI and second-highest kBET, and adding a linear batch term gave the best kBET at slightly lower ARI ([[10-Summaries/fan-2026-gfetm|GFETM]]).

**Foundation models**

- Embeddings from fine-tuned EpiFoundation had the best NMI, cASW, bASW and graph connectivity against PCA, Harmony, LIGER and scANVI on kidney, BMMC and PBMC, but not the best isolated-label score in kidney or PBMC ([[10-Summaries/wu-2025-epifoundation|EpiFoundation]]).
- Fine-tuned CLM-X improved the NMI/bASW overall batch-correction score by 5.9–35.0% over MultiVI, Multigrate, MIRA and scMoMaT across 2-, 4- and 13-batch multiome benchmarks ([[10-Summaries/li-2026-clm-x|CLM-X]]).

## Contested points

- **When the "batch effect" is the finding.** Donor is a nuisance variable in meta-analysis and the object of study in others — inter-individual differences in brain nuclei were the reported result, using the same class of machinery ([[10-Summaries/welch-2019-liger|LIGER]]).
- **LISI is size-sensitive.** LISI degrades when datasets differ greatly in size, since most neighbourhoods are then dominated by one dataset ([[10-Summaries/korsunsky-2019-harmony|Harmony]]).
- **Landmark projection fails on novel types.** Cells outside the reference's transcriptional space get projected somewhere arbitrary ([[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]) — the same limitation that [[30-Concepts/reference-atlas-mapping|reference mapping]] inherits by design.
- **scATAC has no common feature set.** GFETM notes that cross-tissue and cross-species scATAC integration is hard because, unlike genes in scRNA-seq, scATAC lacks a common feature set ([[10-Summaries/fan-2026-gfetm|GFETM]]). Representing peaks by sequence embeddings rather than coordinates is a plausible way around that (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/multimodal-integration-methods|Multimodal integration methods]] — Combining paired or unpaired single-cell modalities into one representation.
> - `concept` [[30-Concepts/reference-atlas-mapping|Reference atlas mapping]] — Placing query cells into an annotated reference and transferring labels.
> - `concept` [[30-Concepts/dimensionality-reduction|Dimensionality reduction]] — Projecting cells into a few coordinates; where most corrections operate.
> - `concept` [[30-Concepts/cell-type-annotation|Cell type annotation]] — Assigning biological identity to clusters, which batch correction must preserve.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — The tool layer: aligners, callers, imputers and integrators.

## All sources on this page

> [!info]- 14 summaries cited here
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
> - [[10-Summaries/haghverdi-2018-mnn|Haghverdi 2018]]
> - [[10-Summaries/hao-2024-seurat-v5|Hao 2024]]
> - [[10-Summaries/kang-2021-symphony|Kang 2021]]
> - [[10-Summaries/korsunsky-2019-harmony|Korsunsky 2019]]
> - [[10-Summaries/li-2026-clm-x|CLM-X 2026]]
> - [[10-Summaries/tang-2024-sccase|Tang 2024]]
> - [[10-Summaries/tayyebi-2024-cellspace|Tayyebi 2024]]
> - [[10-Summaries/welch-2019-liger|Welch 2019]]
> - [[10-Summaries/wu-2025-epifoundation|EpiFoundation 2025]]
> - [[10-Summaries/yadav-2025-scffpe-atac|Yadav 2025]]
> - [[10-Summaries/zhang-2022-higashi|Zhang 2022]]
> - [[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]
> - [[10-Summaries/zhou-2019-schicluster|Zhou 2019]]
