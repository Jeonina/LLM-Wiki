---
type: summary
title: "Kim et al. 2026 — DNAChunker: Learnable Tokenization for DNA Language Models"
source: "[[00-Sources/papers/DNACHUNKER- Learnable Tokenization for DNA Language Models.pdf]]"
source_quality: full
source_sha256: "b3ec75dde147ad864b05aa2920112769f6869e327bb7ac7230942869040a8bd2"
source_kind: paper
author: "Taewon Kim (correspondence), Jihwan Shin, Hyomin Kim, Youngmok Jung, Jonghoon Lee, Won-Chul Lee, … (co-advised by Sungsoo Ahn and Insu Han)"
published: 2026-05-20
ingested: 2026-10-08
doi: "10.48550/arXiv.2601.03019"
journal: "arXiv preprint (v4, 2026-05-20); accepted at ICML 2026 (PMLR 306)"
tags: [DNAChunker, DNA-language-model, tokenization, learnable-tokenization, dynamic-chunking, H-Net, masked-language-model, BiMamba, transformer, repeat-downweighting, mutation-robustness, NT-benchmark, BEND, DNALongBench, GRCh38, Inocras, KAIST]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[transcription-factor-motif]]", "[[transposable-elements]]", "[[structural-variants]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Kim et al. (2026) — *DNAChunker: Learnable Tokenization for DNA Language Models* — *arXiv preprint* (ICML 2026). [DOI](https://doi.org/10.48550/arXiv.2601.03019)

# Kim 2026 — DNAChunker

> DNAChunker is a masked [[dna-language-model]] that learns its own segmentation instead of using k-mers or BPE. Single-nucleotide input passes through two encoder stages, each a 2-layer bidirectional Mamba followed by a router that places a chunk boundary wherever adjacent representations are dissimilar (cosine dissimilarity ≥ 0.5), compressing the sequence roughly 3× per stage. A 30-layer Transformer (147.5 M of 171.6 M parameters) models the compressed sequence, and a mirrored two-stage "dechunker" restores base-pair resolution for the MLM loss. It adapts H-Net-style dynamic chunking from autoregressive LMs to bidirectional MLM, with two fixes for [MASK] leakage. Trained only on GRCh38 for about 52 B bp, it reports the best average on the NT benchmark (MCC 0.772 vs 0.728 for the 1.2 B GENERator), the revised NT benchmark and BEND, and its learned chunks keep TF motifs intact and stay stable under variants.

## Key claims

- **Learned chunks preserve motifs.** Across 29 JASPAR 2024 TF motifs plus CpG islands, TATA boxes and splice donors in 10,000 hg38 windows of 8,192 bp, DNAChunker splits a motif occurrence into 1.22 tokens on average, against 2.47 for BPE (GROVER's tokenizer) and 2.32 for fixed 6-mers. The authors say BPE is statistically indistinguishable from the sequence-blind k-mer baseline.
- **Chunk length tracks information density.** Median chunk length is about 14–16 bp over coding exons, 20–28 bp over promoters and introns, and longest over SINEs, decaying with SINE age (≈32 > 28 > 17 bp for young/mid/old copies). The BPE baseline puts six of seven categories into one ≈10 bp band because of its 16 bp cap.
- **Robust to variants.** With a combined boundary-Jaccard and edit-similarity score, Stage-1 chunking is more stable than BPE for ClinVar indels (0.851 vs 0.751 benign) and for GIAB HG002 structural variants in every size bin from <50 bp to >5 kb. SNVs barely change either tokenizer (≈0.99).
- **NT benchmark (18 tasks, 10-fold CV).** Best on 13 of 18 tasks; total average MCC 0.772, average rank 1.67. Gains are largest on histone marks (average 0.701 vs 0.625 for GENERator; +0.144 on H3K4me2, +0.110 on H3K4me3). Splice-site average is 0.965, below GENERator (0.979) and NT-v2 (0.975).
- **Revised NT benchmark.** Average MCC 0.660 vs 0.637 for MxDNA and 0.626 for PatchDNA (other learnable tokenizers) and 0.650 for NT-multi-100M. Most of the margin over the learnable tokenizers comes from splice sites, where segmentation methods usually underperform.
- **Genomic Benchmarks.** Second-best average rank (3.29), average accuracy 0.885 vs 0.892 for GENERator, with about 7× fewer parameters.
- **BEND (frozen embeddings).** Best average rank 1.9 vs 2.1 for PatchDNA; best zero-shot expression-variant AUROC (0.59). Disease-variant AUROC is 0.55, well below PatchDNA (0.84) and NT-multi (0.77).
- **DNALongBench (linear probe).** Beats Caduceus-PH on all five tasks, most on enhancer–target gene (+0.061) and transcription-initiation signal (+0.047). It also beats the task-specific expert models on those two tasks and eQTL. Figure 2 is an image, so per-task values were not readable in the clipping.
- **Efficiency.** At 16 kb input, BPE costs 1.58× forward and 1.25× backward FLOPs relative to DNAChunker at matched 170 M size; single-nucleotide tokenization costs 17.6× and 13.9×.
- **Controlled ablation** (50 M BiMamba–Transformer–BiMamba, 2 B tokens, linear probe on revised NT): DNAChunker 0.390 overall MCC vs 0.375 BPE and 0.347 6-mer. Removing mask protection (0.332), residual gating (0.353) or the ratio loss (0.348) each hurts. With a multispecies corpus the gap over BPE widens (0.448 vs 0.375).

## Methods / evidence

Architecture: vocabulary of 10 single-nucleotide and special tokens, 640-d. Router boundary probability p_t = ½(1 − cos(q_t, k_{t−1})), hard boundaries at p ≥ 0.5, and an H-Net ratio loss pulling each stage toward a 0.33 retention target. **Mask protection** forces boundaries before and after each masked base so [MASK] never merges into a chunk. **Masked residual gating** zeroes encoder skip connections into segments containing a mask, so masked bases must be predicted by the main network. The dechunker uses bidirectional probability-gated linear scans. Pretraining: GRCh38 with Enformer's 1 Mb split regions, 8,192 bp windows, 15% BERT-style masking, RepeatMasker positions down-weighted to 0.1 in the loss (following Evo 2), 50k steps of 2^20 tokens on 4 GPUs, AdamW with a WSD schedule. Fine-tuning: mean pooling plus a linear head, grid search over 20 (learning rate, batch) settings per task. For DNALongBench, 8 kb windows with 50% overlap are tiled and re-aggregated.

Weight: an ICML paper with five benchmarks and a controlled ablation. Most baseline numbers are copied from earlier papers (Wu et al. 2025 for NT and Genomic Benchmarks, Del Vecchio et al. 2026 for revised NT, Marin et al. 2024 for BEND), not re-run under one protocol. Three authors are at Inocras Korea Inc., which co-developed and funded the work (declared).

## Limitations

**Authors' own:**
- Prior work found segmentation-based tokenizers can underperform on tasks that need uniform base-level resolution such as splice sites; the authors claim to close that gap, but on the original NT splice tasks DNAChunker still trails GENERator and NT-v2.
- The Impact Statement flags genetic-privacy, re-identification and dual-use risks.

**Reviewer notes:**
- The main text says DNAChunker compresses "repetitive or redundant sequence", but Appendix D says tandem simple repeats get the *shortest* chunks (≈14–16 bp) alongside exons. Only SINEs get long chunks, so "repeats are compressed" holds for interspersed repeats, not simple repeats. (synthesis)
- The input is still single-nucleotide; the "tokenizer" is internal pooling, so the model keeps base-level resolution at input and output. That makes the comparison with BPE/k-mer models partly a comparison of architectures, not only of tokenization. The 50 M ablation controls for this better than the headline tables. (synthesis)
- Zero-shot disease-variant AUROC (0.55) is near chance, so motif preservation and mutation-stable chunking did not translate into pathogenicity scoring. (synthesis)

## Surprising or load-bearing bits

- BPE fragments TF motifs about as badly as fixed 6-mers (2.47 vs 2.32 tokens per motif), which undercuts the common argument that BPE finds "biological words".
- SINE chunk length falls with SINE age: the model gives longer chunks to young, near-identical copies and shorter chunks to diverged copies. Chunk length works as a learned redundancy measure. (synthesis)
- The multispecies run improved DNAChunker much more than BPE (+0.073 overall), suggesting learned tokenization benefits more from sequence diversity than fixed vocabularies do.

## Concepts touched

- [[genomic-tokenization]] — learnable, context-dependent chunking as the alternative to k-mer, BPE and single-nucleotide input.
- [[dna-language-model]] — hierarchical BiMamba–Transformer MLM, human-only pretraining.
- [[transcription-factor-motif]] — motif fragmentation as an evaluation of tokenizers.
- [[transposable-elements]] — SINE chunk length decays with element age.
- [[structural-variants]] / [[variant-effect-prediction]] — tokenization stability under GIAB SVs and ClinVar indels; BEND zero-shot variant scoring.

## Connections to other sources

- Baselines: [[zhou-2023-dnabert-2]], [[nguyen-2023-hyenadna]], [[dallatorre-2025-nucleotide-transformer]], [[schiff-2024-caduceus]], [[sanabria-2024-grover]] (BPE tokenizer used for the fragmentation and robustness tests), [[li-2026-generator]], [[fishman-2025-gena-lm]], [[avsec-2021-enformer]] (benchmark baseline and data splits).
- Other tokenization papers in this ingest: [[chen-2023-genomicbert]] (Unigram), [[chen-2026-genart]] (adaptive words), [[medvedev-2025-biofm]] (variant-aware tokens). (synthesis)

## Open questions

- How does DNAChunker compare with PatchDNA and MxDNA when all are re-run under the same fine-tuning protocol? (synthesis)
- Does learned chunking help variant scoring if the score is computed at chunk level rather than by cosine distance at the variant base? (synthesis)
- Why do simple repeats receive short chunks while SINEs receive long ones? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[sanabria-2024-grover]] · [[schiff-2024-caduceus]] · [[chen-2026-genart]] · [[40-Topics/sequence-models-and-foundation-models]]
