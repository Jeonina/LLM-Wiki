---
type: summary
title: "Ding et al. 2025 — NucEL: Single-Nucleotide ELECTRA-Style Genomic Pre-training for Efficient and Interpretable Representations"
source: "[[00-Sources/papers/NucEL- Single-Nucleotide ELECTRA-Style Genomic Pre-training for Efficient and Interpretable Representations.pdf]]"
source_quality: full
source_sha256: "17594b05da8192aecb258206dff41edb88e8570e27ecdcce41e2a615f1972ffe"
source_kind: paper
author: "Ke Ding, Brian John Parker (corresponding), Jiayu Wen (corresponding)"
published: 2025-08-17
ingested: 2026-10-08
doi: "10.1101/2025.08.17.670700"
journal: "bioRxiv preprint"
tags: [NucEL, DNA-language-model, ELECTRA, replaced-token-detection, pretraining-objective, ModernBERT, single-nucleotide-tokenization, local-global-attention, FlashAttention, GUE, Genomic-Benchmarks, NT-benchmark, attention-interpretability, efficiency, preprint]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[transcription-factor-motif]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Ding et al. (2025) — *NucEL: Single-Nucleotide ELECTRA-Style Genomic Pre-training for Efficient and Interpretable Representations* — *bioRxiv preprint*. [DOI](https://doi.org/10.1101/2025.08.17.670700)

# Ding 2025 — NucEL

> **Clipping note:** the PDF text has the full main paper (pp. 1–12) but no Appendix, which the text cites for hyperparameters, benchmark details, histone results, the motif-order task and attention heatmaps.
>
> NucEL is a [[dna-language-model]] whose contribution is the **pretraining objective**. It is the first genomic model, by the authors' account, to use ELECTRA's **replaced token detection (RTD)**: a small generator (11 layers, 256-d) fills masked positions, and the main model, a 93 M-parameter ModernBERT discriminator (22 layers, 512-d, local 128-token attention with global attention every third layer), classifies every position as original or replaced. All N positions get a training signal instead of the ~15% in MLM, a 6.67× supervision ratio. With single-nucleotide tokens and human-only pretraining, it reports the best average on GUE (75.16 vs 72.94 for NT-2.5B-multi), Genomic Benchmarks (0.899) and the revised NT benchmark (0.664), and sharper attention on motifs than NT2-100M.

## Key claims

- **GUE (7 tasks, MCC, 3 seeds).** Average 75.16, ahead of NT-2500M-multi (72.94) and DNABERT-2 (72.11). Best on core promoter (75.13), splice sites (90.30), mouse TF binding (70.62) and yeast epigenetic marks (65.01, vs 58.06 next best). DNABERT-2 is better on human TF binding (70.10 vs 67.64), and NT-2500M-multi on promoter detection (88.14 vs 87.10) and COVID variant classification (73.04 vs 70.29).
- **Cross-species transfer.** Despite human-only pretraining, NucEL is in the top two on 6 of 7 GUE tasks including mouse, yeast and virus.
- **Genomic Benchmarks (7 human tasks, accuracy, 5 seeds).** Average 0.899 vs 0.890 for NT2-100M and 0.882 for Caduceus-Ph; best on 4 tasks, with the largest margin on non-TATA promoters (0.973 vs 0.946).
- **Revised NT benchmark (18 tasks, MCC, 10 seeds).** Average 0.664 vs 0.651 NT2-Multi-100M, 0.634 NT-HumanRef-500M, 0.628 DNABERT-2; best on 11 of 18. Gains are in enhancers (0.578 vs ≤0.517), TATA promoters (0.922 vs ≤0.831) and splice sites. On histone marks it is mixed, losing to DNABERT-2 on H3K36me3, H3K4me3, H3K27ac and H4K20me1.
- **Tokenization ablation.** Within NucEL, single-nucleotide tokens beat 6-mer and BPE across training epochs on human GUE tasks (Figure 2A; values readable only as a plot).
- **Compute.** On human GUE tasks, NucEL beats NT-2.5B models that are about 25× larger and use more than 100× the compute, and beats similar-compute NT-500M models by more than 10% MCC (Figure 2B, PF-days on a log axis).
- **Gene-biotype embeddings.** An XGBoost classifier on frozen embeddings gave NucEL the best macro-F1 (0.731 vs 0.688 HyenaDNA, 0.640 DNABERT-2, 0.633 NT2-100M). Micro and weighted F1 margins are small (0.760 vs 0.758; 0.749 vs 0.747).
- **Attention interpretability.** On a synthetic "motif order" task (motif A before B is positive), both NucEL and NT2-100M reached near-perfect accuracy, but NucEL's global-layer attention had 65% (motif A) and 152% (motif B) higher maximum signal-to-noise at the motif positions.

## Methods / evidence

Loss = L_generator (MLM cross-entropy on masked positions) + 50 × L_discriminator (binary cross-entropy over all positions). Pretraining corpus: GRCh38, 1,224 bp sliding windows with 100 bp overlap, 1,024 bp segments sampled; 27-token vocabulary (4 bases, 7 special tokens, 16 reserved). AdamW, learning rate 1e-4, 50 epochs, global batch 192, FP16 on 8 A100s. Fine-tuning: a linear head on the discriminator's [CLS] output, full fine-tuning. Baselines are taken from published protocols (DNABERT-2 for GUE, Caduceus for Genomic Benchmarks, NT for revised NT); the text does not say whether they were re-run.

Weight: a preprint marked "under review" with three standard benchmarks and seeds. There is no controlled MLM-vs-RTD comparison in the main text at matched architecture and data. The abstract mentions ablations of "masking strategies", but these are not in the clipped text.

## Limitations

**Authors' own:**
- Pretraining is limited to the human genome. Adding invertebrates, microbes and other clades could help with clade-specific regulatory elements and non-conserved motifs.

**Reviewer notes:**
- The paper credits gains to RTD, single-nucleotide tokens and ModernBERT together, but only tokenization is ablated in the main text. Without an MLM baseline on the same ModernBERT backbone, the RTD contribution is not isolated. (synthesis)
- The text says NucEL's 0.664 "matches NT2-Multi (500M parameters)", but Table 3's NT2-Multi is the 100 M model (0.651), and no NT2-500M row appears. (synthesis)
- Context is 1,024 bp; the efficiency claims concern training compute, not long-range modeling. (synthesis)

## Surprising or load-bearing bits

- **The objective, not the tokenizer, is the lever.** Most DNA-LM papers change the tokenizer or backbone; NucEL changes what the encoder is trained to predict, and gets every position supervised. (synthesis)
- Yeast epigenetic-mark prediction jumps 7 MCC points over every baseline from a human-only model, the largest single gain in the GUE table.
- Its tokenization ablation points the opposite way to DNAChunker and GenART: under RTD, single nucleotides beat both 6-mers and BPE, while those papers find learned chunks beat single nucleotides under MLM. (synthesis)

## Concepts touched

- [[dna-language-model]] — ELECTRA-style RTD as an alternative to MLM and autoregressive objectives.
- [[genomic-tokenization]] — single-nucleotide tokens beat 6-mer and BPE inside the same model.
- [[transcription-factor-motif]] — motif-order task and attention signal-to-noise as an interpretability test.

## Connections to other sources

- Baselines: [[ji-2021-dnabert]], [[zhou-2023-dnabert-2]], [[dallatorre-2025-nucleotide-transformer]], [[nguyen-2023-hyenadna]], [[schiff-2024-caduceus]]. BPE critique cites [[sanabria-2024-grover]].
- Same ModernBERT recipe, different objective: [[aspidova-2026-moderngena]] uses ModernBERT with MLM and BPE. (synthesis)
- Contrasting tokenization conclusions: [[kim-2026-dnachunker]], [[chen-2026-genart]]. (synthesis)

## Open questions

- How much of the gain survives a matched MLM baseline on the same ModernBERT discriminator? (synthesis)
- Does RTD pretraining improve zero-shot variant scoring, given that the discriminator is trained to spot single-base substitutions? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[aspidova-2026-moderngena]] · [[zhou-2023-dnabert-2]] · [[40-Topics/sequence-models-and-foundation-models]]
