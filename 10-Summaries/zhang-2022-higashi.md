---
type: summary
title: "Zhang, Zhou & Ma 2022 — Multiscale and integrative single-cell Hi-C analysis with Higashi"
source: "[[00-Sources/papers/Multiscale and integrative single-cell Hi-C analysis with Higashi]]"
source_kind: paper
author: "Ruochi Zhang, Tianming Zhou, Jian Ma (corresponding)"
published: 2021-10-11
ingested: 2026-08-10
doi: "10.1038/s41587-021-01034-y"
journal: "Nature Biotechnology"
tags: [Higashi, hypergraph, representation-learning, scHi-C, imputation, insulation-score, sn-m3C-seq, prefrontal-cortex]
entities: ["[[jian-ma]]"]
concepts: ["[[single-cell-hi-c]]", "[[imputation]]", "[[topologically-associating-domain]]", "[[chromatin-compartments]]", "[[multimodal-integration-methods]]", "[[dimensionality-reduction]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]", "[[single-cell-multiomics]]"]
---

**Citation:** Zhang, Zhou & Ma (2022) — *Multiscale and integrative single-cell Hi-C analysis with Higashi* — *Nature Biotechnology* 40, 254–261. [DOI](https://doi.org/10.1038/s41587-021-01034-y)

# Zhang 2022 — Higashi

> Represent an entire scHi-C dataset as **one hypergraph**: cells and genomic bins are nodes, and every non-zero contact is a hyperedge joining {cell, locus₁, locus₂}. Embedding cells becomes node-embedding; imputing sparse contact maps becomes hyperedge prediction. Because the whole dataset is one structure, imputation for a cell can borrow from its neighbours in embedding space.

## Key claims

- **The architectural difference from [[zhou-2019-schicluster|scHiCluster]]**: scHiCluster treats each contact map as a separate graph and imputes it by random walk with restart; Higashi models all cells jointly, so **latent correlations across cells inform each imputation**. Built on the authors' Hyper-SAGNN hypergraph neural network.
- Practical consequence beyond accuracy: random-walk imputation requires **dense matrices in memory**, which is impractical at high resolution. The hypergraph formulation is sparse-native.
- **Embedding performance.** Evaluated on the 4DN sci-Hi-C, [[ramani-2017-scihi-c|Ramani]] and Nagano datasets at 1 Mb, Higashi embeddings consistently outperform HiCRep/MDS, scHiCluster and LDA across unsupervised metrics, for both categorical cell types and continuous cell states, and are robust to embedding dimension.
- **Imputation validated against imaging ground truth.** Multiplexed STORM imaging of a 2.5 Mb chr21 region in 11,631 cells at 30 kb was converted into simulated scHi-C maps at controlled coverage. Higashi with *k* = 0 (no cross-cell sharing) already beats scHiCluster; **Higashi(4) improves median similarity by 30–43% at the lowest coverage**, and 22–50% on a second imaging dataset. Downsampled real WTC-11 data gave up to **89% improvement** in distance-stratified Spearman correlation.
- **Single-cell A/B compartments.** After 50 kb imputation, merged correlation matrices show clear checkerboarding and per-cell compartment scores are directly comparable across the population. Genes in **more variable compartments have higher transcriptional variability** (*P* < 0.001 against WTC-11 scRNA-seq); the trend holds in 71% of 50 Mb sliding windows.
- **Single-cell TAD-like boundaries.** Per-cell insulation scores yield two distinct kinds of variability: boundaries **present or absent** across the population, and boundaries that **slide along the genome** between cells. More frequently occurring boundaries are stronger (lower insulation score) and have more and stronger CTCF peaks — matching the STORM imaging result. Differentially expressed genes across WTC-11 differentiation are over-represented near variable boundaries (*P* ≤ 7.9 × 10⁻⁸).
- **Multimodal integration.** On sn-m3C-seq from human prefrontal cortex, Hi-C alone resolves neuron subtypes (Pvalb, Sst, Vip, Ndnf, L2/3, L4–6) that scHiCluster could not; jointly modelling co-assayed methylation as a prediction target — not as network input — gives the best embeddings of all.
- Cell-type-specific biology recovered: ODC-specific boundaries (784 genes) are enriched for synapse GO terms via [[mclean-2010-great|GREAT]]; the *THBS2* boundary is visible per cell but **obscured in the pooled population map**; the *SULF1* boundary is present in 93.2% of L6 cells versus 65.3% of other excitatory neurons.

## Methods / evidence

The imaging-derived simulation is the strongest element: STORM traces give a physically measured per-cell 3D structure, so simulated contact maps have real ground truth rather than a downsampled bulk proxy. Supplemented by downsampling real data, comparison against 3D structure modelling, pooled-imputed-versus-true-bulk comparison, and sensitivity analyses on both embedding dimension and the neighbour count *k*. Includes an explicit batch-effect removal mechanism, used because one sn-m3C-seq batch had lower depth.

## Surprising or load-bearing bits

- **"Sliding" boundaries are a genuinely new observation.** Population Hi-C can only report a boundary as present or absent with some strength; per-cell insulation shows boundaries whose *position* shifts gradually between cells. That is a different model of what a boundary is — a distribution over positions rather than a fixed element — and it is invisible to any bulk method.
- **Borrowing across cells is a double-edged design.** Higashi(4) outperforms Higashi(0) substantially, which means much of the accuracy comes from *k*-nearest-neighbour smoothing in embedding space. The risk is circularity: cells are imputed toward their neighbours, so measured cell-to-cell variability is partly a function of the imputation. The authors show the effect is real by validating against imaging, but any variability claim from imputed data inherits this concern.
- **Co-assayed methylation as a target rather than an input** is a subtle and reusable choice — the network is asked to *predict* the second modality from conformation, so integration improves the conformation representation without letting methylation dominate the embedding. Compare the anchor-based strategies in [[argelaguet-2021-integration-principles]].
- **The pooled map actively hides real structure.** *THBS2*'s ODC-specific boundary vanishes in the population contact map. This is the 3D-genome instance of the general single-cell argument — the average is not any cell — and it parallels [[zahn-2017-dlp|DLP's]] finding that minor clones disappear from merged genomes.
- Higashi's cell-cycle handling is implicit: clusters of likely-mitotic cells appear in both the compartment and insulation heatmaps and are **removed before the transcription-correlation analyses**. Consistent with [[ramani-2017-scihi-c|sciHi-C's]] finding that cell-cycle state dominates scHi-C variation, and a reminder that it must be handled in every analysis.
- The compartment-variability-to-transcription-variability correlation (71% of windows) is close to the 76% baseline for bulk compartment-A-to-expression, which the authors state directly — an honest framing that keeps the result from being oversold.

## Entities mentioned

- [[jian-ma]] — corresponding author; the hypergraph/representation-learning program for 3D genomics.

## Concepts touched

- [[imputation]] — hypergraph hyperedge prediction as an alternative to random-walk smoothing.
- [[single-cell-hi-c]] — supplies the per-cell compartment and boundary analysis machinery the assays lacked.
- [[multimodal-integration-methods]] — co-assay integration by prediction target.

## Connections to other sources

- Direct comparison target: [[zhou-2019-schicluster]]; input assays: [[ramani-2017-scihi-c]], [[nagano-2013-nature]], [[lee-2019-natmethods]] (sn-m3C-seq).
- Features it resolves per cell: [[lieberman-aiden-2009-hic]] (compartments), [[dixon-2012-tads]] (domains, insulation).
- Downstream annotation: [[mclean-2010-great]]; storage/visualization: [[abdennur-2020-cooler]], [[kerpedjiev-2018-higlass]].
- Embedding/visualization machinery: [[mcinnes-2018-umap]].

## Open questions

- **How much of the reported cell-to-cell variability survives the imputation's own smoothing** is not fully separable — Higashi(0) results are reported and are weaker, but no analysis isolates the variability attributable to *k*-NN borrowing.
- Whether sliding boundaries reflect genuine per-cell positional variation or residual imputation uncertainty at boundary edges is not directly tested.
- The imaging-based ground truth covers a 2.5 Mb region on one chromosome and a 1 Mb-resolution chr2 dataset; generalization of the accuracy figures genome-wide is assumed.

## Related

- [[zhou-2019-schicluster]] · [[single-cell-hi-c]] · [[imputation]] · [[3d-genome]]
