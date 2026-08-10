---
type: summary
title: "Jones et al. 2020 — Inference of single-cell phylogenies from lineage tracing data using Cassiopeia"
source: "[[00-Sources/papers/Inference of single-cell phylogenies from lineage tracing data using Cassiopeia]]"
source_kind: paper
author: "Matthew G. Jones, Alex Khodaverdian, Jeffrey J. Quinn, Michelle M. Chan, Jeffrey A. Hussmann, Robert Wang, Chenling Xu, Jonathan S. Weissman, Nir Yosef (corresponding)"
published: 2020-04-14
ingested: 2026-08-10
doi: "10.1186/s13059-020-02000-8"
journal: "Genome Biology"
tags: [Cassiopeia, CRISPR-lineage-tracing, maximum-parsimony, Steiner-tree, ILP, perfect-phylogeny, homoplasy, missing-data]
entities: ["[[jonathan-weissman]]", "[[nir-yosef]]"]
concepts: ["[[lineage-tracing]]", "[[phylogenetic-inference]]", "[[crispr-lineage-recording]]", "[[allele-dropout]]", "[[doublet-detection]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[computational-methods]]"]
---

**Citation:** Jones et al. (2020) — *Inference of single-cell phylogenies from lineage tracing data using Cassiopeia* — *Genome Biology* 21, 92. [DOI](https://doi.org/10.1186/s13059-020-02000-8)

# Jones 2020 — Cassiopeia

> CRISPR lineage recorders produce character matrices — cells × target sites, values are Cas9-induced indels — at a scale and with a missing-data structure that classical phylogenetics was never built for. Cassiopeia supplies three maximum-parsimony algorithms tuned to the actual mutational process, a simulation engine for benchmarking, and **34,557 human cells traced over 15 generations** as a reference dataset.

## Key claims

- **Three reasons classical algorithms fail here.** Neighbour joining and Camin-Sokal were built for few samples, so **scalability** is limiting; they handle poorly the **missing data** typical of lineage tracing, which is either *heritable* (large Cas9 resections removing target sites, or transcriptional silencing) or *stochastic* (incomplete target-site capture); and they ignore the **design principles of the recorder** — that mutations are irreversible and the founder cell is unedited.
- **Cassiopeia-ILP**: build a "potential graph" whose vertices are unique observed and plausible ancestral cells and whose edges are possible evolutionary paths, then solve for the minimum-weight **Steiner tree** by integer linear programming. Irreversibility is modelled and missing data imputed exhaustively over all possible indels. Steiner tree is NP-hard, so this does not scale.
- **Cassiopeia-Greedy**: split cells recursively on mutations that likely occurred earliest. The theoretical contribution is a **reduction from the multi-state case to a binary one**, valid precisely because the founder is unedited and edited sites cannot be recut — which lets a perfect-phylogeny greedy algorithm apply, with a guarantee (Theorem 1) that if a perfect phylogeny exists the algorithm finds it. The heuristic that common mutations arose early is justified in expectation for realistic mutation rates.
- **Cassiopeia-Hybrid**: greedy to split into clades of roughly 300 cells, then ILP on each in parallel, then merge — scalable *and* near-optimal.
- **The trade between the two is homoplasy.** Greedy is by design **not robust to parallel evolution**, where the same character state arises independently in different parts of the tree; ILP is. Simulations quantify greedy's behaviour across homoplasy levels.
- **A simulation engine** varying number of characters, number of states, the state probability distribution, mutation rate, generation depth and missing-data rate, with defaults estimated from real experimental data and the state distribution interpolated from the empirical indel outcome distribution.
- **"Triplets correct" as the metric** — the proportion of cell triplets ordered correctly, stratified by triplet depth from the root — chosen over Robinson-Foulds because determining evolutionary relationships between cells is what downstream analyses actually need.
- **Results**: the Cassiopeia suite beats Camin-Sokal and neighbour joining across every parameter regime tested, and produces **more parsimonious trees** as well as more accurate ones. Greedy and Hybrid scale to **50,000 cells** — around the upper limit of current single-cell experiments — without substantial accuracy loss, where Camin-Sokal and ILP cannot. Bootstrapping shows robustness.
- The pipeline also handles the messy front end: read collapsing and error correction, local alignment and indel calling, per-cell molecule aggregation with **intra-doublet** detection, and clone segmentation with **inter-doublet** detection.
- The paper's third contribution is prescriptive: using the framework to derive **design principles for better Cas9 recorders**.

## Methods / evidence

A three-part evidence structure that is unusually complete for a methods paper: theory (the multi-state-to-binary reduction with a proof of optimality under perfect phylogeny), simulation across six independently varied parameters with 10–50 replicates each, and a purpose-generated experimental reference dataset of 34,557 cells across 11 clonal populations — the largest at the time — with continuous *in vitro* tracing giving partial ground truth.

## Surprising or load-bearing bits

- **Irreversibility plus an unedited founder is not a modelling nicety — it is what makes the problem tractable.** Those two experimental facts are exactly what licenses the multi-state-to-binary reduction, converting an NP-hard multi-state perfect-phylogeny problem into one with an efficient algorithm. Encoding assay design into the algorithm, rather than fitting a generic model, is the transferable lesson; [[wang-2021-medalt|MEDALT]] does the same thing with homozygous loss.
- **Missing data has two distinct causes with opposite implications.** Heritable dropout (a resection removing a target site) is itself lineage information and is shared by descendants; stochastic dropout (failed capture) is noise. Treating them identically — as classical methods do — throws away signal and creates false relationships.
- **Homoplasy is the fundamental limit of any recorder.** If the same indel arises twice independently, no algorithm can distinguish shared ancestry from convergence. That drives the design principle: **more possible states per target site** makes independent recurrence less likely, which is why the state distribution is a parameter in the simulation and a lever in recorder design.
- **Choosing triplets-correct over Robinson-Foulds is a claim about what a tree is for.** RF counts split disagreements; triplets ask whether A is more closely related to B than to C — the question every downstream analysis actually poses. Metric choice determines which method wins, so stating the reasoning matters.
- **Doublets are handled at two levels** — within a cell's molecules and between clones — reflecting that a doublet in lineage tracing produces a chimeric character vector that will be placed somewhere plausible and wrong. Compare the 4.3%/10.3% doublet accounting in [[cao-2019-moca]].
- The 50,000-cell ceiling was chosen to match single-cell experiment scale, not algorithmic limits — a rare instance of a method paper scoping its benchmark to the experiments people will actually run.

## Entities mentioned

- [[jonathan-weissman]] — co-author; the CRISPR recorder and Perturb-seq programs.
- [[nir-yosef]] — corresponding author; single-cell computational methods.

## Concepts touched

- [[lineage-tracing]] — the engineered-recorder branch, complementary to endogenous barcodes.
- [[phylogenetic-inference]] — maximum parsimony via Steiner tree and perfect-phylogeny greedy splitting.

## Connections to other sources

- The endogenous-barcode alternative, applicable in humans where engineering is impossible: [[ludwig-2019-mtdna-lineage-tracing]].
- Copy-number-based lineage inference facing the analogous infinite-sites problem: [[wang-2021-medalt]], [[lu-2024-cnaphylogeny-review]].
- Developmental context these trees are built to interrogate: [[cao-2019-moca]], [[wolf-2019-paga]].

## Open questions

- **Homoplasy is mitigated by recorder design, not solved by inference** — greedy is explicitly vulnerable and ILP does not scale, so at 50,000 cells the hybrid inherits some of greedy's exposure.
- The experimental reference dataset is *in vitro* with continuous tracing; whether the accuracy rankings hold on *in vivo* data with silencing, sparser sampling and unknown generation depth is not established.
- Simulation defaults are estimated from one experimental system, so parameter-regime conclusions are conditional on that recorder's indel outcome distribution.

## Related

- [[lineage-tracing]] · [[ludwig-2019-mtdna-lineage-tracing]] · [[wang-2021-medalt]] · [[single-cell-lineage-tracing]]
