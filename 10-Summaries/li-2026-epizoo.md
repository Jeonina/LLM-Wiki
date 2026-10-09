---
type: summary
title: "Li et al. 2026 — EpiZoo: a DNA sequence-aware foundation model for cross-species single-cell epigenomics"
source: "[[00-Sources/papers/EpiZoo- a DNA sequence-aware foundation model for cross-species single-cell epigenomics.pdf]]"
source_quality: full
source_sha256: "ed89fd98bad544ac586bc0652e558ab86fe85624d8430441d5a6c41133801338"
source_kind: paper
author: "Keyi Li, Xiaoyang Chen (corresponding), Qun Jiang, Zian Wang, Hairong Lv, Rui Jiang (corresponding)"
published: 2026-09-29
ingested: 2026-10-08
doi: "10.64898/2026.09.24.754017"
journal: "bioRxiv preprint"
tags: [EpiZoo, scATAC-seq, foundation-model, mixture-of-experts, DNABERT-2, sequence-aware, cross-species, EpiAgent, Omni-scATAC, LoRA, imputation, variant-prioritization, cancer, primate-evolution, cell-type-specific-accessibility, preprint-text]
entities: ["[[20-Entities/rui-jiang]]"]
concepts: ["[[single-cell-foundation-model]]", "[[dna-language-model]]", "[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[genomic-tokenization]]", "[[scatac-seq]]", "[[scatac-imputation]]", "[[cell-type-annotation]]", "[[cis-regulatory-element]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/single-cell-atac-seq]]"]
---

**Citation:** Li et al. (2026) — *EpiZoo: a DNA sequence-aware foundation model for cross-species single-cell epigenomics* — *bioRxiv preprint*. [DOI](https://doi.org/10.64898/2026.09.24.754017)

# Li 2026 — EpiZoo

> EpiZoo is a 2.6-billion-parameter mixture-of-experts transformer **pretrained on single-cell ATAC-seq** from human and mouse: the "Omni-scATAC" corpus of about 20.9 million cells, 46 datasets, more than 30 tissues and cell lines. It builds on the same group's EpiAgent. Each cell becomes a "cell sentence" of up to 8,192 accessible cCREs ranked by TF-IDF. Each cCRE token's embedding is the sum of (1) a **DNA-sequence embedding** from SEAM, a DNABERT-2 encoder with a projection head that is calibrated to the learned embeddings and then frozen, (2) a learnable cCRE identity embedding and (3) a rank embedding. Pretraining has two tasks: cell–cCRE alignment (is this cCRE open in this cell?) and reconstruction of the whole accessibility profile through species-specific linear decoders. The sequence component is what lets the model move beyond species-specific coordinates. It can be post-trained on macaque, zebrafish, fly and maize, applied to a human–macaque primate comparison (EpiZoo-Evo), used to score noncoding somatic mutations (EpiZoo-Cancer), and used to predict cell-type-specific accessibility from sequence.

## Key claims

- **Architecture.** Hidden size 512. The MoE has 4 experts with top-2 routing. Cell embedding = [CLS] output. Species-specific signal decoders are linear maps from the cell embedding to that species' cCRE vocabulary. The human vocabulary comes from the Human-scATAC-Corpus (also used by EpiAgent); the mouse vocabulary from a large mouse atlas (Lu 2025). The human part of the corpus is about 8.1M cells (EpiAgent's 4.8M plus 12 datasets); the mouse part is about 12.8M cells from 33 datasets.
- **Feature extraction.** On four held-out datasets (Kanemaru2023 human heart, Li2023b human brain, Cusanovich2018 multi-tissue mouse, Fang2021 mouse brain), fine-tuned EpiZoo beat EpiAgent, CASTLE, cisTopic, scBasset, PeakVI and SCALE on NMI and ARI. Zero-shot EpiZoo was "competitive". Models using only sequence or only identity embeddings were both worse than the full model (supplementary).
- **Fine-tuning strategy.** Full fine-tuning overfits small datasets: embedding quality fell after the first steps. The best of 8 configurations was full fine-tuning of the embedding module plus LoRA on the MoE and decoders. It was more stable and used less GPU memory and time.
- **Cell-type annotation.** In five-fold within-dataset cross-validation, EpiZoo beat all baselines; on Cusanovich2018 (39 types) accuracy was 0.935 and macro-F1 0.901. Across datasets (trained on a tissue-matched Omni-scATAC reference), the average relative gains over the strongest baseline were 9.96% (accuracy), 12.40% (κ) and 23.17% (macro-F1). Accuracy dropped from within- to across-dataset by 0.053 (Kanemaru2023) and 0.069 (Fang2021), against average baseline drops of 0.111 and 0.216.
- **Imputation.** With 50% of non-zero entries masked, EpiZoo had the highest clustering NMI and the highest PCCs at cell-type, cell and cCRE level. Median cell-type-level PCC was 0.874, above EpiAgent, scOpen and scCASE.
- **New species.** Macaque zero-shot (using only cCREs that lift over to human cCREs, no training) gave NMI 0.854. After post-training, EpiZoo beat five baselines in macaque, zebrafish, fruit fly and maize. Gains over the best baseline were 7.0% (fly) and 11.2% (maize). For distant species, all identity embeddings and decoder weights start from scratch, so the transferred parts are SEAM, the MoE transformer, rank embeddings and the alignment head.
- **EpiZoo-Evo (human–macaque cortex).** A hybrid vocabulary of shared, human-specific and macaque-specific cCREs. kNN label transfer from macaque to human on raw embeddings reached accuracy 0.9095, including 0.9069 for rare L6b neurons (0.17% of cells); human to macaque reached 0.8046. cCRE embeddings formed six clusters along a conservation gradient: promoter-proximal shared cCREs fell from 86.48% in cluster C0 to 0% in C5. In C4, nearest-neighbour human-specific/macaque-specific cCRE pairs mapped to homologous genes 93 times against 21 for random pairs (Fisher's exact test, p = 2.64 × 10^−n; the exponent is garbled in the clipped text). The authors call these "macro-cCREs". Human-specific C5 cCREs were enriched for schizophrenia but not Alzheimer's GWAS SNPs (permutation p < 0.01).
- **EpiZoo-Cancer.** Fine-tuned on a pan-cancer scATAC dataset (200,936 cells, 8 TCGA cancer types) with a learnable cancer-type embedding. The loss-of-accessibility (LoA) score for each of 5,959 TCGA noncoding variants in cCREs comes from the change in SEAM embedding (alt − ref), added to the cell embedding and decoded. High-impact variants (top 2.5%) were enriched near COSMIC Tier 1 driver genes In BRCA, both zero-shot and fine-tuned models were significant (p = 8.59 and 4.69 × 10^−n; exponents garbled in the clipped text), with 19 and 20 driver genes hit. KIRC odds ratios were 1.75 (zero-shot) and 2.26 (fine-tuned). Fine-tuning added on average 20.5% new genes per cancer type.
- **Cell-type-specific accessibility from sequence.** SEAM sequence embeddings concatenated with averaged cell-type embeddings were trained on the CREsted BICCN2 mouse cortex data (19 cell types) with the CREsted chromosome split. Cell-type-level PCC was 0.663 (consensus peaks) and 0.677 (cell-type-specific peaks), against 0.648 and 0.634 for DeepBICCN2. Median peak-level PCC rose from 0.646 to 0.706. Sliding-window prediction reached PCC 0.647 at the mouse *Chsy3* locus and 0.657 on the chicken *UACA* locus. Integrated-gradient attribution on two enhancers pointed to EBF/MEF2C and FOXP1/MECOM/GATA motifs.

## Methods / evidence

SEAM calibration: the model is first trained without sequence embeddings, and SEAM is then regressed onto the learned identity embeddings (MSE). After alternating frozen and updated phases early on, SEAM is frozen for the rest of pretraining, fine-tuning and inference. The exception is the accessibility-from-sequence task, where it is unfrozen. Cell sentences exceeding 8,190 cCREs are randomly subsampled and re-sorted by TF-IDF rank. The alignment head is a 2-layer MLP on [cell embedding; cCRE identity embedding], trained on balanced positive and negative cCREs with BCE. Reconstruction is BCE over the species vocabulary; for imputation, MSE on TF-IDF values. Annotation uses a 3-layer MLP head with focal loss. Cross-species initialisation uses liftOver for close species and random initialisation for distant ones. Evo analyses use Louvain clustering of cCRE embeddings, Metascape GO, XSTREME/JASPAR 2026 motifs and GWAS Catalog permutation tests. Code: github.com/likeyi19/EpiZoo.

Weight: a broad, ambitious paper with many applications. The core benchmark numbers (NMI/ARI per dataset, annotation scores) are mostly in figures and supplements not reproduced in the text. EpiAgent, the main foundation-model baseline, comes from the same group, and EpiZoo reuses its corpus, vocabulary, objectives and token length. The cancer, evolution and sequence-to-accessibility applications are each shown on one dataset with enrichment-style validation. (synthesis)

## Limitations

**Authors' own:**
- Future directions: extend to multi-omics (transcriptome, proteome); test variant interpretation on larger variant catalogues, disease cohorts and experimentally validated perturbation data; and build perturbation-response prediction.
- Rapid cCRE turnover means only some cCREs map across species by coordinates. This is why the sequence component is needed, but distant species still start with no identity embeddings.

**Reviewer notes:**
- The LoA score adds the change in one cCRE's sequence embedding directly to the *cell* embedding and decodes it. The variant never passes through the transformer as part of the cell sentence. This is a strong linear shortcut, and its validation is enrichment near COSMIC genes, not measured allelic accessibility. (synthesis)
- Much of the 2.6B parameter count probably sits in per-species identity embeddings and linear decoders over about a million cCREs each, not in the transformer, so "2.6B" is not comparable to a dense model. Layer count is not stated in the text. (synthesis)
- Held-out benchmarks overlap closely with the pretraining data. Fang2021 (mouse brain) is held out, but Zu2023 (mouse brain) is in the corpus and is the reference for cross-dataset annotation. The sequence-to-accessibility comparison is against one CNN baseline (DeepBICCN2), with small PCC gains at the cell-type level. (synthesis)

## Surprising or load-bearing bits

- **Sequence plus identity beats either alone.** The ablation supports a central design question for scATAC foundation models: DNA sequence (as in scBasset or GFETM) and learned peak identity (as in Atacformer, CLM-access and EpiFoundation) carry complementary information. (synthesis)
- **Sequence is the bridge across species.** Without shared coordinates, the frozen DNABERT-2–derived SEAM is the only token-level component that transfers to zebrafish, fly or maize, along with the shared transformer weights.
- **Sequence-divergent "macro-cCREs".** Species-specific cCREs that sit together in embedding space and map to homologous genes are offered as candidates for functional conservation despite sequence turnover. This is a testable hypothesis, not a validated finding.
- **Best fine-tuning recipe: LoRA on the trunk, full updates on the embeddings.** This is a practical lesson for adapting billion-parameter single-cell models to small datasets.

## Entities mentioned

- [[20-Entities/rui-jiang]] — co-corresponding author (Tsinghua). His lab also developed EpiAgent and the Human-scATAC-Corpus that EpiZoo builds on.

## Concepts touched

- [[single-cell-foundation-model]] — the largest scATAC foundation model in this ingest, and cross-species.
- [[dna-language-model]] — DNABERT-2 used as a frozen sequence encoder (SEAM) inside a single-cell model.
- [[sequence-to-function-model]] — predicts cell-type-specific accessibility from sequence plus cell-type embedding, benchmarked against a CREsted CNN.
- [[variant-effect-prediction]] — LoA scores for noncoding somatic mutations in cancer.
- [[genomic-tokenization]] — TF-IDF-ranked cCRE tokens summing sequence, identity and rank embeddings.
- [[scatac-seq]] — the data type; 20.9M-cell human and mouse corpus.
- [[scatac-imputation]] — 50% dropout recovery against EpiAgent, scOpen and scCASE.
- [[cell-type-annotation]] — within- and across-dataset fine-tuned classification.
- [[cis-regulatory-element]] — cCRE embeddings show conservation gradients and sequence-divergent analogues.

## Connections to other sources

- Peer scATAC foundation models in this ingest: [[leroy-2025-atacformer]], [[liu-2025-clm-access]], [[wu-2025-epifoundation]] (cited). EpiZoo is the only one that encodes DNA sequence.
- Sequence encoder: [[zhou-2023-dnabert-2]]. Sequence-to-accessibility baseline and data: [[kempynck-2026-crested]].
- Feature-extraction baselines: [[yuan-2022-scbasset]], [[ashuach-2022-peakvi]], [[bravo-2019-cistopic]], [[xiong-2019-scale]]. Benchmark datasets include [[fang-2021-snapatac]] (mouse brain).
- Pretraining corpus includes [[li-2025-scnanoatac-seq2]] (mouse early embryos). Earlier sequence-plus-scATAC model: [[fan-2026-gfetm]]. (synthesis)
- Benchmark context for scATAC methods: [[luo-2024-scatac-benchmark]] (cited as reference 18).

## Open questions

- Do LoA scores match measured allele-specific accessibility (e.g. caQTLs or MPRA)? The current validation is indirect. (synthesis)
- How much of the cross-species gain comes from SEAM, and how much from the shared transformer weights alone? A post-training ablation without SEAM is not shown. (synthesis)
- Does the sequence-to-accessibility head compete with dedicated sequence-to-function models beyond DeepBICCN2, such as ChromBPNet or Borzoi-style models? (synthesis)

## Related

- [[leroy-2025-atacformer]] · [[liu-2025-clm-access]] · [[wu-2025-epifoundation]] · [[zhou-2023-dnabert-2]] · [[kempynck-2026-crested]] · [[yuan-2022-scbasset]] · [[scatac-seq]] · [[single-cell-foundation-model]] · [[40-Topics/single-cell-atac-seq]] · [[40-Topics/sequence-models-and-foundation-models]]
