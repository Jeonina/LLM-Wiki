---
type: summary
title: "Sanders 2020 — Single-cell analysis of structural variations and complex rearrangements with tri-channel processing (scTRIP)"
source: "[[00-Sources/papers/Single-cell analysis of structural variations and complex rearrangements with tri-channel processing]]"
aliases: ["Sanders 2020 scTRIP", "scTRIP", "Strand-seq SV"]
tags: [scTRIP, Strand-seq, structural-variants, complex-rearrangements, Korbel-lab, EMBL, leukemia, chromothripsis]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/Single-cell analysis of structural variations and complex rearrangements with tri-channel processing]]"
---

**Citation:** Sanders et al. (2020) — *Single-cell analysis of structural variations and complex rearrangements with tri-channel processing (scTRIP)* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-019-0366-x)

Sanders, Meiers, Ghareghani, Porubsky, Jeong, van Vliet, Rausch, Richter-Pechańska, Kunz, Jenni, Bolognini, Longo, Raeder, Kinanen, Zimmermann, Benes, Schrappe, Mardin, Kulozik, Bornhauser, Bourquin, Marschall and Korbel (EMBL, Saarland, Heidelberg) developed **scTRIP** (single-cell Tri-channel processing), a computational framework that detects structural variants in individual cells from Strand-seq data by integrating three orthogonal information layers: **read depth**, **template strand state** (W/C, derived from BrdU-marked nascent strands), and **haplotype phase** (W/C ratios resolved by haplotype).

Each SV class has a diagnostic "footprint" across the three layers: deletions cause read-depth loss on one haplotype; duplications cause haplotype-specific read-depth gain with unchanged orientation; inversions reverse read orientation on a single haplotype; inverted-duplications combine reorientation with read-depth gain; balanced translocations co-segregate strand states without read-depth change. A Bayesian joint-calling framework infers SVs in a haplotype-aware manner. Applied to 565 single cells from transformed RPE-1, C7-RPE-1, and patient-derived T-cell acute lymphoblastic leukemia, scTRIP detected somatic SVs at very-low cell-fractions (<1%), discovered four-fold more somatic SVs in leukemia samples than cytogenetic karyotyping, and resolved a sub-clonal chromothripsis event.

## Why this matters

scTRIP is the gold-standard SV-detection workflow for single-cell data, distinct from CNV-only methods (Ginkgo, HMMcopy). The Strand-seq + tri-channel-processing combination uniquely detects **copy-number-neutral** rearrangements (balanced translocations, inversions, inverted duplications) that are invisible to read-depth alone. Anchors §3.1 (Strand-seq variant family), §4 (SV calling computational tools), and §5 (cancer applications — leukemia clonal architecture).

---
**Source:** [DOI](https://doi.org/10.1038/s41587-019-0366-x) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/31873213/)

---
**Source:** [DOI](https://doi.org/10.1038/s41587-019-0366-x) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/31873213/)

## Related

- [[10-Summaries/falconer-2012-natmethods]]
- [[10-Summaries/sanders-2017-natprotoc]]
- [[20-Entities/jan-korbel]]
- [[30-Concepts/strand-seq]]
