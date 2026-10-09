---
type: summary
title: "Ying et al. 2024 — MethylGPT: a foundation model for the DNA methylome"
source: "[[00-Sources/papers/MethylGPT- a foundation model for the DNA methylome.pdf]]"
source_quality: full
source_sha256: "d83db3817e2ac5d10c9de7b45acbcf75a561a46d7e25b9829f98a2f18148e97e"
source_kind: paper
author: "Kejun Ying (co-first; corresponding), Jinyeop Song, Haotian Cui, Yikun Zhang, Siyuan Li, Xingyu Chen, … Mahdi Moqri (corresponding), Bo Wang (corresponding), Vadim N. Gladyshev (corresponding)"
published: 2024-11-04
ingested: 2026-10-08
doi: "10.1101/2024.10.30.621013"
journal: "bioRxiv preprint"
tags: [MethylGPT, DNA-methylation, foundation-model, transformer, bulk-methylation, Illumina-array, EWAS, epigenetic-clock, age-prediction, disease-risk, Generation-Scotland, attention-analysis, missing-data, preprint-text]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[epigenetic-aging]]", "[[imputation]]", "[[cpg-island]]", "[[batch-effect]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/dna-methylation]]"]
---

**Citation:** Ying et al. (2024) — *MethylGPT: a foundation model for the DNA methylome* — *bioRxiv preprint*. [DOI](https://doi.org/10.1101/2024.10.30.621013)

# Ying 2024 — MethylGPT

> MethylGPT is an scGPT-style transformer trained on **bulk human methylation array data**: 154,063 samples (from 226,555 collected out of 5,281 datasets via EWAS Data Hub and ClockBase) over a **fixed vocabulary of 49,156 CpG sites**. Each CpG is a token with a learned ID embedding plus a value embedding. The model masks 30% of the values and predicts them, and it also rebuilds the whole profile from the CLS token. Masked-value prediction reaches Pearson R 0.929 (MAE 0.074). Fine-tuned with a ResNet1D head, it predicts multi-tissue age (median absolute error 4.45 years on the validation set) and stays stable with up to 70% of CpGs missing. It also predicts 10-year risk for 60 diseases in Generation Scotland (AUC 0.72 on the test set). Attention analysis separates young and old samples. The model sees no DNA sequence and no single-cell data. The authors list single-cell methylation as future work.

## Key claims

- **Training corpus and vocabulary.** The 49,156 CpGs are those linked to more than 5 traits in the EWAS Catalog or present in more than 95% of pretraining samples. They come from Illumina 27k, 450k and EPIC arrays across about 20 tissue types, giving 7.6 billion training tokens. Samples with more than 40% missing CpGs were dropped.
- **Masked-value prediction.** Best test MSE was 0.014 at epoch 10, with MAE 0.074 and Pearson R 0.929 between predicted and true values on masked CpGs.
- **CpG embeddings organise by genomic context without supervision.** In UMAP, CpG embeddings separated by CpG-island relation (island, shore, shelf, other), by enhancer status, and sex-chromosome CpGs from autosomal ones. This is shown visually, with no quantitative score.
- **Sample embeddings separate tissue and sex and reduce batch structure.** Whole blood, brain, liver and skin formed distinct clusters. Male and female samples separated. Batch-specific clustering was weaker than in UMAPs of raw values. Again visual only.
- **Age prediction.** On 11,453 multi-tissue samples (47.2% blood, 34.5% brain, ages 0–100), the fine-tuned model had a median absolute error of 4.45 years on the validation set. The authors report it beat ElasticNet, an MLP (AltumAge), Horvath's skin-and-blood clock and other predictors on both validation and test sets.
- **Robust to missing data.** With 10–90% of test CpGs masked, performance held steady up to 70% missing and degraded less than ElasticNet or MLP.
- **Reprogramming rejuvenation.** In an iPSC reprogramming time course, predicted age dropped sharply after day 20 and was near zero by day 30. Horvath's clock and GrimAge showed the same trend.
- **Attention differs by age.** CpGs with differential attention (>1.5-fold, p < 0.05) between young (<20) and old (>60) samples were linked to sex and autoimmune EWAS traits in the young, and to ageing, BMI and thyroid lesions in the old. Young high-attention CpGs were enriched for developmental processes (e.g. response to growth factor). Old ones were enriched for oxidative stress and amino-acid metabolism.
- **Disease risk and interventions.** Fine-tuned to predict 60 diseases in eight categories plus 10-year mortality, overall AUC was 0.736 (validation) and 0.720 (test). Applied to 183 samples from eight interventions in six GEO datasets, smoking cessation had the strongest predicted protective effect on mortality (β = −0.13). High-intensity training (n = 5) helped respiratory, neurological and autoimmune categories. Everolimus (n = 8) increased predicted autoimmune risk.

## Methods / evidence

Architecture: CpG-ID embedding plus an MLP value embedding (dimension 64), summed, with a CLS token. Transformer with FlashAttention over all 49,157 tokens, 4 heads, feed-forward width 64. Two losses: MSE on 30% masked values (Methylation Value Prediction), and an scGPT-style profile reconstruction from the CLS embedding. AdamW, learning rate 0.001 with 10% decay per epoch, 10 epochs, batch size 16, one A100 GPU. Fine-tuning attaches a ResNet1D head (six residual blocks over the 49,156 × 64 embedding) and trains everything end to end with MSE (age) or cross-entropy (disease). Attention analysis uses the last layer, two-sided t-tests with Benjamini-Hochberg correction and methylGSA enrichment.

Weight: the paper is short and mostly descriptive. Embedding claims rest on UMAP pictures with no clustering scores. The age benchmark reports median absolute error, and the baseline numbers are only in a figure. The intervention analysis uses small groups (5–59 samples per intervention) and reads disease-risk changes from a model's predictions, not from outcomes. Code was "to be released upon publication" at this version. (synthesis)

## Limitations

**Authors' own:**
- Integrating epigenetic features beyond CpG methylation is left to future work.
- Better attention-visualisation tools are needed to link predictions to mechanisms.
- Single-cell methylation analysis is named as an unexplored application.

**Reviewer notes:**
- The architecture is internally inconsistent: Results say 12 transformer blocks, Methods say 6. The Generation Scotland cohort is given as n = 18,859, but the disease fine-tuning split is 1,378 / 295 / 296 samples, so fewer than 2,000 samples were used. (synthesis)
- A fixed 49,156-CpG vocabulary chosen by EWAS-trait association ties the model to array probes and biases it toward known trait CpGs. It cannot score CpGs outside the vocabulary, unlike sequence-keyed models such as [[delimacamillo-2024-cpgpt]]. (synthesis)
- The intervention "effects" are shifts in model-predicted risk in small trial subsets. They are not validated against outcomes and should not be read as causal. (synthesis)

## Surprising or load-bearing bits

- **Small model, very long context.** With 64-dimensional embeddings, the model attends over about 49k tokens per sample using FlashAttention. That is a different design point from sequence-keyed models, which sample 5–10k CpGs per input. (synthesis)
- **Robustness to missing data is the most practical result.** Stable age prediction with 70% of CpGs missing matters for cross-array and low-coverage data.
- **Attention shows age-specific CpG sets.** The young/old attention split links to known EWAS traits. This is offered as interpretability, though attention-as-explanation is debated. (synthesis)

## Concepts touched

- [[single-cell-foundation-model]] — a bulk methylation foundation model with the scGPT design (gene token → CpG token). The single-cell extension is only proposed.
- [[epigenetic-aging]] — multi-tissue age prediction, reprogramming rejuvenation and age-specific attention.
- [[imputation]] — masked-value prediction and robustness to missing CpGs.
- [[cpg-island]] — CpG embeddings separate island, shore, shelf and open-sea sites.
- [[batch-effect]] — sample embeddings show less batch clustering than raw values (qualitative).

## Connections to other sources

- Concurrent bulk methylation foundation model [[delimacamillo-2024-cpgpt]], which cites MethylGPT as independent parallel work. CpGPT keys loci by DNA sequence and can query unseen CpGs. MethylGPT uses fixed CpG IDs. (synthesis)
- Single-cell methylation foundation model that fills the gap MethylGPT names: [[liang-2025-scdnam-gpt]].
- Architectural template: scGPT, [[cui-2024-natmethods]] (Haotian Cui and Bo Wang are co-authors on both).
- Single-cell methylation imputation context for comparison: [[angermueller-2017-genomebiol]], [[liang-2026-scmeth-imputation-benchmark]].

## Open questions

- How does MethylGPT compare head-to-head with CpGPT on the same age, imputation and array-conversion tasks? Neither paper runs that comparison. (synthesis)
- Can a fixed-vocabulary model handle sequencing-based or single-cell methylomes, where covered CpGs vary per cell and rarely match array probes? (synthesis)
- Which of the 6- or 12-block configurations produced the reported results?

## Related

- [[delimacamillo-2024-cpgpt]] · [[liang-2025-scdnam-gpt]] · [[cui-2024-natmethods]] · [[epigenetic-aging]] · [[single-cell-foundation-model]] · [[40-Topics/dna-methylation]] · [[40-Topics/sequence-models-and-foundation-models]]
