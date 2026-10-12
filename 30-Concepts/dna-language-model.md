---
type: concept
title: DNA language model
aliases: [genomic language model, gLM, genome foundation model, GFM, DNA foundation model, nucleotide language model]
tags: [foundation-model, dna-language-model, self-supervised, deep-learning, sequence-model]
created: 2026-10-08
updated: 2026-10-12
---

# DNA language model

> A model pretrained on DNA sequence alone, by masked-token or next-token prediction, whose learned representations are then probed, fine-tuned or scored zero-shot for genomic tasks ([[10-Summaries/ji-2021-dnabert|DNABERT]]; [[10-Summaries/nguyen-2023-hyenadna|HyenaDNA]]; [[10-Summaries/brixi-2026-evo2|Evo 2]]).

> [!abstract] 한눈에
> DNA language model은 label 없이 DNA 서열만으로 masked-token 또는 next-token 예측을 학습한 모델이며, 그 표현을 고정해서 쓰거나 fine-tuning하거나 likelihood로 zero-shot 변이 점수를 매긴다 ([[10-Summaries/ji-2021-dnabert|DNABERT]]; [[10-Summaries/brixi-2026-evo2|Evo 2]]). 다만 supervised 모델이나 단순한 baseline을 실제로 넘어서는지는 아직 논쟁 중이고 ([[10-Summaries/sun-2026-succeed|SUCCEED]]; [[10-Summaries/sanabria-2024-grover|GROVER]]), single-cell genotype으로 학습한 모델은 아직 없다 (synthesis).

<!-- explainer-links -->
> [!tip] 📘 교재
> [서열 모델과 foundation model 교재](../60-Explainers/sequence-models-and-foundation-models.html)
<!-- /explainer-links -->

## Definition

A DNA language model (DNA LM, also called a genome foundation model) learns from unlabelled sequence ([[10-Summaries/ji-2021-dnabert|DNABERT]]). Encoder models such as DNABERT mask tokens and predict them from both sides ([[10-Summaries/ji-2021-dnabert|DNABERT]]); decoder models such as HyenaDNA, GENERator and Evo 2 predict the next nucleotide or token ([[10-Summaries/nguyen-2023-hyenadna|HyenaDNA]]; [[10-Summaries/li-2026-generator|GENERator]]; [[10-Summaries/brixi-2026-evo2|Evo 2]]). Downstream use takes three forms: a small head on frozen embeddings, full or parameter-efficient fine-tuning, and zero-shot scoring from the model's own likelihoods ([[10-Summaries/dallatorre-2025-nucleotide-transformer|Nucleotide Transformer]]; [[10-Summaries/benegas-2025-gpn-msa|GPN-MSA]]).

This is distinct from a [[sequence-to-function-model]], which is trained with labels (measured chromatin, expression or contact tracks) rather than on sequence alone; NTv3 and SUCCEED sit between the two ([[10-Summaries/boshar-2025-ntv3|NTv3]]; [[10-Summaries/sun-2026-succeed|SUCCEED]]).

## Why it matters

- **A sequence prior for sparse single-cell data.** Several single-cell epigenome models in this wiki borrow DNA-LM embeddings to describe genomic regions: GFETM fine-tunes DNABERT inside a topic model for scATAC ([[10-Summaries/fan-2026-gfetm|GFETM]]), EpiZoo adds a frozen DNABERT-2 sequence component to every scATAC token ([[10-Summaries/li-2026-epizoo|EpiZoo]]), CpGPT keys each CpG with Nucleotide Transformer v2 embeddings ([[10-Summaries/delimacamillo-2024-cpgpt|CpGPT]]), and Evo2HiC distils Evo 2 into a small CNN for Hi-C ([[10-Summaries/fang-2025-evo2hic|Evo2HiC]]).
- **Variant scoring without labels.** Likelihood-ratio and embedding-distance scores let a DNA LM rank variants it never saw labelled; see [[variant-effect-prediction]] (synthesis).
- **No genotype-layer single-cell model yet.** Every DNA LM here is trained on reference genomes, population genomes or alignments; none is trained on single-cell genotypes or somatic mutations, and the paper-list search for scDNA-seq foundation models returned none (synthesis).

## Models by architecture

The tables cover the 38 models in this wiki that build or use a DNA LM; the grouping below is a synthesis of the summaries cited in each row (synthesis). Tokenisation choices are covered in [[genomic-tokenization]].

### Encoders (masked LM and variants)

| Model | Year | Design | Key result | Source |
|---|---|---|---|---|
| DNABERT | 2021 | 12-layer BERT encoder, masked k-mer prediction on the human reference | First widely used BERT-style DNA LM; fine-tuned for promoters, TF-binding sites and splice sites | ([[10-Summaries/ji-2021-dnabert\|DNABERT]]) |
| DNABERT-2 | 2023 | 117M-parameter multi-species (135 species) BERT with ALiBi and FlashAttention | Roughly matches the 2.5B NT-2500M-multi on its GUE benchmark at about 92× less pre-training GPU time | ([[10-Summaries/zhou-2023-dnabert-2\|DNABERT-2]]) |
| genomicBERT | 2023 | 89.2M-parameter MosaicBERT, 10% masking on GRCh38, only 10k steps (about 15 h on 4 A10G GPUs) | Packaged in the conda toolkit genomeNLP | ([[10-Summaries/chen-2023-genomicbert\|genomicBERT]]) |
| AIDO.DNA | 2024 | 7B encoder at only 4 kb context | Argues DNA LMs are limited by representation capacity, not context length; GUE average 73.3 MCC | ([[10-Summaries/ellington-2024-aido-dna\|AIDO.DNA]]) |
| GROVER | 2024 | BERT trained only on hg19 | Window embeddings separate repeat classes, chromatin states, element orientation and replication timing; a TF-IDF frequency baseline nearly matches DNA LMs on standard NT enhancer and promoter tasks | ([[10-Summaries/sanabria-2024-grover\|GROVER]]) |
| GENA-LM | 2025 | Encoder-only BERT/BigBird family, MLM on the human T2T assembly | Reaches 4.5 kb with full attention, 36 kb with sparse attention and 16–50 kb with a recurrent memory transformer | ([[10-Summaries/fishman-2025-gena-lm\|GENA-LM]]) |
| Nucleotide Transformer | 2025 | Equal-sized DNA LMs trained on the human reference, 3,202 human genomes and 850 species | Multispecies data helps human tasks more than human population data; NT-v2 250M beat the 2.5B model at one tenth the size | ([[10-Summaries/dallatorre-2025-nucleotide-transformer\|Nucleotide Transformer]]) |
| NTv3 | 2025 | Drops the 6-mer encoder for a U-Net with single-base tokens; MLM on ~11 trillion OpenGenome2 tokens up to 1 Mb context | Sits between a DNA LM and a sequence-to-function model | ([[10-Summaries/boshar-2025-ntv3\|NTv3]]) |
| NucEL | 2025 | 93M ModernBERT discriminator trained ELECTRA-style: detects generator-replaced bases at every position, 6.67× the supervision of 15% MLM | First ELECTRA-style genomic model by its authors' account; GUE average 75.16 vs 72.94 for NT-2.5B-multi | ([[10-Summaries/ding-2025-nucel\|NucEL]]) |
| DNAChunker | 2026 | H-Net-style dynamic chunking adapted to bidirectional MLM, with mask protection and masked residual gating so [MASK] tokens do not leak | NT-benchmark average MCC 0.772 vs 0.728 for the 1.2B GENERator | ([[10-Summaries/kim-2026-dnachunker\|DNAChunker]]) |
| GenART | 2026 | Trainable tokenizer between nucleotide-level and token-level Transformer stacks; 350M/1B | Best NT (+3.41%) and GUE (+1.22%) averages, close to Evo2-7B | ([[10-Summaries/chen-2026-genart\|GenART]]) |
| ModernGENA | 2026 | ModernGENA-large: 377M ModernBERT encoder, MLM, ~1.3T tokens from 443 vertebrate assemblies | First among encoder-only DNA models under 500M on the NT benchmark, second overall behind the 1.2B GENERator | ([[10-Summaries/aspidova-2026-moderngena\|ModernGENA]]) |

### Decoders (next-token prediction)

| Model | Year | Design | Key result | Source |
|---|---|---|---|---|
| HyenaDNA | 2023 | Decoder-only, Hyena long-convolution operators; next-nucleotide prediction on the human reference; contexts up to 1M bases; 0.4–6.6M parameters | 160× faster than a Transformer at 1M tokens | ([[10-Summaries/nguyen-2023-hyenadna\|HyenaDNA]]) |
| Gene42 | 2025 | Decoder-only LLaMA-style, 500M and 1.1B parameters | Keeps full dense attention out to 192,000 bp by raising the RoPE base frequency from 10k to 15M during staged continued pre-training | ([[10-Summaries/vishniakov-2025-gene42\|Gene42]]) |
| HybriDNA | 2025 | Mamba2 and Transformer blocks interleaved 7:1; 845 species (~160 billion nucleotides) | Scales 300M → 3B → 7B with context warmed from 8k to 131k tokens | ([[10-Summaries/ma-2025-hybridna\|HybriDNA]]) |
| OmniReg-GPT | 2025 | 270M-parameter causal model, 12 sliding-window local attention blocks and 2 global ones, attention cost O(L·w) | 200-kb inputs fit on one 32-GB V100; 20-kb pre-training took 60 h on four RTX 3090s | ([[10-Summaries/wang-2025-omnireg-gpt\|OmniReg-GPT]]) |
| STRAND | 2025 | ~1B decoder trained on raw aligned 151-bp exome reads from up to 499 Tapestry participants plus reference and multispecies genomes | Consecutive positional packing and inverse-frequency loss weighting work best | ([[10-Summaries/ayanian-2025-strand\|STRAND]]) |
| Evo 2 | 2026 | 40B parameters, 9.3 trillion tokens from bacteria, archaea, eukarya and bacteriophage, 1 Mb context, StripedHyena 2 convolutional multi-hybrid | Current scale reference for autoregressive single-nucleotide DNA LMs; weights, code and the OpenGenome2 dataset released openly | ([[10-Summaries/brixi-2026-evo2\|Evo 2]]) |
| GENERator | 2026 | Decoder-only 6-mer model, 1.2B and 3B parameters, 98-kb context; 386 billion nucleotides of gene-centric eukaryotic RefSeq | — | ([[10-Summaries/li-2026-generator\|GENERator]]) |
| Genos | 2026 | Mixture of experts (8 experts, 2 active per token; 1.25B and 10.27B total), single-nucleotide resolution, 636 human assemblies from HPRC, HGSVC and CEPH | Context window up to 1 Mb | ([[10-Summaries/lin-2025-genos\|Genos]]) |
| OmniNA | 2026 | Sequence and free-text annotation in one token stream: 91.7 million NCBI nt sequences, 1,076.2 billion bases, 197 million annotation words | Fine-tuned as a question-answering model over 23 tasks | ([[10-Summaries/shen-2026-omnina\|OmniNA]]) |

### Bidirectional state-space and alignment-conditioned models

| Model | Year | Design | Key result | Source |
|---|---|---|---|---|
| Caduceus | 2024 | BiMamba and MambaDNA blocks: bidirectional and reverse-complement equivariant by construction | RC equivariance and weight-tied bidirectionality both lowered masked-LM loss on the human genome | ([[10-Summaries/schiff-2024-caduceus\|Caduceus]]) |
| JanusDNA | 2025 | Janus modelling: two independent causal Mamba/MoE stacks read forward and backward, one masked FlexAttention layer fuses them | Every token is predicted from both sides, giving masked-model bidirectionality with autoregressive full-token training efficiency | ([[10-Summaries/duan-2025-janusdna\|JanusDNA]]) |
| GPN-MSA | 2025 | Small RoFormer masked LM conditioned on the 100-vertebrate whole-genome alignment; trained in ~3.5 h on four A100s | Outperforms the 2.5B Nucleotide Transformer and HyenaDNA on ClinVar missense classification | ([[10-Summaries/benegas-2025-gpn-msa\|GPN-MSA]]) |

### Variant- and genotype-aware inputs

| Model | Year | Input | Key result | Source |
|---|---|---|---|---|
| MutBERT | 2025 | Per-position allele-frequency distributions from 1000 Genomes instead of one-hot reference | Beats an identical reference-only twin (average MCC 66.36 vs 64.64 over 23 tasks) | ([[10-Summaries/long-2025-mutbert\|MutBERT]]) |
| BMFM-DNA | 2025 | BMFM-DNA-SNP: ModernBERT encoder on a genome where dbSNP variant sites are single symbols | Beats its reference-only twin on five of six fine-tuning tasks by about 0.5–1.5 points | ([[10-Summaries/li-2025-bmfm-dna\|BMFM-DNA]]) |
| BioFM | 2025 | Next-token prediction on 333B tokens from 50 phased 1000 Genomes individuals, with variant tokens | Last-layer embeddings need no per-task layer search | ([[10-Summaries/medvedev-2025-biofm\|BioFM]]) |
| DeepGene | 2025 | Pangenome graph: the HPRC 47-individual Minigraph, made acyclic, BPE-tokenised per node and cut into 128-token subgraphs | The only model in this cohort pretrained on a pangenome graph; best GUE average (67.79) at 118M parameters | ([[10-Summaries/zhang-2025-deepgene\|DeepGene]]) |
| Mendel | 2026 | Evo 2's architecture trained from scratch on GTEx personal genomes, loss only on diploid genotype tokens | Recovers held-out genotypes with 0.984 accuracy vs 0.311 for Evo 2, though most of that accuracy is the major allele | ([[10-Summaries/salman-2026-mendel\|Mendel]]) |
| DNT | 2026 | Continual pretraining of Nucleotide Transformer v3 (8M/100M) on phased 1000 Genomes sequences as one diploid token stream | Needs an auxiliary contrastive phase loss before the model actually uses phase tokens | ([[10-Summaries/leib-2026-dnt\|DNT]]) |
| UKBioBERT | 2026 | Continued DNABERT-2 MLM pretraining on sequences edited with ~13 million UK Biobank variants | Best gene-function clustering score among a broad panel of DNA LMs | ([[10-Summaries/liu-2026-ukbiobert\|UKBioBERT]]) |

### Fine-tunes, downstream uses and head-to-head tests

| Model | Year | How it uses a DNA LM | Key result | Source |
|---|---|---|---|---|
| SegmentNT | 2025 | Fine-tune of the pretrained Nucleotide Transformer, not a new pretrained model; segments 14 element classes | Random-init NT encoder reaches average MCC 0.16 vs 0.37 pretrained, and converges seven times slower | ([[10-Summaries/dealmeida-2025-segmentnt\|SegmentNT]]) |
| CpGPT | 2024 | Frozen Nucleotide Transformer v2-500M embeddings of the 2,001 bp around each CpG as the locus identifier | Beat HyenaDNA backbones in ablation; lets the model query CpGs never seen in training | ([[10-Summaries/delimacamillo-2024-cpgpt\|CpGPT]]) |
| Evo2HiC | 2025 | Distils Evo 2-7B layer-27 embeddings into a 3.6 M-parameter CNN with a SigLIP contrastive loss; trained on human sequence only | Keeps Evo 2's pairwise bin similarity (r = 0.63 human, 0.47 mouse vs 0.13/0.14 undistilled) at about 500× faster inference | ([[10-Summaries/fang-2025-evo2hic\|Evo2HiC]]) |
| EpiZoo | 2026 | Frozen DNABERT-2 encoder (SEAM), calibrated to learned cCRE identity embeddings, adds a sequence component to every scATAC token | That component is what carries over to species without coordinate correspondence | ([[10-Summaries/li-2026-epizoo\|EpiZoo]]) |
| ATGC-Gen | 2025 | Plain decoder and encoder transformers with cross-modal conditioning for sequence generation | Outperform discrete-diffusion and flow-matching baselines (promoter MSE 0.0192 vs 0.0219 for D3; enhancer FBD 0.5080 vs 1.0404 for Dirichlet flow matching) | ([[10-Summaries/su-2025-atgc-gen\|ATGC-Gen]]) |
| CREsted | 2026 | HyenaDNA and Nucleotide Transformer fine-tuned for cell-type-specific accessibility in mouse cortex | Both did worse than a fine-tuned Borzoi and a CREsted CNN trained from scratch | ([[10-Summaries/kempynck-2026-crested\|CREsted]]) |
| SUCCEED | 2026 | DNABERT-2, Nucleotide Transformer and HyenaDNA as frozen sequence encoders with a shared ATAC encoder | Supervised SUCCEED and Sei beat them on cell-type epigenome, ATAC denoising and Hi-C prediction, though the LMs were run on chunked 1–8 kb inputs | ([[10-Summaries/sun-2026-succeed\|SUCCEED]]) |

## Evidence and examples

- Evo 2 has 40B parameters and a 1 Mb context and was trained across all domains of life ([[10-Summaries/brixi-2026-evo2|Evo 2]]).
- GPN-MSA, an 86M alignment-based model, beats the 2.5B Nucleotide Transformer on ClinVar missense ([[10-Summaries/benegas-2025-gpn-msa|GPN-MSA]]).
- SegmentNT gives one of the clearest cases for DNA-LM pretraining: the same architecture with a randomly initialised NT encoder reaches average MCC 0.16 against 0.37 ([[10-Summaries/dealmeida-2025-segmentnt|SegmentNT]]).
- A 1.7–3.7 M-parameter k-mer BERT (GenomeBert) pretrained on GRCh37 gave driver-prediction features only marginally better than HyenaDNA or DeepSEA features (CV AUROC 83.25 vs 82.83 vs 82.34%), while the choice of downstream classifier moved AUROC by about 16 points ([[10-Summaries/zeng-2025-somatic-driver-lm|Zeng 2025]]).

## Contested points

- **Do DNA LMs beat supervised or simple baselines?** Used as frozen encoders, supervised SUCCEED and Sei beat DNABERT-2, Nucleotide Transformer and HyenaDNA ([[10-Summaries/sun-2026-succeed|SUCCEED]]); fine-tuned HyenaDNA and Nucleotide Transformer did worse than a small CNN and Borzoi in CREsted ([[10-Summaries/kempynck-2026-crested|CREsted]]); SpliceAI still beat the best transformer on splice sites ([[10-Summaries/fishman-2025-gena-lm|GENA-LM]]); a TF-IDF frequency baseline nearly matched DNA LMs on standard enhancer and promoter tasks ([[10-Summaries/sanabria-2024-grover|GROVER]]).
- **Frozen versus fine-tuned.** Frozen DNA-LM peak embeddings did not significantly beat randomly initialised ones in GFETM; only joint fine-tuning helped ([[10-Summaries/fan-2026-gfetm|GFETM]]). SegmentNT, in contrast, shows a clear pretraining gain once fine-tuned (average MCC 0.37 vs 0.16 from a random encoder) ([[10-Summaries/dealmeida-2025-segmentnt|SegmentNT]]).
- **Bigger is not always better.** NT-v2 250M beat the 2.5B Nucleotide Transformer ([[10-Summaries/dallatorre-2025-nucleotide-transformer|Nucleotide Transformer]]), and AIDO.DNA-300M scored ClinVar better than the 7B model ([[10-Summaries/ellington-2024-aido-dna|AIDO.DNA]]).
- **Benchmarks are reused, not rerun.** Many papers copy baseline numbers from earlier papers or leaderboards (e.g. [[10-Summaries/vishniakov-2025-gene42|Gene42]]; [[10-Summaries/kim-2026-dnachunker|DNAChunker]]; [[10-Summaries/fishman-2025-gena-lm|GENA-LM]]), and HyenaDNA's Nucleotide Transformer comparison used its own splits, which conflict with later reports ([[10-Summaries/nguyen-2023-hyenadna|HyenaDNA]]).
- **Representation from a DNA LM matters less than the downstream model.** In somatic driver prediction the classifier choice moved AUROC about 16 points while the feature source moved it under 1 point ([[10-Summaries/zeng-2025-somatic-driver-lm|Zeng 2025]]); this echoes the TF-IDF and CNN baselines above (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/sequence-to-function-model|Sequence-to-function model]] — Models trained on measured tracks rather than sequence alone.
> - `concept` [[30-Concepts/genomic-tokenization|Genomic tokenization]] — How DNA sequence is cut into model tokens.
> - `concept` [[30-Concepts/variant-effect-prediction|Variant effect prediction]] — Scoring variants, including zero-shot from DNA-LM likelihoods.
> - `concept` [[30-Concepts/single-cell-foundation-model|Single-cell foundation model]] — Pretrained models over single-cell profiles rather than sequence.
> - `concept` [[30-Concepts/convolutional-neural-network|Convolutional neural network]] — The small supervised baseline DNA LMs are often measured against.
> - `hub` [[40-Topics/sequence-models-and-foundation-models|Sequence models and foundation models]] — DNA LMs, sequence-to-function models and their single-cell uses.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — Pipelines, algorithms and tools across the wiki.

## All sources on this page

> [!info]- 40 summaries cited here
> - [[10-Summaries/aspidova-2026-moderngena|ModernGENA 2026]]
> - [[10-Summaries/ayanian-2025-strand|STRAND 2025]]
> - [[10-Summaries/benegas-2025-gpn-msa|GPN-MSA 2025]]
> - [[10-Summaries/boshar-2025-ntv3|NTv3 2025]]
> - [[10-Summaries/brixi-2026-evo2|Evo 2 2026]]
> - [[10-Summaries/chen-2023-genomicbert|genomicBERT 2023]]
> - [[10-Summaries/chen-2026-genart|GenART 2026]]
> - [[10-Summaries/dallatorre-2025-nucleotide-transformer|Nucleotide Transformer 2025]]
> - [[10-Summaries/dealmeida-2025-segmentnt|SegmentNT 2025]]
> - [[10-Summaries/delimacamillo-2024-cpgpt|CpGPT 2024]]
> - [[10-Summaries/ding-2025-nucel|NucEL 2025]]
> - [[10-Summaries/duan-2025-janusdna|JanusDNA 2025]]
> - [[10-Summaries/ellington-2024-aido-dna|AIDO.DNA 2024]]
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
> - [[10-Summaries/fang-2025-evo2hic|Evo2HiC 2025]]
> - [[10-Summaries/fishman-2025-gena-lm|GENA-LM 2025]]
> - [[10-Summaries/ji-2021-dnabert|DNABERT 2021]]
> - [[10-Summaries/kempynck-2026-crested|CREsted 2026]]
> - [[10-Summaries/kim-2026-dnachunker|DNAChunker 2026]]
> - [[10-Summaries/leib-2026-dnt|DNT 2026]]
> - [[10-Summaries/li-2025-bmfm-dna|BMFM-DNA 2025]]
> - [[10-Summaries/li-2026-epizoo|EpiZoo 2026]]
> - [[10-Summaries/li-2026-generator|GENERator 2026]]
> - [[10-Summaries/lin-2025-genos|Genos 2026]]
> - [[10-Summaries/liu-2026-ukbiobert|UKBioBERT 2026]]
> - [[10-Summaries/long-2025-mutbert|MutBERT 2025]]
> - [[10-Summaries/ma-2025-hybridna|HybriDNA 2025]]
> - [[10-Summaries/medvedev-2025-biofm|BioFM 2025]]
> - [[10-Summaries/nguyen-2023-hyenadna|HyenaDNA 2023]]
> - [[10-Summaries/salman-2026-mendel|Mendel 2026]]
> - [[10-Summaries/sanabria-2024-grover|GROVER 2024]]
> - [[10-Summaries/schiff-2024-caduceus|Caduceus 2024]]
> - [[10-Summaries/shen-2026-omnina|OmniNA 2026]]
> - [[10-Summaries/su-2025-atgc-gen|ATGC-Gen 2025]]
> - [[10-Summaries/sun-2026-succeed|SUCCEED 2026]]
> - [[10-Summaries/vishniakov-2025-gene42|Gene42 2025]]
> - [[10-Summaries/wang-2025-omnireg-gpt|OmniReg-GPT 2025]]
> - [[10-Summaries/zeng-2025-somatic-driver-lm|GenomeBert]]
> - [[10-Summaries/zhang-2025-deepgene|DeepGene 2025]]
> - [[10-Summaries/zhou-2023-dnabert-2|DNABERT-2 2023]]
