---
type: summary
title: "Zafar 2016 — Monovar: single-nucleotide variant detection in single cells"
aliases: ["Zafar 2016 Monovar", "Monovar"]
tags: [Monovar, scDNA-SNV-calling, allelic-dropout, multi-cell-pooled, Nakhleh-lab, Navin-lab, founding-tool]
created: 2026-05-13
updated: 2026-05-13
sources: ["Hamim_2016_NatureMethods.pdf"]
---

**Citation:** Zafar et al. (2016) — *Monovar: single-nucleotide variant detection in single cells* — *Nature Methods*. [DOI](https://doi.org/10.1038/nmeth.3835)

Zafar, Wang, Nakhleh, Navin and Chen (Rice, MD Anderson, BCM) developed **Monovar**, the first statistical method specifically for detecting SNVs from scDNA-seq data. Monovar leverages multi-cell data to discover SNVs with high confidence and explicitly models the dominant scWGA error modes: allelic dropout (ADO), false-positive errors from amplification artefacts, and non-uniform coverage.

Algorithm: for each locus, observed bases and base-quality scores from multiple single cells form the input. A dynamic-programming algorithm computes the posterior probability of the locus carrying a variant, modeling FP rates specific to WGA and explicit ADO terms for heterozygous-genotype likelihoods. After detection, per-cell genotyping derives the posterior probability; an optional consensus filter removes singleton-cell variants.

Benchmarked against GATK HaplotypeCaller, Samtools, SOAPsnp, SNVMix2, and Varscan2 (all bulk-designed) on simulated and real scDNA-seq data. Monovar achieved substantially higher precision (0.8376 vs ~0.6) and reduced C>G:T>A FP transitions (the dominant WGA artefact class). Applied to TNBC, bladder cancer, and pediatric ALL single-cell exome data, Monovar identified driver mutations and delineated clonal substructure that bulk-designed callers missed.

## Why this matters

Founding paper for scDNA-seq variant calling. Direct predecessor of SCcaller (Dong 2017, adds local-bias modeling), SCAN-SNV (more refined statistical model), LiRA (Luquette 2019, adds linkage-disequilibrium phasing), and Monopogen (Dou 2024, generalizes to any modality). Existing `zafar2016` bibkey already present. Anchors §4 (variant-calling tool family — Monovar is the canonical first reference).

---
**Source:** [DOI](https://doi.org/10.1038/nmeth.3835) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/27088313/)

## Related

- [[10-Summaries/dong-2017-sccaller]]
- [[10-Summaries/luquette-2019-natcomm]]
- [[10-Summaries/dou-2023-monopogen]]
- [[10-Summaries/zafar-2017-sifit]]
- [[20-Entities/nicholas-navin]]
- [[30-Concepts/monovar]]
