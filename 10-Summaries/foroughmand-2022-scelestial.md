---
type: summary
title: "Foroughmand-Araabi, Goliaei & McHardy 2022 — Scelestial: fast and accurate single-cell lineage tree inference based on a Steiner tree approximation algorithm"
source: "[[00-Sources/papers/Scelestial_ Fast and accurate single-cell lineage tree inference based on a Steiner tree approximation algorithm]]"
source_kind: paper
author: "Mohammad-Hadi Foroughmand-Araabi, Sama Goliaei, Alice C. McHardy (corresponding)"
published: 2022-08-11
ingested: 2026-08-17
doi: "10.1371/journal.pcbi.1009100"
journal: "PLOS Computational Biology 18:e1009100"
tags: [Scelestial, Steiner-tree, approximation-algorithm, neighbor-joining, missing-value-imputation, benchmark, scalability]
entities: []
concepts: ["[[phylogenetic-inference]]", "[[allele-dropout]]", "[[imputation]]", "[[clustering-algorithms]]"]
topics: ["[[cancer-clonal-evolution]]", "[[single-cell-lineage-tracing]]", "[[computational-methods]]"]
---

**Citation:** Foroughmand-Araabi, Goliaei & McHardy (2022) — *Scelestial: fast and accurate single-cell lineage tree inference based on a Steiner tree approximation algorithm* — *PLOS Computational Biology* 18, e1009100. [DOI](https://doi.org/10.1371/journal.pcbi.1009100)

# Foroughmand-Araabi 2022 — Scelestial

> The one paper in the single-cell phylogeny literature that offers a **performance guarantee**. Scelestial adapts a Steiner-tree approximation algorithm — a generalisation of neighbour joining — so that, unlike heuristics and MCMC samplers, its solution quality is bounded. It also folds **missing-value imputation into the tree objective**: internal nodes are chosen to minimise cost including the cost of filling in missing entries.

## Key claims

- **Approximation guarantees are the differentiator.** The author summary states it directly: the Steiner tree approximation algorithm, *unlike other heuristics and sampling-based methods (e.g. MCMC), provides guarantees of its performance*. In a field of MCMC samplers and local searches, this is a distinct methodological stance.
- **It is a generalisation of neighbour joining** — placing it on the distance-based side of the divide, but with internal (Steiner) nodes representing inferred ancestral genotypes rather than only interpolated points.
- **Two adaptations make it practical**: efficiently selecting a *limited subset* of candidate sequences as internal nodes (the full Steiner node space is intractable), and lineage-tree-based **missing-value imputation** folded into cost minimisation rather than done as preprocessing.
- **Beats seven state-of-the-art methods on accuracy and run time** — BitPhylogeny, [[ross-2016-onconem|OncoNEM]], [[jahn-2016-scite|SCITE]], [[zafar-2017-sifit|SiFit]], SASC, [[singer-2018-sciphi|SCIPhI]], and SiCloneFit — on simulated and real single-cell tumour samples, and produces the most plausible evolutionary scenarios on the real cancer data.
- **Scalability is the stated motivation**: dataset sizes are growing, so scalable *and* accurate methods are needed — the MCMC generation does not scale.
- Implemented in C++ with an R package (RScelestial).

## Methods / evidence

Large simulation study plus real single-cell tumour datasets, benchmarked against seven competitors. The introduction contains an unusually complete taxonomy of the field — worth reading as a map: mutation trees (Kim & Simon), MCMC mixture models (BitPhylogeny), maximum-likelihood trees with heuristic search (OncoNEM) versus MCMC search (SCITE), finite-sites Bayesian (SiCloneFit), *k*-Dollo (SASC via simulated annealing, SPhyR via *k*-means), and bulk-integrating (B-SCITE via MCMC, PhISCS via mathematical programming).

Weight: a benchmark by the method's own authors, so the ranking should be read with the usual caution — but the comparator set is unusually broad and includes every major modelling family.

## Surprising or load-bearing bits

- **Imputation inside the objective, not before it.** Most pipelines impute missing genotypes and then build a tree, which lets imputation errors propagate silently. Making imputation part of what the tree is optimising means the tree and the filled-in values are mutually consistent — the same logic [[singer-2018-sciphi|SCIΦ]] applies to calling. (synthesis)
- **The introduction's taxonomy is the most useful artifact here** for a review: it sorts a decade of tools by *evolutionary model* × *search strategy*, which is exactly the two-axis cut a methods section needs. (synthesis)
- **Distance-based methods came back.** Neighbour joining was the naive baseline that the 2016 model-based generation was built to beat; Scelestial shows a principled distance/Steiner formulation can win on both accuracy and speed. The same reversal appears in the CRISPR lineage-tracing world with [[gong-2022-dclear|DCLEAR]] winning DREAM sub-challenges with distance methods. (synthesis)
- Editor of record was Joshua Welch — a reminder that the [[welch-2019-liger|LIGER]] integration line and the phylogeny line share a community.

## Concepts touched

- [[phylogenetic-inference]] — Steiner-tree approximation with guarantees; NJ generalisation.
- [[imputation]] — missing values imputed as part of tree cost minimisation.

## Connections to other sources

- Benchmarked against: [[ross-2016-onconem]], [[jahn-2016-scite]], [[zafar-2017-sifit]], [[singer-2018-sciphi]], [[el-kebir-2018-sphyr]] (as the SASC/SPhyR *k*-Dollo family), [[malikic-2019-phiscs]].
- Distance-based counterpart in the CRISPR-barcode world: [[gong-2022-dclear]].
- Copy-number tree methods outside this comparison: [[kaufmann-2022-medicc2]], [[wang-2021-medalt]].
- Review context: [[lu-2024-cnaphylogeny-review]].

## Open questions

- **Self-benchmarking.** An independent evaluation across these seven methods does not exist in the corpus.
- The approximation guarantee is on the Steiner tree objective, not on recovering the true lineage — a bounded answer to the stated problem is not the same as a bounded distance from biological truth. (synthesis)
- How the limited internal-node subset is chosen, and what that costs in optimality, is the key implementation detail.

## Related

- [[jahn-2016-scite]] · [[ross-2016-onconem]] · [[gong-2022-dclear]] · [[phylogenetic-inference]]
