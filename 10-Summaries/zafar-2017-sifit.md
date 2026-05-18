---
type: summary
title: "Zafar 2017 — SiFit: inferring tumor trees from single-cell sequencing data under finite-sites models"
source: "[[00-Sources/papers/SiFit_ inferring tumor trees from single-cell sequencing data under finite-sites models]]"
aliases: ["Zafar 2017 SiFit", "SiFit", "finite-sites tumor phylogeny"]
tags: [SiFit, tumor-phylogeny, finite-sites-model, scDNA-seq, allelic-dropout, Nakhleh-lab, Navin-lab, Rice]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/SiFit_ inferring tumor trees from single-cell sequencing data under finite-sites models]]"
---

**Citation:** Zafar et al. (2017) — *SiFit: inferring tumor trees from single-cell sequencing data under finite-sites models* — *Genome Biology*. [DOI](https://doi.org/10.1186/s13059-017-1311-2)

Zafar, Tzen, Navin, Chen and Nakhleh (Rice, MD Anderson, BCM) developed **SiFit**, a likelihood-based tumor-phylogeny inference method that operates under a **finite-sites model** rather than the infinite-sites assumption used by SCITE (Jahn 2016) and OncoNEM. The finite-sites model accommodates the reality that chromosomal deletions, loss of heterozygosity (LOH), and convergent evolution can cause apparent SNV state-reversals — events that infinite-sites methods cannot explain.

The likelihood model includes: (i) error terms for SCS-specific noise (ADO, FP rates from WGA, FN rates); (ii) finite-sites transition probabilities between genotype states accounting for point mutation, deletion, and LOH; (iii) heuristic search over tree space. Benchmarked on simulated and experimental scDNA-seq data from two colorectal-cancer patients (primary + metastatic tumors), SiFit produced phylogenies more consistent with observed CNAs than SCITE/OncoNEM.

## Why this matters

A key methodological advance over SCITE — SiFit's finite-sites accommodation is critical for tumors with active chromosomal instability (most solid tumors). Conceptual predecessor of SCARLET (Satas 2020), which formalizes the SNV-loss/CN-loss joint modeling. Existing `zafar2017` bibkey already present. Anchors §4 (phylogenetic methods family) and §5 (cancer applications). The Zafar 2016 Monovar + Zafar 2017 SiFit pair is the canonical Nakhleh-Navin contribution to scDNA-seq computational methodology.

---
**Source:** [DOI](https://doi.org/10.1186/s13059-017-1311-2) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28927434/)

## Related

- [[10-Summaries/zafar-2016-monovar]]
- [[10-Summaries/jahn-2016-scite]]
- [[10-Summaries/satas-2020-scarlet]]
- [[10-Summaries/mallory-2020-cna-review]]
- [[20-Entities/nicholas-navin]]
