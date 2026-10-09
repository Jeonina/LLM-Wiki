---
type: concept
title: Genomic tokenization
aliases: [DNA tokenization, DNA tokenizer, k-mer tokenization, BPE tokenization, single-nucleotide tokenization]
tags: [tokenization, dna-language-model, foundation-model, k-mer, BPE]
created: 2026-10-08
updated: 2026-10-08
---

# Genomic tokenization

> The rule that turns DNA (or a single-cell epigenome profile) into the discrete units a model reads — overlapping or non-overlapping k-mers, byte-pair-encoded "words", single nucleotides, learned variable-length chunks, or region and variant symbols ([[10-Summaries/ji-2021-dnabert]]; [[10-Summaries/zhou-2023-dnabert-2]]; [[10-Summaries/nguyen-2023-hyenadna]]; [[10-Summaries/kim-2026-dnachunker]]).

## Definition

DNA has no word boundaries, so every [[dna-language-model]] must choose one. The choice sets the trade-off between context length and resolution: single-nucleotide tokens keep base-level detail but cost the most per base, while BPE packs more sequence into the same number of tokens ([[10-Summaries/fishman-2025-gena-lm]]; [[10-Summaries/nguyen-2023-hyenadna]]). For single-cell epigenome models the "token" is a region, a patch of regions or a CpG context instead ([[10-Summaries/leroy-2025-atacformer]]; [[10-Summaries/liu-2025-clm-access]]; [[10-Summaries/liang-2025-scdnam-gpt]]).

## Why it matters

- Point mutations and indels behave differently under each scheme: one base change alters every overlapping k-mer and can shift BPE or learned boundaries ([[10-Summaries/zhou-2023-dnabert-2]]; [[10-Summaries/chen-2026-genart]]), which matters for [[variant-effect-prediction]].
- Variant-aware and diploid tokenizers are the only way current DNA LMs see genotypes rather than a single reference ([[10-Summaries/medvedev-2025-biofm]]; [[10-Summaries/leib-2026-dnt]]; [[10-Summaries/salman-2026-mendel]]).

## Variants and refinements

- *Overlapping k-mers:* DNABERT (k = 3–6) ([[10-Summaries/ji-2021-dnabert]]).
- *Non-overlapping 6-mers:* Nucleotide Transformer, GENERator ([[10-Summaries/dallatorre-2025-nucleotide-transformer]]; [[10-Summaries/li-2026-generator]]).
- *BPE:* DNABERT-2, GROVER, GENA-LM, ModernGENA; OmniNA shares one BPE vocabulary between DNA and English ([[10-Summaries/zhou-2023-dnabert-2]]; [[10-Summaries/sanabria-2024-grover]]; [[10-Summaries/fishman-2025-gena-lm]]; [[10-Summaries/aspidova-2026-moderngena]]; [[10-Summaries/shen-2026-omnina]]).
- *Unigram:* genomicBERT ([[10-Summaries/chen-2023-genomicbert]]).
- *Single nucleotide:* HyenaDNA, Caduceus, AIDO.DNA, Gene42, HybriDNA, JanusDNA, NucEL; NTv3 keeps single bases by down-sampling inside a U-Net ([[10-Summaries/boshar-2025-ntv3]]).
- *Learned or adaptive:* DNAChunker, GenART ([[10-Summaries/kim-2026-dnachunker]]; [[10-Summaries/chen-2026-genart]]).
- *Variant and genotype symbols:* BioToken, BMFM-DNA, DNT, Mendel (IUPAC codes), MutBERT (allele-frequency vectors) ([[10-Summaries/medvedev-2025-biofm]]; [[10-Summaries/li-2025-bmfm-dna]]; [[10-Summaries/leib-2026-dnt]]; [[10-Summaries/salman-2026-mendel]]; [[10-Summaries/long-2025-mutbert]]).
- *Single-cell epigenome tokens:* consensus regions, cCRE patches, non-zero peaks, CpG-centred 6-mers ([[10-Summaries/leroy-2025-atacformer]]; [[10-Summaries/liu-2025-clm-access]]; [[10-Summaries/wu-2025-epifoundation]]; [[10-Summaries/liang-2025-scdnam-gpt]]).

**Models in this wiki** (30, by year):

- **DNABERT** (2021) — DNABERT tokenises DNA into overlapping k-mers (k = 3–6, vocabulary 4^k + 5) and must mask contiguous k-token spans because a single overlapping k-mer can be read off its neighbours ([[10-Summaries/ji-2021-dnabert]])
- **DNABERT-2** (2023) — DNABERT-2 replaces k-mers with BPE (vocabulary 4,096 chosen from a 2^8–2^15 sweep), arguing overlapping k-mers leak masked tokens and non-overlapping k-mers make one-base shifts change the whole token string; BPE beat 6-mers on 21 of 28 GUE datasets in a controlled ablation ([[10-Summaries/zhou-2023-dnabert-2]])
- **HyenaDNA** (2023) — HyenaDNA uses single-nucleotide tokens; replacing them with a 6-mer tokeniser in the same architecture cut GenomicBenchmarks accuracy on most datasets by up to 10 points ([[10-Summaries/nguyen-2023-hyenadna]])
- **genomicBERT** (2023) — genomicBERT replaces k-mer/BPE with a SentencePiece Unigram vocabulary of 4,096 tokens (max length 16, mostly 5–9 nt), giving about n/5 tokens per sequence and roughly 10x fewer tokens than 9-mers on a pre-miRNA set ([[10-Summaries/chen-2023-genomicbert]]).
- **AIDO.DNA** (2024) — AIDO.DNA uses character-level A/T/C/G/N tokens on the grounds that k-mer and BPE "words" dilute single-nucleotide pathogenic effects and local grammars such as codons ([[10-Summaries/ellington-2024-aido-dna]]).
- **Caduceus** (2024) — Caduceus uses single-nucleotide tokens, citing k-mer instability under small input shifts as the reason ([[10-Summaries/schiff-2024-caduceus]])
- **GROVER** (2024) — GROVER selects its BPE vocabulary (600 cycles, 601 tokens, mean length 4.07 nt) by fine-tuned next-k-mer prediction rather than biological benchmarks; for next-6-mers it reached 2% accuracy vs 0.6% for DNABERT-2 and ≤0.4% for fixed-k-mer models including NT ([[10-Summaries/sanabria-2024-grover]])
- **Atacformer** (2025) — Atacformer tokenises a cell by overlapping its fragments or peaks with a fixed 890,704-region consensus vocabulary and uses no positional encoding or DNA sequence; it treats the cell as an unordered bag of regions ([[10-Summaries/leroy-2025-atacformer]]).
- **BMFM-DNA** (2025) — A BPE vocabulary trained on BMFM-DNA's variant-encoded genome shares 84.3% of tokens with the reference vocabulary, and 6.8% of its tokens contain a variant symbol, with A/G and C/T transitions dominating ([[10-Summaries/li-2025-bmfm-dna]]).
- **BioFM** (2025) — BioToken keeps single nucleotides but adds variant tokens for alternate alleles and inline transcript/exon/CDS boundary tokens; a matched-compute nucleotide-only model (ACGT-265M) does clearly worse on variant benchmarks ([[10-Summaries/medvedev-2025-biofm]]).
- **CLM-access** (2025) — CLM-access splits about 1.15M position-ordered cCREs into 2,000 fixed patches, each one token; binarised per-peak BCE raised pretraining ARI from about 0.003 (summed, patch-level) to 0.25, and masking patch tokens as well as values collapsed training ([[10-Summaries/liu-2025-clm-access]]).
- **DeepGene** (2025) — DeepGene applies BPE inside variation-graph nodes and gives each token a position derived from the DAG, letting a standard RoPE transformer consume branching sequence without a graph neural network; the authors note the BPE vocabulary still comes from reference-genome statistics ([[10-Summaries/zhang-2025-deepgene]]).
- **EpiFoundation** (2025) — EpiFoundation inputs only a cell's non-zero peaks (up to 12,000) as peak-ID plus chromosome embeddings; removing the chromosome embedding lowered kidney NMI from 0.568 to 0.435 ([[10-Summaries/wu-2025-epifoundation]]).
- **GENA-LM** (2025) — Byte-pair encoding with a 32,000-token vocabulary gives DNA tokens of 1–64 bp (median 9 bp), so 512 non-overlapping tokens cover about 4.5 kb against 512 bp for 512 overlapping 6-mers, at the cost of token-level rather than base-level resolution ([[10-Summaries/fishman-2025-gena-lm]]).
- **Gene42** (2025) — Gene42 uses single-nucleotide character tokens, arguing that SNP-level tasks need base resolution, and shows dense attention can still reach 192 kb under that choice ([[10-Summaries/vishniakov-2025-gene42]]).
- **HybriDNA** (2025) — HybriDNA keeps single-nucleotide tokens and argues the Mamba2 blocks make them affordable at long context, where earlier encoder models had to use k-mers or BPE for cost reasons ([[10-Summaries/ma-2025-hybridna]]).
- **JanusDNA** (2025) — JanusDNA uses single-nucleotide tokens explicitly to keep SNP-level resolution, treating k-mer tokenization as a resolution/context trade-off it avoids ([[10-Summaries/duan-2025-janusdna]]).
- **MutBERT** (2025) — MutBERT uses single-nucleotide tokens projected linearly from a 9 x L probability matrix, and argues BPE suits TF/histone tasks while 6-mer tokens suit splice sites ([[10-Summaries/long-2025-mutbert]]).
- **NTv3** (2025) — NTv3 makes single-nucleotide tokenization affordable at megabase scale by compressing 1 bp to 128 bp through seven convolutional down-sampling blocks before the transformer and restoring base resolution through a mirrored decoder ([[10-Summaries/boshar-2025-ntv3]]).
- **NucEL** (2025) — Inside NucEL, single-nucleotide tokens outperformed 6-mer and BPE tokenization across training epochs on human GUE tasks ([[10-Summaries/ding-2025-nucel]]).
- **Nucleotide Transformer** (2025) — Nucleotide Transformer uses non-overlapping 6-mers with single-base fallback tokens (4,104-token vocabulary) and notes that BPE would make nucleotide-level heads such as splice-site calling harder to implement ([[10-Summaries/dallatorre-2025-nucleotide-transformer]])
- **SegmentNT** (2025) — SegmentNT upsamples NT's 6-mer token embeddings to per-nucleotide predictions with a U-Net head, and shows that Enformer's 128 bp and Borzoi's 32 bp binning is what prevents those encoders from calling splice sites and poly(A) signals ([[10-Summaries/dealmeida-2025-segmentnt]]).
- **scDNAm-GPT** (2025) — scDNAm-GPT tokenises each covered CpG as a CpG-centred 6-mer ('XXC(M)GXX'), mixing methylated and unmethylated token embeddings by the methylation rate so bulk data can also be input; 6-mers gave the most flanking DNA per unit memory ([[10-Summaries/liang-2025-scdnam-gpt]]).
- **DNAChunker** (2026) — DNAChunker's learned chunks split JASPAR TF motifs into 1.22 tokens on average vs 2.47 for BPE and 2.32 for fixed 6-mers, and are more stable than BPE under ClinVar indels and GIAB structural variants ([[10-Summaries/kim-2026-dnachunker]]).
- **DNT** (2026) — DNT defines unphased, ordered-phase and marker-phase diploid tokenizers with atomic allele-pair symbols and gap-padded indel spans, expanding the NTv3 vocabulary from 11 to 55 tokens ([[10-Summaries/leib-2026-dnt]]).
- **GENERator** (2026) — A controlled sweep of 1- to 8-mers and BPE vocabularies 512–8,192 found 6-mer best for next-token prediction, with every BPE variant near the 0.25 random baseline because BPE's nested vocabulary penalises valid prefixes — the opposite of BPE's reported advantage under masked objectives ([[10-Summaries/li-2026-generator]]).
- **GenART** (2026) — In a controlled ablation, GenART's adaptive tokenizer beat single-nucleotide tokenization by 3.27% on average and 9.35% on histone marks; sharp-peak marks preferred dense, clustered boundaries and broad-domain marks sparse ones ([[10-Summaries/chen-2026-genart]]).
- **Mendel** (2026) — Mendel writes each donor's diploid SNV genotype as a single unordered IUPAC ambiguity code between ^ and & markers, which needs no vocabulary change but discards phase ([[10-Summaries/salman-2026-mendel]]).
- **ModernGENA** (2026) — ModernGENA trails NTv2 on splice sites (acceptor MCC 86.4 vs 95.0), which its authors attribute to 32k BPE tokenization being less suited than fine-grained tokens to short, precisely placed motifs ([[10-Summaries/aspidova-2026-moderngena]]).
- **OmniNA** (2026) — OmniNA shares a single 32,001-token SentencePiece BPE vocabulary between nucleotides and English words, trained jointly on DNA and WikiText-103 ([[10-Summaries/shen-2026-omnina]]).

## Contested points

- **BPE wins under masking but fails under next-token prediction.** BPE beat 6-mers on 21 of 28 GUE datasets in DNABERT-2's controlled test ([[10-Summaries/zhou-2023-dnabert-2]]), yet GENERator found every BPE vocabulary near the random baseline for next-token prediction and 6-mers best ([[10-Summaries/li-2026-generator]]).
- **Single nucleotides versus k-mers.** Swapping to 6-mers cut HyenaDNA accuracy by up to 10 points, and single nucleotides beat 6-mer and BPE inside NucEL ([[10-Summaries/nguyen-2023-hyenadna]]; [[10-Summaries/ding-2025-nucel]]); ModernGENA's authors blame 32k BPE for weak splice-site results ([[10-Summaries/aspidova-2026-moderngena]]).
- **Adaptive tokenizers and variants.** GenART reports near-random zero-shot variant scoring because a mutation shifts its chunk boundaries ([[10-Summaries/chen-2026-genart]]), while DNAChunker reports its chunks are more stable than BPE under indels and structural variants ([[10-Summaries/kim-2026-dnachunker]]).

## Related

- [[dna-language-model]] · [[variant-effect-prediction]] · [[single-cell-foundation-model]] · [[structural-variants]]
- [[40-Topics/sequence-models-and-foundation-models]]
