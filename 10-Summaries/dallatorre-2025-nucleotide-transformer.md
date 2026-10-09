---
type: summary
title: "Dalla-Torre et al. 2025 — Nucleotide Transformer: building and evaluating robust foundation models for human genomics"
source: "[[00-Sources/papers/Nucleotide Transformer_ building and evaluating robust foundation models for human genomics]]"
source_quality: full
source_sha256: "c7a9519f127124d0d73a6439810e5ad976fe5acec1e3ae16097975f2f65470d4"
source_kind: paper
author: "Hugo Dalla-Torre, Liam Gonzalez, Javier Mendoza-Revilla, Nicolas Lopez Carranza, Adam Henryk Grzywaczewski, Francesco Oteri, … Thomas Pierrot (15 authors; corresponding author not marked in the clipping)"
published: 2024-11-28
ingested: 2026-10-08
doi: "10.1038/s41592-024-02523-z"
journal: "Nature Methods (online 2024-11-28; 2025 issue — volume/pages not given in the clipping)"
tags: [Nucleotide-Transformer, NT, NT-v2, dna-language-model, masked-language-modeling, 6-mer-tokenization, multi-species-pretraining, 1000-Genomes, scaling, IA3, parameter-efficient-fine-tuning, probing, zero-shot, variant-effect-prediction, SpliceAI, DeepSEA, DeepSTARR, BPNet, InstaDeep]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[sequence-to-function-model]]", "[[convolutional-neural-network]]", "[[cis-regulatory-element]]", "[[chip-seq]]", "[[transcription-factor-motif]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[histone-modifications]]", "[[computational-methods]]"]
---

**Citation:** Dalla-Torre et al. (2024 online; 2025 issue) — *Nucleotide Transformer: building and evaluating robust foundation models for human genomics* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-024-02523-z)

# Dalla-Torre 2025 — Nucleotide Transformer

> Nucleotide Transformer (NT) is a family of BERT-style encoder-only DNA language models from InstaDeep (with Nvidia co-authors), pre-trained by masked 6-mer prediction on 6 kb windows. The first set compares equal-sized models trained on different data: the human reference (Human ref 500M), 3,202 human genomes from 1000 Genomes (1000G 500M and 1000G 2.5B), and 850 species (Multispecies 2.5B). On an 18-task benchmark (histone marks, promoters, enhancers, splice sites) evaluated with tenfold cross-validation, fine-tuned NT models matched or beat a supervised BPNet baseline on all 18 tasks, and the Multispecies 2.5B model was the best of the first-generation models. It also beat DNABERT-2, HyenaDNA and an Enformer trunk overall. A second generation, NT-v2 (50M–500M, rotary embeddings, SwiGLU, 12 kb context, up to 1 trillion training tokens), reached better scores with ten times fewer parameters. The paper also shows that attention and embeddings pick out gene-structure and regulatory elements without labels, and that zero-shot embedding distances rank functional variants (AUC up to 0.80 for ClinVar).

## Key claims

- **Fine-tuning beats probing, and both are competitive with supervised CNNs.** Supervised BPNet averaged MCC 0.665 (original) and 0.683 (28M-parameter version) on the 18 tasks. Probing NT embeddings matched BPNet on 5 tasks and beat it on 8. Parameter-efficient fine-tuning (IA³, ~0.1% of weights) matched it on 6 and beat it on 12. The best probing layer was never the final layer, and layer choice changed performance by up to 38% on enhancer types.
- **Sequence diversity matters as much as size.** Multispecies 2.5B outperformed or matched 1000G 2.5B on several human tasks. Mixing 3,202 human genomes gave "limited improvements" over the reference alone, which the authors attribute to most of each genome being shared.
- **Close to specialised supervised models on their own tasks.** On DeepSEA's 919 chromatin profiles, Multispecies 2.5B averaged about 1% lower AUC than DeepSEA. On SpliceAI-style nucleotide-level splice prediction it reached top-k accuracy 95% and PR-AUC 0.98 with 6 kb context, matching SpliceAI-10k (trained on 15 kb inputs) and beating SpliceAI when both used 6 kb. On DeepSTARR enhancer activity it was about 1% better on housekeeping and 4% worse on developmental enhancers. Full fine-tuning added nothing on chromatin and splicing and about 3% on enhancers.
- **Benchmark against other DNA foundation models.** On the 18 tasks with the same protocol, Multispecies 2.5B had the best overall performance against DNABERT-2, HyenaDNA (1 kb and 32 kb) and Enformer. Enformer was best on enhancer prediction and some chromatin tasks. NT was best on all promoter and splicing tasks. Against HyenaDNA it matched (7) or beat (11) on all 18. DNABERT-1 was excluded because of its 512-token limit.
- **Unsupervised structure in the model.** Embeddings separated intergenic, intronic, coding and UTR sequence (3′ UTRs least well); supervised probes reached accuracy above 0.78. In Multispecies 2.5B, 117 of 640 attention heads were significant for introns, 72 for exons and 74 for TF-binding sites. Masked-token probabilities across chromosome 22 highlighted splice sites, polyA signals and CTCF sites, and correlated with an *MST1R* exon 11 saturation-mutagenesis splicing assay (PCC 0.44).
- **Zero-shot variant scoring.** Cosine similarity between reference and alternative embeddings was the best zero-shot score for ranking ten VEP consequence classes by severity (reported r² −0.35 to −0.3, P < 6.55 × 10⁻¹⁸⁶). Across eQTLs, meQTLs, ClinVar and HGMD, the best zero-shot AUCs were 0.7–0.8, highest for ClinVar (0.80, Multispecies 2.5B). Fine-tuned models slightly beat or matched CADD, GERP, phastCons, phyloP and DeepSEA. Human-trained models were best for eQTLs and meQTLs; the multispecies model was best for pathogenic variants.
- **NT-v2 is smaller and better.** NT-v2 50M matched the two 500M models and 1000G 2.5B. NT-v2 250M had the best benchmark score (average MCC 0.769) at one tenth the size of the 2.5B models. NT-v2 500M with 12 kb context reached SpliceAI top-k accuracy 96% and PR-AUC 0.98, which the authors say surpasses SpliceAI-10k.

## Methods / evidence

Architecture: encoder-only Transformer with learned positional embeddings (max 1,000 tokens), pre-LayerNorm and GELU MLPs; layer and head counts are in Supplementary Table 1 (not in the clipping). Tokeniser: non-overlapping 6-mers (4,096) plus stand-alone A/T/C/G/N and three special tokens, 4,104 in total; 6-mers were chosen as a trade-off between context length and embedding size and because they performed best among token lengths tried. Pre-training: BERT MLM (15% of tokens, 80% masked, plus random-token replacement except for 1000G), effective batch 1 million tokens, Adam. Data: GRCh38 (3.2B nt); 1000 Genomes phased high-coverage set (3,202 genomes, 27 populations, 125M variants, inserted on the fly into reference chunks); 850 RefSeq species (174B nt, plants and viruses excluded). 500M models saw 50B tokens; 2.5B models 300B tokens and took 28 days on 128 A100s. NT-v2: rotary embeddings, SwiGLU without bias, 2,048 tokens (12 kb), up to 1 trillion tokens.

Benchmark: 18 tasks from ENCODE K562 histone ChIP-seq (10 marks), EPDnew promoters, ENCODE SCREEN enhancers and GENCODE splice sites; balanced, capped at 30,000 training examples, chromosomes 20–21 held out, tenfold cross-validation, MCC as metric. Probing trained 760,000 downstream models over ten layers. Other foundation models were ported into the authors' framework and fine-tuned with IA³ (HyenaDNA with full fine-tuning). Most numeric results are in figures and supplementary tables that are images or links in the clipping; only values given in the text are recorded here.

Weight: a large, careful benchmark by the model's developers. The 18-task benchmark is the authors' own and was revised for the journal version (a "revised" HuggingFace dataset is linked). (synthesis)

## Limitations

**Authors' own:**
- Attention span is limited (6 kb, 12 kb in NT-v2), far short of the ~200 kb that Enformer suggests is needed for distal regulation; quadratic attention makes such inputs intractable.
- Encoding intra-species variation by mixing individual genomes gave limited gains; better ways to use population variation are needed.
- Enformer was pre-trained with different data splits, so its benchmark scores may be inflated by data leakage; using its trunk as a pre-trained model is not its intended use.
- Supervised models with optimised architectures trained on large datasets still perform better on some tasks.
- With a BPE tokeniser, nucleotide-level prediction such as splice-site calling would be harder to implement because tokens cover a variable number of bases.

**Reviewer notes:**
- The tokenisation (non-overlapping 6-mers) is fixed across all models, so the paper cannot separate tokenisation effects from data and size effects; DNABERT-2 argues this tokenisation is sample-inefficient ([[zhou-2023-dnabert-2]]). (synthesis)
- The zero-shot severity correlation is reported as "r²" values that are negative, which reads as a correlation coefficient rather than r²; the exact statistic is in Supplementary Fig. 19, not in the clipping. (synthesis)
- Training and evaluation are on reference-genome sequence windows; there is no cell-type-specific input, so outputs are not cell-state-resolved without task-specific fine-tuning. (synthesis)

## Surprising or load-bearing bits

- **Multispecies data beat human population data for human tasks.** 850 species helped human promoter and splice tasks more than 3,202 human genomes did.
- **NT-v2 250M beat the 2.5B model.** Architecture updates plus longer training (800B tokens at the chosen checkpoint) gave the best score at one tenth the size. Scale in parameters was not the main lever. (synthesis)
- **Probing is not cheap.** Rigorous probing needed layer and hyperparameter sweeps (760,000 models) and was slower and more variable than IA³ fine-tuning.
- **Human-only models were better for eQTLs/meQTLs; multispecies for pathogenic variants.** The authors read this as conservation helping coding/pathogenic variants and population variation helping regulatory variants.
- **HyenaDNA degrades with longer pre-training context** on these short-sequence tasks, by the authors' reading of their benchmark.

## Concepts touched

- [[dna-language-model]] — the large-scale, multi-species BERT-style DNA LM; data-diversity and scaling study.
- [[genomic-tokenization]] — non-overlapping 6-mers with single-base fallback tokens; explicit argument against BPE for nucleotide-level heads.
- [[variant-effect-prediction]] — zero-shot embedding-distance scores and fine-tuned classifiers on eQTL, meQTL, ClinVar and HGMD sets.
- [[sequence-to-function-model]] — comparisons with DeepSEA, SpliceAI, DeepSTARR, BPNet and an Enformer trunk.
- [[convolutional-neural-network]] — BPNet as the supervised baseline.
- [[chip-seq]] / [[histone-modifications]] — ten K562 histone-mark tasks.
- [[cis-regulatory-element]] / [[transcription-factor-motif]] — promoter and enhancer tasks, DeepSTARR motif-mutation predictions.

## Connections to other sources

- Extends [[ji-2021-dnabert]] to billions of parameters, multi-species data and non-overlapping k-mers; excludes DNABERT-1 from its benchmark for input-length reasons.
- [[zhou-2023-dnabert-2]] uses NT as its main comparator and criticises non-overlapping k-mers; NT in turn includes DNABERT-2 in its own benchmark and finds Multispecies 2.5B better overall. The two papers' benchmarks were each built by the authors of one model. (synthesis)
- Compares against [[nguyen-2023-hyenadna]] and argues HyenaDNA's long pre-training contexts hurt short-task performance.
- Benchmarks against supervised sequence-to-function models [[zhou-2015-deepsea]] (chromatin profiles) and [[avsec-2021-enformer]] (trunk as pre-trained model).
- Later InstaDeep models in this ingest: [[boshar-2025-ntv3]] and [[dealmeida-2025-segmentnt]]. (synthesis)
- [[fan-2026-gfetm]] tests NT variants as frozen peak encoders for scATAC topic modelling: NT-2.5b-multi-species did best, and NT-500M-human-ref beat NT-500M-1000g.

## Open questions

- How should population variation be encoded so that it helps? The 1000G models gained little over the reference.
- Does the NT-v2 advantage persist on long-range tasks beyond 12 kb, where the authors themselves expect transformers to struggle? (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[variant-effect-prediction]] · [[ji-2021-dnabert]] · [[zhou-2023-dnabert-2]] · [[nguyen-2023-hyenadna]] · [[avsec-2021-enformer]] · [[fan-2026-gfetm]] · [[40-Topics/sequence-models-and-foundation-models]]
