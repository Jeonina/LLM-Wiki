---
type: summary
title: "Bai 2024 — SIMPLE-seq: single-cell joint analysis of 5mC and 5hmC"
aliases: ["Bai 2024 SIMPLE-seq", "SIMPLE-seq"]
tags: [SIMPLE-seq, 5mC, 5hmC, single-cell-methylation, bisulfite-free, hmC-CATCH, TAPS, Yi-lab, Peking]
created: 2026-05-13
updated: 2026-05-13
sources: ["Simultaneous single-cell analysis of 5mC and 5hmC with SIMPLE-seq.md"]
---

Bai, Zhang, Xiang, Guo, Zhu, Yi (Peking + UNC) developed **SIMPLE-seq** for simultaneous single-cell 5mC + 5hmC base-resolution profiling. Sequential bisulfite-free chemical labeling: hmC-CATCH (ruthenate(VI) oxidation + indanedione labeling of 5hmC → C-to-T) → primer extension → TAPS (TET + borane reduction of 5mC → C-to-T). Pre-deposited 5caC base on primer distinguishes 5hmC- vs 5mC-derived signals after PCR. Tn5 tagmentation + combinatorial indexing for high throughput. Applied to mESCs (2i vs serum), human PBMCs, mouse brain — identified divergent epigenetic programs across cell states.

## Why this matters

The first single-cell joint 5mC + 5hmC method. Important §3.3 advance — 5hmC is dynamic in active demethylation; separating it from 5mC reveals demethylation kinetics that bisulfite-only methods miss. Mouse-brain application directly relevant to brain mosaicism.

---
**Source:** [Open paper](https://www.nature.com/articles/s41587-024-02148-9)
## Related

- [[10-Summaries/luo-2018-snmc-seq2]]
- [[10-Summaries/nichols-2022-scimet-v2]]
- [[10-Summaries/tavares-2026-6base-cuttag]]
- [[10-Summaries/liu-2023-mouse-brain-methylome-3d]]
