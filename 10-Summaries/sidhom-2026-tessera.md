---
type: summary
title: "Sidhom et al. 2026 — A Foundation Model for the Cancer Genome"
source: "[[00-Sources/papers/A Foundation Model for the Cancer Genome.pdf]]"
source_quality: full
source_sha256: "f427085804aa0d95f377e2e8bb159b28fc313f71ccb95ce92dc50c25de11b83a"
source_kind: paper
author: "John-William Sidhom (corresponding), Alex S. Baras, Olivier Elemento, Manish A. Shah"
published: 2026-06-01
ingested: 2026-10-09
doi: "10.64898/2026.05.27.728319"
journal: "bioRxiv preprint (posted June 1, 2026; not peer reviewed)"
tags: [TESSERA, cancer-genome-foundation-model, somatic-SNV, copy-number-alteration, masked-token, InfoNCE, contrastive-learning, TCGA, MSK-CHORD, GENIE, bulk-tumour, panel-sequencing, pathogenicity, tumour-type-classification, predictive-biomarker, DR-learner, genotype-layer-gap, preprint-text]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[dna-language-model]]", "[[variant-effect-prediction]]", "[[copy-number-variation]]", "[[mutational-signatures]]", "[[cancer-of-unknown-primary]]", "[[structural-variants]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/cancer-clonal-evolution]]", "[[40-Topics/computational-methods]]", "[[40-Topics/scdna-seq]]"]
---

**Citation:** Sidhom et al. (2026) — *A Foundation Model for the Cancer Genome* — *bioRxiv* preprint. [DOI](https://doi.org/10.64898/2026.05.27.728319)

# Sidhom 2026 — TESSERA

> TESSERA (Tumour Embeddings via Self-Supervised Encoding and Reconstruction of Alterations) is a self-supervised model of a tumour's **bulk somatic genotype**. It has two transformer encoders. The SNV encoder predicts masked reference and alternate alleles from flanking sequence and from the other variants in the same tumour. The CNA encoder predicts masked segment means and LOH from the other copy-number segments of the tumour. A cross-modal InfoNCE loss then aligns the two views of the same tumour. Pretraining uses TCGA Pan-Cancer Atlas whole-exome data: about 10,000 tumours, with MC3 SNVs and ABSOLUTE purity-adjusted segments. The frozen representation is reused **without retraining** for ClinVar pathogenicity, 23-class tumour typing, survival stratification, and doubly-robust estimation of chemotherapy benefit on MSK-CHORD panel cohorts. For this wiki's question, TESSERA is the clearest example of a **pretrained, reusable genotype-layer model**. It works on one bulk profile per tumour, not on cells.

## Key claims

- **Training data: bulk, sample-level, two modalities.** SNVs come from the TCGA MC3 MAF (WES, about 10,000 tumours, 31 solid tumour types). CNAs are TCGA ABSOLUTE allele-specific segments. Segment mean is computed as log2 of purity-adjusted observed copy number over 2, and LOH comes from the allele-specific calls. The split is 75/25 by patient, stratified by tumour type. Cross-platform tests use GENIE v18 panels (SNV) and MSK-IMPACT panels from MSK-CHORD (CNA).
- **SNV masked-token pretraining.** With global attention and ±25 bp context, the model predicts both masked alleles correctly 45.9% of the time, against 17.2% with no context. Most of the gain comes from local sequence context. Global attention over other variants adds a smaller but consistent gain, and that gain grows with variant burden. It is largest in tumours with strong mutational processes (SKCM, UCEC). The TCGA-trained models kept the same ordering and scale of accuracy on GENIE panel data.
- **Pathogenicity as a linear probe.** A logistic regression on PCA of the SNV embeddings, scored on ClinVar, reached ROC AUC 0.705 with no context, 0.865 with local_25 and 0.869 with global attention (unique-variant split). On the harder unique-gene split it reached 0.653 for the baseline and 0.828 for local_25. Restricting to variants whose alleles the model reconstructed correctly in pretraining raised performance, so the authors propose reconstruction accuracy as a per-variant confidence filter.
- **CNA pretraining needs attention between segments.** Segment-mean Pearson r rose from 0.222 with no attention to 0.779 with one attention block, and was 0.772 with two. LOH AUC rose from 0.683 to 0.943 (one block) and 0.944 (two blocks). On MSK-CHORD panels, using a NoLOH variant after quantile normalisation, r was 0.727 (one block) and 0.746 (two blocks), while the attention-free baseline fell to 0.053.
- **Tumour typing across 23 TCGA classes.** The best single modality reached 0.644 macro-AP (SNV global_25, or CNA attn_2). Concatenating the two modalities gave 0.851 macro-AP and 0.982 macro-AUC. Joint InfoNCE pretraining raised this to 0.893 macro-AP and 0.986 macro-AUC.
- **Disagreements with pathology carry prognosis.** Across 8,939 TCGA samples, tumours the classifier got "wrong" had worse disease-specific survival than correctly classified tumours of the same pathology class (HR 1.35, 95% CI 1.20–1.52). In 7 of 11 significant classes, their survival matched the predicted class. In glioma the disagreements follow the WHO 2021 reclassification (Fisher P = 8 × 10⁻²⁴ within TCGA-GBM).
- **Unsupervised structure and prognosis.** UMAPs of the joint features separate the WHO 2021 glioma classes (n = 865) and the UCEC MSI and serous-like subtypes (n = 458). BRCA (n = 933) and PRAD (n = 391) form continuous manifolds instead. A risk score read off the manifold stayed significant after adjustment for OncotypeDX in BRCA (HR 1.53, 95% CI 1.05–2.23; OncotypeDX became null). In PRAD both the TESSERA score (HR 1.87) and Decipher (HR 1.35) stayed significant.
- **Predictive chemotherapy biomarker.** The frozen features feed a DR-learner. In the MSK-CHORD stage IV CRC cohort (1,452 patients: 1,204 FOLFOX, 248 FOLFIRI), the score split patients into 1,039 predicted FOLFOX-favoured and 413 predicted FOLFIRI-favoured. The pooled split was not prognostic (HR 1.03). Within strata the treatment effect reversed direction: FOLFOX was better in its stratum (PFS HR 0.68) and FOLFIRI in its stratum (HR 1.39). The reversal held on held-out OS (0.77 and 1.42). In PDAC (771 patients) PFS reversed (0.80 and 2.38, the latter in 42 patients), but OS did not reach significance. A rule distilled from the CRC attributions, TP53+/KRAS+/17p−, picked out 192 patients with PFS HR 0.43 in favour of FOLFOX.
- **Orthogonal check.** The frozen CRC score, applied to 44 DepMap CRC cell lines, correlated with oxaliplatin-over-SN-38 sensitivity (Spearman ρ = +0.27, one-sided P = 0.041). The FOLFOXai random-forest comparator was prognostic on the same cohort but showed no reversal.
- **Released as a reusable model.** Code (PolyForm Noncommercial), a pip package (`tessera-foundation`), Hugging Face weights for the LOH and NoLOH joint variants (CC-BY-NC-4.0), and Zenodo per-sample and per-token TCGA features.

## Methods / evidence

Architecture: multi-head attention blocks with 12 heads of 12 dimensions, pre-layer norm, GELU and 288-unit feed-forward layers, implemented in TensorFlow. **SNV tokens** carry ref and alt alleles, chromosome, position, VAF and flanking sequence (1, 10 or 25 bp each side, one-hot over A/C/G/T/deletion/unknown). Two parallel streams (a reference stream with position only, and a mutation stream with alleles) plus a diagonal mask stop a token from seeing its own alleles. The local module cross-attends to CNN-processed flanks and the global module attends over the sample's other variants, with three blocks each. **CNA tokens** carry chromosome, normalised start and end, log length, segment mean and LOH, again in a query stream and a key/value stream with a diagonal mask. Joint pretraining adds 256-unit projection heads, project-then-mean pooling and bidirectional InfoNCE (weight 0.1, temperature 0.1). Inputs are capped at 1,000 variants (recurrent variants first) and 1,000 segments (highest |segment mean| + 0.5 × LOH first). Training uses AdamW at learning rate 2 × 10⁻⁴ with early stopping (patience 10).

Downstream use is frozen. Per-sample features are the mean and max pools of each modality plus log counts. Tumour typing uses an MLP under 5 outer × 10 inner nested CV. The predictive analyses use a DR-learner with Cox-PLS outcome models, a logistic-PLS propensity model and a sparse-PLS second stage, under 10 × 5 nested CV. Attributions come from collapsing the linear chain into a 3,716-d effective coefficient vector, aggregating to genes and chromosome arms, and decomposing with a penalised matrix decomposition. Panel data are bridged by quantile-mapping MSK segment means onto the TCGA distribution.

Weight: a broad single-model demonstration with careful nested CV and an explicit prognostic-versus-predictive framing. It is a preprint, and the author contributions state that one author ran all analyses. All clinical claims are retrospective and observational. The pathogenicity task is not benchmarked numerically against AlphaMissense or CADD, which are only discussed. (synthesis)

## Limitations

**Authors' own:**
- The pretraining corpus is TCGA, mostly treatment-naïve primary tumours, so it does not reflect the metastatic, post-treatment and resistance states where the predictive biomarkers are evaluated.
- Only SNVs are tokenised. Small indels and multi-nucleotide substitutions are not modelled, which the authors call a tokenisation choice rather than a structural limit.
- The clinical cohorts are routine-care MSK-CHORD data, not randomised trials. Treatment assignment is confounded by performance status, comorbidity and physician preference, and every clinical claim is retrospective. No score has met the bar of prospective randomised validation.
- The PDAC OS signal was not significant, which the authors attribute to the event-poor 42-patient GA-favoured stratum and PDAC's natural history. No binary rule recovered PDAC's two-way prediction.
- The FOLFOXai comparison covers only the 28 of 67 Abraham genes that MSK-IMPACT profiles.
- Proposed extensions: panel-native pretraining on GENIE, fusions, SVs, methylation and expression, PCAWG-scale WGS, and alignment with a pathology FM.

**Reviewer notes:**
- The token is a **bulk, purity-adjusted segment of one tumour**. The model has no notion of subclones, cell-to-cell variation or a cancer cell fraction per segment (VAF enters only as an SNV feature). Its "genotype" is therefore a population average, which is the quantity scDNA-seq was built to break apart. (synthesis)
- Cross-platform transfer depends on quantile-mapping new segment means onto the TCGA distribution. This keeps the within-sample ranking but discards absolute scale, and it was validated only for WES-to-panel shifts. (synthesis)
- Several evaluations are modest in size or effect: 44 cell lines at ρ = 0.27, a 42-patient PDAC stratum, and a TP53/KRAS/17p rule that covers about 26% of the CRC cohort. The DR-learner pipeline has many tuned stages. (synthesis)

## Surprising or load-bearing bits

- **CNA structure is learnable from other segments in one attention layer.** Segment-mean r jumps from 0.22 to 0.78 with a single block, and a second block adds nothing. The authors read this as evidence that copy-number co-alteration is mostly pairwise or local.
- **The predictive signal sits in the "foundation" parts.** In the feature-slice ablation, the direction reversal sharpened from local-only, to local + global, to the full InfoNCE features. That is the paper's best argument that pretraining, not just featurisation, matters.
- **Misclassification as signal.** The genome-derived class tracks survival better than the pathology label, and in glioma it anticipates the WHO 2021 molecular reclassification.
- **What it would take to use TESSERA on single-cell DNA.** The CNA encoder's input is just a list of segments (chromosome, start, end, length, log2 ratio, optional LOH). A per-cell profile from a scDNA caller could be fed in the same way, using the NoLOH weights unless allele-specific calls exist, as from CHISEL. Three gaps remain. First, single-cell segment means are near-integer states without purity mixing, so the TCGA quantile bridge is untested for them. Second, sparse per-cell SNVs with allelic dropout do not resemble WES variant lists. Third, each cell would be embedded as if it were a whole tumour, with no attention across cells or clones. A genotype-layer single-cell FM would need pretraining on cell-level profiles, or at least a validated cell-to-tumour domain bridge. (synthesis)

## Concepts touched

- [[single-cell-foundation-model]] — TESSERA is a pretrained, frozen, reusable genotype model, but at bulk-tumour resolution. It marks what the single-cell genotype layer still lacks. (synthesis)
- [[dna-language-model]] — the SNV encoder is a masked-token model over somatic alleles in flanking-sequence context, not over the reference genome.
- [[variant-effect-prediction]] — ClinVar pathogenicity as a linear probe, with reconstruction accuracy as a confidence filter.
- [[copy-number-variation]] — a masked segment-mean and LOH objective with inter-segment attention, plus arm-level attributions (17p loss, 20q gain).
- [[mutational-signatures]] — global attention gains are largest in signature-strong tumours (SKCM UV, UCEC).
- [[cancer-of-unknown-primary]] — 23-class genome-derived tumour typing, set against clinical classifiers such as GDD-ENS.
- [[structural-variants]] — listed as a future modality and not modelled.

## Connections to other sources

- Sister genotype-FM paper: [[kong-2026-mutationprojector]] pretrains on about 30,000 GENIE + TCGA tumours with gene-level binary panel calls and molecular networks. TESSERA instead uses variant- and segment-level tokens from WES. Both are bulk and both freeze the representation for clinical tasks. (synthesis)
- The authors contrast TESSERA with reference- and germline-trained sequence models, [[avsec-2021-enformer]] and [[avsec-2026-alphagenome]], which do not represent copy-number alterations.
- The FM analogy is drawn to Geneformer, ESM-2 and UNI. On the transcriptome side the wiki's anchor is [[cui-2024-natmethods]] (scGPT). (synthesis)
- Single-cell CNA tools whose per-cell segment output could, in principle, feed the CNA encoder: [[garvin-2015-natmethods]], [[wang-2020-scope]], [[zaccaria-2021-chisel]], [[kuipers-2025-scicone]]. For a per-dataset transformer on scDNA read counts, see [[liu-2024-cot]]. (synthesis)
- Signature background: [[alexandrov-2013-mutational-signatures]].

## Open questions

- Would a CNA encoder pretrained on bulk segments produce meaningful embeddings for single cells, and would those embeddings separate clones the way scDNA-specific methods do? Nobody has tested this. (synthesis)
- How much does pretraining natively on panel data (GENIE), which the authors propose, change transfer compared with the TCGA-plus-quantile-mapping route?
- Can the treatment-selection score survive prospective randomised validation? The authors state it has not.
- Would adding indels, SVs and fusions as tokens change the CNA/SNV balance in the predictive signal? (synthesis)

## Related

- [[40-Topics/sequence-models-and-foundation-models]] · [[single-cell-foundation-model]] · [[copy-number-variation]] · [[variant-effect-prediction]] · [[kong-2026-mutationprojector]] · [[liu-2024-cot]] · [[40-Topics/cancer-clonal-evolution]] · [[40-Topics/scdna-seq]]
