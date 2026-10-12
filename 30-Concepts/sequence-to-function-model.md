---
type: concept
title: Sequence-to-function model
aliases: [seq2func, sequence-to-activity model, supervised genomic deep learning, sequence-based deep learning model, genomic track prediction]
tags: [sequence-model, deep-learning, variant-effect, chromatin, gene-expression]
created: 2026-10-08
updated: 2026-10-12
---

# Sequence-to-function model

> A supervised model that predicts measured functional readouts — chromatin profiles, accessibility, expression or 3D contacts — directly from DNA sequence, and scores a variant by the difference between its reference and alternative predictions ([[10-Summaries/zhou-2015-deepsea|DeepSEA]]; [[10-Summaries/avsec-2021-enformer|Enformer]]).

> [!abstract] 한눈에
> Sequence-to-function model은 DNA 서열만 보고 chromatin profile, accessibility, 발현, 3D contact 같은 실측 신호를 예측하도록 지도학습한 모델이며, reference와 alternative 서열의 예측 차이로 변이를 평가한다 ([[10-Summaries/zhou-2015-deepsea|DeepSEA]]; [[10-Summaries/avsec-2021-enformer|Enformer]]). 입력 길이와 출력 해상도는 1 kb peak에서 1 Mb·1-bp track으로 커졌지만, 먼 enhancer의 효과를 여전히 과소평가한다는 점이 남은 쟁점이다 ([[10-Summaries/avsec-2026-alphagenome|AlphaGenome]]; [[10-Summaries/lal-2026-decima|Decima]]).

## Definition

The template was set by DeepSEA in 2015: a multitask CNN reads 1 kb of reference sequence and predicts 919 TF, DNase and histone peak profiles ([[10-Summaries/zhou-2015-deepsea|DeepSEA]]). Later models changed four things — input length, output resolution, output type and architecture — while keeping the training signal: consortium tracks such as ENCODE and Roadmap ([[10-Summaries/kelley-2018-basenji|Basenji]]; [[10-Summaries/avsec-2026-alphagenome|AlphaGenome]]). Unlike a [[dna-language-model]], the model never learns from unlabelled sequence alone ([[10-Summaries/zhou-2015-deepsea|DeepSEA]]; [[10-Summaries/avsec-2021-enformer|Enformer]]).

## Why it matters

- They connect sequence to every DNA layer in the review's frame: accessibility (Basset, ChromBPNet), histone marks and TF binding (DeepSEA, Sei), 3D contacts (Akita, Orca) and expression (ExPecto, Enformer, Borzoi) ([[10-Summaries/kelley-2016-basset|Basset]]; [[10-Summaries/pampari-2024-chrombpnet|ChromBPNet]]; [[10-Summaries/chen-2022-sei|Sei]]; [[10-Summaries/fudenberg-2020-akita|Akita]]; [[10-Summaries/zhou-2022-orca|Orca]]; [[10-Summaries/zhou-2018-expecto|ExPecto]]; [[10-Summaries/linder-2025-borzoi|Borzoi]]).
- They are the main route from a noncoding variant to a mechanistic hypothesis; see [[variant-effect-prediction]] (synthesis).
- For single-cell data they are starting to act as priors: SUCCEED denoises shallow ATAC ([[10-Summaries/sun-2026-succeed|SUCCEED]]), and scooby, Decima and CREsted predict single-cell or cell-type profiles from sequence ([[10-Summaries/hingerl-2025-scooby|scooby]]; [[10-Summaries/lal-2026-decima|Decima]]; [[10-Summaries/kempynck-2026-crested|CREsted]]).

## Lineage

The models fall into a few lines of descent (synthesis of the summaries):

- *Peaks from short windows:* DeepSEA → Basset → Sei ([[10-Summaries/zhou-2015-deepsea|DeepSEA]]; [[10-Summaries/kelley-2016-basset|Basset]]; [[10-Summaries/chen-2022-sei|Sei]]).
- *Coverage from long windows:* Basenji → Enformer → Borzoi → AlphaGenome ([[10-Summaries/kelley-2018-basenji|Basenji]]; [[10-Summaries/avsec-2021-enformer|Enformer]]; [[10-Summaries/linder-2025-borzoi|Borzoi]]; [[10-Summaries/avsec-2026-alphagenome|AlphaGenome]]).
- *Expression in stages:* ExPecto predicts chromatin first, then tissue expression with linear models ([[10-Summaries/zhou-2018-expecto|ExPecto]]).
- *3D contacts:* Akita and Orca ([[10-Summaries/fudenberg-2020-akita|Akita]]; [[10-Summaries/zhou-2022-orca|Orca]]).
- *Base resolution with bias correction:* ChromBPNet separates Tn5/DNase-I bias from regulatory signal ([[10-Summaries/pampari-2024-chrombpnet|ChromBPNet]]).
- *Context-conditioned:* EpiGePT adds a TF-expression vector to reach unseen cell types; EPInformer feeds measured DNase/H3K27ac and Hi-C alongside sequence ([[10-Summaries/gao-2024-epigept|EpiGePT]]; [[10-Summaries/lin-2026-epinformer|EPInformer]]).
- *Single-cell outputs:* scooby, Decima and CREsted ([[10-Summaries/hingerl-2025-scooby|scooby]]; [[10-Summaries/lal-2026-decima|Decima]]; [[10-Summaries/kempynck-2026-crested|CREsted]]).
- *Bridges to language models:* SUCCEED is a supervised "foundation model"; NTv3 post-trains a DNA LM on ~16k tracks ([[10-Summaries/sun-2026-succeed|SUCCEED]]; [[10-Summaries/boshar-2025-ntv3|NTv3]]).

## Models

### Bulk tracks from sequence alone

| Model | Year | Input | Output | Key result | Source |
|---|---|---|---|---|---|
| DeepSEA | 2015 | 1 kb | 919 TF, DNase and histone peak profiles | Multitask CNN; median held-out AUC 0.958 for TF binding vs 0.896 for gkm-SVM | ([[10-Summaries/zhou-2015-deepsea\|DeepSEA]]) |
| Basset | 2016 | 600 bp | Accessibility in 164 cell types, trained on 2.07 M merged DHSs | CNN; mean AUC 0.895 vs 0.780 for gkm-SVM; a model pretrained on 149 cell types adapts to a new cell type in one training pass | ([[10-Summaries/kelley-2016-basset\|Basset]]) |
| Basenji | 2018 | 131 kb | 4,229 DNase, histone ChIP and CAGE tracks in 128-bp bins | Moved the field from binary peaks to quantitative coverage; dilated convolutions (~32 kb receptive field); prediction–experiment correlation exceeded replicate correlation on average | ([[10-Summaries/kelley-2018-basenji\|Basenji]]) |
| Enformer | 2021 | 196 kb | 128-bp bins | Swapped Basenji2's dilated convolutions for 11 transformer blocks so each bin can draw on sequence up to ~100 kb away; mean CAGE-at-TSS correlation across held-out genes rose from 0.81 to 0.85 | ([[10-Summaries/avsec-2021-enformer\|Enformer]]) |
| Sei | 2022 | 4 kb | 21,907 Cistrome/ENCODE/Roadmap chromatin profiles | Average AUROC 0.972, AUPRC 0.409; genome-wide predictions cluster into 40 sequence classes (promoter, 12 enhancer, CTCF, Polycomb, heterochromatin and others) covering >97.4% of the genome | ([[10-Summaries/chen-2022-sei\|Sei]]) |
| Borzoi | 2025 | 524 kb | Stranded RNA-seq coverage at 32 bp, plus CAGE, DNase, ATAC and ChIP tracks | Extends Enformer with U-net upsampling; test bin-level Pearson 0.75 ensembled, gene-level 0.87 | ([[10-Summaries/linder-2025-borzoi\|Borzoi]]) |
| AlphaGenome | 2026 | 1 Mb | 5,930 human tracks across 11 modalities at up to 1-bp resolution | U-net (conv encoder, transformer tower with 2D pair embeddings, conv decoder); distilled into one student model that scores a variant in under 1 s | ([[10-Summaries/avsec-2026-alphagenome\|AlphaGenome]]) |
| SUCCEED | 2026 | — | Pretrained on 6,389 ENCODE tracks | Lighter Enformer-style model (RoPE, RMSNorm, grouped-query attention, SwiGLU); on Enformer's data CAGE PCC 0.76 vs 0.703, but DNase/ATAC 0.813 vs 0.847 | ([[10-Summaries/sun-2026-succeed\|SUCCEED]]) |

### Specialised outputs: expression stages, 3D contacts, base resolution

| Model | Year | Input | Output | Key result | Source |
|---|---|---|---|---|---|
| ExPecto | 2018 | ±20 kb of the TSS | 2,002 chromatin profiles, then expression in 218 tissues | A CNN predicts chromatin, fixed exponential spatial bases compress it, and per-tissue L2 linear models give median Spearman 0.819 on held-out chromosome 8 | ([[10-Summaries/zhou-2018-expecto\|ExPecto]]) |
| Akita | 2020 | ~1 Mb | Five Hi-C/Micro-C maps at 2,048 bp | Basenji trunk plus a symmetric 2D dilated-residual head; test Pearson 0.61 with 746,149 parameters | ([[10-Summaries/fudenberg-2020-akita\|Akita]]) |
| Orca | 2022 | 1 Mb up to 256 Mb | Micro-C contact maps at nine scales, from 4 kb at 1 Mb | Hierarchical encoder and cascading "zooming" decoders; held-out Pearson 0.78–0.85 (H1-ESC) and 0.73–0.79 (HFF) | ([[10-Summaries/zhou-2022-orca\|Orca]]) |
| ChromBPNet | 2024 | 2,114 bp | 1-kb base-resolution ATAC/DNase profiles | A frozen small CNN trained on non-peak background (enzyme bias) plus a 512-filter dilated BPNet trained on the residual; dropping the bias head yields bias-corrected profiles and footprints | ([[10-Summaries/pampari-2024-chrombpnet\|ChromBPNet]]) |

### Context-conditioned models

| Model | Year | Input | Output | Key result | Source |
|---|---|---|---|---|---|
| EpiGePT | 2024 | 128 kb plus a 711-dimensional TF vector (motif score × TF expression) | DNase, CTCF and six histone marks, including in cell types not seen in training | Cross-cell-type DNase PCC 0.787; mean PCC 0.510 vs 0.440 for pretrained Enformer on 19 held-out contexts | ([[10-Summaries/gao-2024-epigept\|EpiGePT]]) |
| GET | 2025 | Peaks as summed scores for 282 motif clusters, not raw sequence | Gene expression | Zero-shot K562 lentiMPRA Pearson 0.55 vs Enformer's 0.44 | ([[10-Summaries/fu-2025-get\|GET]]) |
| EPInformer | 2026 | Promoter and up to 60 candidate enhancers, plus their measured DNase/H3K27ac (or ATAC) and Hi-C | Gene expression | Beat sequence-only Borzoi on held-out CAGE (K562 r = 0.841 vs 0.792) with 447,149 parameters — a comparison that gives EPInformer measured epigenomic input | ([[10-Summaries/lin-2026-epinformer\|EPInformer]]) |

### Single-cell and cell-type outputs

| Model | Year | Built on | Output | Key result | Source |
|---|---|---|---|---|---|
| scooby | 2025 | Borzoi with rank-8 LoRA adapters | Per-cell profiles; an MLP writes the decoder weights from each cell's 14-dimensional MultiVI embedding | The number of parameters does not grow with the number of cells | ([[10-Summaries/hingerl-2025-scooby\|scooby]]) |
| CREsted | 2026 | Multi-class CNNs | Pseudobulk scATAC peak heights (trained on all peaks, then fine-tuned on cell-type-specific peaks) | Pearson 0.82 on held-out chromosomes in mouse motor cortex; beat gReLU models of 6M and 22M parameters | ([[10-Summaries/kempynck-2026-crested\|CREsted]]) |
| Decima | 2026 | All of Borzoi, fine-tuned | One gene's expression across 8,856 cell type × tissue × disease pseudobulks; multinomial loss across pseudobulks rather than positions | Mean Pearson 0.80 within pseudobulks and 0.58 within genes on held-out genes | ([[10-Summaries/lal-2026-decima\|Decima]]) |
| EpiZoo | 2026 | EpiZoo sequence embeddings combined with averaged cell-type embeddings | Cell-type-specific accessibility | On CREsted BICCN2 mouse cortex data, cell-type PCC 0.677 vs 0.634 for DeepBICCN2 on cell-type-specific peaks | ([[10-Summaries/li-2026-epizoo\|EpiZoo]]) |

### Language and foundation models benchmarked against sequence-to-function models

| Model | Year | Comparison | Source |
|---|---|---|---|
| HyenaDNA | 2023 | On DeepSEA's 919 chromatin profiles, a 7M-parameter HyenaDNA reached median AUROC 96.4/93.0/86.3 (TF/DHS/HM) vs DeepSEA 95.8/92.3/85.6 | ([[10-Summaries/nguyen-2023-hyenadna\|HyenaDNA]]) |
| Nucleotide Transformer | 2025 | Fine-tuned NT Multispecies 2.5B came within ~1% AUC of DeepSEA on 919 chromatin profiles and matched SpliceAI-10k on splice sites with 6 kb input, while Enformer's trunk was best on enhancer tasks in NT's benchmark | ([[10-Summaries/dallatorre-2025-nucleotide-transformer\|Nucleotide Transformer]]) |
| BioFM | 2025 | Linearly probed or LoRA-tuned, it beat Enformer on expression (median AUROC 0.812 vs 0.782 at 98 kb) and Borzoi on eQTLs (0.697 vs 0.674), and SpliceTransformer on sQTLs (0.676 vs 0.629) | ([[10-Summaries/medvedev-2025-biofm\|BioFM]]) |
| NTv3 | 2025 | After post-training on 15,889 functional tracks it matches Borzoi on DNase and ChIP at base resolution and beats it on ATAC, CAGE and RNA-seq, staying stable down to 8 kb inputs where Borzoi degrades — one backbone serving both roles | ([[10-Summaries/boshar-2025-ntv3\|NTv3]]) |
| OmniReg-GPT | 2025 | With the backbone frozen and a single head, embeddings predicted cell-type-agnostic expression (R² 0.55 human, 0.65 mouse on Xpresso), per-cell expression (mean AUROC 0.83 on a 134,557-cell human atlas) and 2-Mb Hi-C maps (insulation-score Pearson 0.80 on the test chromosome) | ([[10-Summaries/wang-2025-omnireg-gpt\|OmniReg-GPT]]) |
| Evo2HiC | 2025 | Combining the distilled sequence embedding with a bulk Hi-C embedding improved Pearson correlation for DNase, CTCF, H3K27ac, H3K27me3 and H3K4me3 by 34.7% over Hi-C-only and 26.2% over Evo 2-only inputs on held-out chromosomes | ([[10-Summaries/fang-2025-evo2hic\|Evo2HiC]]) |
| Genos | 2026 | Fine-tuned with a dilated convolutional head on 667 ENCODE and GTEx groups, Genos-1.2B predicted single-base RNA-seq tracks with log1p Pearson up to 0.9335 genome-wide in GM12878 | ([[10-Summaries/lin-2025-genos\|Genos]]) |
| UKBioBERT | 2026 | UKBioFormer fuses frozen UKBioBERT gene embeddings with a pruned, fine-tuned Enformer and beats Performer on 63.3% of genes with PCC > 0.6 for individual-level expression prediction in GTEx | ([[10-Summaries/liu-2026-ukbiobert\|UKBioBERT]]) |
| Mendel | 2026 | Reuses Borzoi's QTL benchmark sets and frames sequence-to-variation residuals as complementary to sequence-to-function predictions from Enformer, Borzoi and AlphaGenome | ([[10-Summaries/salman-2026-mendel\|Mendel]]) |

## Evidence and examples

- AlphaGenome predicted multi-gene effects for somatic clonal-haematopoiesis variants, such as raised MTCP1 and CMC4 for chrX_155066068_C_T and lowered UGT2B7 with raised UGT2B11 for a UGT2B7 intronic indel; none were tested experimentally ([[10-Summaries/weinstock-2025-ch-noncoding-drivers|Weinstock 2025]]).
- Fischbach used AlphaGenome as a stand-in for the molecular consequence of somatic mutation load in ageing colon, scoring more than 200,000 simulated random SNVs and thousands of catalogued crypt mutations through the RNA_SEQ output only ([[10-Summaries/fischbach-2026-alphagenome-aging|Fischbach 2026]]).

## Contested points

- **Local versus long-range.** A ~6M-parameter local ChromBPNet matched or beat Enformer on caQTL/dsQTL depending on how Enformer was scored ([[10-Summaries/pampari-2024-chrombpnet|ChromBPNet]]), yet AlphaGenome later beat ChromBPNet on the same benchmarks ([[10-Summaries/avsec-2026-alphagenome|AlphaGenome]]).
- **Distal enhancers are still under-weighted.** Decima's learned enhancer effects decay with distance in a CRISPRi comparison, as in earlier models ([[10-Summaries/lal-2026-decima|Decima]]); EPInformer beats sequence-only Borzoi but only by also reading measured epigenomic data ([[10-Summaries/lin-2026-epinformer|EPInformer]]).
- **Splits.** Basset and Basenji used random rather than chromosome-held-out splits ([[10-Summaries/kelley-2016-basset|Basset]]; [[10-Summaries/kelley-2018-basenji|Basenji]]), which may overstate held-out accuracy (synthesis).
- **Tissue-specific splicing** is mostly not captured by Borzoi ([[10-Summaries/linder-2025-borzoi|Borzoi]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/dna-language-model|DNA language model]] — Pretrained on unlabelled sequence alone, then probed, fine-tuned or scored zero-shot.
> - `concept` [[30-Concepts/variant-effect-prediction|Variant effect prediction]] — Scoring a variant by comparing model outputs for reference and alternative alleles.
> - `concept` [[30-Concepts/convolutional-neural-network|Convolutional neural network]] — The sliding-filter architecture behind DeepSEA, Basset and Basenji.
> - `concept` [[30-Concepts/transcription-factor-motif|Transcription factor motif]] — The sequence patterns these models learn and GET takes as input.
> - `concept` [[30-Concepts/cis-regulatory-element|Cis-regulatory element]] — Promoters and enhancers whose activity the models predict.
> - `concept` [[30-Concepts/topologically-associating-domain|Topologically associating domain]] — 3D structure targeted by Akita and Orca.
> - `hub` [[40-Topics/sequence-models-and-foundation-models|Sequence models and foundation models]] — Supervised and self-supervised models of genomic sequence.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromatin folding, contacts and their measurement.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Chromatin accessibility in single cells.

## All sources on this page

> [!info]- 30 summaries cited here
> - [[10-Summaries/avsec-2021-enformer|Enformer 2021]]
> - [[10-Summaries/avsec-2026-alphagenome|AlphaGenome 2026]]
> - [[10-Summaries/boshar-2025-ntv3|NTv3 2025]]
> - [[10-Summaries/chen-2022-sei|Sei 2022]]
> - [[10-Summaries/dallatorre-2025-nucleotide-transformer|Nucleotide Transformer 2025]]
> - [[10-Summaries/fang-2025-evo2hic|Evo2HiC 2025]]
> - [[10-Summaries/fischbach-2026-alphagenome-aging|Fischbach 2026]]
> - [[10-Summaries/fu-2025-get|GET 2025]]
> - [[10-Summaries/fudenberg-2020-akita|Akita 2020]]
> - [[10-Summaries/gao-2024-epigept|EpiGePT 2024]]
> - [[10-Summaries/hingerl-2025-scooby|scooby 2025]]
> - [[10-Summaries/kelley-2016-basset|Basset 2016]]
> - [[10-Summaries/kelley-2018-basenji|Basenji 2018]]
> - [[10-Summaries/kempynck-2026-crested|CREsted 2026]]
> - [[10-Summaries/lal-2026-decima|Decima 2026]]
> - [[10-Summaries/li-2026-epizoo|EpiZoo 2026]]
> - [[10-Summaries/lin-2025-genos|Genos 2026]]
> - [[10-Summaries/lin-2026-epinformer|EPInformer 2026]]
> - [[10-Summaries/linder-2025-borzoi|Borzoi 2025]]
> - [[10-Summaries/liu-2026-ukbiobert|UKBioBERT 2026]]
> - [[10-Summaries/medvedev-2025-biofm|BioFM 2025]]
> - [[10-Summaries/nguyen-2023-hyenadna|HyenaDNA 2023]]
> - [[10-Summaries/pampari-2024-chrombpnet|ChromBPNet 2024]]
> - [[10-Summaries/salman-2026-mendel|Mendel 2026]]
> - [[10-Summaries/sun-2026-succeed|SUCCEED 2026]]
> - [[10-Summaries/wang-2025-omnireg-gpt|OmniReg-GPT 2025]]
> - [[10-Summaries/weinstock-2025-ch-noncoding-drivers|Weinstock 2025]]
> - [[10-Summaries/zhou-2015-deepsea|DeepSEA 2015]]
> - [[10-Summaries/zhou-2018-expecto|ExPecto 2018]]
> - [[10-Summaries/zhou-2022-orca|Orca 2022]]
