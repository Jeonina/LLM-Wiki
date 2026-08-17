---
type: summary
title: "Ross & Markowetz 2016 — OncoNEM: inferring tumor evolution from single-cell sequencing data"
source: "[[00-Sources/papers/OncoNEM_ inferring tumor evolution from single-cell sequencing data]]"
source_kind: paper
author: "Edith M. Ross, Florian Markowetz (corresponding)"
published: 2016-04-15
ingested: 2026-08-17
doi: "10.1186/s13059-016-0929-9"
journal: "Genome Biology 17:69"
tags: [OncoNEM, nested-effects-model, clonal-lineage-tree, unobserved-subpopulations, infinite-sites, allele-dropout, bladder-cancer, essential-thrombocythemia]
entities: []
concepts: ["[[phylogenetic-inference]]", "[[allele-dropout]]", "[[intratumor-heterogeneity]]", "[[single-cell-variant-calling]]", "[[clustering-algorithms]]"]
topics: ["[[cancer-clonal-evolution]]", "[[single-cell-lineage-tracing]]", "[[computational-methods]]"]
---

**Citation:** Ross & Markowetz (2016) — *OncoNEM: inferring tumor evolution from single-cell sequencing data* — *Genome Biology* 17, 69. [DOI](https://doi.org/10.1186/s13059-016-0929-9)

# Ross 2016 — OncoNEM

> One of the two 2016 papers (with [[jahn-2016-scite|SCITE]]) that turned single-cell tumour phylogeny into a modelled statistical problem rather than a clustering exercise. OncoNEM's distinctive move is to borrow the **nested effects model** from gene-perturbation screens: if clone A is ancestral to clone B, then A's mutations are a *subset* of B's — so tree inference becomes the problem of scoring **noisy subset relations**. It also does something its contemporaries do not: it explicitly tests for and infers **unobserved subpopulations**.

## Key claims

- **Two challenges are named and each is addressed.** (1) *Genotype noise* — reported false discovery rates of 2.67 × 10⁻⁵ to 6.7 × 10⁻⁵ mean false positives can outnumber true somatic variants, and reported ADO rates of 0.16–0.43 make false negatives and missing values pervasive. Because of this noise, standard clustering often fails even at the simple task of mapping cells to clones. (2) *Unobserved subpopulations* — sampling bias, undersampling, and extinction mean the sequenced cells represent only a subset of the clones that ever existed.
- **The scoring function comes from nested effects models**, which were built to read noisy subset relations in perturbation screens. Under the infinite-sites assumption and no mutation loss, ancestry implies mutation-set containment; OncoNEM predicts the expected mutation pattern from a candidate tree and scores the fit to the observed pattern while probabilistically absorbing genotyping error.
- **Inputs are minimal**: a binary genotype matrix plus the false-positive rate α and false-negative rate β, both estimable from the data. Outputs are three things at once — inferred subpopulations, a tree over them, and posterior probabilities for each mutation's occurrence.
- **It clusters and builds the tree simultaneously**, rather than clustering cells into clones first and then connecting them — the two-step approach used by Gawad and by Yuan, which OncoNEM argues loses information.
- **Mixture models are the wrong tool at this sample size.** The paper's explicit argument against BitPhylogeny-style tree-structured mixture models: they need large datasets to converge, while contemporary single-cell datasets contain **fewer than 100 cells**.
- Validated by simulation for robustness, benchmarked against a representative set of prior approaches (UPGMA, neighbour joining, likelihood optimisation, Bayesian phylogenetics, BitPhylogeny, mutation trees), then applied to 44 single cells from muscle-invasive bladder transitional cell carcinoma and 58 from essential thrombocythemia.

## Methods / evidence

Simulation studies for robustness and benchmarking; two real datasets of 44 and 58 cells. The related-work section is unusually thorough and is itself a useful map of the pre-2016 landscape — it separates classic phylogenetics (UPGMA, NJ, GTR likelihood, Bayesian), cluster-then-tree approaches, mixture models, and mutation-tree methods, and explains why each falls short on noisy single-cell data.

## Surprising or load-bearing bits

- **Inferring clones that were never sampled** is the capability that distinguishes OncoNEM from most of its successors, and it follows directly from the nested-effects formulation: an unobserved ancestor is just an internal node whose mutation set is implied by its descendants. (synthesis)
- **"Fewer than 100 cells" is the design constraint of the whole 2016 generation.** Every modelling choice in OncoNEM, SCITE, and their contemporaries is downstream of small *n*. Methods built for that regime should be re-evaluated against modern droplet-scale data ([[pellegrino-2018-tapestri]]). (synthesis)
- **The ADO range 0.16–0.43 is quoted from the primary literature** and matches the independent four-way measurement in [[gawad-2014-all-clonal-origins]] (median 20–24% after filtering) — the field's error model was empirically grounded by 2016.
- **Census-based variant calling is named as an incomplete fix**: requiring a variant in multiple cells removes random false positives but not recurrent sequencing-error sites.
- OncoNEM assumes the infinite-sites assumption and no mutation loss — precisely the assumption that [[el-kebir-2018-sphyr|SPhyR]] and [[zafar-2017-sifit|SiFit]] were built to relax two years later.

## Concepts touched

- [[phylogenetic-inference]] — nested effects models as a tree-scoring framework; joint clustering and tree inference.
- [[allele-dropout]] — the FP/FN parameterisation (α, β) that became standard for single-cell tree builders.

## Connections to other sources

- Published essentially alongside [[jahn-2016-scite]]; the two are the standard pairing in every subsequent benchmark.
- Relaxations of its infinite-sites assumption: [[zafar-2017-sifit]] (finite sites), [[el-kebir-2018-sphyr]] (*k*-Dollo), [[satas-2020-scarlet]] (loss-aware with CNA).
- Bulk-integrating successors: [[malikic-2019-phiscs]].
- Joint calling + tree inference: [[singer-2018-sciphi]].
- Benchmarked against by [[foroughmand-2022-scelestial]].
- Copy-number tree alternatives: [[kaufmann-2022-medicc2]], [[wang-2021-medalt]].
- Error-model context: [[gawad-2014-all-clonal-origins]], [[zafar-2016-monovar]], [[dong-2017-sccaller]].

## Open questions

- **Scalability past ~100 cells** is not addressed, and the method's search over tree structures is heuristic.
- The no-mutation-loss assumption is violated wherever copy-number loss removes an SNV — ubiquitous in cancer, as the *k*-Dollo literature later argued.
- α and β are estimated from data but treated as global constants; per-cell or per-locus variation in dropout is not modelled.

## Related

- [[jahn-2016-scite]] · [[phylogenetic-inference]] · [[40-Topics/cancer-clonal-evolution]]
