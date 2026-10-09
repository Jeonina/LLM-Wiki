---
type: summary
title: "Gao et al. 2024 — EpiGePT: a pretrained transformer-based language model for context-specific human epigenomics"
source: "[[00-Sources/papers/EpiGePT_ a pretrained transformer-based language model for context-specific human epigenomics]]"
source_quality: full
source_sha256: "b5cfa7018469e6066a9b96aae733808f3fba859ec7697894b1b528bc6f23330b"
source_kind: paper
author: "Zijing Gao, Qiao Liu, Wanwen Zeng, Rui Jiang, Wing Hung Wong"
published: 2024-12-18
ingested: 2026-10-08
doi: "10.1186/s13059-024-03449-7"
journal: "Genome Biology"
tags: [EpiGePT, sequence-to-function, transformer, context-specific, TF-expression, cross-cell-type, DNase-seq, histone-marks, CTCF, HiChIP, attention, enhancer-promoter, variant-effect, eQTL, ClinVar, COVID-19, Enformer, ENCODE]
entities: ["[[20-Entities/rui-jiang]]", "[[20-Entities/wing-hung-wong]]"]
concepts: ["[[sequence-to-function-model]]", "[[variant-effect-prediction]]", "[[chromatin-accessibility]]", "[[dnase-seq]]", "[[chip-seq]]", "[[chromatin-loop]]", "[[cis-regulatory-element]]", "[[gene-regulatory-network]]", "[[transcription-factor-motif]]", "[[pseudo-bulk]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/histone-modifications]]", "[[40-Topics/3d-genome]]"]
---

**Citation:** Gao et al. (2024) — *EpiGePT: a pretrained transformer-based language model for context-specific human epigenomics* — *Genome Biology*. [DOI](https://doi.org/10.1186/s13059-024-03449-7)

# Gao 2024 — EpiGePT

> EpiGePT makes a sequence-to-function model **conditional on cellular context**, so it can predict epigenomic tracks in cell types it was not trained on. Context is a 711-dimensional TF vector: for each 128-bp bin, the HOMER motif score of each HOCOMOCO TF times that TF's expression (quantile-normalised log TPM from bulk RNA-seq) in the context. A five-block CNN compresses 128 kb of sequence into 1,000 bin tokens, each token is concatenated with its TF vector (968 dimensions total), and a transformer encoder (12–16 layers, 8 heads, 71.3 M parameters) predicts eight signals per bin: DNase, CTCF, H3K27ac, H3K4me3, H3K36me3, H3K27me3, H3K9me3 and H3K4me1. Each (region, context) pair is a training example, and a masked loss lets contexts with missing assays still contribute. An optional loss term aligns attention maps with HiChIP loops (EpiGePT-3D). The headline is cross-cell-type prediction (DNase PCC 0.787 in new cell types) and better-than-Enformer performance on held-out contexts, enhancer–promoter links from attention, and variant scoring.

## Key claims

- **Cross-cell-type DNase prediction.** On ENCODE DNase-seq from 129 contexts and 1,175,374 regions, EpiGePT beat BIRD, ChromDragoNN and DeepCAGE in cross-region, cross-cell-type and cross-both settings. Cross-cell-type PCC was 0.787, 6.9% above ChromDragoNN. Binary accessibility auPRC was 0.767 vs 0.623 (DeepCAGE) and 0.476 (ChromDragoNN). Against ChromHMM functional states it had 8.1% higher auROC than ChromDragoNN.
- **Versus Enformer.** An Enformer retrained on the same DNase data was 3.3–5.2% lower in median PCC; one retrained on the eight signals was 12.3% lower in mean PCC. Against the published pretrained Enformer on 19 held-out contexts (78 matched tracks), EpiGePT had higher PCC on 60 of 78 tracks, mean 0.510 vs 0.440, and DNase 0.710 vs 0.455. The authors note this compares EpiGePT's out-of-sample predictions with Enformer's in-sample ones.
- **Mouse transfer.** Using 688 shared TFs, zero-shot PCC on mouse brain, lung and kidney DNase was 0.330–0.422. Fine-tuning raised PCC by 18.1–19.5%.
- **Attention as enhancer–promoter evidence.** Without 3D training, attention scores beat Enformer on CRISPRi enhancer–gene pairs (Gasperini auPRC 0.647–0.887 by distance; Fulco 0.504 vs 0.307 at 30–45 kb), silencer–promoter pairs (auROC 0.575 vs 0.483 at 32–64 kb) and HiChIP loops (GM12878 auPRC 0.520 vs 0.484 at 40–64 kb).
- **HiChIP-guided training (EpiGePT-3D).** A cosine-similarity loss between last-layer attention rows and row-normalised HiChIP contact rows (4,107,687 H3K27ac loops, 13 contexts, K562 and GM12878 held out) raised cross-cell-type PCC by 3.3% and Gasperini auPRC at 24–40 kb from 0.652 to 0.695.
- **Fine-tuned E-P classifier.** Freezing EpiGePT and training a two-layer MLP on anchor embeddings gave auROC 0.982 vs 0.886 (DeepTACT) and 0.694 (k-mer MLP) for GM12878 loops at 0–20 kb.
- **TF–target ranking.** Gradients of predicted signals with respect to TF inputs (GIS) rank POU5F1 3rd of 711 for *ESRRB* in ESC context. Known TRRUST regulators ranked at a median percentile of 3.1% vs 20.4% by expression alone (GRNdb: 6.3% vs 36.0%).
- **Variants.** On 20,913 fine-mapped GTEx eQTL variant–gene pairs, random-forest classifiers on EpiGePT log-ratio scores beat Enformer (lung auPRC 0.922 vs 0.873). Swapping in stomach TF expression dropped lung to 0.892. Adding EpiGePT features to CADD raised ClinVar pathogenic-vs-benign auROC from 0.772 to 0.806. COVID-19 GWAS SNPs ranked at mean 0.250 among nearby benign SNPs with a lung TF profile, near 0.5 with K562 or testis.
- **Ablations.** Removing the TF module dropped cross-cell-type DNase PCC from 0.787 to 0.74. Removing the sequence module cost 0.084 PCC. Single-task models were worse than multi-task (H3K4me1 0.408 → 0.329). More training contexts helped steadily.

## Methods / evidence

All training data are bulk ENCODE: DNase from 129 contexts (hg19, 200-bp bins, 50-bin input for the DNase-only model), eight signals from 28 complete contexts (hg19) and 104 contexts with missing assays (hg38, 15,870 regions of 128 kb). Five-fold cross-validation by cell type. Baselines: BIRD, ChromDragoNN, DeepCAGE, Enformer (retrained and pretrained), DeepTACT and a 5-mer MLP. HiChIP loops from HiChIPdb (FitHiChIP 5 kb, q < 0.001). A web server (EpiGePT-online) and code (GitHub, MIT) are provided.

Weight: many comparisons, mostly on ENCODE cell lines. Most numbers sit in figures and supplementary files that are images or downloads in the clipping; values here are those stated in the text. Downstream variant tasks use separately trained random forests or MLPs on EpiGePT features, so they test feature usefulness, not zero-shot scoring.

## Limitations

**Authors' own:**
- Does not include chromatin regulators or DNA methylation; both are proposed extensions.
- 3D data exist for few contexts; imputation of missing 3D data is suggested.
- Cross-species use has limits (mouse, plants and fungi discussed).
- Performance falls as more TF expression values are missing; the authors provide guidance for building TF profiles from similar contexts.
- Single-cell data are not used; the authors propose adding it as pseudo-bulk.

**Reviewer notes:**
- The context vector is built from bulk RNA-seq of the same context, so "new cell type" means a new context with expression data. It is not sequence-only generalisation. (synthesis)
- The pretrained-Enformer comparison mixes out-of-sample EpiGePT with in-sample Enformer and uses EpiGePT's 128-kb window. It is fair in direction but not like-for-like. (synthesis)
- The clipped Methods have small errors: the one-hot code lists A and T with the same vector, the GIS input is described as "128 kbp upstream and downstream" while the model takes 128 kb, and the ClinVar text calls benign SNPs "positive samples". (synthesis)

## Surprising or load-bearing bits

- **Context as input, not as output head.** Enformer-style models fix cell types as output tracks. EpiGePT moves context into the input via TF expression × motif scores, which is what allows predictions for unseen contexts and multiplies training examples.
- **Supervising attention with 3D contacts.** The HiChIP loss is a soft constraint that leaves the architecture unchanged; it improves both tracks and E-P prediction.
- **Context choice changes variant scores.** The same SNPs score differently with lung, stomach, K562 or testis TF profiles, which is the intended behaviour.

## Entities mentioned

- [[20-Entities/rui-jiang]] — co-author (Tsinghua; HiChIPdb, SilencerDB and OpenAnnotate resources come from this group).
- [[20-Entities/wing-hung-wong]] — co-author (Stanford).

## Concepts touched

- [[sequence-to-function-model]] — context-conditioned seq-to-function transformer.
- [[variant-effect-prediction]] — eQTL, ClinVar and GWAS scoring through log-ratio features.
- [[chromatin-accessibility]] / [[dnase-seq]] — main benchmark target.
- [[chip-seq]] — CTCF and six histone marks as joint outputs.
- [[chromatin-loop]] / [[cis-regulatory-element]] — attention-derived enhancer–promoter and silencer–promoter links; HiChIP-guided training.
- [[gene-regulatory-network]] / [[transcription-factor-motif]] — gradient-based TF–target ranking.
- [[pseudo-bulk]] — proposed route for adding single-cell data.

## Connections to other sources

- Main baseline: [[avsec-2021-enformer]]. Same broad family as [[zhou-2015-deepsea]], [[kelley-2018-basenji]] and [[linder-2025-borzoi]], which fix cell types as outputs. (synthesis)
- Context-conditioning by TF expression is shared with [[fu-2025-get]], which conditions on cell-type accessibility instead of TF expression and predicts expression rather than chromatin marks. (synthesis)
- The 3D component relates to Hi-C-based sequence models [[fudenberg-2020-akita]] and [[zhou-2022-orca]], and to [[wang-2026-hicfoundation]]. (synthesis)
- Single-cell extensions of the same idea appear in [[hingerl-2025-scooby]] (cell embedding as context) and [[lal-2026-decima]] (pseudobulk outputs). (synthesis)

## Open questions

- Does the TF-expression context work with scRNA-seq pseudobulks, as the authors propose, or is it too noisy at that resolution?
- How much of the cross-context gain comes from TF expression versus motif scores? The ablations remove both or replace TF scores but do not separate them in the text.
- Would 3D-guided attention help in contexts with no HiChIP at all, beyond the two held-out lines? (synthesis)

## Related

- [[sequence-to-function-model]] · [[variant-effect-prediction]] · [[avsec-2021-enformer]] · [[fu-2025-get]] · [[chromatin-loop]] · [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/histone-modifications]] · [[40-Topics/3d-genome]]
