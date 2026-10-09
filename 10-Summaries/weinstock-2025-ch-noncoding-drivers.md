---
type: summary
title: "Weinstock et al. 2025 — Genome-wide characterization of clonal hematopoiesis reveals extensive non-coding putative driver mutations"
source: "[[00-Sources/papers/Genome-wide characterization of clonal hematopoiesis reveals extensive non-coding putative driver mutations.pdf]]"
source_quality: full
source_sha256: "01edd1a4d832215fd005b920c9ffba6638d489a9e249a9e26090c0352477fb36"
source_kind: paper
author: "Joshua S. Weinstock (lead contact), Karen Conneely, Janghee Woo, Marios Arvanitis, Mitchell J. Machiela, Cameron Russell"
published: 2025-10-14
ingested: 2026-10-09
doi: "10.1101/2025.10.12.25337792"
journal: "medRxiv preprint"
tags: [clonal-hematopoiesis, CHIP, non-coding-driver, TERT-promoter, UGT2B7, IGH, IGLL5, UK-Biobank, TOPMed, age-GWAS, PACER, telomere-length, PheWAS, somatic-heritability, GRAMD1B, AlphaGenome, AlphaMissense, centromere, mosaic-loss-of-Y, preprint]
entities: []
concepts: ["[[variant-effect-prediction]]", "[[sequence-to-function-model]]", "[[copy-number-variation]]", "[[highly-repetitive-regions]]", "[[methylation-clones-epimutation]]"]
topics: ["[[40-Topics/clonal-hematopoiesis]]", "[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/somatic-mosaicism]]", "[[40-Topics/mosaic-variant-calling]]", "[[40-Topics/hematopoietic-malignancies]]"]
---

**Citation:** Weinstock et al. (2025) — *Genome-wide characterization of clonal hematopoiesis reveals extensive non-coding putative driver mutations* — *medRxiv preprint* (posted 2025-10-14, not peer reviewed). [DOI](https://doi.org/10.1101/2025.10.12.25337792)

# Weinstock 2025 — Genome-wide noncoding CH drivers in UK Biobank

> **Source note:** full preprint text from PDF extraction, including Methods and supplementary figure captions. Figures and Supplementary Data 1–3 (variant list, AlphaGenome outputs, PheWAS results) are not in the source.
>
> The authors search the whole genome for clonal haematopoiesis (CH) drivers without a gene list. They run an association test of **age at blood draw** on all ~147 M SNVs and indels with minor allele count ≥ 10 in ~490K UK Biobank blood WGS. The idea is that somatic alleles that rise with age mark selective clonal sweeps. They find 68 age-associated variants: 23 look germline and 45 look somatic. The 45 include canonical genes (*DNMT3A*, *ASXL1*, *GNB1*, *IDH2*, *SF3B1*) and 35 novel putative drivers, **32 of which are noncoding**. Among these are a *TERT* promoter mutation (72 carriers), an intronic insertion in *UGT2B7* (1,165 carriers), IGH point mutations and 17 centromeric variants. The paper then estimates clone fitness (PACER), telomere-length associations, a 30-disease PheWAS with "somatic h²", and germline GWAS of the IG and *UGT2B7* mutations. **Sequence-model use:** the only DNA sequence model is **AlphaGenome**. It is used once, as a downstream **annotation step**: it predicts expression changes of genes within 1 Mb of each mutation in hematopoietic multipotent progenitors, to suggest a causal gene. It is not a variant scorer for discovery and is not benchmarked. Discovery is purely statistical (age association), and noncoding variants are otherwise annotated only with Ensembl VEP categories.

## Key claims

- **An age association recovers known CH and finds noncoding drivers.** REGENIE linear mixed model, genome-wide threshold 5 × 10⁻⁸, λGC = 1.01. Of the 45 likely somatic variants, 43 are more frequent in older people and two are less frequent. All 35 novel ones are rare (<0.5%) with |β| > 0.10 SD of age. By VEP: 2 missense (*IGHV2-70D*, *IGLV3-1*), 1 possible splice variant (*MTCP1*, chrX_155066068_C_T) and 32 noncoding.
- **Somatic origin checks.** Beta-binomial tests show 5 of 35 have VAFs compatible with germline origin. All centromeric variants have VAF > 0.5. The five IGH mutations overlap a relatively frequent IGH mosaic chromosomal alteration (mCA; 0.25%) and may hitchhike on it. The *FRG2B*, *UGT2B7*, *DGKB* and *FGF1* mutations do not overlap frequent mCAs. In 184,878 TOPMed blood genomes, 43 of 45 variants are present and allele frequencies agree for non-centromeric variants (ρ = 0.63, p = 0.008).
- **Centromeric hits likely tag copy-number change.** Read depth at the chr17 centromere (normalised to *OCT4*) rises with age (p = 3.0 × 10⁻¹⁵). It tracks relative depth at *TET2* (β = 0.199, p < 10⁻³⁰⁰) and is negatively associated with mosaic loss of Y in males (β = −0.008, p = 5.3 × 10⁻⁴). The authors read it as a broader genomic-instability marker that needs long reads to resolve.
- **AlphaGenome as a cis-gene assigner (the only sequence-model use).** For the *TERT* promoter variant (chr5_1295113_G_A), AlphaGenome predicts up-regulation of *TERT* in hematopoietic progenitors (Supplementary Fig. 7 shows predicted RNA-seq tracks). For several variants it predicts effects on more than one gene. chrX_155066068_C_T is predicted to raise both *MTCP1* (a *TCL1A* paralogue) and *CMC4*. The *UGT2B7* intronic indel is predicted to lower *UGT2B7* and raise *UGT2B11*. No accuracy, comparison or experimental check of these predictions is reported, and despite a "(Methods)" pointer the Methods section has no AlphaGenome subsection.
- **Coding-variant scoring is protein-based and adds nothing.** Two ACAT gene-based tests were run: one on rare variants with AlphaMissense > 0.3 (a protein model, not a DNA model) and one on all rare variants. Neither added discoveries beyond the single-variant scan at 2.5 × 10⁻⁶.
- **Fitness (PACER, relative to *DNMT3A* R882H).** Splicing factors (*SF3B1*, *SRSF2*, *PRPF8*) and *JAK2* exceed R882H, as previously reported. The *TERT* promoter mutation is similar to splicing factors and *IDH2* and above *JAK2*. *IGLL5* and IGH mutations come out higher than the splicing factors. Telomere-length associations correlate negatively with PACER (ρ = −0.37, p = 0.016). *SRSF2*, the *TERT* promoter and IG mutations show less telomere shortening than their fitness predicts.
- **Disease correlates.** 421,584 individuals; 8,460 tests (282 variants × 30 phenotypes) with mashr. There are 881, 503 and 396 hits at LFSR 5%, 1% and 0.5%, and 60 at Bonferroni, all in cancer phenotypes. "Somatic h²" is largest for leukaemia (0.003). Non-canonical mutations contribute on average 47% of it, ranging from 19% (obesity) to 90% (lymphoid leukaemia). The *UGT2B7* indel is associated with myeloproliferative neoplasm (OR 1.89, LFSR 3.7 × 10⁻⁷). An IGH variant is associated with about 6.5-fold odds of atrial fibrillation (LFSR 1.2 × 10⁻³).
- **Germline determinants.** A GWAS of carrying any IG mutation (343 cases, 482,326 controls) finds one locus at *GRAMD1B* (rs12797056, 10% AF, OR 1.87, p = 1.6 × 10⁻⁹), which is also a CLL GWAS locus. A GWAS of the *UGT2B7* mutation finds a cis locus (rs4348158, MAF 0.6%, OR 0.26, p = 3.0 × 10⁻⁴⁴) and a second locus near *SULT1E1*. The authors suggest a sex-hormone pathway.

## Methods / evidence

Variant calls: UKB DRAGEN population-level WGS (PLINK/pVCF, 500k release). Canonical CH was recalled by bcftools mpileup at 4,737 prespecified sites (union of TOPMed and earlier UKB CH calls). 577 sites with mean VAF 0.46–0.54 were excluded, leaving canonical mutations in 18,010 people. Passengers were counted as singleton SNPs with VAF 0.05–0.35 and 4–6 alt reads. PACER uses negative binomial regression with spline adjustment for VAF × sex and age. Telomere length is the UKB qPCR measure. Somatic h² is the sum of β²_liability · AF(1 − AF), ignoring covariance between mutations. GWAS exclusion lists cover hg19/hg38 contig differences, UCSC "unusual" regions and GRC exclusions. Portal: somatic.emory.edu.

Weight: a very large, well-replicated statistical discovery study (TOPMed cross-check, VAF tests, mCA overlap). Its sequence-model content is thin: a single qualitative AlphaGenome use for gene assignment, with outputs held in a supplement that is not in the source.

## Limitations

**Authors' own:**
- Causality is hard to infer. The timing of somatic acquisition is unknown, and confounders (smoking, chronic inflammation) are common and hard to fully adjust for.
- Age-associated variants show positive selection, but true drivers cannot be separated from hitchhikers.
- *UGT2B7*, *FGF1*, *MTCP1*/*TCL1C* and *DGKB* are expressed mostly outside blood. Their role in CH is uncharacterised and needs functional work.
- Sensitivity at centromeres is very limited with short reads. Long-read cohorts are needed.

**Reviewer notes:**
- AlphaGenome is used as an oracle for gene assignment with no validation. The Results also attach "resulting in increased telomere lengths" to the AlphaGenome *TERT* prediction, but that is not a model output. AlphaGenome predicts expression tracks, not telomere length. (synthesis)
- Internal inconsistencies: the IGH variant is listed as chr14_105860408_G_C but the atrial-fibrillation association uses chr14-105860408-G-T. The text describes AlphaMissense filtering as "moderate deleteriousness" while Methods use a score > 0.3. Canonical CH recalling is said to run on "UKB exomes" in Methods, in a WGS study. *ASXL1* is spelled "ASLX1". (synthesis)
- Bulk blood WGS at about 30× with a MAC ≥ 10 filter can only see clones that are large and recurrent at the exact base. Private noncoding drivers and small clones are invisible to this design, which is where per-variant model scoring would be needed. (synthesis)

## Surprising or load-bearing bits

- **Noncoding CH drivers exist at population scale.** 32 of 35 novel age-associated somatic variants are noncoding, and a *TERT* promoter mutation, previously known from pan-cancer work, has fitness comparable to splicing-factor CH.
- **The only sequence-model use in a genome-wide CH driver study is an unbenchmarked AlphaGenome annotation.** Neither discovery nor prioritisation used a DNA model, and no CADD-type or deep-learning score was applied to the noncoding hits. For the review's argument, this is direct evidence that sequence-to-function models have not been evaluated on CH variants, only used decoratively. (synthesis)
- **IG mutations look like the fittest clones** in this analysis. A germline GWAS on them recovers a CLL locus de novo, so a CLL precursor phenotype can be defined from blood WGS alone.
- Non-canonical CH carries about half of CH's liability-scale variance on average. Gene-list CH studies may miss a large share of the signal.

## Concepts touched

- [[variant-effect-prediction]] — AlphaGenome cis-expression predictions on somatic CH variants, used without evaluation. AlphaMissense used for coding burden tests.
- [[sequence-to-function-model]] — AlphaGenome applied to age-selected somatic blood variants in hematopoietic progenitor context.
- [[copy-number-variation]] — centromeric point mutations reinterpreted as chr17-centromere depth change. IGH hits overlap mCAs.
- [[highly-repetitive-regions]] — centromere calling limits.
- [[methylation-clones-epimutation]] — cited as an alternative explanation for driverless clones.

## Connections to other sources

- Model used: [[avsec-2026-alphagenome]]. The preprint cites the 2025 bioRxiv version.
- Unexplained driverless clonal expansion, one motivation here: epimutation-based clone tracing in [[scherer-2025-nature]] (cited as ref. 23).
- Context for CH and blood clonality: [[40-Topics/clonal-hematopoiesis]], [[40-Topics/hematopoietic-malignancies]].
- Other somatic uses of sequence models in this ingest: [[zeng-2025-somatic-driver-lm]] (benchmarked DNA LM, cancer coding point mutations) and [[gjoni-2026-pediatric-tumor-3d]] (Akita on paediatric tumour SVs). (synthesis)

## Open questions

- Do AlphaGenome's multi-gene predictions (e.g. *MTCP1* vs *CMC4*, *UGT2B7* vs *UGT2B11*) agree with expression in carriers, or with eQTL/CRISPR data in HSPCs? Not tested. (synthesis)
- Would a variant-effect score have ranked the 32 noncoding hits above matched non-age-associated rare noncoding variants? That is the natural benchmark this dataset enables. (synthesis)
- How do the IGH point mutations in myeloid-risk carriers relate to B-cell vs myeloid clones? The authors argue they must be present in myeloid progenitors to be detectable at ~30×.

## Related

- [[variant-effect-prediction]] · [[sequence-to-function-model]] · [[avsec-2026-alphagenome]] · [[40-Topics/clonal-hematopoiesis]] · [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/somatic-mosaicism]] · [[40-Topics/mosaic-variant-calling]]
