---
type: summary
title: "Schep 2017 — chromVAR: TF-associated accessibility from single-cell epigenomic data"
aliases: ["Schep 2017 chromVAR", "chromVAR"]
tags: [chromVAR, scATAC-seq, TF-motif, bias-corrected-deviation, Greenleaf-lab, Buenrostro]
created: 2026-05-13
updated: 2026-05-13
sources: ["chromVAR_ inferring transcription-factor-associated accessibility from single-cell epigenomic data.md"]
---

**Citation:** Schep et al. (2017) — *chromVAR: TF-associated accessibility from single-cell epigenomic data* — *?*.

Schep, Wu, Buenrostro, Greenleaf (Stanford) developed **chromVAR**, an R package for analyzing sparse scATAC-seq data by computing bias-corrected per-cell accessibility deviation z-scores within motif/annotation peak sets. Aggregates across peaks sharing a TF motif to overcome sparsity; controls for GC content and mean accessibility via background peak sets. Enables cell clustering, motif discovery, and TF activity inference from ~10⁴ fragments per cell. Robust on Buenrostro 2018 hematopoiesis and other scATAC datasets.

## Why this matters

The canonical motif-based scATAC analysis tool. Used by virtually every scATAC publication. Anchors §4 (scATAC analysis tools) alongside cisTopic, SnapATAC, scBasset, SCALE.

---
**Source:** [Open paper](https://www.nature.com/articles/nmeth.4401)
## Related

- [[10-Summaries/buenrostro-2015-nature]]
- [[10-Summaries/bravo-2019-cistopic]]
- [[10-Summaries/fang-2021-snapatac]]
- [[10-Summaries/yuan-2022-scbasset]]
