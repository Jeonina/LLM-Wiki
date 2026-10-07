---
type: concept
title: Single-cell phylogenetic inference
aliases: [phylogenetic reconstruction, cell phylogeny, lineage tree inference]
tags: [lineage-tracing, phylogenetics, computational, fate-mapping]
created: 2026-06-02
updated: 2026-10-07
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


## Added 2026-10-07

Phylogenetic inference is NP-hard under most scoring criteria, and exhaustive search is infeasible beyond roughly 20 single cells ([[10-Summaries/lahnemann-2020-grand-challenges]]). An extension of RAxML-NG with a 10-state unphased diploid genotype model outperformed a ternary model only slightly and only at very high (10–50%) error rates ([[10-Summaries/lahnemann-2020-grand-challenges]]); this line was later published as CellPhy ([[10-Summaries/kozlov-2022-cellphy]]).

SiCloneFit couples a tree-structured Chinese restaurant process (clones at the leaves of a clonal phylogeny) with SiFit's finite-site model, an FP/FN error model and a Beta-binomial doublet model, sampling clone number, membership, genotypes and tree jointly by MCMC ([[10-Summaries/zafar-2019-siclonefit]]). In two targeted CRC datasets, 104/120 and 347/630 SNV pairs violated the four-gamete test ([[10-Summaries/zafar-2019-siclonefit]]).

COMPASS infers joint trees of SNVs and CNAs (gains, losses, copy-neutral LOH) from amplicon scDNA-seq by modelling per-amplicon coverage weights, per-variant dropout, doublets and learned node attachment probabilities; it outperformed BiTSC² (which assumes uniform coverage) and SCITE (uniform attachment prior) in Tapestri-like simulations [[10-Summaries/sollier-2023-compass]]. Its two-stage search keeps CNA false positives very low but misses CNAs in subclones not marked by an SNV or LOH [[10-Summaries/sollier-2023-compass]].

ScisTree2 scales infinite-sites maximum-posterior tree search to tens of thousands of cells via an SPR local search that evaluates the full O(n²) neighbourhood in O(n²m) time plus branch-and-bound pruning, calling genotypes as a by-product of mutation placement ([[10-Summaries/zhang-2025-scistree2]]). In simulations it remained more accurate than SiFit and CellPhy even with up to 75% finite-sites sites, but no method recovered accurate topologies below 1× coverage or with few sites ([[10-Summaries/zhang-2025-scistree2]]). For copy-number data, WGD-aware MEDICC2 trees plus SNV-based doubleTime timing were used to separate truncal, parallel and subclonal WGD histories ([[10-Summaries/mcpherson-2025-ongoing-wgd]]).

CNA trees differ from SNV mutation trees because overlapping, nested and recurrent CNAs break the infinite-sites assumption. SCICoNE allows arbitrary violations at the bin level, forbids regaining a segment after CN 0, and forbids duplicate genotypes ([[10-Summaries/kuipers-2025-scicone]]). It reuses SCITE's prune-and-reattach and label-swap MCMC moves and adds event, node and genotype-preserving moves ([[10-Summaries/kuipers-2025-scicone]]).

**Acquisition bias and branch lengths.** Using only variant sites overestimates branch lengths; SIEVE corrects this with the count of invariant background sites, reporting branch lengths as expected somatic mutations per site, and outperformed CellPhy and SiFit on branch-score distance in all simulated scenarios ([[10-Summaries/kang-2022-sieve]]). Models under the finite-sites assumption performed as well as ISA models when ISA held, while SCIPhI degraded at 100 cells when ISA was violated ([[10-Summaries/kang-2022-sieve]]).

CellPhy extends the 4-state GTR model to a 16-state diploid-genotype model (GT16) with explicit allelic-dropout and amplification/sequencing-error parameters, implemented in RAxML-NG so that somatic SNV trees get maximum-likelihood search, bootstrap branch support and ancestral-state mutation mapping ([[10-Summaries/kozlov-2022-cellphy]]). In its simulations it was the most accurate of the methods tested (TNT, infSCITE, SiFit, SCIPhI, ScisTree), especially at 5× depth when it uses genotype likelihoods, and it ran about 1–2 orders of magnitude faster than SiFit, SCIPhI or infSCITE ([[10-Summaries/kozlov-2022-cellphy]]). Growing-population genealogies have short internal branches and need hundreds to tens of thousands of SNVs to resolve, a limit the authors say applies to every method ([[10-Summaries/kozlov-2022-cellphy]]).


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
| Subperfect | keep perfect phylogeny as target, **eliminate** up to k_max violating mutations (likelihood objective under FP/FN rates) | [[10-Summaries/malikic-2019-phiscs]] |
| Star homoplasy | mutate at most once *per lineage*, convergence allowed | [[10-Summaries/sashittal-2023-startle]] |
| PMM (mixed-type missing) | non-modifiability + rate decay + heritable vs dropout missingness + heterogeneous sites | [[10-Summaries/chu-2025-laml]] |

For cancer SNVs the model encodes a biological claim — loss via copy-number aberration is ubiquitous, parallel gain is rare ([[10-Summaries/el-kebir-2018-sphyr]]). For CRISPR recorders it encodes a property of the *engineering*: non-modifiability exists because an edited target no longer matches its guide RNA ([[10-Summaries/sashittal-2023-startle]]), which makes those models far better justified. (synthesis)

**Search strategy**: MCMC ([[10-Summaries/jahn-2016-scite]], [[10-Summaries/singer-2018-sciphi]], [[10-Summaries/seidel-2022-tidetree]], [[10-Summaries/seidel-2026-sciphy]]) · heuristic likelihood ([[10-Summaries/ross-2016-onconem]]) · ILP/CSP with optimality guarantees ([[10-Summaries/el-kebir-2018-sphyr]], [[10-Summaries/malikic-2019-phiscs]]) · approximation algorithm with performance bounds ([[10-Summaries/foroughmand-2022-scelestial]]) · EM + topology search ([[10-Summaries/chu-2025-laml]]) · distance-based ([[10-Summaries/gong-2022-dclear]]).

**Three ideas worth carrying beyond phylogenetics.**

- **Tree inference and error correction are the same problem.** Reached independently in 2018 at two different levels — read counts ([[10-Summaries/singer-2018-sciphi]]) and genotype matrices ([[10-Summaries/el-kebir-2018-sphyr]]). The tree is a prior on genotypes, so a mutation can be called in a cell with zero variant reads ([[10-Summaries/singer-2018-sciphi]]) — powerful when the tree is right, and a generator of correlated false positives when it is not. (synthesis)
- **Imputation belongs inside the objective**, not before it ([[10-Summaries/foroughmand-2022-scelestial]]; [[10-Summaries/chu-2025-laml]]).
- **Missing data can be informative.** Heritable missingness is inherited by descendants and carries phylogenetic signal; dropout does not — and the two look identical in the data ([[10-Summaries/chu-2025-laml]]).

**Only topology, or topology plus time?** Non-probabilistic methods (distance, parsimony) are robust and scalable but cannot produce time-resolved branch lengths, which precludes asking *when* migration, fate or fitness changes occurred ([[10-Summaries/chu-2025-laml]]). That gap is what the probabilistic generation closes — and [[10-Summaries/chu-2025-laml|LAML]] uses it to map metastasis to real time, finding three epochs and a burst at ~month 2.
