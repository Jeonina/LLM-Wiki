---
type: concept
title: Genomic tokenization
aliases: [DNA tokenization, DNA tokenizer, k-mer tokenization, BPE tokenization, single-nucleotide tokenization]
tags: [tokenization, dna-language-model, foundation-model, k-mer, BPE]
created: 2026-10-08
updated: 2026-10-12
---

# Genomic tokenization

> The rule that turns DNA (or a single-cell epigenome profile) into the discrete units a model reads — overlapping or non-overlapping k-mers, byte-pair-encoded "words", single nucleotides, learned variable-length chunks, or region and variant symbols ([[10-Summaries/ji-2021-dnabert|DNABERT]]; [[10-Summaries/zhou-2023-dnabert-2|DNABERT-2]]; [[10-Summaries/nguyen-2023-hyenadna|HyenaDNA]]; [[10-Summaries/kim-2026-dnachunker|DNAChunker]]).

> [!abstract] 한눈에
> DNA에는 단어 경계가 없어서 모든 DNA language model은 k-mer, BPE, 단일 염기, 학습된 chunk 가운데 하나를 골라야 하고, 이 선택이 context 길이와 염기 단위 해상도 사이의 균형을 정한다 ([[10-Summaries/fishman-2025-gena-lm|GENA-LM]]; [[10-Summaries/nguyen-2023-hyenadna|HyenaDNA]]). 어느 방식이 나은지는 학습 목표에 따라 달라서, BPE는 masked 학습에서는 6-mer보다 낫지만 next-token 예측에서는 무작위 수준에 머문다 ([[10-Summaries/zhou-2023-dnabert-2|DNABERT-2]]; [[10-Summaries/li-2026-generator|GENERator]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [서열 모델과 foundation model 교재](../60-Explainers/sequence-models-and-foundation-models.html)
<!-- /explainer-links -->

## Definition

DNA has no word boundaries, so every [[dna-language-model]] must choose one. The choice sets the trade-off between context length and resolution: single-nucleotide tokens keep base-level detail but cost the most per base, while BPE packs more sequence into the same number of tokens ([[10-Summaries/fishman-2025-gena-lm|GENA-LM]]; [[10-Summaries/nguyen-2023-hyenadna|HyenaDNA]]). For single-cell epigenome models the "token" is a region, a patch of regions or a CpG context instead ([[10-Summaries/leroy-2025-atacformer|Atacformer]]; [[10-Summaries/liu-2025-clm-access|CLM-access]]; [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]).

## Why it matters

- Point mutations and indels behave differently under each scheme: one base change alters every overlapping k-mer and can shift BPE or learned boundaries ([[10-Summaries/zhou-2023-dnabert-2|DNABERT-2]]; [[10-Summaries/chen-2026-genart|GenART]]), which matters for [[variant-effect-prediction]].
- Variant-aware and diploid tokenizers are the only way current DNA LMs see genotypes rather than a single reference ([[10-Summaries/medvedev-2025-biofm|BioFM]]; [[10-Summaries/leib-2026-dnt|DNT]]; [[10-Summaries/salman-2026-mendel|Mendel]]).

## Tokenization schemes

| Scheme | Models | Source |
|---|---|---|
| Overlapping k-mers | DNABERT (k = 3–6) | ([[10-Summaries/ji-2021-dnabert\|DNABERT]]) |
| Non-overlapping 6-mers | Nucleotide Transformer, GENERator; SegmentNT inherits NT's tokens | ([[10-Summaries/dallatorre-2025-nucleotide-transformer\|Nucleotide Transformer]]; [[10-Summaries/li-2026-generator\|GENERator]]; [[10-Summaries/dealmeida-2025-segmentnt\|SegmentNT]]) |
| BPE | DNABERT-2, GROVER, GENA-LM, ModernGENA, DeepGene; OmniNA shares one BPE vocabulary between DNA and English | ([[10-Summaries/zhou-2023-dnabert-2\|DNABERT-2]]; [[10-Summaries/sanabria-2024-grover\|GROVER]]; [[10-Summaries/fishman-2025-gena-lm\|GENA-LM]]; [[10-Summaries/aspidova-2026-moderngena\|ModernGENA]]; [[10-Summaries/zhang-2025-deepgene\|DeepGene]]; [[10-Summaries/shen-2026-omnina\|OmniNA]]) |
| Unigram | genomicBERT | ([[10-Summaries/chen-2023-genomicbert\|genomicBERT]]) |
| Single nucleotide | HyenaDNA, Caduceus, AIDO.DNA, Gene42, HybriDNA, JanusDNA, NucEL; NTv3 keeps single bases by down-sampling inside a U-Net | ([[10-Summaries/nguyen-2023-hyenadna\|HyenaDNA]]; [[10-Summaries/schiff-2024-caduceus\|Caduceus]]; [[10-Summaries/ellington-2024-aido-dna\|AIDO.DNA]]; [[10-Summaries/vishniakov-2025-gene42\|Gene42]]; [[10-Summaries/ma-2025-hybridna\|HybriDNA]]; [[10-Summaries/duan-2025-janusdna\|JanusDNA]]; [[10-Summaries/ding-2025-nucel\|NucEL]]; [[10-Summaries/boshar-2025-ntv3\|NTv3]]) |
| Learned or adaptive | DNAChunker, GenART | ([[10-Summaries/kim-2026-dnachunker\|DNAChunker]]; [[10-Summaries/chen-2026-genart\|GenART]]) |
| Variant and genotype symbols | BioToken, BMFM-DNA, DNT, Mendel (IUPAC codes), MutBERT (allele-frequency vectors) | ([[10-Summaries/medvedev-2025-biofm\|BioFM]]; [[10-Summaries/li-2025-bmfm-dna\|BMFM-DNA]]; [[10-Summaries/leib-2026-dnt\|DNT]]; [[10-Summaries/salman-2026-mendel\|Mendel]]; [[10-Summaries/long-2025-mutbert\|MutBERT]]) |
| Single-cell epigenome tokens | Consensus regions, cCRE patches, non-zero peaks, CpG-centred 6-mers | ([[10-Summaries/leroy-2025-atacformer\|Atacformer]]; [[10-Summaries/liu-2025-clm-access\|CLM-access]]; [[10-Summaries/wu-2025-epifoundation\|EpiFoundation]]; [[10-Summaries/liang-2025-scdnam-gpt\|scDNAm-GPT]]) |

## Models in this wiki

Thirty models, grouped by scheme. Benchmark numbers are under Evidence and examples.

| Model | Year | Scheme | Design choice | Source |
|---|---|---|---|---|
| DNABERT | 2021 | Overlapping k-mers | k = 3–6, vocabulary 4^k + 5; must mask contiguous k-token spans because a single overlapping k-mer can be read off its neighbours | ([[10-Summaries/ji-2021-dnabert\|DNABERT]]) |
| Nucleotide Transformer | 2025 | Non-overlapping 6-mers | Single-base fallback tokens (4,104-token vocabulary); notes that BPE would make nucleotide-level heads such as splice-site calling harder to implement | ([[10-Summaries/dallatorre-2025-nucleotide-transformer\|Nucleotide Transformer]]) |
| SegmentNT | 2025 | Non-overlapping 6-mers (from NT) | Upsamples NT's 6-mer token embeddings to per-nucleotide predictions with a U-Net head | ([[10-Summaries/dealmeida-2025-segmentnt\|SegmentNT]]) |
| GENERator | 2026 | Non-overlapping 6-mers | 6-mer chosen by a controlled sweep against 1- to 8-mers and BPE | ([[10-Summaries/li-2026-generator\|GENERator]]) |
| DNABERT-2 | 2023 | BPE | Vocabulary 4,096 chosen from a 2^8–2^15 sweep; argues overlapping k-mers leak masked tokens and non-overlapping k-mers make one-base shifts change the whole token string | ([[10-Summaries/zhou-2023-dnabert-2\|DNABERT-2]]) |
| GROVER | 2024 | BPE | Vocabulary (600 cycles, 601 tokens, mean length 4.07 nt) selected by fine-tuned next-k-mer prediction rather than biological benchmarks | ([[10-Summaries/sanabria-2024-grover\|GROVER]]) |
| GENA-LM | 2025 | BPE | 32,000-token vocabulary gives DNA tokens of 1–64 bp (median 9 bp), so 512 non-overlapping tokens cover about 4.5 kb against 512 bp for 512 overlapping 6-mers, at the cost of token-level rather than base-level resolution | ([[10-Summaries/fishman-2025-gena-lm\|GENA-LM]]) |
| DeepGene | 2025 | BPE on a variation graph | BPE inside variation-graph nodes, each token given a position derived from the DAG, so a standard RoPE transformer consumes branching sequence without a graph neural network; the authors note the BPE vocabulary still comes from reference-genome statistics | ([[10-Summaries/zhang-2025-deepgene\|DeepGene]]) |
| ModernGENA | 2026 | BPE | 32k BPE vocabulary | ([[10-Summaries/aspidova-2026-moderngena\|ModernGENA]]) |
| OmniNA | 2026 | BPE (DNA + text) | A single 32,001-token SentencePiece BPE vocabulary shared between nucleotides and English words, trained jointly on DNA and WikiText-103 | ([[10-Summaries/shen-2026-omnina\|OmniNA]]) |
| genomicBERT | 2023 | Unigram | SentencePiece Unigram vocabulary of 4,096 tokens (max length 16, mostly 5–9 nt), giving about n/5 tokens per sequence and roughly 10x fewer tokens than 9-mers on a pre-miRNA set | ([[10-Summaries/chen-2023-genomicbert\|genomicBERT]]) |
| HyenaDNA | 2023 | Single nucleotide | Single-nucleotide tokens | ([[10-Summaries/nguyen-2023-hyenadna\|HyenaDNA]]) |
| AIDO.DNA | 2024 | Single nucleotide | Character-level A/T/C/G/N tokens, on the grounds that k-mer and BPE "words" dilute single-nucleotide pathogenic effects and local grammars such as codons | ([[10-Summaries/ellington-2024-aido-dna\|AIDO.DNA]]) |
| Caduceus | 2024 | Single nucleotide | Cites k-mer instability under small input shifts as the reason | ([[10-Summaries/schiff-2024-caduceus\|Caduceus]]) |
| Gene42 | 2025 | Single nucleotide | Argues SNP-level tasks need base resolution; dense attention still reaches 192 kb under that choice | ([[10-Summaries/vishniakov-2025-gene42\|Gene42]]) |
| HybriDNA | 2025 | Single nucleotide | Argues the Mamba2 blocks make single-nucleotide tokens affordable at long context, where earlier encoder models had to use k-mers or BPE for cost reasons | ([[10-Summaries/ma-2025-hybridna\|HybriDNA]]) |
| JanusDNA | 2025 | Single nucleotide | Keeps SNP-level resolution explicitly, treating k-mer tokenization as a resolution/context trade-off it avoids | ([[10-Summaries/duan-2025-janusdna\|JanusDNA]]) |
| NTv3 | 2025 | Single nucleotide | Compresses 1 bp to 128 bp through seven convolutional down-sampling blocks before the transformer and restores base resolution through a mirrored decoder, making single-nucleotide tokens affordable at megabase scale | ([[10-Summaries/boshar-2025-ntv3\|NTv3]]) |
| NucEL | 2025 | Single nucleotide | Single-nucleotide tokens, chosen over 6-mer and BPE in an internal comparison | ([[10-Summaries/ding-2025-nucel\|NucEL]]) |
| DNAChunker | 2026 | Learned chunks | Learned variable-length chunks | ([[10-Summaries/kim-2026-dnachunker\|DNAChunker]]) |
| GenART | 2026 | Adaptive | Adaptive tokenizer whose boundaries move with the input | ([[10-Summaries/chen-2026-genart\|GenART]]) |
| BioFM | 2025 | Variant symbols | BioToken keeps single nucleotides but adds variant tokens for alternate alleles and inline transcript/exon/CDS boundary tokens | ([[10-Summaries/medvedev-2025-biofm\|BioFM]]) |
| BMFM-DNA | 2025 | Variant symbols + BPE | A BPE vocabulary trained on the variant-encoded genome shares 84.3% of tokens with the reference vocabulary; 6.8% of its tokens contain a variant symbol, with A/G and C/T transitions dominating | ([[10-Summaries/li-2025-bmfm-dna\|BMFM-DNA]]) |
| MutBERT | 2025 | Allele-frequency vectors | Single-nucleotide tokens projected linearly from a 9 x L probability matrix; argues BPE suits TF/histone tasks while 6-mer tokens suit splice sites | ([[10-Summaries/long-2025-mutbert\|MutBERT]]) |
| DNT | 2026 | Diploid genotype symbols | Unphased, ordered-phase and marker-phase diploid tokenizers with atomic allele-pair symbols and gap-padded indel spans, expanding the NTv3 vocabulary from 11 to 55 tokens | ([[10-Summaries/leib-2026-dnt\|DNT]]) |
| Mendel | 2026 | IUPAC codes | Writes each donor's diploid SNV genotype as a single unordered IUPAC ambiguity code between ^ and & markers, which needs no vocabulary change but discards phase | ([[10-Summaries/salman-2026-mendel\|Mendel]]) |
| Atacformer | 2025 | Consensus regions | Tokenises a cell by overlapping its fragments or peaks with a fixed 890,704-region consensus vocabulary; no positional encoding or DNA sequence, so the cell is an unordered bag of regions | ([[10-Summaries/leroy-2025-atacformer\|Atacformer]]) |
| CLM-access | 2025 | cCRE patches | Splits about 1.15M position-ordered cCREs into 2,000 fixed patches, each one token | ([[10-Summaries/liu-2025-clm-access\|CLM-access]]) |
| EpiFoundation | 2025 | Non-zero peaks | Inputs only a cell's non-zero peaks (up to 12,000) as peak-ID plus chromosome embeddings | ([[10-Summaries/wu-2025-epifoundation\|EpiFoundation]]) |
| scDNAm-GPT | 2025 | CpG-centred 6-mers | Each covered CpG becomes a CpG-centred 6-mer ('XXC(M)GXX'); methylated and unmethylated token embeddings are mixed by the methylation rate so bulk data can also be input; 6-mers gave the most flanking DNA per unit memory | ([[10-Summaries/liang-2025-scdnam-gpt\|scDNAm-GPT]]) |

## Evidence and examples

**Controlled comparisons of schemes**

- BPE beat 6-mers on 21 of 28 GUE datasets in DNABERT-2's controlled ablation ([[10-Summaries/zhou-2023-dnabert-2|DNABERT-2]]).
- Replacing HyenaDNA's single-nucleotide tokens with a 6-mer tokeniser in the same architecture cut GenomicBenchmarks accuracy on most datasets by up to 10 points ([[10-Summaries/nguyen-2023-hyenadna|HyenaDNA]]).
- Inside NucEL, single-nucleotide tokens outperformed 6-mer and BPE tokenization across training epochs on human GUE tasks ([[10-Summaries/ding-2025-nucel|NucEL]]).
- GENERator's sweep of 1- to 8-mers and BPE vocabularies of 512–8,192 found 6-mer best for next-token prediction, with every BPE variant near the 0.25 random baseline because BPE's nested vocabulary penalises valid prefixes ([[10-Summaries/li-2026-generator|GENERator]]).
- For next-6-mer prediction GROVER reached 2% accuracy vs 0.6% for DNABERT-2 and ≤0.4% for fixed-k-mer models including NT ([[10-Summaries/sanabria-2024-grover|GROVER]]).
- GenART's adaptive tokenizer beat single-nucleotide tokenization by 3.27% on average and 9.35% on histone marks in a controlled ablation; sharp-peak marks preferred dense, clustered boundaries and broad-domain marks sparse ones ([[10-Summaries/chen-2026-genart|GenART]]).
- DNAChunker's learned chunks split JASPAR TF motifs into 1.22 tokens on average vs 2.47 for BPE and 2.32 for fixed 6-mers, and are more stable than BPE under ClinVar indels and GIAB structural variants ([[10-Summaries/kim-2026-dnachunker|DNAChunker]]; see [[structural-variants]]).

**Resolution-limited tasks**

- ModernGENA trails NTv2 on splice sites (acceptor MCC 86.4 vs 95.0), which its authors attribute to 32k BPE tokenization being less suited than fine-grained tokens to short, precisely placed motifs ([[10-Summaries/aspidova-2026-moderngena|ModernGENA]]).
- SegmentNT shows that Enformer's 128 bp and Borzoi's 32 bp binning is what prevents those encoders from calling splice sites and poly(A) signals ([[10-Summaries/dealmeida-2025-segmentnt|SegmentNT]]).

**Variant-aware tokens**

- A matched-compute nucleotide-only model (ACGT-265M) does clearly worse than BioFM on variant benchmarks ([[10-Summaries/medvedev-2025-biofm|BioFM]]).

**Single-cell epigenome tokens**

- In CLM-access, binarised per-peak BCE raised pretraining ARI from about 0.003 (summed, patch-level) to 0.25, and masking patch tokens as well as values collapsed training ([[10-Summaries/liu-2025-clm-access|CLM-access]]).
- Removing EpiFoundation's chromosome embedding lowered kidney NMI from 0.568 to 0.435 ([[10-Summaries/wu-2025-epifoundation|EpiFoundation]]).

## Contested points

- **BPE wins under masking but fails under next-token prediction.** BPE beat 6-mers on 21 of 28 GUE datasets in DNABERT-2's controlled test ([[10-Summaries/zhou-2023-dnabert-2|DNABERT-2]]), yet GENERator found every BPE vocabulary near the random baseline for next-token prediction and 6-mers best — the opposite of BPE's reported advantage under masked objectives ([[10-Summaries/li-2026-generator|GENERator]]).
- **Single nucleotides versus k-mers.** Swapping to 6-mers cut HyenaDNA accuracy by up to 10 points, and single nucleotides beat 6-mer and BPE inside NucEL ([[10-Summaries/nguyen-2023-hyenadna|HyenaDNA]]; [[10-Summaries/ding-2025-nucel|NucEL]]); ModernGENA's authors blame 32k BPE for weak splice-site results ([[10-Summaries/aspidova-2026-moderngena|ModernGENA]]).
- **Adaptive tokenizers and variants.** GenART reports near-random zero-shot variant scoring because a mutation shifts its chunk boundaries ([[10-Summaries/chen-2026-genart|GenART]]), while DNAChunker reports its chunks are more stable than BPE under indels and structural variants ([[10-Summaries/kim-2026-dnachunker|DNAChunker]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/dna-language-model|DNA language model]] — A model pretrained on DNA sequence alone; every one must pick a tokenizer.
> - `concept` [[30-Concepts/variant-effect-prediction|Variant effect prediction]] — Scoring reference versus alternative alleles, which tokenization can blur or sharpen.
> - `concept` [[30-Concepts/single-cell-foundation-model|Single-cell foundation model]] — Pretrained models on single-cell epigenome profiles, where regions or CpGs are the tokens.
> - `concept` [[30-Concepts/structural-variants|Structural variants]] — Large rearrangements used to test tokenizer stability.
> - `hub` [[40-Topics/sequence-models-and-foundation-models|Sequence models and foundation models]] — Models that learn from DNA sequence or single-cell epigenome corpora.

## All sources on this page

> [!info]- 30 summaries cited here
> - [[10-Summaries/aspidova-2026-moderngena|ModernGENA 2026]]
> - [[10-Summaries/boshar-2025-ntv3|NTv3 2025]]
> - [[10-Summaries/chen-2023-genomicbert|genomicBERT 2023]]
> - [[10-Summaries/chen-2026-genart|GenART 2026]]
> - [[10-Summaries/dallatorre-2025-nucleotide-transformer|Nucleotide Transformer 2025]]
> - [[10-Summaries/dealmeida-2025-segmentnt|SegmentNT 2025]]
> - [[10-Summaries/ding-2025-nucel|NucEL 2025]]
> - [[10-Summaries/duan-2025-janusdna|JanusDNA 2025]]
> - [[10-Summaries/ellington-2024-aido-dna|AIDO.DNA 2024]]
> - [[10-Summaries/fishman-2025-gena-lm|GENA-LM 2025]]
> - [[10-Summaries/ji-2021-dnabert|DNABERT 2021]]
> - [[10-Summaries/kim-2026-dnachunker|DNAChunker 2026]]
> - [[10-Summaries/leib-2026-dnt|DNT 2026]]
> - [[10-Summaries/leroy-2025-atacformer|Atacformer 2025]]
> - [[10-Summaries/li-2025-bmfm-dna|BMFM-DNA 2025]]
> - [[10-Summaries/li-2026-generator|GENERator 2026]]
> - [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT 2025]]
> - [[10-Summaries/liu-2025-clm-access|CLM-access 2025]]
> - [[10-Summaries/long-2025-mutbert|MutBERT 2025]]
> - [[10-Summaries/ma-2025-hybridna|HybriDNA 2025]]
> - [[10-Summaries/medvedev-2025-biofm|BioFM 2025]]
> - [[10-Summaries/nguyen-2023-hyenadna|HyenaDNA 2023]]
> - [[10-Summaries/salman-2026-mendel|Mendel 2026]]
> - [[10-Summaries/sanabria-2024-grover|GROVER 2024]]
> - [[10-Summaries/schiff-2024-caduceus|Caduceus 2024]]
> - [[10-Summaries/shen-2026-omnina|OmniNA 2026]]
> - [[10-Summaries/vishniakov-2025-gene42|Gene42 2025]]
> - [[10-Summaries/wu-2025-epifoundation|EpiFoundation 2025]]
> - [[10-Summaries/zhang-2025-deepgene|DeepGene 2025]]
> - [[10-Summaries/zhou-2023-dnabert-2|DNABERT-2 2023]]
