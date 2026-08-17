---
type: summary
title: "Malikic et al. 2019 — PhISCS: a combinatorial approach for subperfect tumor phylogeny reconstruction via integrative use of single-cell and bulk sequencing data"
source: "[[00-Sources/papers/PhISCS_ a combinatorial approach for subperfect tumor phylogeny reconstruction via integrative use of single-cell and bulk sequencing data]]"
source_kind: paper
author: "Salem Malikic, et al."
published: 2019-11-01
ingested: 2026-08-17
doi: "10.1101/gr.234435.118"
journal: "Genome Research 29:1860–1877"
tags: [PhISCS, subperfect-phylogeny, ISA-violation, integer-linear-programming, constraint-satisfaction, bulk-integration, VAF, B-SCITE]
entities: []
concepts: ["[[phylogenetic-inference]]", "[[allele-dropout]]", "[[copy-number-variation]]", "[[intratumor-heterogeneity]]"]
topics: ["[[cancer-clonal-evolution]]", "[[computational-methods]]"]
---

**Citation:** Malikic et al. (2019) — *PhISCS: a combinatorial approach for subperfect tumor phylogeny reconstruction via integrative use of single-cell and bulk sequencing data* — *Genome Research* 29, 1860–1877. [DOI](https://doi.org/10.1101/gr.234435.118)

# Malikic 2019 — PhISCS

> Two moves at once: **integrate bulk with single-cell data**, and **give up on perfect phylogeny**. PhISCS defines the *optimal subperfect phylogeny* problem — minimise a weighted combination of false negatives (from dropout and coverage), false positives (read errors), and the number of mutations that **violate the infinite-sites assumption** — subject to lineage constraints derived from bulk variant allele frequencies. Solved as an ILP and, for the first time in tumour phylogenetics, as a **Boolean constraint satisfaction problem**.

> **Source caveat:** the ingested clipping is frontmatter abstract plus two figure captions and one reference — no main text or methods. Claims below come from the abstract and the two captions.

## Key claims

- **ISA violations are real and multi-causal.** They arise from loss of heterozygosity, deletions, convergent evolution — and also from *incorrect copy-number estimation*, i.e. some apparent violations are artifacts of the analysis rather than biology. PhySCS counts them rather than forbidding them.
- **The objective is a single linear combination of three error types**: false negatives, false positives, and ISA-violating mutations. Rather than assuming one is negligible, it prices them against each other.
- **Bulk VAFs supply lineage constraints.** Bulk sequencing gives population-level allele frequencies that constrain which nesting relationships are possible; PhISCS enforces these while fitting the single-cell genotypes.
- **Optimality is guaranteed, unlike probabilistic competitors.** Because the formulation is combinatorial and solved by state-of-the-art ILP/CSP solvers, PhISCS returns a provably optimal solution for its objective — the paper's explicit contrast with MCMC and heuristic methods.
- **Benchmarked against SCITE and B-SCITE** using MLTD (multi-labeled tree dissimilarity) and its dual MLTSM. Against SCITE: 10 trees, 15 subclones, 100 SNVs, 100 cells, bulk at 5000× coverage. Against B-SCITE: 10 trees, 7 subclones, 40 SNVs, 100 cells, including cases where three SNVs sit in regions with clonal copy number 3 or 4 — i.e. testing exactly the copy-number-induced ISA violations the method is built for.

## Methods / evidence

Simulation benchmarks with systematically varied bulk-sample count (*h*), single-cell false-negative rate (*fn*), and number of ISA-violating mutations; plus real datasets (not visible in this clipping). Evaluation by MLTD/MLTSM against ground-truth trees.

Weight: limited by the clipping. The simulation design visible in the figure captions is well-constructed — it varies the three factors the method claims to handle, independently.

## Surprising or load-bearing bits

- **"Subperfect" is an honest name for what tumour phylogenies actually are.** Rather than choosing a relaxed evolutionary model as [[el-kebir-2018-sphyr|SPhyR]] does, PhISCS keeps perfect phylogeny as the target and **penalises deviation from it** — a different philosophy for the same problem, and arguably more interpretable, since the number of violations is reported rather than absorbed into the model. (synthesis)
- **Boolean CSP as a first in the field** matters practically: modern SAT solvers scale differently from ILP, and for combinatorial phylogeny problems the choice of solver technology can be the difference between seconds and hours.
- **Naming incorrect copy-number estimation as a source of apparent ISA violation** is a caution that generalises: some of what looks like exotic evolution is upstream analysis error. (synthesis)
- **Bulk + single-cell integration** is the pragmatic answer to single-cell's small *n*: bulk supplies frequency information that hundreds of cells cannot, while single cells supply the co-occurrence information bulk cannot. Both [[gawad-2014-all-clonal-origins]] and [[wang-2014-nuc-seq]] used bulk alongside single cells experimentally; PhISCS formalises it.

## Concepts touched

- [[phylogenetic-inference]] — subperfect phylogeny; ILP/CSP formulation; bulk-VAF lineage constraints.

## Connections to other sources

- Direct comparators: [[jahn-2016-scite]] and its bulk-integrating variant B-SCITE.
- Alternative relaxations of ISA: [[el-kebir-2018-sphyr]] (*k*-Dollo), [[zafar-2017-sifit]] (finite sites), [[satas-2020-scarlet]] (CNA-informed loss).
- Cited within: El-Kebir et al. 2016, multi-state perfect phylogeny mixtures — the same combinatorial lineage as SPhyR.
- Benchmarked against by [[foroughmand-2022-scelestial]].
- Bulk/single-cell hybrid designs in practice: [[gawad-2014-all-clonal-origins]], [[wang-2014-nuc-seq]].

## Open questions

- **The relative weights on FN, FP and ISA violations are user-set** and determine the answer; how to choose them is not recoverable from this clipping.
- Whether guaranteed optimality of a *chosen objective* beats approximate optimisation of a *better-specified likelihood* is the open methodological argument between the combinatorial and probabilistic camps. (synthesis)
- Full-text re-ingest needed for methods and real-data results.

## Related

- [[jahn-2016-scite]] · [[el-kebir-2018-sphyr]] · [[phylogenetic-inference]] · [[40-Topics/cancer-clonal-evolution]]
