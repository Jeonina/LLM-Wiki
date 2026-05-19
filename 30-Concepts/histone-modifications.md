---
type: concept
title: Histone modifications
aliases: [histone marks, PTMs, chromatin marks]
tags: [chromatin, epigenetics, enhancers, promoters]
created: 2026-05-12
updated: 2026-05-19
---

# Histone modifications

> Post-translational modifications of histone tails — methylation, acetylation, ubiquitylation, phosphorylation — that demarcate functional chromatin states ([[10-Summaries/sandy-2019-naturereviewsgenetics]]).

## Definition

Modifications occur predominantly on histone H3 and H4 lysines and arginines ([[10-Summaries/sandy-2019-naturereviewsgenetics]]). Canonical mark-state mapping:

- **H3K4me3**: active promoters ([[10-Summaries/sandy-2019-naturereviewsgenetics]])
- **H3K4me1**: enhancers — alone = primed; + H3K27ac = active; + H3K27me3 = poised ([[10-Summaries/sandy-2019-naturereviewsgenetics]])
- **H3K27ac**: active promoters and enhancers ([[10-Summaries/sandy-2019-naturereviewsgenetics]])
- **H3K36me3**: actively transcribed gene bodies ([[10-Summaries/sandy-2019-naturereviewsgenetics]])
- **H3K27me3**: facultative heterochromatin (Polycomb-repressed) ([[10-Summaries/sandy-2019-naturereviewsgenetics]]; LAD borders per [[10-Summaries/van-steensel-2017-lads-review]])
- **H3K9me3**: constitutive heterochromatin ([[10-Summaries/sandy-2019-naturereviewsgenetics]]; cLAD anchoring mark per [[10-Summaries/van-steensel-2017-lads-review]])

## Why it matters

Histone marks are the substrate for cell-type-specific gene regulation ([[10-Summaries/sandy-2019-naturereviewsgenetics]]). Profile them and you know which regions are active, primed, repressed, or silenced. Single-cell methods extend this to individual cells: scChIC-seq, scCUT&Tag ([[10-Summaries/bartosovic-2021-sccut-tag]]), sciCUT&Tag ([[10-Summaries/janssens-2023-scicut-tag]]), nano-CUT&Tag ([[10-Summaries/bartosovic-2022-nano-cut-tag]]), scChIX-seq ([[10-Summaries/yeung-2023-scchix-seq]]), and scEpi²-seq ([[10-Summaries/geisenberger-2025-scepi2-seq]]).

## Redundancy with chromatin compartments

Histone marks are not independent of other regulatory axes:
- **H3K9me2/3 anchors LADs to the nuclear lamina** via G9a, SUV39H1/2 acting redundantly ([[10-Summaries/van-steensel-2017-lads-review]]).
- **H3K27me3 enriched at LAD boundaries** in some cell types ([[10-Summaries/van-steensel-2017-lads-review]]).
- **H3K27ac and active marks** co-localize with accessible chromatin and compartment A regions ([[10-Summaries/sandy-2019-naturereviewsgenetics]]; [[10-Summaries/klemm-2019-chromatin-accessibility-review]]).
- **DNA methylation is partially redundant with H3K9me3** at heterochromatic regions but not at LADs, where CpG methylation is *not* enriched ([[10-Summaries/van-steensel-2017-lads-review]]).

## Examples

- LLPS-competent IDR fusions (NUP98-HOXA9) induce H3K27ac at off-target proto-oncogenes ([[10-Summaries/ahn-2021-llps-cancer-looping]]).
- Polycomb (H3K27me3) occupancy decoupled from gene expression in mouse embryoid bodies (EpiDamID, [[10-Summaries/rooijers-2019-scdamt-seq]]).
- scCUT&Tag profiles H3K4me3/H3K27me3 transitions during oligodendrocyte differentiation in mouse brain ([[10-Summaries/bartosovic-2021-sccut-tag]]).

## Related

- [[30-Concepts/chip-seq]] · [[30-Concepts/cut-and-tag]] · [[30-Concepts/cut-and-run]] · [[30-Concepts/cut-and-run]]
- [[30-Concepts/chic-seq]] · [[30-Concepts/scchix-seq]] · [[30-Concepts/scicut-tag]] · [[30-Concepts/multi-tag]]
- [[40-Topics/histone-modifications]] · [[40-Topics/chromatin-architecture]]
- [[50-Notes/regulatory-layers-overview]] — histone marks as one of the four molecular regulatory layers
