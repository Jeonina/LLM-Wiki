---
type: summary
title: "Dou 2020 — Accurate detection of mosaic variants in sequencing data without matched controls (MosaicForecast)"
source: "[[00-Sources/papers/Accurate detection of mosaic variants in sequencing data without matched controls]]"
aliases: ["Dou 2020", "MosaicForecast", "MF"]
tags: [MosaicForecast, mosaic-variant-calling, read-phasing, machine-learning, brain-mosaicism, Park-lab, Walsh-lab, Harvard]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Dou et al. (2020) — *Accurate detection of mosaic variants in sequencing data without matched controls (MosaicForecast)* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-019-0368-8)

Dou, Kwon, Rodin, Cortés-Ciriano, Doan, Luquette, Galor, Bohrson, Walsh and Park (Harvard, Boston Children's) developed **MosaicForecast**, a machine-learning framework for detecting mosaic single-nucleotide variants and indels from bulk sequencing data **without a matched control sample**. The key idea is to leverage read-based **phasing** between candidate mosaic variants and nearby germline heterozygous variants: a true mosaic variant is co-haplotyped consistently with one and only one germline haplotype, while a germline het should generate both haplotypes.

The framework has three steps: (1) generate a training set by read-based phasing; (2) train a random forest model on >30 read-level features (VAF, mismatches per read, mapQ, strand bias, etc.); (3) extend to nonphasable sites via multinomial logistic regression. Applied to ~250× brain WGS data from 60 ASD and 15 neurotypical individuals, MosaicForecast achieved 80–90% validation rate for SNVs and 60–80% for indels — a multifold improvement in specificity over MuTect2 (8.9% in nonrepeat regions, 1% in repeat regions). In repeat regions, MosaicForecast reaches 77% precision.

## Why this matters

A workhorse mosaic-variant caller used widely in brain-mosaicism studies post-2020 (often paired with deep WGS). Conceptual companion to MosaicHunter (Huang 2017), DeepMosaic (Yang 2023), and Strelka2-modified. Anchors §4 (variant-calling tool family) and §5 (neuropsychiatric applications). Important context for our review: the read-phasing strategy that works for bulk samples ≥250× is one of the technical reasons bulk deep-WGS remains competitive with scWGS at moderate VAFs — a tension we want to articulate.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-019-0368-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/31907404/)

## Related

- [[10-Summaries/luquette-2019-natcomm]]
- [[10-Summaries/ha-2023-natmethods]]
- [[40-Topics/mosaic-variant-calling]]
- [[20-Entities/peter-park]]
