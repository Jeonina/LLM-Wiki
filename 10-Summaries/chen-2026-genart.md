---
type: summary
title: "Chen et al. 2026 — GenART: Reading the genome's language with adaptive \"words\""
source: "[[00-Sources/papers/GenART_ Reading the genome’s language with adaptive “words”]]"
source_quality: full
source_sha256: "d03e12a2c3126d2e49fa74c443b1328cd5c7beb10f894f62aaf73fd727d2ba13"
source_kind: paper
author: "K. C. (first author; full author names not in the clipping), P. H., Z. L., S. G., X. Y., X. Z., Y. G., Zhiliang Ji, Chen Lin (lead contact)"
published: 2026
ingested: 2026-10-08
doi: "10.1016/j.crmeth.2026.101516"
journal: "Cell Reports Methods"
tags: [GenART, DNA-language-model, tokenization, adaptive-tokenization, learnable-tokenization, Gumbel-softmax, masked-language-model, NT-benchmark, GUE, SpliceAI, genome-annotation, histone-marks, DNA-methylation, MxDNA, SegmentNT, Evo2]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[cpg-island]]", "[[chip-seq]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[histone-modifications]]", "[[computational-methods]]"]
---

**Citation:** Chen et al. (2026) — *GenART: Reading the genome's language with adaptive "words"* — *Cell Reports Methods*. [DOI](https://doi.org/10.1016/j.crmeth.2026.101516)

# Chen 2026 — GenART

> **Clipping note:** the ScienceDirect clipping has the full Results, Discussion, Limitations and STAR Methods, but the abstract, highlights, figures and all tables (Tables S1–S10, including pretraining corpus and hyperparameters) are empty or images. Author names appear only as initials in the contributions statement. Numbers below are those stated in the text.
>
> GenART is a [[dna-language-model]] whose tokenizer is a trainable layer inside the network. Single nucleotides go through Transformer "nucleotide encoder" layers, then an adaptive tokenizer (five parallel CNNs with kernels 2–6, an MLP boundary score, Gumbel-softmax merge/split decisions) mean-pools runs of bases into variable-length tokens, which a second Transformer stack encodes. A cross-attention decoder maps token states back to bases for the MLM loss. The tokenizer keeps training during fine-tuning, and an optional "refining" loss lets the user steer token density and boundary clustering per task. At 350 M and 1 B parameters it reports the best average on the NT benchmark (+3.41% over the best baseline) and on 15 GUE tasks (+1.22%), and its boundaries recover 62.9% of GENCODE feature boundaries without supervision.

## Key claims

- **Benchmarks.** On the 18 NT tasks, GenART-1B was best on 15 and GenART-350M on 12. On three promoter tasks both scored 0.971 vs 0.974 for Evo2-7B. On 15 GUE tasks not in NT (TF binding in human and mouse, core promoters, COVID variant, splice sites), GenART was best on 8 and second on 6, trailing Evo2-7B or NT-multi-2.5B by 1.1–1.3%.
- **Long-context splicing.** Against SpliceAI at 400 nt, 2 kb and 10 kb context, GenART had higher top-k accuracy at every length (0.962 vs 0.950 at 10 kb) and near-perfect PR-AUC throughout.
- **Tokenizer ablation.** Replacing the adaptive tokenizer with single-nucleotide tokens in GenART-350M (everything else fixed) lowered the average by 3.27% across both benchmarks, with the largest effect on histone marks (+9.35% for adaptive). Core-promoter tasks were already saturated (>0.96) with single nucleotides.
- **Representations.** t-SNE of final-layer embeddings from pretrained, not fine-tuned, models separated functional categories for GenART but not for baselines. Token-frequency profiles for enhancer vs splice-site sequences were nearly identical under overlapping/non-overlapping k-mers, BPE and MxDNA, but distinct under GenART.
- **Species diversity, controlled.** At fixed steps and matched token count, a multispecies corpus cost 1.45% on human tasks, gained 2.87% on non-human tasks (yeast, mouse, virus), and gave a net +0.98%.
- **Scaling.** Performance rose from 100 M to 350 M to 1 B. Attention became more uniform (lower coefficient of variation) with size, and average token length *decreased* with model size.
- **Task-steered tokenization.** Grid search over target token density ρ and cluster factor c_f on eight histone tasks found sharp-peak marks prefer high density and clustering (H3K4me3: mean ρ 0.626, c_f 0.709; MCC 0.628 → mean 0.636, max 0.650) and broad-domain marks prefer low values (H3K79me3: ρ 0.185, c_f 0.266; MCC 0.743 → mean 0.749, max 0.757).
- **Unsupervised genome annotation.** On GRCh38.p14 vs GENCODE v49, merged tokens (≥3 bp) recovered 10.27 M of 16.32 M boundaries (recall 0.629, ±1 bp), highest for CDS (0.662), start codons (0.657) and exons (0.640), lower for CpG islands (0.534) and enhancer/promoter regions (0.523). Length-1 tokens recalled about 0.8 of known methylated sites from 218 human methylation datasets (per chromosome 0.77–0.92). Under boundary-level MCC, supervised SegmentNT beat GenART on most features, and GenART beat DNABERT-2, MxDNA and fixed 6-mer NT.

## Methods / evidence

Architecture: pre-LayerNorm Transformer blocks with FlashAttention, grouped-query attention and RoPE on both sides of the tokenizer. Boundary score for the gap between bases i and i+1 is the sum of per-base MLP scores, turned into split/merge logits and sampled by Gumbel-softmax (τ = 1.0). Pretraining: BERT-style 80/10/10 masking of nucleotides, MLM loss plus an auxiliary length loss. Refining: λ = 0.1 times an MSE between predicted boundaries and a target pattern; a uniform pattern sets density, and a Gaussian-smoothed noise pattern thresholded at density ρ adds clustering. Evaluation: NT benchmark with 10-fold CV for hyperparameters and fixed held-out tests; GUE with fixed splits and three seeds. Compute: 8 A800 GPUs; about 50 GPU-hours (350 M) and 70 GPU-hours (1 B) of pretraining. Code and checkpoints: github.com/XMUDM/GenART.

Weight: a peer-reviewed methods paper with a controlled tokenizer ablation and a controlled species-diversity ablation, which few DNA LM papers do. The pretraining corpus and all per-task numbers are in tables that were not captured. It is unclear from the text whether baseline numbers were re-run or copied, except that GUE baselines used fixed hyperparameters. The authors declare using Gemini 3.1 and ChatGPT-5 for language editing.

## Limitations

**Authors' own:**
- Many *de novo* "words" have no known biological function and need experimental validation.
- Context tops out around 10 kb; megabase-scale 3D contacts and large SVs are out of reach for the Transformer.
- Genome annotation uses a simple heuristic that merges bases to ≥3 bp by tokenizer logits.
- **Zero-shot variant-effect prediction is near random**: a point mutation shifts the dynamic chunk boundaries, so reference and alternate embeddings are misaligned and embedding distances become noise.

**Reviewer notes:**
- The Results say "we randomly mask certain tokens", while Methods say nucleotides are masked. Methods are the more specific source. (synthesis)
- Boundary recall at ±1 bp rewards dense segmentation; recall without precision is weak evidence, and the ≥3 bp merge only partly controls for this. SegmentNT, which is supervised, still wins on MCC. (synthesis)
- The 0.8 recall for methylated sites using length-1 tokens may largely reflect where CpGs are, since the curated set comes from CpG-focused assays (arrays, RRBS, WGBS); the paper gives no CpG-matched null. (synthesis)

## Surprising or load-bearing bits

- **Bigger model, shorter tokens.** Token length falls as capacity grows, which suggests the tokenizer compresses to make up for limited capacity, not because DNA has fixed "words". (synthesis)
- **Token granularity tracks histone-mark shape.** Sharp-peak marks want dense, clustered boundaries; broad-domain marks want sparse ones. The gains are small (+0.006 to +0.008 mean MCC).
- **Dynamic tokenization trades off zero-shot VEP.** Both GenART and DNAChunker show weak zero-shot variant scoring, which points to a general weakness of learned segmentation. (synthesis)

## Concepts touched

- [[genomic-tokenization]] — trainable, task-tunable segmentation; ablation against single-nucleotide input.
- [[dna-language-model]] — hierarchical nucleotide → token Transformer at 100 M–1 B.
- [[variant-effect-prediction]] — explicit failure mode for zero-shot VEP under dynamic tokens.
- [[cpg-island]] — CpG-island boundaries recovered at recall 0.534.
- [[chip-seq]] / [[histone-modifications]] — sharp-peak vs broad-domain marks guide refining parameters.

## Connections to other sources

- Closest relative: [[kim-2026-dnachunker]] — also learns chunk boundaries inside an MLM (cosine-similarity router vs GenART's CNN + Gumbel-softmax), also reports weak zero-shot variant scoring. (synthesis)
- Baselines named: [[ji-2021-dnabert]], [[zhou-2023-dnabert-2]], [[dallatorre-2025-nucleotide-transformer]], [[nguyen-2023-hyenadna]]; supervised segmentation comparator [[dealmeida-2025-segmentnt]].
- Fixed-vocabulary alternatives in this batch: [[chen-2023-genomicbert]] (Unigram) and [[medvedev-2025-biofm]] (variant-aware tokens). (synthesis)

## Open questions

- Does GenART beat a single-nucleotide model of equal compute on long-range tasks beyond splicing? (synthesis)
- Can a boundary-aligned scoring scheme recover zero-shot VEP for dynamic tokenizers? (synthesis)
- Do the de novo "words" match known motif families (JASPAR), as DNAChunker tested? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[kim-2026-dnachunker]] · [[dealmeida-2025-segmentnt]] · [[40-Topics/sequence-models-and-foundation-models]]
