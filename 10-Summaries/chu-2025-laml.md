---
type: summary
title: "Chu et al. 2025 — Maximum likelihood inference of time-scaled cell lineage trees with mixed-type missing data using LAML"
source: "[[00-Sources/papers/Maximum likelihood inference of time-scaled cell lineage trees with mixed-type missing data using LAML]]"
source_kind: paper
author: "Gillian Chu, Uyen Mai, Henri Schmidt, Benjamin J. Raphael (corresponding)"
published: 2025-07-02
ingested: 2026-08-17
doi: "10.1186/s13059-025-03649-9"
journal: "Genome Biology 26:198"
tags: [LAML, PMM-model, time-resolved-tree, mixed-type-missing-data, heritable-dropout, EM-algorithm, KP-tracer, metastasis-timing, gastruloid, intMEMOIR]
entities: []
concepts: ["[[crispr-lineage-recording]]", "[[lineage-tracing]]", "[[phylogenetic-inference]]", "[[imputation]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[cancer-clonal-evolution]]", "[[computational-methods]]"]
---

**Citation:** Chu, Mai, Schmidt & Raphael (2025) — *Maximum likelihood inference of time-scaled cell lineage trees with mixed-type missing data using LAML* — *Genome Biology* 26, 198. [DOI](https://doi.org/10.1186/s13059-025-03649-9)

# Chu 2025 — LAML

> The paper that separates **two kinds of missing data that look identical** and shows one of them is informative. In dynamic lineage tracing, an entry can be missing because of a **heritable modification** (epigenetic silencing, or resection removing several target sites at once) or because of **dropout** (technical failure in scRNA-seq). Heritable missingness is inherited by descendants and therefore carries **phylogenetic signal**; dropout does not. No prior method distinguished them. LAML's Probabilistic Mixed-type Missing (PMM) model does, and delivers **time-resolved branch lengths** as a result.

## Key claims

- **Four features define a modern dynamic lineage tracing system**, and PMM models all four: (1) **non-modifiability** — an edited target site cannot be edited again; (2) **decay in mutation rate** over time, because the finite pool of target sites is consumed; (3) **mixed-type missing data** — heritable versus non-heritable; (4) **heterogeneous target sites** — each site has its own set of possible edits, which is "unconventional in statistical phylogenetics and has not been modeled in either species phylogenetics or single-cell lineage trees."
- **The field splits cleanly into two camps, and each has a structural limitation.** Non-probabilistic methods — distance-based ([[gong-2022-dclear|DCLEAR]]) and maximum parsimony ([[jones-2020-cassiopeia|Cassiopeia]], [[sashittal-2023-startle|Startle]]) — make few generative assumptions and are robust, but **without a temporal model they can only estimate topology, precluding questions about the timing of migration, fate and fitness**. Probabilistic methods give branch times, but general-purpose phylogenetics software (PhyML, IQ-Tree, RAxML, BEAST, MrBayes) does not capture irreversibility, non-modifiability, or heritable missingness — and the adaptations that exist ([[seidel-2022-tidetree|TiDeTree]], GAPML) "were designed for older generations" of recorders and are "very computationally intensive."
- **LAML jointly estimates** tree topology, time-scaled branch lengths, editing rate, heritable missing rate, and dropout probability; it also imputes missing data and infers MAP ancestral sequences.
- **The algorithm is EM plus topology search**, iterated. In the no-heritable-missing case there is a **closed-form solution**; in the general case, an efficient block coordinate ascent. This is where the speed advantage over MCMC comes from.
- **A multi-progenitor extension** handles experiments starting from several progenitors, imputes missing progenitor labels, and detects missing progenitor cells.
- **The biological payoff is timing.** On KP-tracer mouse lung adenocarcinoma, LAML maps metastasis events to real time and finds **three temporal epochs of metastasis progression with distinct migration patterns and a metastasis burst at around month 2** — described as a novel application of dynamic lineage tracing.
- Validated on simulated data plus three model systems: KP-tracer lung adenocarcinoma, mouse embryonic trunk-like structures (gastruloids), and mouse embryos traced with intMEMOIR.

## Methods / evidence

Simulation benchmarks on topology accuracy and scalability against existing methods, plus three real lineage-tracing datasets from different recorder technologies. Time-resolved branch lengths validated against known experimental timing.

Weight: the three-technology validation is a strength — it tests whether the PMM model generalises across recorder chemistries rather than fitting one. The metastasis-epoch result is the novel biological claim and rests on one dataset.

## Surprising or load-bearing bits

- **"Missing data is informative" is the reusable insight.** Heritable missingness is a *character state*, not an absence of information — and treating it as absence throws away signal. The same distinction plausibly applies elsewhere in single-cell analysis, wherever a technical zero and a biological zero are conflated (scRNA-seq dropout, [[scatac-imputation|scATAC binarisation]], methylation coverage gaps). (synthesis)
- **Timing was the thing the field could not do**, and it is the thing clinicians and developmental biologists actually want. "When did this clone metastasise" is unanswerable from a topology. The month-2 burst is the first concrete demonstration. (synthesis)
- **Closed-form EM in the special case** is why LAML can claim both accuracy and scalability where TiDeTree cannot — a reminder that in this literature the winning move is often a tractable likelihood rather than a richer model.
- **Heterogeneous target sites had never been modelled** in either species phylogenetics or cell-lineage work. Recorder engineering outran the statistics.
- **Non-modifiability is modelled by both LAML and [[sashittal-2023-startle|Startle]]** — same lab, same constraint, two different formalisms (probabilistic vs parsimony). Reading them together shows what the probabilistic framing buys: branch times, at higher computational cost.

## Concepts touched

- [[crispr-lineage-recording]] — the PMM model as the current best description of dynamic recorder data.
- [[imputation]] — missing data imputed as part of likelihood maximisation, with the heritable/dropout distinction carried through.
- [[phylogenetic-inference]] — time-resolved trees for somatic lineages.

## Connections to other sources

- Same-lab parsimony predecessor: [[sashittal-2023-startle]].
- Classified competitors: [[gong-2022-dclear]] (distance), [[jones-2020-cassiopeia]] (parsimony), [[seidel-2022-tidetree]] (Bayesian, criticised as slow and built for older recorders).
- Contemporary Bayesian alternative for sequential recorders: [[seidel-2026-sciphy]].
- Recorder technologies referenced: [[mckenna-2016-science]] (GESTALT), CARLIN, iTracer, intMEMOIR, KP-tracer.
- Endogenous-marker lineage tracing where no recorder is available: [[ludwig-2019-mtdna-lineage-tracing]], [[kwok-2022-mquad]], [[scherer-2025-nature]], [[chen-2025-methyltree]], [[coorens-2021-nature]].
- Review context: [[rodriguez-fraticelli-2026-lineage-tracing-review]], [[wang-2026-multimodal-lineage-computational]].

## Open questions

- **Metastasis epochs rest on one dataset** (KP-tracer); replication in an independent traced tumour model is the obvious next test.
- Branch times are calibrated against experiment duration, so absolute timing inherits whatever the experimental design assumes.
- Engineered recorders are unavailable in human tissue, so the timing capability does not transfer to human somatic mosaicism — where only endogenous markers exist and mutation rates are far lower. (synthesis)

## Related

- [[sashittal-2023-startle]] · [[seidel-2026-sciphy]] · [[crispr-lineage-recording]] · [[40-Topics/single-cell-lineage-tracing]]
