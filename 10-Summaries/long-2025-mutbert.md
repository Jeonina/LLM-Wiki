---
type: summary
title: "Long et al. 2025 — MutBERT: probabilistic genome representation improves genomics foundation models"
source: "[[00-Sources/papers/MutBERT_ probabilistic genome representation improves genomics foundation models]]"
source_quality: full
source_sha256: "41d30f6112322ac711fda07260d441f293b09bbb7cd346f8279f74b7902cab9f"
source_kind: paper
author: "Weicai Long, Houcheng Su, Jiaqi Xiong, Yanlin Zhang (supervisor)"
published: 2025-07-15
ingested: 2026-10-08
doi: "10.1093/bioinformatics/btaf229"
journal: "Bioinformatics 41(Supplement_1):i294 (ISMB 2025 proceedings)"
tags: [MutBERT, DNA-language-model, probabilistic-genome, allele-frequency, 1000-Genomes, SNP-aware, masked-language-model, single-nucleotide-tokenization, RoPE, eQTL, GUE, NT-benchmark, population-variation]
entities: []
concepts: ["[[dna-language-model]]", "[[variant-effect-prediction]]", "[[genomic-tokenization]]", "[[transcription-factor-motif]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Long et al. (2025) — *MutBERT: probabilistic genome representation improves genomics foundation models* — *Bioinformatics* 41(Suppl 1):i294. [DOI](https://doi.org/10.1093/bioinformatics/btaf229)

# Long 2025 — MutBERT

> MutBERT replaces the one-hot reference sequence with a **probabilistic genome**: each position is a distribution over A/C/G/T taken from 1000 Genomes allele frequencies (variants with AF < 2% dropped), so one 4 × L matrix stands in for thousands of largely redundant individual genomes. An 86 M-parameter, 12-layer transformer encoder with a linear input projection, RoPE and FlashAttention is trained by masking preferentially at SNV positions and predicting the temperature-scaled allele-frequency distribution. Across 23 fine-tuning tasks (GUE TF binding, NT benchmark) and an eQTL task, MutBERT ranks third on average MCC, behind only the much larger NT-2500M-Multi and the multi-species NTv2-500M, and beats its reference-only and multi-species-alignment twins. Gains are small (a few MCC points, eQTL AUROC 0.615 vs ≤ 0.613 for comparators).

## Key claims

- **Population data are redundant when fed as individual genomes.** In 1000 Genomes, SNVs cover only 0.34% of training positions, and about 71% of 510-bp samples contain any SNV. Encoding allele frequencies once avoids re-reading the same loci across individuals.
- **Probabilistic input helps over a reference-only twin.** Same architecture and training: MutBERT average MCC 66.36 vs MutBERT-Ref 64.64 and MutBERT-Multi 65.71 across 23 tasks. Test perplexity: MutBERT 1.996, MutBERT-Ref 2.233, MutBERT-Multi 2.936.
- **Competitive with larger models.** Averages: NTv2-500M-Multi 67.32, MutBERT 66.36, NT-2500M-Multi 66.43, NTv2-250M-Multi 65.06, DNABERT-2 64.62. (The text says MutBERT "ranked third"; the table's averages place NT-2500M-Multi 0.07 above it.) MutBERT is best on 5 of 23 tasks overall and 13 of 23 when larger or multi-species-trained models are excluded.
- **GUE TF binding.** MutBERT has the highest average MCC of 68.29 on the five GUE TFBS tasks, marginally above DNABERT-2; per task, MutBERT-Ref wins three of five.
- **eQTL causality.** Embedding-plus-SVM AUROC averaged across TSS-distance bins: MutBERT 0.615, MutBERT-Multi 0.616, NTv2-500M 0.613, NT-500M-Human 0.610, DNABERT-2 0.590 (NT-2500M excluded for GPU limits). The authors credit RoPE extrapolation (512 → 2,048 bp) for the long-distance bins.
- **Tokenization hypothesis.** BPE (DNABERT-2) suits TFBS and histone tasks; 6-mer NT models do better on splice sites; single-nucleotide tokenization in MutBERT-Ref gives balanced performance. Multi-species NT models are clearly best on splice-site tasks.

## Methods / evidence

Architecture: 12 transformer encoder layers, GELU, 86 M parameters; a linear layer maps a 9 × L matrix (4 nucleotide probabilities plus 5 special tokens) to embeddings, so each position's embedding is the probability-weighted sum of nucleotide embeddings. RoPE with dynamic NTK scaling for longer inputs; FlashAttention; LoRA supported but not used for MutBERT. Pretraining: hg38 autosomes plus X, N removed, chr22 held out; 512-token inputs; batch 2,048; 120,000 steps (≈126 B tokens, ~40 epochs over unique tokens); AdamW, peak LR 4e−4 with cosine decay; trained on 4 L20 GPUs for 6 days. Masking: 15%, SNV positions first, filled with non-SNV positions as needed; target is the allele-frequency distribution with temperature τ = 0.7 (best of 0.7, 1, 2). Data variants: MutBERT (1000 Genomes, 3,202 high-coverage genomes, 27 populations, AF ≥ 2%), MutBERT-Multi (100-vertebrate multiz alignment including the 10 closest primates, column counts as probabilities), MutBERT-Ref (hg38 one-hot).

Evaluation: fine-tuning 1,000 steps, three seeds, MCC; NT models > 300 M parameters fine-tuned with LoRA instead of full fine-tuning, which is a confound. eQTL: Enformer/NT eQTL set, mean embeddings of a 1,536-bp window around the SNV for ref and alt, concatenated, RBF-SVM per TSS-distance bucket with 5,000 training samples, five repeats. Figure 2 is an image; numbers above come from Tables 3–5.

## Limitations

**Authors' own:**
- Positions are treated independently. This fits 1000 Genomes, where usually only one SNV falls in a 512-bp window, but cannot capture co-variation across loci (linkage); it is why MutBERT-Multi, with dense alignment variation, did worse.
- Unknown behaviour on denser variant sets such as gnomAD, and with rare variants included (AF < 2% was excluded by convention, not necessity).
- Scaling the model up is untested.

**Reviewer notes:**
- Collapsing individuals to allele frequencies discards haplotypes and genotypes entirely, so the model sees population marginals, not any person's diploid sequence; it is the opposite design choice from [[leib-2026-dnt]] and [[liu-2026-ukbiobert]]. (synthesis)
- Margins are small (often < 1 MCC point) with three seeds and no reported variance or significance tests, and larger comparators were fine-tuned with LoRA rather than fully. (synthesis)
- No zero-shot variant scoring is reported; the only variant task uses embeddings plus an SVM, so the model's likelihoods for alleles were never tested directly. (synthesis)

## Surprising or load-bearing bits

- **Allele frequency as soft labels.** The MLM target at an SNV is a distribution, not the reference base, so the model is explicitly told that both alleles are "allowed". This is the cleanest way in this ingest of telling a DNA LM about polymorphism without multiplying data. (synthesis)
- **Reference-only twin is already strong.** MutBERT-Ref wins three of five GUE TF tasks, so part of the result is the modern architecture and single-nucleotide tokens rather than population data.
- **Multi-species probabilities hurt** relative to population probabilities, in contrast to the gains [[benegas-2025-gpn-msa]] gets by feeding the alignment as separate rows rather than collapsed frequencies. (synthesis)

## Concepts touched

- [[dna-language-model]] — probabilistic-genome input as a third way to use population data, besides individual genomes (NT-1000G) and alignments (GPN-MSA).
- [[genomic-tokenization]] — single-nucleotide "char" tokens; argues BPE vs k-mer trade-offs depend on task.
- [[variant-effect-prediction]] — eQTL causal-variant classification by embedding difference; modest AUROC gains.
- [[transcription-factor-motif]] — GUE TFBS tasks; PSWM analogy motivates the probabilistic representation.

## Connections to other sources

- Builds on [[benegas-2025-gpn-msa]] (reuses its 100-way alignment for MutBERT-Multi).
- Main comparators: [[zhou-2023-dnabert-2]], [[dallatorre-2025-nucleotide-transformer]]; context models [[ji-2021-dnabert]], [[nguyen-2023-hyenadna]], [[schiff-2024-caduceus]], [[sanabria-2024-grover]].
- eQTL task inherited from [[avsec-2021-enformer]].
- Alternative population-aware designs in this batch: [[li-2025-bmfm-dna]] (SNP-encoded tokens), [[liu-2026-ukbiobert]] (UK Biobank variants), [[salman-2026-mendel]], [[leib-2026-dnt]] (diploid). (synthesis)

## Open questions

- Does including rare variants (or gnomAD-scale frequencies) help or hurt, given that the independent-position assumption weakens as variant density rises?
- Could a per-position probability input represent a *within-individual* mixture, e.g. a somatic variant at its VAF in a tissue or a heteroplasmic site, rather than a population frequency? (synthesis)

## Related

- [[dna-language-model]] · [[variant-effect-prediction]] · [[genomic-tokenization]] · [[40-Topics/sequence-models-and-foundation-models]] · [[benegas-2025-gpn-msa]] · [[li-2025-bmfm-dna]]
