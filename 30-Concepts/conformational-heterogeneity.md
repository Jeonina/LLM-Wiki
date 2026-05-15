---
type: concept
title: Conformational Heterogeneity (C.H.)
aliases: [structural heterogeneity, cell-to-cell 3D variability, Relative C.H.]
tags: [3D-genome, scHi-C, polymer-model, metric, single-cell]
created: 2026-05-15
updated: 2026-05-15
---

# Conformational Heterogeneity (C.H.)

> A single-number, distribution-aware metric for **cell-to-cell variability of 3D chromatin folding**, defined by Mali et al. 2025. For an ensemble of *n* single-cell chromatin conformations and a genomic separation *s*, compute the per-cell average Euclidean inter-loci distance ⟨R_s⟩^(i) (averaged over all locus pairs separated by *s* within cell *i*), then take the standard deviation across cells:
>
> **C.H.(s) = stdev_i ⟨R_s⟩^(i)**
>
> By averaging *within* cells first and taking dispersion *across* cells, C.H. isolates inter-cell heterogeneity from intra-cell conformational dynamics. An ensemble of identical-but-internally-variable nuclei yields C.H. = 0.

## Relative C.H.

Dimensionless variant for cross-model comparison:

**Relative C.H.(s) = C.H.(s) / mean_i ⟨R_s⟩^(i)**

This makes models in different length units (DPD arbitrary units vs microns) directly comparable.

## What C.H. exposes

- **Bulk Hi-C is underdetermined**: the same bulk contact map can arise from very different scHi-C distributions. C.H. discriminates these where bulk Hi-C cannot.
- **Resolution matters**: C.H. is near-zero at the model's resolution limit; rises through ~100 kb (TAD size); peaks or dips at 1–10 Mb depending on training data.
- **Bulk-Hi-C-trained vs scHi-C-trained models diverge at 1–10 Mb** in opposite directions ([[10-Summaries/mali-2025-conformational-heterogeneity]]) — a signal of insufficient single-cell sample size in current scHi-C atlases.
- **Lamin depletion raises C.H.** at nearly all genomic separations, supporting a structural prediction of increased transcriptional noise in lamin-depleted nuclei.

## How it's computed

1. Generate or load ensemble of single-cell 3D models (or experimental 3D imaging data).
2. For each cell *i* and genomic separation *s*, compute ⟨R_s⟩^(i) by averaging Euclidean distances between all locus pairs separated by *s*.
3. C.H.(s) = stdev_i ⟨R_s⟩^(i).
4. For resolution matching, use **MC-TAD algorithm** to up-convert lower-resolution models by Monte-Carlo sampling permissible chromatin paths through TAD-internal sub-bins.

## Complementary metrics

- **Per-cell quality scores** (e.g., [[30-Concepts/sscce]] from STARK pipeline) measure how good a single scHi-C map is.
- **C.H.** measures dispersion *across* a population of maps.

## Open frontiers

- Higher moments of the ⟨R_s⟩ distribution (skewness, multi-modality) — C.H. captures only the second moment.
- Time evolution within interphase: does C.H. itself change as cells cycle?
- Disease applications: laminopathies, cancer chromatin re-arrangements, viral infection (SARS-CoV-2 cited in Mali 2025).

## Related

- [[30-Concepts/single-cell-hi-c]] · [[30-Concepts/topologically-associating-domain]] · [[30-Concepts/lamina-associated-domains]] · [[30-Concepts/nuclear-lamina]]
- Source: [[10-Summaries/mali-2025-conformational-heterogeneity]]
- Related quality metric: [[30-Concepts/sscce]]
