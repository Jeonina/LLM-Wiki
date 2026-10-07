---
type: summary
title: "Zhang et al. 2022 — Ultrafast and interpretable single-cell 3D genome analysis with Fast-Higashi"
source: "[[00-Sources/papers/Ultrafast and interpretable single-cell 3D genome analysis with Fast-Higashi]]"
source_quality: full
source_sha256: "829a48ac6c5819d6c91b47a6b0021587c8dc68c046b396699d3e56b6a1913070"
source_kind: paper
author: "Ruochi Zhang, Tianming Zhou, Jian Ma (corresponding)"
published: 2022-10
ingested: 2026-10-07
doi: "10.1016/j.cels.2022.09.004"
journal: "Cell Systems 13(10):798–807.e6"
tags: [Fast-Higashi, scHi-C, tensor-decomposition, PARAFAC2, core-PARAFAC2, meta-interactions, random-walk-with-restart, partial-RWR, embedding, rare-cell-types, sn-m3C-seq, Dip-C, sci-Hi-C, GPU]
entities: ["[[20-Entities/jian-ma]]"]
concepts: ["[[single-cell-hi-c]]", "[[imputation]]", "[[dimensionality-reduction]]", "[[chromatin-compartments]]", "[[topologically-associating-domain]]", "[[trajectory-inference]]", "[[dip-c]]", "[[batch-effect]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]"]
---

**Citation:** Zhang et al. (2022) — *Ultrafast and interpretable single-cell 3D genome analysis with Fast-Higashi* — *Cell Systems* 13(10):798–807.e6. [DOI](https://doi.org/10.1016/j.cels.2022.09.004)

# Zhang 2022 — Fast-Higashi

> scHi-C embedding methods were either memory-bound (scHiCluster stores every imputed dense map), slow (3DVI trains a VAE per chromosome per genomic distance; Higashi iterates over individual contacts in a hypergraph network), and none were interpretable. **Fast-Higashi** (Ma lab) represents each chromosome's contact maps as a 3-way tensor (bin × bin-feature × cell) and jointly decomposes all chromosomes with a generalised **core-PARAFAC2** model sharing only the cell dimension. Outputs are cell embeddings plus **"meta-interactions"** — aggregated contact patterns analogous to metagenes, each tied to embedding dimensions. Sparsity is handled by a **partial random walk with restart (RWR)** computed batch-wise inside the optimisation. It is reported ~40× faster than 3DVI and ~9× faster than Higashi, with equal or better embeddings.

## Key claims

- **Embedding quality**: on three complex-tissue datasets at 500 kb (human prefrontal cortex sn-m3C-seq, "Lee et al."; mouse hippocampus sn-m3C-seq, "Liu et al."; developing mouse brain Dip-C, "Tan et al."), Fast-Higashi had the highest or second-best scores on all metrics (modularity, ARI, AMI, micro/macro-F1) vs **Higashi, scHiCluster (updated version) and 3DVI**.
- **Layer-resolved excitatory neurons**: on PFC it separated Pvalb, Sst, Vip, Ndnf and L2–3, L4, L5, L6 neurons — described as the first separation of excitatory neurons of different layers from chromatin interactions alone. Higashi and scHiCluster separated most subtypes but excitatory layers weakly; 3DVI split only excitatory vs inhibitory; scHiCluster and 3DVI showed obvious batch effects.
- **Rare types**: in hippocampus, only Fast-Higashi separated CA3 from CA1 and found small VLMC, PC and EC clusters (others failed except Higashi). In PFC, sub-clusters matched finer methylation-derived subtypes (e.g. Sst CALB1 vs B3GAT2); Fast-Higashi and Higashi alone found the small UNC5B inhibitory cluster; Fast-Higashi had the highest mean silhouette on neuron subtypes. Downsampling contacts to 10–50% showed it more coverage-robust than Higashi.
- **Meta-interactions are biological**: on sci-Hi-C of four cell lines, the first meta-interaction captured shared contact patterns; cell-type-specific meta-interactions (weighted by mean loadings) resembled bulk-Hi-C differential maps (cell-type bulk minus four-line average), with the highest Spearman correlation to the matching cell type. In PFC, per-bin differential contact values from meta-interactions correlated positively with scRNA-seq marker-gene expression.
- **Refined developmental annotation**: in developing mouse brain, sub-clusters within interneurons and neonatal neurons were assigned via aggregated single-cell A/B values over marker genes — interneuron (A) ≈ Vip, (B) ≈ Pvalb/Sst; neonatal neuron (A) inhibitory, (B) excitatory — whereas the original neonatal neuron 1/2 labels did not show different distributions of neonatal-excitatory marker scA/B. Joint embedding with a P7–P28 visual cortex dataset filled in age-ordered inhibitory and excitatory trajectories; scHiCluster did not separate the two trajectories.
- **Not a Higashi replacement**: RWR imputation is efficient but limited; a Fast-Higashi-initialised Higashi performed better than either alone (tensor model described as a quasi-linear version of Higashi's hypergraph).
- **Lower-coverage sci-Hi-C** (1 Mb; two datasets): all four methods performed well; Fast-Higashi/Higashi best at isolating the small GM12878 cluster in one dataset, 3DVI best in the other (IMR90 vs HFFc6).

## Methods / evidence

Bin-wise form of core-PARAFAC2 with orthogonality constraints (bin-specific rotations along the feature dimension accommodate TAD-like structures whose interaction peaks shift across bins); coordinate descent with closed-form SVD updates and ALS for the PARAFAC core; GPU mini-batching over sparse COO tensors (a 10,000-cell human dataset at 500 kb makes chr1 a ~6 GB dense tensor). Partial RWR at batch size 64 (correlation with full RWR >0.9 at batch 32–64). Default R = 64. Runtime comparisons exclude data reformatting, disable imputation in 3DVI/Higashi, and parallelise competitors where possible.

Weight: developer benchmark against their own predecessor plus two others, on public datasets with labels from original studies; the "first layer separation" claim rests on UMAP inspection plus silhouette scores. Meta-interaction validation is correlative. Runtime fairness was explicitly addressed.

## Surprising or load-bearing bits

- **Interpretability by construction**: because each embedding dimension maps to a meta-interaction (a contact pattern), one can ask *which contacts* separate a cluster — something neural embeddings do not give directly.
- **A linear model matching or beating deep models** on cell-type delineation suggests scHi-C embedding quality has been limited by sparsity handling and scalability more than model expressiveness (synthesis).
- **Fine neuron subtypes from chromatin conformation alone** — chromatin structure carries cell-identity information down to cortical layer.

## Concepts touched

- [[single-cell-hi-c]] — a scalable, interpretable embedding approach; meta-interactions as a new analysis unit.
- [[imputation]] — partial RWR inside the optimisation trades imputation power for memory/speed.
- [[chromatin-compartments]] — aggregated scA/B values used to annotate sub-clusters.
- [[topologically-associating-domain]] — model constraints designed around variable TAD-like structures across cells.
- [[trajectory-inference]] — age-ordered neuronal branches recovered from joint embedding.

## Connections to other sources

- Predecessor and direct baseline: [[zhang-2022-higashi]]; follow-on from the same lab: [[xiong-2024-scghost]].
- Other baselines: scHiCluster [[zhou-2019-schicluster]]; 3DVI/scVI-3D [[zheng-2022-bandnorm-scvi-3d]].
- Data sources in the wiki: sn-m3C-seq [[lee-2019-natmethods]]; sci-Hi-C [[ramani-2017-scihi-c]]; Dip-C method [[tan-2018-science]].
- Review placing it among random-walk imputation methods: [[dautle-2025-schic-review]], [[hong-2025-sc3d-genome-review]].
- Parallel sparsity-vs-scale trade-offs in methylation imputation: [[liang-2026-scmeth-imputation-benchmark]].

## Open questions

- Partial RWR's limited imputation may miss fine features (e.g. single-cell TAD-like boundaries) that Higashi recovers; the best-of-both route (Fast-Higashi initialising Higashi) costs back the speed.
- Integration with co-assayed modalities (methylation in sn-m3C-seq, RNA) is proposed but not implemented.
- Meta-interactions are validated against bulk differential maps and expression correlation, not perturbation (synthesis).

## Related

- [[zhang-2022-higashi]] · [[single-cell-hi-c]] · [[20-Entities/jian-ma]] · [[40-Topics/3d-genome]]
