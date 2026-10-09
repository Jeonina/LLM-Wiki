---
type: concept
title: Single-cell foundation model
aliases: [scFM, single-cell FM, epigenome foundation model, cell language model, scATAC foundation model, methylation foundation model]
tags: [foundation-model, single-cell, scATAC-seq, DNA-methylation, multi-omics, transfer-learning]
created: 2026-10-08
updated: 2026-10-09
---

# Single-cell foundation model

> A model pretrained on a large corpus of single-cell (or bulk epigenomic) profiles to produce cell or region embeddings that transfer to new datasets and tasks; this wiki tracks the ones built on DNA layers — accessibility, methylation and 3D contacts — and their RNA+ATAC multimodal versions ([[10-Summaries/leroy-2025-atacformer]]; [[10-Summaries/liang-2025-scdnam-gpt]]; [[10-Summaries/liu-2025-scarf]]).

## Definition

Transcriptome models such as scGPT set the pattern: tokenise each cell, pretrain with a masked or contrastive objective, then fine-tune ([[10-Summaries/cui-2024-natmethods]]). The DNA-layer versions differ mainly in what a token is — a consensus region (Atacformer), a patch of cCREs (CLM-access), a non-zero peak (EpiFoundation), a CpG-centred 6-mer (scDNAm-GPT), a Hi-C image patch (HiCFoundation) or a region plus its DNA-LM sequence embedding (EpiZoo) ([[10-Summaries/leroy-2025-atacformer]]; [[10-Summaries/liu-2025-clm-access]]; [[10-Summaries/wu-2025-epifoundation]]; [[10-Summaries/liang-2025-scdnam-gpt]]; [[10-Summaries/wang-2026-hicfoundation]]; [[10-Summaries/li-2026-epizoo]]). See [[genomic-tokenization]].

## Why it matters

- DNA-layer single-cell data are sparse (see [[scatac-imputation]]), and pretraining on millions of cells is one way to borrow strength across datasets: EpiZoo is pretrained on ~20.9M scATAC cells and scDNAm-GPT on ~1M single-cell methylomes ([[10-Summaries/li-2026-epizoo]]; [[10-Summaries/liang-2025-scdnam-gpt]]).
- The multimodal models are the first to pretrain jointly on RNA and accessibility ([[10-Summaries/liu-2025-scarf]]; [[10-Summaries/li-2026-clm-x]]; [[10-Summaries/liu-2025-scmomer]]; [[10-Summaries/yu-2026-scdynomics]]), which bears on [[multimodal-integration-methods]].
- **Layer coverage is uneven** (synthesis): this set has accessibility, methylation and 3D models but no histone-modification model and no genotype-layer (CNV/SNV) model.

## Variants and refinements

- *scATAC:* Atacformer, CLM-access, EpiFoundation, EpiZoo; GET pretrains on pseudobulk scATAC of 213 cell types ([[10-Summaries/fu-2025-get]]).
- *DNA methylation:* scDNAm-GPT is pretrained on single cells; CpGPT and MethylGPT are pretrained on bulk array data ([[10-Summaries/liang-2025-scdnam-gpt]]; [[10-Summaries/delimacamillo-2024-cpgpt]]; [[10-Summaries/ying-2024-methylgpt]]).
- *3D genome:* HiCFoundation is pretrained on bulk Hi-C and fine-tuned for scHi-C ([[10-Summaries/wang-2026-hicfoundation]]).
- *RNA + ATAC:* SCARF needs truly paired multiome cells; scMomer and CLM-X pretrain their fusion on pseudo-paired cells matched only by cell-type label; scDynOmics uses mouse multiome with promoter-level ATAC ([[10-Summaries/liu-2025-scarf]]; [[10-Summaries/liu-2025-scmomer]]; [[10-Summaries/li-2026-clm-x]]; [[10-Summaries/yu-2026-scdynomics]]).

**Models in this wiki** (14, by year):

- **CpGPT** (2024) — CpGPT is a methylation foundation model pretrained only on bulk human array data (CpGCorpus, 155,151 samples), and it reaches single cells only through fine-tuning on sciMETv3, where it scored AUPRC 0.909 against 0.897 for DeepCpG, while DeepCpG kept the best AUROC ([[10-Summaries/delimacamillo-2024-cpgpt]]).
- **MethylGPT** (2024) — MethylGPT applies the scGPT design (token = CpG ID plus value embedding, masked-value and CLS-reconstruction losses) to 154,063 bulk array methylomes; single-cell methylation is listed only as future work ([[10-Summaries/ying-2024-methylgpt]]).
- **Atacformer** (2025) — Atacformer is a lightweight scATAC foundation model pretrained on single cells with ELECTRA replaced-token detection; a triplet-loss fine-tune raised PBMC clustering ARI by about 15%, and the CRAFT RNA–ATAC variant clustered best and fastest on PBMC5k ([[10-Summaries/leroy-2025-atacformer]]).
- **CLM-access** (2025) — CLM-access is a 20M-parameter scATAC cell language model pretrained on about 2.8M human cells; after fine-tuning it beat scATAnno and Cellcano on annotation (accuracy 0.76 and 0.75) and BABEL and MultiVI on RNA prediction (Pearson 0.918) ([[10-Summaries/liu-2025-clm-access]]).
- **EpiFoundation** (2025) — EpiFoundation pretrains a scATAC encoder by predicting each cell's paired binary gene expression ('peak-to-gene alignment') on a 100k-cell 10x Multiome MiniAtlas, rather than by reconstructing masked peaks ([[10-Summaries/wu-2025-epifoundation]]).
- **GET** (2025) — GET is pretrained by masked reconstruction of motif features over 200-peak windows from pseudobulk scATAC-seq of 213 human fetal and adult cell types, then fine-tuned for expression; it reaches Pearson 0.94 on held-out astrocytes, and only 0.6 without pretraining ([[10-Summaries/fu-2025-get]]).
- **OmniReg-GPT** (2025) — A frozen DNA language model with one per-cell classification layer predicted Buenrostro-2018 single-cell chromatin accessibility at mean AUROC 0.717 and beat scBasset, SnapATAC, ArchR and chromVAR on ARI, AMI and homogeneity when its classifier weights were used as cell embeddings ([[10-Summaries/wang-2025-omnireg-gpt]]).
- **SCARF** (2025) — SCARF pretrains modality-specific masked-reconstruction encoders on 2.7 M truly paired human 10x Multiome cells (454 GEO profiles, 21 tissues, one 1.74 M-peak reference) and aligns RNA and ATAC [CLS] embeddings with a CLIP-style contrastive loss, so paired multiome data are required ([[10-Summaries/liu-2025-scarf]])
- **scDNAm-GPT** (2025) — scDNAm-GPT is pretrained directly on about 1 million single-cell whole-genome bisulfite methylomes (human and mouse, brain-heavy), and pretraining raised average cell-type accuracy on four unseen datasets from 60.7% to 83.7% ([[10-Summaries/liang-2025-scdnam-gpt]]).
- **scMomer** (2025) — scMomer combines unimodal masked pretraining (scBERT for RNA, an scCLIP-style ViT for peak patches), fusion on 377,134 cell-type-matched pseudo-paired fetal cells, and distillation of a feed-forward student that predicts the ATAC embedding from RNA, so only RNA is needed at inference ([[10-Summaries/liu-2025-scmomer]])
- **CLM-X** (2026) — CLM-X uses shared self-attention with RNA, ATAC and fusion FFN experts, pretrained in stages on ~36 M CELLxGENE scRNA-seq cells, ~2.8 M CATlas/Descartes scATAC cells and 377,134 scCLIP pseudo-paired cells; no truly paired multiome data enter pretraining ([[10-Summaries/li-2026-clm-x]])
- **EpiZoo** (2026) — EpiZoo is a 2.6B-parameter mixture-of-experts scATAC foundation model pretrained on about 20.9M human and mouse cells; after post-training it beat baselines in macaque, zebrafish, fly and maize (gains of 7.0% and 11.2% NMI in fly and maize) ([[10-Summaries/li-2026-epizoo]]).
- **HiCFoundation** (2026) — HiCFoundation pretrains a 304M-parameter ViT masked autoencoder on Hi-C submatrices with a patchwise contrastive + SSIM loss, then fine-tunes only small task decoders; without pretraining, every task performed worse and training was about 10× slower ([[10-Summaries/wang-2026-hicfoundation]]).
- **scDynOmics** (2026) — scDynOmics pretrains a ~78–80 M-parameter whole-coding-genome Linformer (latent l = 500, with alternating TF-restricted and full-gene layers) on 752,155 mouse multiome cells, with ATAC collapsed to per-gene pan-promoter counts (−1.5 kb to +0.5 kb of TSS) ([[10-Summaries/yu-2026-scdynomics]])

## Contested points

- **Pseudo-pairs versus true pairs.** scMomer and CLM-X train cross-modal fusion on cells paired only by label ([[10-Summaries/liu-2025-scmomer]]; [[10-Summaries/li-2026-clm-x]]), while SCARF requires 2.7M truly paired cells ([[10-Summaries/liu-2025-scarf]]); no study here compares the two directly (synthesis).
- **Coordinates versus sequence.** Atacformer uses no DNA sequence at all ([[10-Summaries/leroy-2025-atacformer]]), whereas EpiZoo argues the sequence component is what transfers across species ([[10-Summaries/li-2026-epizoo]]).
- **Bulk-trained models on single cells.** Fine-tuned on sciMETv3 cells, bulk-pretrained CpGPT beat DeepCpG on AUPRC but not AUROC ([[10-Summaries/delimacamillo-2024-cpgpt]]; [[10-Summaries/angermueller-2017-genomebiol]]).
- **Weak baselines.** EpiFoundation's cell-type annotation has no baselines, and scDynOmics gives no numbers for its foundation-model comparison ([[10-Summaries/wu-2025-epifoundation]]; [[10-Summaries/yu-2026-scdynomics]]).

## Added 2026-10-09 — foundation-model gap evidence

- CoT is a transformer on scDNA-seq read counts, but it is trained per dataset with no pretraining corpus or reusable weights, which leaves the single-cell genotype layer without a foundation model ([[10-Summaries/liu-2024-cot]])
- CANDI is a bulk counterpart and not a single-cell model: a transformer trained self-supervised by masking whole assays (histone ChIP-seq, DNase-seq, ATAC-seq) across 361 ENCODE cell types, which can impute unseen cell types zero-shot ([[10-Summaries/foroozandeh-2025-candi]])
- As of late 2025 no pretrained model existed for single-cell histone modification data: the first scHPTM imputation benchmark tested only scRNA/scATAC tools (SAVER, scImpute, MAGIC, scOpen, SCALE, cisTopic and others) ([[10-Summaries/morenogonzalez-2025-schistone-imputation]])
- MutationProjector pretrains a graph-attention model by masked-gene reconstruction on 30,328 bulk GENIE and TCGA tumours and reuses the frozen embedding for immunotherapy, chemotherapy, metastasis and tissue-of-origin prediction, but it has no single-cell counterpart ([[10-Summaries/kong-2026-mutationprojector]])
- TESSERA shows that a self-supervised genotype foundation model exists at bulk-tumour resolution: it pretrains on TCGA WES SNVs and ABSOLUTE copy-number segments and is reused frozen across tasks, but it embeds one bulk profile per tumour, not cells ([[10-Summaries/sidhom-2026-tessera]])

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[multimodal-integration-methods]] · [[scatac-imputation]] · [[cell-type-annotation]] · [[batch-effect]]
- [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/single-cell-atac-seq]] · [[40-Topics/dna-methylation]] · [[40-Topics/3d-genome]] · [[40-Topics/single-cell-multiomics]]
