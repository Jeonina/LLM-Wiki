---
type: summary
title: "Ayanian et al. 2025 — Introducing a foundational sequence transformer for range adaptive nucleotide decoding (STRAND)"
source: "[[00-Sources/papers/Introducing a foundational sequence transformer for range adaptive nucleotide decoding (STRAND)]]"
source_quality: full
source_sha256: "2ad7e18b197df39157836387901080f90e9b8c9ef8f309bdf8c433c4f837a3d7"
source_kind: paper
author: "Shant Ayanian, Collin Osborne, Clark Xu, Carl Molnar, Pravat Das, Xoab Perez, … Elena Myasoedova (19 authors; corresponding author not marked in clipping)"
published: 2025-11-24
ingested: 2026-10-08
doi: "10.1093/bib/bbaf618"
journal: "Briefings in Bioinformatics 26(6):bbaf618"
tags: [STRAND, DNA-language-model, exome, aligned-reads, BAM, Tapestry, Mayo-Clinic, Cerebras, decoder-only, next-token-prediction, sequence-packing, dynamic-loss-weighting, ClinVar, rheumatoid-arthritis, IBD, NT-benchmark]
entities: []
concepts: ["[[dna-language-model]]", "[[variant-effect-prediction]]", "[[read-alignment]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Ayanian et al. (2025) — *Introducing a foundational sequence transformer for range adaptive nucleotide decoding (STRAND)* — *Briefings in Bioinformatics* 26(6):bbaf618. [DOI](https://doi.org/10.1093/bib/bbaf618)

# Ayanian 2025 — STRAND

> STRAND is a Mayo Clinic / Cerebras decoder-only DNA language model (~1 B parameters, 20 layers, hidden 1,856, RoPE, ~1 kb context) trained by next-token prediction on the human reference, multispecies genomes and — unusually — **raw aligned 151-bp exome reads** from up to 499 participants of the Tapestry clinical exome study (219 with rheumatoid arthritis, 280 without). To make reads trainable it packs reads consecutively by position, filters redundant reads eightfold, and up-weights rare (variant) positions in the loss. Fine-tuned STRAND reports the best MCC on most NT-benchmark categories and on new ClinVar-derived and RA/IBD variant-classification tasks. The read-level training idea is the distinctive part; the benchmark claims rest on new, loosely described datasets and some text–table mismatches.

## Key claims

- **Reads, not VCFs.** Training on aligned reads rather than called variants is said to avoid inductive bias from variant calling and GWAS processing. Reads carry 1–180× depth redundancy and typically only 1–2 bases differ from the reference per 151-bp read, so the model could trivially learn the reference.
- **Consecutive packing works best.** Packing reads from the same chromosome in positional order gave the highest next-token accuracy on every test set (e.g. 87.28% on consecutive-packed test vs 83.97% for a reference-only model), beating random, spaced and overlap packing, contrary to the authors' hypothesis.
- **8× filtering plus dynamic loss weighting.** Filtering low-quality reads cut reads eightfold with comparable accuracy, but reference accuracy dropped (58.29 → 56.04). Adding reference copies and inverse-frequency "dynamic loss weighting" recovered it to 58.87–58.89, above the reference-only model.
- **Causal beats masked.** GPT-style next-token accuracy 58.75% vs 43.41% for BERT-style 15% masking. Context length 600 → 16,384 bp raised accuracy only from 56.93% to 58.7%, so ~1 kb was chosen. RoPE was the best positional encoding (58.75%).
- **More subjects and multispecies help slightly.** Going from 1 to 100 subjects and adding multispecies genomes raised accuracy by fractions of a percentage point (e.g. HRG 58.29 → 58.87 with multispecies).
- **NT benchmark (MCC, median of 10-fold CV).** STRAND: splicing 0.975, regulatory 0.920, chromatin 0.745; NT-2.5B multispecies 0.973 / 0.919 / 0.544; NTv2-500M 0.974 / 0.930 / 0.559; DNABERT-2, HyenaDNA-1kb and Evo-1 lower. Abstract: mean accuracy 0.880, 8.2% over NT and 7% over NT-v2.
- **ClinVar-derived tasks (MCC).** STRAND best on four of five: cardiovascular phenotype 77.4 (NT-2.5B 38.3), hereditary cancer-predisposing syndrome 93.7, BRCA gene 87.7, pathogenic variant 36; NT-2.5B best on Top-5 genes (99.8 vs 99.6). Mean 78.8 vs 65.8 (DNABERT-2).
- **Disease-specific tasks.** RA-variant MCC 0.827 (NT-2.5B 0.812); IBD-variant 0.941 (DNABERT-2 0.926). IBD exomes were not seen in training.

## Methods / evidence

Data: GRCh38 reference, multispecies genomes, and BAM-derived reads from 1–499 Tapestry participants (a 98,222-person decentralised clinical exome study); RA cases had ≥ 2 ICD codes plus a methotrexate claim; 93% non-Hispanic white. Two-phase training: reference first, then mixed with participant reads. Tokenizer: integer codes with a dictionary up to 16. Compute: Mayo Clinic Cloud and up to four Cerebras CS-3 systems. Downstream: classifier head with full fine-tuning; ClinVar tasks built from 26,438–106,843 sequences each; RA (612 variants vs 38,224 controls) and IBD (5,111 vs 38,224) with a 70/12/18 split. Layer probing with a two-layer MLP on three tasks (Figure 2, image only). Benchmark construction details are in a supplementary PDF not included in the clipping. Data and code are available only partly, on request, because of PHI.

## Limitations

**Authors' own:**
- Exomes are mostly from white US participants; generalisation to diverse populations is untested.
- Context is ~1,000 bp, short for interpreting whole exons in one input.
- Still compute-heavy to run and fine-tune despite its size.
- Indels, soft clipping and HLA typing are not yet modelled.
- Patient-level conclusions and clinical validation (software as a medical device) are still needed.

**Reviewer notes:**
- The text's claims do not match its own Table 5: NTv2-500M has a higher regulatory MCC (0.930) than STRAND (0.920), yet STRAND is bolded and said to beat the second-best model by 21.91% on regulatory tasks; the stated 8.2% / 7% gains and "mean accuracy 0.880" cannot be reproduced from the table shown. (synthesis)
- The ClinVar and RA/IBD tasks are new, split details and negative construction are in an unavailable supplement, and fine-tuning budgets per baseline are not given, so the large margins (e.g. 77.4 vs 38.3 MCC) are hard to judge. Several tasks (Top-5 genes, BRCA gene identity) test gene recognition rather than variant effect. (synthesis)
- Training on raw reads means the model also sees sequencing and alignment errors. The authors filter low-quality reads but do not separate true variants from errors in the loss weighting, so "variant positions" up-weighted by frequency may include artefacts. (synthesis)

## Surprising or load-bearing bits

- **A DNA LM that reads BAMs.** STRAND is the only model in this batch trained on read-level data rather than reference sequence, frequencies or genotype calls. For single-cell DNA, where amplification errors and allele dropout make calling the hard part, a read-level LM is a conceptually closer fit than a genotype-level one, though STRAND does not test this. (synthesis)
- **Order matters more than diversity.** Keeping reads in genomic order beat smarter packing, implying the model relies on local continuity even when reads are fragmentary.
- **Next-token accuracy barely moves** (≈ 56–59%) across nearly every design choice, so ablations are decided on sub-percentage differences.

## Concepts touched

- [[dna-language-model]] — decoder-only model trained on aligned exome reads plus reference and multispecies genomes.
- [[variant-effect-prediction]] — fine-tuned ClinVar pathogenicity, phenotype and disease-specific variant classification.
- [[read-alignment]] — uses aligned reads (BAM) as model input and packs them by genomic coordinate.
- [[sequencing-depth-and-coverage]] — 1–180× depth redundancy handled by 8× read filtering and frequency-based loss weighting.

## Connections to other sources

- Benchmarked against [[dallatorre-2025-nucleotide-transformer]], [[zhou-2023-dnabert-2]] and [[nguyen-2023-hyenadna]] on the NT benchmark.
- Other ways of exposing a DNA LM to personal variation: genotype tokens ([[salman-2026-mendel]], [[leib-2026-dnt]]), population frequencies ([[long-2025-mutbert]]), variant-edited sequence ([[liu-2026-ukbiobert]], [[li-2025-bmfm-dna]]). STRAND is the most upstream of these. (synthesis)
- Read-level error modelling is the core problem in [[single-cell-variant-calling]]; a read-trained LM might be a prior there, which remains to be tested. (synthesis)

## Open questions

- Does the model learn genuine variants, or also systematic sequencing and alignment artefacts, from raw reads? An error-aware evaluation is missing.
- Does read-level pretraining help with variant calling or genotype quality, rather than only downstream classification?
- Would the same packing and loss-weighting recipe transfer to amplified single-cell reads with uneven coverage and allele dropout? (synthesis)

## Related

- [[dna-language-model]] · [[variant-effect-prediction]] · [[read-alignment]] · [[40-Topics/sequence-models-and-foundation-models]] · [[dallatorre-2025-nucleotide-transformer]] · [[single-cell-variant-calling]]
