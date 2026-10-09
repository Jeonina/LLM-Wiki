---
type: summary
title: "Aspidova et al. 2026 — Back to BERT in 2026: ModernGENA as a Strong, Efficient Baseline for DNA Foundation Models"
source: "[[00-Sources/papers/Back to BERT in 2026- ModernGENA as a Strong, Efficient Baseline for DNA Foundation Models.pdf]]"
source_quality: full
source_sha256: "1c3d77c9ba371a5c48bd373291e469d71cb1bc45012e596baec641d5f7e3dd75"
source_kind: paper
author: "Alena Aspidova, Yuri Kuratov, Artem Shadskiy, Mikhail Burtsev, Veniamin Fishman (corresponding)"
published: 2026-04-23
ingested: 2026-10-08
doi: "10.64898/2026.04.21.719816"
journal: "bioRxiv preprint"
tags: [ModernGENA, GENA-LM, ModernBERT, DNA-language-model, BPE, masked-language-model, efficiency, FlashAttention, RoPE, local-global-attention, NT-benchmark, vertebrate-pretraining, TSS-centred-sampling, baseline, preprint]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Aspidova et al. (2026) — *Back to BERT in 2026: ModernGENA as a Strong, Efficient Baseline for DNA Foundation Models* — *bioRxiv preprint*. [DOI](https://doi.org/10.64898/2026.04.21.719816)

# Aspidova 2026 — ModernGENA

> ModernGENA is the GENA-LM group's short paper arguing that a plain, modernized BERT encoder is still a strong [[dna-language-model]]. It swaps GENA-LM's original BERT blocks for **ModernBERT** (RoPE, alternating 128-token local and global attention, pre-norm, GeGLU, no biases, unpadding, FlashAttention) and keeps MLM with a 32k BPE vocabulary. Two sizes (135 M and 377 M) are pretrained on TSS-centred windows from 443 vertebrate RefSeq assemblies for about 1.3–1.5 T tokens. On the 18-task NT benchmark, ModernGENA-large has the best average rank among encoder-only models under 500 M parameters and is second overall behind the 1.2 B GENERator. With FlashAttention 2 it is several times faster at inference than DNABERT-2 and NTv2, and the gap grows with sequence length.

## Key claims

- **Benchmark rank.** Within the primary set (DNABERT-2, GENA base, NTv2-100M, NTv2-250M), ModernGENA-large has average rank 1.50 and base 2.39. In the full 13-model comparison, large ranks 3.61, behind GENERator (1.67) and ahead of NTv2-500M (4.89) and NT-multi-2.5B (8.06).
- **Where it wins and loses.** ModernGENA-large leads the primary set on most histone, enhancer and promoter tasks (e.g. enhancer 57.5 vs ≤53.6 MCC×100; TATA promoter 90.4 vs ≤87.0). On splice sites it falls well behind NTv2 (acceptor 86.4 vs 95.0; donor 88.2 vs 96.7). The authors attribute this to BPE: splice detection needs short, precisely placed motifs that fixed fine-grained tokens capture better, citing DNAChunker.
- **Pretraining clearly helps here.** Following Vishniakov et al.'s pretrained-vs-random protocol, ModernGENA-large's average NT MCC rises from 0.420 (random init) to 0.671 (pretrained), improving all 18 tasks. The authors contrast this with the modest or architecture-dependent gains Vishniakov et al. reported for other genomic models.
- **Inference throughput** (A100-80GB, maximum batch that fits). With FlashAttention 2 and bf16, ModernGENA-base processes 552 (256 tokens) to 333 (8,192 tokens) in the table's tokens/s units, against 69 → 15 for DNABERT-2 and 71 → 9 for NTv2-100M. Without FlashAttention, base is 78 → 71, roughly flat with length, while the baselines fall steeply. GENA base and large cannot run beyond 512 tokens.
- **Benchmark caveat.** The authors note that NT-benchmark differences between architectures, and even between very different model sizes, are often modest and can partly be closed by tuning fine-tuning hyperparameters. They therefore question how much scale buys for genomic sequence understanding.

## Methods / evidence

Architecture (Appendix A): base 22 layers, 768-d, 12 heads; large 28 layers, 1,024-d, 16 heads; sliding window 128 with global attention every third layer. Data: all 443 vertebrate assemblies with RefSeq gene annotation (353.6 Gbp total), but training intervals are [−16 kb, +8 kb] windows around every unique TSS of genes and pseudogenes, merged, both strands, no ambiguous bases. This follows Evo 2 and GPN-style sampling to reduce repeat over-learning. Validation is whole chromosomes (human chr8, 20, 21; ~10% for other species). Tokenizer: 32k BPE following GENA-LM, runs of N collapsed. Training: 8 A100-80GB, global batch 4,096 sequences, dynamic packing of 10–1,024 tokens (mean ≈700), AdamW with learning rate 4e-4 under a warmup–stable schedule; base saw 1,510 B tokens (158 epochs), large 1,320 B (138 epochs). NT benchmark: 10-fold CV, per-task grid search over learning rate, weight decay and batch size, no reverse-complement augmentation. Baseline scores are copied from Dalla-Torre et al. 2025 and Wu et al. 2025, except GENA base, which was re-tuned.

Weight: a short workshop-style preprint with one benchmark suite. Figures 1–3 are images; the appendix tables give the numbers used here.

## Limitations

**Authors' own:**
- Lower splice-site scores than NT variants, plausibly due to BPE tokenization.
- DNABERT-2's FlashAttention build could not be installed (a pinned Triton version is incompatible with the released code), so DNABERT-2 was benchmarked without it.
- Small metric differences on the NT benchmark may reflect fine-tuning variance; broader and longer-range benchmarks are needed.

**Reviewer notes:**
- The main text says ModernGENA has "slightly higher throughput under the standard inference configuration", but Table 2 shows GENA base faster at 256 and 512 tokens (91.8 and 82.0 vs 78.1 and 77.7). The large speed-up depends on FlashAttention 2 with bf16, which DNABERT-2 was not given. (synthesis)
- Only the NT benchmark is used; no variant-effect, long-range or cross-species tasks, so "strong baseline" is shown for short-sequence classification only. (synthesis)
- TSS-centred sampling is a data change bundled with the architecture change; the paper does not separate their contributions. (synthesis)

## Surprising or load-bearing bits

- **A plain BERT trained on a lot of data is competitive.** A 377 M encoder with no long-range or hybrid modules ranks second only to a 1.2 B model on the most-used DNA benchmark. (synthesis)
- **Gene-centred sampling instead of whole genomes.** Like other recent models, ModernGENA trains only on windows around TSSs, which moves the field away from uniform genome sampling. (synthesis)
- **The pretraining gain is large here** (0.420 → 0.671 average MCC). That contrasts with Vishniakov et al.'s ICLR study "Tokenization to transfer", which found modest or architecture-dependent gains from pretraining for several genomic models.

## Concepts touched

- [[dna-language-model]] — ModernBERT backbone as a reusable, efficient encoder.
- [[genomic-tokenization]] — BPE as the likely cause of weak splice-site performance.

## Connections to other sources

- Successor to [[fishman-2025-gena-lm]] (same group, same 32k BPE tokenizer).
- Baselines: [[zhou-2023-dnabert-2]], [[dallatorre-2025-nucleotide-transformer]], [[li-2026-generator]], [[avsec-2021-enformer]], [[nguyen-2023-hyenadna]], [[schiff-2024-caduceus]], [[sanabria-2024-grover]].
- Cites [[kim-2026-dnachunker]] for the claim that splice prediction favours fine-grained tokenization.
- Same ModernBERT backbone, different objective and tokenization: [[ding-2025-nucel]] (ELECTRA RTD, single nucleotides). (synthesis)

## Open questions

- Would ModernGENA with single-nucleotide or learned tokens close the splice-site gap without losing histone and enhancer performance? (synthesis)
- How does it do on long-range and variant-effect benchmarks, which the ModernBERT backbone is meant to support? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[fishman-2025-gena-lm]] · [[ding-2025-nucel]] · [[40-Topics/sequence-models-and-foundation-models]]
