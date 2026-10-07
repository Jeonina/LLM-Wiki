---
type: concept
title: scATAC-seq
aliases: [single-cell ATAC-seq, single-cell ATAC]
tags: [chromatin-accessibility, single-cell, ATAC, Tn5]
created: 2026-05-12
updated: 2026-10-07
---

# scATAC-seq

> Single-cell Assay for Transposase-Accessible Chromatin using sequencing. Profiles genome-wide chromatin accessibility in individual cells using hyperactive Tn5 transposase to insert sequencing adapters preferentially at open chromatin (regulatory elements) ([[10-Summaries/buenrostro-2015-nature]]; [[10-Summaries/cusanovich-2015-sciatac]]).

## Definition

Workflow: lyse cells / isolate nuclei → Tn5 tagmentation → barcoded library prep → sequencing ([[10-Summaries/buenrostro-2015-nature]]). Each cell yields ~1k–20k unique accessibility fragments (synthesis). The diploid genome inherently caps per-locus reads at 2, making scATAC-seq matrices extremely sparse — a structural property that drives downstream tool design ([[10-Summaries/derop-2024-natbiotech]]).

## Platforms

Two parallel cell-barcoding strategies emerged in 2015 and define the family today:

- **Microfluidic plate (Fluidigm C1)** — Buenrostro 2015 ([[10-Summaries/buenrostro-2015-nature]]); ~100 cells per run, deeper per-cell coverage.
- **Combinatorial indexing (sci-ATAC-seq)** — Cusanovich 2015 ([[10-Summaries/cusanovich-2015-sciatac]]); thousands of cells per run, no microfluidics, lower per-cell depth.

Subsequent platforms split along the same axis:

- **Nanowell / nanoliter Tn5** — µATAC-seq ([[10-Summaries/mezger-2018-microfluidic-atac]]) increases throughput while preserving per-cell coverage.
- **Droplet** — 10x Genomics Chromium scATAC (and 10x Multiome, which co-captures RNA in the same droplet); the dominant commercial platform today.
- **Combinatorial-droplet hybrids** — benchmarked by De Rop 2024's PUMATAC pipeline across eight protocols (10x v1/v1.1/v2/multiome/mtscATAC, Bio-Rad ddSEQ, HyDrop, s3-ATAC) ([[10-Summaries/derop-2024-natbiotech]]).

## Why it matters

- Maps cell-type-specific regulatory landscapes from heterogeneous tissue ([[10-Summaries/cusanovich-2015-sciatac]]).
- Provides the per-cell substrate for [[40-Topics/single-cell-multiomics]] when paired with RNA (10x Multiome, sci-CAR — [[10-Summaries/cao-2018-sci-car]]) or with genotype (GoT-ChA — [[10-Summaries/izzo-2024-got-cha]]).
- Foundation for the [[40-Topics/single-cell-atac-seq]] tooling stack: chromVAR ([[10-Summaries/schep-2017-chromvar]]), cisTopic ([[10-Summaries/bravo-2019-cistopic]]), SnapATAC2 ([[10-Summaries/zhang-2024-snapatac2]]), ArchR ([[10-Summaries/granja-2021-archr]]), EpiScanpy ([[10-Summaries/danese-2021-episcanpy]]), scABC ([[10-Summaries/zamanighomi-2018-scabc]]).

## Quality metrics

- **TSS enrichment** — fold-enrichment of reads at transcription start sites; primary per-cell QC signal ([[10-Summaries/derop-2024-natbiotech]]).
- **Unique fragments per cell** — typical thresholds 1,000–5,000 depending on platform (synthesis).
- **Fraction of reads in peaks (FRiP)** — proxy for signal-to-noise; varies systematically across platforms ([[10-Summaries/derop-2024-natbiotech]]).
- **Doublet rate** — droplet platforms inherit doublet artifacts from 10x scRNA chemistry.

## Contested points

- **Platform comparability** — PUMATAC benchmarking ([[10-Summaries/derop-2024-natbiotech]]) shows non-trivial systematic differences in peak calls and cell-type assignment across 10x / ddSEQ / HyDrop / s3-ATAC; cross-platform meta-analysis requires platform-aware correction.
- **Peak vs bin matrix** — fixed-genomic-bin matrices (SnapATAC2 — [[10-Summaries/zhang-2024-snapatac2]]) avoid peak-calling bias but inflate feature count; peak-based matrices are more interpretable but sensitive to peak-call parameters (ArchR instead uses a 500-bp tile matrix — [[10-Summaries/granja-2021-archr]]).
- **Sparsity vs information content** — only ~5–15% of accessible peaks fire per cell; binarization vs continuous count modeling remains a live methods debate (synthesis). Imputation/denoising is one response: scOpen (regularized NMF, [[10-Summaries/li-2021-scopen]]) and SCALE (VAE + GMM, [[10-Summaries/xiong-2019-scale]]) recover dropout signal, though whether imputation clarifies or hallucinates remains contested ([[10-Summaries/li-2021-scopen]]). See [[30-Concepts/scatac-imputation]].

## Variants and refinements

- **scATAC-seq (Tn5 only)** — Buenrostro 2015 ([[10-Summaries/buenrostro-2015-nature]]) and the family above.
- **scCUT&Tag / nano-CUT&Tag** — antibody-tethered protein A–Tn5 (scCUT&Tag) or nanobody–Tn5 fusions (nano-CUT&Tag) for histone-mark / TF profiling ([[10-Summaries/bartosovic-2021-sccut-tag]]; [[10-Summaries/bartosovic-2022-nano-cut-tag]]).
- **Multimodal** — sci-CAR (RNA + ATAC, [[10-Summaries/cao-2018-sci-car]]), SHARE-seq (RNA + ATAC, [[10-Summaries/ma-2020-cell]]), scNMT-seq (RNA + methylation + accessibility, [[10-Summaries/clark-2018-scnmt-seq]]), GoT-ChA (genotype + ATAC, [[10-Summaries/izzo-2024-got-cha]]), DOGMA-seq (RNA + ATAC + protein).

## Examples

- Cell-type-specific accessibility in heterogeneous hematopoietic populations ([[10-Summaries/buenrostro-2015-nature]]; [[10-Summaries/cusanovich-2015-sciatac]]).
- JAK2-V617F cell-intrinsic pro-inflammatory chromatin priming in HSCs, visible only by linking genotype to accessibility in the same cell ([[10-Summaries/izzo-2024-got-cha]]).
- Systematic benchmark of 8 scATAC-seq protocols across 47 PBMC experiments via the PUMATAC pipeline ([[10-Summaries/derop-2024-natbiotech]]).
- Computational benchmark of analysis methods across multiple datasets ([[10-Summaries/luo-2024-scatac-benchmark]]).

## Added 2026-10-07

Beyond accessibility, scATAC-seq read depth carries copy-number signal: in basal cell carcinoma, epiAneufinder found CNA clones that peak-based embedding and Leiden clustering could not recover ([[10-Summaries/ramakrishnan-2023-epianeufinder]]).

scNanoATAC-seq2 performs isolation, permeabilisation and Tn5 transposition of a single cell in one tube and reads fragments on Oxford Nanopore (median fragment 5,486 bp), giving a median 0.65% mitochondrial reads versus >50% in short-read embryo ATAC ([[10-Summaries/li-2025-scnanoatac-seq2]]). In 3,302 mouse preimplantation cells it detected ICM/TE epigenomic heterogeneity already at the 16-cell stage ([[10-Summaries/li-2025-scnanoatac-seq2]]).

GFETM jointly trains an embedded topic model (VAE with a linear decoder) and a pretrained genome foundation model over peak sequences, and reports transfer across tissues, species and omics plus imputation at unseen peaks ([[10-Summaries/fan-2026-gfetm]]). On clustering it matches scBasset; its gains are on unseen cells, unseen peaks and transfer, at about 3× scBasset's runtime ([[10-Summaries/fan-2026-gfetm]]).

Because scATAC-seq signal is nearly binary per locus, aggregating reads over feature sets (motif sites, co-regulated ENCODE DHS clusters, genes, MSigDB gene sets) separated GM12878 from HEK293T cells where peak-level clustering failed; SCRAT packaged this as a GUI toolbox with ENCODE-DNase-based identity inference [[10-Summaries/ji-2017-scrat]].

Analysis models for scATAC-seq now span peak-free k-mer factorisation ([[10-Summaries/de-boer-2018-brockman]]), Bernoulli VAEs with region- and cell-level nuisance factors ([[10-Summaries/ashuach-2022-peakvi]]), ZINB-based differential tests ([[10-Summaries/zhao-2024-scada]]) and a ~1.4B-parameter transformer pretrained on ~5 million cells that tokenises each cell as its accessible cCREs ([[10-Summaries/chen-2025-epiagent]]). Peak-by-cell matrices are cited as about 3% non-zero versus over 10% for scRNA-seq gene matrices ([[10-Summaries/zhao-2024-scada]]).

**Archival FFPE tissue.** Conventional split-and-pool scATAC-seq on FFPE nuclei fails to resolve cell types because formalin/paraffin DNA breaks collapse per-cell library complexity (e.g. only 30–595 cells passing QC vs 4843 fresh in mouse spleen) ([[10-Summaries/yadav-2025-scffpe-atac]]). scFFPE-ATAC rescues this by anchoring amplification on a single T7-promoter-bearing barcode and in vitro transcription, recovering 13,954 high-quality cells with r = 0.83 to fresh tissue, at the cost of lower FRiP (21% vs 42% fresh) ([[10-Summaries/yadav-2025-scffpe-atac]]).

**Sequence-informed embedding.** CellSpace co-embeds DNA k-mers and cells (StarSpace with N-grams and negative sampling) instead of reducing the cell-by-peak matrix, giving covariate-free batch mitigation and post hoc per-cell TF motif scores; it can integrate datasets processed against different peak atlases ([[10-Summaries/tayyebi-2024-cellspace]]).

Same-cell ground truth from wellDA-seq shows that copy number inferred from scATAC reads (10-Mb sliding windows, Satpathy-style method) correlated with directly measured CNAs at only median Pearson R = 0.47 in MDA-MB-231, with many false-positive events, and resolved none of the DNA-defined subclonal structure in three breast tumours ([[10-Summaries/wang-2024-wellda-seq]]). In the same data, ATAC clustering recovered DNA superclones but not finer subclones ([[10-Summaries/wang-2024-wellda-seq]]).

## Related

- [[30-Concepts/atac-seq]] · [[30-Concepts/tn5-tagmentation]] · [[30-Concepts/chromatin-accessibility]]
- [[30-Concepts/chromvar]] · [[30-Concepts/cistopic]] · [[30-Concepts/snapatac]] · [[30-Concepts/episcanpy]] · [[30-Concepts/scabc]]
- [[30-Concepts/scatac-imputation]] · [[30-Concepts/scopen]] · [[30-Concepts/scale]]
- [[30-Concepts/cut-and-tag]] · [[30-Concepts/scchic-seq]] · [[40-Topics/single-cell-multiomics]]
- [[40-Topics/single-cell-atac-seq]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/chromatin-architecture]]
