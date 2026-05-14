---
type: summary
title: "Zafar 2017 — SiFit: inferring tumor trees from single-cell sequencing data under finite-sites models"
aliases: ["SiFit", "Zafar 2017"]
tags: [computational, tumor-phylogeny, finite-sites, scDNA-seq, Navin-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Hamim_2017_GenomeBiology.pdf"]
---

Zafar, Tzen, Navin, Chen and Nakhleh developed SiFit, a likelihood-based tumor-phylogeny inference method that operates on scDNA-seq genotype data under a finite-sites model of evolution. SiFit extends the error models of SCITE and OncoNEM (both of which assume infinite-sites evolution, meaning each site mutates at most once) to accommodate the chromosomal deletions, loss of heterozygosity, and convergent evolution observed in real tumors, which violate the infinite-sites assumption.

SiFit's error model integrates allele-dropout, false-positive errors, and finite-sites transition probabilities, and uses a heuristic search to find the phylogeny that maximizes the likelihood of the observed scDNA-seq genotype matrix. Benchmarking on synthetic data and on scDNA-seq from two colorectal cancer patients (primary + metastatic) showed improved tumor-phylogeny accuracy over SCITE, OncoNEM, and distance-based methods.

## Why this matters

Computational phylogeny inference is the bridge between scDNA-seq genotype matrices and the clonal-evolution biology that drives §5 cancer applications. SiFit is one of the canonical tumor-phylogeny tools alongside SCITE, OncoNEM, BitPhylogeny, and PhyloWGS. Anchors §4 (computational framework).

---
**Source:** [DOI](https://doi.org/10.1186/s13059-017-1311-2) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28927434/)

## Related

- [[10-Summaries/zafar-2016-natmethods]]
- [[30-Concepts/tumor-phylogeny]]
- [[10-Summaries/kim-2018-cell]]
- [[20-Entities/nicholas-navin]]
