---
type: summary
title: "Luquette 2019 — SCAN-SNV: identification of somatic mutations in single cell DNA-seq using a spatial model of allelic imbalance"
aliases: ["SCAN-SNV", "Luquette 2019"]
tags: [scDNA-seq, computational, variant-calling, allele-balance, MDA]
created: 2026-05-13
updated: 2026-05-13
sources: ["Lovelace_2019_NatureCommunications.pdf"]
---

Luquette and colleagues (Park lab) developed SCAN-SNV, a single-cell somatic SNV caller built around a spatial Bayesian model of allele-specific amplification imbalance. The problem: MDA whole-genome amplification produces non-uniform amplification of homologous alleles, so observed variant-allele frequencies (VAFs) deviate substantially from the expected 50%. Standard bulk callers (MuTect, Strelka, etc.) and even single-cell-aware callers (Monovar, SCcaller) misclassify many MDA artifacts as somatic mutations, inflating false-discovery rates.

SCAN-SNV's central insight is that allele balance (AB) varies smoothly across the genome on the scale of MDA amplicons (~5–10 kb). The method genome-wide infers AB at each position by Gaussian-process regression over phased heterozygous SNPs in the neighborhood, then assesses whether a candidate sSNV's VAF is consistent with its inferred AB. SCAN-SNV simultaneously estimates artifact burden and an upper bound on true somatic mutation count, providing FDR control before genotyping. Benchmarking on Lodato-2015-style single-neuron data showed >3-fold reduction in false-discovery rate at similar sensitivity compared to Monovar and SCcaller.

## Why this matters

SCAN-SNV is one of the canonical computational scaffolds for MDA-based single-cell mutation calling. Anchors §4 (computational framework) and the artifact-correction infrastructure that makes the Lodato 2018 / Miller 2022 / Bae 2018 conclusions defensible.

## Related

- [[30-Concepts/scwga-chemistries]]
- [[30-Concepts/single-cell-variant-calling]]
- [[10-Summaries/lodato-2015-science]]
- [[10-Summaries/lodato-2018-science]]
