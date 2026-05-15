---
type: summary
title: "Zafar 2016 — Monovar: single-nucleotide variant detection in single cells"
aliases: ["Monovar", "Zafar 2016"]
tags: [computational, variant-calling, single-cell, Monovar, Navin-lab, Nakhleh-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Hamim_2016_NatureMethods.pdf"]
---

**Citation:** Zafar et al. (2016) — *Monovar: single-nucleotide variant detection in single cells* — *Nature Methods*. [DOI](https://doi.org/10.1038/nmeth.3835)

Zafar, Wang, Nakhleh, Navin and Chen developed Monovar, one of the first SNV callers built specifically for single-cell DNA sequencing. The method addresses three scDNA-seq artifact classes that confound bulk callers (GATK, Samtools, VarScan2): non-uniform coverage, allelic dropout, and false-positive errors from MDA polymerase. Monovar models genotype likelihoods across multiple single cells jointly, computing per-locus posterior probabilities under a dynamic-programming framework that accounts for allelic dropout and per-cell false-positive rates.

Validation on simulated and real data showed Monovar substantially outperforming GATK HaplotypeCaller and Samtools on a normal isogenic fibroblast control (precision 0.84 vs 0.66 and 0.58 respectively) and on tumor samples from TNBC, bladder cancer, and ALL patients. Monovar was particularly effective at reducing the spurious C:G→A:T transversion rate characteristic of MDA artifacts.

## Why this matters

The first single-cell-aware variant caller and the methodological reference against which SCAN-SNV (Luquette 2019), SCcaller, ProSolo (Lähnemann 2021), and LiRA (Lodato 2018) were subsequently benchmarked. Anchors §4 (computational framework) and provides the historical context for why specialized scDNA-seq callers exist.

---
**Source:** [DOI](https://doi.org/10.1038/nmeth.3835) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/27088313/)

## Related

- [[10-Summaries/luquette-2019-natcomm]]
- [[10-Summaries/lahnemann-2021-natcomm]]
- [[30-Concepts/single-cell-variant-calling]]
- [[20-Entities/nicholas-navin]]
