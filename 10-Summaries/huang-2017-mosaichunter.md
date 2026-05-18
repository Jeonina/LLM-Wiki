---
type: summary
title: "Huang 2017 — MosaicHunter: accurate detection of postzygotic single-nucleotide mosaicism through next-generation sequencing of unpaired, trio, and paired samples"
source: "[[00-Sources/papers/MosaicHunter_ accurate detection of postzygotic single-nucleotide mosaicism through next-generation sequencing of unpaired, trio, and paired samples]]"
aliases: ["Huang 2017 MosaicHunter", "MosaicHunter", "August Yue Huang"]
tags: [MosaicHunter, mosaic-variant-calling, Bayesian-genotyper, unpaired-detection, Wei-lab, PKU, founding-method]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/MosaicHunter_ accurate detection of postzygotic single-nucleotide mosaicism through next-generation sequencing of unpaired, trio, and paired samples]]"
---

**Citation:** Huang et al. (2017) — *MosaicHunter: accurate detection of postzygotic single-nucleotide mosaicism through next-generation sequencing of unpaired, trio, and paired samples* — *NucleicAcidsResearch*. [DOI](https://doi.org/10.1093/nar/gkx024)

Huang, Zhang, Ye, Dou, Yan, Yang, Zhang and Wei (Peking University, Tsinghua) developed **MosaicHunter**, a Bayesian bioinformatics framework for detecting postzygotic single-nucleotide mosaicisms (SNMs) from unpaired NGS data — i.e., without a matched control tissue. The Bayesian genotyper computes posterior probabilities over four states (mosaic, reference-homozygous, heterozygous, alternative-homozygous) by integrating base-calling error rates, random sampling variation, and dbSNP population allele frequencies, then applies a series of stringent error filters to remove systematic NGS artefacts.

Three operating modes: (i) **single mode** for unpaired WGS (binomial model); (ii) **single mode for WES** (new beta-binomial model handling over-dispersion in exome alternative-allele fractions); (iii) **trio mode** that incorporates parental sequencing to improve specificity in healthy parents of affected children; (iv) **paired mode** for matched-tumor-normal cancer samples. Validated on simulated and real WGS/WES data against existing somatic-mutation callers, showing improved precision particularly in non-cancer settings where mutation rates are 1-3 orders of magnitude lower than tumors.

## Why this matters

The founding paper for unpaired mosaic-SNM calling — the methodological ancestor of MosaicForecast (Dou 2020), DeepMosaic (Yang 2023), and the M2SMH meta-strategy (Ha 2023). MosaicHunter remains the recommended caller for very-low-VAF mosaic variants (<5%) per Ha 2023 benchmark. Anchors §4 (mosaic-caller family) and §5 (brain-somatic-mosaicism applications — used extensively in BSMN cohorts). Important authorship note: Yanmei Dou and Xiaoxu Yang are co-authors here and later first-authored MosaicForecast and DeepMosaic respectively — the Wei/Park/Gleeson labs cluster around this lineage.

---
**Source:** [DOI](https://doi.org/10.1093/nar/gkx024) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28132024/)

---
**Source:** [DOI](https://doi.org/10.1093/nar/gkx024) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28132024/)

## Related

- [[10-Summaries/dou-2020-mosaicforecast]]
- [[10-Summaries/yang-2023-deepmosaic]]
- [[10-Summaries/ha-2023-natmethods]]
- [[40-Topics/mosaic-variant-calling]]
