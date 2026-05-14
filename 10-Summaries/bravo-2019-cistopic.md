---
type: summary
title: "Bravo González-Blas 2019 — cisTopic: cis-regulatory topic modeling on scATAC-seq"
aliases: ["Bravo 2019 cisTopic", "cisTopic"]
tags: [cisTopic, scATAC-seq, topic-modeling, LDA, Bayesian, Aerts-lab, KU-Leuven]
created: 2026-05-13
updated: 2026-05-13
sources: ["cisTopic_ cis-regulatory topic modeling on single-cell ATAC-seq data.md"]
---

Bravo González-Blas, Minnoye, Papasokrati et al. (Aerts lab; KU Leuven) developed **cisTopic**, a Bayesian topic modeling framework for scATAC-seq using Latent Dirichlet Allocation with collapsed Gibbs sampling. Co-optimizes cell clustering and enhancer categorization — produces (i) region-topic distribution (probability that a region belongs to a topic) and (ii) topic-cell distribution. Validated on hematopoietic differentiation, human/mouse brain, and SOX10 melanoma perturbation. Outperforms chromVAR for time-resolved cistromes (different GATA stages).

## Why this matters

The LDA branch of scATAC analysis. Complements chromVAR (motif-deviation) and SnapATAC (genome-bin) approaches. Anchors §4 (scATAC analysis). Particularly useful when cell states are continuous rather than discrete clusters.

---
**Source:** [Open paper](https://www.nature.com/articles/s41592-019-0367-1)
## Related

- [[10-Summaries/schep-2017-chromvar]]
- [[10-Summaries/fang-2021-snapatac]]
- [[10-Summaries/yuan-2022-scbasset]]
- [[10-Summaries/zhang-2024-snapatac2]]
