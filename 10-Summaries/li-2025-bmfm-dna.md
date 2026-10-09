---
type: summary
title: "Li et al. 2025 — BMFM-DNA: A SNP-aware DNA foundation model to capture variant effects"
source: "[[00-Sources/papers/BMFM-DNA- A SNP-aware DNA foundation model to capture variant effects.pdf]]"
source_quality: full
source_sha256: "e7db03c30c75cb6df9dae698d656360f5fe59cf8aba1eb55acff18d57f0e3b96"
source_kind: paper
author: "Hongyang Li, Sanjoy Dey, Bum Chul Kwon, Michael Danziger, Michal Rosen-Tzvi, Jianying Hu, … Bharath Dandala (corresponding), Pablo Meyer (corresponding)"
published: 2025-06-26
ingested: 2026-10-08
doi: "10.48550/arXiv.2507.05265"
journal: "arXiv preprint (q-bio.GN, v1)"
tags: [BMFM-DNA, IBM, DNA-language-model, SNP-aware, dbSNP, variant-encoding, ModernBERT, BPE, masked-language-model, GUE, lenti-MPRA, GWAS-Catalog, ClinVar, preprint]
entities: []
concepts: ["[[dna-language-model]]", "[[variant-effect-prediction]]", "[[genomic-tokenization]]", "[[cis-regulatory-element]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Li et al. (2025) — *BMFM-DNA: A SNP-aware DNA foundation model to capture variant effects* — arXiv preprint 2507.05265v1. [DOI](https://doi.org/10.48550/arXiv.2507.05265)

# Li 2025 — BMFM-DNA

> IBM's BMFM-DNA builds two ModernBERT encoders (22 layers, hidden 768, 2,048-token context, BPE vocabulary of 4,096) on GRCh38: **BMFM-DNA-REF** on reference sequence and **BMFM-DNA-SNP** on a "variation-encoded" genome. For the SNP model, 20 million dbSNP variants (SNPs and indels) give each variable position a multinomial over 11 states; a biallelic pair is sampled per position and written as one of **121 Chinese characters** (taken from the poem *Li Sao*), so a heterozygous-like ambiguity occupies one symbol that BPE can merge into tokens. On six fine-tuning tasks the SNP model beats the REF model on five and roughly matches DNABERT-2, which was trained on 135 species for longer. The gains are small (e.g. promoter F1 93.5 vs 92.08; MPRA PCC 75.53 vs 74.70) and the authors say current benchmarks cannot fully evaluate the idea.

## Key claims

- **Variant encoding helps a little, consistently.** BMFM-DNA-SNP vs BMFM-DNA-REF (F1 unless stated): promoter 93.5 vs 92.08; core promoter 83.19 vs 81.97; TF binding 82.42 vs 81.87; splicing 90.44 vs 89.29; lenti-MPRA K562 PCC 75.53 vs 74.70; SNP-to-disease AUC 90 vs 90 (no gain).
- **Parity with DNABERT-2, not superiority.** DNABERT-2 scores 94.00, 83.85, 83.91, 90.66 and 75.00 on the same first five tasks; BMFM-DNA-SNP is slightly lower on four and slightly higher on MPRA. On SNP-to-disease the comparator is EVE (AUC 91 vs 90). A no-pretraining ModernBERT is clearly worse everywhere (e.g. splicing 68.18).
- **Variant-aware tokenizer learns variant patterns.** The two BPE vocabularies share 84.3% of tokens. 6.8% of variant-encoded vocabulary tokens contain a variant, against ~1% natural variant abundance, and variant tokens are shorter. In 4-mers, A/G and C/T SNPs each make up ~40% of single-variant tokens. Mapping variant tokens back to reference k-mers raises k-mer space usage for 2- to 5-mers.
- **Variant-encoded fine-tuning data.** On promoter detection with dbSNP variants inserted: aligning both classes with bwa-mem gives F1 93.01 (vs 93.5 baseline, on fewer negatives); random SNPs from all 121 symbols in negatives gives 97.46 (an easier, leaky task); same-distribution SNPs at random positions gives 94.10; random SNPs inserted into positives as negatives gives 64.6 with pretraining vs 57.04 from scratch.

## Methods / evidence

Pretraining data: GRCh38 sampled ten times into 1–10 kb windows plus reverse complements, 9,982,678 samples (~20× genome, ~60 B nt). Variant matrix: population-specific frequencies averaged per position across dbSNP; positions without variants get probability 1 for the reference base. Separate SentencePiece BPE tokenizers trained on 20 kb sequences for each genome version. ModernBERT: RoPE (global θ 160,000; local 10,000), GeGLU, alternating global attention every third layer with local window 128, FlashAttention. MLM with 90% [MASK] / 10% unchanged; 70/20/10 split; 150,000 steps, batch 40, peak LR 5e−4; ~10 days on 4 A100-80GB. Fine-tuning: three seeds, best-validation checkpoint.

Tasks: four GUE tasks from DNABERT-2 (promoter −249/+50 bp; core promoter −34/+35 bp; five ENCODE TFBS sets; splice sites with adversarial examples), K562 lenti-MPRA (143,295 train sequences), and a new SNP-to-disease task: 475,694 SNPs with ±500 bp from GWAS Catalog and ClinVar, top 2,000 of 14,435 diseases, 80/10/10 split. Figures 1–3 are images in the PDF text; values above are from text and Tables 1–3. Code and models: github.com/BiomedSciAI/biomed-multi-omic and Hugging Face.

## Limitations

**Authors' own:**
- Current benchmarks are limited in their ability to evaluate SNP-aware models; more datasets and experiments are needed to judge how well natural SNP patterns are captured.
- Fine-tuning tasks use short sequences, which favour DNABERT-2 (pretrained on 128-length sequences); longer-context benchmarks are planned.
- Some datasets (artificially generated negatives) could not be aligned, so variant encoding of negatives required synthetic strategies.

**Reviewer notes:**
- No variance or significance is reported across the three seeds, and most SNP-vs-REF differences are 0.5–1.5 F1 points. (synthesis)
- The 121-symbol encoding represents a sampled *pair* of alleles at a position, not a phased haplotype, and the pair is drawn from population frequencies rather than any individual; it encodes "this site is polymorphic", not genotype. (synthesis)
- The SNP-to-disease task splits by SNP, not by locus or chromosome, so nearby or linked SNPs can sit in both train and test. (synthesis)

## Surprising or load-bearing bits

- **One symbol per ambiguous site.** Writing a variable position as a single character lets an off-the-shelf BPE tokenizer and ModernBERT handle variation with no architecture change, and BPE then discovers which variant contexts recur (A/G and C/T transitions dominate). (synthesis)
- **Class 2 is a warning about leakage.** When negatives carry variant symbols that positives never use, F1 jumps to 97.46: models can trivially learn the injection procedure. Any variant-encoded benchmark needs matched variant distributions. (synthesis)
- **Text inconsistencies.** The tokenizer section says vocabularies were built "for all three approaches" but describes two; the MPRA section says "three human cell types for lymphoblasts (K562)" but uses one cell line, and K562 is erythroleukaemia-derived, not lymphoblastoid. (synthesis)

## Concepts touched

- [[dna-language-model]] — SNP-aware pretraining via variant-encoded symbols in a ModernBERT/BPE model.
- [[genomic-tokenization]] — variant-aware BPE vocabulary analysis; 84.3% overlap with reference vocabulary, 6.8% variant tokens.
- [[variant-effect-prediction]] — SNP-to-disease association task (GWAS Catalog + ClinVar); no gain from SNP pretraining there.
- [[cis-regulatory-element]] — lenti-MPRA K562 regulatory activity regression, where the SNP model is best.

## Connections to other sources

- Main baseline: [[zhou-2023-dnabert-2]] (GUE tasks and BPE tokenization); background models [[fishman-2025-gena-lm]], [[dallatorre-2025-nucleotide-transformer]], [[sanabria-2024-grover]], [[chen-2022-sei]].
- Same goal, different encoding: [[long-2025-mutbert]] feeds allele frequencies as soft inputs rather than sampled symbols; [[liu-2026-ukbiobert]] uses biobank variants; [[leib-2026-dnt]] models diploid genomes. (synthesis)
- Lenti-MPRA as a regulatory benchmark also appears in sequence-to-function work such as [[linder-2025-borzoi]]. (synthesis)

## Open questions

- Does variant encoding help on tasks where variants matter directly (eQTL, MPRA allelic effects), rather than on promoter or splice classification where it mainly acts as augmentation?
- Could the same one-symbol scheme encode an individual's *heterozygous* or *somatic* sites (from a single-cell genotype) instead of population frequencies? (synthesis)

## Related

- [[dna-language-model]] · [[variant-effect-prediction]] · [[genomic-tokenization]] · [[40-Topics/sequence-models-and-foundation-models]] · [[zhou-2023-dnabert-2]] · [[long-2025-mutbert]]
