---
type: summary
title: "Liu et al. 2025 — scMomer: A modality-aware pretraining framework for single-cell multi-omics modeling under missing modality conditions"
source: "[[00-Sources/papers/scMomer- A modality-aware pretraining framework for single-cell multi-omics modeling under missing modality conditions.pdf]]"
source_quality: full
source_sha256: "8b3dbee51e45ae15fdc4d70f151e617fc71c7a64d271a991ca064cfe5f9eb6a7"
source_kind: paper
author: "Yuhang Liu, Quan Zou, Ran Su, Leyi Wei (corresponding)"
published: 2025-08-05
ingested: 2026-10-08
doi: "10.1101/2025.08.04.668374"
journal: "bioRxiv preprint"
tags: [scMomer, single-cell-foundation-model, missing-modality, knowledge-distillation, scBERT, Performer, scCLIP, ViT, pseudo-paired, scRNA-seq, scATAC-seq, cross-modal-translation, drug-response, perturbation-prediction, gene-embedding, preprint]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[multimodal-integration-methods]]", "[[joint-single-cell-multi-omics]]", "[[scrna-seq]]", "[[scatac-seq]]", "[[cell-type-annotation]]", "[[batch-effect]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/single-cell-multiomics]]"]
---

**Citation:** Liu et al. (2025) — *scMomer: A modality-aware pretraining framework for single-cell multi-omics modeling under missing modality conditions* — bioRxiv preprint (posted 5 August 2025). [DOI](https://doi.org/10.1101/2025.08.04.668374)

# Liu 2025 — scMomer

> scMomer is a three-stage framework for using RNA-only data while keeping some ATAC-derived knowledge. It is assembled from existing parts rather than trained from scratch. **Stage I** is unimodal masked pretraining: a pretrained **scBERT** (Performer, gene2vec gene embeddings, binned expression) for RNA, and an scCLIP-style ViT encoder over genome-ordered peak "patches" for ATAC, trained on independent scRNA-seq and scATAC-seq data from Panglao and GEO. The paper does not give the size of either corpus. **Stage II** fine-tunes both encoders jointly with a concatenation + MLP fusion, reconstruction losses and a modality-matching discriminator, on a **pseudo-paired** fetal atlas from scCLIP (377,134 cells; RNA and ATAC cells matched by annotated cell type) plus a 3,233-cell 10x human brain multiome set. **Stage III** freezes the RNA encoder and distils a small feed-forward "student" that predicts the ATAC embedding from RNA. At inference, a cell's RNA alone yields an RNA embedding plus an inferred ATAC embedding, fused into one vector. Most evaluations are RNA-only tasks: annotation, disease phenotype, gene-property prediction, drug response and Perturb-seq.

## Key claims

- **Fused embeddings beat single modalities (zero-shot, human brain, k-means k = 7).** RNA and ATAC embeddings each scored higher AMI and ARI than raw features, and the fused embedding scored highest. RNA and ATAC embeddings occupied different regions of UMAP space. The authors read this as complementary rather than forcibly aligned representations.
- **RNA → ATAC translation (fine-tuned on human brain).** Pseudo-bulk accessibility from translated cells correlated with real accessibility at PCC 0.981, against 0.333 for scButterfly. The authors attribute scButterfly's low score partly to its TF-IDF normalisation. Oligodendrocyte marker peaks showed the expected cell-type patterns in held-out cells.
- **Zero-shot phenotype and cell-type probes (aorta and cardiomyocyte disease sets).** Logistic regression on 80/20 splits favoured scMomer over scGPT, Geneformer, GenePT-w and scBERT. Fine-tuning reached about 0.95 accuracy on both datasets. k-means ARI on aorta for cell type / phenotype was 0.1319 / 0.3699 (raw 0.1214 / 0.0734; scBERT 0.0659 / 0.1628). Patient-identity ARI was 0.2271, lower than raw data's 0.3014, which the authors read as reduced batch sensitivity.
- **Gene-property tasks (Geneformer's tasks, 5-fold CV).** scMomer beat scBERT on all four tasks by small AUC margins (+0.018, +0.036, +0.004, +0.004). GenePT was best on two tasks. Best scores: dosage sensitivity 0.858 (RF), bivalent vs Lys4-methylated 0.803 (RF). GGI AUC was 0.787 and PPI AUC (HuRI) 0.636.
- **Cell-type annotation (MLP head, mostly frozen backbone).** On Zheng68K: accuracy 0.808 and F1 0.703, against 0.768 and 0.647 for scBERT. With 100:1 synthetic imbalance: accuracy 0.838 and macro F1 0.829 (+0.023 and +0.033 over scBERT). For out-of-distribution pancreas (train Baron, test the other three; four shared cell types), scMomer and scBERT were near-tied (0.962 vs 0.955).
- **Drug response (scMomer embeddings in place of DeepCDR's expression encoder).** IC50 PCC was 0.907, +0.053 over DeepCDR and +0.060 over scBERT. In leave-one-drug-out over 223 drugs, scMomer won on 213 with a mean PCC gain of 0.362. HDAC inhibitors (vorinostat, belinostat, tubastatin) gained more than kinase inhibitors, which the authors take as evidence that ATAC knowledge is captured. Drug-synergy AUC gains were +0.037 over DeepSynergy and +0.048 over scBERT.
- **Perturbation.** scMomer gene embeddings inside GEARS gave a +0.034 PCC gain on the top 20 DE genes (Adamson, Norman). A cross-modal perturbation test on PerturBase data is reported only in supplementary tables.

## Methods / evidence

Losses: Stage I uses cross-entropy over binned RNA expression and L1 over patch accessibility. Stage II uses weighted RNA and ATAC reconstruction plus BCE pair-matching. Stage III uses an L1 distillation loss on the ATAC embedding plus reconstruction. Gene embeddings are 200-dimensional and averaged across cells. Preprocessing follows scBERT (normalise to 10,000, log, keep cells with ≥ 200 genes). Downstream datasets: 10x human brain 3k, aorta (11 patients) and cardiomyocyte (NF/HCM/DCM) disease sets curated by GenePT, Zheng68K plus four pancreas sets, GDSC/CCLE/TCGA (561 cell lines, 223 drugs), O'Neil synergy, and Adamson/Norman Perturb-seq. No code URL is given in the text.

Weight: the "multi-omics" benefit is shown mostly indirectly, as small gains over scBERT (the same RNA backbone) on RNA-only tasks. The only direct cross-modal benchmark is one 3,233-cell brain dataset, and the paper says this dataset was also used "for model pretraining and cross-modality evaluation". Several reported deltas are internally implausible. GGI AUC 0.787 "outperforming scBERT by 0.766" would put scBERT at about 0.02, and PPI AUC 0.636 "by 0.632" would put it at about 0.004. Per-class "gains of 0.820 and 0.870 in accuracy" on Zheng68K CD8 subtypes are likely absolute accuracies. Leave-one-drug-out gains are against "baseline", not named. (synthesis)

## Limitations

**Authors' own:**
- High-quality multi-omics data are limited. The multimodal stage used an atlas-level **pseudo-paired** dataset, which may bias embeddings toward specific biological contexts and under-represent rare states or diseases.
- Performance depends on the backbone choices (scBERT, scCLIP's ATAC encoder). More advanced or scalable foundation models could improve it.

**Reviewer notes:** (at most three, each marked `(synthesis)`)
- Because the Stage II pairs are cell-type-matched pseudo-pairs, the distilled RNA → ATAC student can at best learn a cell-type-level mapping. Within-type regulatory variation cannot be inferred from it. (synthesis)
- The comparisons isolate scBERT vs scBERT + ATAC distillation, but there is no ablation of Stage II or III. Gains of +0.004 AUC on gene tasks are within the reported standard deviations. (synthesis)
- Possible leakage: the human brain multiome set is listed as both pretraining and cross-modal evaluation data, despite the stated "strict" train/eval separation. (synthesis)

## Surprising or load-bearing bits

- **Missing-modality inference by distillation.** Only RNA is needed at test time; the ATAC half of the embedding is a predicted vector. This is the opposite design choice to [[liu-2025-scarf]], which needs both modalities and matches them at inference. (synthesis)
- **Bulk transfer.** Single-cell-pretrained embeddings dropped into DeepCDR improved bulk cell-line IC50 prediction. The HDAC-inhibitor gains are the paper's main argument that chromatin information survives distillation, though this is indirect evidence. (synthesis)
- **Same pseudo-paired atlas as CLM-X.** Both this paper and [[li-2026-clm-x]] rely on the scCLIP fetal pseudo-pairs (377,134 cells, 1,154,464 peaks), which shows how scarce true paired data at scale still is. (synthesis)

## Concepts touched

- [[single-cell-foundation-model]] — a modular, distillation-based RNA + ATAC framework built on scBERT.
- [[multimodal-integration-methods]] / [[joint-single-cell-multi-omics]] — fusion-not-alignment; compared with scButterfly for translation.
- [[scatac-seq]] — ViT-style genome-ordered patches for about 1.15 M peaks.
- [[cell-type-annotation]] — Zheng68K and pancreas benchmarks, imbalance and down-sampling tests.
- [[batch-effect]] — patient-level ARI used as a batch-sensitivity proxy.

## Connections to other sources

- Shares pretraining data (scCLIP pseudo-pairs) with [[li-2026-clm-x]]. Contrasts with true-paired [[liu-2025-scarf]]. Another RNA + ATAC model in this ingest: [[yu-2026-scdynomics]]. (synthesis)
- Cites MultiVI ([[ashuach-2023-multivi]]) as a generative approach focused on reconstruction rather than transferable representations.
- RNA foundation-model baselines include scGPT ([[cui-2024-natmethods]]).
- Integration context: [[cao-2022-glue]], [[gong-2021-cobolt]], [[argelaguet-2020-mofa-plus]], [[stuart-2021-natmethods]], [[xiao-2024-multiomics-benchmark]].

## Open questions

- Does the distilled ATAC embedding carry information beyond what the RNA embedding already encodes? A test would compare RNA-only vs RNA + inferred-ATAC embeddings with matched capacity. (synthesis)
- How would true multiome pairs (for example SCARF's X-Omics) change Stage II? (synthesis)
- Could the student run in reverse (ATAC → RNA embedding) for ATAC-only datasets? The framework claims symmetry, but only RNA-only inference is shown. (synthesis)

## Related

- [[single-cell-foundation-model]] · [[multimodal-integration-methods]] · [[liu-2025-scarf]] · [[li-2026-clm-x]] · [[yu-2026-scdynomics]] · [[ashuach-2023-multivi]] · [[cui-2024-natmethods]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/sequence-models-and-foundation-models]]
