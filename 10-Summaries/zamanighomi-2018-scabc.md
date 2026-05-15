---
type: summary
title: "Zamanighomi 2018 — scABC: unsupervised clustering of single-cell scATAC-seq"
aliases: ["Zamanighomi 2018 scABC", "scABC"]
tags: [scABC, scATAC-seq, unsupervised-clustering, weighted-K-medoids, landmark-based, Wong-lab, Greenleaf-lab, Stanford]
created: 2026-05-13
updated: 2026-05-13
sources: ["Unsupervised clustering and epigenetic classification of single cells.md"]
---

**Citation:** Zamanighomi et al. (2018) — *scABC: unsupervised clustering of single-cell scATAC-seq* — *?*.

Zamanighomi, Lin, Daley et al. (Wong, Greenleaf labs; Stanford) developed **scABC** (single cell Accessibility Based Clustering). Weighted K-medoids clustering — cells weighted by sequencing-depth-derived reliability. Uses ranked peaks (not raw counts) to prevent bias from over-represented regions. Calculates per-cluster "landmarks" (prototypical cells) then re-clusters via Spearman correlation to landmarks. Cluster-specific peaks identified via empirical Bayes regression. ~0.4% misclassification on 966-cell in silico mixture.

## Why this matters

An early (2018) scATAC clustering tool predating chromVAR (motif-deviation), cisTopic (LDA), SnapATAC (genome-bin). Anchors §4 (scATAC analysis tool history). Lower priority citation than chromVAR/cisTopic — useful only as historical reference.

---
**Source:** [Open paper](https://www.nature.com/articles/s41467-018-04629-3)
## Related

- [[10-Summaries/schep-2017-chromvar]]
- [[10-Summaries/bravo-2019-cistopic]]
- [[10-Summaries/fang-2021-snapatac]]
- [[10-Summaries/buenrostro-2015-nature]]
