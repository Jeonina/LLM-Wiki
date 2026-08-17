---
type: summary
title: "Singer et al. 2018 — Single-cell mutation identification via phylogenetic inference (SCIΦ)"
source: "[[00-Sources/papers/Single-cell mutation identification via phylogenetic inference]]"
source_kind: paper
author: "Jochen Singer, Jack Kuipers, Katharina Jahn, Niko Beerenwinkel (corresponding)"
published: 2018-12-04
ingested: 2026-08-17
doi: "10.1038/s41467-018-07627-7"
journal: "Nature Communications 9:5144"
tags: [SCIPhI, joint-calling, MCMC, beta-binomial, allele-dropout, tumor-phylogeny, breast-cancer, ALL]
entities: []
concepts: ["[[single-cell-variant-calling]]", "[[phylogenetic-inference]]", "[[allele-dropout]]", "[[monovar]]", "[[sccaller]]", "[[mda]]"]
topics: ["[[mosaic-variant-calling]]", "[[cancer-clonal-evolution]]", "[[computational-methods]]"]
---

**Citation:** Singer, Kuipers, Jahn & Beerenwinkel (2018) — *Single-cell mutation identification via phylogenetic inference* — *Nature Communications* 9, 5144. [DOI](https://doi.org/10.1038/s41467-018-07627-7)

# Singer 2018 — SCIΦ

> Stop treating variant calling and tree building as two steps. Cells are related by a phylogeny, mutations propagate along its branches, so **the tree is prior information about where mutations should be**. SCIΦ jointly calls mutations and estimates the tumour phylogeny by MCMC — and can therefore recover a mutation in a cell with **very low or even zero variant-read support**, because the tree says it should be there.

## Key claims

- **The circular dependency is the opportunity.** Every prior caller treats cells as independent (SCcaller) or pools them without structure ([[zafar-2016-monovar|Monovar]]). SCIΦ makes the dependency explicit: candidate loci are identified from the posterior probability of ≥1 mutated cell, those loci are used to learn a cell lineage tree by MCMC, and mutations are then assigned to cells by sampling from the posterior.
- **Two reasons it beats Monovar**, stated by the authors: tree inference lets a mutation be assigned to a cell with missing or minimal variant support, and a **beta-binomial** model of nucleotide counts (with learned parameters) reflects the real count-generating process better than the alternatives.
- **It outperforms Monovar on F1** across cell numbers — more sensitive at comparable precision. Monovar is the only prior tool that shares information across cells at all.
- **The existing-caller critique is precise.** GATK HaplotypeCaller and SAMtools are ill-suited because single-cell noise profiles differ from bulk. [[zafar-2016-monovar|Monovar]] addresses low, uneven coverage by pooling across cells but assumes no dependency across sites. [[dong-2017-sccaller|SCcaller]] handles local allelic amplification bias but does so per cell, requires germline SNPs (unavailable for panel data), and **cannot recover mutations lost to dropout or LOH**.
- **The MDA error profile is quantified**: allelic dropout at roughly 10–20%, plus false positives from early-cycle φ29 errors amplified to high frequency, plus uneven coverage leaving some sites unreadable.
- Applied to a whole-exome breast cancer dataset and a panel acute lymphoblastic leukaemia dataset.

## Methods / evidence

Simulation across cell numbers and dropout rates, benchmarked against Monovar; two real datasets (WES breast cancer, panel ALL). MCMC posterior sampling for both tree and mutation assignment.

Weight: the comparison is against Monovar only, because at the time no other caller shared information across cells. That makes the benchmark narrow but fair for the specific claim being made.

## Surprising or load-bearing bits

- **"Call the mutation because the tree says it should be there"** is powerful and dangerous in the same breath. It is exactly right when the tree is right, and it manufactures correlated false positives when the tree is wrong. The paper does not characterise this failure mode. (synthesis)
- **2018 produced two independent statements of the same idea** — that error correction and phylogeny inference are one problem. SCIΦ makes it at the read/count level; [[el-kebir-2018-sphyr|SPhyR]] makes it at the genotype-matrix level. Neither cites the other's framing. (synthesis)
- **SCcaller's inability to recover dropout-lost mutations** is the specific gap SCIΦ targets, and it is a structural limitation of any per-cell caller: with the alternative allele absent from the library, no amount of per-cell modelling recovers it. Only cross-cell information can.
- **Panel data breaks germline-SNP-dependent methods.** A practical constraint worth remembering when choosing a caller for targeted assays like [[pellegrino-2018-tapestri|Tapestri]].

## Concepts touched

- [[single-cell-variant-calling]] — joint calling + tree inference as a single MCMC problem.
- [[phylogenetic-inference]] — the tree used as a prior on genotypes rather than only as an output.

## Connections to other sources

- Direct comparator and the only prior cross-cell caller: [[zafar-2016-monovar]].
- Critiqued per-cell alternative: [[dong-2017-sccaller]]; see also [[luquette-2019-natcomm]] and [[luquette-2021-scan2]] for the mosaicism-side caller line.
- Tree-building contemporaries whose trees SCIΦ effectively co-estimates: [[jahn-2016-scite]] (same group), [[ross-2016-onconem]], [[el-kebir-2018-sphyr]], [[zafar-2017-sifit]].
- Benchmarked against by [[foroughmand-2022-scelestial]] (as SCIPhI).
- Caller-concordance context: [[ha-2023-natmethods]], [[valecha-2022-scsnv-review]].
- Amplification error source: [[dean-2002-mda]], [[hou-2015-wga-comparison]].

## Open questions

- **No analysis of tree-misspecification risk** — how many false positives appear when the inferred tree is wrong is unmeasured.
- MCMC scalability to droplet-scale cell numbers is not addressed.
- Copy-number changes are claimed to be tolerated ("robust to copy number changes") but not modelled explicitly.

## Related

- [[zafar-2016-monovar]] · [[jahn-2016-scite]] · [[single-cell-variant-calling]] · [[40-Topics/mosaic-variant-calling]]
