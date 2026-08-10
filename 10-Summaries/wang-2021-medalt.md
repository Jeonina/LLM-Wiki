---
type: summary
title: "Wang et al. 2021 — MEDALT: single-cell copy number lineage tracing enabling gene discovery"
source: "[[00-Sources/papers/MEDALT_ single-cell copy number lineage tracing enabling gene discovery]]"
source_kind: paper
author: "Fang Wang, Qihan Wang, Vakul Mohanty, Shaoheng Liang, Jinzhuang Dou, Jincheng Han, Darlan Conterno Minussi, Ruli Gao, Li Ding, Nicholas Navin, Ken Chen (corresponding)"
published: 2021-02-23
ingested: 2026-08-10
doi: "10.1186/s13059-021-02291-5"
journal: "Genome Biology"
tags: [MEDALT, minimal-event-distance, lineage-tracing, copy-number, LSA, TNBC, convergent-evolution, infinite-sites]
entities: ["[[nicholas-navin]]", "[[ken-chen]]"]
concepts: ["[[copy-number-variation]]", "[[phylogenetic-inference]]", "[[chromosomal-instability]]", "[[intratumor-heterogeneity]]", "[[lineage-tracing]]", "[[somatic-mosaicism]]"]
topics: ["[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]", "[[computational-methods]]"]
---

**Citation:** Wang et al. (2021) — *MEDALT: single-cell copy number lineage tracing enabling gene discovery* — *Genome Biology* 22, 70. [DOI](https://doi.org/10.1186/s13059-021-02291-5)

# Wang 2021 — MEDALT

> Species-phylogenetics assumptions do not hold for aneuploid genomes. MEDALT replaces them: cells are related by **minimal event distance** — the fewest single-copy gains or losses converting one genome into another — and the lineage is a **directed minimum spanning tree** rooted at a normal diploid cell. A companion statistic, **lineage speciation analysis (LSA)**, then asks which alterations are associated with lineage expansion.

## Key claims

- **Why standard phylogenetics fails on CNAs.** Most methods assume sites evolve independently under the **infinite sites assumption**, but under aneuploidy a locus is repeatedly altered by successive CNAs — because of genome and chromatin structural constraints, replication/repair properties, and selection. Applying maximum parsimony forces over-segmentation of the genome into disjoint character intervals, which "ill-represents the properties of DNAs and distorts evolution propensity across copy number states." Euclidean, Hamming and correlation distances equally misrepresent the **segmental, non-linear** nature of CNA evolution, giving wrong topologies and branch lengths.
- **Minimal event distance (MED)** postulates the minimal number and series of single-copy gains or losses needed to evolve one genome into another. MEDICC introduced the metric but the problem is **NP-hard** and even simplified solutions scale only to tens of genomes; Zeira et al. gave a linear-time integer-programming formulation but released no tool. MEDALT uses an efficient greedy algorithm with the same asymptotic bound.
- **The tree**: a directed minimum spanning tree via an adapted **Edmonds' algorithm** that scales polynomially in cell number. Nodes are cells, edges are kinship, arrows point to younger cells, root is a normal diploid cell. The result is the parsimonious interpretation — the minimal total gains and losses explaining the whole population — while **allowing a region to be altered repeatedly**.
- **A biological constraint encoded as infinity**: chromosomal fragments cannot be recovered once completely lost, so MEDs originating from cells with homozygous loss are set to infinity. Irreversibility is in the distance, not bolted on afterwards.
- **LSA closes the gap between tree and function.** Having a phylogeny does not tell you which variants matter; LSA quantifies the impact of an alteration over the tree, accounting for sparse cell sampling, multiplicity in subset partitioning, and the intrinsic propensity of alteration at a given locus. It operates at both **focal (gene) and broad (chromosome-arm)** resolution, on individual samples and across cohorts, and detects **parallel/convergent evolution**.
- **Benchmarking**: MEDALT was more accurate than maximum-parsimony, neighbour-joining and maximum-likelihood trees at identifying fitness-associated alterations across 100 synthetic datasets.
- **Application**: on 20 triple-negative breast cancer patients, the approach prioritized genes essential for breast cancer cell fitness and predicted patient survival, including instances implicating convergent evolution.
- Motivating context: single-cell DNA platforms (tagmentation-based, 10x Genomics CNV) now give **tens of thousands of cells at ~100 kb resolution and ~0.1× coverage per cell**, and somatic mosaicism is extensive even in pathologically normal tissue such as blood and esophagus — so distinguishing pathogenic from normal CNA variation matters beyond cancer.

## Methods / evidence

Synthetic datasets with known fitness-associated alterations for the AUC comparison against three classes of conventional phylogenetic method, plus a 20-patient TNBC cohort where the output is validated against independent fitness essentiality and against patient survival — an external endpoint rather than internal consistency.

## Surprising or load-bearing bits

- **The infinite-sites violation is the crux, and it is structural rather than statistical.** Point mutations rarely recur at the same base; copy number changes recur at the same locus constantly. Any tool that treats copy-number states as independent characters is applying a model it is known to violate — which makes MEDALT's argument a general caution for the CNA-phylogeny tools in this corpus ([[lu-2024-cnaphylogeny-review]]).
- **Homozygous loss as an infinite distance is the most elegant detail.** Biological irreversibility becomes a property of the metric, so no tree can ever propose recovering a fully deleted fragment. Compare [[jones-2020-cassiopeia|Cassiopeia]], which encodes the irreversibility of Cas9 edits into its search in an analogous way — two very different data types, the same modelling instinct.
- **A minimum spanning tree over observed cells, not a bifurcating tree with inferred ancestors**, is a real departure: cells can be one another's ancestors. For a rapidly dividing tumour sampled densely, that is arguably more faithful than positing unobserved internal nodes — and it is what makes polynomial scaling possible.
- **LSA is the part that makes the tree useful.** A phylogeny alone is descriptive; asking which alterations associate with lineage expansion converts it into a driver-discovery instrument. Accounting for **locus-specific alteration propensity** is what keeps fragile genomic regions from dominating the results — the CNA analogue of correcting for background mutation rate in driver-gene discovery.
- **Convergent evolution is detectable and is the interesting signal**, because an alteration arising independently in multiple branches is much harder to explain as drift than one arising once — the same logic as recurrence across patients, applied within a single tumour.
- Survival prediction from single-tumour lineage structure is the strongest external validation available for a method of this kind, and it is rare in this corpus.

## Entities mentioned

- [[nicholas-navin]] — co-author; founding single-cell CNV work in [[navin-2011-sns-tumor-evolution]].
- [[ken-chen]] — corresponding author.

## Concepts touched

- [[phylogenetic-inference]] — MED as a CNA-appropriate distance, and the explicit break with the infinite-sites assumption.
- [[copy-number-variation]] — recurrent alteration of the same locus as the defining property.

## Connections to other sources

- Input SCCN profiles from [[zahn-2017-dlp]], [[laks-2019-dlp-plus]], and callers [[bakker-2016-aneufinder]], [[garvin-2015-natmethods]], [[wang-2020-scope]].
- Review of the CNA-phylogeny problem: [[lu-2024-cnaphylogeny-review]].
- Contrasting lineage-tracing substrates: [[jones-2020-cassiopeia]] (Cas9 scars), [[ludwig-2019-mtdna-lineage-tracing]] (mtDNA).
- Tumour-evolution applications: [[navin-2011-sns-tumor-evolution]], [[kim-2018-tnbc-chemoresistance]], [[xu-2012-single-cell-exome-kidney]].

## Open questions

- A minimum spanning tree over observed cells means **the inferred "parent" of a cell is whichever sampled cell is nearest in MED**, which under sparse sampling may be a cousin rather than an ancestor. The consequences for branch interpretation are not quantified here.
- The greedy MED computation approximates an NP-hard optimum; how often the approximation matters for downstream LSA calls is not reported.
- LSA identifies fitness *association*, not causation; the TNBC gene prioritization is validated against essentiality screens and survival, which is strong but still correlative.

## Related

- [[phylogenetic-inference]] · [[lu-2024-cnaphylogeny-review]] · [[bakker-2016-aneufinder]] · [[cancer-clonal-evolution]]
