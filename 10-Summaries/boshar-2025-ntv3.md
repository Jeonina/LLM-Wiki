---
type: summary
title: "Boshar et al. 2025 — A foundational model for joint sequence-function multi-species modeling at scale for long-range genomic prediction"
source: "[[00-Sources/papers/A foundational model for joint sequence-function multi-species modeling at scale for long-range genomic prediction.pdf]]"
source_quality: full
source_sha256: "5ad206af5c6e673739c2311cecf75663197c8dc2ea67601372adbfef9f0b36da"
source_kind: paper
author: "Sam Boshar, Benjamin Evans, Ziqi Tang, Armand Picard, Yanis Adel, Franziska K. Lorbeer, … Alexander Stark, Bernardo P. de Almeida (corresponding), Thomas Pierrot (corresponding)"
published: 2025-12-22 (bioRxiv; posted 2025-12-25)
ingested: 2026-10-08
doi: "10.64898/2025.12.22.695963"
journal: "bioRxiv preprint"
tags: [NTv3, Nucleotide-Transformer, InstaDeep, dna-language-model, sequence-to-function, U-Net, 1Mb-context, single-nucleotide-tokenization, OpenGenome2, multispecies, post-training, genome-annotation, plants, masked-diffusion, enhancer-design, STARR-seq, NTv3-Benchmark, preprint-text]
entities: []
concepts: ["[[dna-language-model]]", "[[sequence-to-function-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[cis-regulatory-element]]", "[[chromatin-accessibility]]", "[[transcription-factor-motif]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Boshar, Evans, Tang et al. (2025) — *A foundational model for joint sequence-function multi-species modeling at scale for long-range genomic prediction* — *bioRxiv preprint*. [DOI](https://doi.org/10.64898/2025.12.22.695963)

# Boshar 2025 — NTv3 (Nucleotide Transformer v3)

> **NTv3 is the third generation of InstaDeep's Nucleotide Transformer**, and it breaks with NT v1/v2 in three ways: it uses **single-nucleotide tokens instead of 6-mers**, a **U-Net (conv down-sampling → transformer at 128 bp → conv up-sampling) instead of a plain encoder**, and a **two-stage recipe** — masked-language-model pretraining on OpenGenome2 (the Evo2 corpus) with a length curriculum up to **1 Mb**, followed by **multispecies post-training** that adds supervised heads for ~16,000 functional tracks (9 species) and 21 genome-annotation labels (24 species) while keeping the MLM loss. The resulting model is both a DNA language model and a Borzoi/AlphaGenome-style sequence-to-function model, and the same backbone is fine-tuned with masked diffusion to design Drosophila enhancers that were tested by STARR-seq. The paper's claim is unification: one efficient backbone for representation, base-resolution track and annotation prediction across animals and plants, interpretation, and controllable generation.

## Key claims

- **Model family and scale.** Pretrained sizes 8M, 100M and 650M (pre); post-trained 100M and 650M (post). The 8M model "lacked sufficient capacity for stable multispecies post-training". Pretraining ran about 10.5 trillion tokens at 1–8 kb (~95% of tokens) plus seven ~50B-token length-extension stages that double context from 16 kb to 1 Mb, about 11 trillion tokens in all, which the authors call "the largest trained genomics model to date". Even 650M runs 1 Mb inference on one A100/H100, and is reported faster than HyenaDNA, Caduceus and NT-style transformers "with up to 60× fewer parameters" (Fig. 2H).
- **Pretraining helps post-training, more for annotation than for tracks.** Starting post-training from the pretrained checkpoint converges faster than random initialisation; the asymptotic gain is "large and consistent" for genome annotation and "more modest" for functional tracks (Supp. Fig. A.5B).
- **Versus Borzoi.** Fine-tuned on Borzoi's own 32 bp human/mouse data, NTv3 650M (post) beats Borzoi on CAGE, ChIP, ATAC and DNase by up to ~3% relative, with a small loss on RNA-seq (up to −0.5%). At single-base resolution on shared tracks, it matches Borzoi on DNase and ChIP and is "substantially" better on ATAC, CAGE and RNA-seq. Borzoi degrades sharply below its 524 kb training length; NTv3 stays stable down to 8 kb (Fig. 3F–G).
- **Versus ChromBPNet.** On two shared DNase experiments, Pearson r 0.753 (HepG2) and 0.755 (IMR-90) for NTv3 vs 0.704 and 0.717 for ChromBPNet.
- **Genome annotation.** NTv3 beats **SegmentNT** at SegmentNT's own 30 kb context and improves further at 1 Mb; it also beats AUGUSTUS on shared elements and SpliceAI on splice donors/acceptors across species. In human the largest gains are for enhancers, promoters, lncRNAs and CTCF-bound sites (Fig. 3E, H, I; values are in figures not readable in the clipped text).
- **NTv3 Benchmark (106 tasks, 32 kb in / 1 bp out).** New tracks for post-training species (human, chicken, Arabidopsis, rice, maize) plus unseen species (cattle, tomato) and assays absent from post-training (PRO-cap, eCLIP, Ribo-seq); three fine-tuning seeds per model per task. Scaling is monotone (8M < 100M < 650M < 650M post). The 8M (pre) model already beats NTv2 500M and Evo2 1B on functional tracks and reaches the 44M Residual-CNN baseline. Caduceus (human) and PlantCAD2 (plants) are the strongest baselines. Post-training gives "the highest scores across every single species", including tomato and the unseen assay types; human annotation MCC reaches "approximately 0.7".
- **Random-init control.** The same U-Net fine-tuned from random weights is consistently and significantly worse (Supp. Fig. A.12), so the gains are attributed to learned representations rather than the architecture alone.
- **Plant gene-level tasks.** Against the 1B-parameter AgroNT, the 8M model gives maize expression R² 0.57 vs 0.54 and protein abundance R² 0.26 vs 0.23 at 6 kb; 650M (pre) gives 0.66/0.37; 650M (post) reaches 0.75 for maize expression at 32 kb and 0.46 for protein abundance at 262 kb.
- **Long-range interpretation.** At the HBE1 locus (131 kb window), attention links the promoter to HS1–HS5, and in-silico single-enhancer restoration on a shuffled background ranks HS2 > HS1 > HS4 > HS3 > HS5, Spearman ρ = 0.900 (p = 0.037) against measured activity (n = 5 elements). Over 3,792 GTEx whole-blood eQTLs, attribution differences are larger for "pathogenic" than "benign" variants (Wilcoxon p < 0.001); case studies are sorted into motif ablation, motif creation and distributed rewiring (e.g. APOL4 rs9610445, ~16-fold drop in predicted RNA-seq).
- **Experimentally validated design.** Fine-tuned with masked diffusion (MDLM) and adaptive-layer-norm conditioning on Drosophila S2 UMI-STARR-seq data (DSCP and RpS12 promoters), with classifier-free guidance (γ = 2, 50 steps). 600 activity-binned designs show the intended stratification in STARR-seq. For promoter-selective design, 150 NTv3 enhancers reach mean specificity 2.14-fold (DSCP) and 4.37-fold (RpS12), higher than 150 sequences picked by DeepSTARR from 512,000 random sequences.

## Methods / evidence

Architecture: embedding + kernel-15 conv stem; 7 residual conv down-sampling blocks (1 → 128 bp; 1 Mb → 8,192 tokens); a RoPE transformer tower (650M: 12 layers, 1,536 width, 24 heads); a mirrored up-sampling decoder with U-Net skips; heads for MLM (11-token vocabulary), species-specific functional tracks (softplus; e.g. 7,362–7,632 human tracks) and a shared 21-label annotation head. Species conditioning (adaptive LayerNorm + scaled residuals, zero-initialised) is added only at post-training; unseen species get the mask token. Pretraining: BERT-style 15% MLM, AdamW (β2 = 0.98), 8M-token batches, sequence-length mixing with a 5% floor per length; OpenGenome2 filtered to ~8 T unique nucleotides, whole eukaryotic genomes withheld until the 32 kb stage. Post-training: 1.2 T tokens up to 131 kb then 54 B tokens up to 1 Mb; loss = Poisson-multinomial on AlphaGenome-scaled tracks (centre 37.5%) + focal loss (γ = 2) on annotations + continued MLM; dataset weights 45% human, 5% each for 8 other track species, 1% each for 15 annotation-only species. Tracks: Borzoi's human/mouse ENCODE/FANTOM5/GEO set, the Calderon Drosophila embryo sc-atlas (90 cell types), and newly processed plant RNA-/ATAC-/ChIP-seq (plant RNA-seq replicates were selected with the help of an OpenAI o3 prompt plus spot-check curation). Splits: Borzoi folds for human/mouse; homology-aware Markov clustering of 1 Mb windows for other species. Compute: e.g. 6,736 H100-hours for 650M 8 kb pretraining; JAX/Flax, TPU v6 and H100. Code, checkpoints, benchmark and leaderboard released on GitHub and Hugging Face.

Weight: a large, carefully documented industrial preprint with extensive ablations (down-sampling depth, length mixing, random init, multitask vs single-task) and wet-lab validation of designs. Most head-to-head numbers live in figures that are not readable in the clipped text, so many comparisons are reported here only as the text describes them. (synthesis)

## Limitations

**Authors' own:**
- Uniform performance across the length spectrum is "non-trivial"; mixed-length training mitigates short-context forgetting but "residual length sensitivity remains an open area". A 1 T-token length-extension run degraded short-sequence sub-datasets (mRNA, ncRNA, transcripts) and was not used.
- Very distal regulation (>100 kb) is still hard because functional tracks give "limited causal linkage and only indirect access to 3D genome organization"; gene-level responses are harder than genome-wide tracks.
- Not yet benchmarked for personal-genome prediction.
- Post-training is "a starting point": no single-cell, perturbation or multiome supervision yet, and batch effects across independently generated tracks are not resolved.
- Attention maps and annotations aggregate across cell types, which "can obscure cell-type-specific regulatory logic"; exon and intron probabilities can be co-elevated where isoforms disagree.
- Reduced down-sampling (5 vs 7 blocks) improved pretraining loss but gave only comparable or modest downstream gains, suggesting a saturation effect.

**Reviewer notes:** (at most three, each marked `(synthesis)`)
- Internal inconsistencies: the abstract and intro say 1,000 constructs were validated, but Methods select 600 + 150 + 150 = 900; post-training is described as 24 species in Results and 25 in Methods 4.1; human track counts are given as 7,362, 7,632 and 7,326; the enhancer-design model is said to start from post-trained weights in the text but from NTv3 650M (pre) in the Fig. 7 legend and Supp. Note B.8. (synthesis)
- The NTv3 Benchmark is built, curated and first reported by the model's authors; baselines were fine-tuned under one shared recipe that may not suit every architecture (e.g. Evo2 run through BioNeMo with Adam). Independent replication of the leaderboard would strengthen the "every species" claim. (synthesis)
- The HBE1 enhancer-ranking result rests on five elements (ρ = 0.9 with p = 0.037), and the eQTL "pathogenic vs benign" labels come from GTEx allelic effects rather than clinical pathogenicity; both are illustrative rather than systematic VEP benchmarks. (synthesis)

## Surprising or load-bearing bits

- **A U-Net can be pretrained self-supervised at trillion-token scale.** U-Nets were previously used only in supervised models (Borzoi, AlphaGenome); NTv3 shows MLM pretraining works for them, given length mixing to avoid short-context forgetting.
- **Tiny models go far.** The 8M (pre) model beats NTv2 500M and Evo2 1B on the 32 kb base-resolution benchmark and beats the 1B AgroNT on maize gene-level tasks — architecture and output resolution matter more than parameter count in this regime. (synthesis on the comparison)
- **Pretraining helps annotation more than functional tracks**, consistent across post-training curves, down-sampling ablations and random-init controls: abundant supervised track data appears to wash out pretraining gains. This parallels the GFETM finding that pretrained DNA features only pay off once adapted. (synthesis)
- **Masked diffusion reuses the MLM head without new parameters**, enabling in-context infilling of an enhancer inside a 4 kb plasmid — something a left-to-right autoregressive model cannot do directly.
- **Plants and fly are first-class.** Six crop species with functional tracks, and the biggest relative gains are claimed in agronomics, where earlier models were limited to <8 kb context.

## Concepts touched

- [[dna-language-model]] — NT v3 moves the Nucleotide Transformer line from 6-mer encoder to single-base U-Net MLM with 1 Mb context.
- [[sequence-to-function-model]] — post-training turns the language model into a multi-species, base-resolution track predictor that beats Borzoi and ChromBPNet on shared tracks.
- [[genomic-tokenization]] — abandons NT's 6-mers for single-nucleotide tokens, made affordable by convolutional down-sampling.
- [[variant-effect-prediction]] — attribution-difference analysis of GTEx eQTLs and mechanism classes (motif ablation/creation/rewiring).
- [[cis-regulatory-element]] — enhancer–promoter ranking at HBE1 and promoter-selective enhancer design.
- [[chromatin-accessibility]] — ATAC/DNase tracks across human, mouse, fly and plants are a core supervised target.
- [[transcription-factor-motif]] — GATA/AP1, ETS/ELK1 and IRF motifs recovered by attribution; promoter-specific motif sets in designed enhancers.

## Connections to other sources

- **Direct predecessor:** [[dallatorre-2025-nucleotide-transformer]] (NT v1/v2, 6-mer encoders); NTv2 500M is a baseline here and is beaten by the 8M NTv3.
- **Annotation predecessor:** [[dealmeida-2025-segmentnt]] — SegmentNT fine-tuned NT for 14-class segmentation; NTv3 reuses its annotation recipe, extends it to 21 labels, and beats it at 30 kb and 1 Mb.
- **Sequence-to-function comparators:** [[linder-2025-borzoi]] (track set, folds and main baseline), [[avsec-2026-alphagenome]] (U-Net design and target scaling borrowed), [[pampari-2024-chrombpnet]] (DNase comparison and BPNet-Large baseline), [[avsec-2021-enformer]] (CNN + transformer lineage).
- **LM baselines:** [[nguyen-2023-hyenadna]], [[schiff-2024-caduceus]]. The opposite design bet — short 4 kb context, 7B parameters — is [[ellington-2024-aido-dna]]. (synthesis)
- **Generative design:** compare autoregressive, tag-conditioned design in [[su-2025-atgc-gen]]. (synthesis)
- **Pretrained-features-need-adaptation pattern** also seen in [[fan-2026-gfetm]]. (synthesis)

## Open questions

- Does post-training on bulk tracks transfer to single-cell chromatin or methylation tasks? The authors list single-cell supervision as future work; no scDNA-relevant task is tested. (synthesis)
- How much of the Borzoi gain comes from post-training breadth (multispecies, annotations, MLM) versus base-resolution output and length mixing? There is no ablation that removes one ingredient at a time against Borzoi. (synthesis)
- Would independent groups reproduce the NTv3 Benchmark leaderboard, especially for Evo2 and PlantCAD2 under their own recommended fine-tuning recipes? (synthesis)

## Related

- [[dna-language-model]] · [[sequence-to-function-model]] · [[genomic-tokenization]] · [[dallatorre-2025-nucleotide-transformer]] · [[dealmeida-2025-segmentnt]] · [[linder-2025-borzoi]] · [[avsec-2026-alphagenome]] · [[40-Topics/sequence-models-and-foundation-models]]
