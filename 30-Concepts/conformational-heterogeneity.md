---
type: concept
title: Conformational Heterogeneity (C.H.)
aliases: [structural heterogeneity, cell-to-cell 3D variability, Relative C.H.]
tags: [3D-genome, scHi-C, polymer-model, metric, single-cell]
created: 2026-05-15
updated: 2026-10-12
---

# Conformational Heterogeneity (C.H.)

> A single-number, distribution-aware metric for **cell-to-cell variability of 3D chromatin folding**: the standard deviation across cells of each cell's average distance between loci at a given genomic separation ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).

> [!abstract] 한눈에
> C.H.는 세포마다 같은 genomic 거리의 locus 쌍 사이 평균 3D 거리를 구한 뒤 그 값의 세포 간 표준편차를 재는 지표로, 세포 안의 요동이 아니라 세포 사이의 folding 차이만 잡아낸다 ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]). 같은 bulk Hi-C map이 서로 다른 scHi-C 분포에서 나올 수 있다는 점을 드러내며, lamin을 줄이면 거의 모든 거리에서 C.H.가 오른다 ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [3D 유전체 교재](../60-Explainers/3d-genome.html)
<!-- /explainer-links -->

## Definition

Defined by Mali et al. 2025: for an ensemble of *n* single-cell chromatin conformations and a genomic separation *s*, compute the per-cell average Euclidean inter-loci distance ⟨R_s⟩^(i) (averaged over all locus pairs separated by *s* within cell *i*), then take the standard deviation across cells ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]):

**C.H.(s) = stdev_i ⟨R_s⟩^(i)**

By averaging *within* cells first and taking dispersion *across* cells, C.H. isolates inter-cell heterogeneity from intra-cell conformational dynamics; an ensemble of identical-but-internally-variable nuclei yields C.H. = 0 ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).

## Why it matters

**Bulk Hi-C is underdetermined**: the same bulk contact map can arise from very different scHi-C distributions, and C.H. discriminates these where bulk Hi-C cannot ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).

## Variants and computation

**Relative C.H.** is a dimensionless variant for cross-model comparison ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]):

**Relative C.H.(s) = C.H.(s) / mean_i ⟨R_s⟩^(i)**

This makes models in different length units (DPD arbitrary units vs microns) directly comparable ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).

**How it's computed** ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]):

1. Generate or load an ensemble of single-cell 3D models (or experimental 3D imaging data).
2. For each cell *i* and genomic separation *s*, compute ⟨R_s⟩^(i) by averaging Euclidean distances between all locus pairs separated by *s*.
3. C.H.(s) = stdev_i ⟨R_s⟩^(i).
4. For resolution matching, use the **MC-TAD algorithm** to up-convert lower-resolution models by Monte-Carlo sampling permissible chromatin paths through TAD-internal sub-bins.

**Complementary metrics.** Per-cell quality scores (e.g., [[30-Concepts/sscce|SSCE]] from the STARK pipeline) measure how good a single scHi-C map is, while C.H. measures dispersion *across* a population of maps (synthesis).

## Evidence and examples

- **Resolution matters**: C.H. is near-zero at the model's resolution limit, rises through ~100 kb (TAD size), and peaks or dips at 1–10 Mb depending on training data ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).
- **Bulk-Hi-C-trained vs scHi-C-trained models diverge at 1–10 Mb** in opposite directions — a signal of insufficient single-cell sample size in current scHi-C atlases ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).
- **Lamin depletion raises C.H.** at nearly all genomic separations, supporting a structural prediction of increased transcriptional noise in lamin-depleted nuclei ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).

## Open questions

- Higher moments of the ⟨R_s⟩ distribution (skewness, multi-modality) — C.H. captures only the second moment (synthesis).
- Time evolution within interphase: does C.H. itself change as cells cycle? (synthesis)
- Disease applications: laminopathies, cancer chromatin re-arrangements, viral infection (SARS-CoV-2 cited in Mali 2025) ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — The per-cell contact maps whose population spread C.H. summarises.
> - `concept` [[30-Concepts/topologically-associating-domain|Topologically associating domain]] — The ~100 kb scale where C.H. starts to rise; basis of MC-TAD up-conversion.
> - `concept` [[30-Concepts/lamina-associated-domains|Lamina-associated domains]] — Lamina-tethered regions; lamin depletion raises C.H.
> - `concept` [[30-Concepts/nuclear-lamina|Nuclear lamina]] — The structure whose depletion is the main perturbation tested.
> - `concept` [[30-Concepts/sscce|SSCE]] — Per-cell scHi-C quality score, complementary to population-level C.H.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]
