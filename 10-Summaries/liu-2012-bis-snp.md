---
type: summary
title: "Liu et al. 2012 — Bis-SNP: Combined DNA methylation and SNP calling for Bisulfite-seq data"
source: "[[00-Sources/papers/Bis-SNP_ Combined DNA methylation and SNP calling for Bisulfite-seq data]]"
source_quality: full
source_sha256: "c3ffc974d3a91892762b7343b2a077c12e3b8ea98470f603c2f027bc4a44102b"
source_kind: paper
author: "Yaping Liu, Kimberly D Siegmund, Peter W Laird, Benjamin P Berman (corresponding)"
published: 2012-07-11
ingested: 2026-10-07
doi: "10.1186/gb-2012-13-7-r61"
journal: "Genome Biology 13(7):R61"
tags: [Bis-SNP, bisulfite-sequencing, WGBS, RRBS, SNP-calling, GATK, Bayesian-genotyping, base-quality-recalibration, allele-specific-methylation, C>T-SNP, directional-library, methQTL]
entities: []
concepts: ["[[bisulfite-sequencing]]", "[[allele-specific-methylation]]", "[[read-alignment]]", "[[single-cell-variant-calling]]", "[[cpg-island]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[dna-methylation]]", "[[computational-methods]]"]
---

**Citation:** Liu et al. (2012) — *Bis-SNP: Combined DNA methylation and SNP calling for Bisulfite-seq data* — *Genome Biology* 13(7):R61. [DOI](https://doi.org/10.1186/gb-2012-13-7-r61)

# Liu 2012 — Bis-SNP

> In bisulfite sequencing a C>T change at a cytosine is ambiguous — unmethylated C or real C>T SNP — and C>T is the most common human substitution (65% of dbSNP SNPs, usually in CpG context). Methylation callers that score every reference cytosine therefore mis-measure methylation at polymorphic sites. **Bis-SNP** resolves this by exploiting library **directionality**: reads from the strand opposite a cytosine (the "G-strand") are unaffected by conversion and reveal the true genotype. It adapts GATK's Bayesian genotyper with a strand-aware likelihood that includes methylation level (β), under-conversion (α) and over-conversion (γ), plus a bisulfite-aware base-quality recalibration, and outputs SNPs and methylation together.

## Key claims

- **Better cytosine calling than reference-based callers**: on a 32× WGBS colon mucosa sample (75 bp single-end, Illumina GAIIx) against an Illumina 1M-Duo SNP array, Bis-SNP (locus-specific β + recalibration, default cutoff) recovered **95.22% of 435,120 homozygous cytosines** (414,327) with a false-positive rate of 0.37% (2,461). Bismark — which scores all reference cytosines — and the lab's earlier "Berman2012" method performed worse, as expected on array sites chosen for polymorphism.
- **Heterozygous SNPs**: 93.18% of 303,656 autosomal heterozygous loci (282,944) at 0.094% false positives (755); 79.81% of these were C/T heterozygotes, the hardest class because C-strand reads are uninformative. Bis-SNP beat k-allele read-count methods, the Shoemaker method and bisReadMapper. (The abstract summarises this as 96% of SNPs at ~30×.)
- **Coverage requirements**: at FDR <5%, sensitivity rises steeply up to ~10×; homozygous SNPs reach 98% sensitivity by 10×, heterozygous SNPs 80% at 10× and 95% at 30×.
- **Methylation estimation choice matters**: locus-specific β (C/(C+T) per site) outperformed context-specific and naive (0.5) priors.
- **Recalibration needs a bisulfite trick**: Ts at reference Cs are treated as a fifth base "X" so quality recalibration proceeds for all other substitutions, including G-strand Gs opposite cytosines.
- **Genome-wide sanity check** on chr1 of five WGBS samples (colon, TCGA normal lung and breast, two mouse frontal-cortex methylomes): ~0.5–0.6% of reference CpGs absent in the human sample genomes (~2.5% in F1 mice, attributed to strain differences); homozygous CpGs that are SNPs vs reference had higher methylation (consistent with methylation-driven C>T deamination); CpG/CpH heterozygotes sat halfway; mouse cortex showed elevated CpH methylation.
- **Practical**: ~3 h for chr1 on a 12-core, 10 GB server; ~30–40 h per human genome on one server (or ~3 h with chromosomes in parallel). Works with BAMs from Bismark, BSMAP, MAQ, Novoalign etc., and supports user-defined cytosine contexts (CG/CH, plant CHG/CHH, RRBS CCGG).

## Methods / evidence

Bayesian diploid genotyping per locus over 10 genotypes, priors from dbSNP (incl. 1000 Genomes) as in SOAPsnp; strand-specific likelihood for C/G alleles (eq. 5); score = log odds of best vs next-best genotype. α default 0.25% (estimable from spike-ins or chrM), γ default 0. Additional filters: 5′ non-conversion filter (off for RRBS), SNP-cluster, depth >120, relaxed strand-bias cutoff (−0.02) because bisulfite data show apparent strand bias, QD <1.0. Truth set = SNP array on the same sample; coverage titrated by GATK downsampling.

Weight: a single deeply sequenced human sample with array truth confined to array positions — the authors note the false-positive rates are not genome-wide rates. Comparisons to Bismark are somewhat unfair by design (Bismark does not attempt genotyping). The algorithm is sound and the directional-strand logic is the durable idea.

## Surprising or load-bearing bits

- **The G-strand is the genotype channel**: in a directional library half the reads at any cytosine carry no methylation information but carry the genotype — the key that makes simultaneous SNP + methylation calling possible from one assay.
- **Methylation and mutation are entangled at CpGs**: SNP CpGs being more methylated is a direct readout of methylation-dependent deamination.
- The authors foresee single-assay methQTL and "bisulfite GWAS" designs at ≥50× WGBS — anticipating the later practice of genotyping and phasing from bisulfite reads (synthesis).

## Concepts touched

- [[bisulfite-sequencing]] — formalises the C>T ambiguity and the directional-protocol strand asymmetry.
- [[allele-specific-methylation]] — heterozygous SNPs called from the same reads enable ASM and imprinting analyses without a separate genotyping assay.
- [[read-alignment]] — Bis-SNP sits downstream of bisulfite aligners; it recalculates CIGARs for GATK indel realignment.
- [[single-cell-variant-calling]] — a bulk ancestor of genotype-from-bisulfite-reads logic later used for allele-resolved single-cell methylation (synthesis).

## Connections to other sources

- Built on [[mckenna-2010-gatk]] (GATK LocusWalker, recalibration, realignment); compared against [[krueger-2011-bismark]].
- Descendant single-cell use of within-read SNPs for allele-resolved methylation, from a group including Laird: [[spix-2025-scdeep-mc]] (which notes existing read-backed phasing tools cannot handle bisulfite changes).
- Genotype information inside methylation data, used for lineage/clonal work: [[chen-2025-methyltree]], [[scherer-2025-nature]] (synthesis).

## Open questions

- C/T heterozygotes remain the weakest class; methylation cannot be measured at CpG/TpG heterozygous positions at all.
- Over-conversion (γ) is not measured and defaults to zero; recalibration of the "X" base is not possible without unconverted spike-in DNA.
- Performance at the very low per-cell coverages typical of single-cell bisulfite data is outside the paper's scope (lowest tested 2×) (synthesis).

## Related

- [[bisulfite-sequencing]] · [[allele-specific-methylation]] · [[krueger-2011-bismark]] · [[40-Topics/dna-methylation]]
