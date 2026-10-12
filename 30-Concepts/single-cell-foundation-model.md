---
type: concept
title: Single-cell foundation model
aliases: [scFM, single-cell FM, epigenome foundation model, cell language model, scATAC foundation model, methylation foundation model]
tags: [foundation-model, single-cell, scATAC-seq, DNA-methylation, multi-omics, transfer-learning]
created: 2026-10-08
updated: 2026-10-12
---

# Single-cell foundation model

> A model pretrained on a large corpus of single-cell (or bulk epigenomic) profiles to produce cell or region embeddings that transfer to new datasets and tasks; this wiki tracks the ones built on DNA layers — accessibility, methylation and 3D contacts — and their RNA+ATAC multimodal versions ([[10-Summaries/leroy-2025-atacformer|Atacformer]]; [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]; [[10-Summaries/liu-2025-scarf|SCARF]]).

> [!abstract] 한눈에
> Single-cell foundation model은 대량의 single-cell(또는 bulk epigenome) profile로 사전학습해 새 데이터셋과 과제에 옮겨 쓸 수 있는 cell·region embedding을 만드는 모델이며, DNA 층에서는 accessibility, methylation, 3D contact 모델이 나와 있다 ([[10-Summaries/leroy-2025-atacformer|Atacformer]]; [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]; [[10-Summaries/wang-2026-hicfoundation|HiCFoundation]]). 반면 single-cell histone과 genotype(CNV/SNV) 층에는 아직 사전학습 모델이 없다 ([[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025]]; [[10-Summaries/liu-2024-cot|CoT]]).

## Definition

Transcriptome models such as scGPT set the pattern: tokenise each cell, pretrain with a masked or contrastive objective, then fine-tune ([[10-Summaries/cui-2024-natmethods|scGPT]]). The DNA-layer versions differ mainly in what a token is — a consensus region (Atacformer), a patch of cCREs (CLM-access), a non-zero peak (EpiFoundation), a CpG-centred 6-mer (scDNAm-GPT), a Hi-C image patch (HiCFoundation) or a region plus its DNA-LM sequence embedding (EpiZoo) ([[10-Summaries/leroy-2025-atacformer|Atacformer]]; [[10-Summaries/liu-2025-clm-access|CLM-access]]; [[10-Summaries/wu-2025-epifoundation|EpiFoundation]]; [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]; [[10-Summaries/wang-2026-hicfoundation|HiCFoundation]]; [[10-Summaries/li-2026-epizoo|EpiZoo]]). See [[genomic-tokenization]].

## Why it matters

- DNA-layer single-cell data are sparse (see [[scatac-imputation]]), and pretraining on millions of cells is one way to borrow strength across datasets: EpiZoo is pretrained on ~20.9M scATAC cells and scDNAm-GPT on ~1M single-cell methylomes ([[10-Summaries/li-2026-epizoo|EpiZoo]]; [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]).
- The multimodal models are the first to pretrain jointly on RNA and accessibility ([[10-Summaries/liu-2025-scarf|SCARF]]; [[10-Summaries/li-2026-clm-x|CLM-X]]; [[10-Summaries/liu-2025-scmomer|scMomer]]; [[10-Summaries/yu-2026-scdynomics|scDynOmics]]), which bears on [[multimodal-integration-methods]].
- **Layer coverage is uneven** (synthesis): this set has accessibility, methylation and 3D models; histone marks appear only as channels in bulk models such as ChromBERT ([[10-Summaries/yu-2026-chrombert|ChromBERT]]), and there is no single-cell histone or genotype-layer (CNV/SNV) model — see [Layer coverage](#layer-coverage-and-bulk-counterparts).

## Models by layer

### Chromatin accessibility (scATAC)

Atacformer, CLM-access, EpiFoundation and EpiZoo are scATAC models; GET pretrains on pseudobulk scATAC of 213 cell types ([[10-Summaries/fu-2025-get|GET]]).

| Model | Year | Pretraining data | Token / objective | Key result | Source |
|---|---|---|---|---|---|
| Atacformer | 2025 | Single cells | Consensus region; ELECTRA replaced-token detection; no DNA sequence | Lightweight; a triplet-loss fine-tune raised PBMC clustering ARI by about 15%, and the CRAFT RNA–ATAC variant clustered best and fastest on PBMC5k | ([[10-Summaries/leroy-2025-atacformer\|Atacformer]]) |
| CLM-access | 2025 | About 2.8M human cells | Patch of cCREs | 20M parameters; after fine-tuning beat scATAnno and Cellcano on annotation (accuracy 0.76 and 0.75) and BABEL and MultiVI on RNA prediction (Pearson 0.918) | ([[10-Summaries/liu-2025-clm-access\|CLM-access]]) |
| EpiFoundation | 2025 | 100k-cell 10x Multiome MiniAtlas | Non-zero peak; predicts each cell's paired binary gene expression ("peak-to-gene alignment") rather than reconstructing masked peaks | — | ([[10-Summaries/wu-2025-epifoundation\|EpiFoundation]]) |
| GET | 2025 | Pseudobulk scATAC-seq of 213 human fetal and adult cell types | Masked reconstruction of motif features over 200-peak windows, then fine-tuned for expression | Pearson 0.94 on held-out astrocytes, and only 0.6 without pretraining | ([[10-Summaries/fu-2025-get\|GET]]) |
| OmniReg-GPT | 2025 | DNA sequence (a frozen DNA language model) | One per-cell classification layer on the frozen model | Predicted Buenrostro-2018 single-cell accessibility at mean AUROC 0.717; its classifier weights as cell embeddings beat scBasset, SnapATAC, ArchR and chromVAR on ARI, AMI and homogeneity | ([[10-Summaries/wang-2025-omnireg-gpt\|OmniReg-GPT]]) |
| EpiZoo | 2026 | About 20.9M human and mouse cells | Region plus its DNA-LM sequence embedding; 2.6B-parameter mixture of experts | After post-training beat baselines in macaque, zebrafish, fly and maize (NMI gains of 7.0% in fly and 11.2% in maize) | ([[10-Summaries/li-2026-epizoo\|EpiZoo]]) |

### DNA methylation

scDNAm-GPT is pretrained on single cells; CpGPT and MethylGPT are pretrained on bulk array data ([[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]; [[10-Summaries/delimacamillo-2024-cpgpt|CpGPT]]; [[10-Summaries/ying-2024-methylgpt|MethylGPT]]).

| Model | Year | Pretraining data | Token / objective | Key result | Source |
|---|---|---|---|---|---|
| CpGPT | 2024 | Bulk human arrays only (CpGCorpus, 155,151 samples) | — | Reaches single cells only through fine-tuning on sciMETv3: AUPRC 0.909 vs 0.897 for DeepCpG, while DeepCpG kept the best AUROC | ([[10-Summaries/delimacamillo-2024-cpgpt\|CpGPT]]; [[10-Summaries/angermueller-2017-genomebiol\|DeepCpG]]) |
| MethylGPT | 2024 | 154,063 bulk array methylomes | scGPT design: token = CpG ID plus value embedding; masked-value and CLS-reconstruction losses | Single-cell methylation listed only as future work | ([[10-Summaries/ying-2024-methylgpt\|MethylGPT]]) |
| scDNAm-GPT | 2025 | About 1 million single-cell whole-genome bisulfite methylomes (human and mouse, brain-heavy) | CpG-centred 6-mer | Pretraining raised average cell-type accuracy on four unseen datasets from 60.7% to 83.7% | ([[10-Summaries/liang-2025-scdnam-gpt\|scDNAm-GPT]]) |

### 3D genome

| Model | Year | Pretraining data | Token / objective | Key result | Source |
|---|---|---|---|---|---|
| HiCFoundation | 2026 | Bulk Hi-C submatrices; fine-tuned for scHi-C | Hi-C image patch; 304M-parameter ViT masked autoencoder with a patchwise contrastive + SSIM loss; only small task decoders are fine-tuned | Without pretraining every task performed worse and training was about 10× slower | ([[10-Summaries/wang-2026-hicfoundation\|HiCFoundation]]) |

### RNA + ATAC multimodal

SCARF needs truly paired multiome cells; scMomer and CLM-X pretrain their fusion on pseudo-paired cells matched only by cell-type label; scDynOmics uses mouse multiome with promoter-level ATAC ([[10-Summaries/liu-2025-scarf|SCARF]]; [[10-Summaries/liu-2025-scmomer|scMomer]]; [[10-Summaries/li-2026-clm-x|CLM-X]]; [[10-Summaries/yu-2026-scdynomics|scDynOmics]]).

| Model | Year | Pretraining data | Pairing | Design | Source |
|---|---|---|---|---|---|
| SCARF | 2025 | 2.7 M human 10x Multiome cells (454 GEO profiles, 21 tissues, one 1.74 M-peak reference) | Truly paired; paired multiome data are required | Modality-specific masked-reconstruction encoders; RNA and ATAC [CLS] embeddings aligned with a CLIP-style contrastive loss | ([[10-Summaries/liu-2025-scarf\|SCARF]]) |
| scMomer | 2025 | Unimodal pretraining, then fusion on 377,134 fetal cells | Pseudo-paired by cell type | scBERT for RNA, an scCLIP-style ViT for peak patches; a distilled feed-forward student predicts the ATAC embedding from RNA, so only RNA is needed at inference | ([[10-Summaries/liu-2025-scmomer\|scMomer]]) |
| CLM-X | 2026 | ~36 M CELLxGENE scRNA-seq cells, ~2.8 M CATlas/Descartes scATAC cells and 377,134 scCLIP pseudo-paired cells, in stages | Pseudo-paired; no truly paired multiome data enter pretraining | Shared self-attention with RNA, ATAC and fusion FFN experts | ([[10-Summaries/li-2026-clm-x\|CLM-X]]) |
| scDynOmics | 2026 | 752,155 mouse multiome cells | Mouse multiome, ATAC at promoter level | ~78–80 M-parameter whole-coding-genome Linformer (latent l = 500, alternating TF-restricted and full-gene layers); ATAC collapsed to per-gene pan-promoter counts (−1.5 kb to +0.5 kb of TSS) | ([[10-Summaries/yu-2026-scdynomics\|scDynOmics]]) |

## Layer coverage and bulk counterparts

Where no single-cell foundation model exists, the nearest models are bulk or per-dataset:

| Layer | Nearest model | Why it is not a single-cell FM | Source |
|---|---|---|---|
| Histone modification | ChromBERT | Pretrained only on bulk Cistrome profiles (6,391 ChIP-seq, DNase-seq and ATAC-seq cistromes in 1-kb bins, no DNA sequence); reaches single cells only through scGPT transcriptome prompts and pseudobulk PBMC fine-tuning | ([[10-Summaries/yu-2026-chrombert\|ChromBERT]]) |
| Histone modification | CANDI | A bulk transformer trained self-supervised by masking whole assays (histone ChIP-seq, DNase-seq, ATAC-seq) across 361 ENCODE cell types; can impute unseen cell types zero-shot | ([[10-Summaries/foroozandeh-2025-candi\|CANDI]]) |
| Histone modification (single-cell) | None | As of late 2025 no pretrained model existed for single-cell histone data: the first scHPTM imputation benchmark tested only scRNA/scATAC tools (SAVER, scImpute, MAGIC, scOpen, SCALE, cisTopic and others) | ([[10-Summaries/morenogonzalez-2025-schistone-imputation\|Moreno-González 2025]]) |
| Genotype: scDNA-seq read counts | CoT | A transformer trained per dataset, with no pretraining corpus or reusable weights | ([[10-Summaries/liu-2024-cot\|CoT]]) |
| Genotype: bulk tumour mutations | MutationProjector | Graph-attention model pretrained by masked-gene reconstruction on 30,328 bulk GENIE and TCGA tumours; the frozen embedding is reused for immunotherapy, chemotherapy, metastasis and tissue-of-origin prediction, but there is no single-cell counterpart | ([[10-Summaries/kong-2026-mutationprojector\|MutationProjector]]) |
| Genotype: bulk tumour SNVs and CNAs | TESSERA | Self-supervised, pretrained on TCGA WES SNVs and ABSOLUTE copy-number segments and reused frozen across tasks, but it embeds one bulk profile per tumour, not cells | ([[10-Summaries/sidhom-2026-tessera\|TESSERA]]) |

## Evidence and examples

- Pretraining matters for transfer: GET's held-out astrocyte Pearson fell from 0.94 to 0.6 without it ([[10-Summaries/fu-2025-get|GET]]), scDNAm-GPT's cell-type accuracy on unseen datasets rose from 60.7% to 83.7% with it ([[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]), and HiCFoundation without pretraining did worse on every task and trained about 10× slower ([[10-Summaries/wang-2026-hicfoundation|HiCFoundation]]).
- Cross-species transfer: post-trained EpiZoo gained 7.0% and 11.2% NMI in fly and maize ([[10-Summaries/li-2026-epizoo|EpiZoo]]).
- A self-supervised genotype foundation model exists at bulk-tumour resolution (TESSERA), which leaves the single-cell genotype layer as the gap ([[10-Summaries/sidhom-2026-tessera|TESSERA]]; [[10-Summaries/liu-2024-cot|CoT]]).

## Contested points

- **Pseudo-pairs versus true pairs.** scMomer and CLM-X train cross-modal fusion on cells paired only by label ([[10-Summaries/liu-2025-scmomer|scMomer]]; [[10-Summaries/li-2026-clm-x|CLM-X]]), while SCARF requires 2.7M truly paired cells ([[10-Summaries/liu-2025-scarf|SCARF]]); no study here compares the two directly (synthesis).
- **Coordinates versus sequence.** Atacformer uses no DNA sequence at all ([[10-Summaries/leroy-2025-atacformer|Atacformer]]), whereas EpiZoo argues the sequence component is what transfers across species ([[10-Summaries/li-2026-epizoo|EpiZoo]]).
- **Bulk-trained models on single cells.** Fine-tuned on sciMETv3 cells, bulk-pretrained CpGPT beat DeepCpG on AUPRC but not AUROC ([[10-Summaries/delimacamillo-2024-cpgpt|CpGPT]]; [[10-Summaries/angermueller-2017-genomebiol|DeepCpG]]).
- **Weak baselines.** EpiFoundation's cell-type annotation has no baselines, and scDynOmics gives no numbers for its foundation-model comparison ([[10-Summaries/wu-2025-epifoundation|EpiFoundation]]; [[10-Summaries/yu-2026-scdynomics|scDynOmics]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/dna-language-model|DNA language model]] — Foundation models pretrained on DNA sequence rather than cell profiles.
> - `concept` [[30-Concepts/genomic-tokenization|Genomic tokenization]] — How DNA or a single-cell epigenome profile is turned into tokens.
> - `concept` [[30-Concepts/multimodal-integration-methods|Multimodal integration methods]] — Combining paired or unpaired single-cell modalities.
> - `concept` [[30-Concepts/scatac-imputation|scATAC imputation]] — Recovering missing signal in sparse scATAC matrices.
> - `concept` [[30-Concepts/cell-type-annotation|Cell-type annotation]] — Assigning identity to clusters, a common fine-tuning task.
> - `concept` [[30-Concepts/batch-effect|Batch effect]] — Technical variation that pretrained embeddings must handle.
> - `hub` [[40-Topics/sequence-models-and-foundation-models|Sequence models and foundation models]] — Supervised and self-supervised models of genomic data.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Chromatin accessibility in single cells.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — Methylation measurement and analysis.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromatin folding and contacts.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Several modalities from the same cells.

## All sources on this page

> [!info]- 22 summaries cited here
> - [[10-Summaries/angermueller-2017-genomebiol|Angermueller 2017]]
> - [[10-Summaries/cui-2024-natmethods|Cui 2024]]
> - [[10-Summaries/delimacamillo-2024-cpgpt|CpGPT 2024]]
> - [[10-Summaries/foroozandeh-2025-candi|Foroozandeh 2025 CANDI]]
> - [[10-Summaries/fu-2025-get|GET 2025]]
> - [[10-Summaries/kong-2026-mutationprojector|Kong 2026 (Cancer Discov)]]
> - [[10-Summaries/leroy-2025-atacformer|Atacformer 2025]]
> - [[10-Summaries/li-2026-clm-x|CLM-X 2026]]
> - [[10-Summaries/li-2026-epizoo|EpiZoo 2026]]
> - [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT 2025]]
> - [[10-Summaries/liu-2024-cot|Liu 2024 (Brief Bioinform)]]
> - [[10-Summaries/liu-2025-clm-access|CLM-access 2025]]
> - [[10-Summaries/liu-2025-scarf|SCARF 2025]]
> - [[10-Summaries/liu-2025-scmomer|scMomer 2025]]
> - [[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025 SCIBED]]
> - [[10-Summaries/sidhom-2026-tessera|Sidhom 2026 (bioRxiv)]]
> - [[10-Summaries/wang-2025-omnireg-gpt|OmniReg-GPT 2025]]
> - [[10-Summaries/wang-2026-hicfoundation|HiCFoundation 2026]]
> - [[10-Summaries/wu-2025-epifoundation|EpiFoundation 2025]]
> - [[10-Summaries/ying-2024-methylgpt|MethylGPT 2024]]
> - [[10-Summaries/yu-2026-chrombert|Yu 2026 ChromBERT]]
> - [[10-Summaries/yu-2026-scdynomics|scDynOmics 2026]]
