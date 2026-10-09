---
type: summary
title: "Fang et al. 2025 — Evo2HiC: a multimodal foundation model for integrative analysis of genome sequence and architecture"
source: "[[00-Sources/papers/Evo2HiC- a multimodal foundation model for integrative analysis of genome sequence and architecture.pdf]]"
source_quality: full
source_sha256: "14dace2deb4649f2971cfbc89c44f3b75b8be205383e07b90254282e7a639d51"
source_kind: paper
author: "Tangqi Fang, Xiao Wang, Zhiping Xiao, Shengqi Hang, Ghulam Murtaza, Junwei Yang, … William Noble (corresponding), Sheng Wang (corresponding)"
published: 2025-11-19
ingested: 2026-10-08
doi: "10.1101/2025.11.18.689171"
journal: "bioRxiv preprint"
tags: [Evo2HiC, Evo-2, knowledge-distillation, dna-language-model, Hi-C, Micro-C, 3D-genome, contact-map-prediction, Hi-C-resolution-enhancement, epigenome-prediction, SigLIP, contrastive-learning, DNA-Zoo, cross-species, Orca, HiCARN, motif-attribution, preprint]
entities: []
concepts: ["[[dna-language-model]]", "[[sequence-to-function-model]]", "[[hi-c-normalization]]", "[[single-cell-hi-c]]", "[[topologically-associating-domain]]", "[[chromatin-loop]]", "[[transcription-factor-motif]]", "[[micro-c]]", "[[histone-modifications]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/3d-genome]]", "[[40-Topics/chromatin-architecture]]"]
---

**Citation:** Fang et al. (2025) — *Evo2HiC: a multimodal foundation model for integrative analysis of genome sequence and architecture* — bioRxiv preprint (posted 19 November 2025). [DOI](https://doi.org/10.1101/2025.11.18.689171)

# Fang 2025 — Evo2HiC

> Evo2HiC compresses the 7-billion-parameter DNA language model **Evo 2** into a **3.6 M-parameter CNN** that embeds DNA in 2 kb bins, and pairs it with a small CNN encoder for **bulk Hi-C** contact patches. Two SigLIP-style contrastive losses are trained jointly. The first pulls the CNN's embedding of each 2 kb bin toward the precomputed Evo 2 (layer 27) embedding of the same bin; this is sequence distillation. The second pulls the CNN's pairwise (row-bin + column-bin) DNA embedding toward the Hi-C-encoder embedding of the same 2 kb × 2 kb pixel; this is structure distillation. Evo 2 and Hi-C are never aligned directly, which keeps compute low. Pretraining uses human sequence only (hg38) and **138 human Hi-C/Micro-C maps from ENCODE and 4DN** (124 maps from 46 cell lines for training). The model has two modes: a sequence-only encoder, and a co-embedding that concatenates sequence and Hi-C embeddings. Task heads are a U-Net for contact maps and a transformer for epigenomic tracks. The paper reports better sequence-to-contact prediction than Orca, better epigenome prediction than Hi-C-only or Evo 2-only inputs, cell-type-specific motif attribution, and Hi-C resolution enhancement that transfers to 177 DNA Zoo species.

## Key claims

- **Distillation keeps Evo 2's geometry.** Pairwise similarities of 2 kb bins correlated r = 0.63 between Evo 2 and Evo2HiC on human chr10, against 0.13 for the same CNN trained without Evo 2. On mouse (never seen in training) the values were 0.47 and 0.14. Sequence-to-Hi-C-patch retrieval had higher recall and lower average rank with distillation, and the gain was larger in mouse.
- **About 500× cheaper.** Inference is up to 500-fold faster than Evo 2 at 70 kb input (< 0.02 s per sequence) and uses < 0.2 GB of memory. The paper also gives about a 2,000-fold reduction in parameters.
- **Sequence → contact map.** On 4 kb SCALE-normalised Micro-C from H1ESC (fully held out of pretraining) and HFF (test chromosomes held out), Evo2HiC beat Orca and an Evo 2-embedding + same-decoder ablation on distance-stratified Spearman correlation and insulation-score Pearson correlation. The abstract gives a **10.9% Spearman improvement over Orca**. The gap widened at longer genomic distances.
- **Hi-C + sequence → epigenome.** The five tracks were DNase, CTCF, H3K27ac, H3K27me3 and H3K4me3 at 2 kb, in GM12878 and H1ESC, with chr9/10 as test. The co-embedding improved Pearson correlation on average by 34.7% over a Hi-C-only model and 26.2% over Evo 2-only. On held-out K562 (cross-cell-type plus cross-chromosome), it won on 3 of 5 assays.
- **Cell-type-specific motifs.** DeepLiftShap attributions conditioned on each cell type's Hi-C map, scanned against the Vierstra footprint motif catalogue, recovered CTCF as a shared motif. They found SPIB, IRF2 and PRDM1 as GM12878-specific and RARG, GLI2 and YY1 as H1ESC-specific. Cell-type-specific motifs showed larger RNA-seq expression differences between the two lines than shared motifs, and K562 showed neither high expression nor attribution for them. Removing a loop from the input contact map switched an IRF2 site's predicted H3K27ac from active to inactive.
- **Resolution enhancement across species.** The input was 1/16 binomially downsampled Hi-C plus sequence, trained on human at 2 kb with a multi-resolution MSE. Evo2HiC was best on all four metrics on 14 held-out human maps. On 11 mouse maps it gained +5.9% Spearman and +2.5% SSIM over the best competitor. Across 177 DNA Zoo species, which span mammals, marsupials, reptiles, fish, protostomes and angiosperms, it beat HiCARN2 on 157.

## Methods / evidence

DNA encoder: seven 1D residual blocks adapted from Orca, taking one-hot DNA plus a mappability track and pooling to 2 kb. The 2D embedding is the sum of the row-bin and column-bin embeddings, passed through a multi-resolution module (pool sizes 1/2/4/5). Hi-C encoder: multi-kernel (3/7/15) cross-embedding plus two multi-resolution residual blocks, d = 128. Evo 2 embeddings were precomputed on 60 kb windows with a 50 kb stride, dropping the first 10 kb because of causal masking, for both strands (concatenated, 8,192-d). Pretraining sampled 200 kb windows, with 500 kb near-diagonal Hi-C submatrices averaged over eight maps per step. It ran 50k steps on 4 × A100. Splits: chr8 for validation and chr9/10 for test everywhere; 14 human maps from 6 cell lines and 11 mouse maps from 4 lines held out entirely. Code and weights: github.com/CHNFTQ/Evo2HiC (Apache 2.0).

Weight: a careful design with explicit ablations (no-Evo 2 CNN; Evo 2 embeddings with the same decoder). But most comparisons appear only as figures with significance stars, and the main text gives only the relative gains quoted above. The Orca comparison uses Orca's published predictions rather than a retrained Orca. Resolution-enhancement baselines (HiCNN, HiCARN1/2) are sequence-free, so the comparison partly measures the value of adding sequence. (synthesis)

## Limitations

**Authors' own:**
- Only Evo 2 is distilled. Distilling from several DNA foundation models might improve robustness.
- Epigenome prediction does not yet extend to RNA-seq or expression.
- Evo 2 was frozen during embedding extraction because fine-tuning it is too expensive. Parameter-efficient adaptation of Evo 2 with Hi-C is left for future work.

**Reviewer notes:** (at most three, each marked `(synthesis)`)
- All Hi-C inputs are **bulk** maps, with low coverage simulated by downsampling. Real single-cell Hi-C sparsity (about 10⁴–10⁶ contacts per cell, cell-to-cell structural variation) is not tested. Whether the sequence prior helps scHi-C imputation is still open. (synthesis)
- The epigenome-prediction baselines are internal ablations (Hi-C-only, Evo 2-only). External sequence-to-function models such as Enformer or Borzoi, or Hi-C-aware predictors such as C.Origami, are not compared. (synthesis)
- Text and captions disagree in places. Fig. 1 says "56 biosamples" while Methods give 46 training plus 6 test human cell lines plus 4 mouse lines. The Fig. 5a caption names "GM12878 and K562" while the text and panels compare GM12878 and H1ESC. (synthesis)

## Surprising or load-bearing bits

- **Hi-C as a distillation filter.** Rather than compress Evo 2 in full, the structure loss steers the 2,000× smaller student toward the sequence features that predict contacts. This is a cheap way to make a giant DNA language model usable genome-wide for one task. (synthesis)
- **Human-only distillation transfers across the tree of life.** The student never saw non-human sequence or Evo 2's non-human embeddings, yet it improved Hi-C enhancement in 157 of 177 species, including plants and insects. The authors credit Evo 2's multi-species pretraining being inherited through distillation.
- **Counterfactual loop removal.** Editing the input contact map to delete a loop changed the predicted histone mark at a motif site. This gives a structure-conditioned way to call motif sites active or inactive, which sequence-only models cannot do.

## Concepts touched

- [[dna-language-model]] — Evo 2 (7B) distilled into a 3.6 M CNN; the embedding geometry is largely kept and transfers cross-species.
- [[sequence-to-function-model]] — sequence → contact map (vs Orca) and sequence + Hi-C → five epigenomic tracks.
- [[topologically-associating-domain]] / [[chromatin-loop]] — insulation-score accuracy; loop-ablation counterfactual.
- [[micro-c]] — 4 kb H1ESC and HFF Micro-C maps as the contact-prediction targets.
- [[hi-c-normalization]] — SCALE-normalised targets; multi-resolution loss for 2 kb sparsity.
- [[single-cell-hi-c]] — relevant by analogy: sparse-contact enhancement with a sequence prior, tested here only on downsampled bulk maps. (synthesis)
- [[transcription-factor-motif]] — DeepLiftShap + Vierstra motif catalogue for cell-type-specific motifs.

## Connections to other sources

- Main sequence → 3D baseline: [[zhou-2022-orca]] (the DNA encoder architecture is adapted from Orca). Related sequence-only 3D predictor: [[fudenberg-2020-akita]].
- Other Hi-C foundation model in this ingest: [[wang-2026-hicfoundation]], trained on contact maps alone rather than distilled from a DNA LM. (synthesis)
- DNA LMs it names as alternatives to distil: [[ji-2021-dnabert]], [[zhou-2023-dnabert-2]], [[dallatorre-2025-nucleotide-transformer]].
- Epigenome-prediction context: sequence-only predictors such as [[avsec-2021-enformer]] and [[linder-2025-borzoi]] are not benchmarked. (synthesis)
- Hi-C foundations: [[rao-2014-in-situ-hic]], [[hsieh-2015-micro-c]], [[dixon-2012-tads]]. Single-cell Hi-C imputation for contrast: [[zhang-2022-higashi]], [[zhou-2019-schicluster]].

## Open questions

- Would the Hi-C co-embedding help impute real scHi-C cells, where coverage is far lower than 1/16 downsampling and the structure is cell-specific? (synthesis)
- How much of the 177-species gain comes from sequence features rather than the Hi-C encoder? A Hi-C-only ablation on DNA Zoo is not shown. (synthesis)
- Does distilling a newer or larger DNA LM, or several of them as the authors propose, improve on Evo 2 for 3D tasks? (synthesis)

## Related

- [[dna-language-model]] · [[sequence-to-function-model]] · [[zhou-2022-orca]] · [[wang-2026-hicfoundation]] · [[single-cell-hi-c]] · [[hi-c-normalization]] · [[topologically-associating-domain]] · [[40-Topics/3d-genome]] · [[40-Topics/sequence-models-and-foundation-models]]
