---
type: summary
title: "Su et al. 2025 — Language Models for Controllable DNA Sequence Design"
source: "[[00-Sources/papers/Language Models for Controllable DNA Sequence Design.pdf]]"
source_quality: full
source_sha256: "f2f203c193a7531e044a6fc253f5271c8f8baa8c8a3d3d2563e1eb5d111254ce"
source_kind: paper
author: "Xingyu Su, Xiner Li, Yuchao Lin, Ziqian Xie, Degui Zhi, Shuiwang Ji (corresponding)"
published: 2025-12 (TMLR 12/2025; arXiv v2 2025-12-09)
ingested: 2026-10-08
doi: "10.48550/arXiv.2507.19523"
journal: "Transactions on Machine Learning Research (arXiv preprint 2507.19523)"
tags: [ATGC-Gen, dna-language-model, conditional-generation, regulatory-sequence-modelling, GPT, BERT, masked-recovery, promoter, enhancer, ChIP-seq, ESM-2, Sei-oracle, diffusion-baselines, benchmark]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[cis-regulatory-element]]", "[[transcription-factor-motif]]", "[[chip-seq]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Su et al. (2025) — *Language Models for Controllable DNA Sequence Design* — *Transactions on Machine Learning Research* (12/2025); arXiv:2507.19523. [DOI](https://doi.org/10.48550/arXiv.2507.19523)

# Su 2025 — ATGC-Gen

> ATGC-Gen is a **machine-learning framework that asks whether ordinary transformer language models can model regulatory DNA conditioned on biological context**, as an alternative to the diffusion and flow-matching models that dominate this benchmark family. The conditioning signal — a cell-class label, a transcription-factor protein embedding, or a per-base transcription-initiation profile — is turned into vectors and either prepended as global "property tokens" or concatenated to each position's one-hot encoding. The same framework is instantiated as a decoder (next-token objective) and as an encoder (masked-recovery objective). The paper evaluates on two existing benchmarks (promoter profiles and cell-class enhancer sets) and a new ChIP-seq-derived benchmark, scoring outputs with the Sei chromatin-profile model, a perplexity-style fluency measure under HyenaDNA, and an n-gram diversity score. This is a modelling and benchmarking study; there is no experimental validation.

## Key claims

- **Which objective wins depends on how the condition aligns with the sequence.** On the promoter benchmark, where the conditioning profile is defined per base pair (feature-level integration), the encoder variant is best: MSE 0.0192 and KS statistic 0.043, against 0.0219/0.052 for D3, 0.0269/0.399 for Dirichlet flow matching, 0.0334 for DDSM, 0.0375 for D3PM-uniform and 0.0395 for Bit Diffusion. The decoder variant gets 0.0289 MSE but the best fluency (3.5231), because pooling the base-resolution signal into a prefix destroys per-token alignment.
- **With a single global label the ordering reverses.** On the cell-class benchmark the decoder more than halves Fréchet Biological Distance against Dirichlet flow matching: 0.5080 vs 1.0404 (fly brain) and 0.9228 vs 1.9051 (melanoma), with slightly better fluency and slightly lower diversity. The encoder variant collapses on this task (FBD 27.63 and 45.27, Appendix Table 7), which the authors attribute to masked recovery handling global conditions poorly.
- **Conditioning is what carries the advantage.** Without property inputs the decoder is only mixed against the same baseline (FBD 14.6412 vs 15.2107 on fly brain; 8.3796 vs 5.3874 on melanoma), so the gain comes from using the biological context rather than from the architecture alone.
- **New ChIP-seq benchmark.** Conditioned on an ESM-2-3B embedding of the transcription factor plus cell type, the decoder reaches a mean Sei binding score of 0.1176 against 0.0747 unconditioned, 0.0036 for random sequence and 0.2319 for real sequence; diversity is 0.1228 against 0.0513 for real sequence. The model therefore recovers only about half of the real-sequence score.
- **Outputs carry expected promoter motifs.** Scanning generated promoter-task sequences against ten JASPAR matrices, more than 80% contain at least one GABPA, KLF4 or YY1 match, and sampled sequences show clustered ETS1, SP1 and NFYA matches.
- **Masked recovery can be run in few steps.** Revealing 10% of positions per step (about 103 steps for a 1,024-length sequence) matches the one-position-per-step schedule; revealing everything in one pass degrades MSE to 0.0334. The reported table uses the conservative one-per-step setting to avoid tuning on the test set.

## Methods / evidence

Two integration modes: sequence-level (property matrix linearly projected and prepended, Eq. 1) and feature-level (property vector concatenated to the one-hot base and projected, Eq. 2–3). Tokenisation is single-nucleotide. Objectives: cross-entropy next-token (Eq. 4) and masked reconstruction (Eq. 5). Architectures: BERT-base encoder (12 layers, 12 heads, 768 hidden) and a 16-layer, 16-head, 768-hidden decoder; AdamW, lr 1e−4, 10% linear warmup, A100-80GB. Datasets: 100,000 promoter sequences of 1,024 bp around FANTOM transcription start sites with per-base initiation profiles; 104k fly-brain and 89k melanoma 500 bp sequences with 81 and 47 ATAC-derived cell classes, using the Stark et al. splits; and a new ENCODE ChIP-seq set — 10 million raw rows over 340 factors and 129 cell types, filtered to GM12878, Sei-supported factor names, sequences under 500 bp and proteins under 1,000 residues, leaving 55,830 rows and 62 proteins split 51,800/2,181/1,849 by chromosome (20–21 validation, 22 and X test). Metrics: Sei-predicted activity (MSE on the H3K4me3 mark for promoters; binding probability for ChIP-seq), KS statistic, FBD from a pretrained classifier, HyenaDNA perplexity, and a weighted 10–12-mer uniqueness ratio.

Weight: a focused benchmark paper with sensible ablations (no-property, encoder vs decoder, unmasking schedule) but small models, single runs without error bars, and evaluation that leans almost entirely on one oracle model (Sei) plus a second model for fluency. (synthesis)

## Limitations

**Authors' own:**
- Limited compute prevented training larger models; frequent evaluation during autoregressive training adds overhead.
- No wet-lab validation; the authors present the conditioning interface as aligned with how design constraints are applied in practice, not as experimentally verified.
- The masked-recovery formulation needs a fixed sequence length and is "not naturally suited for generation".
- The authors raise biosafety and responsible-use concerns for this class of model in their broader-impacts statement.

**Reviewer notes:** (at most three, each marked `(synthesis)`)
- Functional scoring is circular in a mild sense: outputs are scored by Sei, and the ChIP-seq benchmark was filtered to cell types and factors Sei supports, so sequences that satisfy Sei's learned features will score well regardless of true activity. (synthesis)
- The encoder-vs-decoder comparison confounds objective with integration mode — the encoder gets per-base conditioning on the promoter task and only a global prefix on the cell-class task — so the "masked recovery handles global properties poorly" conclusion is not isolated. (synthesis)
- Diversity on the ChIP-seq task (0.1228) is more than double that of real sequence (0.0513) while the binding score is half, which is consistent with outputs drifting off the real sequence distribution rather than with a better design. (synthesis)

## Surprising or load-bearing bits

- **Conditioning placement matters more than objective choice.** Base-resolution signals must stay aligned per token; pooling them into a prefix is what sinks the decoder on the promoter task.
- **A plain transformer beats discrete-diffusion and flow-matching baselines on both benchmarks**, which is the paper's main argument that this family has been under-explored here relative to diffusion.
- **Protein language-model embeddings as the condition.** Using full-length ESM-2-3B residue embeddings for the factor, rather than a factor-name label, is what lets the model handle factors as a continuous space.
- **Masked recovery here is close to masked discrete diffusion**, as the authors note — the same equivalence NTv3 exploits when it converts its masked language-model head into a conditional generator. (synthesis)

## Concepts touched

- [[dna-language-model]] — plain decoder and encoder transformers used for conditional regulatory-sequence modelling rather than representation learning.
- [[genomic-tokenization]] — single-nucleotide tokens throughout, following DNABERT-2 and Caduceus practice.
- [[cis-regulatory-element]] — promoter and enhancer benchmarks are the main evaluation setting.
- [[transcription-factor-motif]] — JASPAR scanning of outputs; factor identity supplied as an ESM-2 embedding.
- [[chip-seq]] — ENCODE ChIP-seq peaks repurposed as a conditional benchmark with variable-length targets.

## Connections to other sources

- Uses [[chen-2022-sei]] as the scoring oracle for both promoter activity and binding, and [[nguyen-2023-hyenadna]] as the fluency model.
- Cites the DNA language-model line it builds on: [[ji-2021-dnabert]], [[zhou-2023-dnabert-2]], [[dallatorre-2025-nucleotide-transformer]], [[schiff-2024-caduceus]].
- The enhancer benchmark comes from the cell-type-directed enhancer work that [[kempynck-2026-crested]] also builds on. (synthesis)
- Closest methodological neighbour in this ingest: [[boshar-2025-ntv3]], which adds masked-diffusion conditional generation on top of a pretrained 650M backbone and validates in cells; [[ellington-2024-aido-dna]] adds a small diffusion head to an encoder for the same purpose. ATGC-Gen trains from scratch without a pretrained genome backbone. (synthesis)

## Open questions

- How much would initialising from a pretrained DNA foundation model improve these numbers? The authors train task-specific models and cite compute as the limit. (synthesis)
- Would the ranking against diffusion baselines survive evaluation by an oracle other than Sei, or by measurement? (synthesis)
- Can the per-base integration mode be combined with a global label so that one model handles both conditioning types? (synthesis)

## Related

- [[dna-language-model]] · [[cis-regulatory-element]] · [[chen-2022-sei]] · [[boshar-2025-ntv3]] · [[nguyen-2023-hyenadna]] · [[40-Topics/sequence-models-and-foundation-models]]
