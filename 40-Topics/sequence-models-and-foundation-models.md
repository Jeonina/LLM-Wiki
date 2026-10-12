---
type: topic
title: Sequence models and foundation models
explainer: sequence-models-and-foundation-models
aliases: [genomic foundation models, sequence-based prediction, scFM, foundation models, sequence models]
tags: [foundation-model, dna-language-model, sequence-to-function, single-cell-foundation-model, deep-learning]
created: 2026-10-08
updated: 2026-10-12
paper_section: ["4.4"]
description: "Hub for §4.4: supervised sequence-to-function models, DNA language models, single-cell epigenome and multimodal foundation models, plus evidence for the genotype, histone and somatic-variant gaps."
---

# Sequence models and foundation models

> Models that learn from DNA sequence or from large single-cell epigenome corpora and transfer to new tasks: supervised [[sequence-to-function-model]]s ([[10-Summaries/zhou-2015-deepsea|DeepSEA]]; [[10-Summaries/avsec-2026-alphagenome|AlphaGenome]]), self-supervised [[dna-language-model]]s ([[10-Summaries/ji-2021-dnabert|DNABERT]]; [[10-Summaries/brixi-2026-evo2|Evo 2]]), and [[single-cell-foundation-model]]s for accessibility, methylation, 3D contacts and RNA+ATAC ([[10-Summaries/leroy-2025-atacformer|Atacformer]]; [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]; [[10-Summaries/wang-2026-hicfoundation|HiCFoundation]]; [[10-Summaries/liu-2025-scarf|SCARF]]). This hub gathers the 64 papers from the review's foundation-model list (§4.4 and the future-perspective paragraph) and the papers that test where single-cell DNA still lacks a foundation model.

> [!abstract] 한눈에
> DNA 서열이나 대규모 epigenome 데이터로 사전학습한 모델은 accessibility, methylation, 3D 구조 층에는 이미 있지만, single-cell genotype(CNV/SNV)과 single-cell histone 데이터로 사전학습한 모델은 아직 없다 ([[10-Summaries/sidhom-2026-tessera|TESSERA]]; [[10-Summaries/yu-2026-chrombert|ChromBERT]]). 변이 점수화도 germline 벤치마크 중심이어서, somatic 변이에 대한 예측은 대부분 검증 없이 쓰이고 있다 ([[10-Summaries/fischbach-2026-alphagenome-aging|Fischbach 2026]]; [[10-Summaries/terekhanova-2026-tal1-enhancer|Terekhanova 2026]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [서열 모델과 foundation model 교재](../60-Explainers/sequence-models-and-foundation-models.html)
<!-- /explainer-links -->

## Key points

- **Every DNA layer except genotype has a pretrained model, and histone only in bulk.** Accessibility, methylation and 3D contacts each have one ([[10-Summaries/leroy-2025-atacformer|Atacformer]]; [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]; [[10-Summaries/wang-2026-hicfoundation|HiCFoundation]]); ChromBERT pretrains on bulk Cistrome profiles that include 76 histone marks, but no model is pretrained on single-cell histone data or single-cell genotypes ([[10-Summaries/yu-2026-chrombert|ChromBERT]]; [[10-Summaries/liu-2024-cot|CoT]]; [[10-Summaries/sidhom-2026-tessera|TESSERA]]).
- **Sequence priors are entering single-cell epigenomics.** GFETM, EpiZoo, CpGPT and Evo2HiC all reuse DNA-LM embeddings ([[10-Summaries/fan-2026-gfetm|GFETM]]; [[10-Summaries/li-2026-epizoo|EpiZoo]]; [[10-Summaries/delimacamillo-2024-cpgpt|CpGPT]]; [[10-Summaries/fang-2025-evo2hic|Evo2HiC]]).
- **Supervised sequence-to-function models now reach 1 Mb input at base resolution.** AlphaGenome takes 1 Mb, outputs 11 modalities at 1 bp and matches or beats specialists on 25/26 variant-effect benchmarks ([[10-Summaries/avsec-2026-alphagenome|AlphaGenome]]); NTv3 also reads 1 Mb with single-base tokens ([[10-Summaries/boshar-2025-ntv3|NTv3]]).
- **Self-supervised pretraining is not always worth its cost.** TF-IDF frequency baselines explain much of the NT/GUE benchmarks ([[10-Summaries/sanabria-2024-grover|GROVER]]), and swapping a DNA LM for HyenaDNA or DeepSEA features moves somatic-driver AUROC by less than 1 point ([[10-Summaries/zeng-2025-somatic-driver-lm|GenomeBert]]).
- **Somatic variants are scored more often than they are benchmarked.** AlphaGenome and Akita are applied to somatic SNVs, indels and SVs without ground truth ([[10-Summaries/fischbach-2026-alphagenome-aging|Fischbach 2026]]; [[10-Summaries/gjoni-2026-pediatric-tumor-3d|Gjoni 2026]]), and in one held-out test AlphaGenome under-predicted a somatic T-ALL enhancer ([[10-Summaries/terekhanova-2026-tal1-enhancer|Terekhanova 2026]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/sequence-to-function-model|Sequence-to-function model]] — Supervised prediction of functional tracks from sequence (DeepSEA → AlphaGenome).
> - `concept` [[30-Concepts/dna-language-model|DNA language model]] — Self-supervised models of DNA sequence (DNABERT → Evo 2).
> - `concept` [[30-Concepts/single-cell-foundation-model|Single-cell foundation model]] — Pretrained models of single-cell accessibility, methylation, Hi-C and RNA+ATAC.
> - `concept` [[30-Concepts/genomic-tokenization|Genomic tokenization]] — k-mers, BPE, single nucleotides, learned chunks, variant and region tokens.
> - `concept` [[30-Concepts/variant-effect-prediction|Variant effect prediction]] — Scoring variants from model outputs, likelihoods or embeddings.
> - `note` [[50-Notes/computational-framework-structure|Computational framework structure]] — Draft scaffold for the review's computational section.

## Supervised sequence-to-function models

These models predict measured chromatin, expression or contact tracks from DNA sequence; see [[sequence-to-function-model]].

| Model | Year | Input | Training | Note |
|---|---|---|---|---|
| [[10-Summaries/zhou-2015-deepsea\|DeepSEA]] | 2015 | 1 kb sequence | Multitask CNN, 919 chromatin profiles | TF median AUC 0.958; >95% accuracy on confident allelic-imbalance SNPs ([[10-Summaries/zhou-2015-deepsea\|DeepSEA]]) |
| [[10-Summaries/kelley-2016-basset\|Basset]] | 2016 | 600 bp | CNN, DNase hypersensitivity in 164 cell types | Mean AUC 0.895 vs 0.780 gkm-SVM; SAD scores enrich PICS-causal GWAS SNPs ([[10-Summaries/kelley-2016-basset\|Basset]]) |
| [[10-Summaries/kelley-2018-basenji\|Basenji]] | 2018 | 131 kb | Dilated CNN, 4,229 coverage tracks (DNase, ChIP, CAGE) in 128 bp bins | Gene CAGE r 0.85; SED scores enrich GTEx eQTLs 3.2–5.8× ([[10-Summaries/kelley-2018-basenji\|Basenji]]) |
| [[10-Summaries/zhou-2018-expecto\|ExPecto]] | 2018 | 40 kb | DeepSEA-style CNN + spatial basis + per-tissue linear models | Expression in 218 tissues (Spearman 0.819); scores 140 M promoter mutations ([[10-Summaries/zhou-2018-expecto\|ExPecto]]) |
| [[10-Summaries/fudenberg-2020-akita\|Akita]] | 2020 | ~1 Mb | CNN, Hi-C/Micro-C maps at 2 kb | Test Pearson 0.61; orientation-specific CTCF grammar and buffered mouse B2 SINEs ([[10-Summaries/fudenberg-2020-akita\|Akita]]) |
| [[10-Summaries/avsec-2021-enformer\|Enformer]] | 2021 | 196 kb | Conv + transformer, 5,313 tracks at 128 bp | CAGE gene r 0.81 → 0.85 vs Basenji2; better eQTL/MPRA scoring ([[10-Summaries/avsec-2021-enformer\|Enformer]]) |
| [[10-Summaries/zhou-2022-orca\|Orca]] | 2022 | 4 kb within 1 Mb up to 256 Mb, incl. trans | Multiscale CNN, Micro-C | Pearson 0.73–0.85; predicts SV effects; TSS sequences drive A compartments ([[10-Summaries/zhou-2022-orca\|Orca]]) |
| [[10-Summaries/chen-2022-sei\|Sei]] | 2022 | 4 kb | CNN, 21,907 chromatin profiles | AUROC 0.972; 40 sequence classes for directional variant scoring, heritability and HGMD mechanisms ([[10-Summaries/chen-2022-sei\|Sei]]) |
| [[10-Summaries/pampari-2024-chrombpnet\|ChromBPNet]] | 2024 | Sequence, base-resolution ATAC/DNase | ~6M-param bias-factorized BPNet CNN | Removes Tn5/DNase-I bias, gives TF footprints; competitive with Enformer on caQTLs ([[10-Summaries/pampari-2024-chrombpnet\|ChromBPNet]]) |
| [[10-Summaries/gao-2024-epigept\|EpiGePT]] | 2024 | Sequence + TF expression × motif | Context-conditioned transformer, 8 epigenomic tracks | Unseen cell types; DNase PCC 0.787 cross-cell-type; HiChIP-guided attention ([[10-Summaries/gao-2024-epigept\|EpiGePT]]) |
| [[10-Summaries/linder-2025-borzoi\|Borzoi]] | 2025 | 524 kb | Enformer-derived U-net, RNA-seq coverage at 32 bp | One model scores expression, splicing and polyA variants; eQTL AUROC 0.794 vs 0.747 ([[10-Summaries/linder-2025-borzoi\|Borzoi]]) |
| [[10-Summaries/fang-2025-evo2hic\|Evo2HiC]] | 2025 | Sequence + bulk Hi-C guidance | Evo 2 (7B) distilled into a 3.6M CNN | +10.9% Spearman over Orca; Hi-C enhancement beats HiCARN2 in 157/177 species ([[10-Summaries/fang-2025-evo2hic\|Evo2HiC]]) |
| [[10-Summaries/boshar-2025-ntv3\|NTv3]] | 2025 | 1 Mb, single-base tokens | U-Net Nucleotide Transformer successor, post-trained on ~16k tracks / 24 species | Beats Borzoi, SegmentNT, SpliceAI ([[10-Summaries/boshar-2025-ntv3\|NTv3]]) |
| [[10-Summaries/avsec-2026-alphagenome\|AlphaGenome]] | 2026 | 1 Mb | 1-bp output, 11 modalities incl. splice junctions and contact maps | Matches or beats specialists on 25/26 variant-effect benchmarks ([[10-Summaries/avsec-2026-alphagenome\|AlphaGenome]]) |
| [[10-Summaries/lin-2026-epinformer\|EPInformer]] | 2026 | Sequence + DNase/H3K27ac/Hi-C | 0.4M-param promoter–enhancer transformer | Beats Enformer/Borzoi on CAGE and ABC on CRISPRi enhancer–gene links ([[10-Summaries/lin-2026-epinformer\|EPInformer]]) |
| [[10-Summaries/sun-2026-succeed\|SUCCEED]] | 2026 | Sequence | Lightweight CNN + transformer, supervised pretraining on 6,389 ENCODE tracks | Reused as encoder for epigenome, ATAC denoising and Hi-C prediction ([[10-Summaries/sun-2026-succeed\|SUCCEED]]) |

## Sequence-to-single-cell models

Sequence-to-function models whose outputs are single cells or cell-type pseudobulks.

| Model | Year | Input | Training | Note |
|---|---|---|---|---|
| [[10-Summaries/hingerl-2025-scooby\|scooby]] | 2025 | Sequence + cell embedding | Borzoi + LoRA + cell-embedding decoder; single-cell RNA/ATAC profiles | Beats seq2cells (0.77 → 0.87); maps eQTLs to cell types ([[10-Summaries/hingerl-2025-scooby\|scooby]]) |
| [[10-Summaries/kempynck-2026-crested\|CREsted]] | 2026 | Sequence; scATAC | Aerts-lab package for sequence-to-accessibility enhancer models and design | Small CNN matches fine-tuned Borzoi; zebrafish enhancers validated in vivo ([[10-Summaries/kempynck-2026-crested\|CREsted]]) |
| [[10-Summaries/lal-2026-decima\|Decima]] | 2026 | Sequence; 8,856 sc/snRNA pseudobulks (22M cells) | Borzoi fine-tuned | Cell-type/disease expression; beats Borzoi on sc-eQTLs in 19/21 cell types ([[10-Summaries/lal-2026-decima\|Decima]]) |

## DNA language models

Pretrained on sequence alone; see [[dna-language-model]] and [[genomic-tokenization]]. Tokenization ranges from overlapping k-mers and BPE to single nucleotides, learned chunks and variant tokens.

| Model | Year | Input | Training | Note |
|---|---|---|---|---|
| [[10-Summaries/ji-2021-dnabert\|DNABERT]] | 2021 | Human genome, overlapping k-mers | BERT-base masked LM | Fine-tunes to promoter/TFBS/splice SOTA (ENCODE 690 TF mean acc/F1 >0.9) ([[10-Summaries/ji-2021-dnabert\|DNABERT]]) |
| [[10-Summaries/zhou-2023-dnabert-2\|DNABERT-2]] | 2023 | Multi-species, BPE tokens | 117M BERT with ALiBi | Matches NT-2500M-multi on the new GUE benchmark (66.80 vs 66.93) at 21× fewer params ([[10-Summaries/zhou-2023-dnabert-2\|DNABERT-2]]) |
| [[10-Summaries/nguyen-2023-hyenadna\|HyenaDNA]] | 2023 | Single-nt tokens, up to 1M context | Attention-free Hyena long-convolution causal LM | SOTA on 12/18 NT and 7/8 GenomicBenchmarks with ≤7M params ([[10-Summaries/nguyen-2023-hyenadna\|HyenaDNA]]) |
| [[10-Summaries/chen-2023-genomicbert\|genomicBERT]] | 2023 | 4k SentencePiece-Unigram vocabulary | 89M MosaicBERT, 10k pretraining steps | Near-parity with DNABERT-2 on 5 tasks at far lower compute ([[10-Summaries/chen-2023-genomicbert\|genomicBERT]]) |
| [[10-Summaries/ellington-2024-aido-dna\|AIDO.DNA]] | 2024 | Single-nt tokens, 4 kb, NT's 796-genome data | 7B encoder-only | GUE avg 73.3 vs 67.7 (DNABERT-2) ([[10-Summaries/ellington-2024-aido-dna\|AIDO.DNA]]) |
| [[10-Summaries/schiff-2024-caduceus\|Caduceus]] | 2024 | 131k context | Bidirectional, reverse-complement-equivariant Mamba (~2M params) | Beats NT-v2 and Enformer on distal (>100 kb) eQTL VEP ([[10-Summaries/schiff-2024-caduceus\|Caduceus]]) |
| [[10-Summaries/sanabria-2024-grover\|GROVER]] | 2024 | Human only, BPE vocabulary (600 cycles) chosen by next-k-mer prediction | BERT | Shows TF-IDF frequency baselines explain much of NT/GUE ([[10-Summaries/sanabria-2024-grover\|GROVER]]) |
| [[10-Summaries/su-2025-atgc-gen\|ATGC-Gen]] | 2025 | Regulatory sequence + cross-modal conditioning | Plain GPT/BERT transformers | Beats diffusion and flow-matching baselines on promoter, enhancer and a new ChIP-seq benchmark ([[10-Summaries/su-2025-atgc-gen\|ATGC-Gen]]) |
| [[10-Summaries/li-2025-bmfm-dna\|BMFM-DNA]] | 2025 | dbSNP-variant-encoded genome (121 symbols) | ModernBERT (IBM) | Beats its reference twin on 5/6 tasks; roughly matches DNABERT-2 ([[10-Summaries/li-2025-bmfm-dna\|BMFM-DNA]]) |
| [[10-Summaries/medvedev-2025-biofm\|BioFM]] | 2025 | 1000G personal genomes + variant and GENCODE annotation tokens (BioToken) | 265M decoder | Beats Enformer/SpliceTransformer on eQTL/sQTL by linear probe ([[10-Summaries/medvedev-2025-biofm\|BioFM]]) |
| [[10-Summaries/zhang-2025-deepgene\|DeepGene]] | 2025 | HPRC 47-individual Minigraph pangenome graph | 85M/118M BERT with RoPE | 118M tops the GUE average (67.79 vs NT-2500M-multi 66.93) on yeast/mouse wins but trails on human promoter/splice tasks; edges DNABERT-2 on 2–5 kb promoter detection ([[10-Summaries/zhang-2025-deepgene\|DeepGene]]) |
| [[10-Summaries/fishman-2025-gena-lm\|GENA-LM]] | 2025 | BPE tokens (median 9 bp), 4.5–36 kb context | BERT/BigBird family with recurrent memory | Top average on the 18-task NT benchmark at 330M params ([[10-Summaries/fishman-2025-gena-lm\|GENA-LM]]) |
| [[10-Summaries/benegas-2025-gpn-msa\|GPN-MSA]] | 2025 | 100-vertebrate alignment | 86M masked DNA LM | Beats NT-2.5B, HyenaDNA, CADD, phyloP on most VEP benchmarks; ~9B human SNVs scored ([[10-Summaries/benegas-2025-gpn-msa\|GPN-MSA]]) |
| [[10-Summaries/vishniakov-2025-gene42\|Gene42]] | 2025 | Single-nt, dense attention to 192 kb | Decoder-only LLaMA-style, RoPE-based continued pretraining | Best biotype F1 0.782 ([[10-Summaries/vishniakov-2025-gene42\|Gene42]]) |
| [[10-Summaries/ma-2025-hybridna\|HybriDNA]] | 2025 | Single-nt, 131 kb | Decoder-only Transformer–Mamba2 hybrid (7:1 blocks), 300M/3B/7B | Leads most GUE tasks; designs enhancers beating HyenaDNA ([[10-Summaries/ma-2025-hybridna\|HybriDNA]]) |
| [[10-Summaries/duan-2025-janusdna\|JanusDNA]] | 2025 | — | Bidirectional hybrid Mamba/MoE, 'Janus' full-token two-sided objective | ~2M activated params lead 12/18 NT tasks and 8/9 DNALongBench eQTL tissues ([[10-Summaries/duan-2025-janusdna\|JanusDNA]]) |
| [[10-Summaries/long-2025-mutbert\|MutBERT]] | 2025 | 1000 Genomes allele-frequency 'probabilistic genome' | 86M encoder | 3rd on 23 tasks behind much larger NT models; eQTL AUROC 0.615 ([[10-Summaries/long-2025-mutbert\|MutBERT]]) |
| [[10-Summaries/ding-2025-nucel\|NucEL]] | 2025 | Single nucleotides, human only | 93M ModernBERT, ELECTRA replaced-token detection | Best GUE (75.16), GB and revised-NT averages ([[10-Summaries/ding-2025-nucel\|NucEL]]) |
| [[10-Summaries/dallatorre-2025-nucleotide-transformer\|Nucleotide Transformer]] | 2025 | 6-mer; 1000G / 850 species | 50M–2.5B BERT | Fine-tuned NT matches/beats BPNet on 18/18 tasks; NT-v2 250M best (MCC 0.769) ([[10-Summaries/dallatorre-2025-nucleotide-transformer\|Nucleotide Transformer]]) |
| [[10-Summaries/ayanian-2025-strand\|STRAND]] | 2025 | Raw aligned exome reads + reference | ~1B decoder (Mayo/Cerebras) | Claims SOTA on NT and new ClinVar/RA/IBD tasks ([[10-Summaries/ayanian-2025-strand\|STRAND]]) |
| [[10-Summaries/dealmeida-2025-segmentnt\|SegmentNT]] | 2025 | 30 kb | Nucleotide Transformer fine-tuned with a 1D U-Net head; 14 element classes at base resolution | Avg MCC 0.45 at 30 kb; at 3 kb, 0.37 vs 0.16 with a randomly initialised encoder ([[10-Summaries/dealmeida-2025-segmentnt\|SegmentNT]]) |
| [[10-Summaries/kim-2026-dnachunker\|DNAChunker]] | 2026 | Human only; learned two-stage dynamic chunking | 172M masked LM (BiMamba router + Transformer) | Best NT-benchmark average (MCC 0.772) ([[10-Summaries/kim-2026-dnachunker\|DNAChunker]]) |
| [[10-Summaries/leib-2026-dnt\|DNT]] | 2026 | Single-stream diploid tokens (zygosity, indels, optional phase) | On NTv3 + contrastive phase loss | Cis/trans compound-het AUROC 0.649 vs ~0.5 ([[10-Summaries/leib-2026-dnt\|DNT]]) |
| [[10-Summaries/brixi-2026-evo2\|Evo 2]] | 2026 | 1 Mb context, all domains of life | Autoregressive, 7B/40B | Zero-shot variant effects from likelihood change; genome-scale generation ([[10-Summaries/brixi-2026-evo2\|Evo 2]]) |
| [[10-Summaries/li-2026-generator\|GENERator]] | 2026 | 6-mer; 386 Gb of gene-centric eukaryotic DNA | 1.2B/3B LLaMA-style generative | Beats Evo2-1B on recovery/ClinVar at ~19× speed; designs validated enhancers ([[10-Summaries/li-2026-generator\|GENERator]]) |
| [[10-Summaries/chen-2026-genart\|GenART]] | 2026 | Trainable CNN + Gumbel-softmax tokenizer, tunable per task | 350M/1B hierarchical | Best NT and GUE averages; 0.629 recall of GENCODE boundaries ([[10-Summaries/chen-2026-genart\|GenART]]) |
| [[10-Summaries/lin-2025-genos\|Genos]] | 2026 | 636 human pangenome assemblies, 1-Mb context | BGI mixture-of-experts (1.25B/10.27B total, 0.33B/2.87B active) | Best mutation-hotspot and ClinVar AUCs ([[10-Summaries/lin-2025-genos\|Genos]]) |
| [[10-Summaries/salman-2026-mendel\|Mendel]] | 2026 | GTEx genotypes as IUPAC tokens | 1B StripedHyena2 | Residual errors flag fine-mapped cis-eQTLs (AUROC 0.731); improves TWAS in 50/50 tissues ([[10-Summaries/salman-2026-mendel\|Mendel]]) |
| [[10-Summaries/aspidova-2026-moderngena\|ModernGENA]] | 2026 | 32k BPE; vertebrate TSS windows | GENA-LM rebuilt on ModernBERT (135M/377M) | Top NT rank under 500M, faster inference; weak on splice sites ([[10-Summaries/aspidova-2026-moderngena\|ModernGENA]]) |
| [[10-Summaries/shen-2026-omnina\|OmniNA]] | 2026 | 91.7M NCBI nt sequences + their annotations | LLaMA-style DNA + text | Fine-tuned as QA on 23 tasks; F1 0.90 vs EVE 0.81 on 48 genes ([[10-Summaries/shen-2026-omnina\|OmniNA]]) |
| [[10-Summaries/liu-2026-ukbiobert\|UKBioBERT]] | 2026 | 13M UK Biobank variants | DNABERT-2 continued pretraining | Fused with Enformer (UKBioFormer), beats Performer on 63% of predictable genes ([[10-Summaries/liu-2026-ukbiobert\|UKBioBERT]]) |

## Epigenome foundation models

Pretrained on accessibility, methylation or Hi-C profiles; see [[single-cell-foundation-model]].

| Model | Year | Input | Training | Note |
|---|---|---|---|---|
| [[10-Summaries/delimacamillo-2024-cpgpt\|CpGPT]] | 2024 | 155k bulk Illumina-array methylomes; loci keyed by NTv2 sequence embeddings | Transformer | Zero-shot imputation/array conversion; CpGPTGrimAge3 top mortality HR in 3 held-out cohorts ([[10-Summaries/delimacamillo-2024-cpgpt\|CpGPT]]) |
| [[10-Summaries/ying-2024-methylgpt\|MethylGPT]] | 2024 | 154k bulk array methylomes; fixed 49,156-CpG vocabulary | scGPT-style transformer | Masked-value R 0.929; age MedAE 4.45 y; robust to 70% missing ([[10-Summaries/ying-2024-methylgpt\|MethylGPT]]) |
| [[10-Summaries/leroy-2025-atacformer\|Atacformer]] | 2025 | scATAC; cells as unordered sets of 890k region tokens, reads fragments directly | ELECTRA-pretrained transformer | CRAFT RNA–ATAC; icTSS promoter discovery ([[10-Summaries/leroy-2025-atacformer\|Atacformer]]) |
| [[10-Summaries/liu-2025-clm-access\|CLM-access]] | 2025 | scATAC, 2.8M cells; 2,000 patch tokens over 1.15M cCREs | BERT-style | Ablations show binarised peak-level BCE essential; beats scATAnno/Cellcano, BABEL ([[10-Summaries/liu-2025-clm-access\|CLM-access]]) |
| [[10-Summaries/wu-2025-epifoundation\|EpiFoundation]] | 2025 | scATAC non-zero peak tokens; 100k-cell 10x Multiome MiniAtlas | Transformer pretrained to predict paired binary RNA | Top integration metrics; 2× Gene Activity correlation ([[10-Summaries/wu-2025-epifoundation\|EpiFoundation]]) |
| [[10-Summaries/fu-2025-get\|GET]] | 2025 | Motif-scored accessible peaks; scATAC pseudobulks of 213 cell types | Transformer | Expression in unseen cell types (r = 0.94); TF–TF interactions ([[10-Summaries/fu-2025-get\|GET]]) |
| [[10-Summaries/liang-2025-scdnam-gpt\|scDNAm-GPT]] | 2025 | ~1M scWGBS cells; CpG-centred 6-mer fuzzy tokens | Mamba | 80–87% cell-type accuracy on unseen sets; pseudotime; cfDNA tumour signal ([[10-Summaries/liang-2025-scdnam-gpt\|scDNAm-GPT]]) |
| [[10-Summaries/li-2026-epizoo\|EpiZoo]] | 2026 | scATAC, 20.9M human + mouse cells; DNABERT-2 sequence-aware cCRE tokens | 2.6B-param MoE | Transfers to macaque/fish/fly/maize; scores cancer variants; predicts cell-type accessibility ([[10-Summaries/li-2026-epizoo\|EpiZoo]]) |
| [[10-Summaries/wang-2026-hicfoundation\|HiCFoundation]] | 2026 | Hi-C maps | ViT masked autoencoder | Frozen encoder fine-tuned for loops (F1 0.816), enhancement, epigenome-from-Hi-C and scHi-C ([[10-Summaries/wang-2026-hicfoundation\|HiCFoundation]]) |

## Multimodal foundation models

RNA + ATAC single-cell models, and sequence-conditioned multimodal models.

| Model | Year | Input | Training | Note |
|---|---|---|---|---|
| [[10-Summaries/wang-2025-omnireg-gpt\|OmniReg-GPT]] | 2025 | DNA, 20-kb pretraining | 270M causal DNA LM, 12 local + 2 global attention blocks; 60 h on 4 RTX 3090s | Frozen embeddings drive expression, scATAC and 2-Mb Hi-C heads ([[10-Summaries/wang-2025-omnireg-gpt\|OmniReg-GPT]]) |
| [[10-Summaries/liu-2025-scarf\|SCARF]] | 2025 | 2.7M paired 10x Multiome cells (X-Omics) | Mamba-based RNA + ATAC | Best FOSCTTM/matching on PBMC vs GLUE/Seurat/Harmony ([[10-Summaries/liu-2025-scarf\|SCARF]]) |
| [[10-Summaries/liu-2025-scmomer\|scMomer]] | 2025 | RNA + ATAC, pseudo-paired | 3-stage: scBERT + ViT-ATAC, pseudo-paired fusion, RNA → ATAC distillation | RNA-only inference; pseudo-bulk ATAC PCC 0.981 ([[10-Summaries/liu-2025-scmomer\|scMomer]]) |
| [[10-Summaries/li-2026-clm-x\|CLM-X]] | 2026 | 36M scRNA + 2.8M scATAC + 377k pseudo-paired cells | BEiT-3 multiway Transformer | Best RNA ↔ ATAC translation (lowest RMSE 7/7 datasets) ([[10-Summaries/li-2026-clm-x\|CLM-X]]) |
| [[10-Summaries/yu-2026-scdynomics\|scDynOmics]] | 2026 | 752k mouse multiome cells (promoter-ATAC per gene) | ~80M-param Linformer with TF-guided attention | LoRA adapters + IG attribution ([[10-Summaries/yu-2026-scdynomics\|scDynOmics]]) |

## Earlier sequence-based single-cell models in the wiki

- **DeepCpG** uses sequence plus neighbouring CpGs for single-cell methylation imputation ([[10-Summaries/angermueller-2017-genomebiol|DeepCpG]]).
- **scBasset** is a sequence-based scATAC model ([[10-Summaries/yuan-2022-scbasset|scBasset]]).
- **GFETM** places DNA-LM embeddings inside a scATAC topic model ([[10-Summaries/fan-2026-gfetm|GFETM]]).
- **scGPT** is the transcriptome foundation-model template ([[10-Summaries/cui-2024-natmethods|scGPT]]).

## Where this sits in the review

- **Layer coverage.** Accessibility (Atacformer, CLM-access, EpiFoundation, EpiZoo, GET), methylation (scDNAm-GPT; bulk CpGPT and MethylGPT) and 3D (HiCFoundation, Evo2HiC) are covered ([[10-Summaries/leroy-2025-atacformer|Atacformer]]; [[10-Summaries/liu-2025-clm-access|CLM-access]]; [[10-Summaries/wu-2025-epifoundation|EpiFoundation]]; [[10-Summaries/li-2026-epizoo|EpiZoo]]; [[10-Summaries/fu-2025-get|GET]]; [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]; [[10-Summaries/delimacamillo-2024-cpgpt|CpGPT]]; [[10-Summaries/ying-2024-methylgpt|MethylGPT]]; [[10-Summaries/wang-2026-hicfoundation|HiCFoundation]]; [[10-Summaries/fang-2025-evo2hic|Evo2HiC]]). ChromBERT pretrains on bulk Cistrome profiles that include 76 histone marks, but no model is pretrained on single-cell histone data or on single-cell genotypes (CNV/SNV) ([[10-Summaries/yu-2026-chrombert|ChromBERT]]) (synthesis).
- **Sequence priors.** GFETM, EpiZoo, CpGPT and Evo2HiC all reuse DNA-LM embeddings ([[10-Summaries/fan-2026-gfetm|GFETM]]; [[10-Summaries/li-2026-epizoo|EpiZoo]]; [[10-Summaries/delimacamillo-2024-cpgpt|CpGPT]]; [[10-Summaries/fang-2025-evo2hic|Evo2HiC]]).
- **Variant scoring is germline-centred.** Benchmarks are eQTL, caQTL and ClinVar ([[10-Summaries/avsec-2021-enformer|Enformer]]; [[10-Summaries/pampari-2024-chrombpnet|ChromBPNet]]; [[10-Summaries/lin-2025-genos|Genos]]); somatic and single-cell genotype inputs are largely untested (see [[variant-effect-prediction]]) (synthesis).

## Evidence for the three gaps

A verified literature search (Europe PMC, PubMed, arXiv; 2026-10-08) tested whether the gaps above were search gaps or real absences. All three held for single-cell data (synthesis).

### Genotype layer: no single-cell genotype foundation model

| Study | Year | Input | Model | Why it does not close the gap |
|---|---|---|---|---|
| [[10-Summaries/liu-2024-cot\|CoT]] | 2024 | scDNA read counts / copy-number profiles | Transformer autoencoder, self-attention; GMM clones + clone-level HMM CNA calls | Trains from scratch on each dataset with an MSE reconstruction loss and no pretraining or transfer; beats rcCAE on 10x breast data, but even the closest transformer for the scDNA genotype layer is not a foundation model ([[10-Summaries/liu-2024-cot\|CoT]]) |
| [[10-Summaries/kong-2026-mutationprojector\|MutationProjector]] | 2026 | Binary gene-level mutation/amplification/deletion calls over a fixed 468-gene panel, 30,328 bulk tumours | Graph-attention FM over 468 genes × 8 molecular networks; reused frozen | Predicts ICI/chemo response, but single-cell DNA would need gene-level per-cell calls, explicit handling of allelic dropout and missing genes, and a way to represent clone structure ([[10-Summaries/kong-2026-mutationprojector\|MutationProjector]]) |
| [[10-Summaries/sidhom-2026-tessera\|TESSERA]] | 2026 | Bulk, purity-adjusted TCGA WES SNVs + ABSOLUTE CNA segments, ~10,000 tumours | Masked SNV- and CNA-segment objectives with SNV–CNA contrastive alignment; frozen, reusable | Embeddings reused for typing, prognosis and chemo selection, but no cell- or clone-level input and never tested on single-cell copy-number profiles ([[10-Summaries/sidhom-2026-tessera\|TESSERA]]) |

### Histone layer: no single-cell histone foundation model

| Study | Year | Input | Model | Why it does not close the gap |
|---|---|---|---|---|
| [[10-Summaries/yu-2026-chrombert\|ChromBERT]] | 2026 | 6,391 bulk Cistrome profiles (991 TRs, 76 histone marks, DNase/ATAC) in 1-kb bins | BERT | Shows a bulk regulatory FM has been pretrained with 76 histone ChIP-seq channels, so the gap holds only for FMs pretrained on single-cell histone data or built mainly around histone marks; not single-cell ([[10-Summaries/yu-2026-chrombert\|ChromBERT]]) |
| [[10-Summaries/foroozandeh-2025-candi\|CANDI]] | 2025 | Bulk ENCODE histone/accessibility tracks as raw counts (35 assays, 361 merged cell types) | Self-supervised masked-assay transformer; imputes and denoises with calibrated uncertainty | Nearest histone-inclusive pretrained epigenome model, but never called a foundation model and has no single-cell input ([[10-Summaries/foroozandeh-2025-candi\|CANDI]]) |
| [[10-Summaries/morenogonzalez-2025-schistone-imputation\|Moreno-González 2025]] | 2025 | sortChIC/scCUT&Tag histone data | SCIBED benchmark of 10 borrowed, non-pretrained scRNA/scATAC imputers | No imputation or cross-modality method exists for single-cell histone data; none improved both signal and clustering; neighbouring-bin, cell-type-prior and multi-mark models are listed as missing ([[10-Summaries/morenogonzalez-2025-schistone-imputation\|Moreno-González 2025]]) |

### Somatic variants: sequence models are applied more than they are tested

| Study | Year | Variants | Model | Finding |
|---|---|---|---|---|
| [[10-Summaries/weinstock-2025-ch-noncoding-drivers\|Weinstock 2025]] | 2025 | ~147M variants in ~490K UKB blood WGS; 35 novel CH drivers (32 noncoding, incl. TERT promoter, UGT2B7, IGH) | AlphaGenome, used only for gene assignment | First genome-wide noncoding CH driver scan; discovery is purely statistical and AlphaGenome guesses cis target genes with no benchmark or validation, so CH variants remain unevaluated as a sequence-model test set ([[10-Summaries/weinstock-2025-ch-noncoding-drivers\|Weinstock 2025]]) |
| [[10-Summaries/zeng-2025-somatic-driver-lm\|GenomeBert]] | 2025 | Curated cancer somatic driver vs passenger point mutations (likely coding); 71-mutation xenograft test set | Small k-mer BERT DNA LM + XGBoost on REF−ALT embeddings | AUROC 84.6%; swapping in HyenaDNA or DeepSEA features changes AUROC by less than 1 point ([[10-Summaries/zeng-2025-somatic-driver-lm\|GenomeBert]]) |
| [[10-Summaries/fischbach-2026-alphagenome-aging\|Fischbach 2026]] | 2026 | Normal-tissue somatic SNVs and short indels from human and mouse colonic crypts (Cagan 2022) | AlphaGenome RNA-seq scores | Scores sit 10^3–10^4× below the aging transcriptome, arguing against mutation accumulation; no variant effect was measured, so near-zero predictions were never checked and somatic calibration stays untested ([[10-Summaries/fischbach-2026-alphagenome-aging\|Fischbach 2026]]) |
| [[10-Summaries/gjoni-2026-pediatric-tumor-3d\|Gjoni 2026]] | 2026 | ~300k somatic SVs from 1,843 CBTN paediatric tumours | SuPreMo-Akita, predicted 3D-contact disruption; ABC enhancer weighting | 5 recurrent hotspots; an unbenchmarked screen never checked against tumour contact maps, supported only by enhancer overlap and single-sample expression outliers ([[10-Summaries/gjoni-2026-pediatric-tumor-3d\|Gjoni 2026]]) |
| [[10-Summaries/terekhanova-2026-tal1-enhancer\|Terekhanova 2026]] | 2026 | Somatic T-ALL noncoding indels and ITDs in TAL1 downstream enhancer I | AlphaGenome, held-out test | The variants reactivate a TAL1 progenitor enhancer (short isoform, exon-4 TSS); AlphaGenome scored them significantly lower than other TAL1 enhancer variants (P = 3.32 × 10^-7) although measured TAL1 expression did not differ (P = 0.35), and did not predict the exon-4 short-isoform transcription seen in patient xenografts ([[10-Summaries/terekhanova-2026-tal1-enhancer\|Terekhanova 2026]]) |

## Open questions

- Would a DNA LM trained on single-cell genotypes, with allele dropout and amplification error, help somatic variant calling? No such model exists in this set (synthesis).
- Do pseudo-paired multimodal pretraining corpora (scMomer, CLM-X) transfer as well as truly paired ones (SCARF)? Untested ([[10-Summaries/liu-2025-scmomer|scMomer]]; [[10-Summaries/li-2026-clm-x|CLM-X]]; [[10-Summaries/liu-2025-scarf|SCARF]]) (synthesis).
- Self-supervised DNA LMs often do not beat supervised or simple baselines on regulatory tasks (see [[dna-language-model]] › Contested points); when is pretraining worth its cost ([[10-Summaries/sanabria-2024-grover|GROVER]])?
- AlphaGenome's somatic calibration is untested in normal tissue and under-predicts a somatic T-ALL enhancer; how far can germline-trained scores be trusted on somatic variants ([[10-Summaries/fischbach-2026-alphagenome-aging|Fischbach 2026]]; [[10-Summaries/terekhanova-2026-tal1-enhancer|Terekhanova 2026]])? (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/computational-methods|Computational methods]] — The tool layer: aligners, formats, callers, imputers, integrators and network inference.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Genome-wide chromatin accessibility in individual cells via Tn5.
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5mC at CpG dinucleotides, the most stable epigenetic mark.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromosome territories, A/B compartments and TADs in the nucleus.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Two or more modalities measured in the same cell.
> - `hub` [[40-Topics/mosaic-variant-calling|Mosaic variant calling]] — Detecting low-allele-frequency somatic variants.

## All sources on this page

> [!info]- 79 summaries cited here
> - [[10-Summaries/angermueller-2017-genomebiol|Angermueller 2017]]
> - [[10-Summaries/aspidova-2026-moderngena|ModernGENA 2026]]
> - [[10-Summaries/avsec-2021-enformer|Enformer 2021]]
> - [[10-Summaries/avsec-2026-alphagenome|AlphaGenome 2026]]
> - [[10-Summaries/ayanian-2025-strand|STRAND 2025]]
> - [[10-Summaries/benegas-2025-gpn-msa|GPN-MSA 2025]]
> - [[10-Summaries/boshar-2025-ntv3|NTv3 2025]]
> - [[10-Summaries/brixi-2026-evo2|Evo 2 2026]]
> - [[10-Summaries/chen-2022-sei|Sei 2022]]
> - [[10-Summaries/chen-2023-genomicbert|genomicBERT 2023]]
> - [[10-Summaries/chen-2026-genart|GenART 2026]]
> - [[10-Summaries/cui-2024-natmethods|Cui 2024]]
> - [[10-Summaries/dallatorre-2025-nucleotide-transformer|Nucleotide Transformer 2025]]
> - [[10-Summaries/dealmeida-2025-segmentnt|SegmentNT 2025]]
> - [[10-Summaries/delimacamillo-2024-cpgpt|CpGPT 2024]]
> - [[10-Summaries/ding-2025-nucel|NucEL 2025]]
> - [[10-Summaries/duan-2025-janusdna|JanusDNA 2025]]
> - [[10-Summaries/ellington-2024-aido-dna|AIDO.DNA 2024]]
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
> - [[10-Summaries/fang-2025-evo2hic|Evo2HiC 2025]]
> - [[10-Summaries/fischbach-2026-alphagenome-aging|Fischbach 2026]]
> - [[10-Summaries/fishman-2025-gena-lm|GENA-LM 2025]]
> - [[10-Summaries/foroozandeh-2025-candi|Foroozandeh 2025 CANDI]]
> - [[10-Summaries/fu-2025-get|GET 2025]]
> - [[10-Summaries/fudenberg-2020-akita|Akita 2020]]
> - [[10-Summaries/gao-2024-epigept|EpiGePT 2024]]
> - [[10-Summaries/gjoni-2026-pediatric-tumor-3d|Gjoni 2026]]
> - [[10-Summaries/hingerl-2025-scooby|scooby 2025]]
> - [[10-Summaries/ji-2021-dnabert|DNABERT 2021]]
> - [[10-Summaries/kelley-2016-basset|Basset 2016]]
> - [[10-Summaries/kelley-2018-basenji|Basenji 2018]]
> - [[10-Summaries/kempynck-2026-crested|CREsted 2026]]
> - [[10-Summaries/kim-2026-dnachunker|DNAChunker 2026]]
> - [[10-Summaries/kong-2026-mutationprojector|Kong 2026 (Cancer Discov)]]
> - [[10-Summaries/lal-2026-decima|Decima 2026]]
> - [[10-Summaries/leib-2026-dnt|DNT 2026]]
> - [[10-Summaries/leroy-2025-atacformer|Atacformer 2025]]
> - [[10-Summaries/li-2025-bmfm-dna|BMFM-DNA 2025]]
> - [[10-Summaries/li-2026-clm-x|CLM-X 2026]]
> - [[10-Summaries/li-2026-epizoo|EpiZoo 2026]]
> - [[10-Summaries/li-2026-generator|GENERator 2026]]
> - [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT 2025]]
> - [[10-Summaries/lin-2025-genos|Genos 2026]]
> - [[10-Summaries/lin-2026-epinformer|EPInformer 2026]]
> - [[10-Summaries/linder-2025-borzoi|Borzoi 2025]]
> - [[10-Summaries/liu-2024-cot|Liu 2024 (Brief Bioinform)]]
> - [[10-Summaries/liu-2025-clm-access|CLM-access 2025]]
> - [[10-Summaries/liu-2025-scarf|SCARF 2025]]
> - [[10-Summaries/liu-2025-scmomer|scMomer 2025]]
> - [[10-Summaries/liu-2026-ukbiobert|UKBioBERT 2026]]
> - [[10-Summaries/long-2025-mutbert|MutBERT 2025]]
> - [[10-Summaries/ma-2025-hybridna|HybriDNA 2025]]
> - [[10-Summaries/medvedev-2025-biofm|BioFM 2025]]
> - [[10-Summaries/morenogonzalez-2025-schistone-imputation|Moreno-González 2025 SCIBED]]
> - [[10-Summaries/nguyen-2023-hyenadna|HyenaDNA 2023]]
> - [[10-Summaries/pampari-2024-chrombpnet|ChromBPNet 2024]]
> - [[10-Summaries/salman-2026-mendel|Mendel 2026]]
> - [[10-Summaries/sanabria-2024-grover|GROVER 2024]]
> - [[10-Summaries/schiff-2024-caduceus|Caduceus 2024]]
> - [[10-Summaries/shen-2026-omnina|OmniNA 2026]]
> - [[10-Summaries/sidhom-2026-tessera|Sidhom 2026 (bioRxiv)]]
> - [[10-Summaries/su-2025-atgc-gen|ATGC-Gen 2025]]
> - [[10-Summaries/sun-2026-succeed|SUCCEED 2026]]
> - [[10-Summaries/terekhanova-2026-tal1-enhancer|Terekhanova 2026]]
> - [[10-Summaries/vishniakov-2025-gene42|Gene42 2025]]
> - [[10-Summaries/wang-2025-omnireg-gpt|OmniReg-GPT 2025]]
> - [[10-Summaries/wang-2026-hicfoundation|HiCFoundation 2026]]
> - [[10-Summaries/weinstock-2025-ch-noncoding-drivers|Weinstock 2025]]
> - [[10-Summaries/wu-2025-epifoundation|EpiFoundation 2025]]
> - [[10-Summaries/ying-2024-methylgpt|MethylGPT 2024]]
> - [[10-Summaries/yu-2026-chrombert|Yu 2026 ChromBERT]]
> - [[10-Summaries/yu-2026-scdynomics|scDynOmics 2026]]
> - [[10-Summaries/yuan-2022-scbasset|Yuan & Kelley 2022]]
> - [[10-Summaries/zeng-2025-somatic-driver-lm|GenomeBert]]
> - [[10-Summaries/zhang-2025-deepgene|DeepGene 2025]]
> - [[10-Summaries/zhou-2015-deepsea|DeepSEA 2015]]
> - [[10-Summaries/zhou-2018-expecto|ExPecto 2018]]
> - [[10-Summaries/zhou-2022-orca|Orca 2022]]
> - [[10-Summaries/zhou-2023-dnabert-2|DNABERT-2 2023]]
