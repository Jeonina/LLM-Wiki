---
type: concept
title: Batch Effect
aliases: [batch correction, dataset integration, technical variation]
tags: [integration, batch, LISI, Harmony, meta-analysis]
created: 2026-08-10
updated: 2026-10-08
---

# Batch Effect

> Systematic variation attributable to when, where, by whom or on what platform data were generated. In single-cell work biological and technical differences are interspersed, so joint analysis across studies requires explicit correction ([[korsunsky-2019-harmony]]).

## Correction strategies

- **Correct the shared embedding.** Soft-cluster cells with an information-theoretic penalty on clusters dominated by one dataset, compute per-cluster linear corrections from each dataset's centroid, and give every cell a cluster-weighted correction — so corrections are cell-type-specific, because a protocol rarely affects all cell types equally ([[korsunsky-2019-harmony]]).
- **Factorize into shared and dataset-specific factors**, keeping both halves so differences remain legible rather than removed ([[welch-2019-liger]]).
- **Anchor and bridge transfer** across modalities ([[hao-2024-seurat-v5]]); see [[multimodal-integration-methods]].
- **Explicit removal mechanisms inside a model**, e.g. when one batch has lower sequencing depth ([[zhang-2022-higashi]]).

## Measuring success

LISI computes the local inverse Simpson's index in each cell's neighbourhood twice — **iLISI** on dataset labels (higher = better mixing) and **cLISI** on cell-type labels (should stay at 1) — formalizing the trade that perfect mixing is achievable by merging everything and perfect accuracy by not integrating at all ([[korsunsky-2019-harmony]]). LISI degrades when datasets differ greatly in size, since most neighbourhoods are then dominated by one dataset ([[korsunsky-2019-harmony]]).

## Multiple covariates

Real designs confound technology *and* donor *and* tissue. Correcting jointly over 36 donors and five platforms reached technology iLISI 2.17 and donor iLISI 5.05 at >98% cell-type accuracy, where single-variable methods could not ([[korsunsky-2019-harmony]]).

## When the "batch effect" is the finding

Donor is a nuisance variable in meta-analysis and the object of study in others — inter-individual differences in brain nuclei were the reported result, using the same class of machinery ([[welch-2019-liger]]).

## The related confound in single-cell Hi-C

Coverage heterogeneity is the leading factor driving clustering results, ahead of biology, and is not removable by simply dropping the first principal component ([[zhou-2019-schicluster]]).

## Added 2026-10-07

**Implicit batch mitigation by sequence.** CellSpace mixes donors without a batch covariate by updating cell embeddings from k-mer content rather than peak identity; on HSPC data it beat ArchR itLSI on batch score (tie on biological score), though batch-corrected PeakVI beat it overall on a large haematopoietic dataset ([[10-Summaries/tayyebi-2024-cellspace]]). FFPE versus fresh scATAC data also show a residual batch effect even when cell-type signals agree ([[10-Summaries/yadav-2025-scffpe-atac]]).

For band-normalized scHi-C (Lee2019, 5 libraries), Harmony removed batch effects and slightly sharpened neuronal sub-type separation. SVA worsened results, dropping the batch-correlated PC did not remove the bias, and Seurat regression introduced new biases in other clusters ([[10-Summaries/zheng-2022-bandnorm-scvi-3d]]).

An optional extension of scCASE corrects protocol batch effects in scATAC data. On a mouse-brain dataset mixing 10X and snATAC, it improved kBET and batch ASW and merged L2/3 IT cells from both batches into one cluster ([[10-Summaries/tang-2024-sccase]]).

On Buenrostro 2018, GFETM without any batch term had the highest ARI and second-highest kBET, and adding a linear batch term gave the best kBET at slightly lower ARI ([[10-Summaries/fan-2026-gfetm]]). GFETM attributes its scalability on large scATAC datasets to batch-agnostic embeddings, and notes that cross-tissue and cross-species scATAC integration is hard because, unlike genes in scRNA-seq, scATAC lacks a common feature set ([[10-Summaries/fan-2026-gfetm]]). Representing peaks by sequence embeddings rather than coordinates is a plausible way around that (synthesis).

## Added 2026-10-08 — sequence models & foundation models

- Embeddings from fine-tuned EpiFoundation had the best NMI, cASW, bASW and graph connectivity against PCA, Harmony, LIGER and scANVI on kidney, BMMC and PBMC, but not the best isolated-label score in kidney or PBMC ([[10-Summaries/wu-2025-epifoundation]]).
- Fine-tuned CLM-X improved the NMI/bASW overall batch-correction score by 5.9–35.0% over MultiVI, Multigrate, MIRA and scMoMaT across 2-, 4- and 13-batch multiome benchmarks ([[10-Summaries/li-2026-clm-x]])

## Related

- [[multimodal-integration-methods]] · [[dimensionality-reduction]] · [[cell-type-annotation]] · [[computational-methods]]

## Added 2026-08-17

Founding single-cell treatment ingested 2026-08-14: [[10-Summaries/haghverdi-2018-mnn]].

**The composition-invariance assumption is the flaw.** limma's `removeBatchEffect` and ComBat fit a linear model with a batch blocking term and zero its coefficient; RUVseq and svaseq identify unknown factors and regress them out. All assume population composition is identical across batches — true enough for bulk, false for single cell, because dissociation, culture, and sorting all shift cell-type abundance. When composition differs, "the estimated coefficients for the batch blocking factors are not purely technical but contain a nonzero biological component", and correction "might potentially be worse than if no correction were performed" ([[10-Summaries/haghverdi-2018-mnn]]).

**MNN's weaker assumption**: only a *subset* of the population need be shared. Cells that are mutually nearest neighbours across batches are taken to be the same type; their expression difference estimates the batch effect, averaged over many pairs ([[10-Summaries/haghverdi-2018-mnn]]). Overlap is discovered rather than assumed, so batch-specific cell types do not distort the estimate.

**Landmark projection fails on novel types** — cells outside the reference's transcriptional space get projected somewhere arbitrary ([[10-Summaries/haghverdi-2018-mnn]]), the same limitation that [[reference-atlas-mapping|reference mapping]] inherits by design.

The MNN pair is the **ancestor of the "anchor"**: Seurat v3 generalised it, and [[10-Summaries/hao-2024-seurat-v5|bridge integration]] and [[10-Summaries/kang-2021-symphony|Symphony]] are both descendants of the same intuition — find provably corresponding cells, then use their difference as the correction. (synthesis)

Batch effects are structural rather than accidental at atlas scale: large projects must generate data at different times, by different operators, with different dissociation protocols, chemistries and sequencers ([[10-Summaries/haghverdi-2018-mnn]]).
