---
type: summary
title: "Jiang 2026 — STARK and scNucleome: harmonizing sc3DG-seq data"
aliases: ["Jiang 2026 STARK", "STARK", "scNucleome"]
tags: [STARK, scNucleome, sc3DG-seq, benchmark, EmptyCells, SSCE, single-cell-3D-genome, Wu-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Harmonizing single-cell 3D genome data with STARK and scNucleome.md"]
---

Jiang, Cai, Sun et al. (Wu lab) developed **STARK**, a unified preprocessing/QC/analysis toolkit for sc3DG-seq across 15 technologies (scHi-C, sciHi-C, Dip-C, sn-m3C, scMethyl, HiRES, scSPRITE, snHi-C, scNanoHi-C, LiMCA, GAGE-seq, Droplet Hi-C, Paired Hi-C, etc.). Includes **EmptyCells** filter (Monte Carlo simulation of empty barcodes), **SSCE** (Spatial Structure Capture Efficiency) QC metric, and downstream A/B compartment/TAD/loop calling + 3D reconstruction. Benchmarks all 15 technologies on shared metrics. **scNucleome** is the companion uniformly-processed sc3DG-seq data repository.

## Why this matters

The 2026 unifying sc3D-genome analysis tool. Anchors §4 (computational) and §3.5 (3D genome). The first cross-technology benchmark for sc3DG-seq — analogous to what Luo 2024 did for scATAC and Xiao 2024 for multi-omics integration.

---
**Source:** [Open paper](https://link.springer.com/article/10.1186/s13059-026-03938-x)
## Related

- [[10-Summaries/nagano-2013-nature]]
- [[10-Summaries/ma-2020-cell]]
- [[10-Summaries/liu-2023-mouse-brain-methylome-3d]]
- [[10-Summaries/luo-2024-scatac-benchmark]]
