---
type: summary
title: "Wang et al. 2025 — OmniReg-GPT: a high-efficiency foundation model for comprehensive genomic sequence understanding"
source: "[[00-Sources/papers/Omnireg-gpt_ a high-efficiency foundation model for comprehensive genomic sequence understanding]]"
source_quality: full
source_sha256: "af031c467d56fb5a1b3efdd83dbb3d7bcd5efc71ec96e51a5b62e13882670c2f"
source_kind: paper
author: "Aowen Wang, Jiaqi Li, Hongyu Dong, Bocheng Xu, Qingyu Yin, Yanchao Xu, Jie Fu, Junbo Zhao"
published: 2025-11-19
ingested: 2026-10-08
doi: "10.1038/s41467-025-65066-7"
journal: "Nature Communications 16 (2025)"
tags: [OmniReg-GPT, DNA-language-model, decoder-only, local-global-attention, sliding-window-attention, RoPE, FlashAttention, BPE, T2T, gene-expression-prediction, Xpresso, Nvwa, scATAC-seq, Buenrostro2018, Hi-C, C.Origami, insulation-score, enhancer-design, CODA, STARR-seq, in-silico-mutagenesis, eQTL, ClinVar]
entities: []
concepts: ["[[dna-language-model]]", "[[sequence-to-function-model]]", "[[genomic-tokenization]]", "[[variant-effect-prediction]]", "[[scatac-seq]]", "[[chromatin-accessibility]]", "[[transcription-factor-motif]]", "[[topologically-associating-domain]]", "[[cis-regulatory-element]]", "[[hematopoietic-differentiation]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[single-cell-atac-seq]]", "[[3d-genome]]", "[[computational-methods]]"]
---

**Citation:** Wang et al. (2025) — *OmniReg-GPT: a high-efficiency foundation model for comprehensive genomic sequence understanding* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-025-65066-7)

# Wang 2025 — OmniReg-GPT

> OmniReg-GPT (Zhejiang University) is a 270M-parameter decoder-only DNA language model whose point is cheap long-context pre-training: 12 blocks of causal **sliding-window local attention** followed by 2 blocks of **global attention**, with GENA-LM's BPE tokenizer, RoPE and FlashAttention. That reduces attention cost from O(L²) to O(L·w), so 200 kb fits on one 32-GB V100 and pre-training on 20-kb windows of the human T2T assembly took 60 h on four RTX 3090s (about 5 billion tokens, 3 epochs). The paper's wider claim is that one pre-trained sequence model can be pushed, mostly with a frozen backbone and a linear head, across scales that usually need separate specialist models: regulatory-element classification, gene expression (bulk and single-cell), **single-cell chromatin accessibility**, 2-Mb **Hi-C contact maps**, and zero-shot enhancer design.

## Key claims

- **Hybrid attention beats both extremes.** At 5-kb and 20-kb inputs, 12 local + 2 global layers gave lower pre-training loss than 14 local-only or 14 full-attention layers. On one 32-GB V100 the architecture accommodated 200-kb inputs against 100 kb for GENA-BigBird, with higher training throughput despite roughly twice the parameters.
- **Short-sequence benchmarks.** On 13 NT-benchmark tasks (10 histone marks at 1 kb, 2 promoter sets at 300 bp, 1 enhancer set at 400 bp), OmniReg-GPT had the best MCC on 9 of 13 among human-genome-only models and the best aggregate on both histone and regulatory-element groups. On BEND it beat the other foundation models on all 7 CpG-methylation tasks (Wilcoxon P < 0.02) and all 18 histone marks (P < 2e-4). On DeepSEA it was slightly below DNABERT-2 overall for TF, histone and DHS AUROC, but better on some TF tasks (NRSF, BRF1) where DNABERT-2 fell below 0.8.
- **Window size helps distal elements.** Extending inputs to 1, 2 and 4 kb slightly lowered promoter performance while enhancer performance stayed stable; for distal enhancers specifically, F1 and recall rose with window size.
- **Variant tasks.** Fine-mapped eQTL classification (SuSiE PIP > 0.9 positive, < 0.01 negative) gave AUROC 0.724, 0.719 and 0.701 at 2, 6 and 10 kb, the best of the models tested. Pathogenic ClinVar SNPs against common gnomAD SNPs (MAF > 5%) gave AUROC 0.679 against GENA-BigBird 0.633, NT-v2 0.622, DNABERT-2 0.608 and HyenaDNA-32kb 0.497.
- **Cell-type-agnostic expression (Xpresso, 20 kb around the TSS, frozen backbone + regression head).** R² 0.55 for human and 0.65 for mouse, against DNABERT-2 0.11, HyenaDNA-32k 0.18, GENA-BigBird 0.23 and NT multispecies 0.27 for human — roughly double the next-best model.
- **Single-cell expression (Nvwa binarised atlases).** On the human atlas (134,557 cells, 97 cell types) average per-cell AUROC was 0.83 against DNABERT-2 0.75, with GENA-BigBird and HyenaDNA-32k failing to give usable results; mean per-gene AUROC was 0.70 for human. The classifier weight vectors clustered by cell type in t-SNE, scored by AMI.
- **Single-cell chromatin accessibility (Buenrostro 2018, 1,344-bp peak sequences, frozen backbone).** Mean AUROC 0.717 both per cell and per peak. Louvain clustering of the classifier weights beat scBasset, SnapATAC, ArchR and chromVAR on ARI, AMI and homogeneity. In-silico motif insertion recovered CEBPB activity in monocytes, GATA1 in MEPs and HOXA9 in HSCs; saturation mutagenesis of a 100-bp β-globin enhancer recovered GATA1 and KLF1 motifs, with their contribution rising along erythroid differentiation.
- **3D contacts (C.Origami's IMR-90 Hi-C, 2-Mb windows at 8,192-bp bins).** Using frozen embeddings as input to a C.Origami-style head, insulation-score Pearson correlations were 0.82 (train chr2), 0.85 (validation chr10) and 0.80 (test chr15); chromosome-wide median insulation correlations were 0.52 and 0.49. Distance-stratified correlation exceeded 0.6 within 1 Mb on chr10 and within 0.5 Mb on chr15.
- **Enhancer–promoter compatibility and design.** On Bergman et al.'s 1,000 × 1,000 enhancer–promoter STARR-seq matrix in K562, a Gamma model on zero-shot log-likelihoods attributed 20% of the variance to enhancer strength against 6% for Enformer's CAGE track (both explained 97% overall). Using CODA's oracle and two rounds of prompt-based generation, K562 designs improved activity by 1.3% then 30.5% over the best CODA sequence when seeded from optimisation-algorithm sources, and by 23.1% then 81.7% when seeded from natural DHS sequences; final-round gains were 33.8% (HepG2) and 5.4% (SK-N-SH) from algorithm seeds, 53.4% and 93.3% from natural seeds. Generated sequences shared only 40.75% then 23.76% identity with their seeds. TF-MoDISco on in-silico mutagenesis found 60, 51 and 62 motifs in K562, HepG2 and SK-N-SH, with GATA specific to K562, HNF1B/HNF4A to HepG2 and ASCL1 detected in SK-N-SH.

## Methods / evidence

Architecture: decoder-only, width 1,024, 12 local blocks (non-overlapping windows, each query attending within its window and the preceding one) and 2 global blocks, FlashAttention throughout, RoPE, mean-pooled final-layer tokens as the sequence embedding. Pre-training: human T2T v2 (GCF_009914755.1) cut into 20-kb "sentences", GENA's 32,000-token BPE vocabulary, autoregressive loss, AdamW, weight decay 0.001, batch 32, 3 epochs, 5,000 warm-up steps, peak LR 1e-4. Most downstream tasks freeze the backbone and train one linear or MLP head (LR 5e-3, batch 32); the NT and DeepSEA benchmarks use full fine-tuning (LR 2e-5, batch 16). NT-benchmark baseline numbers are taken from the Nucleotide Transformer paper rather than rerun. Code and weights are open (GitHub `wawpaopao/OmniReg-GPT`, Zenodo 10.5281/zenodo.16933275).

Weight: peer-reviewed, with a genuinely broad application sweep and mostly frozen-backbone probes, which makes the comparisons about representation quality rather than fine-tuning budget. The specialist comparisons are uneven: scBasset and C.Origami appear as baselines, but Enformer and Borzoi-class expression models are not fine-tuned on the Xpresso or single-cell tasks, and the enhancer designs were never tested experimentally. Figures are images in the clipping, so values not stated in the text could not be read.

## Limitations

**Authors' own:**
- Pre-training uses the human reference genome only; cross-species data and scaling-law-guided hyperparameter tuning (including the local-to-global layer ratio) are future work.
- Only one modality and a limited set of cell types; protein-level data and larger cell atlases are not integrated.
- Enhancer generation is shown only through CODA MinGap scores; experimental validation is still needed.
- No post-training context extension, so RoPE extrapolation far beyond the 20-kb pre-training length is untested.

**Reviewer notes:**
- The 3D and single-cell results come from task-specific heads over frozen embeddings, so they show embedding quality rather than that the language model itself models contacts or accessibility. (synthesis)
- The single-cell accessibility AUROC of 0.717 is reported without a matched per-cell/per-peak AUROC for scBasset, so only the clustering metrics are directly comparable. (synthesis)
- The expression comparison uses 20-kb windows for every model, which disadvantages baselines trained at 512 bp to 6 kb; the near-doubling of R² partly measures that mismatch. (synthesis)

## Surprising or load-bearing bits

- **Local + a couple of global layers was enough.** Two global blocks over 12 windowed ones beat full attention on pre-training loss while keeping linear cost, a cheaper route to long context than sparse attention or state-space models. (synthesis)
- **A generic DNA LM used for single-cell ATAC.** Freezing the backbone and training one classification layer per cell beat scBasset, SnapATAC, ArchR and chromVAR on clustering metrics, which puts a sequence foundation model directly in scBasset's and GFETM's territory.
- **Enhancer strength, not promoter strength.** Zero-shot log-likelihoods tracked enhancer contribution three times better than Enformer's CAGE track on the same compatibility data, which speaks to the known weakness of expression models on distal enhancers.
- **60 h on four consumer GPUs** for a 270M model with 20-kb context, in contrast to the thousands of A100-hours typical for this model class. (synthesis)

## Concepts touched

- [[dna-language-model]] — causal DNA LM with hybrid local/global attention for cheap long-context pre-training.
- [[sequence-to-function-model]] — frozen embeddings drive expression, accessibility and Hi-C heads, the usual territory of supervised specialist models.
- [[genomic-tokenization]] — reuses GENA-LM's 32k BPE vocabulary rather than training a new one.
- [[variant-effect-prediction]] — fine-mapped eQTL and ClinVar pathogenic-variant classification.
- [[scatac-seq]] / [[chromatin-accessibility]] — per-cell peak accessibility on Buenrostro 2018, with classifier weights as cell embeddings.
- [[transcription-factor-motif]] — motif insertion and in-silico mutagenesis recover CEBPB, GATA1, HOXA9, KLF1 and cell-type-specific motifs in designed enhancers.
- [[topologically-associating-domain]] — 2-Mb Hi-C maps and insulation scores from sequence embeddings.
- [[cis-regulatory-element]] — zero-shot prompt-based enhancer generation scored by the CODA oracle.
- [[hematopoietic-differentiation]] — Buenrostro 2018 as the single-cell testbed.

## Connections to other sources

- Baselines and predecessors: [[fishman-2025-gena-lm]] (tokenizer source and BigBird comparator), [[zhou-2023-dnabert-2]], [[dallatorre-2025-nucleotide-transformer]], [[nguyen-2023-hyenadna]], [[zhou-2015-deepsea]] (chromatin-profile labels), [[avsec-2021-enformer]] (CAGE comparison on enhancer–promoter compatibility).
- scATAC comparators: [[yuan-2022-scbasset]], [[fang-2021-snapatac]], [[granja-2021-archr]], [[schep-2017-chromvar]]; the dataset is [[buenrostro-2015-nature]]'s successor Buenrostro 2018, also used by [[fan-2026-gfetm]].
- Closest in ambition to [[fan-2026-gfetm]], which puts a genome foundation model inside an scATAC topic model; OmniReg-GPT instead keeps the backbone frozen and trains a per-cell classifier. (synthesis)
- Hi-C head follows C.Origami; related sequence-to-contact work in this wiki includes [[fudenberg-2020-akita]] and [[zhou-2022-orca]]. (synthesis)

## Open questions

- Would the model keep its advantage if baselines were given their native context windows on the expression tasks? (synthesis)
- Do the designed enhancers work in cells, or only against the CODA oracle? The authors list this as unfinished.
- The architecture supports 200-kb inputs but was pre-trained at 20 kb; without context extension, how much of the 2-Mb Hi-C result comes from the model rather than the convolutional head? (synthesis)

## Related

- [[dna-language-model]] · [[sequence-to-function-model]] · [[scatac-seq]] · [[yuan-2022-scbasset]] · [[fan-2026-gfetm]] · [[fishman-2025-gena-lm]] · [[40-Topics/sequence-models-and-foundation-models]]
