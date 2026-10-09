---
type: summary
title: "Ellington et al. 2024 — Accurate and General DNA Representations Emerge from Genome Foundation Models at Scale"
source: "[[00-Sources/papers/Accurate and General DNA Representations Emerge from Genome Foundation Models at Scale.pdf]]"
source_quality: full
source_sha256: "46da40c215612ebe2fec3193e64cef6862f346a5004ce96af58a7ea7b319d056"
source_kind: paper
author: "Caleb N. Ellington, Ning Sun, Nicholas Ho, Tianhua Tao, Sazan Mahbub, Dian Li, … Le Song (corresponding), Eric P. Xing (corresponding)"
published: 2024-12 (bioRxiv; this version posted 2025-01-11)
ingested: 2026-10-08
doi: "10.1101/2024.12.01.625444"
journal: "bioRxiv preprint (AI for New Drug Modalities workshop, NeurIPS 2024)"
tags: [AIDO.DNA, GenBio-AI, dna-language-model, genome-foundation-model, encoder-only, BERT, masked-language-model, single-nucleotide-tokenization, scaling, 7B, zero-shot-variant-effect, nucleotide-dependency, masked-diffusion, promoter-design, preprint-text]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[cis-regulatory-element]]", "[[transcription-factor-motif]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/histone-modifications]]"]
---

**Citation:** Ellington et al. (2024) — *Accurate and General DNA Representations Emerge from Genome Foundation Models at Scale* — *bioRxiv preprint* (NeurIPS 2024 workshop paper). [DOI](https://doi.org/10.1101/2024.12.01.625444)

# Ellington 2024 — AIDO.DNA

> AIDO.DNA is a **7-billion-parameter BERT-style encoder** (plus a 300M sibling) trained with masked language modelling on **single-nucleotide tokens** with a **short 4 kb context**, using essentially the same multi-species genome set as the Nucleotide Transformer (796 genomes, 10.6 billion training nucleotides). The paper argues that the bottleneck for DNA language models is **representation capacity, not context length or new data**: with the same data as NT and only modest architecture changes (SwiGLU, RoPE), scaling the encoder gives new best scores on the DNABERT-2 (GUE) and NT benchmark suites, better zero-shot pathogenic-variant detection, richer unsupervised nucleotide-dependency maps, and — with a small diffusion head — expression-conditioned promoter generation. It is a short workshop-style preprint from GenBio AI, framed as one module of an "AI-driven Digital Organism".

## Key claims

- **Scale beats context.** The authors place AIDO.DNA against a catalogue of 17 earlier sequence models (Table 1) and deliberately keep context at 4,000 nt, the longest that fit at 7B during pretraining. They state that "the main limitation of such models is their size", and that AIDO.DNA beats prior encoder-only models "without new data", which they read as a sign that new scaling laws are needed for compute-optimal DNA LMs.
- **GUE benchmark (Table 2, MCC).** AIDO.DNA-7B averages **73.33** over all GUE tasks, against 67.75 (DNABERT-2 117M), 66.71 (NT 2.5B), 66.65 (older DNABERT-2 numbers) and 60.69 (DNABERT 89M). Gains are largest on histone marks (average 64.01 vs 58.83 for DNABERT-2) and mouse TF binding (77.37 vs 71.22). On the 10 TF tasks the 7B used **continued MLM on the test-set input sequences** before fine-tuning (marked †). The 300M model was not run on the histone tasks, so it has no overall GUE average.
- **NT benchmark (Table 3, MCC).** Average 72.83 for 7B vs 69.96 (NT v2 500M), 68.98 (NT 2.5B), 69.36 (HyenaDNA 1.8M) and 69.97 (AIDO.DNA 300M). NT v2 still wins on the promoter and splice-acceptor/donor tasks (e.g. promoter-all 97.6 vs 95.08).
- **Zero-shot variant effect (Table 4).** On NT's ClinVar-pathogenic vs gnomAD-benign set, scoring a variant by the max-normalised L2 distance between mean-pooled reference and alternate embeddings over a 1 kb window, AUROC is **0.807 (300M)** and **0.785 (7B)** vs 0.720 for NT 2.5B. The smaller model wins; the authors suggest the 7B embedding has more channels unrelated to pathogenicity.
- **Unsupervised element discovery.** Using the nucleotide-dependency map of Da Silva et al. (log-odds change at nucleotide j when nucleotide i is mutated, computed in O(L) inferences rather than O(L²)), the 7B model reveals promoters, coding regions, TF binding sites, RNA secondary-structure-like pairings and, in one example at KIF26B, a putative minisatellite enhancer and hairpin-like regulator. Many such elements "are revealed only at the largest 7B model scale" (Fig. 3, qualitative).
- **Sample-efficient expression prediction (Table 5).** Fine-tuned on the de Boer et al. 10 M random yeast promoter dataset, Pearson r is 0.802 with all 10 M samples, 0.584 with 1,000 (73% of full performance) and 0.408 with 100 (about half).
- **Directed promoter generation (Table 6).** Fine-tuning with a masked diffusion objective plus a 4.5 M-parameter conditional head (two transformer blocks with a linear expression encoding and a skip connection) gives 0.528 per-base recovery accuracy vs 0.460 unconditional. The authors calculate that a perfect unconditional generator would reach 0.45–0.48 on this scaffolded 80 bp design, so values above that require learning expression-specific grammar. High-expression designs are G-rich; low-expression designs show a noisy alternating TATA motif (Fig. 4).

## Methods / evidence

Data: the original NT multi-species set (812 genomes, 712/50/50 split), minus 17 genomes deleted from NCBI, with *Rattus norvegicus* replaced by its current reference — 696 training, 50 validation, 50 test genomes, chunked into non-overlapping 4 kb segments. Tokenisation: characters A, T, C, G, N plus [CLS]/[EOS]. Architecture: encoder-only transformer with SwiGLU, LayerNorm and rotary position embeddings; 300M = 24 layers × 1,024 hidden, 16 heads; 7B = 32 layers × 4,352 hidden, 32 heads, FFN 11,584. Objective: standard BERT MLM (15% selected; 80/10/10 mask/random/keep), Adam (β = 0.9, 0.95), cosine schedule. Compute: 7B on 256 H100s with Megatron-LM, bf16 and FlashAttention-2, global batch 1,024, 100,000 iterations in 8 days; 300M on 32 A100s for 4 days. Full Megatron configs are in Appendix D. Downstream: full fine-tuning with [CLS] pooling and a linear head (binary cross-entropy for classification, MSE for expression). Code via the ModelGenerator package and Hugging Face (genbio-ai).

Weight: a short benchmark paper with no ablations separating scale from the small architecture changes, no error bars or repeated seeds, and baseline numbers taken from earlier papers. The dependency-map and promoter-motif results are qualitative. (synthesis)

## Limitations

**Authors' own:**
- MLM-trained encoders "are not suitable for complex sequence generation", which is why a separate masked-diffusion fine-tune is needed for design.
- The NT data splits are "highly correlated with taxonomy": most training data are bacteria, fungi and invertebrates. In preliminary reshuffled splits that added mammals, vertebrates and model organisms, performance "dramatically" decreased as more eukaryotes were added; the authors hypothesise that noisy intergenic eukaryotic sequence hurts unsupervised training, and leave this outside the study's scope.
- The 7B model underperforms the 300M model on zero-shot variant effect prediction, attributed to a lower signal-to-noise embedding.

**Reviewer notes:** (at most three, each marked `(synthesis)`)
- The TF results for the 7B model use continued MLM pretraining on the **test-set input sequences** (self-pretraining) before supervised fine-tuning; this is unlabelled transductive training, but the TF gains are not cleanly comparable with baselines that did not get it. (synthesis)
- The scaling claim compares models that differ in tokenisation, architecture and data as well as size; there is no same-recipe size sweep beyond 300M vs 7B, and on several tasks (zero-shot VEP, core promoters, COVID) the 300M model matches or beats the 7B. (synthesis)
- The text gives "796 species" and "796 genomes" but the training set is 696 genomes; and the directed-generation dataset is cited as [39], which is the GRASP GWAS database rather than the de Boer promoter paper [37] used elsewhere. These look like editing slips. (synthesis)

## Surprising or load-bearing bits

- **Training mostly on prokaryotes may help eukaryotic tasks.** The appendix reports that adding more eukaryotic genomes made the model worse in preliminary runs, and argues that "clean", highly constrained prokaryotic genomes teach conservation structure better. This runs against the human-centric data choices of many DNA LMs. (synthesis on the comparison)
- **Bigger is not better for zero-shot VEP.** The 300M model gives the best embedding-distance AUROC; size helps fine-tuned tasks more than frozen-embedding scoring.
- **Single-nucleotide tokens are argued for on biological grounds** — k-mer and BPE "words" dilute single-nucleotide pathogenic effects and local grammars such as codons.
- **The nucleotide-dependency approach turns an MLM into an unsupervised annotator** at O(L) cost, with no labels.

## Concepts touched

- [[dna-language-model]] — a 7B encoder-only MLM at single-nucleotide resolution; argues for parameter scaling over context scaling.
- [[genomic-tokenization]] — character-level tokens (A/T/C/G/N) chosen to keep single-nucleotide and codon-level effects visible.
- [[variant-effect-prediction]] — zero-shot embedding-distance scoring on ClinVar/gnomAD; 300M > 7B > NT 2.5B.
- [[cis-regulatory-element]] — promoter classification, unsupervised element discovery, and expression-conditioned promoter design.
- [[transcription-factor-motif]] — GUE TF-binding tasks and TATA-like motifs in generated low-expression promoters.

## Connections to other sources

- Uses the **Nucleotide Transformer** pretraining data and benchmark: [[dallatorre-2025-nucleotide-transformer]]. NT's successor, [[boshar-2025-ntv3]], takes the opposite bet — long (1 Mb) context plus supervised functional tracks.
- Benchmarked against [[ji-2021-dnabert]], [[zhou-2023-dnabert-2]] (GUE suite) and [[nguyen-2023-hyenadna]]; lists [[schiff-2024-caduceus]], [[fishman-2025-gena-lm]], [[benegas-2025-gpn-msa]], [[zhou-2015-deepsea]], [[kelley-2018-basenji]] and [[avsec-2021-enformer]] in its model catalogue.
- Promoter design here (masked diffusion on an encoder) contrasts with the autoregressive, multi-task design of [[su-2025-atgc-gen]]. (synthesis)

## Open questions

- Does the gain survive a controlled size sweep on fixed architecture, tokeniser and data, with repeated seeds? (synthesis)
- Why does adding eukaryotic genomes hurt? The paper's data-quality hypothesis is untested.
- Would a 4 kb encoder still hold up on tasks that need distal context (enhancer–gene links, 3D contacts), where long-context models such as [[boshar-2025-ntv3]] or [[avsec-2021-enformer]] are designed to win? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[variant-effect-prediction]] · [[dallatorre-2025-nucleotide-transformer]] · [[zhou-2023-dnabert-2]] · [[boshar-2025-ntv3]] · [[40-Topics/sequence-models-and-foundation-models]]
