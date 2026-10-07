---
type: summary
title: "Li et al. 2022 — SnapHiC2: A computationally efficient loop caller for single cell Hi-C data"
source: "[[00-Sources/papers/SnapHiC2_ A computationally efficient loop caller for single cell Hi-C data _ Computational and Structural Biotechnology Journal]]"
source_quality: full
source_sha256: "29c7918a23e68dc1fbfe62492d7500f3966fee2027393f434c89a83b19245a60"
source_kind: paper
author: "Xiaoqi Li, Lindsay Lee, Armen Abnousi, Miao Yu, Weifang Liu, Le Huang, Yun Li, Ming Hu"
published: 2022-06-04
ingested: 2026-10-07
doi: "10.1016/j.csbj.2022.05.046"
journal: "Computational and Structural Biotechnology Journal 20:2778–2783"
tags: [SnapHiC2, SnapHiC, single-cell-Hi-C, chromatin-loops, random-walk-with-restart, imputation, sliding-window, HiCCUPS, GWAS, enhancer-promoter, Sox2, Hu-lab]
entities: ["[[20-Entities/ming-hu]]"]
concepts: ["[[30-Concepts/chromatin-loop]]", "[[30-Concepts/single-cell-hi-c]]", "[[30-Concepts/imputation]]", "[[30-Concepts/pseudo-bulk]]", "[[30-Concepts/cis-regulatory-element]]"]
topics: ["[[40-Topics/3d-genome]]", "[[40-Topics/computational-methods]]"]
---

**Citation:** Li et al. (2022) — *SnapHiC2: A computationally efficient loop caller for single cell Hi-C data* — *Computational and Structural Biotechnology Journal* 20:2778–2783. [DOI](https://doi.org/10.1016/j.csbj.2022.05.046)

# Li 2022 — SnapHiC2

> SnapHiC called loops from scHi-C by imputing each cell with **random walk with restart (RWR)** over the whole chromosome and then testing bin pairs against global and local backgrounds, treating each cell as an independent unit. The RWR step was the bottleneck. SnapHiC2 runs RWR in **half-overlapping sliding windows along the diagonal** (keeping only the central band of each window, out to 1 Mb), with window size chosen as the distance that retains >80% of a cell's intra-chromosomal contacts. Result: **>3× faster, ~70% less memory**, loop quality comparable to SnapHiC, and enough headroom to call loops at **5 kb** resolution.

## Key claims

- **Window size**: >80% of contacts fall within 20 Mb for 100 human-cortex oligodendrocytes (ODCs) and within 10 Mb for 742 mESCs. Across windows of 10–50 Mb, SnapHiC2 called slightly more loops than SnapHiC, with 60.9–77.3% overlap.
- **Accuracy vs SnapHiC** (reference = loops from bulk Hi-C, H3K4me3 PLAC-seq, cohesin and H3K27ac HiChIP): ODCs, 20 Mb window — precision 0.699 / recall 0.261 / F1 0.380 vs SnapHiC 0.775 / 0.232 / 0.357. mESCs, 10 Mb window — 0.560 / 0.285 / 0.378 vs 0.655 / 0.278 / 0.391.
- **Efficiency (RWR step, 20 Mb windows, three repeats)**: ODCs 1.56 h vs 5.04 h (3.2× faster), 16.02 vs 53.02 GB memory (30.2%); mESCs 8.98 h vs 27.81 h (3.1×), 13.04 vs 35.55 GB (36.7%). A JAX GPU implementation of the loop-calling step gave >2× speed-up over SnapHiC's CPU version (single processor each).
- **5 kb loops beat pseudo-bulk HiCCUPS** (chr3, 742 mESCs): SnapHiC 252, SnapHiC2 294, HiCCUPS-default 6, HiCCUPS-lenient 24 loops. SnapHiC2 precision 0.534 / recall 0.182 / F1 0.271 (SnapHiC 0.623 / 0.180 / 0.279); HiCCUPS-default 0.667 / 0.006 / 0.013; lenient 0.708 / 0.031 / 0.060 — slightly lower precision, much higher recall.
- **Sox2 enhancer–promoter loop** (to the super-enhancer ~100 kb downstream, CRISPR-validated in prior work): detected by SnapHiC/SnapHiC2 with as few as **100 cells** vs ≥600 (HiCCUPS-default) and ≥500 (lenient). The 5 kb anchor (chr3:34.755–34.76 Mb) overlaps the CRISPR-deleted region and an H3K27ac peak better than SnapHiC's 10 kb bin.
- **GWAS target nomination**: in 261 cells each of astrocytes, L2/3 neurons, microglia and oligodendrocytes, many loops were cell-type-specific; an L2/3-specific loop links the *PAGR1* promoter to a 5 kb bin with six schizophrenia GWAS SNPs (four in neuronal enhancers), >100 kb away with intervening genes; *PAGR1* is most expressed in L2/3 neurons among the four types.

## Methods / evidence

Each chromosome per cell is a graph (bins as nodes, edges between adjacent bins and contacting bins); RWR gives imputed contact probabilities. SnapHiC2 computes RWR within d × d windows stepped by d/2 and keeps a central rectangle to avoid corner artefacts; loop calling (step 2) is unchanged from SnapHiC. Benchmarks against the original SnapHiC and against HiCCUPS on aggregated cells; reference loop lists from bulk/HiChIP/PLAC-seq data. Reference genomes mm10 and hg19.

Weight: a short engineering update. Accuracy claims are relative to SnapHiC; recall against bulk-derived references is low for all methods (~0.18–0.29), so "high sensitivity" means "far higher than pseudo-bulk HiCCUPS". The 5 kb comparison uses one chromosome; SnapHiC was run once at 5 kb because of its cost. The GWAS example is a single illustrative locus.

## Surprising or load-bearing bits

- **Why single-cell loop calling beats pooling**: ~1 billion contacts are usually needed for bulk loop calling, yet typical datasets have a few hundred cells per type at ~1 million contacts each; pooling stays far below that, whereas treating cells as replicates (SnapHiC's design) gains power. HiCCUPS on 742 pooled mESCs found 6 loops on chr3.
- **Most contacts are local** (80% within 10–20 Mb), so whole-chromosome imputation was wasted computation — a general lesson for scHi-C imputation methods. (synthesis)
- **5 kb resolution matters for variant-to-gene mapping** — the Sox2 example shows a 10 kb bin can blur which element is the enhancer.

## Concepts touched

- [[chromatin-loop]] — loops from sparse single cells at 5 kb; cell-type-specific loops in brain.
- [[single-cell-hi-c]] — sparsity (~1 million contacts/cell) as the core obstacle.
- [[imputation]] — RWR imputation, windowed approximation.
- [[pseudo-bulk]] — pooled HiCCUPS as the underpowered baseline.
- [[cis-regulatory-element]] — enhancer–promoter loops linking GWAS SNPs to target genes.

## Connections to other sources

- Direct predecessor: [[yu-2021-snaphic]]; same RWR imputation as [[zhou-2019-schicluster]].
- Bulk loop calling it compares to: [[durand-2016-juicer]] (HiCCUPS); loops discovered in deep bulk Hi-C: [[lieberman-aiden-2009-hic]].
- Single-cell methylome + 3D data in brain (sn-m3C-seq family): [[lee-2019-natmethods]], [[liu-2023-mouse-brain-methylome-3d]].
- Other scHi-C structure callers: [[peng-2026-scdiagram]] (compartments without imputation — the opposite stance on imputation), [[zhang-2022-higashi]].
- Reviews: [[hong-2025-sc3d-genome-review]], [[dautle-2025-schic-review]].

## Open questions

- Recall against bulk references stays ≤0.29 — are missed loops absent in single cells or undetectable?
- Does windowing drop genuinely long-range (>window) loops? Calls are restricted to ≤1 Mb anyway.
- Cell-type-specific loops in brain are reported in aggregate; no independent validation beyond the PAGR1 example.

## Related

- [[yu-2021-snaphic]] · [[chromatin-loop]] · [[20-Entities/ming-hu]] · [[40-Topics/3d-genome]]
