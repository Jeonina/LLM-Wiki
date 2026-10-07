---
type: summary
title: "Fan et al. 2026 — GFETM: Genome foundation-based embedded topic model for scATAC-seq modeling"
source: "[[00-Sources/papers/GFETM_ Genome foundation-based embedded topic model for scATAC-seq modeling]]"
source_kind: paper
author: "Yimin Fan, Adrien Osakwe, Shi Han, Yu Li, Jun Ding, Yue Li (lead contact)"
published: 2026-05
ingested: 2026-10-07
doi: "10.1016/j.cels.2026.101563"
journal: "Cell Systems 17(5):101563"
tags: [GFETM, scATAC-seq, genome-foundation-model, embedded-topic-model, ETM, VAE, DNABERT, sequence-informed, transfer-learning, zero-shot, abstract-only-clipping]
entities: []
concepts: ["[[scatac-seq]]", "[[latent-dirichlet-allocation]]", "[[cistopic]]", "[[convolutional-neural-network]]", "[[dimensionality-reduction]]", "[[scatac-imputation]]", "[[transcription-factor-motif]]"]
topics: ["[[single-cell-atac-seq]]", "[[computational-methods]]"]
---

**Citation:** Fan et al. (2026) — *GFETM: Genome foundation-based embedded topic model for scATAC-seq modeling* — *Cell Systems* 17(5):101563. [DOI](https://doi.org/10.1016/j.cels.2026.101563)

# Fan 2026 — GFETM

> **Clipping caveat:** the ingested source is a paywalled ScienceDirect landing page. It holds the introduction, a truncated method overview, discussion and key-resources snippets, and the reference list, but **no results, figures or numbers**. Everything below about performance is the authors' stated claim, not checked evidence.
>
> GFETM joins two ideas. One is an **embedded topic model (ETM)**: a VAE whose encoder maps each cell's peak vector to a cell-topic mixture and whose **linear decoder** keeps topics interpretable. The other is a pretrained **genome foundation model (GFM)** that embeds each peak's DNA sequence. The two are **jointly optimised**, so sequence knowledge from large-scale self-supervised pretraining shapes the peak embeddings the topic model uses. The pitch is that sequence-informed scATAC models (scBasset, CellSpace) cannot generalise to unseen cells and see only short-range sequence context through k-mers, motifs or CNNs, while GFMs bring attention-based long-range context and transfer.

## Key claims

- **Two families of scATAC methods.** *Sequence-free* methods (PCA, Cicero, SCALE, PeakVI, cisTopic) treat data as a cell × peak count matrix and ignore the DNA underneath. *Sequence-informed* methods (chromVAR, BROCKMAN, CellSpace, SIMBA, scBasset) encode peak sequence.
- **Two limitations of current sequence-informed methods.** scBasset and CellSpace "can only make inferences on cells seen during training". Existing methods use k-mers, TF motifs or CNNs, which "are limited to short-range sequence context".
- **Three hypothesised advantages of GFMs.** (i) Self-supervised pretraining on vast unlabelled genomic data gives richer, more generalisable features, unlike supervised CNNs such as scBasset. (ii) Larger capacity. (iii) Attention captures global dependencies and yields interpretable attention maps.
- **Architecture.** The ETM component takes the cell × peak matrix; a two-layer MLP encoder gives a latent cell-topic mixture, passed to the linear ETM decoder. The GFM component takes peak nucleotide sequences. GFMs cited include DNABERT, DNABERT-2, Nucleotide Transformer and HyenaDNA. The ETM lineage is ETM → scETM (scRNA-seq) → moETM (multi-omics).
- **Claimed capabilities (no numbers in clipping).** State-of-the-art cell clustering; scalability via batch-agnostic embeddings; imputation of peak accessibility on **unseen chromosome regions**; denoising of raw scATAC; knowledge transfer **across tissues, species and omics**; zero-shot inference; and post hoc attention analysis that captures cell-state TF activity.
- **Motivating data problems.** Peaks number in the millions and the matrix is high-dimensional and sparse. scATAC has fewer reads per cell than scRNA-seq and larger features, hence lower signal-to-noise. Cross-species integration is hard because scATAC lacks a common feature set (genes play this role in scRNA-seq).

## Methods / evidence

Datasets in the key resources table: human HSC differentiation (Buenrostro et al., GSE96772), 10x PBMC and E18 mouse brain multiome, Catlas-human (Zhang et al., GSE184462), Cusanovich mouse atlas (GSE111586) and a myocardial dataset (Kuppe et al.). Baselines and metrics are not visible in the clipping. A.O. "ran several baseline methods" per the author contributions. Code: github.com/fym0503/GFETM.

Weight: **cannot be assessed from this clipping.** Treat every performance claim as unverified until the full text is ingested. (synthesis)

## Surprising or load-bearing bits

- **Peak sequence as the common feature for transfer.** If peaks are represented by the embedding of their DNA rather than by genomic coordinates, datasets with different peak sets, or different species, share a feature space. That is the stated route to cross-species scATAC transfer, which coordinate-based count matrices cannot offer. (synthesis)
- **Imputing "unseen chromosome regions"** implies a peak's accessibility pattern can be predicted from sequence alone at held-out loci. This is the scBasset-style sequence→accessibility mapping, now inside a generative topic model. (synthesis)
- **Interpretability kept by design.** The linear decoder means topics remain peak-loading vectors comparable to cisTopic/LDA topics, while the encoder side gains deep-learning capacity. (synthesis)

## Concepts touched

- [[scatac-seq]] — a sequence-informed, transferable representation model for scATAC.
- [[latent-dirichlet-allocation]] / [[cistopic]] — the topic-model lineage; ETM is an embedding-space topic model implemented as a VAE.
- [[convolutional-neural-network]] — positioned as the short-range, supervised predecessor (scBasset) that GFMs replace.
- [[scatac-imputation]] — imputation and denoising claimed as by-products.
- [[transcription-factor-motif]] — TF activity is recovered through attention analysis rather than motif scanning.

## Connections to other sources

- Sequence-free baselines it positions against: [[bravo-2019-cistopic]], [[xiong-2019-scale]], [[pliner-2018-cicero]]. Sequence-informed predecessors: [[yuan-2022-scbasset]], [[schep-2017-chromvar]], [[de-boer-2018-brockman]].
- Foundation-model framing parallels [[cui-2024-natmethods]] (scGPT) on the transcriptome side. (synthesis)
- Benchmark context for scATAC embedding methods: [[luo-2024-scatac-benchmark]]. The Cusanovich mouse atlas it uses was built with the combinatorial-indexing assay of [[cusanovich-2015-sciatac]]. (synthesis)

## Open questions

- What are the actual effect sizes against cisTopic / SCALE / scBasset, and on which metrics? Not available from this clipping.
- How much of the gain comes from the GFM and how much from joint fine-tuning? Is a frozen GFM enough? (synthesis)
- Does cross-species transfer hold for distantly related genomes, where sequence embeddings of orthologous regulatory elements may diverge? (synthesis)

## Related

- [[scatac-seq]] · [[cistopic]] · [[yuan-2022-scbasset]] · [[40-Topics/single-cell-atac-seq]]
