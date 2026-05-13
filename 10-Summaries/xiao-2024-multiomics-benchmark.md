---
type: summary
title: "Xiao 2024 — Benchmarking multi-omics integration algorithms across single-cell RNA and ATAC data"
aliases: ["Xiao 2024 multiomics benchmark", "scRNA+scATAC integration benchmark"]
tags: [benchmark, multi-omics-integration, scRNA-seq, scATAC-seq, MOFA, Cobolt, MultiVI, Seurat, GLUE, Wei-lab, Tsinghua]
created: 2026-05-13
updated: 2026-05-13
sources: ["Yan_2024_BriefingsInBioinformatics.pdf"]
---

Xiao, Chen, Meng, Wei and Zhang (Tsinghua) benchmarked 12 multi-omics integration methods across scRNA-seq and scATAC-seq datasets, organized into three categories: **paired** (scMVP, MOFA+), **paired-guided** (MultiVI, Cobolt), and **unpaired** (scDART, UnionCom, MMD-MA, scJoint, Harmony, Seurat v3, LIGER, GLUE).

Three datasets used for the benchmark: (i) P0 mouse cerebral cortex SNARE-seq (paired, 5,081 cells); (ii) human uterus paired dataset (paired-guided with trajectory, 1,469 cells); (iii) unpaired scRNA-seq (8,237 cells) + scATAC-seq (8,314 cells) human-tissue datasets. Four evaluation axes: omics-mixing, cell-type conservation, single-cell-level alignment accuracy (FOSCTTM), and trajectory preservation.

Key practical guidelines: **MultiVI** is best for paired-guided integration when the goal is using paired data to assist unpaired analysis. **GLUE** is best for unpaired integration when prior knowledge (regulatory graph) is available. **MOFA+** is best for paired integration when interpretability of latent factors matters. The benchmark also assessed scalability and ease-of-use.

## Why this matters

The independent multi-method benchmark for §4's multimodal-integration subsection. Validates our placement of MultiVI, GLUE, and MOFA+ as the three pillars of the integration tool family. Important nuance for the review: choice of method depends not only on the data layout (paired/unpaired/guided) but also on the downstream question (cell-type discovery vs trajectory vs regulatory inference). Anchors §4 (multimodal integration) and §6 (limitations).

## Related

- [[10-Summaries/ashuach-2023-multivi]]
- [[10-Summaries/cao-2022-glue]]
- [[10-Summaries/argelaguet-2019-mofa]]
- [[10-Summaries/gong-2021-cobolt]]
- [[30-Concepts/multimodal-integration-methods]]
