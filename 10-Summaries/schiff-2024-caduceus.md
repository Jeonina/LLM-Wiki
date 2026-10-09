---
type: summary
title: "Schiff et al. 2024 — Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling"
source: "[[00-Sources/papers/Caduceus_ Bi-Directional Equivariant Long-Range DNA Sequence Modeling]]"
source_quality: full
source_sha256: "62ff0f80b7077c097a2592c1a71ce2feec3414835020d40aad00af170a1fdf36"
source_kind: paper
author: "Yair Schiff, Chia-Hsiang Kao, Aaron Gokaslan, Tri Dao, Albert Gu, Volodymyr Kuleshov (corresponding author not marked in the clipping)"
published: 2024-07
ingested: 2026-10-08
doi: "10.48550/arXiv.2403.03234"
pmid: "40567809"
journal: "Proceedings of Machine Learning Research 235:43632–43648 (ICML 2024); source is the PMC author manuscript PMC12189541"
tags: [Caduceus, dna-language-model, Mamba, state-space-model, SSM, BiMamba, MambaDNA, reverse-complement-equivariance, RC-equivariance, post-hoc-conjoining, bidirectional, long-context, single-nucleotide-tokenization, masked-language-modeling, variant-effect-prediction, eQTL, GenomicBenchmarks, Nucleotide-Transformer-benchmark]
entities: []
concepts: ["[[dna-language-model]]", "[[variant-effect-prediction]]", "[[genomic-tokenization]]", "[[sequence-to-function-model]]", "[[histone-modifications]]", "[[convolutional-neural-network]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Schiff et al. (2024) — *Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling* — *Proceedings of Machine Learning Research* 235 (ICML 2024). [DOI](https://doi.org/10.48550/arXiv.2403.03234) · PMID 40567809

# Schiff 2024 — Caduceus

> Caduceus is a small DNA language model built from Mamba selective state-space blocks, changed to fit two properties of DNA that earlier long-range models ignored: context matters on both sides of a base, and the two strands carry the same information in reverse complement (RC). The authors add BiMamba (forward and reversed passes that share projection weights, so depth is not halved) and MambaDNA (forward and RC passes with shared weights, giving RC equivariance by construction). Caduceus-PS is RC-equivariant end to end, including embeddings and the LM head; Caduceus-Ph is a BiMamba stack trained with RC augmentation and averaged over both strands at inference (post-hoc conjoining). Pre-trained by masked-token prediction on the human reference at single-nucleotide resolution and contexts up to 131k, the ~0.5–2M-parameter models beat HyenaDNA of similar size on most short tasks. On long-range eQTL variant-effect prediction, Caduceus-PS beats the 500M-parameter NT-v2, and beyond 100 kb from the TSS it also beats Enformer.

## Key claims

- **Mamba beats Hyena on next-token prediction** at comparable size and length on the human genome (Fig. 3a), and was more robust to high learning rates.
- **Weight-tied bidirectionality helps.** BiMamba with shared projections allows deeper models at the same parameter count and gave lower MLM loss than naive bidirectional Mamba at half depth (Fig. 3b).
- **RC equivariance helps pre-training.** RC-equivariant language modelling gave lower MLM loss across sequence lengths (Fig. 3c). Caduceus-PS needs no RC augmentation because its predictions are symmetric by construction (Theorems 3.1 and 4.1, with proofs).
- **GenomicBenchmarks.** With 5-fold CV on true train/test splits, a Caduceus model was best on all 8 datasets; Caduceus-Ph (470k parameters) was best overall. Examples: human enhancers Ensembl 0.900 (PS) and 0.893 (Ph) vs HyenaDNA 0.849 and CNN 0.744; human OCR Ensembl 0.828 (Ph) vs 0.783; mouse enhancers 0.793 (PS) vs 0.780.
- **Nucleotide Transformer tasks.** Against leaderboard results for Enformer (252M), DNABERT-2 (117M) and NT-v2 (500M), Caduceus-Ph (1.9M) was best on 8 of 18 tasks, mostly histone marks (e.g. H3K14ac MCC 0.631 vs 0.551 for NT-v2; H4ac 0.621 vs 0.495). NT-v2 led on promoters and all splice tasks (splice all accuracy 0.983 vs 0.940). Caduceus beat HyenaDNA (1.6M) on almost all histone and regulatory tasks; HyenaDNA was better on splice sites.
- **Long-range variant effects.** On an Enformer-derived eQTL task (SuSiE causal probability > 0.9; chromosomes 9 and 10 held out), SVMs on embeddings from Caduceus models beat HyenaDNA in all distance bins; Caduceus-PS beat NT-v2 increasingly with distance to the TSS and beat Enformer for SNPs more than 100 kb from the TSS. The AUROC values are in Fig. 4, an image not readable in the clipping.

## Methods / evidence

Architecture: Mamba blocks (selective SSM + gated MLP). BiMamba runs the block on the sequence and its reversal with shared in/out projections and sums the outputs. MambaDNA splits channels in two, applies the reverse complement to one half, runs a shared (Bi)Mamba on both and concatenates. Caduceus-PS adds RC-equivariant token embeddings and LM head; downstream, the two halves of the final hidden state are averaged for RC invariance. Caduceus-Ph uses BiMamba only, RC augmentation in pre-training and fine-tuning, and averages forward and RC predictions at inference. Tokens are single nucleotides; the authors avoid k-mers because small input changes can change the whole tokenisation (citing DNABERT-2).

Pre-training: human reference genome with Enformer's splits (34,021 training segments extended to 2²⁰ bp, about 35B tokens); BERT masking (15%; 80/10/10); 2²⁰ tokens per batch; learning rate 8e-3; models at 1k (4 layers, hidden 118–256, 10k updates), 32k (8 layers, 256, 10k) and 131k (16 layers, 256, 50k). HyenaDNA was re-pre-trained under the same recipe for the loss comparison. Downstream: GenomicBenchmarks with 5-fold CV and 10 epochs; NT tasks with 10-fold CV, NT protocol, baseline numbers pulled from the NT leaderboard; VEP with averaged 1,536 bp embeddings (ref and alt concatenated, plus tissue), input 131k for SSMs, 12k for NT-v2 and 196k for Enformer, RBF-SVM on 5,000 training points per distance bin, 5 repeats.

Weight: a clear architecture paper with ablations. Baselines in the NT table come from a leaderboard rather than re-runs, and the VEP evaluation uses frozen embeddings plus an SVM, not fine-tuned models. (synthesis)

## Limitations

**Authors' own:**
- Scope is limited to human-genome tasks and pre-training on the human reference genome.
- On the NT benchmark, Caduceus does not beat large Transformers on promoter and splice-site tasks, and HyenaDNA is better than Caduceus on splice sites.
- The impact statement notes possible misuse, as for any language model.

**Reviewer notes:**
- The VEP comparison feeds each model a different input length and a different embedding window (1,536 tokens for SSMs, 256 tokens for NT, 12 positions for Enformer), so the long-range result mixes architecture with input design. (synthesis)
- The headline VEP numbers are only in a figure; the text gives the ranking but no AUROC values. (synthesis)
- Models are 0.5–2M parameters and trained on one genome; whether the RC-equivariance gain holds at the scale of NT or Evo-class models is not tested. (synthesis)

## Surprising or load-bearing bits

- **RC equivariance as an architecture constraint rather than augmentation.** Caduceus-PS is, by the authors' account, the first RC-equivariant DNA language model.
- **Post-hoc conjoining (Ph) often beat the fully equivariant model (PS)** on short tasks, matching earlier supervised-model findings that the authors cite.
- **Tiny models beat Enformer on distal eQTLs.** Beyond 100 kb from the TSS, a ~2M-parameter self-supervised model's embeddings beat a supervised 252M-parameter Enformer in this frozen-embedding setup.
- **Histone-mark tasks favour small SSMs, splice tasks favour large Transformers** on the NT benchmark — the same split HyenaDNA reported. (synthesis)

## Concepts touched

- [[dna-language-model]] — bidirectional, RC-equivariant, attention-free DNA LM.
- [[variant-effect-prediction]] — long-range eQTL classification stratified by distance to TSS.
- [[genomic-tokenization]] — single-nucleotide tokens, justified against k-mer instability.
- [[sequence-to-function-model]] — Enformer as the supervised long-range baseline.
- [[histone-modifications]] — yeast histone-mark tasks where Caduceus gains most.
- [[convolutional-neural-network]] — GenomicBenchmarks CNN baseline; RC parameter sharing originates in CNNs.

## Connections to other sources

- Direct successor in approach to [[nguyen-2023-hyenadna]]: keeps single-nucleotide tokens and long context but adds bidirectionality and RC equivariance; re-pre-trains HyenaDNA as a baseline and fixes its train/test-split practice on GenomicBenchmarks.
- Compares with [[dallatorre-2025-nucleotide-transformer]] (NT-v2 500M) and [[zhou-2023-dnabert-2]] using the NT leaderboard, and with [[avsec-2021-enformer]] on eQTLs.
- Cites [[ji-2021-dnabert]] and [[fishman-2025-gena-lm]] as Transformer DNA LMs limited by quadratic attention, and GPN ([[benegas-2025-gpn-msa]] is a later GPN-family paper in this ingest) for zero-shot variant prediction. (synthesis)

## Open questions

- Does RC equivariance improve variant-effect prediction when models are fine-tuned rather than probed with an SVM? (synthesis)
- Would the long-range eQTL advantage hold against long-context models given the same input window, and at larger scale? (synthesis)

## Related

- [[dna-language-model]] · [[variant-effect-prediction]] · [[nguyen-2023-hyenadna]] · [[dallatorre-2025-nucleotide-transformer]] · [[avsec-2021-enformer]] · [[40-Topics/sequence-models-and-foundation-models]]
