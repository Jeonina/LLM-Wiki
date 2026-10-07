---
type: concept
title: cisTopic
aliases: [LDA-based scATAC clustering]
tags: [scATAC-seq, topic-modeling, LDA, Aerts-lab, software]
created: 2026-05-12
updated: 2026-10-07
---

# cisTopic

> An R/Bioconductor package by the Aerts lab that applies Latent Dirichlet Allocation (LDA) with collapsed Gibbs sampling to scATAC-seq, co-optimizing the clustering of cells and the clustering of regulatory regions into "cis-regulatory topics."

## Definition

Input: binary cell × region accessibility matrix. LDA derives two distributions: region-topic (which regions belong to which topic) and topic-cell (how each cell's accessibility maps to topics). Topics can be interpreted as combinatorial regulatory programs.

## Why it matters

- Resolves temporal heterogeneity that chromVAR averages away (e.g., GATA-mediated regulation at HSC vs intermediate vs MEP stages, each a distinct topic).
- Naturally handles sparsity via topic aggregation.
- Topic regions enrich for TF motifs that correspond to cell-type master regulators.
- Its multiplied topic-cell × region-topic distributions also serve as an imputation ("cisTopic-impute"), a baseline later benchmarked against scOpen and SCALE ([[10-Summaries/li-2021-scopen]], [[10-Summaries/xiong-2019-scale]]). See [[30-Concepts/scatac-imputation]].

## Examples

- Hematopoietic differentiation, brain cell types (cortical excitatory layers, glia), SOX10-knockdown dynamics in melanoma ([[10-Summaries/bravo-2019-cistopic]]).

## Added 2026-10-07

In PeakVI's benchmark, cisTopic was nearly as good as PeakVI at matching RNA-defined clusters on 10x PBMC multiome data and at separating sorted hematopoietic cell types, but did not correct batch effects ([[10-Summaries/ashuach-2022-peakvi]]). EpiAgent reports outperforming cisTopic on NMI and ARI after fine-tuning ([[10-Summaries/chen-2025-epiagent]]).

cisTopic (15 topics) was applied beyond accessibility data to single-cell Pol II and H3K36me3 CoBATCH profiles of E16.5 cardiac Cdh5-traced cells. It resolved macrophage-like, mesenchymal, arterial and venous endothelial clusters ([[10-Summaries/wang-2019-cobatch]]).

In a benchmark on single-cell histone PTM data, cisTopic ranked behind the TF-IDF methods (ChromSCape_LSI, TFIDF-NMF, Signac) as well as SnapATAC and PeakVI, despite being among the best tools in an earlier scATAC-seq benchmark ([[10-Summaries/raimundo-2023-schptm-benchmark]]).


## Related

- [[30-Concepts/latent-dirichlet-allocation]] · [[30-Concepts/scatac-seq]] · [[30-Concepts/chromvar]] · [[30-Concepts/snapatac]] · [[30-Concepts/scatac-imputation]] · [[30-Concepts/scopen]] · [[30-Concepts/scale]] · [[40-Topics/single-cell-atac-seq]] · [[20-Entities/stein-aerts]]
