---
type: summary
title: "Bravo González-Blas et al. 2019 — cisTopic: LDA topic modeling for scATAC-seq"
source: "[[00-Sources/papers/cisTopic_ cis-regulatory topic modeling on single-cell ATAC-seq data]]"
source_kind: paper
author: "Carmen Bravo González-Blas, Liesbeth Minnoye, Dafni Papasokrati, Sara Aibar, Gert Hulselmans, Valerie Christiaens, Kristofer Davie, Jasper Wouters, Stein Aerts (corresponding)"
published: 2019-04-08
ingested: 2026-05-12
doi: "10.1038/s41592-019-0367-1"
journal: "Nature Methods"
tags: [scATAC-seq, topic-modeling, LDA, Aerts-lab, enhancers, transcription-factors, melanoma, hematopoiesis]
entities:
  - "[[20-Entities/stein-aerts]]"
  - "[[20-Entities/carmen-bravo-gonzalez-blas]]"
concepts:
  - "[[30-Concepts/cistopic]]"
  - "[[30-Concepts/latent-dirichlet-allocation]]"
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/cis-regulatory-element]]"
  - "[[30-Concepts/chromatin-accessibility]]"
topics:
  - "[[40-Topics/single-cell-atac-seq]]"
  - "[[40-Topics/chromatin-architecture]]"
---

# Bravo González-Blas et al. 2019 — cisTopic

> Thesis: Existing scATAC-seq analysis methods either cluster cells first then call differential peaks (loses dynamic structure) or aggregate peaks into pre-defined cistromes (depends on annotations). **cisTopic** uses Latent Dirichlet Allocation (LDA) with Gibbs sampling to **co-optimize clustering of cells and clustering of regulatory regions** into "topics" — recovering cell types, developmental trajectories, and the regulatory programs that distinguish them in a single unsupervised pass.

## Key claims

- LDA derives two distributions: (1) cell-topic (how strongly each topic contributes to each cell) and (2) region-topic (how strongly each region belongs to each topic). Default Dirichlet hyperparameters α=50/T, β=0.1.
- Applied to **human hematopoietic differentiation** scATAC-seq (Buenrostro 2018): correctly identifies cell types and developmental trajectory using 17 topics, **outperforming peak-only and chromVAR-style methods**, especially at low read depth.
- Topic 3 = constitutive promoter signal (high in all cells). Topic 12 → CLP (EBF1 motif), topic 10 → pDC (PU.1, IRF), topic 1 → GMP (PU.1, CEBP). Three GATA topics (15, 13, 5) recover the **time-resolved HSC → MEP differentiation trajectory** that chromVAR cannot resolve because chromVAR averages GATA cistromes.
- **Brain scTHS-seq / scATAC-seq** application: resolves cortical layer-specific excitatory neurons (ExL23/L4/L56) and interneurons (medial vs caudal ganglionic eminence) in both human and mouse. Cross-species topic mapping shows strong conservation in glia, weaker in neurons.
- **SOX10 knockdown time course in melanoma**: cisTopic recovers a loss-of-accessibility topic enriched for SOX10 motifs and overlapping SOX10 ChIP-seq peaks. Identifies SOXE cell-type-specific cofactors (TFAP2/AP-1 in melanoma vs OLIG1/2 in oligodendrocytes vs NFIA/B in astrocytes).
- Fast Gibbs sampler scales to the Mouse Cell Atlas (~80k cells).

## Methods / evidence

R/Bioconductor package (github.com/aertslab/cistopic). Input: binary cell × region matrix. Tuning: 500 burn-in + 500 recording iterations; topic-number selection by log-likelihood + perplexity stabilization. Validated against ChIP-seq, scRNA-seq integration (SCENIC), and motif enrichment.

## Surprising or load-bearing bits

- **The co-optimization argument** is the methodological insight: pure cell-clustering loses regulatory structure, and pre-defined cistromes lose temporal granularity. LDA optimizes both simultaneously.
- Topic modeling, borrowed from NLP, naturally handles the sparsity of scATAC-seq because it works at the level of distributions over discrete tokens (regions) — analogous to documents and words.
- Time-resolved GATA topics from the same cistrome family is the cleanest example: cisTopic shows that **the same TF can drive multiple distinct regulatory programs at different developmental stages**, undetectable by methods that collapse motifs to single cistromes.

## Connections to other sources

- Compared with [[10-Summaries/chromvar-inferring-transcription-factor-associated-accessibility-from-single-cell-epigenomic-data]] (chromVAR averages cistromes; cisTopic preserves temporal heterogeneity) and [[10-Summaries/comprehensive-analysis-of-single-cell-atac-seq-data-with-snapatac]] (SnapATAC bypasses peak calls entirely with a 5-kb bin Jaccard approach).
- Used as input by [[10-Summaries/scatac-seq-generates-more-accurate-and-complete-regulatory-maps-than-bulk-atac-seq]] (Gur/Hughes 2025) for downstream clustering.
- Topic-modeling logic extended to chromatin in [[10-Summaries/scchix-seq-infers-dynamic-relationships-between-histone-modifications-in-single-cells]] (scChIX-seq) which uses LDA on histone-mark profiles.

## Open questions

- LDA topic-number selection remains empirical; perplexity is not perfectly principled.
- Newer tools (Signac, ArchR, snapATAC2) include LDA-style approaches as one option among many; cisTopic's standalone usage has declined.

---
**Source:** [DOI](https://doi.org/10.1038/s41592-019-0367-1)
## Related

- [[40-Topics/single-cell-atac-seq]] · [[30-Concepts/cistopic]] · [[30-Concepts/latent-dirichlet-allocation]] · [[20-Entities/stein-aerts]]
