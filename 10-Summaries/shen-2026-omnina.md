---
type: summary
title: "Shen et al. 2026 — A foundation model for nucleotide sequences"
source: "[[00-Sources/papers/A foundation model for nucleotide sequences]]"
source_quality: full
source_sha256: "86fc4e4d3095c7721be92599ecb2c160353e25c7575d8a215d7fb9639eb88b1e"
source_kind: paper
author: "Xilin Shen, Jia Xin Li, Meng Yang, Lei Shi, Kexin Chen, Xiangchun Li (study lead)"
published: 2026-03-19
ingested: 2026-10-08
doi: "10.1093/nar/gkag083"
journal: "Nucleic Acids Research 54(6):gkag083"
tags: [OmniNA, dna-language-model, sequence-text, annotation-aware, decoder-only, LLaMA, autoregressive, BPE, NCBI-nt, multitask, question-answering, variant-effect, CRISPR-off-target, cfRNA, microbiology]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[cis-regulatory-element]]", "[[chromatin-accessibility]]", "[[cpg-island]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Shen et al. (2026) — *A foundation model for nucleotide sequences* — *Nucleic Acids Research* 54(6):gkag083. [DOI](https://doi.org/10.1093/nar/gkag083)

# Shen 2026 — OmniNA

> OmniNA is a **LLaMA-style decoder-only language model pretrained on nucleotide sequences paired with their free-text NCBI annotations** (organism, taxonomy, gene and product names, function). The pretraining corpus is the NCBI nt database up to April 2023: 91.7 million sequences (200–3,000 bp after truncation), 1,076.2 billion bases and 197 million annotation words. A shared BPE tokenizer covers both DNA and English text. Three sizes (66M, 330M, 1.7B) are trained by next-token prediction, then fine-tuned in a **question-answering format** (instruction + sequence + question → text answer) on 23 tasks spanning human regulatory elements, splicing, chromatin, methylation, ClinVar variants, CRISPR off-target, virus and bacterial taxonomy, and a cfRNA cancer classifier. At inference only the sequence is given. The claim is that annotation-aware pretraining gives better representations and multitask transfer than sequence-only DNA LMs.

## Key claims

- **Generation quality scales with size.** On annotation generation, OmniNA-1.7B reaches F1 0.66 (genomic type), 0.24 (species, 172 classes) and 0.59 (enzyme, 104 classes); larger models also generate more diverse, more reproducible and more truncation-stable annotations.
- **Layer-specific representations.** Different transformer layers of OmniNA-1.7B best separate different properties (by ARI after Louvain clustering): layer 2 separates GERP-conserved vs non-conserved human sequences and bacterial classes from 16S; layer 3 superkingdoms; layer 8 SARS-CoV-2 clades; layer 20 CpG content; layer 23 non-B DNA structures and genomic element types; layer 17 RNA functional elements.
- **Beats sequence-only LMs on representation tasks.** OmniNA-1.7B outperforms DNABERT-2, Nucleotide Transformer v2 and HyenaDNA on all 11 representation (clustering) tasks (Supp. Fig. S6I–J; numbers in a supplementary table not in the clipped text).
- **Robust to noisy annotations, but not immune.** Taxonomic ARI of sequence embeddings falls from 0.18 (correct annotations) to 0.12 (shuffled) and 0.09 (sparse).
- **23 fine-tuned tasks.** OmniNA "generally achieved better F1 scores than benchmark methods": F1 0.88 (PAS), 0.97 (TIS), 0.98 (splice sites), 0.98 (Cas13d gRNA off-target), median 0.73 across TF-binding targets, and it surpasses Enformer, Sei and ExPecto on chromatin accessibility and histone tasks as reformulated here. Human DNA element detection is "comparable or superior" to task-specific tools. Non-B DNA classification reaches Accuracy@1 0.78.
- **Pathogenic variants vs EVE.** Fine-tuned per gene on ClinVar/1000 Genomes SNVs (1 kb windows), OmniNA-1.7B has mean F1 0.90 vs 0.81 for EVE across 48 shared genes (two-sided t-test p = 0.011), winning in 27 of 48. Synonymous-variant classification over 24 genes reaches mean F1 0.68.
- **Mutation-effect scoring.** Log-likelihood differences from fine-tuned heads track pathogenic/benign odds ratios at PAS and TIS loci (Pearson r = 0.92 for both), correlate with measured Cas13d gRNA position effects (r = 0.65), and are higher in BRCA1 and CHD7 protein-domain regions than elsewhere (p < 1e−5).
- **Microbiology and liquid biopsy.** Bacteriophage host (12-way) Accuracy@1 0.73; eukaryotic-virus host Accuracy@1 0.78; antibiotic-resistance mechanism Accuracy@1 0.59; virulence gene type Accuracy@1 0.93; pancreatic cfRNA tumour vs normal "near-perfect" (all metrics ≈1.0).
- **Few-shot and cross-species.** On histone occupancy, 1.7B performs similarly with 75% and 100% of training data; a model fine-tuned on human elements performs comparably to mouse-specific baselines on mouse elements.

## Methods / evidence

Data: NCBI nt FASTA plus annotations; sequences <200 bp or with ≥2 consecutive Ns removed, longer ones cut to 3,000 bp by sliding window; 98/1/1 split; prompt = instruction + sequence + annotation. Annotation text was parsed into 20 token categories. Tokenizer: SentencePiece BPE trained on nucleotide sequences and WikiText-103, vocabulary 32,001; max input 601 tokens. Model: LLaMA (RMSNorm, SwiGLU, RoPE); 66M, 330M and 1.7B (2,048-dim embeddings); AdamW, lr 1e−4, batch 2,048, 200,000 steps on one 8×A100 DGX. Fine-tuning: 2 epochs per multitask set, loss only on answer tokens. Baselines are task-specific tools (PromID, iEnhancer-DEEP, DeepSilencer, MPRA-DragoNN, DeepSTARR, DeepGSR, SpliceRover, TIGER, Enformer, Sei, ExPecto, EVE, DeePaC, DeepMicrobes) and three DNA LMs for representation only. Ten classification metrics are reported. Several equations (attention, autoregression, loss, effect score) are missing from the clipped text. Code at github.com/xilinshen/OmniNA.

Weight: a broad, many-task paper whose comparisons are mostly against older task-specific models, often after converting regression outputs to classification. Most results are F1 scores in figures and supplementary tables; direct fine-tuning comparisons against other DNA LMs on the same 23 tasks are not shown in the main text. (synthesis)

## Limitations

**Authors' own:**
- Performance scales with model and data size, and both would need to grow.
- Annotation quality affects representations; shuffled or sparse annotations degrade taxonomic ARI ("resilience but non-negligible degradation").
- Possible overlap between OmniNA test sequences and the undisclosed training sets of baselines (Enformer, Sei, ExPecto) cannot be ruled out; the authors argue this would favour the baselines.
- For regression baselines (MPRA-DragoNN, Enformer, ExPecto), cutoffs chosen from training-data AUC were used to convert them to classifiers, which "could introduce evaluation biases".
- Domain-specific annotations in pretraining could bias generalisation.
- Input is limited to ~3,000 bp, so distal enhancer–promoter and 3D effects are not modelled.

**Reviewer notes:** (at most three, each marked `(synthesis)`)
- The Methods describe a causal decoder but state that "attention in the transformer is bidirectional", and give a mean-squared-error loss for next-token prediction; the Zenodo DOI cited is actually a bioRxiv DOI (10.1101/2024.01.14.575543). These descriptions look partly templated and leave the exact training objective unclear. (synthesis)
- The pretraining corpus (NCBI nt) contains many of the benchmark sequences (e.g. viral genomes, 16S, ClinVar genes) together with their annotations; the paper does not report deduplication between pretraining data and downstream test sets, so taxonomy and virus tasks may be partly memorised. (synthesis)
- Task counts are inconsistent: eukaryotic-virus host prediction is called 15-way in Results but uses 144 host taxa in Methods; and the near-perfect cfRNA result rests on a single GEO series (GSE136651) without an external cohort. (synthesis)

## Surprising or load-bearing bits

- **Text as weak supervision.** Unlike almost all DNA LMs, OmniNA trains on sequence and natural-language metadata in one token stream, closer to a nucleotide "captioning" model. It is the main example in this batch of sequence–text co-training. (synthesis)
- **Different biology lives in different layers**, from conservation (layer 2) to non-B structure (layer 23) — useful if OmniNA embeddings are used as frozen features.
- **High precision, lower recall** is presented as a design feature: the authors pitch OmniNA as a first-pass screening tool where false positives are costly.
- **cfRNA patient classification** from random 30 bp fragments is one of the few liquid-biopsy-style tasks in the DNA-LM literature. (synthesis)

## Concepts touched

- [[dna-language-model]] — a decoder-only DNA+text LM fine-tuned as a question-answering model.
- [[genomic-tokenization]] — a single BPE vocabulary shared by nucleotides and English words.
- [[variant-effect-prediction]] — per-gene ClinVar classification vs EVE; log-likelihood effect scores at PAS/TIS, gRNA and protein domains.
- [[cis-regulatory-element]] — promoter, enhancer, silencer and insulator detection tasks.
- [[chromatin-accessibility]] — 114 ENCODE ATAC/DNase profiles across 89 cell lines as binary peak tasks.
- [[cpg-island]] — CpG-content bins separated best by layer 20; a methylated-region task covers 39 human cell types.

## Connections to other sources

- Representation baselines: [[zhou-2023-dnabert-2]], [[dallatorre-2025-nucleotide-transformer]], [[nguyen-2023-hyenadna]].
- Chromatin-task baselines: [[avsec-2021-enformer]], [[chen-2022-sei]], [[zhou-2018-expecto]]; the 1–4 kb context argument leans on [[zhou-2015-deepsea]] and Sei.
- Contrast with sequence-only scaling at short context in [[ellington-2024-aido-dna]], and with 1 Mb context in [[boshar-2025-ntv3]]. (synthesis)
- Conditional text-like control of DNA generation also appears in [[su-2025-atgc-gen]], which conditions on property tags rather than free text. (synthesis)

## Open questions

- How much does the text channel actually help? There is no ablation that pretrains the same model on sequences alone and compares downstream fine-tuning. (synthesis)
- Would the 23-task results hold against current DNA LMs fine-tuned under the same QA protocol, not only against older task-specific models? (synthesis)
- Is there overlap between NCBI nt pretraining sequences and test sequences in the virus, bacterial and ClinVar tasks? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[variant-effect-prediction]] · [[zhou-2023-dnabert-2]] · [[su-2025-atgc-gen]] · [[40-Topics/sequence-models-and-foundation-models]]
