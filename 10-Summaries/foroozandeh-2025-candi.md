---
type: summary
title: "Foroozandeh et al. 2025 — CANDI: self-supervised, confidence-aware denoising imputation of genomic data"
source: "[[00-Sources/papers/CANDI- self-supervised, confidence-aware denoising imputation of genomic data.pdf]]"
source_quality: full
source_sha256: "969c60ddf43ebc8b0eab44287875a1f8e6566a2931280128fcff4cbeaffab180"
source_kind: paper
author: "Mehdi Foroozandeh, Abdul Rahman Diab, Maxwell Libbrecht (corresponding author not marked)"
published: 2025-01-25
ingested: 2026-10-09
doi: "10.1101/2025.01.23.634626"
journal: "bioRxiv (preprint, v1, 25 January 2025)"
tags: [CANDI, epigenome-imputation, denoising, self-supervised-learning, masked-assay-modeling, transformer, uncertainty, calibration, negative-binomial, ENCODE, ENCODE-Imputation-Challenge, histone-modifications, bulk, zero-shot, preprint-text]
entities: []
concepts: ["[[imputation]]", "[[single-cell-foundation-model]]", "[[chip-seq]]", "[[dnase-seq]]", "[[atac-seq]]", "[[sequencing-depth-and-coverage]]", "[[cis-regulatory-element]]", "[[batch-effect]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/histone-modifications]]", "[[computational-methods]]"]
---

**Citation:** Foroozandeh et al. (2025) — *CANDI: self-supervised, confidence-aware denoising imputation of genomic data* — *bioRxiv* (preprint). [DOI](https://doi.org/10.1101/2025.01.23.634626)

# Foroozandeh 2025 — CANDI

> **Version note:** the source is the full bioRxiv v1 text (12 pages, posted 25 January 2025). It has Introduction, Results, a three-sentence Discussion and a full Methods section. It has no supplement and no limitations section. Figure values are images, so results below are reported as the text describes them.
>
> CANDI (Confidence-Aware Neural Denoising Imputer) is a **self-supervised transformer for bulk epigenome imputation** that includes **histone ChIP-seq marks**. It is trained on ENCODE bulk data: 35 assay types (histone marks, DNase-seq, ATAC-seq and others) over 361 merged cell types. For one 30-kb locus it takes the **raw read counts** of whatever assays exist in a cell type, four experimental covariates per assay and the DNA sequence. It outputs, for every assay, a negative binomial distribution over raw counts and a Gaussian over p-value signal. Training is BERT-like but masks **whole assays**, not positions, and adds a second task that recovers full-depth tracks from downsampled reads. The paper's pitch is three fixes to existing imputers: predict raw counts with covariates rather than idealised processed signal, denoise an existing low-quality experiment without retraining, and output calibrated uncertainty. Nothing here is single-cell.

## Key claims

- **Existing imputers model the wrong target.** All prior epigenome imputation methods, the authors say, work on processed signal (e.g. fold enrichment over control) and assume it is free of batch effects. In the ENCODE Imputation Challenge (EIC), subtle train–test differences meant a simple baseline beat most entrants. CANDI instead models raw counts and conditions on depth, read length, coverage and run type.
- **Denoising without retraining.** To denoise an experiment with current tools one must retrain without it and impute it de novo. Only ChromImpute avoids retraining, and it ignores the target assay itself. CANDI can take a low-quality existing track as input and predict a better one in a single pass.
- **Accuracy comparable to EIC winners.** With the EIC train–test split, CANDI matched Avocado, the average baseline and the challenge entries (Guacamole, Lavawizard, imp/eDICE, Hongyang Li and Yuanfang Guan v1) on Spearman correlation and MSE. It did so **without cell-type or position embeddings**: it sees only DNA sequence and the target cell type's observed assays.
- **Active marks are imputed best.** Genome-wide Pearson correlation exceeded 0.8 for H3K27ac and H3K4me3 "in many cell types". Raw-count prediction was more accurate than processed-signal prediction.
- **Zero-shot to unseen cell types.** On the extended dataset, whole cell types were held out (not just assays within a cell type), which the authors call a more realistic, cell type-agnostic test.
- **Calibrated aleatoric uncertainty.** Confidence intervals were near-perfectly calibrated at C ≥ 0.9 and conservative at lower levels. Part of the conservatism is discreteness: the predicted negative binomial median equals the observed count 38% of the time. High-signal (>90th percentile), high-confidence H3K4me3 bins overlapped TSSs significantly more than low-confidence or low-signal bins.
- **Which inputs predict which targets.** In an input-ablation heatmap (single assays, accessibility only, six core histone marks), DNase-seq and ATAC-seq predicted each other well, while H3K27me3 and H3K9me3 carried little information about active marks. The authors propose using this to prioritise which assays to run.

## Methods / evidence

**Data (all bulk).** (1) EIC: 35 assays × 50 biosamples. The authors re-fetched BAM files because EIC released only p-value bigWigs. (2) Extended ENCODE: every biosample with at least one of the 35 assays, 3,064 biosamples, merged by cell type into 361 cell types. Merging raised the median number of assays per sample from 1 to 6. Downsampling factors 1, 2 and 4 simulate shallower experiments. The six "core" histone marks named are H3K4me3, H3K4me1, H3K27ac, H3K27me3, H3K9me3 and H3K36me3. The full 35-assay list is not given in the text.

**Architecture.** 30-kb window at 25-bp resolution (1,200 positions). Encoder: depth-wise Conv1D tower on the 35 × 1,200 count matrix (3 layers, pool 2, expansion 3, giving 150 × 945); a separate Conv1D tower on one-hot DNA (two extra pool-5 layers to reach 150 positions); covariate embedding fused into the signal features; fusion with DNA features; 4 transformer encoder layers, 9 heads, relative positional encoding. Decoder: output-covariate embedding, then two deconvolution towers, one ending in a negative binomial layer (counts) and one in a Gaussian layer (signal). Batch size 50.

**Self-supervised training.** Loss is the sum of four negative log-likelihoods: {NB, Gaussian} × {imputation, upsampling}. Imputation masks random whole assays per cell type and predicts them from the rest. Upsampling predicts original-depth data from downsampled input. Training used 3,000 random non-overlapping 30-kb regions containing at least one ENCODE cCRE, 90 Mb in total (about 3% of the genome). Chromosome 21 was excluded and used for all testing, including the EIC comparison.

**Evaluation.** Genome-wide MSE, Pearson and Spearman on chr21; calibration curves; H3K4me3–TSS overlap as functional validation. Code: github.com/mehdiforoozandeh/EpiDenoise.

Weight: a short first preprint. The headline accuracy result is parity, not superiority, against EIC methods, and most results are shown as figures without numbers in the text. The "denoising an existing low-quality experiment" claim is motivated and built into training (upsampling loss) but not separately benchmarked in the Results. (synthesis)

## Limitations

**Authors' own:**
- The paper has no limitations section. The only self-described constraint is that the cell type-agnostic design (no cell-type or position embeddings) is "a more challenging problem" than methods that use such metadata.
- Lower-confidence intervals are conservatively biased, partly because count data are discrete.

**Reviewer notes:**
- Everything is bulk ENCODE data. Inputs are 25-bp count tracks per assay per cell type, so the model has no notion of single cells, per-cell sparsity or Tn5 open-chromatin bias, and it was not tested on CUT&Tag. (synthesis)
- Training covers only about 3% of the genome, chosen around cCREs, and testing is chromosome 21 only. Performance on heterochromatin and broad repressive domains, where H3K9me3 and H3K27me3 live, is not reported separately. (synthesis)
- The denoising and "supertrack" claims are not backed by a dedicated experiment, such as comparing CANDI output from a downsampled track with the full-depth original across marks. (synthesis)

## Surprising or load-bearing bits

- **This is the nearest thing to a histone-inclusive pretrained epigenome model in the wiki's 2025 set.** It is self-supervised, masks whole assays, and trains jointly on histone marks and accessibility. But it is bulk, ENCODE-scale (361 cell types), and the authors never call it a foundation model. (synthesis)
- **Masking assays, not tokens.** The pretext task is the imputation task itself, so pretraining and the downstream use coincide. That differs from sequence foundation models, where pretraining is generic and use is fine-tuned. (synthesis)
- **Raw counts plus covariates.** Modelling sequencing depth explicitly is what lets one model both impute and upsample. The same idea would be needed for single-cell histone data, where depth per cell varies by orders of magnitude. (synthesis)
- **Repressive marks are weak predictors of active ones.** H3K27me3 and H3K9me3 inputs add little for active-mark targets, which bounds how far multi-mark imputation can go when only repressive marks are measured.

## Concepts touched

- [[imputation]] — bulk cross-assay epigenome imputation reframed as self-supervised masked-assay prediction with calibrated uncertainty.
- [[single-cell-foundation-model]] — a bulk, histone-inclusive, self-supervised counterpart; no single-cell histone model exists to compare it with. (synthesis)
- [[chip-seq]] — histone ChIP-seq tracks are the main training targets; raw counts are modelled instead of fold enrichment.
- [[dnase-seq]] / [[atac-seq]] — accessibility assays predict each other well and are inputs alongside histone marks.
- [[sequencing-depth-and-coverage]] — depth is a model covariate and downsampling is a training task.
- [[cis-regulatory-element]] — training loci are 30-kb windows containing ENCODE cCREs.
- [[batch-effect]] — the motivation: processed signal does not remove batch differences.

## Connections to other sources

- Closest bulk context-conditional model: [[gao-2024-epigept]] (EpiGePT) predicts epigenomic tracks in new cell types from sequence plus a TF-expression context vector. CANDI instead uses the cell type's own observed assays as context. (synthesis)
- Sequence-to-function models that predict histone ChIP-seq from DNA alone — [[avsec-2021-enformer]], [[avsec-2026-alphagenome]] — are supervised on fixed cell types; CANDI adds observed assays as input and is self-supervised. (synthesis)
- Earlier histone-mark prediction from sequence: [[yin-2019-deephistone]]. (synthesis)
- The single-cell histone gap it does not address is mapped by [[morenogonzalez-2025-schistone-imputation]], which benchmarks only non-pretrained scRNA/scATAC imputers on scHPTM data. (synthesis)
- Single-cell accessibility foundation models ([[wu-2025-epifoundation]]) exist, so the missing piece is specifically single-cell histone data. (synthesis)

## Open questions

- Would the same masked-assay, depth-aware design work on single-cell histone data (scCUT&Tag, sortChIC), where each cell has one or two marks at hundreds to thousands of reads? (synthesis)
- How does CANDI do on broad repressive domains genome-wide, outside cCRE-containing windows? (synthesis)
- Has a later version benchmarked the denoising use directly, or compared with ChromImpute's re-imputation?

## Related

- [[imputation]] · [[40-Topics/histone-modifications]] · [[40-Topics/sequence-models-and-foundation-models]] · [[single-cell-foundation-model]] · [[gao-2024-epigept]] · [[morenogonzalez-2025-schistone-imputation]]
