---
type: concept
title: Single-cell phylogenetic inference
aliases: [phylogenetic reconstruction, cell phylogeny, lineage tree inference]
tags: [lineage-tracing, phylogenetics, computational, fate-mapping]
created: 2026-06-02
updated: 2026-06-02
---

# Single-cell phylogenetic inference

> The computational reconstruction of a cell-division tree from heritable markers — synthetic CRISPR edits or natural somatic variants — including the ancestral relationships and, ideally, branch lengths ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).

## Definition

Given a character matrix (e.g. CRISPR indels) or variant calls per cell, phylogenetic inference searches for the tree topology that best explains the data under a distance-based or character-based (parsimony/likelihood) criterion ([[10-Summaries/wang-2026-multimodal-lineage-computational]]). The problem is NP-hard and the number of topologies grows super-exponentially with cell number, so exact search is infeasible at scale ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).

## Why it matters

- Clonal grouping identifies shared ancestry; a resolved *tree* additionally exposes continuous temporal dynamics and ancestral dependencies needed for fate mapping ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).
- Errors in the inferred tree propagate into every downstream analysis (state-transition rates, ancestral states, velocity) ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).

## Variants and refinements

- **Natural somatic variants**: SNV-based (SCIΦ, SIEVE, CellPhy, ScisTree), CNV-based (SCICoNE, MEDICC2), joint SNV+CNV (SCARLET, COMPASS), methylation-based (MethylTree) ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).
- **Classic algorithms**: distance methods (neighbour-joining, UPGMA) and character methods (maximum parsimony, maximum likelihood) — foundational but strained by missing data and tens of thousands of cells ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).
- **CRISPR-aware**: Cassiopeia (parsimony via greedy/ILP, edit irreversibility + dropout), STARTLE (star-homoplasy, each site mutates once), FRACTAL (divide-and-conquer to millions of cells); time-scaled trees via LAML, ConvexML, TiDeTree ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).
- **Expression-aided / expression-only**: LinTIMaT and LinRace integrate transcriptomes; GEMLI and CellTreeQM infer lineage from expression alone — with the caveat that transcriptional convergence is not ancestry ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).

## Contested points

- Synthetic barcodes have heterogeneous mutation rates and hotspots that distort trees ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).
- Without ground truth, branch support relies on bootstrap/approximately-unbiased tests and Robinson–Foulds congruence; phylogenetic artifacts (long-branch attraction, saturation) can create clusters from technical noise ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).

## Related

- [[30-Concepts/crispr-lineage-recording]] · [[30-Concepts/lineage-tracing]] · [[30-Concepts/lineage-tracing-somatic-mutations]] · [[30-Concepts/single-cell-variant-calling]] · [[30-Concepts/monovar]] · [[10-Summaries/jahn-2016-scite]]
- [[40-Topics/single-cell-lineage-tracing]] · [[20-Entities/zheng-hu]]
