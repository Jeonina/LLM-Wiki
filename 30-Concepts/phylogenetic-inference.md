---
type: concept
title: Single-cell phylogenetic inference
aliases: [phylogenetic reconstruction, cell phylogeny, lineage tree inference]
tags: [lineage-tracing, phylogenetics, computational, fate-mapping]
created: 2026-06-02
updated: 2026-08-10
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

## Added 2026-08-10

Two papers make the same structural point from different data. [[10-Summaries/wang-2021-medalt]]: under aneuploidy a locus is repeatedly altered by successive CNAs, so the **infinite-sites assumption is violated**, and Euclidean, Hamming or correlation distances misrepresent the segmental, non-linear nature of CNA evolution. Minimal event distance is the appropriate metric, with homozygous loss encoded as infinite distance because deleted fragments cannot be recovered. [[10-Summaries/jones-2020-cassiopeia]]: encoding the recorder's irreversibility and unedited founder state into the algorithm is what reduces an NP-hard multi-state perfect-phylogeny problem to a tractable binary one.

The transferable lesson is that assay-specific physical constraints belong in the model, not around it (synthesis).


## Related

- [[30-Concepts/crispr-lineage-recording]] · [[30-Concepts/lineage-tracing]] · [[30-Concepts/single-cell-variant-calling]] · [[30-Concepts/monovar]] · [[10-Summaries/jahn-2016-scite]]
- [[40-Topics/single-cell-lineage-tracing]] · [[20-Entities/zheng-hu]]

## Added 2026-08-17

Eleven sources ingested 2026-08-14 make the single-cell tree-inference landscape sortable on **two axes: evolutionary model × search strategy** ([[10-Summaries/foroughmand-2022-scelestial]] supplies the taxonomy). (synthesis)

**Evolutionary model — a claim about the mutational process, not a ladder of generality.**

| Model | Rule | Method |
|---|---|---|
| Infinite sites (perfect phylogeny) | gained once, never lost | [[10-Summaries/jahn-2016-scite]], [[10-Summaries/ross-2016-onconem]] |
| *k*-Dollo | gained once, lost ≤ *k* times | [[10-Summaries/el-kebir-2018-sphyr]] (and SASC) |
| Finite sites | any state change allowed | [[10-Summaries/zafar-2017-sifit]] |
| Subperfect | keep perfect phylogeny as target, **penalise** violations | [[10-Summaries/malikic-2019-phiscs]] |
| Star homoplasy | mutate at most once *per lineage*, convergence allowed | [[10-Summaries/sashittal-2023-startle]] |
| PMM (mixed-type missing) | non-modifiability + rate decay + heritable vs dropout missingness + heterogeneous sites | [[10-Summaries/chu-2025-laml]] |

For cancer SNVs the model encodes a biological claim — loss via copy-number aberration is ubiquitous, parallel gain is rare ([[10-Summaries/el-kebir-2018-sphyr]]). For CRISPR recorders it encodes a property of the *engineering*: non-modifiability exists because an edited target no longer matches its guide RNA ([[10-Summaries/sashittal-2023-startle]]), which makes those models far better justified. (synthesis)

**Search strategy**: MCMC ([[10-Summaries/jahn-2016-scite]], [[10-Summaries/singer-2018-sciphi]], [[10-Summaries/seidel-2022-tidetree]], [[10-Summaries/seidel-2026-sciphy]]) · heuristic likelihood ([[10-Summaries/ross-2016-onconem]]) · ILP/CSP with optimality guarantees ([[10-Summaries/el-kebir-2018-sphyr]], [[10-Summaries/malikic-2019-phiscs]]) · approximation algorithm with performance bounds ([[10-Summaries/foroughmand-2022-scelestial]]) · EM + topology search ([[10-Summaries/chu-2025-laml]]) · distance-based ([[10-Summaries/gong-2022-dclear]]).

**Three ideas worth carrying beyond phylogenetics.**

- **Tree inference and error correction are the same problem.** Reached independently in 2018 at two different levels — read counts ([[10-Summaries/singer-2018-sciphi]]) and genotype matrices ([[10-Summaries/el-kebir-2018-sphyr]]). The tree is a prior on genotypes, so a mutation can be called in a cell with zero variant reads ([[10-Summaries/singer-2018-sciphi]]) — powerful when the tree is right, and a generator of correlated false positives when it is not. (synthesis)
- **Imputation belongs inside the objective**, not before it ([[10-Summaries/foroughmand-2022-scelestial]]; [[10-Summaries/chu-2025-laml]]).
- **Missing data can be informative.** Heritable missingness is inherited by descendants and carries phylogenetic signal; dropout does not — and the two look identical in the data ([[10-Summaries/chu-2025-laml]]).

**Only topology, or topology plus time?** Non-probabilistic methods (distance, parsimony) are robust and scalable but cannot produce time-resolved branch lengths, which precludes asking *when* migration, fate or fitness changes occurred ([[10-Summaries/chu-2025-laml]]). That gap is what the probabilistic generation closes — and [[10-Summaries/chu-2025-laml|LAML]] uses it to map metastasis to real time, finding three epochs and a burst at ~month 2.
