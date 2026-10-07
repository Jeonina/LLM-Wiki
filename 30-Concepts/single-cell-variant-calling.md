---
type: concept
title: Single-cell variant calling
aliases: [scSNV calling, single-cell SNV detection, scDNA variant calling]
tags: [scDNA-seq, variant-calling, SNV, computational]
created: 2026-05-19
updated: 2026-10-07
---

# Single-cell variant calling

> Algorithms for detecting somatic single-nucleotide variants and indels from single-cell DNA sequencing data, which is dominated by amplification artifacts, allelic dropout, and uneven coverage that conventional bulk callers (GATK, MuTect2) handle poorly ([[10-Summaries/valecha-2022-scsnv-review]]; [[10-Summaries/lahnemann-2021-natcomm]]).

## Major tools

- **Monovar** ([[10-Summaries/zafar-2016-monovar]]) — first scSNV caller; multi-cell joint likelihood.
- **SCcaller** ([[10-Summaries/dong-2017-sccaller]]) — local-allele-frequency model.
- **ProSolo** ([[10-Summaries/lahnemann-2021-natcomm]]) — pairs bulk + single-cell.
- **MosaicHunter** ([[10-Summaries/huang-2017-mosaichunter]]) — control-free mosaic SNV detection.
- **MosaicForecast** ([[10-Summaries/dou-2020-mosaicforecast]]) — random-forest classifier.
- **DeepMosaic** ([[10-Summaries/yang-2023-deepmosaic]]) — deep-learning mosaic caller.
- **Monopogen** ([[10-Summaries/dou-2023-monopogen]]) — SNV calls from scRNA/scATAC.
- **SCOUT** ([[10-Summaries/tu-2021-scout-genotyper]]) — leverages local genome territory for genotyping.

## Benchmarks

[[10-Summaries/ha-2023-natmethods]] benchmarks 11 strategies on a constructed reference standard from 6 mixed cell lines.

## The bulk null model these tools reject

- **GATK is the substrate and the assumption.** Its locus-based traversal (all reads spanning each base, plus reference-ordered data) is the data model every single-cell caller inherits; what they replace is its **diploid, uniform-coverage prior**, which WGA violates ([[10-Summaries/mckenna-2010-gatk]]).
- The demonstration genotyper in that paper is explicitly naïve — 99.76% concordance but only 81.70% dbSNP rate against ~90% expected, i.e. an honestly-reported false-positive problem ([[10-Summaries/mckenna-2010-gatk]]).
- **Multi-locus traversals were never implemented** in the original framework and were flagged as memory-expensive — which is why haplotype-aware and phasing-based methods needed separate engineering rather than a walker ([[10-Summaries/mckenna-2010-gatk]]).
- **LOH detection reuses the same logic in reverse**: restrict to ancestral heterozygous sites, then read allele fraction, calling tracts from ≥3 consecutive deviating SNPs ([[10-Summaries/smukowski-heil-2023-loh]]). In single cells this collides with allele dropout, which produces the identical signature.
- **Clone-level aggregation is the amplification-free alternative** to per-cell calling: cluster on copy number, treat each clone as pseudo-bulk, then call SNVs, breakpoints and allele-specific copy number per clone ([[10-Summaries/laks-2019-dlp-plus]]).

## Added 2026-10-07

A 2020 community review classifies scDNA WGA failures into imbalanced allele proportions, allele dropout and complete site dropout ([[10-Summaries/lahnemann-2020-grand-challenges]]). It argues that because somatic evolution is asexual and recombination-free, the shared cell lineage tree can serve as a constraint for joint variant calling, and in 2020 knew of no scDNA-seq indel caller and no systematic comparison of SNV or CNV callers ([[10-Summaries/lahnemann-2020-grand-challenges]]).

SComatic calls somatic SNVs de novo from scRNA-seq and scATAC-seq without matched DNA by pooling reads per cell type, testing against a beta-binomial background error model fitted on non-neoplastic samples, and discarding variants seen in more than one cell type as germline or artefact ([[10-Summaries/muyas-2024-scomatic]]). Against DNA-confirmed mutations in 30 tumours its precision was 0.67–0.87 versus 0.06–0.24 for Strelka2, the next best, although Strelka2, VarScan2 and SCReadCounts had higher sensitivity ([[10-Summaries/muyas-2024-scomatic]]).

SCAN2 adds a mutation-signature rescue step to SCAN-SNV's allele-balance model and the first single-cell somatic indel caller: on synthetic diploid X data it raised sSNV sensitivity from 25% to 46% at similar FDR, and recovered 33.6% of spiked indels at <2% FDR where GATK HaplotypeCaller+VQSR had >99% FDR [[10-Summaries/luquette-2022-neuron-scan2-indels]]. LiRA earlier validated singleton sSNVs by read-backed phasing with nearby germline heterozygous SNPs, filtering 92% of phaseable MDA candidates as artifacts versus 2% of germline–germline pairs [[10-Summaries/bohrson-2019-lira]].

VarScan is an early, aligner-agnostic bulk caller built on read-level filters and simple thresholds (coverage, base quality, supporting reads, variant frequency). It reports per-allele read counts rather than diploid genotypes, which let it detect ~1%-frequency SNPs in a ~6,000× pooled sample ([[10-Summaries/koboldt-2009-varscan]]). Pooled allele-frequency estimates correlated with known frequencies at r = 0.962, but high-VAF variants were slightly underestimated because variant-carrying short reads map less well ([[10-Summaries/koboldt-2009-varscan]]).

**Calling through the tree.** SIEVE calls single and double mutant genotypes from raw four-nucleotide counts conditional on an inferred cell phylogeny, with single-mutant recall 0.16–18.55% above SCIPhI and 28.89–71.74% above Monovar in simulations ([[10-Summaries/kang-2022-sieve]]). **Bulk reference point:** MuTect's free-allele-fraction Bayesian test plus artifact filters and panel of normals reached 95.6% sensitivity at 30× for AF 0.2, but assumes a matched normal and independent sequencing errors ([[10-Summaries/cibulskis-2013-mutect]]).

Downstream tree inference can use genotype likelihoods instead of hard calls. CellPhy reads the VCF PL field, and doing so improved accuracy most at low (5×) depth. The PL field means different things in different callers: SC-Caller's must be converted before use, while Monovar writes a standard PL ([[10-Summaries/kozlov-2022-cellphy]]). A chemistry-side alternative is to require the variant on both complementary strands. META-CS does this, calls SNVs from ≥4 reads (≥2 per strand), and does not depend on heterozygous germline SNPs, so it also works in haploid or aneuploid cells ([[10-Summaries/xing-2021-meta-cs]]).

Sparse droplet genome libraries genotype almost no cells per variant: untargeted SPLONGGET covered 0.01% of cells on average at known B-ALL driver sites ([[10-Summaries/pancikova-2025-splongget]]). Re-amplifying the same barcoded libraries with biotinylated multiplex PCR raised on-target coverage 3,242-fold (DNA) and 4,402-fold (cDNA), and on average 18.4% of cells (range 0–75.1%) could then be genotyped. Targeted VAFs correlated with MissionBio Tapestri at PCC 0.92 ([[10-Summaries/pancikova-2025-splongget]]).

## Related

- [[40-Topics/scdna-seq]] · [[40-Topics/mosaic-variant-calling]] · [[40-Topics/duplex-sequencing]]
- [[40-Topics/scdna-seq]] · [[40-Topics/mosaic-variant-calling]]
- [[10-Summaries/mckenna-2010-gatk]] · [[10-Summaries/smukowski-heil-2023-loh]] · [[10-Summaries/laks-2019-dlp-plus]]

## Added 2026-08-13

SCAN2 extends the SCAN line from SNVs to **indels** and is matched to [[30-Concepts/pta|PTA]] rather than MDA ([[10-Summaries/luquette-2022-neuron-scan2-indels]]). The consequence is not just a new variant class but a revised biological constant: neuronal somatic SNV accumulation drops to **16.5 SNVs/year**, with the revision attributed to artifacts in the older amplification chemistries ([[10-Summaries/luquette-2022-neuron-scan2-indels]]). Somatic indels accumulate at ~3/year per neuron and are enriched in conserved sequence and neuronal enhancers ([[10-Summaries/luquette-2022-neuron-scan2-indels]]).

Indels were effectively unmeasurable before PTA because MDA's polymerase-slippage artifacts sit on top of the indel signal — getting a rate at all is a chemistry result as much as an algorithm result. (synthesis)

**Validation is the recurring weak point.** Duplex sequencing of nuc-seq calls found that only **19.4–27.0% of single-cell-only ("de novo") mutations validated**, against 90.5–64.8% of subclonal and 94.4–99.7% of clonal calls ([[10-Summaries/wang-2014-nuc-seq]]). Read the other way: the majority of single-cell-only calls are artifact even in a high-quality library — which is why the field converged on orthogonal duplex confirmation ([[50-Notes/single-cell-duplex-sequencing]]). (synthesis)

The abundance-inversion problem these callers negotiate — where an artifact in a well-amplified region outweighs a true signal in a poorly-amplified one — was first named a decade earlier in [[30-Concepts/single-cell-genome-assembly|single-cell assembly]] ([[10-Summaries/peng-2012-idba-ud]]). (synthesis)
