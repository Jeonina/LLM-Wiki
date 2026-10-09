---
type: summary
title: "Ji et al. 2021 — DNABERT: pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome"
source: "[[00-Sources/papers/DNABERT_ pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome]]"
source_quality: full
source_sha256: "cb4aca42fc8e866e47b4350a26fab9231456ea744cdc62354286939474a6199c"
source_kind: paper
author: "Yanrong Ji, Zhihan Zhou, Han Liu, Ramana V. Davuluri (joint first authors: Ji and Zhou; corresponding author not marked in the clipping)"
published: 2021-02-04
ingested: 2026-10-08
doi: "10.1093/bioinformatics/btab083"
journal: "Bioinformatics 37(15):2112–2120"
tags: [DNABERT, dna-language-model, BERT, transformer, masked-language-modeling, k-mer-tokenization, self-supervised-pretraining, fine-tuning, promoter-prediction, TFBS-prediction, splice-site-prediction, attention-visualization, variant-effect-prediction, cross-species-transfer, ENCODE]
entities: []
concepts: ["[[dna-language-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[transcription-factor-motif]]", "[[de-novo-motif-discovery]]", "[[convolutional-neural-network]]", "[[chip-seq]]", "[[cis-regulatory-element]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]"]
---

**Citation:** Ji et al. (2021) — *DNABERT: pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome* — *Bioinformatics* 37(15):2112–2120. [DOI](https://doi.org/10.1093/bioinformatics/btab083)

# Ji 2021 — DNABERT

> DNABERT transfers the BERT recipe to the human genome: a 12-layer, 768-hidden, 12-head Transformer encoder is pre-trained by masked-token prediction on unlabeled human reference sequence tokenised into overlapping k-mers (k = 3–6), then fine-tuned with small labelled sets for promoters, transcription-factor binding sites (TFBSs) and splice sites. The paper's argument is that CNNs see only local windows and RNNs compress long context poorly, while self-attention captures context across the whole input and pre-training makes the model usable when labels are scarce. It reports large gains over task-specific tools on each benchmark, attention-based motif discovery (DNABERT-viz), in-silico variant scoring, and transfer of the human-pre-trained model to 78 mouse ChIP-seq sets. It is the first widely used DNA language model and the template that later models (DNABERT-2, Nucleotide Transformer) revise.

## Key claims

- **One pre-trained model fine-tunes to several regulatory tasks.** The same pre-trained DNABERT (k = 6 reported; k = 3–6 gave "very similar performances") was fine-tuned for promoters, TFBSs and splice sites, and beat the task-specific baselines in each.
- **Promoters.** On EPDnew human promoters (−249 to +50 bp around the TSS), DNABERT-Prom-300 exceeded DeePromoter on TATA promoters by 0.335 in accuracy and 0.554 in MCC. In the harder, class-imbalanced 1,001 bp scan setting, the best baseline (FirstEF) had F1 0.277 (TATA), 0.377 (non-TATA) and 0.331 (combined); DNABERT-Prom-scan "largely surpassed" these (exact values are in Fig. 2, an image in the clipping). On 70 bp core promoters it beat CNN, CNN+LSTM and CNN+GRU.
- **TFBSs.** Fine-tuned on 690 ENCODE TF ChIP-seq peak sets, DNABERT-TF was the only method with mean and median accuracy and F1 above 0.9 (0.918 and 0.919), beating the next best, DeepSEA (one-sided Wilcoxon signed-rank, n = 690, adjusted P = 4.5 × 10⁻¹⁰⁰ and 1 × 10⁻⁹⁸). Baselines were DeepBind, DeepSEA, Basset, DeepSite, DanQ and DESSO. The gain was largest on low-quality ChIP-seq experiments, where DNABERT kept higher recall and fewer false positives.
- **Context separates same-motif TFs.** On p53-family sites, binary classification of individual TFs reached ~0.99. With 500 bp of context, DNABERT-TF separated TAp73-α from TAp73-β binding sites with accuracy 0.828.
- **Attention recovers motifs.** DNABERT-viz aggregates attention into landscapes: high attention 20–30 bp upstream of the TSS in TATA promoters (the TATA box), scattered attention in non-TATA promoters. Contiguous high-attention regions, filtered by a hypergeometric test and merged into PWMs, gave 1,999 motifs from the ENCODE 690 set, of which 1,595 matched JASPAR 2018 by TOMTOM (q < 0.01).
- **Splice sites.** On a SpliceFinder-style dataset rebuilt with adversarial examples, baselines dropped sharply while DNABERT-Splice reached accuracy 0.923, F1 0.919 and MCC 0.871. Its attention concentrated on intronic regions next to donors and acceptors, which the authors link to intronic splicing enhancers and silencers.
- **Variant scoring.** Re-predicting dbSNP variants that fall inside high-attention regions with the alternative allele flagged candidates; 24.7% (TATA) and 31.4% (non-TATA) of the dbSNP Common variants found this way in the Prom-300 data appear in ClinVar, GRASP or the GWAS Catalog. Examples: a pathogenic 4 bp deletion removing a CTCF site in *MYO7A*, an SNV at the *SUMF1* initiator codon disrupting a YY1 site, and an intronic *XPC* risk SNP weakening a CTCF site. On the PRVCS benchmark, a model trained on DNABERT mutation scores gave better AUROC than scores from other deep models (Supplementary Fig. S13, not in the clipping).
- **Pre-training is necessary and transfers.** Randomly initialised DNABERT converged to a markedly higher fine-tuning loss on Prom-300, and on Prom-core was untrainable or suboptimal. The human-pre-trained model fine-tuned on 78 mouse ENCODE ChIP-seq sets beat CNN, CNN+LSTM, CNN+GRU and randomly initialised DNABERT.

## Methods / evidence

Architecture: BERT-base (12 layers, 768 hidden units, 12 heads). Tokenisation: overlapping k-mers with vocabulary 4^k + 5 special tokens ([CLS], [PAD], [UNK], [SEP], [MASK]); four models DNABERT-3/4/5/6. Pre-training: human genome only, sequences of 5–510 tokens by non-overlapping splitting plus random sampling; next-sentence prediction removed; contiguous k-length spans are masked because a single overlapping k-mer could be inferred trivially from its neighbours. 120k steps at batch size 2,000, masking 15% for the first 100k steps and 20% for the last 20k; learning rate warmed to 4e-4 over 10k steps. Max input 512 tokens; longer inputs are split and their representations concatenated (DNABERT-XL). Pre-training took about 25 days on 8 NVIDIA 2080Ti GPUs. Fine-tuning used AdamW with linear warm-up and decay; hyperparameters in Supplementary Table S5.

Evidence is benchmark comparison against named tools on public data (EPDnew, ENCODE 690 TF ChIP-seq, GEO GSE15780 p53/TAp73, a rebuilt SpliceFinder dataset, 78 mouse ENCODE sets), with Wilcoxon, DeLong and McNemar tests. Most per-task numbers live in figures and supplementary tables that are images or zip links in the clipping; only the values quoted in the text are recorded above. Code and models: github.com/jerryji1993/DNABERT.

## Limitations

**Authors' own:**
- Pre-training is resource-intensive (~25 days on 8 GPUs), which is why they release the model rather than expect users to retrain it.
- Input length is capped at 512 tokens; longer sequences need the DNABERT-XL split-and-concatenate workaround.
- In low-quality ChIP-seq experiments, attention is dispersed with a spike at the start of the sequence, "likely due to model bias".
- Variant prioritisation uses DNABERT scores alone; they expect gains from adding features such as DHS predictions.
- Many motifs DNABERT-viz extracted for TAp73 isoforms did not align to JASPAR, so their meaning is open.

**Reviewer notes:**
- Pre-training uses only the human reference genome, so no population variation or other species enter the model; the mouse result is fine-tuning transfer, not multi-species pre-training. (synthesis)
- Overlapping k-mers make each nucleotide appear in k tokens, which inflates sequence length and is the inefficiency DNABERT-2 later targets with BPE ([[zhou-2023-dnabert-2]]). (synthesis)
- Several headline comparisons use different input lengths and negative-set designs per baseline (for example dinucleotide-shuffled negatives in Prom-300), so the size of the gains depends on benchmark construction. (synthesis)

## Surprising or load-bearing bits

- **Masking contiguous spans is forced by overlapping k-mers.** Masking a single 6-mer would let the model read it off its neighbours, so DNABERT masks k contiguous tokens. This tokenisation-objective coupling is the root of later tokenisation debates. (synthesis)
- **Gains were largest on noisy ChIP-seq.** The TFBS advantage came mainly from experiments where baselines failed, not from high-quality ones.
- **Human pre-training transferred to mouse** even though non-coding sequence is only ~50% similar between the two genomes, by the authors' framing.
- **Attention as interpretation.** 1,595 of 1,999 attention-derived motifs matched JASPAR, which the authors present as interpretability on par with CNN filter analysis.

## Concepts touched

- [[dna-language-model]] — the first BERT-style DNA LM: masked-token pre-training on the human genome, then task fine-tuning.
- [[genomic-tokenization]] — overlapping k-mers (k = 3–6), 4^k + 5 vocabulary, span masking.
- [[variant-effect-prediction]] — in-silico allele swaps within high-attention regions; PRVCS benchmark.
- [[transcription-factor-motif]] / [[de-novo-motif-discovery]] — attention-derived PWMs matched to JASPAR.
- [[convolutional-neural-network]] — CNN, CNN+LSTM, CNN+GRU, DeepSEA, Basset and DanQ as comparators.
- [[chip-seq]] — ENCODE 690 TF peak sets as the TFBS benchmark.
- [[cis-regulatory-element]] — promoters, TFBSs and splicing elements as the targeted CRE classes.

## Connections to other sources

- Benchmarks against CNN sequence-to-function models [[zhou-2015-deepsea]] (second-best on TFBS) and [[kelley-2016-basset]]. DNABERT reuses the ENCODE 690 TF set that DeepSEA trained on. (synthesis)
- Successor: [[zhou-2023-dnabert-2]] replaces overlapping k-mers with BPE and adds multi-species pre-training; it describes DNABERT's k-mer tokenisation as inefficient.
- Contemporaneous and later DNA LMs that compare against DNABERT: [[dallatorre-2025-nucleotide-transformer]], [[nguyen-2023-hyenadna]], [[sanabria-2024-grover]] (which compares k-mer and BPE vocabularies).
- [[fan-2026-gfetm]] uses DNABERT (6-mer, 768-d) as its default peak-sequence encoder for scATAC topic modelling and fine-tunes its last two layers.

## Open questions

- How much of DNABERT's TFBS gain over DeepSEA comes from pre-training versus fine-tuning on each of the 690 sets with a larger model? The paper's random-initialisation control is shown only for promoters and mouse TFBSs. (synthesis)
- Attention weights are used as importance scores; the paper does not compare them with gradient-based attributions on the same tasks. (synthesis)

## Related

- [[dna-language-model]] · [[genomic-tokenization]] · [[zhou-2023-dnabert-2]] · [[dallatorre-2025-nucleotide-transformer]] · [[zhou-2015-deepsea]] · [[fan-2026-gfetm]] · [[40-Topics/sequence-models-and-foundation-models]]
