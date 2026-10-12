---
type: concept
title: Hi-C Normalization
aliases: [ICE, iterative correction, matrix balancing, valid pair filtering]
tags: [Hi-C, normalization, ICE, bias-correction, pipelines]
created: 2026-08-10
updated: 2026-10-12
---

# Hi-C Normalization

> Converting raw ligation-junction counts into a contact matrix in which differences reflect chromatin proximity rather than restriction-site density, GC content, mappability or library depth ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]; [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

> [!abstract] 한눈에
> Hi-C normalization은 raw ligation count를 restriction site 밀도, GC, mappability, depth 대신 실제 chromatin 근접성을 반영하는 contact matrix로 바꾸는 과정이다 ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]). Bulk에서는 ICE matrix balancing이 표준이지만, 매우 sparse한 single-cell에서는 BandNorm처럼 거리 band별로 depth를 맞추는 방식이 쓰인다 ([[10-Summaries/zheng-2022-bandnorm-scvi-3d|BandNorm]]).

## Definition

Normalization turns raw ligation-junction counts into contacts that can be compared across bins, cells and studies; it runs as a pipeline of alignment, filtering, binning, balancing and distance-expected correction ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]; [[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]).

## Why it matters

Each step sets what counts as a contact, so normalization choices carry through to every feature called downstream. Cross-study comparisons of Hi-C features inherit that variance (synthesis).

## The bulk pipeline

1. **Align**, with chimeric rescue or two-step mapping, because a proximity-ligation read is chimeric by construction ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]).
2. **Filter to valid interaction products**, discarding self-circles, dangling ends and religation artefacts ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]).
3. **Bin** at the target resolution, which suppresses count noise and increases effective coverage ([[10-Summaries/abdennur-2020-cooler|Cooler]]).
4. **Balance** — iterative correction (ICE) equalizes marginal coverage across bins. A compressed-sparse-row implementation normalizes a 20 kb human genome map in under 30 minutes with 5 GB RAM, and genome-wide 5 kb in under 2.5 hours with 24 GB ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]). Rao et al. used a matrix-balancing algorithm to correct coverage non-uniformity caused by restriction-site density and accessibility in their kilobase-resolution in situ Hi-C maps ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).
5. For feature calling, divide by **distance-expected** contact to expose the plaid compartment pattern ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]).

## Single-cell approaches

| Approach | Method | What it does | Source |
|---|---|---|---|
| Band normalization | BandNorm | Divides each diagonal band of a cell's contact matrix by that cell's band total, then multiplies by the across-cell mean band total; removes distance bias and depth while restoring a common contact-decay curve | ([[10-Summaries/zheng-2022-bandnorm-scvi-3d\|BandNorm]]) |
| Model-based | scVI-3D | Fits a zero-inflated negative binomial VAE to each chromosome × band matrix | ([[10-Summaries/zheng-2022-bandnorm-scvi-3d\|BandNorm]]) |
| Cis-only bias correction | scHiCNorm | Normalizes only cis contacts, using local-bias features and distribution fitting | ([[10-Summaries/dautle-2025-schic-review\|Dautle 2025]]) |
| Raw-contact change points | scDIAGRAM | Runs change-point detection on raw contacts and computes O/E only for graph partitioning, using a pseudo-bulk expected profile in the style of BandNorm | ([[10-Summaries/peng-2026-scdiagram\|scDIAGRAM]]) |
| Normalization inside imputation | Most other scHi-C tools | Fold normalization into their imputation step | ([[10-Summaries/dautle-2025-schic-review\|Dautle 2025]]) |

- In BandNorm, the add-back step is what separates it from plain band scaling (BandScale) in cell-type separation, and the authors read this as up-weighting short-range bands ([[10-Summaries/zheng-2022-bandnorm-scvi-3d|BandNorm]]).
- The review describes BandNorm as removing genomic-distance bias, normalizing for sequencing depth and applying a band-dependent contact-decay estimate ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]).

## Evidence and examples

**Resolution economics**

- Improving resolution *n*-fold requires *n*² more reads ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]).
- Sparse matrix representations beat parallel dense implementations below 40 kb bins; dense wins at 500 kb–1 Mb by a negligible margin ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]).
- At kilobase resolution with a billion contacts, under 0.03% of matrix elements are filled ([[10-Summaries/abdennur-2020-cooler|Cooler]]).

## Contested points

- **Filtering stringency is a free parameter.** HiC-Pro and hiclib on identical raw data produce normalized intra-chromosomal maps correlating at mean Spearman **0.83 (range 0.65–0.95)**, and inter-chromosomal coverage vectors at 0.75 (0.46–0.98), because their valid-pair definitions differ ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]). There is no ground truth for a "valid interaction" — only conventions ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]). Cross-study comparisons of Hi-C features inherit that variance (synthesis).
- **ICE in aneuploid genomes.** ICE assumes equal visibility for all bins after correction — an assumption strained in aneuploid genomes, and unexamined in the source pipeline literature ([[10-Summaries/servant-2015-hicpro|HiC-Pro]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — Chromosome conformation capture in individual cells.
> - `concept` [[30-Concepts/chromatin-compartments|Chromatin compartments]] — The A/B plaid pattern exposed by distance-expected normalization.
> - `concept` [[30-Concepts/data-standards|Data standards]] — File formats and conventions such as cooler.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromatin folding, from loops to compartments.

## All sources on this page

> [!info]- 7 summaries cited here
> - [[10-Summaries/abdennur-2020-cooler|Abdennur & Mirny 2020]]
> - [[10-Summaries/dautle-2025-schic-review|Dautle 2025]]
> - [[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]
> - [[10-Summaries/peng-2026-scdiagram|Peng 2026]]
> - [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]
> - [[10-Summaries/servant-2015-hicpro|Servant 2015]]
> - [[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]
