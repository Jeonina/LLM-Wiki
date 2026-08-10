---
type: concept
title: Batch Effect
aliases: [batch correction, dataset integration, technical variation]
tags: [integration, batch, LISI, Harmony, meta-analysis]
created: 2026-08-10
updated: 2026-08-10
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

## Related

- [[multimodal-integration-methods]] · [[dimensionality-reduction]] · [[cell-type-annotation]] · [[computational-methods]]
