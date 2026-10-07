---
type: summary
title: "Gonzalez-Pena 2021 — Accurate genomic variant detection in single cells with primary template-directed amplification (PTA)"
source: "[[00-Sources/papers/Accurate genomic variant detection in single cells with primary template-directed amplification.pdf]]"
source_quality: full
source_sha256: "29274afb730fcd75076d8a749f5aa05a57eed2275fd24fe7de7d503347a4a7be"
source_kind: paper
author: "Veronica Gonzalez-Pena, Sivaraman Natarajan (co-first), Yuntao Xia, David Klein, Robert Carter, Yakun Pang, Bridget Shaner, Kavya Annu, Daniel Putnam, Wenan Chen, Jon Connelly, Shondra Pruett-Miller, Xiang Chen, John Easton, Charles Gawad (corresponding)"
published: 2021-06-07
ingested: 2026-05-13
doi: "10.1073/pnas.2024176118"
journal: "PNAS 118(24):e2024176118"
aliases: ["PTA", "Gonzalez-Pena 2021", "Primary template-directed amplification", "DMEM"]
tags: [scWGA, PTA, single-cell, mutation-detection, Gawad-lab, DMEM, mutagenesis, CRISPR-off-target, structural-variants, BioSkryb]
entities: ["[[charles-gawad]]", "[[christopher-walsh]]"]
concepts: ["[[pta]]", "[[mda]]", "[[scwga]]", "[[scwga-chemistries]]", "[[single-cell-variant-calling]]", "[[allele-dropout]]", "[[mutational-signatures]]", "[[copy-number-variation]]", "[[structural-variants]]", "[[malbac]]", "[[dop-pcr]]", "[[quality-control-metrics]]"]
topics: ["[[whole-genome-amplification]]", "[[scdna-seq]]", "[[somatic-mosaicism]]", "[[mosaic-variant-calling]]"]
created: 2026-05-13
updated: 2026-10-07
---

**Citation:** Gonzalez-Pena et al. (2021) — *Accurate genomic variant detection in single cells with primary template-directed amplification* — *PNAS* 118(24):e2024176118. [DOI](https://doi.org/10.1073/pnas.2024176118) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34099548/)

# Gonzalez-Pena 2021 — PTA

> PTA keeps the phi29 polymerase of MDA (processive, strand-displacing, low error) but adds **exonuclease-resistant alpha-thio dideoxynucleotide terminators** to the reaction. Extension stops early, amplicons stay short, and most copies are made from the original template rather than from daughter amplicons, so MDA's exponential, error-propagating reaction becomes "a quasilinear process". On GM12878 cells against six other WGA methods, PTA gave the highest genome coverage breadth, the most uniform coverage (CV, Lorenz, Gini), the least allelic skew and the best SNV sensitivity and precision. The paper then uses PTA for two new assays: **DMEM** (direct measurement of environmental mutagenicity: genome-wide mutation maps of single human cells exposed to a mutagen) and single-cell detection of **CRISPR off-target indels and structural variants**. Senior author Charles Gawad is a co-founder of BioSkryb Genomics, which commercialises PTA.

## Key claims

- **Irreversible terminators are what make it work.** Standard ddNTPs shortened amplicons but gave poor products (reads mapped 15.0 ± 2.2%, mapping quality 0.8 ± 0.08), which the authors attribute to the polymerase removing the terminator and re-priming, producing chimeras. Switching to alpha-thio ddNTPs, which form an exonuclease-resistant phosphorothioate bond, raised mapping "from 15.0 ± 2% to 97.9 ± 0.62%" and mapping quality "from 0.8 ± 0.08 to 46.3 ± 3.18". No-template controls gave no detectable product, unlike MDA, where NTCs yield as much as single cells (Fig. 1B).
- **Coverage breadth and uniformity.** PTA and an improved single-cell MDA (SCMDA) were run on 10 GM12878 cells each and compared, at matched subsampling (300 M reads), with DOP-PCR, GE MDA, Qiagen MDA, MALBAC, LIANTI and PicoPLEX data from the LIANTI study (BJ1 fibroblasts, n = 3–11). PTA "approaches the two bulk samples at every sequencing depth" and had the lowest CV, the Lorenz curve closest to bulk and the lowest, most reproducible Gini index. PTA, LIANTI and SCMDA had similar GC content; PCR duplication rates were similar across methods. PTA also amplified small circular templates such as mtDNA relatively more.
- **SNV sensitivity.** Against bulk subsampled to 650 M reads, PTA detected "greater than 90% of variants compared 65 to 70% of variants detected with LIANTI, which was the next most sensitive method". PTA had "significantly diminished allele dropout and skewing" at bulk-heterozygous sites, while LIANTI's allelic skew resembled MDA's despite its even coverage.
- **SNV precision.** Discordant calls (absent from bulk) were lowest for PTA. Methods using thermostable polymerases (MALBAC, PicoPLEX, DOP-PCR) lost precision as depth increased, and their false-positive base-change spectra were polymerase-dependent. PTA kept the best sensitivity–precision trade-off across GATK4, Monovar and SCcaller; GATK4 and Monovar performed similarly on PTA data, and SCcaller had the lowest sensitivity and precision.
- **Commercial-kit comparison with a low-temperature lysis.** On five primary leukemia samples, a PTA version with low-temperature lysis (to suppress heat-induced cytosine deamination) was compared with Ampli1, PicoPLEX Gold, GenomiPhi, TruePrime and the newer REPLI-g. PTA remained the most sensitive SNV method at all depths with the highest precision, and had the lowest CV and MAPD in CNV bins except MAPD at large bins vs Ampli1.
- **CNV in the same cells.** In a leukemia with known gains and a deletion on chromosomes 8, 10 and 12, all single cells showed them. Bulk only suggested a chromosome 21 gain; "Three of the eight single cells were indeed found to have a gain of chromosome 21", which the authors read as single-cell CNV profiling being more sensitive for subclonal changes.
- **Kindred-cell design separates false positives from somatic mutations.** Single CD34+ cord-blood cells were expanded 5 days, then sister cells were re-isolated and amplified. A variant in bulk = germline; in bulk but no cell = dropout; in one cell only = false positive; in several cells but not bulk = somatic. Germline precision with low-temperature lysis rose to **99.9%**, which still corresponded to "a mean of 2,785 false positive variant calls across the genome". False positives were mostly heterozygous at low allele frequency; homozygous false positives clustered near centromeres and telomeres.
- **Per-cell somatic rate.** Filtering to DP ≥ 10, GQ ≥ 20 and allele frequency ≥ 0.35 and correcting for genome-wide sensitivity gave "0.33 ± 0.02 per Mb or about 1,000 somatic SNVs per hematopoietic stem cell genome". The authors flag this as possibly an overestimate.
- **DMEM.** CD34+ cord-blood cells were exposed for 48 h to ENU (8.54, 85.4, 854 µM) or D-mannitol (1,152.8 and 11,528 µM, negative control). Mutation counts rose with ENU dose; the lowest ENU dose resembled vehicle and toxic mannitol. The most common changes were T>A, T>C and C>T, matching mouse ENU data rather than *E. coli*. C>G changes were rare, and cytosine variants were not enriched in Roadmap DNase I hypersensitive sites. SigProfiler matched the ENU signature to COSMIC **SBS5 (76.6%) and SBS51 (23.4%)**, but the reconstruction missed an excess of C>G and a deficit of T>A, so the ENU signature is not fully captured by COSMIC.
- **CRISPR off-target editing at single-cell resolution.** U2OS, CD34+ cord-blood cells and H9 ES cells were edited with EMX1 (precise) or VEGFA (promiscuous) gRNAs; calling was restricted to sites with a PAM and up to five protospacer mismatches. VEGFA cells had more indels "with wide cell-to-cell variance", EMX1 very few. Most presumed false-positive edits in control cells were single-base insertions; removing non-recurrent ones improved precision. Targeted deep sequencing of ES-cell PTA product validated five VEGFA off-target events. Most recurrent off-target sites, indel and SV, were **cell-type specific**, and ES cells carried more SVs.

## Methods / evidence

Single cells were FACS-sorted (Calcein AM+, PI−) into 3 µl PBS. PTA lysis used Triton X-100 plus proteinase K; the amplification mix (REPLI-g Single Cell reagents) contained alpha-thio-ddNTPs at 1,200 µM, run at 30 °C for 8 h. Libraries were KAPA HyperPlus with 400–700 bp size selection, sequenced on NovaSeq 6000. Analysis: Trimmomatic, GATK 4.1 best practices on GRCh38, HaplotypeCaller with VQSR tranche 99.0 (99.9 for DMEM, 90.0 for CRISPR indels), Ginkgo for CNV at 1 Mb bins, svABA for SVs, Cas-OFFinder for candidate off-target sites, SigProfiler for signatures. The kindred-cell and DMEM experiments use sister cells and the bulk as internal truth sets. Data: SRA PRJNA514916; code in the Gawad lab GitHub.

Weight: a strong, multi-angle benchmark with an internal truth set (kindred cells) that most WGA comparisons lack. But the first-round comparators were re-used data from the LIANTI study on a different cell line (BJ1) with different upstream screening, and PTA was developed by the reporting lab, whose senior author co-founded the company commercialising it. Applications (DMEM, CRISPR) are proof-of-concept with small cell numbers (n = 4–6 per condition). (synthesis)

## Limitations

**Authors' own:**
- Discordance with bulk cannot tell false positives from true somatic variants; the kindred-cell design was added to address this.
- The 0.33 SNV/Mb somatic rate "may still be an overestimate", because the filters were less stringent than in other newborn-cell estimates.
- Even at 99.9% germline precision, thousands of false positives per cell remain; variant callers need PTA-specific artifact models (the authors point to SCAN2), plus mobile-element detection.
- One kindred cell had much lower sensitivity, possibly from manual handling of fragile primary cells; heterozygous false positives may come from tetraploid S/G2M cells.
- Indels are hard to call, WGA chimeras can produce false SV calls, and whether ES cells are more prone to CRISPR-induced SVs needs more study.

**Reviewer notes:**
- The headline "> 95% of the genome" and the matched-depth benchmark rely on ~600 M reads (~30×) per cell; sensitivity at the shallower depths typical of cohort studies is shown only on curves. (synthesis)
- The DMEM dose–response rests on n = 4–5 cells per dose, and the lowest ENU dose was indistinguishable from controls, so the assay's floor for weak mutagens is not established. (synthesis)
- Nothing here tests PTA in post-mitotic cells such as neurons, where the kindred-cell control is impossible; that was left to later work. (synthesis)

## Surprising or load-bearing bits

- **PTA does not remove the need for artifact-aware calling.** The paper itself reports ~2,785 false-positive calls per cell at 99.9% germline precision and calls for PTA-specific callers. Claims that PTA made "direct SNV calling without correction" feasible go beyond this source. (synthesis)
- **Uniform coverage is not the same as allelic balance.** LIANTI was even across the genome yet skewed between alleles like MDA. PTA's gain is mainly at the allele level, and that is what drives its SNV sensitivity.
- **The thermostable-polymerase penalty.** Precision of MALBAC, PicoPLEX and DOP-PCR falls as depth rises, because their polymerase errors accumulate; phi29-based methods do not show this.
- **ENU in human cells ≠ COSMIC.** The ENU signature is mostly SBS5-like with an SBS51 component, but the residual C>G excess shows single-cell exposure assays can find signature features that tumour-derived catalogues miss.
- **Off-target editing is cell-type specific**, so gRNA safety should be assessed in the target cell type.

## Entities mentioned

- [[charles-gawad]] — senior and corresponding author; co-founder of BioSkryb Genomics.
- [[christopher-walsh]] — handling editor at PNAS.

## Concepts touched

- [[pta]] / [[scwga]] — the source paper for the chemistry: alpha-thio ddNTP terminators, 30 °C isothermal reaction, quasilinear amplification.
- [[mda]] / [[malbac]] / [[dop-pcr]] / [[scwga-chemistries]] — benchmarked comparators; thermostable-polymerase methods lose precision with depth.
- [[single-cell-variant-calling]] — GATK4, Monovar and SCcaller compared on PTA data; kindred-cell truth set.
- [[allele-dropout]] — PTA's main gain over LIANTI and MDA is reduced dropout and allelic skew.
- [[mutational-signatures]] — ENU signature deconvolved into SBS5 + SBS51 with a residual C>G excess.
- [[copy-number-variation]] / [[structural-variants]] — CNV and CRISPR-induced SVs called from the same PTA cells.
- [[quality-control-metrics]] — CV, Lorenz curves, Gini index and MAPD as uniformity metrics.

## Connections to other sources

- Benchmarked against [[chen-2017-lianti]] (re-used LIANTI data; LIANTI the next most sensitive), [[dean-2002-mda]], [[chenghang-2012-science]] / [[zong-2017-malbac-protocol]] (MALBAC) and [[telenius-1992-dop-pcr]]. Earlier comparative context: [[debourcy-2014-plosone]], [[hou-2015-wga-comparison]], [[huang-2015-scwga-review]].
- Callers tested: [[zafar-2016-monovar]], [[dong-2017-sccaller]]. The PTA-specific caller it anticipates: [[luquette-2022-neuron-scan2-indels]] (SCAN2), later used with PTA at scale in [[luquette-2025-pta-duplex-mosaicism]].
- Somatic mosaicism motivation and neuron SNV work: [[lodato-2017-aging-neurons]]; low-input mutation burden at single-molecule level: [[abascal-2021-nanoseq]]. Signature framework: [[alexandrov-2013-mutational-signatures]].
- CNV calling via [[garvin-2015-natmethods]] (Ginkgo); proposed multi-omic extension in the style of [[macaulay-2015-gt-seq]].
- Opposite design philosophy for CNV-only scaling: [[zahn-2017-dlp]] and [[laks-2019-dlp-plus]] avoid WGA altogether. (synthesis)

## Open questions

- How much of PTA's residual false-positive load is chemistry-specific, and can it be modelled without kindred cells or bulk? (synthesis)
- Does PTA's advantage persist at the 10–20× depths typical of cohort designs?
- Is the ENU C>G excess a real human-cell feature or a PTA artifact? The paper does not test this with an orthogonal method. (synthesis)
- The authors suggest droplet or microfluidic PTA for high throughput; not demonstrated here.

## Related

- [[pta]] · [[scwga-chemistries]] · [[single-cell-variant-calling]] · [[chen-2017-lianti]] · [[luquette-2022-neuron-scan2-indels]] · [[charles-gawad]] · [[40-Topics/whole-genome-amplification]]
