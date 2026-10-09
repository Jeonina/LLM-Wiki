---
type: summary
title: "Lin et al. 2026 — Genos: a human-centric genomic foundation model"
source: "[[00-Sources/papers/Genos_ a human-centric genomic foundation model]]"
source_quality: full
source_sha256: "e3559b511773c3331318c25ab9a5040b02dea45746c096f4a8f0d8a3a681c7fc"
source_kind: paper
author: "Adi Lin, Bin Xie, Cheng Ye, Cheng Wang, Duoyuan Chen, Ercheng Wang, … (≈60 authors, BGI-Hangzhou AI; author list alphabetical, no lead contact stated)"
published: 2026-01
ingested: 2026-10-08
doi: "10.1093/gigascience/giaf132"
journal: "GigaScience 14 (2026), giaf132"
tags: [Genos, DNA-language-model, mixture-of-experts, MoE, long-context, 1Mb-context, RoPE, grouped-query-attention, Megatron-LM, HPRC, HGSVC, pangenome, single-nucleotide, RNA-seq-prediction, AlphaGenome, Evo2, KEGG, Bioreason, multimodal, BGI]
entities: []
concepts: ["[[dna-language-model]]", "[[sequence-to-function-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[highly-repetitive-regions]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Lin et al. (2026) — *Genos: a human-centric genomic foundation model* — *GigaScience* 14:giaf132. [DOI](https://doi.org/10.1093/gigascience/giaf132)

# Lin 2026 — Genos

> Genos (BGI-Hangzhou AI) is a pair of mixture-of-experts DNA language models (1.25B total / 0.33B activated, and 10.27B / 2.87B) trained by next-token prediction at single-nucleotide resolution with a context window of up to 1 Mb. Its two stated arguments are **human-centric data** — 636 high-quality assemblies from HPRC release 2, HGSVC, CEPH plus GRCh38 and CHM13, rather than Evo2's cross-species corpus — and **deployability**: MoE routing (2 of 8 experts per token), grouped-query attention, FlashAttention, RoPE with a base frequency of 50,000,000, and five-dimensional parallelism in Megatron-LM, so that long-context inference does not need an Evo2-40B-scale cluster. Benchmarks are run as frozen-embedding probes against a fixed downstream head; two case studies fine-tune the model for single-base RNA-seq track prediction and pair it with a text LLM for KEGG-based disease classification.

## Key claims

- **Human pangenome corpus.** 231 haplotype-resolved HPRC release-2 assemblies, 65 HGSVC assemblies, 21 CEPH genomes and 2 references (GRCh38, CHM13) — 636 genomes in total. One-hot tokenizer over A/T/C/G/N plus special tokens; no epigenetic or cell-type labels at pre-training.
- **Two-stage curriculum with a deliberate filtering reversal.** Pre-training (~1,400B tokens) used progressively longer windows (8,192 / 32,768 / 131,072 / 1,024,000 bp in roughly 3:3:3:1 proportion), with a quarter of samples reverse-complemented, and excluded sequence more than 5,120 bp (8-kb fragments) or 10,240 bp (32-kb fragments) from gene boundaries. Continued pre-training added ~2,600B tokens with **all distance filtering removed**, deliberately exposing the model to distal intergenic regions, segmental duplications and transposable elements.
- **Architecture.** 12 layers, 16 attention heads over 8 KV groups, 8 experts with 2 selected per token, SwiGLU, three RMSNorm layers, MoE auxiliary load-balancing loss (1e-3) and router Z-loss (1e-3) to stop router collapse under a 4-letter vocabulary. Trained on 256 GPUs, global batch 1,024, AdamW, cosine schedule peaking at 1e-4, BF16 with FP32 kept for attention softmax, gradient accumulation/all-reduce and MoE routing. The 1.2B model saw 1,600B tokens and the 10B model 2,200B.
- **Short-sequence benchmarks (AUC, frozen embeddings + fixed head).** Genos-10B leads on coding-vs-intergenic (0.9914 against GENERator-3B 0.9855, Evo2-40B 0.9886, NT-2.5B 0.9763) and H3 (0.9400). Genos-1.2B leads human enhancers Cohn (0.8715 against Evo2-7B 0.7733, NT-2.5B 0.7873). Genos is behind on splice sites (10B 0.7990 against Evo2-40B 0.9138, NT-2.5B 0.8603) and H3K36me3 (0.7658 against Evo2-40B 0.8823).
- **Mutation-hotspot classification (Chinese Pangenome Consortium data, Poisson right-tail test at FDR < 0.05).** Genos-10B is best at every length: 0.9522 at 8 kb, 0.9625 at 32 kb and 0.9911 at 128 kb, against GENERator-3B 0.9315 / 0.9237 / 0.9620 and HyenaDNA-1M 0.8914 / 0.9064 / 0.9735. Evo2 could not run 128-kb inference under HuggingFace, and NT cannot exceed 6 kb. Accuracy rising with input length is the paper's main evidence that longer context helps.
- **Long-range benchmark (LRB at 8 kb).** Genos-10B gives 0.7532 (enhancer), 0.9249 (promoter) and 0.9326 on pathogenic ClinVar, the last well above GENERator-3B (0.7206), HyenaDNA-1M (0.6117) and Evo2-7B (0.7308) and slightly above Evo2-40B (0.9167). On causal eQTL, Genos trails: 1.2B 0.6990 and 10B 0.6773 against Evo2-40B 0.7054.
- **RNA-seq track prediction (case study).** Genos-1.2B was fully fine-tuned with a three-layer dilated 1-D convolutional head on 667 ENCODE and GTEx metadata groups of single-base RNA-seq, in 32-kb windows with 16-kb overlap, using AlphaGenome-style square-root clipping and MSE loss. log1p Pearson correlations in GM12878 were 0.9335 (whole genome, + strand), 0.9334 (gene region) and 0.8641 (gene expression); in natural killer cells 0.9084 / 0.9036 / 0.9267 on the + strand and 0.8562 / 0.8542 / 0.8969 on the −. A preliminary Genos-10B fine-tune, limited to chromosome 19, is said to beat AlphaGenome (supplementary only).
- **Genome–text fusion (case study, Bioreason KEGG task: 1,449 entries, 37 diseases, 8:1:1 split, DNA ≤1,024 bp, frozen DNA model + LoRA on the text model).** Genome-only accuracy: Genos-10B 92.07%, Genos-1.2B 91.72%, Evo2-1.2B 88.28%, NT-2.5B 86.55%, HyenaDNA-1M 50.00%. Best genome–text pairing: Genos-1.2B + 021-8B at 98.28% accuracy and 90.37% macro F1, just above Evo2-1.2B + 021-8B (97.59%) and HyenaDNA-1M + Qwen3-8B (97.58%, which has the highest macro F1 at 95.61%).

## Methods / evidence

All benchmark tasks feed the model's output embeddings into one fixed, simple downstream network, which makes the comparison about representation quality rather than fine-tuning budget. Tasks are drawn from Genomic Benchmarks (3 human tasks), the NT benchmark (splice sites, H3, H3K36me3) and LRB (4 tasks regenerated at 8,192 bp), scored by AUC or macro-AUC, with chromosome 22 held out for validation on LRB. Weights, inference code and documentation are released on GitHub (`BGI-HangzhouAI/Genos`) and HuggingFace.

Weight: the engineering account (MoE load balancing under a 4-letter vocabulary, mixed-precision rules, the two-stage data curriculum) is unusually concrete and is the paper's stated contribution — it calls itself a technical blueprint and benchmark. The biological evidence is thinner: only about a dozen benchmark tasks, two case studies, no ablation separating the human-centric corpus from the architecture, and the headline AlphaGenome comparison confined to one chromosome in the supplement. Figures and the supplementary file are images or links in the clipping, so values not stated in the text could not be read.

## Limitations

**Authors' own:**
- Training and inference cost still needs optimisation for very large datasets.
- Cross-modal fusion is preliminary; proteomics, metabolomics and phenotype data are not integrated.
- No broad tissue-level benchmark of RNA expression or chromatin accessibility across GTEx or ENCODE contexts; this is named as future validation work.
- The 10B genome-wide RNA-seq fine-tune is incomplete, so the main text reports the 1.2B results.

**Reviewer notes:**
- Nothing isolates the human-centric data claim: no model is trained on the same architecture with a cross-species corpus, so the gains over Evo2 cannot be attributed to the pangenome data. (synthesis)
- The Conclusion cites "accuracy rates reaching up to 99.31%" for the diagnosis case, a figure that appears nowhere in Table 4 (best shown is 98.28%). (synthesis)
- On the KEGG task HyenaDNA-1M goes from 50% alone to 97.58% paired with Qwen3-8B, and the best macro F1 belongs to a HyenaDNA pairing, which suggests the text model carries most of that task and limits what it says about the DNA encoder. (synthesis)

## Surprising or load-bearing bits

- **Filter early, unfilter late.** Gene-proximal filtering during pre-training followed by unfiltered continued pre-training is an explicit answer to the trade-off that GENERator resolves by filtering throughout; the two papers reach opposite conclusions about intergenic sequence. (synthesis)
- **MoE in a 4-letter vocabulary.** With only four input symbols, router collapse is a real risk, handled with an auxiliary load-balancing loss and a Z-loss. This is a genomics-specific wrinkle of applying MoE.
- **Accuracy rising with context on mutation hotspots** (0.952 → 0.963 → 0.991 from 8 kb to 128 kb) is one of the few direct demonstrations in this batch that a model actually benefits from more context, though on a task defined by mutation density over the window. (synthesis)
- **Variant-effect split**: strong on pathogenic ClinVar (0.9326) but behind Evo2 on causal eQTL (0.6773), so coding/constraint signal transfers better than regulatory signal.

## Concepts touched

- [[dna-language-model]] — MoE decoder with 1-Mb context, trained on human pangenome assemblies.
- [[sequence-to-function-model]] — fine-tuned to single-base RNA-seq tracks with an AlphaGenome-style objective and preprocessing.
- [[genomic-tokenization]] — single-nucleotide one-hot vocabulary, no k-mers or BPE.
- [[variant-effect-prediction]] — LRB pathogenic-ClinVar and causal-eQTL probes, plus the KEGG variant-to-disease case study.
- [[highly-repetitive-regions]] — segmental duplications and transposable elements deliberately reintroduced in continued pre-training.

## Connections to other sources

- Positions itself against Evo2 (no summary here) and [[avsec-2026-alphagenome]], naming both as the state of the art and criticising their species coverage and cost; the RNA-seq case study copies AlphaGenome's data scaling.
- Benchmarked against [[li-2026-generator]] (GENERator-3B), [[nguyen-2023-hyenadna]] and [[dallatorre-2025-nucleotide-transformer]].
- Opposite data choice to [[li-2026-generator]], which trains only on gene-centric regions and argues intergenic sequence degrades representations; Genos removes that filter in its second stage. (synthesis)
- Shares the MoE-plus-attention direction with [[duan-2025-janusdna]], though Genos is unidirectional and roughly three orders of magnitude larger. (synthesis)

## Open questions

- Does the human pangenome corpus itself help, or is the gain architectural and scale-driven? No ablation is reported.
- Is the AlphaGenome comparison reproducible genome-wide? Only chromosome 19 was fine-tuned for the 10B model.
- Why does Genos lag on splice sites and causal eQTL while leading on pathogenic ClinVar and hotspots? (synthesis)

## Related

- [[dna-language-model]] · [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[li-2026-generator]] · [[avsec-2026-alphagenome]] · [[40-Topics/sequence-models-and-foundation-models]]
