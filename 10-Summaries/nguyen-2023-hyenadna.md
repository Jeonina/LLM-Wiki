---
type: summary
title: "Nguyen et al. 2023 — HyenaDNA: Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution"
source: "[[00-Sources/papers/HyenaDNA- Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution.pdf]]"
source_quality: full
source_sha256: "2f471549352ff571ac55faa80c8da453f9bf1ff5b01b6b87fa893457828e798c"
source_kind: paper
author: "Eric Nguyen, Michael Poli, Marjan Faizi (equal contribution), Armin W. Thomas, Callum Birch Sykes, Michael Wornow, … Stephen A. Baccus, Christopher Ré (equal senior authors)"
published: 2023-06-27
ingested: 2026-10-08
doi: "10.48550/arXiv.2306.15794"
journal: "arXiv preprint 2306.15794v2 (14 Nov 2023); the source text names no venue"
tags: [HyenaDNA, dna-language-model, Hyena-operator, long-convolution, implicit-convolution, single-nucleotide-tokenization, long-context, 1M-context, next-token-prediction, autoregressive, sequence-length-warmup, soft-prompting, in-context-learning, GenomicBenchmarks, Nucleotide-Transformer-benchmark, DeepSEA, species-classification, Stanford, HazyResearch]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[sequence-to-function-model]]", "[[convolutional-neural-network]]", "[[histone-modifications]]", "[[chromatin-accessibility]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Nguyen et al. (2023) — *HyenaDNA: Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution* — arXiv 2306.15794 (v2, November 2023). [DOI](https://doi.org/10.48550/arXiv.2306.15794)

# Nguyen 2023 — HyenaDNA

> HyenaDNA replaces attention with the Hyena operator (implicitly parameterised long convolutions evaluated by FFT in O(L log² L), with data-controlled gating) and trains a small decoder-only model by next-nucleotide prediction on the human reference genome, using single-nucleotide tokens and contexts up to 1 million bases. The paper's point is that genomic language models had to choose between long context (via k-mers, BPE, dilation or downsampling) and single-base resolution; HyenaDNA claims both, with training up to 160× faster than a FlashAttention Transformer at 1M tokens. Models are tiny (0.44M–6.6M parameters). Fine-tuned, they set new top scores on 7 of 8 GenomicBenchmarks datasets and 12 of 18 Nucleotide Transformer datasets, match DeepSEA and BigBird on 919 chromatin profiles with 5–30× fewer parameters, and solve a 5-species classification task at 450k–1M context where the Transformer cannot train. The paper also tries soft-prompt and few-shot "in-context learning" for genomics.

## Key claims

- **Long context and single-base resolution at once.** HyenaDNA uses a 4-nucleotide vocabulary plus N and special tokens and trains at up to 1M tokens, which the authors describe as up to 500× longer than dense-attention genomic models (512–4k tokens). At 1M tokens a 2-layer HyenaDNA is 160× faster than a 2-layer Transformer (forward and backward pass, A100).
- **Longer pre-training context lowers perplexity, but not for free.** Perplexity on the human genome fell as context grew to 1M (Fig. 1.2), at the cost of more tokens; shallow models can get worse at long context. The authors present context length as a regularisation dimension.
- **Sequence-length warm-up.** Starting at 64 bp and doubling the window each stage cut training time by 40% at 450k and raised species-classification accuracy by 7.5 points.
- **GenomicBenchmarks (8 datasets).** A 436k-parameter HyenaDNA beat the CNN baseline, DNABERT and a GPT baseline on 7 of 8, e.g. human enhancers Ensembl 89.2 vs CNN 68.9 and DNABERT 85.7; human non-TATA promoters 96.6 vs 84.6 and 85.6; mouse enhancers 85.1 vs 69.0 and 66.9. DNABERT was best on coding vs intergenomic (92.5 vs 91.3).
- **Nucleotide Transformer benchmark (18 datasets).** A 1.6M-parameter HyenaDNA was best on 12 of 18 against NT 500M, NT 2.5B (1000G) and NT 2.5B (multispecies). Gains were large on yeast histone marks (H3K4me3 MCC 61.2 vs 42.1 for NT multispecies; H3K4me2 53.9 vs 32.6) and enhancers; NT stayed ahead on most splice-site and promoter tasks (splice acceptor F1 99.0 vs 96.6).
- **Chromatin profiles (DeepSEA 919 tasks).** A 7M-parameter, 1k-context HyenaDNA had median AUROC 96.4 (TF), 93.0 (DHS), 86.3 (HM), vs DeepSEA 95.8/92.3/85.6 and BigBird 96.1/92.1/88.7. A 3.5M, 8k-context version reached 89.3 on histone marks but dropped on TF and DHS (95.5, 91.7).
- **Embeddings encode biotype.** Frozen embeddings with an XGBoost classifier on 10 Ensembl biotypes gave weighted F1 72.0 (HyenaDNA, 7M, 160k context) vs 66.5 (NT, 500M, 6k) and 64.6 (DNABERT, 110M, 512).
- **Long context solves species classification.** On 5-way classification (human, lemur, mouse, pig, hippo) with held-out chromosomes, accuracy rose from 61.1 (1k) to 93.4 (32k), 97.9 (250k), 99.4 (450k) and 99.5 (1M). The Transformer reached 55.4 (1k) and 88.9 (32k) and was infeasible beyond. Without pre-training, the gap at 250k–450k was more than 30 points.
- **In-context learning, partly.** Soft prompts of 2 to 32k learnable tokens, with the model frozen, approached fine-tuned performance on most GenomicBenchmarks datasets (not Human Regulatory). Few-shot demonstrations helped only after enough instruction-tuning samples.

## Methods / evidence

Architecture: decoder-only stack of Hyena blocks (order-2 Hyena operator plus MLP); long convolution filters come from a small neural network over position, so parameter count does not grow with length. Depth 2–8, width 128–256, 0.44M–6.6M parameters; gradient checkpointing above 160k. Pre-training: next-token prediction on GRCh38 using Enformer's training/validation intervals, chromosomes 14 and X held out; 10–20k steps; the 1M-context model saw 2T tokens over 4 weeks; up to 8 A100 GPUs. Short-range models pre-trained in 80 minutes on one A100 (1.3 GPU-hours) vs 12,000 for DNABERT and 215,000 for NT 2.5B (Table A.2). The authors use pre-trained context 2–4× the downstream length. Downstream: full fine-tuning with a linear head; hyperparameter sweeps including reverse-complement augmentation.

Ablations: a 6-mer tokeniser reduced GenomicBenchmarks accuracy on most datasets (by up to 10 points); a bidirectional (circular-FFT) HyenaDNA trained from scratch was 3.8 points worse on average than causal from scratch; pre-training added up to 21 MCC points on harder NT tasks (H3K4me3) and 0–1 points on near-saturated promoter and splice tasks.

Weight: a machine-learning conference-style paper with broad but mostly saturated or authors-assembled benchmarks. For the NT benchmark, the authors built their own 90:10 splits and promoter negatives because NT's splits were not released, so the comparison is with NT's reported numbers, not a shared split. (synthesis)

## Limitations

**Authors' own:**
- Pre-trained on one human reference genome only; adding more humans and species could improve generality and reduce bias.
- DNA only; no protein or chemical sequences.
- Models are much smaller than other genomic foundation models; larger models and model parallelism could extend context further.
- The 8k-context chromatin model lost accuracy on short-range TF and DHS tasks, which the authors think more depth might recover.
- Few-shot in-context learning does not work without a tuning phase, because the DNA vocabulary has no symbols for labels.

**Reviewer notes:**
- The NT comparison uses re-made splits and NT's earlier (preprint) task set, with yeast epigenetic marks; NT's journal version later reports that its Multispecies 2.5B matched or beat HyenaDNA on all 18 of its revised tasks ([[dallatorre-2025-nucleotide-transformer]]), and DNABERT-2 could not reproduce HyenaDNA's epigenetic-mark scores from the public checkpoint ([[zhou-2023-dnabert-2]]). (synthesis)
- The 1M-token context is shown to help species classification, a task that rewards mutational profile over regulatory logic; no task tests long-range regulation such as enhancer–gene links or expression. (synthesis)
- The model is causal (left-to-right) and trained only on the forward strand; DNA has no reading direction, a point Caduceus takes up ([[schiff-2024-caduceus]]). (synthesis)

## Surprising or load-bearing bits

- **Tiny models, competitive scores.** 0.4–7M parameters against 110M–2.5B-parameter baselines; pre-training takes 1.3 GPU-hours for short-range models.
- **Single-nucleotide tokens beat 6-mers** inside the same architecture, the opposite direction from DNABERT-2's BPE argument. (synthesis)
- **Causal beat bidirectional** in the from-scratch ablation, though the bidirectional version was one ad hoc implementation.
- **Pre-training matters more as inputs get longer** (species classification gap >30 points at 250k–450k).

## Concepts touched

- [[dna-language-model]] — attention-free, autoregressive DNA LM with up to 1M context.
- [[genomic-tokenization]] — argues for single-nucleotide tokens; 6-mer ablation.
- [[sequence-to-function-model]] — DeepSEA 919-profile task as a comparison point.
- [[convolutional-neural-network]] — Hyena is a long-convolution model; the GenomicBenchmarks CNN is a baseline.
- [[histone-modifications]] — yeast histone-mark tasks in the NT benchmark, the largest gains.
- [[chromatin-accessibility]] — DHS and open-chromatin-region tasks.

## Connections to other sources

- Benchmarks against [[ji-2021-dnabert]] and [[dallatorre-2025-nucleotide-transformer]] (preprint version); both later papers dispute or fail to reproduce some HyenaDNA numbers ([[zhou-2023-dnabert-2]], NT journal version).
- Uses [[zhou-2015-deepsea]]'s 919-feature dataset and [[avsec-2021-enformer]]'s genome intervals for pre-training splits.
- [[schiff-2024-caduceus]] extends the long-range, single-nucleotide, attention-free direction with bidirectional, reverse-complement-equivariant Mamba blocks and compares directly to HyenaDNA.
- [[fan-2026-gfetm]] includes HyenaDNA variants among the genome foundation models it tests as peak encoders.

## Open questions

- Does long pre-training context help any regulatory task, as opposed to species identity? NT's authors report HyenaDNA degrading as pre-training context grows. (synthesis)
- How much of the NT-benchmark advantage survives on shared splits and the revised task set? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[schiff-2024-caduceus]] · [[dallatorre-2025-nucleotide-transformer]] · [[zhou-2023-dnabert-2]] · [[zhou-2015-deepsea]] · [[fan-2026-gfetm]] · [[40-Topics/sequence-models-and-foundation-models]]
