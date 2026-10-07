---
type: summary
title: "Luquette 2019 — SCAN-SNV: identification of somatic mutations in single cell DNA-seq using a spatial model of allelic imbalance"
source: "[[00-Sources/papers/Identification of somatic mutations in single cell DNA-seq using a spatial model of allelic imbalance]]"
source_quality: full
source_sha256: "3ea258d879768d30e6b95945b6f1e796371e19df0d4c1725de3337b6371c72f7"
aliases: ["SCAN-SNV", "Luquette 2019"]
tags: [scDNA-seq, computational, variant-calling, allele-balance, MDA]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Luquette et al. (2019) — *SCAN-SNV: identification of somatic mutations in single cell DNA-seq using a spatial model of allelic imbalance* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-019-11857-8)

Luquette and colleagues (Park lab) developed SCAN-SNV, a single-cell somatic SNV caller built around a spatial Bayesian model of allele-specific amplification imbalance. The problem: MDA whole-genome amplification produces non-uniform amplification of homologous alleles, so observed variant-allele frequencies (VAFs) deviate substantially from the expected 50%. Standard bulk callers (MuTect, Strelka, etc.) and even single-cell-aware callers (Monovar, SCcaller) misclassify many MDA artifacts as somatic mutations, inflating false-discovery rates.

SCAN-SNV's central insight is that allele balance (AB) varies smoothly across the genome on the scale of MDA amplicons (~5–10 kb). The method genome-wide infers AB at each position by Gaussian-process regression over phased heterozygous SNPs in the neighborhood, then assesses whether a candidate sSNV's VAF is consistent with its inferred AB. SCAN-SNV simultaneously estimates artifact burden and an upper bound on true somatic mutation count, providing FDR control before genotyping. Benchmarking on synthetic-diploid chrX data built from Lodato 2018 single neurons (with spike-in mutations) and a fibroblast kindred-cell system showed >3-fold reduction in false-discovery rate at similar sensitivity compared to Monovar and SCcaller.

## Why this matters

SCAN-SNV is one of the canonical computational scaffolds for MDA-based single-cell mutation calling. Anchors §4 (computational framework) and the artifact-correction infrastructure that makes the Lodato 2018 / Miller 2022 / Bae 2018 conclusions defensible.

---
**Source:** [DOI](https://doi.org/10.1038/s41467-019-11857-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/31467286/)

---
**Source:** [DOI](https://doi.org/10.1038/s41467-019-11857-8) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/31467286/)

## Related

- [[30-Concepts/scwga-chemistries]]
- [[30-Concepts/single-cell-variant-calling]]
- [[10-Summaries/lodato-2015-science]]
- [[10-Summaries/lodato-2017-aging-neurons]]
