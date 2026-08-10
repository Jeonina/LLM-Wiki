---
type: summary
title: "Kremer et al. 2024 — Analyzing single-cell bisulfite sequencing data with MethSCAn"
source: "[[00-Sources/papers/Analyzing single-cell bisulfite sequencing data with MethSCAn]]"
source_kind: paper
author: "Lukas P. M. Kremer, Martina M. Braun, Svetlana Ovchinnikova, Leonie Küchenhoff, Santiago Cerrizuela, Ana Martin-Villalba, Simon Anders (corresponding)"
published: 2024-07-31
ingested: 2026-08-10
doi: "10.1038/s41592-024-02347-x"
journal: "Nature Methods"
tags: [MethSCAn, scBS-seq, VMR, DMR, preprocessing, tiling, signal-dilution, computational-tool]
entities: []
concepts: ["[[scbs-seq]]", "[[bisulfite-sequencing]]", "[[allele-specific-methylation]]", "[[episcanpy]]", "[[scanpy]]", "[[cis-regulatory-element]]"]
topics: ["[[dna-methylation]]"]
---

**Citation:** Kremer et al. (2024) — *Analyzing single-cell bisulfite sequencing data with MethSCAn* — *Nature Methods* 21, 1616–1623. [DOI](https://doi.org/10.1038/s41592-024-02347-x)

# Kremer 2024 — MethSCAn

> The standard scBS preprocessing recipe — tile the genome into 100 kb bins, average methylation per bin per cell — **dilutes signal**, because a small variably-methylated region's CpGs are drowned by the many uninformative CpGs sharing its tile. MethSCAn replaces both halves of that recipe: it discovers variably methylated regions de novo, and quantifies each cell's *deviation from a smoothed ensemble average* rather than its raw methylation fraction.

## Key claims

- **Two distinct problems with tile-averaging.** (i) Sparse coverage means different cells are represented by reads at *different positions* within a tile; if the local methylation profile varies, two cells can look different when their overlapping reads actually agree. (ii) Fixed tile boundaries rarely match the actual variable region.
- **Read-position-aware quantitation**: compute a kernel-smoothed per-CpG average across all cells (bandwidth 1,000 bp in the examples), take each cell's signed residual from that curve, and average residuals over covered CpGs in the interval with **shrinkage toward zero via a pseudocount** to damp low-coverage cells. Cells with no reads in an interval get 0 — justified because zero residual means *no evidence of deviation*, not "unmethylated" — refined by iterative PCA imputation.
- **VMR discovery**: slide overlapping windows at a small fixed step, compute per-window across-cell variance of the residual score, take the top ~2%, merge overlapping windows, requantify. 63,421 VMRs found in the main dataset.
- Benchmark design: four interval sets (VMRs, 100 kb tiles, promoters TSS±2 kb, ENCODE cCREs) × two quantitations (raw average vs shrunken residual mean) × four dimensionality reductions, scored by a "neighbor score" measuring whether a cell's 15-dimensional PC-space neighbors share its transcriptome-derived cell-type label.
- Both changes help, and they are additive. VMRs beat promoters and tiles; residual quantitation improves things further, **most for promoters and tiles** — consistent with the diagnosis, since those intervals are most likely to span heterogeneous methylation.
- **VMRs are more informative per feature than annotation**: 63,421 VMRs match the performance of 339,815 ENCODE cCREs, and when cCREs are subsampled to 63,421 highest-coverage elements they perform worse. VMR/cCRE overlap is limited, so VMR detection yields complementary information — and works in species with no regulatory annotation.
- **VMR methylation predicts expression better than promoter methylation.** Example *Htra1*: the promoter is lowly methylated regardless of expression, while a downstream VMR tracks it.
- **First DMR detection method for scBS data.** Same sliding-window machinery, but with a *t* statistic between two cell groups instead of variance, tails merged into DMRs, and FDR estimated by permuting cell labels. Applied to 130 NSCs vs 58 oligodendrocytes, GREAT enrichment on the DMRs returns myelination genes for oligodendrocyte-hypomethylated regions and stem-cell-maintenance genes for NSC-hypomethylated ones — with the *Mbp* locus as the exemplar.
- Robust to parameters (bandwidth, variance threshold, step size) over wide ranges; works on **CH methylation** as well as CpG; stress-tested to 100,350 cells.
- Benefits are largest in the hard cases: continuous lineage trajectories and **small datasets** — directly relevant since scBS is costly and few labs generate thousands of cells.

## Methods / evidence

Five datasets: the authors' own 1,566-cell mouse forebrain multi-omic set (methylome + transcriptome from the same cells, so transcriptome-derived labels serve as ground truth), Luo et al. mouse cortical neurons, mouse gastrulation embryos, human colorectal cancer, and a 100k-cell stress test. Subsampling curves quantify how performance degrades with cell number. Comparators include MOFA+ and two alternative PCA preprocessing strategies.

Using **matched transcriptomes as ground truth** is the design decision that makes the benchmark meaningful — cell-type labels are not derived from the methylation data being evaluated.

## Surprising or load-bearing bits

- **The residual trick generalizes beyond methylation.** Its logic — when coverage is sparse and positionally random, compare each cell to a smoothed consensus at the positions it actually observed, rather than comparing summary statistics computed over different position sets — applies to any sparse, positionally-sampled single-cell modality. That includes scCUT&Tag and single-cell Hi-C, where tile-averaging is equally standard and equally unexamined.
- The paper is a quiet indictment of accumulated practice: the 100 kb tile convention was inherited from scRNA-seq-shaped thinking and never justified for binary, genome-wide, sparsely-covered data. Every scBS analysis that used it has been leaving signal on the table.
- **VMRs are an empirical answer to Jones's LMR question.** [[jones-2012-dna-methylation-functions|Jones 2012]] argued enhancers are "low-methylated regions" whose intermediate bulk values must reflect cell-to-cell variability; VMR detection finds precisely those regions from single-cell data without needing the annotation. The two papers are the bulk-era hypothesis and the single-cell-era operationalization of the same object.
- VMRs beating promoters as expression predictors reinforces that **promoter methylation is the wrong default feature** for methylome-based cell typing — again matching Jones's context-dependence argument.
- Missing data handled as "zero deviation" rather than imputed methylation is a small but principled choice that avoids inventing signal.
- DMR detection had simply not existed for scBS before this. That is a striking gap for a modality dating to 2014 ([[smallwood-2014-natmethods]]).

## Concepts touched

- [[scbs-seq]] — the preprocessing standard for the whole modality is redefined here.
- [[bisulfite-sequencing]] — inherits the 5mC/5hmC conflation; MethSCAn does not address it.
- [[cis-regulatory-element]] — VMRs are an annotation-free, data-derived alternative to cCREs.

## Connections to other sources

- Consumes output from [[krueger-2011-bismark|Bismark]], methylpy or BISCUIT; feeds [[mcinnes-2018-umap|UMAP]], [[traag-2019-leiden|Leiden]], [[danese-2021-episcanpy|EpiScanpy]]/Scanpy/Seurat; uses [[mclean-2010-great|GREAT]] for DMR interpretation and benchmarks against [[argelaguet-2020-mofa-plus|MOFA+]].
- Re-analyzes [[luo-2018-snmc-seq2]] data; supersedes the tiling convention used there.
- Alternative modeling approaches in this corpus: [[kapourani-2019-melissa|Melissa]], [[kapourani-2021-scmet|scMET]], [[desouza-2020-epiclomal|Epiclomal]], [[angermueller-2017-genomebiol|DeepCpG]] — all of which take the feature set as given, which is exactly what MethSCAn declines to do.
- Method context: [[smallwood-2014-natmethods]], [[nichols-2022-scimet-v2]], [[iqbal-2023-methylome-review]].

## Open questions

- Would residual-based quantitation and de novo variable-region discovery improve **scCUT&Tag** and **single-cell Hi-C** analysis the same way? The logic transfers; nobody in this corpus has tested it.
- VMR detection is unsupervised and variance-driven, so it will also concentrate technical variance (coverage-correlated artifacts, conversion-failure regions). The paper does not separate biological from technical variability in VMR selection.
- No treatment of the 5mC/5hmC conflation — VMRs in tissues with high 5hmC (brain) may partly track oxidation state rather than methylation.

## Related

- [[scbs-seq]] · [[jones-2012-dna-methylation-functions]] · [[luo-2018-snmc-seq2]] · [[dna-methylation]]
