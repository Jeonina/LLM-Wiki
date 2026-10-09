---
type: concept
title: DNA language model
aliases: [genomic language model, gLM, genome foundation model, GFM, DNA foundation model, nucleotide language model]
tags: [foundation-model, dna-language-model, self-supervised, deep-learning, sequence-model]
created: 2026-10-08
updated: 2026-10-09
---

# DNA language model

> A model pretrained on DNA sequence alone, by masked-token or next-token prediction, whose learned representations are then probed, fine-tuned or scored zero-shot for genomic tasks ([[10-Summaries/ji-2021-dnabert]]; [[10-Summaries/nguyen-2023-hyenadna]]; [[10-Summaries/brixi-2026-evo2]]).

## Definition

A DNA language model (DNA LM, also called a genome foundation model) learns from unlabelled sequence. Encoder models such as DNABERT mask tokens and predict them from both sides ([[10-Summaries/ji-2021-dnabert]]); decoder models such as HyenaDNA, GENERator and Evo 2 predict the next nucleotide or token ([[10-Summaries/nguyen-2023-hyenadna]]; [[10-Summaries/li-2026-generator]]; [[10-Summaries/brixi-2026-evo2]]). Downstream use takes three forms: a small head on frozen embeddings, full or parameter-efficient fine-tuning, and zero-shot scoring from the model's own likelihoods ([[10-Summaries/dallatorre-2025-nucleotide-transformer]]; [[10-Summaries/benegas-2025-gpn-msa]]).

This is distinct from a [[sequence-to-function-model]], which is trained with labels (measured chromatin, expression or contact tracks) rather than on sequence alone; NTv3 and SUCCEED sit between the two ([[10-Summaries/boshar-2025-ntv3]]; [[10-Summaries/sun-2026-succeed]]).

## Why it matters

- **A sequence prior for sparse single-cell data.** Several single-cell epigenome models in this wiki borrow DNA-LM embeddings to describe genomic regions: GFETM fine-tunes DNABERT inside a topic model for scATAC ([[10-Summaries/fan-2026-gfetm]]), EpiZoo adds a frozen DNABERT-2 sequence component to every scATAC token ([[10-Summaries/li-2026-epizoo]]), CpGPT keys each CpG with Nucleotide Transformer v2 embeddings ([[10-Summaries/delimacamillo-2024-cpgpt]]), and Evo2HiC distils Evo 2 into a small CNN for Hi-C ([[10-Summaries/fang-2025-evo2hic]]).
- **Variant scoring without labels.** Likelihood-ratio and embedding-distance scores let a DNA LM rank variants it never saw labelled; see [[variant-effect-prediction]].
- **No genotype-layer single-cell model yet.** Every DNA LM here is trained on reference genomes, population genomes or alignments; none is trained on single-cell genotypes or somatic mutations, and the paper-list search for scDNA-seq foundation models returned none (synthesis).

## Variants and refinements

**By architecture** (synthesis of the summaries below):
- *Encoder, masked LM:* DNABERT, DNABERT-2, Nucleotide Transformer, GROVER, GENA-LM, ModernGENA, AIDO.DNA, MutBERT, BMFM-DNA, DeepGene, genomicBERT, DNAChunker, GenART, UKBioBERT; NucEL replaces masking with ELECTRA replaced-token detection ([[10-Summaries/ding-2025-nucel]]).
- *Decoder, next-token:* HyenaDNA, Evo 2, GENERator, Gene42, HybriDNA, OmniReg-GPT, Genos, Mendel, STRAND, OmniNA, BioFM.
- *Bidirectional state-space:* Caduceus adds reverse-complement equivariance ([[10-Summaries/schiff-2024-caduceus]]); JanusDNA fuses forward and backward causal stacks ([[10-Summaries/duan-2025-janusdna]]).
- *Alignment-conditioned:* GPN-MSA reads a 100-vertebrate alignment ([[10-Summaries/benegas-2025-gpn-msa]]).
- *Variant- and genotype-aware inputs:* MutBERT (allele frequencies), BMFM-DNA (dbSNP symbols), BioFM (variant tokens), DeepGene (pangenome graph), Mendel and DNT (diploid genotypes), UKBioBERT (UK Biobank variants) ([[10-Summaries/long-2025-mutbert]]; [[10-Summaries/li-2025-bmfm-dna]]; [[10-Summaries/medvedev-2025-biofm]]; [[10-Summaries/zhang-2025-deepgene]]; [[10-Summaries/salman-2026-mendel]]; [[10-Summaries/leib-2026-dnt]]; [[10-Summaries/liu-2026-ukbiobert]]).
- *Fine-tunes of a pretrained LM:* SegmentNT segments 14 element classes on top of Nucleotide Transformer ([[10-Summaries/dealmeida-2025-segmentnt]]).

**Models in this wiki** (38, by year):

- **DNABERT** (2021) — DNABERT was the first widely used BERT-style DNA language model: a 12-layer encoder pre-trained by masked k-mer prediction on the human reference genome and fine-tuned for promoters, TF-binding sites and splice sites ([[10-Summaries/ji-2021-dnabert]])
- **DNABERT-2** (2023) — DNABERT-2 is a 117M-parameter multi-species (135 species) BERT-style DNA LM with ALiBi and FlashAttention that roughly matches the 2.5B-parameter NT-2500M-multi on its GUE benchmark at about 92× less pre-training GPU time ([[10-Summaries/zhou-2023-dnabert-2]])
- **HyenaDNA** (2023) — HyenaDNA is a decoder-only DNA LM built from Hyena long-convolution operators, pre-trained by next-nucleotide prediction on the human reference with contexts up to 1M bases and 0.4–6.6M parameters, 160× faster than a Transformer at 1M tokens ([[10-Summaries/nguyen-2023-hyenadna]])
- **genomicBERT** (2023) — genomicBERT is an 89.2M-parameter MosaicBERT encoder pretrained for only 10k steps (about 15 h on 4 A10G GPUs) on GRCh38 with 10% masking, packaged in the conda toolkit genomeNLP ([[10-Summaries/chen-2023-genomicbert]]).
- **AIDO.DNA** (2024) — AIDO.DNA argues that DNA language models are limited by representation capacity rather than context length, reaching a GUE average of 73.3 MCC with a 7B encoder at only 4 kb context ([[10-Summaries/ellington-2024-aido-dna]]).
- **Caduceus** (2024) — Caduceus builds DNA LMs from BiMamba and MambaDNA blocks so that models are bidirectional and reverse-complement equivariant by construction; RC equivariance and weight-tied bidirectionality both lowered masked-LM loss on the human genome ([[10-Summaries/schiff-2024-caduceus]])
- **CpGPT** (2024) — CpGPT uses frozen Nucleotide Transformer v2-500M embeddings of the 2,001 bp around each CpG as its locus identifier; this beat HyenaDNA backbones in ablation and lets the model query CpGs never seen in training ([[10-Summaries/delimacamillo-2024-cpgpt]]).
- **GROVER** (2024) — GROVER is a BERT DNA LM trained only on hg19 whose window embeddings separate repeat classes, chromatin states, element orientation and replication timing; it also shows a TF-IDF frequency baseline nearly matches DNA LMs on standard NT enhancer and promoter tasks ([[10-Summaries/sanabria-2024-grover]])
- **ATGC-Gen** (2025) — ATGC-Gen shows plain decoder and encoder transformers with cross-modal conditioning outperform discrete-diffusion and flow-matching baselines on regulatory-sequence benchmarks (promoter MSE 0.0192 vs 0.0219 for D3; enhancer FBD 0.5080 vs 1.0404 for Dirichlet flow matching) ([[10-Summaries/su-2025-atgc-gen]]).
- **BMFM-DNA** (2025) — BMFM-DNA-SNP, a ModernBERT encoder pretrained on a genome where dbSNP variant sites are written as single symbols, beats its reference-only twin on five of six fine-tuning tasks by about 0.5-1.5 points ([[10-Summaries/li-2025-bmfm-dna]]).
- **BioFM** (2025) — BioFM is pretrained by next-token prediction on 333B tokens from 50 phased 1000 Genomes individuals rather than the reference alone, and its last-layer embeddings need no per-task layer search ([[10-Summaries/medvedev-2025-biofm]]).
- **DeepGene** (2025) — DeepGene is the only model in this cohort pretrained on a pangenome graph rather than linear genomes — the HPRC 47-individual Minigraph, made acyclic, BPE-tokenised per node and cut into 128-token subgraphs — and reports the best GUE average (67.79) at 118M parameters ([[10-Summaries/zhang-2025-deepgene]]).
- **Evo2HiC** (2025) — Evo2HiC distils Evo 2-7B layer-27 embeddings into a 3.6 M-parameter CNN with a SigLIP contrastive loss; trained on human sequence only, it keeps Evo 2's pairwise bin similarity (r = 0.63 human, 0.47 mouse vs 0.13/0.14 undistilled) at about 500× faster inference ([[10-Summaries/fang-2025-evo2hic]])
- **GENA-LM** (2025) — GENA-LM is an encoder-only BERT/BigBird family pre-trained with masked language modelling on the human T2T assembly, reaching 4.5 kb with full attention, 36 kb with sparse attention and 16–50 kb with a recurrent memory transformer ([[10-Summaries/fishman-2025-gena-lm]]).
- **GPN-MSA** (2025) — GPN-MSA conditions a small RoFormer masked LM on the 100-vertebrate whole-genome alignment and, trained in ~3.5 h on four A100s, outperforms the 2.5B-parameter Nucleotide Transformer and HyenaDNA on ClinVar missense classification ([[10-Summaries/benegas-2025-gpn-msa]]).
- **Gene42** (2025) — Gene42 is a decoder-only LLaMA-style DNA model (500M and 1.1B parameters) that keeps full dense attention out to 192,000 bp by raising the RoPE base frequency from 10k to 15M during staged continued pre-training ([[10-Summaries/vishniakov-2025-gene42]]).
- **HybriDNA** (2025) — HybriDNA interleaves Mamba2 and Transformer blocks 7:1 in a decoder-only DNA model trained by next-token prediction on 845 species (~160 billion nucleotides), scaling 300M → 3B → 7B with context warmed from 8k to 131k tokens ([[10-Summaries/ma-2025-hybridna]]).
- **JanusDNA** (2025) — JanusDNA introduces Janus modelling, where two independent causal Mamba/MoE stacks read the sequence forward and backward and one masked FlexAttention layer fuses them so every token is predicted from both sides, giving masked-model bidirectionality with autoregressive full-token training efficiency ([[10-Summaries/duan-2025-janusdna]]).
- **MutBERT** (2025) — MutBERT replaces one-hot reference input with per-position allele-frequency distributions from 1000 Genomes and beats an identical reference-only twin (average MCC 66.36 vs 64.64 over 23 tasks) ([[10-Summaries/long-2025-mutbert]]).
- **NTv3** (2025) — NTv3 abandons the Nucleotide Transformer's 6-mer encoder for a U-Net with single-base tokens pretrained by MLM on ~11 trillion OpenGenome2 tokens up to 1 Mb context ([[10-Summaries/boshar-2025-ntv3]]).
- **NucEL** (2025) — NucEL is the first ELECTRA-style genomic model by its authors' account: a 93M ModernBERT discriminator detects generator-replaced bases at every position, giving 6.67x the supervision of 15% MLM, and averages 75.16 on GUE vs 72.94 for NT-2.5B-multi ([[10-Summaries/ding-2025-nucel]]).
- **Nucleotide Transformer** (2025) — Nucleotide Transformer compares equal-sized DNA LMs trained on the human reference, 3,202 human genomes and 850 species, and finds multispecies data helps human tasks more than human population data; NT-v2 250M beat the 2.5B model at one tenth the size ([[10-Summaries/dallatorre-2025-nucleotide-transformer]])
- **OmniReg-GPT** (2025) — OmniReg-GPT is a 270M-parameter causal DNA model with 12 sliding-window local attention blocks and 2 global ones, cutting attention cost to O(L·w) so 200-kb inputs fit on one 32-GB V100 and 20-kb pre-training took 60 h on four RTX 3090s ([[10-Summaries/wang-2025-omnireg-gpt]]).
- **STRAND** (2025) — STRAND trains a ~1B decoder-only DNA LM on raw aligned 151-bp exome reads from up to 499 Tapestry participants plus reference and multispecies genomes, finding consecutive positional packing and inverse-frequency loss weighting work best ([[10-Summaries/ayanian-2025-strand]]).
- **SegmentNT** (2025) — SegmentNT is a fine-tune of the pretrained Nucleotide Transformer rather than a new pretrained model, and provides one of the clearest cases for DNA-LM pretraining: the same architecture with a randomly initialised NT encoder reaches average MCC 0.16 against 0.37, and converges seven times slower ([[10-Summaries/dealmeida-2025-segmentnt]]).
- **CREsted** (2026) — When fine-tuned to predict cell-type-specific accessibility in mouse cortex, HyenaDNA and Nucleotide Transformer did worse than both a fine-tuned Borzoi and a CREsted CNN trained from scratch ([[10-Summaries/kempynck-2026-crested]]).
- **DNAChunker** (2026) — DNAChunker adapts H-Net-style dynamic chunking to bidirectional MLM, adding mask protection and masked residual gating so [MASK] tokens do not leak, and reaches NT-benchmark average MCC 0.772 vs 0.728 for the 1.2B GENERator ([[10-Summaries/kim-2026-dnachunker]]).
- **DNT** (2026) — DNT continually pretrains Nucleotide Transformer v3 (8M/100M) on phased 1000 Genomes sequences written as one diploid token stream, and needs an auxiliary contrastive phase loss before the model actually uses phase tokens ([[10-Summaries/leib-2026-dnt]]).
- **EpiZoo** (2026) — EpiZoo uses a frozen DNABERT-2 encoder (SEAM), calibrated to learned cCRE identity embeddings, to add a sequence component to every scATAC token, and that component is what carries over to species without coordinate correspondence ([[10-Summaries/li-2026-epizoo]]).
- **Evo 2** (2026) — Evo 2 is the current scale reference for autoregressive single-nucleotide DNA language models: 40B parameters, 9.3 trillion training tokens from bacteria, archaea, eukarya and bacteriophage, 1 Mb context, StripedHyena 2 convolutional multi-hybrid architecture, with weights, code and the OpenGenome2 dataset released openly ([[10-Summaries/brixi-2026-evo2]])
- **GENERator** (2026) — GENERator is a decoder-only 6-mer DNA model (1.2B and 3B parameters, 98-kb context) pre-trained by next-token prediction on 386 billion nucleotides of gene-centric eukaryotic RefSeq sequence ([[10-Summaries/li-2026-generator]]).
- **GenART** (2026) — GenART puts a trainable tokenizer between nucleotide-level and token-level Transformer stacks and reports the best NT (+3.41%) and GUE (+1.22%) averages at 350M/1B, close to Evo2-7B ([[10-Summaries/chen-2026-genart]]).
- **Genos** (2026) — Genos is a mixture-of-experts DNA model (8 experts, 2 active per token; 1.25B and 10.27B total parameters) trained by next-token prediction at single-nucleotide resolution on 636 human assemblies from HPRC, HGSVC and CEPH with a context window up to 1 Mb ([[10-Summaries/lin-2025-genos]]).
- **Mendel** (2026) — Mendel trains Evo 2's architecture from scratch on GTEx personal genomes with loss only on diploid genotype tokens, recovering held-out genotypes with 0.984 accuracy versus 0.311 for Evo 2, though most of that accuracy is the major allele ([[10-Summaries/salman-2026-mendel]]).
- **ModernGENA** (2026) — ModernGENA-large (377M ModernBERT encoder, MLM, ~1.3T tokens from 443 vertebrate assemblies) ranks first among encoder-only DNA models under 500M on the NT benchmark and second overall behind the 1.2B GENERator ([[10-Summaries/aspidova-2026-moderngena]]).
- **OmniNA** (2026) — OmniNA is the rare DNA language model trained on sequence and free-text annotation in one token stream — 91.7 million NCBI nt sequences, 1,076.2 billion bases and 197 million annotation words — then fine-tuned as a question-answering model over 23 tasks ([[10-Summaries/shen-2026-omnina]]).
- **SUCCEED** (2026) — When used as frozen sequence encoders with a shared ATAC encoder, the supervised models SUCCEED and Sei beat self-supervised DNABERT-2, Nucleotide Transformer and HyenaDNA on cell-type epigenome, ATAC denoising and Hi-C prediction tasks, though the language models were run on chunked 1–8 kb inputs ([[10-Summaries/sun-2026-succeed]])
- **UKBioBERT** (2026) — UKBioBERT continues DNABERT-2 MLM pretraining on sequences edited with ~13 million UK Biobank variants and gives the best gene-function clustering score among a broad panel of DNA LMs ([[10-Summaries/liu-2026-ukbiobert]]).

## Contested points

- **Do DNA LMs beat supervised or simple baselines?** Used as frozen encoders, supervised SUCCEED and Sei beat DNABERT-2, Nucleotide Transformer and HyenaDNA ([[10-Summaries/sun-2026-succeed]]); fine-tuned HyenaDNA and Nucleotide Transformer did worse than a small CNN and Borzoi in CREsted ([[10-Summaries/kempynck-2026-crested]]); SpliceAI still beat the best transformer on splice sites ([[10-Summaries/fishman-2025-gena-lm]]); a TF-IDF frequency baseline nearly matched DNA LMs on standard enhancer and promoter tasks ([[10-Summaries/sanabria-2024-grover]]).
- **Frozen versus fine-tuned.** Frozen DNA-LM peak embeddings did not significantly beat randomly initialised ones in GFETM; only joint fine-tuning helped ([[10-Summaries/fan-2026-gfetm]]). SegmentNT, in contrast, shows a clear pretraining gain once fine-tuned (average MCC 0.37 vs 0.16 from a random encoder) ([[10-Summaries/dealmeida-2025-segmentnt]]).
- **Bigger is not always better.** NT-v2 250M beat the 2.5B Nucleotide Transformer ([[10-Summaries/dallatorre-2025-nucleotide-transformer]]), and AIDO.DNA-300M scored ClinVar better than the 7B model ([[10-Summaries/ellington-2024-aido-dna]]).
- **Benchmarks are reused, not rerun.** Many papers copy baseline numbers from earlier papers or leaderboards (e.g. [[10-Summaries/vishniakov-2025-gene42]]; [[10-Summaries/kim-2026-dnachunker]]; [[10-Summaries/fishman-2025-gena-lm]]), and HyenaDNA's Nucleotide Transformer comparison used its own splits, which conflict with later reports ([[10-Summaries/nguyen-2023-hyenadna]]).

## Examples

- Evo 2: 40B parameters, 1 Mb context, trained across all domains of life ([[10-Summaries/brixi-2026-evo2]]).
- GPN-MSA: an 86M alignment-based model that beats the 2.5B Nucleotide Transformer on ClinVar missense ([[10-Summaries/benegas-2025-gpn-msa]]).

## Added 2026-10-09 — foundation-model gap evidence

- A 1.7–3.7 M-parameter k-mer BERT (GenomeBert) pretrained on GRCh37 gave driver-prediction features only marginally better than HyenaDNA or DeepSEA features (CV AUROC 83.25 vs 82.83 vs 82.34%), while the choice of downstream classifier moved AUROC by about 16 points ([[10-Summaries/zeng-2025-somatic-driver-lm]])

## Related

- [[sequence-to-function-model]] · [[genomic-tokenization]] · [[variant-effect-prediction]] · [[single-cell-foundation-model]] · [[convolutional-neural-network]]
- [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/computational-methods]]
