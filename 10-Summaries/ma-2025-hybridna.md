---
type: summary
title: "Ma et al. 2025 — HybriDNA: A Hybrid Transformer-Mamba2 Long-Range DNA Language Model"
source: "[[00-Sources/papers/HybriDNA- A Hybrid Transformer-Mamba2 Long-Range DNA Language Model.pdf]]"
source_quality: full
source_sha256: "1a1728d29f1e6bae88dd9bc7d862af8b320a3441f94dc93b22f78575e44e227d"
source_kind: paper
author: "Mingqian Ma, Guoqing Liu, Chuan Cao, Pan Deng (co-first), Tri Dao, Albert Gu, … Tao Qin (corresponding)"
published: 2025-02-18
ingested: 2026-10-08
doi: "10.48550/arXiv.2502.10807"
journal: "arXiv preprint (arXiv:2502.10807v2, cs.LG)"
tags: [HybriDNA, DNA-language-model, decoder-only, Mamba2, state-space-model, hybrid-architecture, long-context, next-token-prediction, echo-embedding, single-nucleotide, GUE, BEND, LRB, regLM, CRE-design, enhancer-design, scaling, Microsoft-Research]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[cis-regulatory-element]]", "[[chromatin-accessibility]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Ma, Liu, Cao, Deng et al. (2025) — *HybriDNA: A Hybrid Transformer-Mamba2 Long-Range DNA Language Model* — arXiv preprint. [DOI](https://doi.org/10.48550/arXiv.2502.10807)

# Ma 2025 — HybriDNA

> HybriDNA (Microsoft Research AI for Science, with Mamba authors Tri Dao and Albert Gu) is a decoder-only DNA language model that interleaves **Mamba2 and Transformer blocks 7:1**, uses single-nucleotide tokens and no positional encoding, and is pre-trained by next-token prediction on a 845-species, ~160-billion-nucleotide corpus. Context is warmed up from 8k to 32k to 131k tokens. Two fine-tuning modes cover both uses of a DNA model: **echo embeddings** (feed the sequence twice and pool the second copy) give a causal model access to "future" context for classification, and **prompt-token generative fine-tuning** designs regulatory sequences. Models at 300M, 3B and 7B parameters show lower pre-training loss with size, lead most GUE tasks, are competitive on BEND, give small gains on long-range eQTL with longer context, and generate enhancers and yeast promoters that a regLM oracle scores higher than HyenaDNA's.

## Key claims

- **Hybrid beats pure Mamba2 on pre-training loss.** A 300M model with no attention layers had higher training and validation loss at 8k context than the hybrid (Fig. A2, curves only, no numbers in text).
- **Scaling.** Training and validation losses decrease from 300M to 3B to 7B (Fig. 3, curves only). Downstream gains with size are visible on most GUE categories but not all (yeast epigenetic marks: 3B 69.06 > 7B 63.05).
- **GUE (28 short tasks, 70–512 bp; category means).** HybriDNA-7B with echo embedding (E) leads human TF (72.01 MCC vs DNABERT-2 68.71), mouse TF (79.02 vs 70.00), splice sites (90.12 vs NT-2.5B 89.35), core promoters (72.03 vs DNABERT-2 71.81) and COVID variants (74.88 for 3B(E) vs NT 73.04). Yeast epigenetic marks are best at 3B (69.06 vs NT 57.64). NT-2.5B-MS keeps human promoter detection (88.15 vs 7B(E) 88.10). Echo embedding adds about 0.1–2 points in most categories.
- **BEND (frozen embeddings + two-layer CNN, AUROC).** HybriDNA-7B: chromatin accessibility 0.84, histone modification 0.79, CpG methylation 0.93, against the best baselines 0.83 (Caduceus), 0.79 (DNABERT-2) and 0.92 (NT-2.5B). HybriDNA-300M is below several baselines (0.78, 0.77, 0.88).
- **Long-range (Genomics LRB).** For causal eQTL with fine-tuning, HybriDNA-300M rises from AUROC 0.71 (8k) to 0.72 (32k) to 0.74 (131k), against 0.68–0.72 for baselines. All models are at chance zero-shot (eQTL AUROC 0.49–0.51; OMIM AUPRC 0.002–0.003).
- **Regulatory-element design (regLM setup).** For human enhancers (200 bp; HepG2, K562, SK-N-SH; target labels that make up 0.16% of training data), HybriDNA-300M's top-100 mean predicted activity is 5.4 / 6.2 / 4.7 against HyenaDNA 4.0 / 3.8 / 2.3 and held-out test sequences 2.6 / 2.4 / 1.6, with higher diversity (mean edit distance 108.74 vs 98.50). For yeast promoters (80 bp; 7.4M training sequences; target labels 0.34%), mean activity is 15.0 / 13.5 vs HyenaDNA 11.4 / 10.8. HybriDNA was fine-tuned from a multispecies checkpoint, whereas regLM's HyenaDNA yeast model was trained from scratch.
- **Efficiency.** Against a ~300M pure Transformer with FlashAttention-2 on four A100s, HybriDNA has about 3.4× higher training throughput at 49k tokens, uses less memory, and trains at ~65k tokens where the Transformer runs out of memory.

## Methods / evidence

Architecture: Mamba2 (SSD layer, scalar-times-identity state transition, RMSNorm) blocks with one Transformer decoder block per eight layers (in the fourth position); the first block is Mamba2, so no explicit positional embedding is used; no mixture-of-experts because MoE was unstable in DNA fine-tuning. Sizes: 7B (32 layers, hidden 4,096), 3B (16 layers, hidden 4,096), 300M (24 layers in Table A1, hidden 1,024). Pre-training: 845 species (647 bacteria, 28 mammals, 51 other vertebrates, 37 invertebrates, 44 fungi, 9 protozoa) curated from the NT multispecies set and NCBI; 0.5M tokens per batch, 500k steps at 8,192 tokens (250B tokens, ~1.5 epochs); each context extension adds 2% of the original steps. Hardware: 300M on 8 MI300X, 3B on 8 H100, 7B on 64 MI300X; about 300 h of training for the 300M and 7B models and 500 h for the 3B. Baselines (NT-500M-human, NT-2.5B-MS, DNABERT-2, HyenaDNA-medium-160k, Caduceus-Ph-131k) were run from their released weights. Generation uses beam search and regLM's own activity oracles.

Weight: broad and partly re-run benchmark, which is better than copied leaderboards. But the design results are oracle scores with no wet-lab validation, the LRB gains are within 0.02 AUROC, and the scaling and hybrid-vs-Mamba claims rest on loss curves shown only as figures.

## Limitations

**Authors' own:**
- Echo embedding doubles input length and raises memory cost, mitigated but not removed by the hybrid design.
- Designed sequences need wet-lab validation; the authors list this and a larger, more diverse pre-training set as future work.
- Evo was excluded because the evaluation focuses on eukaryotic tasks.

**Reviewer notes:**
- Internal inconsistencies: the abstract says 33 datasets, the introduction says 35; Table A1 lists the 300M model with 24 layers while its footnote says 32; the corpus is "160 billion nucleotides" in Methods and "approximately 200 billion tokens" in Appendix A.3. (synthesis)
- Long-range evaluation is thin: one fine-tuned task (eQTL) with a 0.03 AUROC spread, and only the 300M model was evaluated at long context; zero-shot variant effects are at chance for every model. (synthesis)
- "State of the art" mostly means the 7B model against much smaller baselines (Caduceus 7.73M, HyenaDNA 14.2M), so architecture and scale are confounded. (synthesis)

## Surprising or load-bearing bits

- **Echo embeddings** are a cheap fix for the causal model's one-sided context: repeating the input lets every token in the second copy see the whole sequence. The gain is consistent but small (≤2 MCC points).
- **No positional encoding at all** — the first Mamba2 block supplies order, which is part of why context extension needs no RoPE rescaling (contrast Gene42). (synthesis)
- **Generated enhancers beat real held-out ones on the oracle** (mean activity about double the test set), which may say as much about oracle exploitation as about design quality. (synthesis)

## Concepts touched

- [[dna-language-model]] — hybrid SSM/attention decoder for both understanding and generation.
- [[genomic-tokenization]] — single-nucleotide tokens made affordable by Mamba2's linear-time layers.
- [[variant-effect-prediction]] — LRB causal eQTL (fine-tuned) and OMIM (zero-shot, at chance).
- [[cis-regulatory-element]] — prompt-conditioned generation of cell-type-specific enhancers and yeast promoters.
- [[chromatin-accessibility]] — BEND accessibility and histone-mark probes on frozen embeddings.

## Connections to other sources

- Baselines: [[zhou-2023-dnabert-2]] (GUE benchmark source), [[dallatorre-2025-nucleotide-transformer]] (pre-training corpus source), [[nguyen-2023-hyenadna]] (decoder baseline and regLM generator), [[schiff-2024-caduceus]] (bidirectional Mamba1).
- Cites [[li-2026-generator]] (GENErator, as an arXiv preprint) as concurrent long-context generative work.
- Bidirectional hybrid alternative: [[duan-2025-janusdna]], which also mixes attention and Mamba but trains bidirectionally. Dense-attention alternative: [[vishniakov-2025-gene42]]. (synthesis)

## Open questions

- Does the 7B model also gain from 131k context on eQTL, or is the long-context benefit specific to the 300M model? Not tested.
- Would the enhancer designs hold up in MPRA, or are they adversarial to the regLM oracle? (synthesis)
- How does echo embedding compare with true bidirectional training (as in JanusDNA or Caduceus) at matched size? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[cis-regulatory-element]] · [[nguyen-2023-hyenadna]] · [[duan-2025-janusdna]] · [[40-Topics/sequence-models-and-foundation-models]]
