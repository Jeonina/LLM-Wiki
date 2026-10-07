---
type: summary
title: "Cibulskis et al. 2013 — Sensitive detection of somatic point mutations in impure and heterogeneous cancer samples"
source: "[[00-Sources/papers/Sensitive detection of somatic point mutations in impure and heterogeneous cancer samples]]"
source_quality: full
source_sha256: "b9960883f4a34385a96991bd064c671be328e8d3e9b45de7ad37f62f621ca6a5"
source_kind: paper
author: "Kristian Cibulskis, Michael S Lawrence, Scott L Carter, Andrey Sivachenko, David Jaffe, Carrie Sougnez, Stacey Gabriel, Matthew Meyerson, Eric S Lander, Gad Getz"
published: 2013-02-10
ingested: 2026-10-07
doi: "10.1038/nbt.2514"
journal: "Nature Biotechnology 31(3):213–219"
tags: [MuTect, somatic-SNV-calling, tumor-normal, allele-fraction, subclonal-mutations, Bayesian-classifier, panel-of-normals, virtual-tumor-benchmark, ContEst, bulk-sequencing]
entities: []
concepts: ["[[30-Concepts/single-cell-variant-calling]]", "[[30-Concepts/intratumor-heterogeneity]]", "[[30-Concepts/sequencing-depth-and-coverage]]", "[[30-Concepts/post-zygotic-variation]]", "[[30-Concepts/duplicate-marking]]"]
topics: ["[[40-Topics/mosaic-variant-calling]]", "[[40-Topics/cancer-clonal-evolution]]", "[[40-Topics/computational-methods]]"]
---

**Citation:** Cibulskis et al. (2013) — *Sensitive detection of somatic point mutations in impure and heterogeneous cancer samples* — *Nature Biotechnology* 31:213–219. [DOI](https://doi.org/10.1038/nbt.2514)

# Cibulskis 2013 — MuTect

> MuTect is the Broad Institute's tumor–normal somatic SNV caller, designed for the subclonal and impure-tumor regime that callers assuming a pure diploid tumor (fixed 50% allele fraction) miss. Its core is a per-site **Bayesian likelihood-ratio test with a free allele fraction *f***, followed by six hand-tuned **artifact filters**, a **panel-of-normals** filter, and a second classifier that labels calls somatic vs germline using matched-normal depth and dbSNP priors. Equally important is the paper's **benchmarking method**: "virtual tumors" built by splitting and spiking real sequencing data, so sensitivity *and* specificity can be measured on real error profiles as a function of depth and allele fraction.

## Key claims

- **Free allele fraction is the sensitivity lever.** Modelling *f* explicitly, instead of a heterozygous diploid event, is what the authors credit for higher sensitivity than SomaticSniper and JointSNVMix (both assume fixed 50% AF). Strelka also models AF and matches MuTect in standard mode, but loses more sensitivity in its high-confidence mode.
- **Detection threshold**: LOD_T > 6.3, chosen from a prior mutation frequency of 3 × 10⁻⁶ (tumours often carry 1–10 mutations/Mb, so prior odds of a mutated site are ~1:10⁵–10⁶). The LOD accurately predicts sensitivity but **underestimates false positives**, because it assumes independent errors and correct read placement — hence the filters.
- **Sensitivity (30× tumour)**: 95.6% at AF 0.2; 99.9% at 50×; 58.9% at AF 0.1. At 150× (exome) 66.4% for AF 0.03. Three benchmarking routes — analytic calculation, downsampling 3,753 validated colorectal-cancer mutations (median AF 0.28), and virtual tumours — agreed (median CV 3.1%).
- **Specificity**: unfiltered false positives rise with depth (6.7/Mb at 5× to 20.1/Mb at 30×, because more power to call low-AF events, which are enriched for artefacts); the six HC filters cut this ~10-fold to 1.00/Mb at 30×; adding a panel of normals (125 blood normals) gives 0.51/Mb. Germline misclassification falls from 2.4 × 10⁻³ at 8× normal coverage to <0.2 × 10⁻³ at 12×; with ≤7 normal reads (novel sites) or ≤18 (dbSNP sites) MuTect refuses to classify.
- **Head-to-head at 30×, AF 0.1 (HC modes)**: MuTect 53.2%, Strelka 29.7%, JointSNVMix 16.8%, SomaticSniper 7.4%. At AF 0.05: MuTect 16.0% (51.9% at 60×); JointSNVMix and SomaticSniper ≤2.0%; Strelka 4.6% (20.8% at 60×). False positive rates were matched across methods (HC median 1.0/Mb above 20×).
- **Real-world validation**: ~95% validation rate in coding regions across prior studies; median false positive rate 0.16/Mb in coding regions (lower than whole-genome, because coding regions are less error-prone). A 7% AF mutation (8 of 102 reads) was validated by ~6,000× sequencing.
- **Contamination**: even 2% cross-individual DNA contamination can produce 166 false positives/Mb (10/Mb excluding known SNPs); MuTect replaces the null model with a contamination-fraction model (from ContEst).

## Methods / evidence

Inputs are preprocessed tumour and matched-normal BAMs (duplicate marking, base-quality recalibration, local realignment). Per-site: quality filtering → variant LOD → six filters (e.g., poor mapping, proximal gap, clustered position, among others in Table 1) → panel-of-normals → somatic/germline LOD (δ_N threshold 10, f fixed at 0.5 for germline heterozygote, dbSNP-informed priors). Virtual tumours: NA12878 data from three ~30× libraries split into 18 ~5× partitions; tumour and normal drawn from different libraries (all calls = false positives); sensitivity by **SomaticSpike**, which replaces NA12878 reads with NA12891 reads at sites heterozygous in NA12891 and reference in NA12878, across 1 Gb. Comparators: SomaticSniper v1.0.0, JointSNVMix v0.7.5, Strelka 0.4.7, thresholds set for similar false-positive rates; also COLO-829 melanoma (pure, AF median 0.55 — does not discriminate methods).

Weight: the benchmarking framework is the durable contribution; numbers are tied to 2013 Illumina HiSeq error profiles and to filter thresholds tuned by the same group. Virtual tumours simulate somatic events with germline variants, which differ in substitution spectrum and context (authors acknowledge; differences in sensitivity "minimal").

## Surprising or load-bearing bits

- **Calling absence is a feature.** Because sensitivity can be computed per base from depth and quality, MuTect can assert that a mutation of a given AF is *absent* — the basis for power-aware mutation-rate estimates and clinical negatives.
- **Deeper is not automatically cleaner**: raw false positives grow with depth because the caller gains power to call low-AF noise. Filters matter more as depth rises.
- **Panel of normals** turns recurrent, platform- or site-specific artefacts into a learnable blacklist — later reused widely in mosaic-variant pipelines. (synthesis)
- **Bulk-only design.** MuTect assumes a matched normal and independent sequencing errors; single-cell WGA errors are correlated within amplicons and allelic dropout is extreme, which is why scDNA work built dedicated callers. (synthesis)

## Concepts touched

- [[single-cell-variant-calling]] — MuTect/MuTect2 are the bulk reference point that single-cell callers are contrasted against.
- [[intratumor-heterogeneity]] — sensitivity to subclonal (low-AF) mutations is the design goal.
- [[sequencing-depth-and-coverage]] — explicit sensitivity curves vs depth and AF for experiment design.
- [[post-zygotic-variation]] — the low-AF problem is shared with mosaic variant detection in normal tissue (synthesis).

## Connections to other sources

- Preprocessing it assumes: [[mckenna-2010-gatk]], [[li-2009-bwa]], [[li-2009-samtools]].
- Mosaic callers that benchmark against or build on MuTect-class callers: [[ha-2023-natmethods]] (MuTect2 among 11 strategies), [[dou-2020-mosaicforecast]], [[huang-2017-mosaichunter]], [[yang-2023-deepmosaic]].
- Single-cell callers designed because bulk callers fail on WGA data: [[luquette-2019-natcomm]], [[dong-2017-sccaller]], [[zafar-2016-monovar]].
- Error-corrected sequencing that attacks the same low-AF floor chemically rather than statistically: [[abascal-2021-nanoseq]], [[kennedy-2014-duplex-protocol]] (synthesis).

## Open questions

- Filter thresholds are empirical; how well do they transfer to other platforms and to normal-tissue mosaicism with no matched "normal"?
- Virtual tumours use germline substitution spectra; tumour-specific contexts (e.g., APOBEC) may change sensitivity.
- Indels and rearrangements are left to future extension.

## Related

- [[40-Topics/mosaic-variant-calling]] · [[ha-2023-natmethods]] · [[mckenna-2010-gatk]] · [[single-cell-variant-calling]]
