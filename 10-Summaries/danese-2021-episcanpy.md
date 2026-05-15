---
type: summary
title: "Danese 2021 — EpiScanpy: integrated single-cell epigenomic analysis"
aliases: ["Danese 2021 EpiScanpy", "EpiScanpy"]
tags: [EpiScanpy, scATAC-seq, scDNA-methylation, scanpy-extension, Theis-lab, Colome-Tatche-lab, Helmholtz-Munich]
created: 2026-05-13
updated: 2026-05-13
sources: ["EpiScanpy_ integrated single-cell epigenomic analysis.md"]
---

**Citation:** Danese et al. (2021) — *EpiScanpy: integrated single-cell epigenomic analysis* — *?*.

Danese, Richter, Chaichoompu, Fischer, Theis, Colomé-Tatché (Helmholtz Munich) developed **EpiScanpy**, an extension of Scanpy for scATAC-seq AND single-cell DNA methylation. Builds count matrices for arbitrary genomic features (windows, peaks, promoters, enhancers), epigenomic distance-based kNN graph, common clustering/dim-reduction/trajectory tools. Differential methylation/openness calling. Atlas integration via BBKNN. Benchmarked against 11 scATAC tools — outperforms most on cell-type discrimination.

## Why this matters

The unified epigenome analysis framework — covers both arms (accessibility + methylation) of the locus state. Anchors §4 (computational methods). Complements chromVAR / cisTopic / SnapATAC (accessibility only) and Epiclomal / Melissa (methylation only).

---
**Source:** [Open paper](https://www.nature.com/articles/s41467-021-25131-3)
## Related

- [[10-Summaries/schep-2017-chromvar]]
- [[10-Summaries/bravo-2019-cistopic]]
- [[10-Summaries/fang-2021-snapatac]]
- [[10-Summaries/desouza-2020-epiclomal]]
