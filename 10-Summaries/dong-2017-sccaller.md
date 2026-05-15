---
type: summary
title: "Dong 2017 — Accurate identification of single-nucleotide variants in whole-genome-amplified single cells (SCcaller + SCMDA)"
aliases: ["Dong 2017 SCcaller", "SCcaller", "SCMDA"]
tags: [SCcaller, SCMDA, scWGS, MDA, variant-calling, allelic-bias, Vijg-lab, Einstein]
created: 2026-05-13
updated: 2026-05-13
sources: ["Xiao_2017_NatureMethods.pdf"]
---

**Citation:** Dong et al. (2017) — *Accurate identification of single-nucleotide variants in whole-genome-amplified single cells (SCcaller + SCMDA)* — *Nature Methods*. [DOI](https://doi.org/10.1038/nmeth.4227)

Dong, Zhang, Milholland, Lee, Maslov, Wang and Vijg (Albert Einstein College of Medicine) addressed two compounding sources of false-positive SNVs in scWGS data: (i) cytosine-deamination artefacts from cell lysis at elevated temperatures, and (ii) allelic-amplification bias in MDA. They developed **SCMDA** (single-cell MDA), a low-temperature alkaline-lysis protocol that suppresses cytosine deamination, and **SCcaller**, a general-purpose single-cell variant caller that estimates *local* allelic-amplification bias from heterozygous germline SNPs in a kernel-smoothing window and adjusts SNV likelihoods accordingly.

Validation strategy: compare SCMDA-amplified single cells against unamplified kindred clones from the same population, treating clone variants as truth. SCcaller achieved 90.1% sensitivity at 0.12 FPs per Mb for germline SNP calls — substantially better than HaplotypeCaller (7× more FPs) and Monovar. For somatic SNV calls (variants absent from the clone), SCcaller's FDR (0.308–0.393) is much lower than MuTect (0.745–0.860), VarScan (0.85), and Monovar (similar to MuTect). On MALBAC-amplified single cells, SCcaller's overlap consistency between cells is 2× higher than Monovar.

## Why this matters

A foundational scWGS variant-caller paired with a chemistry improvement (SCMDA). SCcaller is the gold-standard for variant calling in MDA-amplified single cells where matched kindred clones are unavailable; conceptual ancestor of SCAN-SNV (which adds a more refined statistical model) and LiRA (which uses linkage-disequilibrium-based phasing). Anchors §4 (variant-calling tool family) and §3.1 (scWGA chemistry-quality discussion). Important historical context: this is the Vijg-lab paper that established quantitative benchmarking of scWGS variant calling against unamplified clones — the methodological pattern reused in nearly all later scWGS-caller papers.

---
**Source:** [DOI](https://doi.org/10.1038/nmeth.4227) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28319112/)

## Related

- [[10-Summaries/luquette-2019-natcomm]]
- [[10-Summaries/zafar-2016-monovar]]
- [[10-Summaries/lodato-2015-science]]
- [[30-Concepts/sccaller]]
- [[20-Entities/jan-vijg]]
