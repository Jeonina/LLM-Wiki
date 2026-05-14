---
type: summary
title: "Lähnemann 2021 — Accurate and scalable variant calling from single cell DNA sequencing data with ProSolo"
aliases: ["ProSolo", "Lähnemann 2021"]
tags: [computational, variant-calling, MDA, single-cell, ProSolo]
created: 2026-05-13
updated: 2026-05-13
sources: ["David_2021_NatureCommunications.pdf"]
---

Lähnemann, Köster and colleagues developed ProSolo, a single-cell SNV caller that probabilistically models a single MDA-amplified cell jointly with a bulk-tissue sample from the same population. ProSolo addresses the two principal failure modes of MDA: differential amplification of the two parental alleles (locally variable, captured by a mechanistically motivated empirical model) and amplification errors introduced by $\phi$29 polymerase at rates orders of magnitude above the somatic mutation rate.

The bulk sample serves as an unamplified background: it samples from the same cell population without WGA artifacts and provides a reference allele-frequency distribution at each locus. ProSolo combines per-locus bulk allele frequencies with single-cell MDA likelihoods to control false discovery rate flexibly. Benchmarking shows higher precision and recall than MonoVar, SCcaller, and SCAN-SNV across simulated and real datasets, with explicit FDR control that the existing tools lack.

## Why this matters

Computational complement to SCAN-SNV (Luquette 2019) and LiRA (Lodato 2018) for the single-cell SNV calling problem. Adds the explicit bulk-paired modeling framework: when bulk DNA from the same sample is available (common in BSMN-style studies), ProSolo uses it as an unamplified background. Anchors §4 (computational framework).

---
**Source:** [DOI](https://doi.org/10.1038/s41467-021-26938-w) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34795237/)

---
**Source:** [DOI](https://doi.org/10.1038/s41467-021-26938-w) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34795237/)

## Related

- [[10-Summaries/luquette-2019-natcomm]]
- [[10-Summaries/lodato-2018-science]]
- [[30-Concepts/single-cell-variant-calling]]
