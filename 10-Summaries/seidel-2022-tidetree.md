---
type: summary
title: "Seidel & Stadler 2022 — TiDeTree: a Bayesian phylogenetic framework to estimate single-cell trees and population dynamic parameters from genetic lineage tracing data"
source: "[[00-Sources/papers/TiDeTree_ a Bayesian phylogenetic framework to estimate single-cell trees and population dynamic parameters from genetic lineage tracing data]]"
source_kind: paper
author: "Sophie Seidel, Tanja Stadler (corresponding)"
published: 2022-11-09
ingested: 2026-08-17
doi: "10.1098/rspb.2022.1844"
journal: "Proceedings of the Royal Society B 289:20221844"
tags: [TiDeTree, BEAST2, birth-death-sampling, phylodynamics, scarring-rate, time-scaled-tree, well-calibrated-simulation]
entities: []
concepts: ["[[crispr-lineage-recording]]", "[[lineage-tracing]]", "[[phylogenetic-inference]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[computational-methods]]"]
---

**Citation:** Seidel & Stadler (2022) — *TiDeTree: a Bayesian phylogenetic framework to estimate single-cell trees and population dynamic parameters from genetic lineage tracing data* — *Proceedings of the Royal Society B* 289, 20221844. [DOI](https://doi.org/10.1098/rspb.2022.1844)

# Seidel 2022 — TiDeTree

> Brings **phylodynamics** to CRISPR lineage tracing: don't just recover the tree topology, jointly estimate the **population-dynamic parameters** that generated it — birth rate, death rate, sampling proportion — under a birth–death-sampling process, with editing modelled explicitly. Development is described as "an elaborate balance between cell division, apoptosis and differentiation," and TiDeTree's premise is that this balance is estimable from the tree rather than merely reflected in it.

> **Source caveat:** the ingested clipping is the appendices (in-silico validation and parameter-inference sections) plus the abstract in frontmatter — no main text, results, or real-data application. Claims below reflect the validation design, which is the part that was captured.

## Key claims

- **Well-calibrated simulation is used for validation**, the correct standard for Bayesian methods: simulate a tree under a birth–death-sampling process from a single cell over 32 time units, draw sampled lineages with probability ρ (modelling the random sequencing of a subset of cells), simulate 10 targets evolving along the tree under the editing model, then infer and check whether the truth falls inside the posterior.
- **1,000 simulations, 860 usable alignments** after discarding trees with >700 sampled lineages (14% of the data); final alignments span 1–687 cells.
- **Coverage and correlation are the reported metrics**: the fraction of simulations where the true parameter falls in the 95% highest-posterior-density interval, plus Pearson correlation between posterior medians and true values.
- **Identifiability forces parameters to be fixed.** The death rate is fixed at 0.4 *because* one birth–death parameter must be fixed for identifiability; one scarring rate is fixed (s₅₀ = 1) so all other scarring rates are interpretable relative to it; the origin is fixed at 32 and the scarring duration at 0–16, both justified as knowledge available from the experimental design.
- **Priors are stated explicitly** with 5th/95th percentiles: scarring rates Exponential(2) → [0.03, 1.5]; clock rate LogNormal(−7, 0.5) → [4×10⁻⁴, 2×10⁻³]; birth rate LogNormal(−0.6, 0.1) → [0.47, 0.65]; sampling proportion Beta(4, 8) → [0.14, 0.56].
- **Relative scarring-rate information is treated as experimentally obtainable** — the paper notes that the relative occurrence of scarring outcomes can readily be measured, so it need not be inferred from the lineage data alone.

## Methods / evidence

Bayesian inference; 10⁸ MCMC steps or until ESS > 200, discarding 10% burn-in. Two validation regimes: parameters drawn from priors (calibration check), then parameters fixed at known values (accuracy and precision check under weakly informative priors).

Weight: the validation methodology visible here is rigorous and well-specified. The biological application is not in this clipping.

## Surprising or load-bearing bits

- **The fixed-parameter requirement is a real constraint, not a convenience.** Birth–death models are non-identifiable without fixing one rate; every phylodynamic estimate from lineage tracing therefore rests on an externally supplied number. Any downstream biological claim about proliferation rates inherits that assumption. (synthesis)
- **14% of simulated trees were discarded for being too large** — a hint that MCMC cost scales badly, which is exactly the criticism [[chu-2025-laml|LAML]] later makes: TiDeTree and GAPML "were designed for *older generations* of dynamic lineage tracing technologies … Additionally, they are very computationally intensive."
- **Experimental design is smuggled into the prior, legitimately.** Fixing the origin at 32 and scarring window at 0–16 "incorporates our knowledge of the duration of the experiment." This is the advantage Bayesian phylodynamics has over distance-based methods — the experiment's known structure becomes information rather than being discarded. (synthesis)
- **Same lab, direct successor**: [[seidel-2026-sciphy|SciPhy]] extends this BEAST 2 line to *sequential* insertion-based recorders, where the order of edits carries extra information.

## Concepts touched

- [[crispr-lineage-recording]] — scarring modelled as a rate process rather than as character states.
- [[phylogenetic-inference]] — birth–death-sampling phylodynamics applied to somatic cell populations.

## Connections to other sources

- Direct successor from the same authors: [[seidel-2026-sciphy]].
- Criticised as computationally intensive and built for older recorders by [[chu-2025-laml]].
- Non-probabilistic alternatives that scale better but give no branch times: [[gong-2022-dclear]], [[jones-2020-cassiopeia]], [[sashittal-2023-startle]].
- Recorder technologies: [[mckenna-2016-science]]; review context [[rodriguez-fraticelli-2026-lineage-tracing-review]], [[wang-2026-multimodal-lineage-computational]].
- Endogenous-barcode alternatives to engineered recorders: [[ludwig-2019-mtdna-lineage-tracing]], [[scherer-2025-nature]], [[chen-2025-methyltree]].

## Open questions

- **Real-data application is absent from this clipping** — a full-text re-ingest is needed to record what TiDeTree found biologically.
- Whether the fixed death rate materially biases the birth-rate and sampling-proportion estimates is not visible here.
- Scalability limits are implied (trees >700 lineages discarded) but not characterised.

## Related

- [[seidel-2026-sciphy]] · [[chu-2025-laml]] · [[crispr-lineage-recording]] · [[40-Topics/single-cell-lineage-tracing]]
