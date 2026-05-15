---
type: summary
title: "Zamanighomi et al. 2018 — scABC: weighted k-medoids unsupervised clustering for scATAC-seq"
source: "[[00-Sources/papers/Unsupervised clustering and epigenetic classification of single cells]]"
source_kind: paper
author: "Mahdi Zamanighomi, Zhixiang Lin, Timothy Daley, Xi Chen, Zhana Duren, Alicia Schep, William J. Greenleaf, Wing Hung Wong (corresponding)"
published: 2018-06-20
ingested: 2026-05-12
doi: "10.1038/s41467-018-04629-3"
journal: "Nature Communications"
tags: [scATAC-seq, k-medoids, unsupervised-clustering, software, Wong-lab, ESC-differentiation, embryoid-body]
entities:
  - "[[20-Entities/wing-hung-wong]]"
  - "[[20-Entities/mahdi-zamanighomi]]"
  - "[[20-Entities/william-greenleaf]]"
concepts:
  - "[[30-Concepts/scabc]]"
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/k-medoids]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/cis-regulatory-element]]"
topics:
  - "[[40-Topics/single-cell-atac-seq]]"
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Zamanighomi et al. (2018) — *scABC: weighted k-medoids unsupervised clustering for scATAC-seq* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-018-04629-3)

# Zamanighomi et al. 2018 — scABC

> Thesis: scATAC-seq sparsity makes peak-based clustering fragile, especially when subpopulation marker peaks are unknown. **scABC** is a fully unsupervised pipeline that (a) weights cells by total in-peak reads (high-coverage cells are more reliable), (b) does weighted k-medoids clustering on rank-transformed peak signals, (c) refines cluster assignment by Spearman correlation to landmark cells, and (d) identifies cluster-specific peaks via empirical-Bayes regression. Validated to 99.6% accuracy on 966-cell in silico mixtures of six cell lines.

## Key claims

- **Weighted k-medoids on ranked peak signals** avoids domination by highly accessible regions (which carry within-cell-type signal noise rather than between-type information).
- **Landmark refinement**: after initial clustering, prototypical cells (landmarks) are defined by top peaks within each cluster; remaining cells are reassigned to the closest landmark by Spearman correlation. This rescues borderline cells.
- **Cluster-specific peak identification**: empirical-Bayes regression hypothesis test gives p-values for whether each peak is differentially accessible in a given cluster. Most cells have either common or highly cluster-specific peaks — the "shoulder" of marginal peaks is small.
- **Validation**: 6 cell-line in silico mixture (966 cells) achieves 99.6% accuracy. Robust to batch effects (GM12878 cells from 4 batches still cluster together).
- **Sensitivity floor**: well-separated cell types resolvable at 1% of total population; similar types (K562 vs HL60, both erythroleukemic) merge below 5%. Recognized cell types from 50–70% peak similarity in synthetic perturbation tests.
- **Novel biology**: scABC on day-4 RA-treated mouse embryoid bodies discovers heterogeneity — 67 neuroectoderm-like cells (GSX, LBX1, LMX1A, NEUROG2, NKX6 motifs) and 28 visceral-endoderm-like cells (GATA, HNF1, AP-1 motifs) within a population assumed to be neural-only.
- Integration with scRNA-seq via cluster-specific open promoters: genes with cell-type-specific open promoters have higher expression in that cell type. PCA on those genes' expression cleanly separates K562 vs HL60 cells where PCA on all genes does not — **cell-identity-defining genes flow from chromatin to expression**.

## Methods / evidence

R package. In silico mixture of 966 cells from 6 cell lines (Buenrostro 2015). Experimental GM12878+HEK293T and GM12878+HL60 mixtures. Hanging-drop mouse embryoid bodies + RA → 95 cells profiled.

## Surprising or load-bearing bits

- **Weighting cells by coverage** is the methodological insight: deep cells are more informative for clustering, and the algorithm should explicitly use that.
- The mEB+RA experiment is a clean **biological discovery**: a population thought to be neural-only (because RA induces neural differentiation in mESCs) turns out to also contain visceral endoderm. The outer EB layer differentiates differently from the inner mass.
- Identifies GM12878 cell-line **internal NF-κB heterogeneity** — a small but real subpopulation distinction that prior chromatin-bulk work had hypothesized but not demonstrated at single-cell resolution.

## Connections to other sources

- Cited as a comparator by [[10-Summaries/cistopic-cis-regulatory-topic-modeling-on-single-cell-atac-seq-data]] (cisTopic outperforms on continuous trajectories) and [[10-Summaries/episcanpy-integrated-single-cell-epigenomic-analysis]] (EpiScanpy benchmark).
- Uses [[10-Summaries/chromvar-inferring-transcription-factor-associated-accessibility-from-single-cell-epigenomic-data]] (chromVAR) for cluster-specific TF motif analysis — common pattern in early scATAC-seq tooling.
- Anticipates findings later confirmed at scale by [[10-Summaries/comprehensive-analysis-of-single-cell-atac-seq-data-with-snapatac]] (SnapATAC) and [[10-Summaries/scatac-seq-generates-more-accurate-and-complete-regulatory-maps-than-bulk-atac-seq]] (Gur/Hughes 2025): "nominally homogeneous populations are not."

## Open questions

- k-medoids requires choosing K; modified gap statistic helps but is not deterministic.
- 2018-era tool, somewhat eclipsed by cisTopic / SnapATAC / EpiScanpy / ArchR for new work. The conceptual contributions (coverage-weighted clustering, landmark refinement, cluster-specific peak testing) live on in modern pipelines.

---
**Source:** [DOI](https://doi.org/10.1038/s41467-018-04629-3)
## Related

- [[40-Topics/single-cell-atac-seq]] · [[30-Concepts/scabc]] · [[30-Concepts/chromvar]]
