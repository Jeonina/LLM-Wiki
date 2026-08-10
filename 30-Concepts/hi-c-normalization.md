---
type: concept
title: Hi-C Normalization
aliases: [ICE, iterative correction, matrix balancing, valid pair filtering]
tags: [Hi-C, normalization, ICE, bias-correction, pipelines]
created: 2026-08-10
updated: 2026-08-10
---

# Hi-C Normalization

> Converting raw ligation-junction counts into a contact matrix in which differences reflect chromatin proximity rather than restriction-site density, GC content, mappability or library depth.

## The steps

1. **Align**, with chimeric rescue or two-step mapping, because a proximity-ligation read is chimeric by construction ([[servant-2015-hicpro]]).
2. **Filter to valid interaction products**, discarding self-circles, dangling ends and religation artefacts ([[servant-2015-hicpro]]).
3. **Bin** at the target resolution, which suppresses count noise and increases effective coverage ([[abdennur-2020-cooler]]).
4. **Balance** — iterative correction (ICE) equalizes marginal coverage across bins. A compressed-sparse-row implementation normalizes a 20 kb human genome map in under 30 minutes with 5 GB RAM, and genome-wide 5 kb in under 2.5 hours with 24 GB ([[servant-2015-hicpro]]).
5. For feature calling, divide by **distance-expected** contact to expose the plaid compartment pattern ([[lieberman-aiden-2009-hic]]).

## Filtering stringency is a free parameter

HiC-Pro and hiclib on identical raw data produce normalized intra-chromosomal maps correlating at mean Spearman **0.83 (range 0.65–0.95)**, and inter-chromosomal coverage vectors at 0.75 (0.46–0.98), because their valid-pair definitions differ ([[servant-2015-hicpro]]). There is no ground truth for a "valid interaction" — only conventions ([[servant-2015-hicpro]]). Cross-study comparisons of Hi-C features inherit that variance (synthesis).

## Resolution economics

Improving resolution *n*-fold requires *n*² more reads ([[lieberman-aiden-2009-hic]]). Sparse matrix representations beat parallel dense implementations below 40 kb bins; dense wins at 500 kb–1 Mb by a negligible margin ([[servant-2015-hicpro]]). At kilobase resolution with a billion contacts, under 0.03% of matrix elements are filled ([[abdennur-2020-cooler]]).

## Open question

ICE assumes equal visibility for all bins after correction — an assumption strained in aneuploid genomes, and unexamined in the source pipeline literature ([[servant-2015-hicpro]]).

## Related

- [[single-cell-hi-c]] · [[chromatin-compartments]] · [[data-standards]] · [[3d-genome]]
