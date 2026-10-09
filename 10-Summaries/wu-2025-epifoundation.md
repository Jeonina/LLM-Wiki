---
type: summary
title: "Wu et al. 2025 — EpiFoundation: A Foundation Model for Single-Cell ATAC-seq via Peak-to-Gene Alignment"
source: "[[00-Sources/papers/EpiFoundation- A Foundation Model for Single-Cell ATAC-seq via Peak-to-Gene Alignment.pdf]]"
source_quality: full
source_sha256: "f1487e066397eeac3d2b813993913a7d28d9eee1ec95a5dc2c32ba7879c3c3c7"
source_kind: paper
author: "Juncheng Wu, Changxin Wan, Zhicheng Ji (corresponding), Yuyin Zhou (corresponding), Wenpin Hou (corresponding)"
published: 2025-02 (clipped text = bioRxiv version posted 2025-09-28)
ingested: 2026-10-08
doi: "10.1101/2025.02.05.636688"
journal: "bioRxiv preprint"
tags: [EpiFoundation, scATAC-seq, foundation-model, transformer, 10x-Multiome, peak-to-gene-alignment, MiniAtlas, non-zero-peaks, batch-correction, cell-type-annotation, gene-expression-prediction, preprint-text]
entities: []
concepts: ["[[single-cell-foundation-model]]", "[[genomic-tokenization]]", "[[scatac-seq]]", "[[batch-effect]]", "[[cell-type-annotation]]", "[[joint-single-cell-multi-omics]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/single-cell-atac-seq]]"]
---

**Citation:** Wu et al. (2025) — *EpiFoundation: A Foundation Model for Single-Cell ATAC-seq via Peak-to-Gene Alignment* — *bioRxiv preprint*. [DOI](https://doi.org/10.1101/2025.02.05.636688)

# Wu 2025 — EpiFoundation

> **Version note:** the clipped text is the bioRxiv version posted 28 September 2025.
>
> EpiFoundation is a transformer **pretrained on single-cell multiome data** (paired scATAC + scRNA from the same cell). Its input is scATAC only; RNA is used solely as the training target. Each cell is fed in as the set of its **non-zero peaks**, up to 12,000, which covers all non-zero peaks for more than 95% of cells. Each token is a learned peak-ID embedding plus a chromosome embedding. There is no DNA sequence and no genomic position within the chromosome. Instead of masked-peak prediction, the [CLS] cell embedding, concatenated with a batch embedding, is trained to predict **binary expression** of 8,000 sampled genes from the paired RNA ("peak-to-gene alignment"). The training set is a curated 10x Multiome "MiniAtlas" of over 100,000 cells from 19 tissues and 56 cell types. After fine-tuning, the model reports cell-type annotation accuracy of 0.76–0.91, beats PCA, Harmony, LIGER and scANVI on most integration metrics, and roughly doubles gene-expression correlation compared with Signac Gene Activity.

## Key claims

- **Only non-zero peaks matter.** The authors argue that knowing which peaks are open is enough to represent a cell. Dropping zero peaks raises the density of cell-specific information and keeps sequence length manageable.
- **RNA supervision instead of peak reconstruction.** scATAC data are sparse, which makes peak-to-peak correlations hard to learn. Predicting binary gene expression gives a dense target. Each cell's 8,000 sampled genes are balanced between expressed and non-expressed.
- **Cell-type annotation (fine-tuned).** Accuracy, macro-F1 and ROC-AUC were: kidney 0.9135, 0.7081, 0.9866; PBMC 0.8837, 0.6299, 0.9764; BMMC 0.7615, 0.5026, 0.9758; ALLTissue 0.8423, 0.6934, 0.978. No baseline annotation methods are reported.
- **Batch correction.** Using embeddings from the cell-type fine-tuned model, EpiFoundation had the best NMI, cASW, bASW and graph connectivity on all three tissues. For example, kidney NMI was 0.5681 against 0.3273 for PCA, and GC was 0.8267 against 0.7732 for scANVI. It was not best on isolated-label score in kidney (scANVI 0.5668 vs 0.4995) or PBMC (PCA 0.7462 vs 0.6377).
- **Gene-expression prediction.** Fine-tuned to predict 10-level binned expression of protein-coding genes, mean per-gene Pearson was 0.38–0.48 (Spearman 0.37–0.42), against about 0.16–0.20 for Signac Gene Activity. MSE was lower on every dataset (e.g. PBMC 6.76 vs 10.21).
- **Ablation.** On kidney batch correction, removing the batch label lowered NMI from 0.5681 to 0.4695, and removing chromosome embeddings lowered it to 0.4354. bASW changed little (0.8891–0.9069).

## Methods / evidence

Data: 10x Multiome FASTQs from GEO and ENCODE, processed with Cell Ranger ARC 2.0.1 on GRCh38. Peaks were called on pooled fragments with MACS2, and the count matrix was built with Signac and binarised. Cell QC used RNA and ATAC read bounds, nucleosome signal < 2 and TSS enrichment > 1. Cell-type labels came from WNN clustering (Seurat) and Spearman matching to DISCO reference profiles. Model: 6 transformer blocks (FlashAttention-2), 8 heads, 512-d, dropout 0.15. Trained 140 epochs with Adam, learning rate 1e-4 with cosine schedule, batch size 8 × 20 accumulation steps. Batch embeddings are used only in pretraining. Downstream: separate decoders for cell type (cross-entropy) and binned expression (MSE). Evaluation sets (kidney, PBMC, BMMC, ALLTissue) are split randomly into fine-tuning and test parts. Code and data: github.com/UCSC-VLAA/EpiFoundation.

Weight: a compact, conference-style paper with tabulated metrics. However, cell-type annotation has no baseline, and expression prediction is compared only with Gene Activity, the simplest option. The "batch-corrected" embedding comes from a model fine-tuned on cell-type labels and pretrained with batch labels, then compared with unsupervised PCA, Harmony and LIGER. That favours EpiFoundation on label-based conservation metrics. (synthesis)

## Limitations

**Authors' own:**
- Future work is a broader single-cell foundation model that unifies scRNA-seq, scATAC-seq and nucleotide sequence. The current model uses none of the DNA sequence.

**Reviewer notes:**
- Pretraining needs paired multiome data, so the corpus is about 100k cells, one to two orders of magnitude below other scATAC foundation models. It also cannot pretrain on the much larger pool of ATAC-only atlases. (synthesis)
- Peaks are dataset-specific MACS2 calls embedded by ID. A new dataset must be mapped to the MiniAtlas peak set, and peaks outside it are lost. This is not discussed. (synthesis)
- Table 4's caption says performance drops when both batch and chromosome information are removed, but the table only shows removing one at a time. The ALLTissue test set "encompasses all tissues of the training set", and the paper does not say whether its cells or donors are separate from the pretraining data. (synthesis)

## Surprising or load-bearing bits

- **Cross-modal pretraining as the objective.** Instead of reconstructing masked peaks (CLM-access) or detecting replaced regions (Atacformer), EpiFoundation learns ATAC representations by predicting RNA. This builds the gene link into the embedding, at the cost of needing paired data. (synthesis)
- **Chromosome identity helps.** The only positional signal is which chromosome a peak is on, and removing it hurt NMI more than removing batch labels.
- **Gene Activity is a weak baseline.** Per-gene correlation of about 0.17 for the standard Signac approach shows how little naive promoter-window summing captures.

## Concepts touched

- [[single-cell-foundation-model]] — scATAC foundation model with RNA-supervised pretraining.
- [[genomic-tokenization]] — non-zero peak-ID tokens plus chromosome embeddings, at most 12,000 per cell.
- [[scatac-seq]] — input modality; peaks binarised.
- [[batch-effect]] — scIB-style integration metrics against PCA, Harmony, LIGER and scANVI.
- [[cell-type-annotation]] — fine-tuned classification on kidney, PBMC, BMMC and all tissues.
- [[joint-single-cell-multi-omics]] — 10x Multiome MiniAtlas as the training resource.

## Connections to other sources

- Other scATAC foundation models in this ingest: [[leroy-2025-atacformer]], [[liu-2025-clm-access]] and [[li-2026-epizoo]]. EpiFoundation is the only one that uses RNA as the pretraining target. (synthesis)
- Pseudobulk regulatory foundation model it contrasts itself with: [[fu-2025-get]] (GET), which gives up single-cell resolution.
- Baselines and related tools: [[ashuach-2023-multivi]], [[xiong-2019-scale]]. scRNA foundation-model template, including the batch-embedding trick: [[cui-2024-natmethods]].
- Benchmark context for scATAC embeddings: [[luo-2024-scatac-benchmark]].

## Open questions

- How does EpiFoundation compare with ATAC-only pretrained models of much larger size (Atacformer, CLM-access, EpiAgent) on the same annotation and integration tasks? (synthesis)
- Can the peak-to-gene objective be combined with ATAC-only self-supervision so that unpaired atlases can also be used? (synthesis)
- How well does the model transfer to tissues outside the 19 in MiniAtlas, or to non-10x scATAC chemistries?

## Related

- [[leroy-2025-atacformer]] · [[liu-2025-clm-access]] · [[li-2026-epizoo]] · [[fu-2025-get]] · [[scatac-seq]] · [[single-cell-foundation-model]] · [[40-Topics/single-cell-atac-seq]] · [[40-Topics/sequence-models-and-foundation-models]]
