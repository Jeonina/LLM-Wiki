---
type: summary
title: "Fishman et al. 2025 — GENA-LM: a family of open-source foundational DNA language models for long sequences"
source: "[[00-Sources/papers/GENA-LM_ a family of open-source foundational DNA language models for long sequences]]"
source_quality: full
source_sha256: "aec88c254b36ceb42d6fe18e6145136a654e1f8befd94b1ade964b8ea89cf763"
source_kind: paper
author: "Veniamin Fishman, Yuri Kuratov (joint first), Aleksei Shmelev, Maxim Petrov, Dmitry Penzar, Denis Shepelin, … Olga Kardymon, Mikhail Burtsev (supervisors)"
published: 2025-01-15
ingested: 2026-10-08
doi: "10.1093/nar/gkae1310"
journal: "Nucleic Acids Research 53(2):gkae1310"
tags: [GENA-LM, DNA-language-model, BERT, BigBird, sparse-attention, recurrent-memory-transformer, RMT, BPE, T2T, 1000-genomes, masked-language-modeling, promoter, splice-site, DeepSEA, species-classification, integrated-gradients, ClinVar, AIRI]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[transcription-factor-motif]]", "[[de-novo-motif-discovery]]", "[[convolutional-neural-network]]", "[[chip-seq]]", "[[transposable-elements]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[histone-modifications]]", "[[computational-methods]]"]
---

**Citation:** Fishman et al. (2025) — *GENA-LM: a family of open-source foundational DNA language models for long sequences* — *Nucleic Acids Research* 53(2):gkae1310. [DOI](https://doi.org/10.1093/nar/gkae1310)

# Fishman 2025 — GENA-LM

> GENA-LM is a family of encoder-only, BERT-style DNA language models from AIRI, pre-trained with masked language modelling on the human T2T assembly (optionally augmented with 1000 Genomes SNPs and multispecies genomes). Two design choices stretch the input: **byte-pair-encoding (BPE) tokens** (median 9 bp, so 512 tokens ≈ 4.5 kb) and **sparse attention** (4,096 tokens ≈ 36 kb). A **recurrent memory transformer (RMT)** added at fine-tuning or pre-training chains 4.5-kb segments through memory tokens to reach 16–50 kb and beyond. Across promoter, splice-site, DeepSEA chromatin-profile and the 18-task Nucleotide Transformer benchmark, GENA-LMs are at or near the top, but no single variant wins everywhere, and the right trade-off between parameter count and context length depends on the task.

## Key claims

- **BPE tokens buy context.** BPE with a 32,000-token vocabulary yields tokens of 1–64 bp with a median of 9 bp. 512 non-overlapping tokens cover about 4.5 kb, against 512 bp for 512 overlapping 6-mers. The longest tokens often correspond to LINEs or simple repeats. The cost is token-level, not base-level, resolution, which the authors list as a limitation.
- **Model family.** BERT-12L (110M) and BERT-24L (336M) full-attention models with 512 tokens; BigBird-style sparse models (DeepSpeed or HuggingFace sparse attention, some with RoPE) with 4,096 tokens (~36 kb); taxon-specific models for yeast (142 strains), *Arabidopsis* (32 ecotypes) and *Drosophila* (298 species); and a multispecies model. Human-only training data total ≈480 × 10⁹ bp; multispecies ≈1,072 × 10⁹ bp.
- **DeepSEA chromatin profiles (919 targets, ROC AUC).** On 1-kb inputs the best GENA-LM reached 96.81 for TF binding and 92.8 for DHS, against BigBird's 96.1 and 92.3 on 8 kb. Extending context to 8 kb mainly helped histone marks (HM AUC 89.71 vs 86.64 at 1 kb; DeepSEA 85.6; BigBird 88.70), and the gain came from **broad marks** rather than narrow ones. TF and DHS gained only marginally.
- **Promoters (EPDnew, F1).** At 300 bp DNABERT beat GENA-LM (93.26 vs 90.62). At 2 kb they tied (DNABERT 94.28 vs bert-large-t2t 94.16, Wilcoxon P = 0.0625), both above DNABERT-2 (92.98). Larger models beat smaller; multispecies pre-training did not help human promoters.
- **Splice sites (SpliceAI data, 15-kb input).** SpliceAI (a task-specific CNN) slightly beat GENA-LM (mean PR AUC 0.960 vs 0.947). Long-context BigBird variants beat the larger 4.5-kb BERT-large here, so context mattered more than parameters.
- **Nucleotide Transformer 18-task benchmark (MCC, 300–600-bp inputs).** gena-lm-bert-large-t2t had the highest average (0.707) against HyenaDNA-1kb (0.693), NT-Multispecies-v2 500M (0.691), NT-Multispecies 2.5B (0.690) and DNABERT-2 (0.668), with about 330M vs 2,500M parameters. It was weaker on the splice tasks (0.91–0.92 vs 0.96–0.97 for NT).
- **RMT extends context.** bert-large-t2t + RMT (10 memory tokens per ~4.5-kb segment) on 16-kb promoters and 15-kb splice sites beat every other GENA-LM, including sparse ones (Wilcoxon P ≤ 0.043). On HyenaDNA's five-mammal species benchmark, RMT + bert-base-t2t reached 99.24 at 32 kb (HyenaDNA 93.4) and 99.67 at 50 kb, above HyenaDNA's accuracy at 1 Mb. Pre-training with RMT helped splice sites by ~0.5 points but not promoters.
- **MLM accuracy does not need >4 kb.** RMT raised MLM accuracy for the base model, but the large model without RMT scored better, and extending it with RMT did not improve MLM. The authors conclude that long-range dependencies beyond 4 kb are not needed for masked-token prediction but matter for downstream tasks.
- **Attribution recovers motifs.** Integrated Gradients on the DeepSEA-tuned sparse model highlighted tokens containing the ATF1 (TGACG), GATA2 (AGATAAG) and GC-rich CTCF motifs in K562. FIMO-scored motifs had higher token importance, and XSTREME on important tokens lacking a FIMO hit still recovered CTCF and GATA2 motifs, which the authors read as variant motifs that a PWM misses. GATA2 motifs were enriched in tokens important for ATF1.
- **Histone-mark determinants.** Important tokens for H3K4me1 carried GATA, JUN and FOSL motifs. For H3K27me3 in K562 they carried non-blood motifs (SNAI2, ASCL1), which the authors interpret as lineage-repressed targets, not causal writers. For H3K9me3 they carried ZNF274.
- **Variant effects.** A promoter-model log-odds difference separated pathogenic from benign ClinVar promoter SNVs with AUC 0.66 and AP 0.59. Pathogenic variants were enriched ~2.5-fold in the top-1% most important tokens (P < 1e-15). *In silico* saturation mutagenesis (±20 bp around splice sites) showed that changes in canonical splice motifs almost always abolished the predicted site.
- **Cross-species transfer.** A human promoter model scored F1 ≈ 0.95 on macaque, mouse, rat and dog; ~0.85 on chicken and zebrafish; ~0.7 on fly and *C. elegans*. A human H3K27ac model fell to F1 ≈ 0.4 in *Hydra*. Taxon-specific pre-training improved promoter prediction in yeast, fly and *Arabidopsis* by 2–7 points over the human model; the multispecies model improved 5 of 6 experiments by 0.2–1.5 points.
- **Embeddings encode phylogeny without fine-tuning.** Gradient boosting on frozen embeddings separated 27 species; accuracy rose with input length and divergence time (F1 ≈ 0.7 at ≤20 MYA; >0.8 at 60–100 MYA with long inputs; near-perfect at ≥200 MYA). Intermediate layers (around 9–12) gave the best embeddings, with a slight drop at the final layers.

## Methods / evidence

Pre-training: MLM with 15% masking (80/10/10 BERT scheme), 1–2 M steps, batch 256, 8–16 A100 GPUs, AdamW, LR 1e-4. Held-out chromosomes 22 and Y (early models) or 7 and 10 (t2t models). Sentences of 500–1,000 bp grouped into 50–100-sentence documents, reverse-complement augmentation, and haplotype-preserving 1000G SNP substitution. Fine-tuning: a single linear head on CLS (sequence tasks) or on all tokens (splice sites); whole model fine-tuned. Benchmarks: DeepSEA, EPDnew promoters (300 bp, 2 kb, 16 kb), SpliceAI data, DeepSTARR enhancers and APARENT polyadenylation (Supplementary Note 1, not in the clipping), the NT 18-task set, and a reconstructed HyenaDNA species task. Most tables report averages of at least three runs. Code, models (HuggingFace `AIRI-Institute/gena-lm-*`) and a web service (GENA-Web, inputs up to 1 Mb) are public.

Weight: a large, honest benchmark that reports where baselines win (DNABERT at 300 bp, SpliceAI on splicing, NT on short splice tasks). NT-benchmark scores for other models are copied from the NT leaderboard rather than rerun. Several figures (Figs 1–5) and supplementary figures are images in the clipping, so values not stated in the text could not be read here.

## Limitations

**Authors' own:**
- BPE tokenization confines predictions to token granularity; alternative tokenizations or nucleotide-level embeddings may be needed for some applications.
- Even 36 kb (sparse) falls short of the hundreds of kb to Mb over which variants can affect expression through loop extrusion and 3D contacts; RMT and external 3D-proximity models are proposed workarounds.
- Motifs enriched in important tokens show association, not causation (e.g., neural/dermal TF motifs for H3K27me3 in K562).
- Cross-species epigenetic inference is weaker than species- and cell-type-specific models and may be limited to taxonomically close groups.
- High MLM accuracy does not guarantee good downstream transfer.

**Reviewer notes:**
- The ClinVar promoter classifier (AUC 0.66) is modest and is not compared against a conservation score or other variant-effect tools, so its added value is unclear. (synthesis)
- The task-dependent winner (bert-large for DHS and short tasks, bigbird for HMs and splicing, RMT for long tasks) means "GENA-LM" results are a best-of-family envelope rather than one model's performance. (synthesis)
- All epigenetic tasks are bulk, cell-line ChIP/DNase labels (DeepSEA, K562); nothing here tests single-cell or cell-type-resolved prediction. (synthesis)

## Surprising or load-bearing bits

- **Context helps broad histone marks, not TFs.** Going from 1 to 8 kb mostly lifted broad-mark AUC, which matches the idea that domain-scale marks need domain-scale input.
- **Recurrent memory beat a 1-Mb HyenaDNA with 50 kb.** On species classification, a segment-recurrent BERT outscored a long-convolution model with 20× less input. (The task is coarse, so this is a narrow result.) (synthesis)
- **Layer choice matters for frozen embeddings.** Middle layers transfer better than the last, which matters for any downstream use of DNA-LM embeddings as features. (synthesis)
- **T2T + population SNPs as pre-training data** rather than hg38 alone, to avoid overfitting to one reference.

## Concepts touched

- [[dna-language-model]] — encoder-only BERT/BigBird family with RMT long-context extension.
- [[genomic-tokenization]] — BPE (32k vocabulary, median 9 bp) as the main context-length lever; resolution trade-off acknowledged.
- [[variant-effect-prediction]] — ClinVar promoter scoring and splice-site *in silico* mutagenesis.
- [[transcription-factor-motif]] / [[de-novo-motif-discovery]] — Integrated Gradients + FIMO/XSTREME recover ATF1, GATA2, CTCF motifs and variant motifs.
- [[chip-seq]] — attribution proposed as a way to sharpen ChIP-seq's ~100–200-bp resolution to motif level.
- [[convolutional-neural-network]] — DeepSEA and SpliceAI as task-specific CNN baselines; SpliceAI still wins on splicing.
- [[transposable-elements]] — the longest BPE tokens map to LINEs and simple repeats.

## Connections to other sources

- Benchmarked against [[ji-2021-dnabert]] and [[zhou-2023-dnabert-2]] (BPE predecessor with shorter input), [[dallatorre-2025-nucleotide-transformer]] (18-task benchmark source; GENA-LM beats NT 2.5B on average with ~8× fewer parameters) and [[nguyen-2023-hyenadna]] (species-classification benchmark; RMT outperforms).
- Uses the DeepSEA dataset from [[zhou-2015-deepsea]]; Enformer ([[avsec-2021-enformer]]) appears as a fine-tuned baseline in the NT benchmark table.
- [[aspidova-2026-moderngena]] shares authors (Fishman, Kuratov, Burtsev) and revisits the BERT-style recipe as a 2026 baseline; this paper does not mention it.
- Long-context alternatives in this batch: [[vishniakov-2025-gene42]] (dense attention), [[ma-2025-hybridna]] and [[duan-2025-janusdna]] (Transformer–Mamba hybrids), [[schiff-2024-caduceus]] (bidirectional Mamba). (synthesis)

## Open questions

- Would base-resolution tokenization close the gap to SpliceAI and to NT on the short splice tasks? The authors flag tokenization granularity but do not test it.
- How does RMT compare with state-space or hybrid long-context models (Caduceus, HybriDNA, JanusDNA) on the same tasks? (synthesis)
- Can cross-species H3K27ac transfer be calibrated so that the performance drop measures regulatory-grammar divergence, as the authors suggest, rather than data-quality differences between species? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[variant-effect-prediction]] · [[ji-2021-dnabert]] · [[zhou-2023-dnabert-2]] · [[nguyen-2023-hyenadna]] · [[40-Topics/sequence-models-and-foundation-models]]
