---
type: concept
title: Sequence-to-function model
aliases: [seq2func, sequence-to-activity model, supervised genomic deep learning, sequence-based deep learning model, genomic track prediction]
tags: [sequence-model, deep-learning, variant-effect, chromatin, gene-expression]
created: 2026-10-08
updated: 2026-10-09
---

# Sequence-to-function model

> A supervised model that predicts measured functional readouts — chromatin profiles, accessibility, expression or 3D contacts — directly from DNA sequence, and scores a variant by the difference between its reference and alternative predictions ([[10-Summaries/zhou-2015-deepsea]]; [[10-Summaries/avsec-2021-enformer]]).

## Definition

The template was set by DeepSEA in 2015: a multitask CNN reads 1 kb of reference sequence and predicts 919 TF, DNase and histone peak profiles ([[10-Summaries/zhou-2015-deepsea]]). Later models changed four things — input length, output resolution, output type and architecture — while keeping the training signal: consortium tracks such as ENCODE and Roadmap ([[10-Summaries/kelley-2018-basenji]]; [[10-Summaries/avsec-2026-alphagenome]]). Unlike a [[dna-language-model]], the model never learns from unlabelled sequence alone.

## Why it matters

- They connect sequence to every DNA layer in the review's frame: accessibility (Basset, ChromBPNet), histone marks and TF binding (DeepSEA, Sei), 3D contacts (Akita, Orca) and expression (ExPecto, Enformer, Borzoi) ([[10-Summaries/kelley-2016-basset]]; [[10-Summaries/pampari-2024-chrombpnet]]; [[10-Summaries/chen-2022-sei]]; [[10-Summaries/fudenberg-2020-akita]]; [[10-Summaries/zhou-2022-orca]]; [[10-Summaries/zhou-2018-expecto]]; [[10-Summaries/linder-2025-borzoi]]).
- They are the main route from a noncoding variant to a mechanistic hypothesis; see [[variant-effect-prediction]].
- For single-cell data they are starting to act as priors: SUCCEED denoises shallow ATAC ([[10-Summaries/sun-2026-succeed]]), and scooby, Decima and CREsted predict single-cell or cell-type profiles from sequence ([[10-Summaries/hingerl-2025-scooby]]; [[10-Summaries/lal-2026-decima]]; [[10-Summaries/kempynck-2026-crested]]).

## Variants and refinements

**Lineage** (synthesis of the summaries):
- *Peaks from short windows:* DeepSEA (1 kb, 919 profiles, 2015) → Basset (600 bp, DNase in 164 cell types, 2016) → Sei (4 kb, 21,907 profiles grouped into 40 sequence classes, 2022) ([[10-Summaries/zhou-2015-deepsea]]; [[10-Summaries/kelley-2016-basset]]; [[10-Summaries/chen-2022-sei]]).
- *Coverage from long windows:* Basenji (131 kb, 128-bp bins, 2018) → Enformer (196 kb, transformer, 2021) → Borzoi (524 kb, 32-bp RNA-seq coverage, 2025) → AlphaGenome (1 Mb in, up to 1-bp out, 11 modalities, 2026) ([[10-Summaries/kelley-2018-basenji]]; [[10-Summaries/avsec-2021-enformer]]; [[10-Summaries/linder-2025-borzoi]]; [[10-Summaries/avsec-2026-alphagenome]]).
- *Expression in stages:* ExPecto predicts chromatin first, then tissue expression with linear models ([[10-Summaries/zhou-2018-expecto]]).
- *3D contacts:* Akita (~1 Mb, 2 kb bins) and Orca (up to 256 Mb, multiscale) ([[10-Summaries/fudenberg-2020-akita]]; [[10-Summaries/zhou-2022-orca]]).
- *Base resolution with bias correction:* ChromBPNet separates Tn5/DNase-I bias from regulatory signal ([[10-Summaries/pampari-2024-chrombpnet]]).
- *Context-conditioned:* EpiGePT adds a TF-expression vector to reach unseen cell types; EPInformer feeds measured DNase/H3K27ac and Hi-C alongside sequence ([[10-Summaries/gao-2024-epigept]]; [[10-Summaries/lin-2026-epinformer]]).
- *Single-cell outputs:* scooby (Borzoi + per-cell decoder), Decima (Borzoi fine-tuned on 8,856 pseudobulks), CREsted (scATAC enhancer models) ([[10-Summaries/hingerl-2025-scooby]]; [[10-Summaries/lal-2026-decima]]; [[10-Summaries/kempynck-2026-crested]]).
- *Bridges to language models:* SUCCEED is a supervised "foundation model"; NTv3 post-trains a DNA LM on ~16k tracks ([[10-Summaries/sun-2026-succeed]]; [[10-Summaries/boshar-2025-ntv3]]).

**Models in this wiki** (28, by year):

- **DeepSEA** (2015) — DeepSEA set the template for sequence-to-function models: a multitask CNN reads 1 kb of reference sequence and predicts 919 TF, DNase and histone peak profiles, with median held-out AUC 0.958 for TF binding vs 0.896 for gkm-SVM ([[10-Summaries/zhou-2015-deepsea]])
- **Basset** (2016) — Basset trained a CNN on 2.07 M merged DHSs to predict accessibility in 164 cell types from 600 bp of sequence (mean AUC 0.895 vs 0.780 for gkm-SVM), and showed that a model pretrained on 149 cell types adapts to a new cell type in one training pass ([[10-Summaries/kelley-2016-basset]])
- **Basenji** (2018) — Basenji moved sequence-to-function models from binary peaks to quantitative coverage: from 131 kb input, dilated convolutions (~32 kb receptive field) predict 4,229 DNase, histone ChIP and CAGE tracks in 128 bp bins, with prediction–experiment correlation exceeding replicate correlation on average ([[10-Summaries/kelley-2018-basenji]])
- **ExPecto** (2018) — ExPecto predicts tissue-specific expression in three stages: a CNN predicts 2,002 chromatin profiles across ±20 kb of the TSS, fixed exponential spatial bases compress them, and per-tissue L2 linear models give median Spearman 0.819 on held-out chromosome 8 across 218 tissues ([[10-Summaries/zhou-2018-expecto]])
- **Akita** (2020) — Akita extended sequence-to-function modelling to 2D contact maps: a Basenji trunk plus a symmetric 2D dilated-residual head predicts five Hi-C/Micro-C maps at 2,048 bp from ~1 Mb, reaching test Pearson 0.61 with 746,149 parameters ([[10-Summaries/fudenberg-2020-akita]])
- **Enformer** (2021) — Enformer swapped Basenji2's dilated convolutions for 11 transformer blocks so each 128-bp bin can draw on sequence up to ~100 kb away, raising mean CAGE-at-TSS correlation across held-out genes from 0.81 to 0.85 ([[10-Summaries/avsec-2021-enformer]])
- **Orca** (2022) — Orca's hierarchical encoder and cascading 'zooming' decoders predict Micro-C contact maps at nine scales from 1 Mb at 4 kb up to 256 Mb, with held-out Pearson 0.78–0.85 (H1-ESC) and 0.73–0.79 (HFF) ([[10-Summaries/zhou-2022-orca]])
- **Sei** (2022) — Sei predicts 21,907 Cistrome/ENCODE/Roadmap chromatin profiles from 4 kb (average AUROC 0.972, AUPRC 0.409) and clusters genome-wide predictions into 40 sequence classes (promoter, 12 enhancer, CTCF, Polycomb, heterochromatin and others) covering >97.4% of the genome ([[10-Summaries/chen-2022-sei]])
- **HyenaDNA** (2023) — On DeepSEA's 919 chromatin profiles a 7M-parameter HyenaDNA reached median AUROC 96.4/93.0/86.3 (TF/DHS/HM) vs DeepSEA 95.8/92.3/85.6 ([[10-Summaries/nguyen-2023-hyenadna]])
- **ChromBPNet** (2024) — ChromBPNet pairs a frozen small CNN trained on non-peak background (enzyme bias) with a 512-filter dilated BPNet trained on the residual, predicting 1-kb base-resolution ATAC/DNase profiles from 2,114 bp; dropping the bias head yields bias-corrected profiles and footprints ([[10-Summaries/pampari-2024-chrombpnet]])
- **EpiGePT** (2024) — EpiGePT conditions a 128-kb CNN-transformer on a 711-dimensional TF vector (motif score × TF expression), which lets it predict DNase, CTCF and six histone marks in cell types it was not trained on (cross-cell-type DNase PCC 0.787; mean PCC 0.510 vs 0.440 for pretrained Enformer on 19 held-out contexts) ([[10-Summaries/gao-2024-epigept]]).
- **BioFM** (2025) — A linearly probed or LoRA-tuned BioFM beat Enformer on expression (median AUROC 0.812 vs 0.782 at 98 kb) and Borzoi eQTLs (0.697 vs 0.674), and SpliceTransformer on sQTLs (0.676 vs 0.629) ([[10-Summaries/medvedev-2025-biofm]]).
- **Borzoi** (2025) — Borzoi extends Enformer with U-net upsampling to predict stranded RNA-seq coverage at 32 bp over 524 kb (test bin-level Pearson 0.75 ensembled; gene-level 0.87), alongside CAGE, DNase, ATAC and ChIP tracks ([[10-Summaries/linder-2025-borzoi]])
- **Evo2HiC** (2025) — Combining the distilled sequence embedding with a bulk Hi-C embedding improved Pearson correlation for DNase, CTCF, H3K27ac, H3K27me3 and H3K4me3 by 34.7% over Hi-C-only and 26.2% over Evo 2-only inputs on held-out chromosomes ([[10-Summaries/fang-2025-evo2hic]])
- **GET** (2025) — GET does not read raw sequence: each peak enters as summed scores for 282 motif clusters, and in zero-shot K562 lentiMPRA prediction it reached Pearson 0.55 vs Enformer's 0.44 ([[10-Summaries/fu-2025-get]]).
- **NTv3** (2025) — NTv3 shows one backbone can serve both roles: after post-training on 15,889 functional tracks it matches Borzoi on DNase and ChIP at base resolution and beats it on ATAC, CAGE and RNA-seq, while staying stable down to 8 kb inputs where Borzoi degrades ([[10-Summaries/boshar-2025-ntv3]]).
- **Nucleotide Transformer** (2025) — Fine-tuned NT Multispecies 2.5B came within ~1% AUC of DeepSEA on 919 chromatin profiles and matched SpliceAI-10k on splice-site prediction with 6 kb input, while Enformer's trunk was best on enhancer tasks in NT's benchmark ([[10-Summaries/dallatorre-2025-nucleotide-transformer]])
- **OmniReg-GPT** (2025) — With the backbone frozen and a single head, OmniReg-GPT embeddings predicted cell-type-agnostic expression (R² 0.55 human, 0.65 mouse on Xpresso), per-cell single-cell expression (mean AUROC 0.83 on a 134,557-cell human atlas) and 2-Mb Hi-C maps (insulation-score Pearson 0.80 on the test chromosome) ([[10-Summaries/wang-2025-omnireg-gpt]]).
- **scooby** (2025) — scooby adapts the bulk Borzoi model to single cells: it adds rank-8 LoRA adapters and replaces the output heads with an MLP that writes the decoder weights from each cell's 14-dimensional MultiVI embedding, so the number of parameters does not grow with the number of cells ([[10-Summaries/hingerl-2025-scooby]]).
- **AlphaGenome** (2026) — AlphaGenome uses a U-net (conv encoder, transformer tower with 2D pair embeddings, conv decoder) on 1 Mb of DNA to predict 5,930 human tracks across 11 modalities at up to 1-bp resolution, and is distilled into one student model that scores a variant in under 1 s ([[10-Summaries/avsec-2026-alphagenome]])
- **CREsted** (2026) — CREsted trains multi-class CNNs on pseudobulk scATAC peak heights (first on all peaks, then fine-tuned on cell-type-specific peaks); on mouse motor cortex it reached Pearson 0.82 on held-out chromosomes and beat gReLU models of 6M and 22M parameters ([[10-Summaries/kempynck-2026-crested]]).
- **Decima** (2026) — Decima fine-tunes all of Borzoi so that it predicts one gene's expression across 8,856 cell type × tissue × disease pseudobulks; the multinomial loss is applied across pseudobulks rather than positions, and it reaches mean Pearson 0.80 within pseudobulks and 0.58 within genes on held-out genes ([[10-Summaries/lal-2026-decima]]).
- **EPInformer** (2026) — EPInformer predicts a gene's expression from its promoter and up to 60 candidate enhancers plus their measured DNase/H3K27ac (or ATAC) and Hi-C, beating sequence-only Borzoi on held-out CAGE (K562 r = 0.841 vs 0.792) with 447,149 parameters — a comparison that gives EPInformer measured epigenomic input ([[10-Summaries/lin-2026-epinformer]])
- **EpiZoo** (2026) — Combining EpiZoo sequence embeddings with averaged cell-type embeddings predicted cell-type-specific accessibility on CREsted BICCN2 mouse cortex data with cell-type PCC 0.677 against 0.634 for DeepBICCN2 on cell-type-specific peaks ([[10-Summaries/li-2026-epizoo]]).
- **Genos** (2026) — Fine-tuned with a dilated convolutional head on 667 ENCODE and GTEx groups, Genos-1.2B predicted single-base RNA-seq tracks with log1p Pearson correlations up to 0.9335 genome-wide in GM12878 ([[10-Summaries/lin-2025-genos]]).
- **Mendel** (2026) — Mendel reuses Borzoi's QTL benchmark sets and frames sequence-to-variation residuals as complementary to sequence-to-function predictions from Enformer, Borzoi and AlphaGenome ([[10-Summaries/salman-2026-mendel]]).
- **SUCCEED** (2026) — SUCCEED is a lighter Enformer-style model (RoPE, RMSNorm, grouped-query attention, SwiGLU) pretrained on 6,389 ENCODE tracks; on Enformer's data it reached CAGE PCC 0.76 vs 0.703 but DNase/ATAC 0.813 vs 0.847 ([[10-Summaries/sun-2026-succeed]])
- **UKBioBERT** (2026) — UKBioFormer fuses frozen UKBioBERT gene embeddings with a pruned, fine-tuned Enformer and beats Performer on 63.3% of genes with PCC > 0.6 for individual-level expression prediction in GTEx ([[10-Summaries/liu-2026-ukbiobert]]).

## Contested points

- **Local versus long-range.** A ~6M-parameter local ChromBPNet matched or beat Enformer on caQTL/dsQTL depending on how Enformer was scored ([[10-Summaries/pampari-2024-chrombpnet]]), yet AlphaGenome later beat ChromBPNet on the same benchmarks ([[10-Summaries/avsec-2026-alphagenome]]).
- **Distal enhancers are still under-weighted.** Decima's learned enhancer effects decay with distance in a CRISPRi comparison, as in earlier models ([[10-Summaries/lal-2026-decima]]); EPInformer beats sequence-only Borzoi but only by also reading measured epigenomic data ([[10-Summaries/lin-2026-epinformer]]).
- **Splits.** Basset and Basenji used random rather than chromosome-held-out splits ([[10-Summaries/kelley-2016-basset]]; [[10-Summaries/kelley-2018-basenji]]), which may overstate held-out accuracy (synthesis).
- **Tissue-specific splicing** is mostly not captured by Borzoi ([[10-Summaries/linder-2025-borzoi]]).

## Added 2026-10-09 — foundation-model gap evidence

- AlphaGenome predicted multi-gene effects for somatic CH variants, such as raised MTCP1 and CMC4 for chrX_155066068_C_T and lowered UGT2B7 with raised UGT2B11 for a UGT2B7 intronic indel. None were tested experimentally ([[10-Summaries/weinstock-2025-ch-noncoding-drivers]])
- Fischbach used AlphaGenome as a stand-in for the molecular consequence of somatic mutation load in aging colon, scoring more than 200,000 simulated random SNVs and thousands of catalogued crypt mutations through the RNA_SEQ output only ([[10-Summaries/fischbach-2026-alphagenome-aging]])

## Related

- [[dna-language-model]] · [[variant-effect-prediction]] · [[convolutional-neural-network]] · [[transcription-factor-motif]] · [[cis-regulatory-element]] · [[topologically-associating-domain]]
- [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/3d-genome]] · [[40-Topics/single-cell-atac-seq]]
