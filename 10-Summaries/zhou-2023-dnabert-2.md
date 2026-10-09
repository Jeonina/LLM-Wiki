---
type: summary
title: "Zhou et al. 2023 — DNABERT-2: Efficient Foundation Model and Benchmark for Multi-Species Genomes"
source: "[[00-Sources/papers/DNABERT-2- Efficient Foundation Model and Benchmark For Multi-Species Genome.pdf]]"
source_quality: full
source_sha256: "49300acee3e4afd44bebc3de9893c3bc310d331bd4805374e0952fdfbf366f06"
source_kind: paper
author: "Zhihan Zhou, Yanrong Ji, Weijian Li, Pratik Dutta, Ramana V. Davuluri, Han Liu (corresponding author not marked)"
published: 2023-06-26
ingested: 2026-10-08
doi: "10.48550/arXiv.2306.15006"
journal: "ICLR 2024 (conference paper; source is arXiv 2306.15006v2, 18 Mar 2024)"
tags: [DNABERT-2, dna-language-model, BPE, byte-pair-encoding, tokenization, ALiBi, FlashAttention, LoRA, multi-species-pretraining, GUE-benchmark, masked-language-modeling, Nucleotide-Transformer, HyenaDNA, efficiency]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[transcription-factor-motif]]", "[[chip-seq]]", "[[histone-modifications]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Zhou et al. (2023) — *DNABERT-2: Efficient Foundation Model and Benchmark for Multi-Species Genomes* — arXiv 2306.15006; published as a conference paper at *ICLR 2024*. [DOI](https://doi.org/10.48550/arXiv.2306.15006)

# Zhou 2023 — DNABERT-2

> DNABERT-2 argues that k-mer tokenisation is the main obstacle to scaling DNA language models. Overlapping k-mers leak masked tokens through their neighbours and leave the sequence almost as long as the input; non-overlapping k-mers (Nucleotide Transformer) shorten the sequence but make a one-base shift produce a completely different token string. The authors replace both with Byte Pair Encoding (BPE, vocabulary 4,096) learned on a 135-species, 32.49B-base corpus, and update the BERT encoder with ALiBi positional biases (no fixed length limit), FlashAttention and GEGLU. They also release GUE, a 36-dataset benchmark across 9 tasks and 4 species groups (human, mouse, yeast, virus, plus fungi in GUE+), with datasets tuned to moderate difficulty. The 117M-parameter DNABERT-2 roughly matches the 2.5B-parameter NT-2500M-multi on GUE (66.80 vs 66.93 average) with 21× fewer parameters and about 92× less pre-training GPU time.

## Key claims

- **k-mer tokenisation is inefficient in two different ways.** Overlapping k-mers make masked-token prediction partly trivial: with unmasked neighbours on both sides a masked token is "entirely leaked", which is why DNABERT had to mask k-token spans. Non-overlapping k-mers cut length by k but are sample-inefficient because near-identical inputs get very different token strings (Fig. 1 example).
- **BPE fixes both.** BPE tokens do not overlap, shorten sequences by about 5×, and give stable tokenisations. Because tokens vary in length, masked prediction becomes a T5-like span-prediction task.
- **Vocabulary size trades compute against accuracy.** Over vocabularies 2⁸–2¹⁵, larger vocabularies gave longer tokens and fewer FLOPs, but GUE performance did not rise monotonically. 2¹² = 4,096 was chosen as the best balance (Fig. 3; plotted values not readable in the PDF text).
- **Parity with NT-2500M-multi at a fraction of the cost.** GUE average (28 datasets): DNABERT-2 66.80 (117M parameters, FLOPs 1.00 relative) vs NT-2500M-multi 66.93 (2,537M, 19.44) vs DNABERT 3-mer 61.62 (86M, 3.27) vs NT-500M-human 55.43. With extra masked-language pre-training on the GUE training sets (0.41B tokens, 0.08% of its total), DNABERT-2♦ reached 67.77 and ranked top-2 on 21 datasets (11 first, 10 second). DNABERT-2 beat DNABERT on 23 of 28 datasets, by 6 points on average.
- **Data and tokenisation, not just size.** NT-2500M-1000g was trained on 2.5× more tokens than DNABERT but scored about the same (61.41 vs 61.62), which the authors read as sample inefficiency of non-overlapping k-mers. NT-500M-human scored lowest (55.43).
- **Multi-species pre-training helps non-human tasks without hurting human ones.** Per-task averages (Table 4): on mouse TF prediction DNABERT-2 scored 67.99 vs NT-2500M-multi 67.01; on human TF prediction 70.10 vs 63.32; on yeast epigenetic marks 55.98 vs 58.06; on human promoter detection 84.21 vs 88.14.
- **Short-input weakness of compressing tokenisers.** DNABERT variants did best on 70 bp core-promoter detection (DNABERT 3-mer 72.96; DNABERT-2 70.52). The authors attribute this to BPE and non-overlapping k-mers shortening a 70 bp input to about 15 tokens.
- **Long inputs via ALiBi.** Pre-trained only on 700 bp sequences, DNABERT-2 beat NT-2500M-multi and DNABERT on all GUE+ datasets (5–10 kb): fungi species classification 93.04 vs 92.85, virus species 48.50 vs 45.00, and enhancer–promoter interaction in six cell lines 73.70–92.90 vs 61.91–86.48. DNABERT could not be fit on the EPI datasets.
- **Tokenisation ablation.** With the same data, architecture and 120k steps, BPE beat 6-mer tokenisation on 21 of 28 GUE datasets (average 65.33 vs 60.92), at 3–4× lower compute.
- **Pre-training matters.** DNABERT-2 without pre-training, a CNN baseline (Grešová et al.) and the HyenaDNA HuggingFace checkpoint all scored below DNABERT-2 on GUE (Table 9).

## Methods / evidence

Model: Transformer encoder, 117M parameters, BPE (SentencePiece) vocabulary 4,096, ALiBi instead of learned positional embeddings, FlashAttention, low-precision LayerNorm, GEGLU activations. Pre-training: MLM with 15% of tokens masked independently (no span masking), batch 4,096, max length 128 tokens, 500k steps, AdamW, peak learning rate 5e-4; about 14 days on eight RTX 2080Ti GPUs (vs an estimated 28 days on 128 A100s for NT-2500M). Data: the DNABERT human set (2.75B bases) and a new multi-species set of 135 species (32.49B bases; N-containing sequences removed); the text says 6 categories in §4.1 and 7 in Table 11.

GUE: 28 datasets in 7 tasks with input 70–1,000 bp (human core promoter, promoter, TF binding and splice sites; mouse TF binding; yeast epigenetic marks; SARS-CoV-2 variant classification). GUE+: 8 datasets with 5–10 kb inputs (human enhancer–promoter interaction in six cell lines; fungi and virus species classification). Datasets were kept if most models scored moderately (e.g. F1 0.3–0.8); others were rebalanced, given adversarial examples or subsampled. Metrics are MCC except F1 for COVID. DNABERT and DNABERT-2 are fully fine-tuned (lr 3e-5); NT is fine-tuned with LoRA (r = 8, lr 1e-4) because it is too large for consumer GPUs. The authors check their NT LoRA implementation against NT's published yeast epigenetic-mark numbers and get slightly higher scores (e.g. 2500M-multi average 58.06 vs 56.90 reported). Three seeds per model; hyperparameters fixed across datasets except length and steps.

Weight: a well-documented benchmark paper, but the benchmark is the authors' own and was filtered using DNABERT and NT performance. (synthesis)

## Limitations

**Authors' own:**
- Compressing tokenisers (BPE and non-overlapping k-mers) lose signal on short inputs; overlapping k-mers still win on 70 bp core promoters. Effective modelling of short and extra-long sequences is left for future work.
- Further pre-training on GUE does not help every task, so task-specific further pre-training may be needed.
- Per-dataset hyperparameter tuning was not done.
- The HyenaDNA HuggingFace checkpoint did not reproduce HyenaDNA's reported epigenetic-mark results; possible reasons are a different checkpoint, the HuggingFace trainer, or insufficient hyperparameter search.
- Future work should use the double-stranded structure of DNA in training targets and augmentation.

**Reviewer notes:**
- GUE was built by keeping datasets where DNABERT and NT scored moderately, so it is calibrated around the very models it compares; results may not transfer to benchmarks built independently. (synthesis)
- Table 9 reports DNABERT-2 scores on human and mouse TF prediction (e.g. 84.38, 81.60) that differ from the Table 6 scores for the same datasets (71.99, 56.76) without explanation. (synthesis)
- No variant-effect, regulatory-activity or zero-shot evaluation is included; all tasks are supervised sequence classification after fine-tuning. (synthesis)

## Surprising or load-bearing bits

- **A 117M model ties a 2.5B model.** The headline is efficiency: parity with NT-2500M-multi at 1/19 the FLOPs on 500 bp inputs.
- **NT's non-overlapping 6-mers did not convert extra data into accuracy** (NT-2500M-1000g ≈ DNABERT despite 2.5× more tokens), which the authors use as evidence against non-overlapping k-mers.
- **BPE vocabulary is not "bigger is better".** Performance peaks around 4,096 tokens even though compute keeps falling with larger vocabularies.
- **Short-sequence penalty.** The core-promoter result shows the cost of compressing tokenisation: 70 bp becomes about 15 tokens. This is a concrete argument for single-nucleotide models on short regulatory elements. (synthesis)

## Concepts touched

- [[dna-language-model]] — second-generation BERT-style DNA LM; multi-species, efficiency-oriented.
- [[genomic-tokenization]] — the paper's core argument: overlapping vs non-overlapping k-mers vs BPE, vocabulary-size sweep, tokenisation ablation.
- [[transcription-factor-motif]] / [[chip-seq]] — human (ENCODE 690) and mouse (78 ENCODE sets) TF-binding tasks in GUE.
- [[histone-modifications]] — yeast epigenetic-mark prediction (H3, H3K14ac, H3K36me3, H3K4me1/2/3, H3K79me3, H3K9ac, H4, H4ac).

## Connections to other sources

- Direct successor to [[ji-2021-dnabert]]; reuses its human pre-training data, promoter and splice-site benchmarks, and names its three limitations (human-only data, k-mer leakage and inefficiency, 512-token limit).
- Main comparator: [[dallatorre-2025-nucleotide-transformer]] (cited as the 2023 bioRxiv preprint). DNABERT-2 claims parity with NT-2500M-multi and attributes NT's sample inefficiency to non-overlapping 6-mers.
- Compares with [[nguyen-2023-hyenadna]] in an appendix and could not reproduce HyenaDNA's published numbers from its public checkpoint.
- [[sanabria-2024-grover]] also uses BPE but chooses its vocabulary by next-token performance on the human genome; the two papers make different vocabulary choices for different reasons. (synthesis)
- [[fan-2026-gfetm]] includes DNABERT-2 among the 13 genome foundation models it tests as frozen peak encoders.

## Open questions

- Does BPE's advantage hold for base-resolution tasks such as variant-effect scoring, where a single substitution can change token boundaries? The paper does not test variants. (synthesis)
- How would DNABERT-2 compare on benchmarks not filtered by its own baselines, such as NT's 18-task suite or long-range benchmarks? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[ji-2021-dnabert]] · [[dallatorre-2025-nucleotide-transformer]] · [[nguyen-2023-hyenadna]] · [[fan-2026-gfetm]] · [[40-Topics/sequence-models-and-foundation-models]]
