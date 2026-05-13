---
type: summary
title: "Kaufmann 2022 — MEDICC2: whole-genome doubling aware copy-number phylogenies for cancer evolution"
aliases: ["Kaufmann 2022 MEDICC2", "MEDICC2", "WGD-aware phylogeny"]
tags: [MEDICC2, copy-number-phylogeny, WGD, whole-genome-doubling, tumor-evolution, Schwarz-lab, BIH-Berlin]
created: 2026-05-13
updated: 2026-05-13
sources: ["Tom_2022_GenomeBiology.pdf"]
---

Kaufmann, Petkovic, Watkins, Colliver, Laskina, Thapa, Minussi, Navin, Swanton, Van Loo, Haase, Tarabichi and Schwarz (BIH Berlin, MDC, Cologne, Crick, MSKCC) developed **MEDICC2**, a method for inferring evolutionary trees from haplotype-specific somatic copy-number alterations (SCNAs) in single-cell or bulk tumor data, **with explicit modeling of whole-genome doubling (WGD)** events.

Methodological advances over MEDICC1: (i) drops the infinite-sites assumption — allows multiple mutations and parallel evolution at the same locus; (ii) does not treat adjacent loci as independent — captures statistical dependencies that simpler distance-based methods (Euclidean, Hamming) miss; (iii) computes minimum-event-distance including WGD events in linear time using a weighted finite-state-transducer framework; (iv) reconstructs ancestral genomes and times SCNA events relative to WGD.

Validated on simulations and applied to 2,778 PCAWG tumors, where MEDICC2 accurately identifies WGD against a consensus "gold standard" from six copy-number callers. Multi-sample prostate-cancer applications demonstrated detection of subclonal WGD events and correct placement of parallel-evolution and **mirrored-subclonal-allelic-imbalance** events (which CHISEL also flags). Inference scales to thousands of single cells without prior clustering.

## Why this matters

MEDICC2 is the gold-standard phylogenetic reconstruction tool for copy-number-driven tumor evolution, especially when WGD is relevant. Complements CHISEL (Zaccaria 2021) for allele/haplotype-specific CN inference: CHISEL produces the per-cell haplotype-specific CN profile; MEDICC2 builds the evolutionary tree from those profiles. Anchors §4 (phylogenetic tools alongside SiFit, Monovar phylogeny) and §5 (cancer-evolution applications). Important context for the review: scDNA phylogenetics is mature for copy-number; **scDNA + chromatin/methylation joint phylogenetics remains underdeveloped** — a gap our §7 future-perspectives section will articulate.

## Related

- [[10-Summaries/zaccaria-2021-chisel]]
- [[10-Summaries/kim-2018-nature]]
- [[10-Summaries/laks-2019-cell]]
- [[30-Concepts/whole-genome-doubling]]
- [[40-Topics/scdna-cancer-applications]]
