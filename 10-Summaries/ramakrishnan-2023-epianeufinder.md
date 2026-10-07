---
type: summary
title: "Ramakrishnan et al. 2023 — epiAneufinder identifies copy number alterations from single-cell ATAC-seq data"
source: "[[00-Sources/papers/epiAneufinder identifies copy number alterations from single-cell ATAC-seq data]]"
source_quality: full
source_sha256: "f21cf2a3c36bdb3c0a8e7b7ae3c63817ef52c0575173ade0b44bf3a94bb63d16"
source_kind: paper
author: "Akshaya Ramakrishnan, Aikaterini Symeonidi, Patrick Hanel, Katharina T. Schmid, Maria L. Richter, Michael Schubert, Maria Colomé-Tatché (last author)"
published: 2023-09-20
ingested: 2026-10-07
doi: "10.1038/s41467-023-41076-1"
journal: "Nature Communications 14:5846"
tags: [epiAneufinder, scATAC-seq, copy-number-alteration, CNA, aneuploidy, binary-segmentation, Anderson-Darling, intratumor-heterogeneity, Copy-scAT, inferCNV, CaSpER, CopyKAT, basal-cell-carcinoma, SNU601]
entities: ["[[20-Entities/maria-colome-tatche]]"]
concepts: ["[[copy-number-variation]]", "[[scatac-seq]]", "[[intratumor-heterogeneity]]", "[[pseudo-bulk]]", "[[mappability]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[single-cell-atac-seq]]", "[[cancer-clonal-evolution]]", "[[computational-methods]]"]
---

**Citation:** Ramakrishnan et al. (2023) — *epiAneufinder identifies copy number alterations from single-cell ATAC-seq data* — *Nature Communications* 14:5846. [DOI](https://doi.org/10.1038/s41467-023-41076-1)

# Ramakrishnan 2023 — epiAneufinder

> scATAC-seq sequences DNA, not RNA, so its read depth along the genome carries copy-number signal, if the sparsity can be handled. epiAneufinder bins reads (100 kb by default), corrects for GC, and runs **per-cell binary segmentation using the Anderson–Darling distance** between read-count distributions on either side of each bin. It prunes weak breakpoints and calls each segment **loss / normal / gain**. It needs **no euploid reference and no other modality**, so CNA calls come for free from existing scATAC or multiome data. Against (sc)WGS of the same lines it correlates better than three scRNA-based callers and the one prior scATAC caller (Copy-scAT). In basal cell carcinoma it reveals CNA clones that peak-based clustering cannot see.

## Key claims

- **Algorithm.** Filter low-coverage cells; bin the genome (default 100,000 bp); remove ENCODE blacklist regions and bins with zero counts in >85% of cells; LOESS GC correction. Per cell and chromosome, place the breakpoint that maximises the AD distance, recursively, up to 15 per chromosome by default. Prune breakpoints with AD below the genome-wide mean. Assign states from the trimmed mean (dropping the 0.1/0.9 quantile bins): z-score within [−1, 1] → genome-wide mean; rounded fold-change 0 → loss, 1 → normal, ≥2 → gain. Cells are clustered by Euclidean distance with Ward linkage into karyotype clusters.
- **Stated limits.** Only gain/loss/normal, with no exact copy number, because of sparsity. **Whole-genome duplications and deletions cannot be detected**, because they shift the genome-wide mean used as baseline.
- **SNU601 gastric cancer line (~3,500 cells, mean 75,013 fragments/cell)** against scWGS from a different lab (1,531 cells, mean 707,188 reads/cell, called with AneuFinder at the same 100-kb bins). Similar pseudo-bulk profiles; maximum F1 of 0.88 (loss), 0.93 (gain), 0.85 (normal); genome-wide MSE 0.09. The smallest CNA called was 100 kb (one bin); the largest gain 266,700 kb and largest loss 361,900 kb. scATAC pseudo-bulk was **less penetrant** than scWGS, missed sharp (peri)centromeric singularities, and missed a very penetrant chr5 gain.
- **More validation.** HCT116 (vs scWGS), COLO320 (vs WGS) and a primary paediatric glioblastoma (vs WGS) were "highly similar" by pseudo-bulk. Seven euploid brain samples plus PBMC and bone marrow showed minimal deviation from diploidy.
- **Benchmark.** On SNU601, correlation with scWGS was **0.86 for epiAneufinder, 0.74 for Copy-scAT**, and 0.61 for the best scRNA method (inferCNV). On HCT116 and COLO320 all scRNA methods (inferCNV, CaSpER, CopyKAT) fell to 0.2–0.4. Copy-scAT reports only chromosome-arm resolution by default; it agreed with epiAneufinder at r = 0.76.
- **Depth robustness (SNU601 downsampling).** At 10% of reads, 87% of the genome kept its full-data state on average across cells passing QC, but <15% of cells passed QC. At 50%, ~28% of loss bins and ~30% of gain bins were no longer called. Gain precision/recall ~0.82/0.65 and loss ~0.69/0.65. The normal state stayed >0.89 on all metrics. The discussion says overall profiles are recovered "even at 40% of the initial coverage".
- **Basal cell carcinoma (SU006, 2,040 cells; SU008, 504 cells).** Both tumours had a near-disomic cluster plus multiple CNA clusters (e.g., SU006 losses of chr2/9 with gains of 13/19, versus the reverse pattern). SU006 cancer cells were highly CNA-heterogeneous, SU008 much less so. Cancer-associated fibroblasts mapped to non-disomic karyotype clusters. **CNA clusters could not be recovered from peak-based embedding/Leiden clustering**, even using the same windows.

## Methods / evidence

Public scATAC (10x and others), multiome and (sc)WGS datasets; CNA ground truth from AneuFinder on scWGS or GC-normalised WGS. Comparison is by pseudo-bulk profiles (mean of 1/2/3 states per bin), with Pearson correlation, MSE and threshold-based precision/recall/F1. RNA methods were run with matched external euploid references (normal stomach, non-tumour colorectal, gut cell atlas). Downsampling used Cell Ranger ATAC subsampling.

Weight: the validation is at **pseudo-bulk level**, not per cell. No dataset had the same cells profiled by ATAC and DNA, and the SNU601 ATAC and scWGS came from different labs. The authors exclude a 134-cell high-ploidy scWGS cluster from the comparison. Per-cell accuracy, which is what "single-cell CNA" implies, is therefore not directly shown. (synthesis)

## Surprising or load-bearing bits

- **CNA heterogeneity is orthogonal to chromatin state.** In BCC, all cancer cells up-regulated cancer markers whatever their karyotype, and CNA clones were invisible to the usual peak-based clustering. Standard scATAC analysis silently ignores a whole layer of genetic variation already present in the data.
- **Read depth in scATAC is not uniform DNA sampling.** Accessible regions are over-represented, which may explain the less penetrant profiles and the missed chr5 gain. The paper attributes discrepancies to protocol and lab differences instead. (synthesis)
- **Gains degrade faster than losses with depth**, and false-positive losses rise at low coverage. Low-depth scATAC CNA calls should be read with an asymmetric error model in mind. (synthesis)
- **Whole-genome doubling is invisible** by design. In tumours where WGD is common, ploidy must come from elsewhere. (synthesis)

## Concepts touched

- [[copy-number-variation]] — CNA calling from a non-WGS modality, at 100-kb bins, ternary states.
- [[scatac-seq]] — read depth as a secondary genetic readout.
- [[intratumor-heterogeneity]] — karyotype clusters in BCC.
- [[pseudo-bulk]] — the level at which concordance is demonstrated.
- [[mappability]] — handled by blacklist plus a dataset-specific zero-count bin filter.

## Connections to other sources

- Validated against scWGS calls from [[bakker-2016-aneufinder]], the scWGS CNV caller on which Colomé-Tatché is also a co-author ([[bakker-2016-aneufinder]]); scDNA CNA context: [[mallory-2020-cna-review]], [[zahn-2017-dlp]], [[laks-2019-dlp-plus]], [[wang-2020-scope]].
- RNA-based comparators: [[tickle-2019-infercnv]], [[gao-2021-copykat]]. Note that CopyKAT is designed to identify its own diploid baseline cells ([[gao-2021-copykat]]), whereas here all RNA methods were run with an external reference. (synthesis)
- Parallel idea in methylation data: [[mukamel-2025-aneuploidy-brain]] reads aneuploidy from snmC-seq read density. Both turn an epigenomic assay's coverage into a karyotype. (synthesis)
- Downstream scATAC tooling used here: [[danese-2021-episcanpy]] (co-developed in the Colomé-Tatché group), [[traag-2019-leiden]], [[zhang-2008-macs]], [[mclean-2010-great]].
- Other "free" genetic signal from scATAC: mtDNA variants ([[ludwig-2019-mtdna-lineage-tracing]], [[kwok-2022-mquad]]) and nuclear SNVs ([[dou-2023-monopogen]]). (synthesis)

## Open questions

- Per-cell accuracy against same-cell DNA ground truth (e.g., a joint scATAC + scDNA assay) is not tested.
- How do open-chromatin differences between cell types confound copy-number signal in mixed tissues, when the euploid baseline is the genome-wide mean? (synthesis)
- Can allele-specific signal (heterozygous SNPs in ATAC reads) add LOH and copy-neutral events, which read depth alone cannot see? (synthesis)

## Related

- [[maria-colome-tatche]] · [[copy-number-variation]] · [[bakker-2016-aneufinder]] · [[40-Topics/single-cell-atac-seq]]
