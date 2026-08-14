---
type: summary
title: "Yu et al. 2021 — SnapHiC: a computational pipeline to identify chromatin loops from single-cell Hi-C data"
source: "[[00-Sources/papers/SnapHiC_ a computational pipeline to identify chromatin loops from single-cell Hi-C data]]"
source_kind: paper
author: "Miao Yu, Armen Abnousi, Yanxiao Zhang, Guoqiang Li, Lindsay Lee, Ziyin Chen, Rongxin Fang, Taylor M. Lagler, Yuchen Yang, Jia Wen, Quan Sun, Yun Li, Bing Ren, Ming Hu (corresponding)"
published: 2021-08-26
ingested: 2026-08-13
doi: "10.1038/s41592-021-01231-2"
journal: "Nature Methods 18:1056–1059"
tags: [SnapHiC, chromatin-loops, scHi-C, random-walk-with-restart, paired-t-test, sn-m3C-seq, GWAS-SNP, prefrontal-cortex]
entities: ["[[bing-ren]]", "[[ming-hu]]"]
concepts: ["[[single-cell-hi-c]]", "[[chromatin-loop]]", "[[imputation]]", "[[hi-c-normalization]]", "[[cis-regulatory-element]]", "[[pseudo-bulk]]", "[[mappability]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]", "[[brain-somatic-mosaicism]]"]
---

**Citation:** Yu et al. (2021) — *SnapHiC: a computational pipeline to identify chromatin loops from single-cell Hi-C data* — *Nature Methods* 18, 1056–1059. [DOI](https://doi.org/10.1038/s41592-021-01231-2)

# Yu 2021 — SnapHiC

> The first loop caller designed for [[single-cell-hi-c|scHi-C]] rather than borrowed from bulk. The key design decision: **do not pool cells into pseudobulk.** Treat each cell as an independent sample, impute per cell, then use a **paired *t*-test across cells** at each bin pair. Cell-to-cell variance becomes statistical power instead of noise — which is why SnapHiC finds **1,050–1,420 loops from 75 cells** where HiCCUPS finds 0–10.

## Key claims

- **Pseudobulk aggregation is the thing to avoid, and the paper says why.** Applying bulk loop callers to aggregated scHi-C needs >500–1,000 cells, which is cost-prohibitive and impossible for rare cell types. Keeping cells separate lets the *variability* of contact frequency across the population enter the test statistic — the power gain is largest exactly when cell numbers are low.
- **Four steps.** (A) [[imputation|Random walk with restart]] (restart probability 0.05) on a per-cell binary contact graph at 10-kb bins, with edges added between adjacent bins; (B) distance-stratified *z*-score normalisation of imputed probabilities, dropping the top 1% per distance stratum before computing μ_d and σ_d, and setting z = 0 where σ_d < 10⁻⁶ to avoid numerical blowup; (C) candidate loop calling against both **global and local** background; (D) Rodriguez–Laio density clustering of candidates, with the lowest-FDR candidate per cluster reported as the summit.
- **The candidate criteria are deliberately conservative and stack five filters**: mean normalised probability > 0; >10% of cells with z > 1.96; paired *t*-test versus a 96-bin-pair local neighbourhood (30–50 kb ring) at FDR < 10% and t > 3; HiCCUPS-style donut/horizontal/vertical/lower-left enrichment thresholds (33% and 20%); and removal of low-mappability (≤0.8) or ENCODE-blacklist anchors. Singletons are discarded as likely false positives.
- **Systematic outperformance across cell numbers.** On 742 mES cells subsampled to 10–700, SnapHiC beat HiCCUPS (default and sparse-optimised parameters) on loop count and F1 at every subsample, with HiCCUPS loops largely a subset of SnapHiC's. Reproducibility between two 371-cell halves: **50.8% vs 38.7%** (P = 7.86 × 10⁻⁸) and 50.8% vs 39.7% (P = 9.90 × 10⁻¹¹).
- **Also beats FastHiC, FitHiC2, and HiC-ACT** at multiple thresholds — higher recall, equivalent or slightly lower precision, higher F1.
- **Two orthogonal validations of loop reality.** Aggregate peak analysis shows focal enrichment for loops called from ≥25 cells; and among loops with CTCF on both anchors, **63.6–78.7% are in convergent orientation** when ≥50 cells are used — the signature predicted by loop extrusion.
- **Known loops recovered from far fewer cells.** *Sox2*, *Wnt6*, and *Mtnr1a* long-range interactions were detected from **75 cells** by SnapHiC versus 200–600 for HiCCUPS.
- **Applied to human prefrontal cortex [[lee-2019-natmethods|sn-m3C-seq]]** (2,869 cells, 14 methylation-defined cell types): **817–27,379 loops per cell type** at 10-kb resolution, best F1 in every cell type except oligodendrocytes — which had ~278M intrachromosomal reads across 1,038 cells after aggregation, i.e. bulk-equivalent depth, where the bulk tools are appropriate again.
- **Cell-type-specific loops are functionally validated.** With cell number equalised at 261, loop anchors show significantly higher matched-cell-type ATAC-seq and H3K27ac signal and higher expression of promoter-linked genes, with matching GO terms.
- **788 SNP–gene linkages from 445 GWAS SNPs to 189 genes** across seven neuropsychiatric traits, including *INPP5D* and *SORL1* (Alzheimer's), *RAB27B* and *ZNF184* (MDD/schizophrenia). The showcase example: two astrocyte-specific loops connect the *APOE* TSS to enhancers containing Alzheimer's SNPs rs112481437 and rs138137383 — assigning *APOE* as the target **specifically in astrocytes**.

## Methods / evidence

Benchmarking on 742 diploid serum mES cells (Nagano data, filtered to >150,000 contacts/cell) with 11 subsampling levels × 6 permutations, against four bulk tools. Reference loop set built by combining bulk in situ Hi-C HiCCUPS loops with MAPS calls from H3K4me3 PLAC-seq, cohesin HiChIP, and H3K27ac HiChIP. Application to 2,869 PFC cells with ATAC/H3K27ac/RNA cross-validation from purified brain cell types.

Weight: the benchmark is thorough and the reference set is multi-assay. The main caveat is that the reference loops themselves come from bulk assays, so recall is measured against a bulk-defined truth — which structurally penalises any genuinely single-cell-specific loop.

## Surprising or load-bearing bits

- **"Cells as replicates, not as reads" is the transferable idea.** Every sparse single-cell modality faces the same choice, and the default everywhere is to aggregate. SnapHiC demonstrates the alternative pays, and quantifies by how much.
- **The 75-cell threshold changes what is askable.** Rare cell types in tissue — a few hundred nuclei — move from impossible to routine for loop calling.
- **Convergent CTCF orientation as a *validation metric*** rather than a biological finding is a neat trick: loop extrusion predicts it, so its rate is a proxy for precision that needs no reference loop set.
- **The oligodendrocyte exception is honest and informative.** Where cell number × depth reaches bulk equivalence, SnapHiC's advantage disappears. The method's value is explicitly a low-*n* value.
- **Systematic biases in imputed scHi-C are negligible** — the paper states normalisation against fragment size, GC, or mappability is unnecessary, unlike bulk Hi-C. Sparsity apparently swamps the systematic biases.
- **This paper is where GWAS interpretation meets single-cell 3D genome.** Assigning *APOE* to astrocyte-specific enhancer loops is the template for cell-type-resolved variant-to-gene mapping.

## Entities mentioned

- [[bing-ren]] — coauthor; 3D genome and regulatory element mapping.
- [[ming-hu]] — corresponding author; Hi-C statistical methodology.

## Concepts touched

- [[chromatin-loop]] — the first single-cell-native loop definition and caller.
- [[imputation]] — RWR reused from [[zhou-2019-schicluster|scHiCluster]] but for a different downstream task.
- [[single-cell-hi-c]] — the cells-as-replicates statistical framing.

## Connections to other sources

- Shares its imputation engine with [[zhou-2019-schicluster]] (RWR), but targets loops rather than clustering.
- Input data: [[nagano-2013-nature]]-lineage mES scHi-C; [[lee-2019-natmethods]] sn-m3C-seq for cortex.
- Cell-type labels come from methylation: [[luo-2017-snmc-seq]], [[luo-2018-snmc-seq2]].
- Contemporary and successor scHi-C methods: [[zhang-2022-higashi]] (embedding + TAD-like boundaries), [[xiong-2024-scghost]] (subcompartments), [[park-2026-mintsc]] (multi-way interactions, which uses SnapHiC-derived cliques as its baseline).
- Bulk comparators referenced: HiCCUPS (via [[durand-2016-juicer]]), FitHiC2, and pipeline context in [[servant-2015-hicpro]], [[abdennur-2020-cooler]], [[kerpedjiev-2018-higlass]].
- Loop-extrusion background: [[dixon-2012-tads]], [[lieberman-aiden-2009-hic]].
- Targeted-loop assays it is benchmarked against: PLAC-seq/HiChIP, and see [[li-2014-chia-pet]] for the protein-anchored lineage.

## Open questions

- **Loops are called per cell *type*, not per cell.** Despite treating cells as replicates, the output is a cell-type-level loop list — single-cell loop variability remains unmeasured.
- The 100 kb–1 Mb distance window excludes both short-range and very-long-range interactions; behaviour beyond 1 Mb is deferred to supplementary material.
- Reference loops derive from bulk assays, so any loop present only in single cells is scored as a false positive by construction.
- Whether the paired *t*-test's assumption of a homogeneous cell population holds within methylation-defined clusters is not tested — the same homogeneity assumption [[park-2026-mintsc]] later makes explicit.

## Related

- [[zhou-2019-schicluster]] · [[zhang-2022-higashi]] · [[chromatin-loop]] · [[40-Topics/3d-genome]]
