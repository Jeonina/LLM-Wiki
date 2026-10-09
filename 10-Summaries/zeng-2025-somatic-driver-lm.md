---
type: summary
title: "Zeng et al. 2025 — Identifying somatic driver mutations in cancer with a language model of the human genome"
source: "[[00-Sources/papers/Identifying somatic driver mutations in cancer with a language model of the human genome]]"
source_quality: full
source_sha256: "7c33874ee5cbece3b663fd9f8f3689029883b7d9e04ecd8b58a0e4457585543d"
source_kind: paper
author: "Guangjian Zeng, Chengzhi Zhao, Guanpeng Li, Zhengyang Huang, Jinhu Zhuang, Xiaohua Liang, … (Xiaxia Yu, Shenying Fang; corresponding author not marked in the clipping)"
published: 2025
ingested: 2026-10-09
doi: "10.1016/j.csbj.2025.01.011"
journal: "Computational and Structural Biotechnology Journal (special issue: AI and Foundation Models in Biomedicine)"
tags: [GenomeBert, dna-language-model, BERT, k-mer, somatic-driver, cancer-driver, driver-vs-passenger, point-mutation, XGBoost, HyenaDNA, DeepSEA, OncoKB, FASMIC, xenograft, somatic-variant-effect, cancer]
entities: []
concepts: ["[[variant-effect-prediction]]", "[[dna-language-model]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/cancer-clonal-evolution]]"]
---

**Citation:** Zeng et al. (2025) — *Identifying somatic driver mutations in cancer with a language model of the human genome* — *Computational and Structural Biotechnology Journal*. [DOI](https://doi.org/10.1016/j.csbj.2025.01.011)

# Zeng 2025 — GenomeBert for cancer driver mutations

> **Source note:** the clipping holds the full text with Tables 1–3. Figures are images, gene symbols set in italics were stripped (e.g. the top-ranked driver gene in Fig. 1D is unnamed in the text), and several equation values and the model dimensions are missing.
>
> The authors pretrain a small BERT-style [[dna-language-model]], **GenomeBert**, on GRCh37 with k-mer tokens (k = 3–6, 1,000-bp inputs, masked-token objective only). They fine-tune it to tell oncogene and tumour-suppressor gene (TSG) sequence from other sequence using the COSMIC Cancer Gene Census. They then use the fine-tuned 6-mer model as a **frozen feature extractor** for **somatic cancer point mutations**: the [CLS] embedding of the 1,000-bp reference window is subtracted from that of the alternate window, and an XGBoost classifier is trained on that difference to call driver vs passenger. Training labels come from three curated sets (PMID25348012, OncoKB, FASMIC; 2,154 drivers, 1,725 passengers). The test set is a 71-mutation xenograft oncogenicity assay (45 drivers, 26 passengers). This is an **application with a small benchmark**, not a germline benchmark. GenomeBert + XGBoost reaches AUROC 83.25% in 10-fold cross-validation and 84.64% on the xenograft set, ahead of CHASM, REVEL, CADD, PrimateAI, OncoVar, DeepAlloDriver and others, and slightly ahead of DeepSEA or HyenaDNA features fed to the same classifier.

## Key claims

- **What model, which variants.** GenomeBert (BERT encoder, 1.7 M–3.7 M parameters depending on k) is applied to **somatic cancer point mutations** with experimental or literature support. The paper says "only point mutations were considered". It does not name cancer types for the mutation sets and does not say whether they are coding or noncoding. Coding missense is likely, given the sources (OncoKB, FASMIC) and the comparators (REVEL, PolyPhen-family tools, MutPred, CHASM). (synthesis)
- **Pretraining.** Forward and reverse-complement GRCh37 is cut into 100-bp bins and each is extended to 1,000 bp. The paper reports 60 million examples from this step and more than 180 million pretraining instances overall. Masking follows BERT: 15% of tokens, split 80/10/10. Next-sentence prediction is dropped. Pretraining accuracy plateaus after about five epochs, from 89.68% (3-mer) to 88.59% (5-mer). Each 6-mer epoch takes 70.8 h on four RTX 3090 GPUs.
- **Gene-function fine-tuning picks k = 6.** The model is fine-tuned on CGC genes (318 oncogenes, 320 TSGs) cut into 1,000-bp windows that inherit the gene's label. A three-kernel 1D convolution (sizes 2, 3, 5) is added before the transformer. The 6-mer model reaches AUROC 96.7% (oncogene) and 96.3% (TSG). The 3-mer model reaches only 59.4% and 58.8%, and performance rises with k.
- **Feature-based driver prediction (10-fold CV on the training set, Table 1).** GenomeBert + XGBoost: accuracy 75.00%, F1 78.20%, AUROC 83.25%, AUPRC 87.20%. The same pipeline with **HyenaDNA** features gives AUROC 82.83%, and with **DeepSEA** features 82.34%. The margin over other sequence models is about 0.4–0.9 AUROC points. The choice of classifier matters more. With GenomeBert features, Random Forest reaches 82.36%, MLP 77.03%, and logistic regression, SVM and naive Bayes 65.8–66.9%.
- **Against published predictors (Table 2).** GenomeBert ranks first on all four metrics. The closest tools are OncoVar (AUROC 82.60%), DeepAlloDriver (81.68%) and CHASM (79.99%). Generic deleteriousness scores do worse: REVEL 75.21%, CADD 60.16%, PrimateAI 62.55%. LOGO, an ALBERT-based DNA language model, reaches 67.89%. The eight conventional comparators were the obtainable tools from the top 10 of the 33 that Chen et al. benchmarked on the same xenograft data.
- **External test (xenograft, 71 mutations).** GenomeBert reaches a mean AUROC of 84.64%, an absolute gain of 4.31 points over the best reference method. Accuracy is 79.04% and F1 82.83%. Of the errors, 60% are drivers called passengers, and most wrong calls have probabilities between 0.25 and 0.75. The authors read this as "cautious" prediction. SMOTE raises accuracy (80.28%) and F1 (83.72%) but lowers AUROC (81.20%) and AUPRC (89.60%). Under-sampling makes every metric worse.
- **The authors' framing.** They call GenomeBert "a pioneer in applying language models to somatic driver identification", and describe pretraining → gene-level fine-tuning → mutation-level features as a "progressive resolution-based transfer learning strategy".

## Methods / evidence

Pretraining: TensorFlow MultiWorkerMirroredStrategy, batch 2,048 across 4 GPUs, Adam, 150 epochs × 4,000 steps, sinusoidal positional encoding, fewer transformer blocks than BERT-base. Driver task: the mutation sits in a 1,000-bp GRCh37 window (499 bp upstream, 500 bp downstream), tokenised as 6-mers. The REF and ALT [CLS] vectors from the gene-function-tuned model are subtracted. XGBoost settings: gbtree, eta 0.1, L1 α = 20, L2 λ = 2,000, 2,000 rounds. Metrics use a fixed 0.5 threshold, with 95% CIs from 200 pivot-bootstrap resamples. SHAP on the gene-function task highlights influential k-mers for one example oncogene. Code: github.com/GaryinDeep/GenomeBert.

Weight: the training labels are curated and the test set is an independent in vivo assay, which is a sound design. The test set is small, though (71 mutations). Gains over the best conventional tool (4.31 AUROC points) and over the other DNA models used as feature extractors (<1 point in CV) are modest. No confidence intervals are given in the text for those differences.

## Limitations

**Authors' own:**
- Transformer decisions are hard to interpret.
- The datasets carry no sex labels, so performance by sex cannot be checked.
- The amount of high-confidence data is limited. The authors plan a loop of model screening, experimental testing and model updates.
- Drivers are misclassified more often than passengers, so the share of drivers in the training set needs adjusting. Some genes (unnamed in the clipping) collect more errors and need more mutations or transfer learning.

**Reviewer notes:**
- The external AUROC is reported as 84.64% in Results and Discussion but 86.64% for the same "Baseline" row in Table 3. Table 2 is labelled "internal validation (10-fold CV on the training set)", yet the text says the comparators were not trained on that set and were compared "with the same test set". Which data each comparator row was scored on is unclear. (synthesis)
- The model never sees the variant in genomic or tissue context beyond 1 kb of reference sequence, and the gene-function fine-tuning teaches it gene identity (oncogene/TSG region), not mutation effect. Part of the driver signal may be "which gene is this window in" rather than the allele change. The top gene alone accounts for 683 mutations in the driver dataset (637 drivers, 46 passengers), and the CV is not described as split by gene. (synthesis)
- Evaluation is limited to curated cancer driver hotspots. It says nothing about noncoding somatic variants, structural variants, normal-tissue mosaicism or clonal haematopoiesis. (synthesis)

## Surprising or load-bearing bits

- **One of the few DNA-LM studies scored on somatic variants at all.** The labels are cancer driver vs passenger, and the test set is an in vivo oncogenicity assay rather than ClinVar or eQTLs. It is still a cancer setting, though. (synthesis)
- **The language model hardly matters.** Swapping GenomeBert for HyenaDNA or DeepSEA embeddings changes CV AUROC by under one point. Swapping XGBoost for logistic regression drops it by about 16 points. Most of the work is done by the downstream classifier on top of fairly generic sequence features. (synthesis)
- **"Large-scale" is 1.7–3.7 M parameters.** That is small by current DNA-LM standards, and smaller than the 89 M-parameter genomicBERT that has a similar name. (synthesis)
- Higher k helped downstream (3-mer AUROC 59% → 6-mer 97% on gene function) even though pretraining accuracy did not track it.

## Concepts touched

- [[variant-effect-prediction]] — a DNA LM's REF-vs-ALT embedding difference used as features to classify somatic cancer point mutations as driver or passenger.
- [[dna-language-model]] — k-mer BERT pretrained on GRCh37; DNABERT-style tokenisation, small model.

## Connections to other sources

- Architecture and tokenisation follow [[ji-2021-dnabert]] (overlapping k-mer BERT). (synthesis)
- Feature-extractor comparators: [[nguyen-2023-hyenadna]] and [[zhou-2015-deepsea]], both within one AUROC point of GenomeBert here.
- Not to be confused with [[chen-2023-genomicbert]] (genomicBERT, Unigram tokeniser, 89.2 M parameters). That paper is a separate model evaluated on germline/regulatory classification tasks. (synthesis)
- [[weinstock-2025-ch-noncoding-drivers]] and [[gjoni-2026-pediatric-tumor-3d]] are the other somatic uses of sequence models in this ingest: AlphaGenome on clonal-haematopoiesis noncoding variants and Akita on paediatric tumour SVs. Neither benchmarks the model. (synthesis)
- Germline-centred evaluation of sequence models: [[avsec-2026-alphagenome]], [[40-Topics/sequence-models-and-foundation-models]].

## Open questions

- Would the result hold under a gene-held-out split, where no test gene appears in training? (synthesis)
- Does the REF−ALT embedding difference carry signal for noncoding somatic drivers (e.g. *TERT* promoter), where protein-based tools such as REVEL cannot be used? The paper does not test this. (synthesis)
- Which external AUROC is correct, 84.64% or 86.64%?

## Related

- [[variant-effect-prediction]] · [[dna-language-model]] · [[ji-2021-dnabert]] · [[nguyen-2023-hyenadna]] · [[zhou-2015-deepsea]] · [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/cancer-clonal-evolution]]
