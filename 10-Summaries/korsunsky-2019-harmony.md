---
type: summary
title: "Korsunsky et al. 2019 — Fast, sensitive and accurate integration of single-cell data with Harmony"
source: "[[00-Sources/papers/Fast, sensitive and accurate integration of single-cell data with Harmony]]"
source_kind: paper
author: "Ilya Korsunsky, Nghia Millard, Jean Fan, Kamil Slowikowski, Fan Zhang, Kevin Wei, Yuriy Baglaenko, Michael Brenner, Po-ru Loh, Soumya Raychaudhuri (corresponding)"
published: 2019-11-18
ingested: 2026-08-10
doi: "10.1038/s41592-019-0619-0"
journal: "Nature Methods"
tags: [Harmony, batch-correction, integration, soft-k-means, LISI, scalability, multi-covariate]
entities: ["[[soumya-raychaudhuri]]"]
concepts: ["[[batch-effect]]", "[[multimodal-integration-methods]]", "[[dimensionality-reduction]]", "[[cell-type-annotation]]", "[[clustering-algorithms]]"]
topics: ["[[computational-methods]]", "[[single-cell-multiomics]]"]
---

**Citation:** Korsunsky et al. (2019) — *Fast, sensitive and accurate integration of single-cell data with Harmony* — *Nature Methods* 16, 1289–1296. [DOI](https://doi.org/10.1038/s41592-019-0619-0)

# Korsunsky 2019 — Harmony

> Batch correction that works **in PCA space rather than on expression**, and iteratively: soft-cluster cells so that clusters are penalized for being dominated by one dataset, compute a per-cluster linear correction from each dataset's centroid, then correct each cell by a cluster-weighted average of those corrections. Because a cell belongs to several soft clusters, **each cell gets its own correction factor**.

## Key claims

- **Four design goals**: scale to large datasets, resolve both broad populations and fine subpopulations, accommodate complex experimental designs, and integrate across modalities.
- **The algorithm.** Start from a low-dimensional embedding (typically PCA). Soft *k*-means clustering with an **information-theoretic diversity penalty** on clusters that over-represent a subset of datasets. Clusters are treated as **surrogate variables, not as cell-type calls**. Per-dataset cluster centroids give cluster-specific correction factors, which — because clusters approximate cell types and states — are effectively **cell-type-specific corrections**. Iterate until assignments stabilize. Soft assignment preserves continuous topologies and avoids local minima from over-aggressive mixing.
- **LISI, the evaluation metric**, is the paper's other contribution: local inverse Simpson's index in each cell's neighbourhood, computed twice — **iLISI** on dataset labels (higher = better mixing) and **cLISI** on cell-type labels (should stay at 1 = types not merged). This formalizes the trade every integration method faces: perfect mixing is achievable by merging everything, and perfect accuracy by not integrating at all.
- **Cell-line benchmark** (pure Jurkat, pure 293T, 50/50 mix) with analytically derived ideal iLISI values (1.8 and 1.5). Harmony reaches median iLISI 1.59 with cLISI 1.00; MNN Correct, BBKNN, MultiCCA and Scanorama were statistically inferior on integration.
- **Scalability.** On downsampled Human Cell Atlas data: 4 minutes on 30,000 cells to **68 minutes on 500,000 cells** — 30–200× faster than MultiCCA and MNN Correct — using **0.9 GB to 7.2 GB** of memory. At 125,000 cells Harmony needed **30–50× less memory** than Scanorama, MNN Correct and MultiCCA, none of which scaled beyond that point. ~10⁶ cells integrate on a personal computer.
- **Fine-grained resolution.** Integrating three PBMC datasets across 10X 3′v1, 3′v2 and 5′ chemistries, Harmony reached median iLISI 1.96 (others ≤1.02) while keeping cLISI 1.00, and the additional mixing is what allowed shared naive/memory/effector CD4 and CD8 T subsets, Tregs, and naive versus memory B cells to be identified across datasets.
- **Multiple covariates simultaneously** — the capability the paper claims is unique among single-cell integration methods. On five pancreatic islet studies with 36 donors on five platforms, Harmony integrated by **both technology (iLISI 2.17) and donor (iLISI 5.05)** at >98% cell-type accuracy; only Harmony mixed both substantially.
- Robust to non-overlapping cell types in downsampled/imbalanced datasets, and to the diversity-penalty parameter. Also demonstrated on mouse embryogenesis and on scRNA-seq-to-spatial-transcriptomics integration.

## Methods / evidence

Six analyses of escalating difficulty, from cell lines with unambiguous ground-truth labels through to cross-modality integration, each benchmarked against four to five contemporary methods with a quantitative metric rather than by eye. Runtime and peak memory reported at five dataset sizes.

The authors state the metric's own limitation: LISI is **sensitive to datasets of very different sizes**, where most neighbourhoods are dominated by one dataset and the values become hard to interpret.

## Surprising or load-bearing bits

- **Correcting in PCA space instead of gene space is why it is fast and why it composes.** Harmony returns a corrected embedding, not corrected counts, so it slots in ahead of any downstream clustering, trajectory or visualization step without committing to a corrected expression matrix — which is also why it is the default in so many pipelines, including [[hao-2024-seurat-v5|Seurat]] workflows.
- **Naming the integration/accuracy trade with two numbers changed how the field argues about batch correction.** Before LISI, methods claimed integration from UMAP appearance; after, a method that over-mixes is visibly penalized on cLISI. Compare the anchor-based framing in [[argelaguet-2021-integration-principles]].
- **Multiple covariates is the underrated capability.** Real experiments confound technology *and* donor *and* tissue; a single "batch" variable forces the analyst to choose one. Correcting jointly is what makes cross-study meta-analysis of the kind the Human Cell Atlas requires tractable.
- **Soft clustering is doing conceptual work, not just numerical work.** Hard assignment would give each cell one cluster's correction, discretizing what are often continuous cell-state gradients. Per-cell corrections arise from cluster membership being fractional.
- **Corrections are cell-type-specific by construction**, which matters because a batch effect is rarely uniform — a protocol may affect monocytes and T cells differently. A single global shift cannot represent that.
- The memory result is the practical one: at 125 k cells three of four competitors simply stop working. Method choice at atlas scale in 2019 was often determined by what would run at all.

## Entities mentioned

- [[soumya-raychaudhuri]] — corresponding author; immunogenomics and the AMP consortium context that motivated multi-covariate integration.

## Concepts touched

- [[batch-effect]] — cluster-specific linear correction in embedding space; LISI as the standard evaluation pair.
- [[multimodal-integration-methods]] — Harmony is the "correct the shared embedding" branch, distinct from anchor-transfer and factorization approaches.

## Connections to other sources

- Contemporary alternatives and comparison targets: [[welch-2019-liger]] (factorization), [[hao-2024-seurat-v5]] (anchors/bridge integration).
- Conceptual framing: [[argelaguet-2021-integration-principles]], [[zhu-2020-multimodal-power-of-many]].
- Downstream steps it feeds: [[traag-2019-leiden]] (clustering), [[mcinnes-2018-umap]] (visualization), [[wolf-2019-paga]] (trajectory).
- Atlas-scale data of the kind it targets: [[cao-2019-moca]], [[lake-2018-brain-snrna-scths]].

## Open questions

- **LISI degrades on size-imbalanced datasets**, acknowledged by the authors — so the metric that made integration comparable has a regime where it is uninformative, and that regime (one large reference, one small query) is common.
- Harmony corrects an embedding, not counts, so differential expression must be done on uncorrected data with batch as a covariate; the paper does not address how to reconcile the two.
- Whether cluster-as-surrogate-variable holds when a cell type is present in only one dataset is tested by downsampling but not resolved in general.

## Related

- [[batch-effect]] · [[welch-2019-liger]] · [[hao-2024-seurat-v5]] · [[computational-methods]]
