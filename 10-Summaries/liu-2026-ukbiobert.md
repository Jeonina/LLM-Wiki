---
type: summary
title: "Liu et al. 2026 — Pre-training genomic language model with variants for better modeling functional genomics"
source: "[[00-Sources/papers/Pre-training genomic language model with variants for better modeling functional genomics - npj Artificial Intelligence]]"
source_quality: full
source_sha256: "a37d44bb9096c51407af68204384195322a589c44563a4992bb7c54f3256c743"
source_kind: paper
author: "Tianyu Liu, Xiangyu Zhang, Jiecong Lin, Luca Pinello, Rex Ying, Hongyu Zhao"
published: 2026-04-20
ingested: 2026-10-08
doi: "10.1038/s44387-026-00103-4"
journal: "npj Artificial Intelligence"
tags: [UKBioBERT, UKBioFormer, UKBioZoi, DNA-language-model, UK-Biobank, DNABERT-2, continued-pretraining, personal-gene-expression, Enformer, Borzoi, Performer, EPInformer, GTEx, eQTL, in-silico-mutagenesis, cross-ancestry]
entities: []
concepts: ["[[dna-language-model]]", "[[variant-effect-prediction]]", "[[sequence-to-function-model]]", "[[transcription-factor-motif]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Liu et al. (2026) — *Pre-training genomic language model with variants for better modeling functional genomics* — *npj Artificial Intelligence*. [DOI](https://doi.org/10.1038/s44387-026-00103-4)

# Liu 2026 — UKBioBERT / UKBioFormer

> UKBioBERT is DNABERT-2 **continued-pretrained** with MLM on sequences edited to carry ~13 million variants (substitutions, insertions, deletions) from ~300,000 European-ancestry UK Biobank participants. Its gene embeddings cluster best by gene function among a wide panel of DNA LMs, add signal to EPInformer for cell-line expression prediction, and match ElasticNet and Performer for predicting individual-level expression from personal genomes. The paper then fuses frozen UKBioBERT gene embeddings with a pruned, fine-tuned Enformer (**UKBioFormer**, 230.7 M parameters) or Borzoi (**UKBioZoi**). UKBioFormer beats Performer on 63.3% of well-predicted genes, transfers better than embedding-only models from European to African-American individuals, and gets the sign of more GTEx blood eQTLs right than Performer or AlphaGenome. Gains are gene-dependent and not universal.

## Key claims

- **Variant-trained embeddings encode gene function.** On a clustering benchmark (NMI, ARI, ASW averaged) of human gene sequences against functional labels, UKBioBERT has the highest average score among DNA LMs including DNABERT, DNABERT-2, GPN, HyenaDNA, NT, GROVER, GENA-LM, Caduceus, Evo 2, Enformer and Borzoi embeddings, ESM and Llama 3.1. MLM beat contrastive and LD-score-regression pretraining, and starting from a reference-trained checkpoint helped. Using a larger fraction of variants improved the score; the best checkpoint came early, with later decline read as overfitting.
- **Cell-line expression.** Adding UKBioBERT promoter/enhancer embeddings plus scELMo text gene embeddings to EPInformer (mode G) beat default EPInformer and other variants on K562 and GM12878 (12-fold CV); GM12878 CAGE PCC averaged over 0.9. EpiBERT embeddings did not help; silencer sequences did not help.
- **Individual-level expression (GTEx, 670 samples, 41 genes).** UKBioBERT embeddings + ElasticNet, SNP ElasticNet and Performer perform almost identically (per-gene PCC correlation 0.988 and 0.991 between methods); ElasticNet is slightly better on average; zero-shot Enformer is worst. Heritability does not explain which genes are predictable (P = 0.19 PCC, 0.17 SCC); how well individuals cluster by expression in embedding space does.
- **UKBioFormer.** Beats Performer and UKBioZoi on average and wins on 63.3% of genes with PCC > 0.6; trains faster with less memory and accepts > 100 kb input versus Performer's 49 kb. Pruning to one transformer layer outperformed LoRA as the PEFT strategy. Cross-attention fusion was no better than an MLP.
- **Cross-ancestry.** Trained on European, tested on African-American individuals, UKBioBERT embeddings alone perform poorly (some genes negative), while Performer and UKBioFormer improve markedly.
- **Multi-gene training does not help.** Joint training on enhancer-shared (n = 8), pathway-shared (n = 9) or Enformer-pretrained (n = 300) gene groups did not reliably improve and sometimes reduced performance; single-gene models remain the recommendation.
- **eQTL direction.** ISM with UKBioFormer gives a higher fraction of correctly signed GTEx blood eQTLs across the 41 genes (one-sided P = 0.02 vs Performer, 0.06 vs AlphaGenome). For *JUP*, 71% of the top 30 eQTLs have the correct sign (Enformer 53%, Performer 68%). Two eQTLs in enhancer GH17J041791 (rs9910080, rs9903086) are matched in direction; JASPAR scanning finds a JUN-class motif near rs9910080.

## Methods / evidence

UKBioBERT: DNABERT-2 checkpoint (BPE tokenizer), MLM continued pretraining on reference sequence edited with UK Biobank EUR variants by replace, insert and delete functions (Algorithm 1); DNABERT-2 default hyperparameters; 80/10/10 split; a single A100/H100. A UK Biobank HyenaDNA (CLM) was trained as a baseline. Embedding-quality metric: Leiden clustering of gene embeddings at optimal resolution scored against functional labels. UKBioFormer: Enformer weights as initialisation, transformer layers pruned, regression head outputs from the trainable Enformer branch and the frozen UKBioBERT branch combined by a learnable weight in (0,1); MSE loss; Adam; 100 epochs; implemented in gReLU. Individual-level tasks: GTEx WGS + RNA-seq (670 samples), fivefold CV (8:1:1); ROSMAP results are in the supplement. Code: github.com/HelloWorldLTY/UKBioLM (MIT).

Most results are shown only in figures (Figs 2–6) and supplementary figures, which are images in the clipping; numbers above are those stated in the text. A few long paragraphs in the clipping are truncated mid-sentence in the source view used here.

## Limitations

**Authors' own:**
- Gains are conditional on gene and cohort; performance varies substantially across genes, and joint multi-gene training can reduce performance.
- Pretraining variants come mostly from European-ancestry UK Biobank participants, which biases the model; cross-ancestry performance could improve with broader populations.
- Multi-gene training remains an open challenge (model design, compute, or data noise).

**Reviewer notes:**
- The variant-editing step writes alternate alleles into a single reference-like sequence; the text does not say whether edits follow individual haplotypes or are pooled across participants, so what "pretrained with variants" means for genotype structure is unclear. (synthesis)
- Only 41 genes are evaluated for individual-level prediction and eQTL direction; the 63.3% win rate and P = 0.02 are modest effects on a small, heritability-selected panel. (synthesis)
- The headline UKBioBERT embedding result is a clustering benchmark that the authors themselves propose; it is not yet validated as a predictor of downstream utility. (synthesis)

## Surprising or load-bearing bits

- **Predictability is not heritability.** Which genes can be predicted from personal sequence tracks how separable individuals are in embedding space, not estimated heritability. (synthesis: this echoes the known gap between personal-genome expression prediction and reference-trained models.)
- **Both parental genomes help.** Using full genome information from both parents gave better ZFP57 prediction than partial information (supplementary), one of the few places in this batch where diploid input is tested directly.
- **The gLM and the sequence-to-function model are complementary.** The frozen gLM branch carries distal, non-TSS-weighted information; the Enformer branch carries local regulatory grammar. The fusion, not either alone, is what beats Performer.

## Concepts touched

- [[dna-language-model]] — continued MLM pretraining on biobank-variant-edited sequence; proposes a gene-function clustering metric for embedding quality.
- [[sequence-to-function-model]] — fuses gLM embeddings with Enformer/Borzoi for personal expression prediction.
- [[variant-effect-prediction]] — ISM-based eQTL sign prediction against GTEx blood eQTLs, compared with Performer and AlphaGenome.
- [[transcription-factor-motif]] — JASPAR motifs (JUN-class, zinc finger) near prioritised eQTLs.

## Connections to other sources

- Base models: [[zhou-2023-dnabert-2]] (checkpoint), [[avsec-2021-enformer]] and [[linder-2025-borzoi]] (fused backbones); baselines include [[kelley-2018-basenji]], [[fishman-2025-gena-lm]], [[nguyen-2023-hyenadna]] and [[avsec-2026-alphagenome]].
- Cell-line expression framework: [[lin-2026-epinformer]].
- Embedding-benchmark panel includes [[ji-2021-dnabert]], [[dallatorre-2025-nucleotide-transformer]], [[sanabria-2024-grover]], [[schiff-2024-caduceus]] and [[benegas-2025-gpn-msa]]'s predecessor GPN.
- Same question, different design: [[salman-2026-mendel]] (genotype-token objective on GTEx), [[leib-2026-dnt]] (diploid model), [[long-2025-mutbert]], [[li-2025-bmfm-dna]]. (synthesis)

## Open questions

- Would pretraining on diverse-ancestry biobanks close the European → African-American gap for the embedding-only model?
- Could the same fused design predict expression differences between cell populations that differ by somatic variants, given that it already reads an individual's sequence? (synthesis)

## Related

- [[dna-language-model]] · [[variant-effect-prediction]] · [[sequence-to-function-model]] · [[40-Topics/sequence-models-and-foundation-models]] · [[avsec-2021-enformer]] · [[salman-2026-mendel]]
