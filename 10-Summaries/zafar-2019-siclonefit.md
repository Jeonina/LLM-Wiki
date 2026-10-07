---
type: summary
title: "Zafar et al. 2019 — SiCloneFit: Bayesian inference of population structure, genotype, and phylogeny of tumor clones from single-cell genome sequencing data"
source: "[[00-Sources/papers/SiCloneFit_ Bayesian inference of population structure, genotype, and phylogeny of tumor clones from single-cell genome sequencing data]]"
source_kind: paper
author: "Hamim Zafar, Nicholas Navin, Ken Chen, Luay Nakhleh"
published: 2019-11
ingested: 2026-10-07
doi: "10.1101/gr.243121.118"
journal: "Genome Research 29(11):1847–1859"
tags: [SiCloneFit, clonal-phylogeny, nonparametric-Bayes, Chinese-restaurant-process, finite-sites, doublets, allelic-dropout, MCMC, reversible-jump, colorectal-cancer, metastasis, MACHINA, SiFit, SCG]
entities: ["[[20-Entities/nicholas-navin]]", "[[20-Entities/ken-chen]]"]
concepts: ["[[phylogenetic-inference]]", "[[allele-dropout]]", "[[doublet-detection]]", "[[intratumor-heterogeneity]]", "[[single-cell-variant-calling]]", "[[clustering-algorithms]]"]
topics: ["[[cancer-clonal-evolution]]", "[[single-cell-lineage-tracing]]", "[[computational-methods]]", "[[scdna-cancer-applications]]"]
---

**Citation:** Zafar et al. (2019) — *SiCloneFit: Bayesian inference of population structure, genotype, and phylogeny of tumor clones from single-cell genome sequencing data* — *Genome Research* 29(11):1847–1859. [DOI](https://doi.org/10.1101/gr.243121.118)

# Zafar 2019 — SiCloneFit

> Single-cell SNV tools had split into two camps. **Clusterers** (Bernoulli mixtures, SCG) find clones but ignore their ancestry. **Tree builders** (SCITE, OncoNEM, SiFit, PhISCS) build lineages but mostly assume infinite sites, give no direct clone reconstruction, and cannot represent **doublets**, because a merged genotype is not a leaf of any lineage tree. SiCloneFit does both at once. A **tree-structured Chinese restaurant process** puts clones (clusters of cells) at the leaves of a clonal phylogeny. Clone genotypes evolve along the tree under SiFit's **finite-site model** (point mutation, deletion, LOH), observations pass through a **false-positive/false-negative error model**, and an optional **Beta-binomial doublet model** lets a cell draw from two clones. A Gibbs sampler with partial reversible-jump and Metropolis–Hastings moves samples the joint posterior. The output is clone number, clone membership, clone genotypes and the tree, each with posterior support.

## Key claims

- **Joint inference with uncertainty.** The authors call SiCloneFit "the first Bayesian framework that jointly reconstructs clonal populations and their evolutionary history from SCS data sets under a finite-site model of evolution while accounting for cell doublets along with other WGA artifacts".
- **The number of clones K is unknown and inferred.** The CRP concentration parameter α₀ has a Gamma(1,1) prior. Tree topology prior is uniform, branch lengths exponential, and error rates and evolution parameters Beta-distributed. The genotype likelihood on the tree uses Felsenstein pruning.
- **Simulation benchmark against SCG, OncoNEM, SiFit and SCITE.** SiCloneFit was best on clustering (ARI), genotyping error (Hamming per cell per site) and tree error (pairwise cell shortest-path distance) in every setting reported. Settings varied cells, sites, clone number, FN rate, FP rate and missing data. OncoNEM failed to run at m = 500 cells. SCG was the overall second-best performer and beat SiCloneFit on genotyping in one setting only (n = 100, 30% missing).
- **Finite sites helps even under infinite-sites data.** Across deletion, LOH and recurrence probabilities, SiCloneFit beat SiFit (the only other finite-site method). Even when data were simulated with d = ω = r = 0, SiCloneFit reconstructed genotypes and phylogeny better than SiFit.
- **Neutral evolution.** Under a Williams et al. neutral-evolution simulation (1/f power law), SiCloneFit was "similar or better" than SCG, SiFit and SCITE.
- **Error rates are learnable.** Estimated α and β correlate with simulated values at 0.998 and 0.992. Under high sampling distortion it missed only rare (single-cell) clusters.
- **Doublets.** With 10% simulated doublets, it beat SCG (the only other doublet-aware method) on clustering (B-cubed F-score) and genotyping. Tree error was lower in all settings except m = 500, n = 100. On a high-grade serous ovarian dataset (370 cells, 43 mutations), 17 doublets were called by both tools; SCG called 11 more, 10 of them with near-equal doublet/singlet posteriors.
- **CRC1 (178 cells, 16 SNVs; Leung et al. 2017 targeted panel).** 104 of 120 SNV pairs violate the four-gamete test. SiCloneFit found 5 clusters: normal N, primary P1/P2 split by a TPM4 mutation, metastatic M, and a mostly metastatic diploid cluster D. Truncal mutations were APC (heterozygous nonsense), KRAS and TP53. A **recurrent GATA1 mutation** not reported in the original study was supported by a mixture-model Bayesian binomial test on read counts. MACHINA on the SiCloneFit tree gave **polyclonal single-source seeding colon → liver** (migration number 2, comigration 1). SCG could not split P1 from P2.
- **CRC2 (182 cells, 36 SNVs).** 347 of 630 pairs violate four-gamete. Six clusters: N, P1, P2, M1, M2, and an independent diploid lineage I of 7 cells. SiCloneFit places **two "bridge mutations" (FHIT, ATP7B)** between the metastatic divergences, where SCITE had placed four (adding APC and CHN1); read-count tests favour SiCloneFit's placement. FUS and LINGO2 show strong evidence of recurrence, read as **convergent evolution** in the two metastatic clones. No doublets were found in either CRC dataset, consistent with FACS doublet removal.

## Methods / evidence

Generative model plus MCMC (Neal-style partial Gibbs / partial MH, with reversible-jump for adding or removing clusters and the corresponding tree edges). Posterior summaries: MPEAR for clustering, maximum clade credibility tree via DendroPy, per-entry posterior genotype. Simulated clonal trees used Beta-splitting topologies with Dirichlet prevalences. Competitors' outputs were adapted, for example by k-medoids/silhouette clustering on SiFit and SCITE trees. Implemented in Java (MIT licence).

Weight: the simulations come from the same group's generator, under assumptions close to the model's own (finite-site transitions, independent FP/FN errors). The large margins over infinite-sites methods partly reflect that match. Real-data claims (GATA1 recurrence, bridge mutations) rest on read-count tests on the same data, not orthogonal validation. Input is a binary or ternary called-genotype matrix, so SiCloneFit inherits upstream caller errors. (synthesis)

## Surprising or load-bearing bits

- **Infinite-sites violations are pervasive in real targeted data.** 87% (104/120) and 55% (347/630) of SNV pairs fail the four-gamete test. Errors alone could produce much of this, which is exactly why a model that separates errors from true recurrence or loss matters.
- **A tree-structured CRP is the trick that unifies clustering and phylogeny.** Clusters are leaves, so adding a cluster means adding an edge, which is why reversible-jump moves are needed.
- **Doublets fall out of the mixture structure.** A second cluster indicator for each cell makes a merged genotype representable, something no lineage-tree-only method can do.
- **The discussion anticipates the joint SNV + CNA future.** Copy number is currently approximated through ternary states; exact copy number would sharpen genotypes and reduce ADO effects. The authors note SNV and CNA datasets then needed different WGA methods.

## Concepts touched

- [[phylogenetic-inference]] — finite-site clonal phylogeny with nonparametric clone number.
- [[allele-dropout]] / [[single-cell-variant-calling]] — FP/FN error model applied after calling.
- [[doublet-detection]] — doublets modelled inside the inference, not filtered beforehand.
- [[intratumor-heterogeneity]] — clone prevalence and metastatic seeding in CRC.
- [[clustering-algorithms]] — Dirichlet-process-style clustering coupled to a tree.

## Connections to other sources

- Direct successor of [[zafar-2017-sifit]] (finite-site model and error model reused). SiFit was also demonstrated on two CRC patients with primary and metastatic tumours; these may be the same Leung et al. datasets. (synthesis)
- Competitors benchmarked: [[jahn-2016-scite]], [[ross-2016-onconem]], [[zafar-2017-sifit]], and SCG (not in the wiki). Related tree methods it discusses: [[malikic-2019-phiscs]]; later finite-site / Dollo work: [[el-kebir-2018-sphyr]], [[kozlov-2022-cellphy]], [[satas-2020-scarlet]].
- Joint calling + phylogeny peers named by the field review [[lahnemann-2020-grand-challenges]] (which lists "SciCloneFit" with single-cell genotyper and SCIΦ — [[singer-2018-sciphi]]).
- Upstream callers whose output it consumes: [[zafar-2016-monovar]] (same first author).
- Clonal-structure context: [[gawad-2014-all-clonal-origins]] (the Bernoulli mixture + BIC clustering that SCG later extended), [[navin-2011-sns-tumor-evolution]].

## Open questions

- Scalability: MCMC over trees and clusterings for thousands of cells and sites is untested here.
- Read-count input instead of called genotypes is proposed but not implemented.
- Can recurrence calls such as GATA1, FUS and LINGO2 be validated orthogonally (deep bulk, other cells) rather than by tests on the same reads? (synthesis)

## Related

- [[zafar-2017-sifit]] · [[phylogenetic-inference]] · [[nicholas-navin]] · [[ken-chen]] · [[40-Topics/cancer-clonal-evolution]]
