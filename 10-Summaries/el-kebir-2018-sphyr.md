---
type: summary
title: "El-Kebir 2018 — SPhyR: tumor phylogeny estimation from single-cell sequencing data under loss and error"
source: "[[00-Sources/papers/SPhyR_ tumor phylogeny estimation from single-cell sequencing data under loss and error]]"
source_kind: paper
author: "Mohammed El-Kebir"
published: 2018-09-08
ingested: 2026-08-17
doi: "10.1093/bioinformatics/bty589"
journal: "Bioinformatics 34:i671–i679"
tags: [SPhyR, k-Dollo, homoplasy, back-mutation, matrix-completion, integer-linear-programming, colorectal-cancer]
entities: []
concepts: ["[[phylogenetic-inference]]", "[[copy-number-variation]]", "[[allele-dropout]]", "[[intratumor-heterogeneity]]"]
topics: ["[[cancer-clonal-evolution]]", "[[computational-methods]]"]
---

**Citation:** El-Kebir (2018) — *SPhyR: tumor phylogeny estimation from single-cell sequencing data under loss and error* — *Bioinformatics* 34, i671–i679. [DOI](https://doi.org/10.1093/bioinformatics/bty589)

# El-Kebir 2018 — SPhyR

> The evolutionary model, not the noise model, is the thing to fix. Infinite-sites says a mutation is gained once and never lost — but in cancer, **SNVs are lost constantly** because copy-number aberrations delete the regions carrying them. SPhyR adopts the ***k*-Dollo** model — a character may be gained **once** but lost at most ***k*** times — and shows that solutions to this problem are **constrained integer matrix completions**, which makes an ILP formulation possible that solves realistic instances in seconds.

## Key claims

- **Parallel evolution is rare in cancer; loss is ubiquitous.** This asymmetry is the paper's central biological premise and it selects the model: Dollo parsimony permits back-mutation/loss but forbids parallel gain, which matches how SNVs actually disappear (copy-number loss of the region), unlike the fully general finite-sites model of [[zafar-2017-sifit|SiFit]].
- ***k*-Dollo bounds the permissiveness.** Unrestricted Dollo allows unlimited losses; capping at *k* keeps the model identifiable and the search tractable.
- **The combinatorial insight**: inferring a *k*-Dollo phylogeny from an error-free binary matrix is a variant of the **cladistic multi-state perfect phylogeny problem**, and its solutions are constrained integer matrix completions of the input. This connection is what yields an efficient ILP.
- **SPhyR is coordinate-ascent** over the noisy case: it simultaneously corrects errors in the observed matrix *D* and infers the tree, producing a corrected matrix *B* plus phylogeny *T*.
- **Outperforms both infinite-sites and finite-sites methods** on simulated data in solution quality and run time, and gives a likelier evolutionary explanation for a metastatic colorectal cancer.
- The problem framing is stated cleanly: single-cell sequencing gives you the **leaves** of *T* directly, bypassing bulk deconvolution — but the leaves are observed through high false-positive, false-negative and missing-data rates, and correcting them *requires* an evolutionary model.

## Methods / evidence

Formal problem statement and combinatorial characterisation, ILP formulation, coordinate-ascent algorithm for the error-tolerant case, simulation benchmarks against infinite-sites and finite-sites competitors, and one real metastatic colorectal cancer dataset. Code at github.com/elkebir-group/SPhyR.

Weight: the theory is the contribution and it is rigorous. The real-data evidence is a single tumour evaluated by likelihood rather than by an external ground truth.

## Surprising or load-bearing bits

- **Choosing an evolutionary model is choosing which biological process you believe dominates.** The infinite-sites → *k*-Dollo → finite-sites progression is not a ladder of generality-is-better; it is a claim about cancer. SPhyR's argument is that Dollo is *exactly right* for cancer because loss (via CNA) is common and parallel gain is not. (synthesis)
- **Error correction and tree inference are the same problem**, and the paper says so explicitly: the errors in *D* "can be corrected by estimating the phylogenetic tree *T*". This is the same insight [[singer-2018-sciphi|SCIΦ]] operationalises at the read level the same year — two independent papers reaching it in 2018. (synthesis)
- **Framing tree inference as matrix completion** connects tumour phylogenetics to a well-studied optimisation literature and is why SPhyR is fast where MCMC methods are slow.
- The *k*-Dollo model was picked up immediately — [[foroughmand-2022-scelestial|Scelestial]] lists SASC and SPhyR together as the *k*-Dollo family in its benchmark.

## Concepts touched

- [[phylogenetic-inference]] — *k*-Dollo as the middle ground between infinite and finite sites; matrix-completion formulation.
- [[copy-number-variation]] — CNA-driven SNV loss is the mechanism motivating the model.

## Connections to other sources

- Relaxes the infinite-sites assumption of [[jahn-2016-scite]] and [[ross-2016-onconem]].
- More restrictive (and therefore more identifiable) than the finite-sites model of [[zafar-2017-sifit]].
- Loss-aware alternative that uses CNA data directly: [[satas-2020-scarlet]].
- Bulk-integrating combinatorial contemporary from the same problem space: [[malikic-2019-phiscs]].
- Benchmarked against by [[foroughmand-2022-scelestial]].
- The CNA-driven-loss premise is documented in [[wang-2014-nuc-seq]] and [[navin-2011-sns-tumor-evolution]].

## Open questions

- **How to choose *k*** is not resolved; it is a user parameter that encodes a prior about how lossy the tumour is.
- Copy-number states are not modelled jointly — SPhyR infers loss from the SNV matrix rather than from observed CNAs, which [[satas-2020-scarlet|SCARLET]] later addresses.
- Single real dataset; no external ground truth for the colorectal result.

## Related

- [[zafar-2017-sifit]] · [[satas-2020-scarlet]] · [[phylogenetic-inference]] · [[40-Topics/cancer-clonal-evolution]]
