---
type: summary
title: "Zhou & Troyanskaya 2015 — Predicting effects of noncoding variants with deep learning–based sequence model"
source: "[[00-Sources/papers/Predicting effects of noncoding variants with deep learning–based sequence model]]"
source_quality: full
source_sha256: "b4f3ea51f7b05c9661cd3f1227add44eb106528c838ba0c9d8407b0cdb7251e6"
source_kind: paper
author: "Jian Zhou, Olga G. Troyanskaya (corresponding)"
published: 2015-08-24
ingested: 2026-10-08
doi: "10.1038/nmeth.3547"
journal: "Nature Methods"
tags: [DeepSEA, sequence-to-function, convolutional-neural-network, multitask-learning, chromatin-profile-prediction, variant-effect-prediction, in-silico-mutagenesis, ENCODE, Roadmap-Epigenomics, eQTL, GWAS, HGMD, allelic-imbalance]
entities: []
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[convolutional-neural-network]]", "[[transcription-factor-motif]]", "[[chromatin-accessibility]]", "[[chip-seq]]", "[[dnase-seq]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[histone-modifications]]", "[[computational-methods]]"]
---

**Citation:** Zhou & Troyanskaya (2015) — *Predicting effects of noncoding variants with deep learning–based sequence model* — *Nature Methods*. [DOI](https://doi.org/10.1038/nmeth.3547)

# Zhou 2015 — DeepSEA

> DeepSEA is a multitask deep convolutional network that reads 1,000 bp of human reference sequence and predicts the presence of 919 chromatin features in the central 200 bp: 690 TF-binding profiles (160 TFs), 125 DNase I hypersensitivity profiles and 104 histone-mark profiles from ENCODE and Roadmap Epigenomics. Because it predicts from sequence alone, the effect of any variant can be scored by predicting the reference and alternative alleles and taking the difference. The paper shows this works at single-nucleotide resolution (allelic imbalance in DNase-seq, histone QTLs) and that the predicted chromatin effects, plus four conservation scores, prioritise HGMD regulatory mutations, eQTLs and GWAS SNPs better than CADD, GWAVA and FunSeq2. It is the paper that established the "train on the reference genome, score variants by in-silico allele swaps" recipe that later sequence-to-function models follow.

## Key claims

- **Chromatin features are predictable from sequence.** On held-out chromosomes 8 and 9, median AUC was 0.958 for TF binding, 0.923 for DHSs and 0.856 for histone marks. For TF binding this beat gkm-SVM (median AUC 0.896) for nearly all TFs.
- **Wider context helps.** Labels always come from the central 200 bp, but models trained on 1,000 bp inputs beat 500 bp and 200 bp inputs (P < 2.2e-16, Wilcoxon signed-rank between any pair). gkm-SVM did not gain from longer context, so the authors compared against its better 300 bp version.
- **Single-nucleotide sensitivity without variant training.** From ENCODE digital genomic footprinting data, the authors called 57,407 allelically imbalanced SNPs in 35 cell types (28,918 reference-biased, 28,489 alternative-biased). The cell-type-matched DHS predictor picked the more DNase-sensitive allele, and accuracy rose with prediction confidence: >95% for the 6,726 SNPs with predicted probability difference >0.1. Histone QTLs (H3K4me3, H3K27ac) from Yoruba LCLs gave top accuracies above 0.9.
- **Known TF-binding variants recovered.** For breast-cancer SNP rs4784227 the strongest predicted effect was increased FOXA1 binding in all five cell types with a FOXA1 predictor; an α-thalassemia SNP was predicted to create a GATA1 site; a pancreatic agenesis mutation was predicted to disrupt FOXA2 binding.
- **Variant prioritisation beats annotation-based scores.** Boosted logistic regression on 1,838 predicted chromatin-effect features plus 4 conservation features outperformed CADD, GWAVA and FunSeq2 on HGMD regulatory mutations, GRASP eQTLs and GWAS Catalog SNPs, across negative sets at several distances from the positives. Chromatin features alone were already accurate. Chromatin predictions were more informative for common variants (eQTLs, GWAS), conservation more informative for HGMD mutations.
- **Indels without indel training.** The HGMD SNP model ranked HGMD regulatory indels above nearby 1000 Genomes indels with high accuracy.
- **Unsupervised score.** A "functional significance score" (product of geometric-mean E values for chromatin effects and conservation, against 1,000,000 1000 Genomes SNPs) also beat earlier methods without supervised training (Supplementary Fig. 6).

## Methods / evidence

Architecture: three convolution layers (320, 480, 960 kernels) with max pooling, one fully connected layer and a 919-way sigmoid output; first-layer kernels act as PWMs. Loss: summed negative log-likelihood with L2, L1 on the penultimate layer outputs, max-norm constraints and dropout; SGD with momentum; Torch7 on a Tesla K20m. Data: GRCh37 split into 200 bp bins, a bin labelled 1 for a feature if more than half lies in a peak; training restricted to bins with at least one TF binding event (521.6 Mbp, 17% of the genome). Test chromosomes 8 and 9; validation 4,000 samples on chr7. Predictions average forward and reverse-complement strands. In-silico saturated mutagenesis scores all 3,000 substitutions of a 1 kb sequence as log2 fold change of odds and recovers canonical motifs (e.g. TGATAA for GATA1, GTAAATA for FOXA1). Variant classifiers use XGBoost with tenfold cross-validation on contiguous chromosome blocks; GWAVA training variants and anything within 2 kbp were excluded to avoid contamination.

Weight: a short Brief Communication with most detail in supplementary figures. Per-feature AUCs, the Fig. 2–3 panels and the comparison AUC values are images or supplementary tables in the clipping, so the head-to-head prioritisation numbers are not reported here.

## Limitations

**Authors' own:**
- gkm-SVM could not use all binding sites (full kernel matrix), so it was trained on at most 5,000 positives and 5,000 negatives per feature, and at 300 bp rather than DeepSEA's 1,000 bp.
- The authors expect the approach to improve as more functional-variant training data become available.

**Reviewer notes:**
- Training bins are restricted to the 17% of the genome bound by at least one measured TF, so negatives are drawn from TF-bound regions; AUC on genome-wide sequence could differ. (synthesis)
- Outputs are binary peak calls in a 200 bp window, not quantitative signal, so the model says whether a feature is present, not how strongly. (synthesis)
- 1 kb of context cannot capture distal enhancer–promoter effects on genes; the paper scores chromatin, not expression. (synthesis)

## Surprising or load-bearing bits

- The model never sees variant data, yet the reference-trained classifier reaches >95% accuracy on confident allelic-imbalance calls. This is the core justification for every later in-silico variant-effect pipeline. (synthesis)
- Multitask sharing is presented both as efficiency and as biology: a feature learned for one TF can be used by the predictor for a physically interacting TF.
- Chromatin features and conservation are complementary: predicted chromatin effects matter more for common variants, conservation for rare deleterious ones.

## Concepts touched

- [[sequence-to-function-model]] — founding multitask CNN that maps sequence to chromatin profiles.
- [[variant-effect-prediction]] — reference-vs-alternative allele scoring, allelic-imbalance validation, HGMD/eQTL/GWAS prioritisation.
- [[convolutional-neural-network]] — first-layer kernels as PWMs, hierarchical pooling over 1 kb.
- [[transcription-factor-motif]] — in-silico mutagenesis recovers canonical motifs for CEBPB, GATA1, FOXA1, FOXA2.
- [[chromatin-accessibility]] / [[dnase-seq]] — 125 DHS predictors validated on DGF allelic imbalance.
- [[chip-seq]] — 690 TF ChIP-seq and 104 histone-mark profiles as training labels.

## Connections to other sources

- Successors in this ingest: [[kelley-2016-basset]] (accessibility-only CNN), [[zhou-2018-expecto]] (same group, extends to expression), [[chen-2022-sei]] (same group, 21,907 profiles and sequence classes), [[kelley-2018-basenji]] (quantitative long-range).
- The Roadmap compendium behind the labels: [[roadmap-2015-111-epigenomes]].
- Covered as a landmark model in the deep-learning review [[angermueller-2017-genomebiol]].
- Single-cell descendant of the sequence-to-accessibility idea: [[yuan-2022-scbasset]]. (synthesis)

## Open questions

- How much of the predictive power comes from the TF-bound restriction of training bins rather than sequence grammar? (synthesis)
- Does single-nucleotide accuracy hold for cell types without matched training profiles? The allelic-imbalance test used cell-type-matched predictors. (synthesis)

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[convolutional-neural-network]] · [[kelley-2016-basset]] · [[zhou-2018-expecto]] · [[chen-2022-sei]] · [[40-Topics/sequence-models-and-foundation-models]]
