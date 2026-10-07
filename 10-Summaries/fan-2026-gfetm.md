---
type: summary
title: "Fan et al. 2026 — GFETM: Genome foundation-based embedded topic model for scATAC-seq modeling"
source: "[[00-Sources/papers/GFETM_ Genome foundation-based embedded topic model for scATAC-seq modeling]]"
source_kind: paper
author: "Yimin Fan, Adrien Osakwe, Shi Han, Yu Li, Jun Ding, Yue Li (lead contact)"
published: 2026-05
ingested: 2026-10-07
updated: 2026-10-07
doi: "10.1016/j.cels.2026.101563"
journal: "Cell Systems 17(5):101563"
tags: [GFETM, scATAC-seq, genome-foundation-model, embedded-topic-model, ETM, VAE, DNABERT, sequence-informed, transfer-learning, zero-shot, partial-clipping]
entities: []
concepts: ["[[scatac-seq]]", "[[latent-dirichlet-allocation]]", "[[cistopic]]", "[[convolutional-neural-network]]", "[[dimensionality-reduction]]", "[[scatac-imputation]]", "[[transcription-factor-motif]]", "[[batch-effect]]"]
topics: ["[[single-cell-atac-seq]]", "[[computational-methods]]"]
---

**Citation:** Fan et al. (2026) — *GFETM: Genome foundation-based embedded topic model for scATAC-seq modeling* — *Cell Systems* 17(5):101563. [DOI](https://doi.org/10.1016/j.cels.2026.101563)

# Fan 2026 — GFETM

> **Clipping caveat (still partial after the 2026-10-07 re-clip):** the source is a ScienceDirect page that the clipping institution does not subscribe to. It holds the keywords, the full Introduction, the first sentences of the Method overview and Discussion, the STAR Methods front matter (lead contact, data/code availability, key resources table), funding, author contributions and the first ~38 of 78 references. It has **no Results, figures, benchmark tables, metrics or numbers**. The re-clip adds little over the first clipping beyond the keywords, a Zenodo code record and the funding text. Every performance statement below is the authors' claim from the Introduction, not checked evidence.
>
> GFETM joins two ideas. One is an **embedded topic model (ETM)**: a topic model implemented as a VAE, whose encoder maps each cell's peak vector to a cell-topic mixture and whose **linear decoder** keeps topics interpretable. The other is a pretrained **genome foundation model (GFM)** that embeds each peak's DNA sequence. The two are **jointly optimised**, so sequence knowledge from large-scale self-supervised pretraining is "integrated and adapted" into the topic model. The argument is that current sequence-informed scATAC models (scBasset, CellSpace) cannot generalise to unseen cells and see only short-range sequence context through k-mers, motifs or CNNs, while GFMs bring attention-based global context and transfer.

## Key claims

- **Two families of scATAC methods.** *Sequence-free* methods (PCA, Cicero, SCALE, PeakVI, cisTopic) treat the data as a peak-by-cell count matrix and ignore the DNA under each peak. The authors say this omission "can lead to sub-optimal performance". *Sequence-informed* methods (chromVAR, BROCKMAN, CellSpace, SIMBA, scBasset) encode peak sequence.
- **Two limitations of current sequence-informed methods.** First, scBasset and CellSpace "can only make inferences on cells seen during training", while transfer to unseen cells is needed for small understudied diseases and tissues. Second, existing methods use k-mer or TF-motif features or CNNs, which "are limited to short-range sequence context".
- **Three hypothesised advantages of GFMs.** (i) Self-supervised pretraining on vast unlabelled genomic data gives richer, more generalisable features, unlike the supervised CNN of scBasset. (ii) Larger parameter count and capacity for large datasets. (iii) Attention captures global sequence dependencies and gives interpretable attention maps. GFMs have already done well on genomics tasks including predicting chromatin profiles.
- **Architecture (from the truncated Method overview).** The ETM component takes the cell-by-peak matrix; the GFM component takes peak-specific nucleotide sequences. The ETM encoder projects each cell's peak vector to a latent cell-topic mixture through a two-layer MLP, which is passed to the linear ETM decoder "and combined with the" (the clipping cuts off here). GFMs cited: DNABERT, DNABERT-2, Nucleotide Transformer, HyenaDNA. ETM lineage: ETM → scETM (scRNA-seq) → moETM (single-cell multi-omics).
- **Claimed capabilities (Introduction only; no numbers in clipping).** State-of-the-art cell clustering; high scalability on large datasets "due to its batch-agnostic embeddings and ability to infer cell states"; imputation of peak accessibility on **unseen chromosome regions**; denoising of raw scATAC to enhance regulatory signals; knowledge transfer **across tissues, species and omics**; and, through zero-shot inference and post hoc attention analysis, capture of cell-state TF activities.
- **Motivating data problems.** Peak callers detect millions of highly variable peaks in datasets of millions of cells, giving a high-dimensional, sparse cell-by-peak matrix. scATAC has fewer reads per cell than scRNA-seq and OCRs much larger than transcribed regions, hence lower signal-to-noise. Cross-tissue and cross-species integration is well explored for scRNA-seq but hard for scATAC, which lacks a common feature set (the role genes play in scRNA-seq).
- **Stated main contribution (Discussion opening).** "Compared with existing methods, our main contribution is the use of a pre-trained GFM to learn sequence embeddings that help model scATAC-seq data."

## Methods / evidence

Datasets in the key resources table: human HSC differentiation (Buenrostro et al., GSE96772); 10x Genomics multiome PBMC (granulocyte-sorted 3k) and E18 mouse brain (fresh 5k); Catlas-human (Zhang et al., GSE184462); Cusanovich-mouse (GSE111586); and a myocardial dataset (Kuppe et al., CELLxGENE). All are existing public data; no new materials were generated. Code: github.com/fym0503/GFETM and Zenodo record 18052308. Per the author contributions, Y.F. implemented the software and ran the experiments, and A.O. "ran several baseline methods". Which baselines and which metrics are not visible.

Weight: **cannot be assessed from this clipping.** The architecture is described only up to the decoder, and no result is shown. Treat every performance claim as unverified until the Results are available. (synthesis)

## Surprising or load-bearing bits

- **Peak sequence as the shared feature for transfer.** If peaks are represented by the embedding of their DNA instead of their genomic coordinates, datasets with different peak sets, or different species, share a feature space. That fits the authors' stated cross-species obstacle (no common feature set) and is the likely route to their cross-species claim. (synthesis)
- **Imputing "unseen chromosome regions"** implies that accessibility can be predicted from sequence alone at held-out loci. This is the scBasset-style sequence-to-accessibility mapping placed inside a generative topic model. (synthesis)
- **Interpretability kept by design.** The linear decoder means topics stay as peak-loading vectors comparable to cisTopic/LDA topics, while the encoder and peak-embedding side gain deep-learning capacity. (synthesis)
- **Hints of unseen analyses in the reference list.** The visible references include kidney disease genes (ADAMTS2/3/14, PTPRO, FGF1, SLC12A1), genome-wide TF-binding maps in human HSPCs, a TCF4-dependent regulatory network in melanoma, fallopian tube/ovary and developing-cortex scATAC atlases, and cross-species scRNA integration work (SATURN, a cross-species benchmark). These suggest kidney, haematopoietic and cross-species case studies in the missing Results, but the clipping does not show them. (synthesis)

## Concepts touched

- [[scatac-seq]] — a sequence-informed, transferable representation model for scATAC.
- [[latent-dirichlet-allocation]] / [[cistopic]] — the topic-model lineage; ETM is an embedding-space topic model implemented as a VAE, and cisTopic is placed in the sequence-free family.
- [[convolutional-neural-network]] — cast as the short-range, supervised predecessor (scBasset) that GFMs are meant to replace.
- [[transcription-factor-motif]] — k-mer and motif features are criticised as short-range; TF activity is said to be recovered through attention analysis rather than motif scanning.
- [[scatac-imputation]] — imputation at unseen regions and denoising claimed as capabilities.
- [[batch-effect]] — "batch-agnostic embeddings" claimed, without detail in the clipping.
- [[dimensionality-reduction]] — the cell-topic mixture is the low-dimensional cell representation.

## Connections to other sources

- Sequence-free methods it positions against: [[bravo-2019-cistopic]], [[xiong-2019-scale]], [[pliner-2018-cicero]], [[ashuach-2022-peakvi]]. Sequence-informed predecessors: [[yuan-2022-scbasset]], [[schep-2017-chromvar]], [[de-boer-2018-brockman]], [[tayyebi-2024-cellspace]]. Whether any of these were run as benchmarks is not visible.
- GFETM's critique of CellSpace (no inference on unseen cells; short-range k-mer context) is a direct response to [[tayyebi-2024-cellspace]]. (synthesis)
- Foundation-model framing parallels [[cui-2024-natmethods]] (scGPT) on the transcriptome side. (synthesis)
- Benchmark context for scATAC embedding methods: [[luo-2024-scatac-benchmark]]. The combinatorial-indexing paper [[cusanovich-2015-sciatac]] appears in GFETM's reference list; the Cusanovich-mouse dataset it uses (GSE111586) probably corresponds to "A Single-Cell Atlas of In Vivo Mammalian Chromatin Accessibility" (*Cell* 2018), also in the reference list. (synthesis)

## Open questions

- What are the actual effect sizes against cisTopic, SCALE, PeakVI and scBasset, and on which metrics? Not in this clipping; still needs a full-text (institutional or PMC) copy.
- How is the GFM peak embedding combined with the topic embeddings in the decoder, and is the GFM fine-tuned end to end or partially frozen? The Method overview is cut off at this point. (synthesis)
- How much of the gain comes from the GFM and how much from joint fine-tuning? Is a frozen GFM enough? (synthesis)
- Does cross-species transfer hold for distantly related genomes, where sequence embeddings of orthologous regulatory elements may diverge? (synthesis)

## Related

- [[scatac-seq]] · [[cistopic]] · [[yuan-2022-scbasset]] · [[tayyebi-2024-cellspace]] · [[40-Topics/single-cell-atac-seq]]
