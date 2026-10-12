---
type: concept
title: scATAC-seq
aliases: [single-cell ATAC-seq, single-cell ATAC]
tags: [chromatin-accessibility, single-cell, ATAC, Tn5]
created: 2026-05-12
updated: 2026-10-12
---

# scATAC-seq

> Single-cell Assay for Transposase-Accessible Chromatin using sequencing: genome-wide chromatin accessibility in individual cells, read out by a hyperactive Tn5 transposase that inserts sequencing adapters preferentially into open chromatin (regulatory elements) ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]; [[10-Summaries/cusanovich-2015-sciatac|Cusanovich 2015]]).

> [!abstract] 한눈에
> scATAC-seq는 Tn5가 열린 chromatin에 adapter를 끼워 넣는 성질을 이용해 세포 하나하나의 accessibility를 읽는 방법이다 ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]). diploid 유전체에서는 한 locus의 read가 최대 2개라 행렬이 극도로 희소하고, 이 희소성을 어떻게 다룰지가 platform 선택과 분석 도구 설계를 좌우한다 ([[10-Summaries/derop-2024-natbiotech|De Rop 2024]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [염색질 구조 교재](../60-Explainers/chromatin-architecture.html)
>
> [scATAC-seq 희소성 시뮬레이터](../60-Explainers/single-cell-atac-seq.html)
<!-- /explainer-links -->

## Definition

The workflow is: lyse cells or isolate nuclei, tagment with Tn5, build a barcoded library, and sequence ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]). Each cell yields ~1k–20k unique accessibility fragments (synthesis). A diploid genome caps per-locus reads at 2, which makes scATAC-seq matrices extremely sparse — a structural property that drives downstream tool design ([[10-Summaries/derop-2024-natbiotech|De Rop 2024]]). Peak-by-cell matrices are cited as about 3% non-zero, versus over 10% for scRNA-seq gene matrices ([[10-Summaries/zhao-2024-scada|scaDA]]).

## Why it matters

- It maps cell-type-specific regulatory landscapes from heterogeneous tissue ([[10-Summaries/cusanovich-2015-sciatac|Cusanovich 2015]]).
- It provides the per-cell substrate for [[40-Topics/single-cell-multiomics]] when paired with RNA (10x Multiome; sci-CAR, [[10-Summaries/cao-2018-sci-car|Cao 2018]]) or with genotype (GoT-ChA, [[10-Summaries/izzo-2024-got-cha|GoT-ChA]]).
- It underlies the [[40-Topics/single-cell-atac-seq]] tooling stack (see the analysis-models table below).
- Its read depth also carries copy-number signal: in basal cell carcinoma, epiAneufinder found CNA clones that peak-based embedding and Leiden clustering could not recover ([[10-Summaries/ramakrishnan-2023-epianeufinder|epiAneufinder]]).

## Platforms

Two cell-barcoding strategies emerged in 2015 and still define the family ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]; [[10-Summaries/cusanovich-2015-sciatac|Cusanovich 2015]]). Later platforms split along the same axis (synthesis).

| Platform | Example | Throughput and depth | Source |
|---|---|---|---|
| Microfluidic plate (Fluidigm C1) | Buenrostro 2015 | ~100 cells per run, deeper per-cell coverage | ([[10-Summaries/buenrostro-2015-nature\|Buenrostro 2015]]) |
| Combinatorial indexing | sci-ATAC-seq | Thousands of cells per run, no microfluidics, lower per-cell depth | ([[10-Summaries/cusanovich-2015-sciatac\|Cusanovich 2015]]) |
| Nanowell / nanoliter Tn5 | µATAC-seq | Higher throughput while preserving per-cell coverage | ([[10-Summaries/mezger-2018-microfluidic-atac\|µATAC-seq]]) |
| Droplet | 10x Genomics Chromium scATAC; 10x Multiome (co-captures RNA in the same droplet) | Dominant commercial platform today | (synthesis) |
| Combinatorial-droplet hybrids and others | 10x v1/v1.1/v2/multiome/mtscATAC, Bio-Rad ddSEQ, HyDrop, s3-ATAC | Eight protocols benchmarked by the PUMATAC pipeline | ([[10-Summaries/derop-2024-natbiotech\|De Rop 2024]]) |
| Single-tube long-read | scNanoATAC-seq2 | Isolation, permeabilisation and Tn5 transposition of one cell in one tube, read on Oxford Nanopore (median fragment 5,486 bp) | ([[10-Summaries/li-2025-scnanoatac-seq2\|scNanoATAC-seq2]]) |
| Archival FFPE | scFFPE-ATAC | Single T7-promoter-bearing barcode plus in vitro transcription anchors amplification | ([[10-Summaries/yadav-2025-scffpe-atac\|scFFPE-ATAC]]) |

### Related assays and multimodal variants

- **scATAC-seq (Tn5 only)** — Buenrostro 2015 and the platforms above ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]).
- **scCUT&Tag / nano-CUT&Tag** — antibody-tethered protein A–Tn5 (scCUT&Tag) or nanobody–Tn5 fusions (nano-CUT&Tag) for histone-mark and TF profiling ([[10-Summaries/bartosovic-2021-sccut-tag|Bartosovic 2021]]; [[10-Summaries/bartosovic-2022-nano-cut-tag|Bartosovic 2022]]).
- **Multimodal** — sci-CAR (RNA + ATAC, [[10-Summaries/cao-2018-sci-car|Cao 2018]]), SHARE-seq (RNA + ATAC, [[10-Summaries/ma-2020-cell|Ma 2020]]), scNMT-seq (RNA + methylation + accessibility, [[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]), GoT-ChA (genotype + ATAC, [[10-Summaries/izzo-2024-got-cha|GoT-ChA]]), DOGMA-seq (RNA + ATAC + protein).

## Quality metrics

- **TSS enrichment** — fold-enrichment of reads at transcription start sites; the primary per-cell QC signal ([[10-Summaries/derop-2024-natbiotech|De Rop 2024]]).
- **Unique fragments per cell** — typical thresholds are 1,000–5,000 depending on platform (synthesis).
- **Fraction of reads in peaks (FRiP)** — a proxy for signal-to-noise that varies systematically across platforms ([[10-Summaries/derop-2024-natbiotech|De Rop 2024]]).
- **Doublet rate** — droplet platforms inherit doublet artifacts from 10x scRNA chemistry (synthesis).

## Analysis models

| Approach | Example | What it does | Source |
|---|---|---|---|
| TF motif accessibility | [[10-Summaries/schep-2017-chromvar\|chromVAR]] | TF motif accessibility from sparse single-cell data | ([[10-Summaries/schep-2017-chromvar\|chromVAR]]) |
| Topic modelling (LDA) | [[10-Summaries/bravo-2019-cistopic\|cisTopic]] | LDA topic modelling | ([[10-Summaries/bravo-2019-cistopic\|cisTopic]]) |
| Fixed-genomic-bin matrices | [[10-Summaries/zhang-2024-snapatac2\|SnapATAC2]] | Avoids peak-calling bias but inflates feature count | ([[10-Summaries/zhang-2024-snapatac2\|SnapATAC2]]) |
| Tile matrix | [[10-Summaries/granja-2021-archr\|ArchR]] | 500-bp tile matrix | ([[10-Summaries/granja-2021-archr\|ArchR]]) |
| Scanpy framework | [[10-Summaries/danese-2021-episcanpy\|EpiScanpy]] | scATAC-seq and scBS-seq in scanpy | ([[10-Summaries/danese-2021-episcanpy\|EpiScanpy]]) |
| Weighted k-medoids clustering | [[10-Summaries/zamanighomi-2018-scabc\|scABC]] | Unsupervised clustering | ([[10-Summaries/zamanighomi-2018-scabc\|scABC]]) |
| Feature-set aggregation | [[10-Summaries/ji-2017-scrat\|SCRAT]] | Aggregates reads over motif sites, co-regulated ENCODE DHS clusters, genes and MSigDB gene sets; GUI toolbox with ENCODE-DNase-based identity inference | ([[10-Summaries/ji-2017-scrat\|SCRAT]]) |
| Peak-free k-mer factorisation | [[10-Summaries/de-boer-2018-brockman\|BROCKMAN]] | Factorises k-mer content instead of peaks | ([[10-Summaries/de-boer-2018-brockman\|BROCKMAN]]) |
| Bernoulli VAE | [[10-Summaries/ashuach-2022-peakvi\|PeakVI]] | Region- and cell-level nuisance factors | ([[10-Summaries/ashuach-2022-peakvi\|PeakVI]]) |
| ZINB differential testing | [[10-Summaries/zhao-2024-scada\|scaDA]] | ZINB-based differential tests | ([[10-Summaries/zhao-2024-scada\|scaDA]]) |
| Imputation / denoising | [[10-Summaries/li-2021-scopen\|scOpen]], [[10-Summaries/xiong-2019-scale\|SCALE]] | Regularised NMF (scOpen) or VAE + GMM (SCALE) to recover dropout signal; see [[30-Concepts/scatac-imputation]] | ([[10-Summaries/li-2021-scopen\|scOpen]]; [[10-Summaries/xiong-2019-scale\|SCALE]]) |
| Sequence-informed co-embedding | [[10-Summaries/tayyebi-2024-cellspace\|CellSpace]] | Co-embeds DNA k-mers and cells (StarSpace with N-grams and negative sampling) instead of reducing the cell-by-peak matrix | ([[10-Summaries/tayyebi-2024-cellspace\|CellSpace]]) |
| Topic model + genome foundation model | [[10-Summaries/fan-2026-gfetm\|GFETM]] | Jointly trains an embedded topic model (VAE with linear decoder) and a pretrained genome foundation model over peak sequences | ([[10-Summaries/fan-2026-gfetm\|GFETM]]) |
| cCRE-token transformer | [[10-Summaries/chen-2025-epiagent\|EpiAgent]] | ~1.4B parameters, pretrained on ~5 million cells; each cell is tokenised as its accessible cCREs | ([[10-Summaries/chen-2025-epiagent\|EpiAgent]]) |
| Fragment-file transformer | [[10-Summaries/leroy-2025-atacformer\|Atacformer]] | Cell embeddings straight from fragment files, skipping peak calling and count matrices | ([[10-Summaries/leroy-2025-atacformer\|Atacformer]]) |
| Frozen DNA language model | [[10-Summaries/wang-2025-omnireg-gpt\|OmniReg-GPT]] | General-purpose DNA LM, frozen except one classification layer over 1,344-bp peak sequences | ([[10-Summaries/wang-2025-omnireg-gpt\|OmniReg-GPT]]) |

## Evidence and examples

**Biology**

- Cell-type-specific accessibility was resolved in heterogeneous hematopoietic populations ([[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]; [[10-Summaries/cusanovich-2015-sciatac|Cusanovich 2015]]).
- JAK2-V617F causes cell-intrinsic pro-inflammatory chromatin priming in HSCs, visible only by linking genotype to accessibility in the same cell ([[10-Summaries/izzo-2024-got-cha|GoT-ChA]]).
- scNanoATAC-seq2 gave a median 0.65% mitochondrial reads versus >50% in short-read embryo ATAC ([[10-Summaries/li-2025-scnanoatac-seq2|scNanoATAC-seq2]]).
- In 3,302 mouse preimplantation cells, scNanoATAC-seq2 detected ICM/TE epigenomic heterogeneity already at the 16-cell stage ([[10-Summaries/li-2025-scnanoatac-seq2|scNanoATAC-seq2]]).

**Platform and tissue benchmarks**

- PUMATAC systematically benchmarked 8 scATAC-seq protocols across 47 PBMC experiments ([[10-Summaries/derop-2024-natbiotech|De Rop 2024]]).
- Analysis methods were benchmarked computationally across multiple datasets ([[10-Summaries/luo-2024-scatac-benchmark|Luo 2024]]).
- Conventional split-and-pool scATAC-seq on FFPE nuclei fails to resolve cell types because formalin/paraffin DNA breaks collapse per-cell library complexity — only 30–595 cells passed QC versus 4843 fresh in mouse spleen ([[10-Summaries/yadav-2025-scffpe-atac|scFFPE-ATAC]]).
- scFFPE-ATAC recovered 13,954 high-quality cells with r = 0.83 to fresh tissue, at the cost of lower FRiP (21% vs 42% fresh) ([[10-Summaries/yadav-2025-scffpe-atac|scFFPE-ATAC]]).

**Analysis models**

- Aggregating reads over feature sets separated GM12878 from HEK293T cells where peak-level clustering failed, because scATAC-seq signal is nearly binary per locus ([[10-Summaries/ji-2017-scrat|SCRAT]]).
- CellSpace gives covariate-free batch mitigation and post hoc per-cell TF motif scores, and can integrate datasets processed against different peak atlases ([[10-Summaries/tayyebi-2024-cellspace|CellSpace]]).
- GFETM reports transfer across tissues, species and omics plus imputation at unseen peaks ([[10-Summaries/fan-2026-gfetm|GFETM]]).
- On clustering GFETM matches scBasset; its gains are on unseen cells, unseen peaks and transfer, at about 3× scBasset's runtime ([[10-Summaries/fan-2026-gfetm|GFETM]]).
- Atacformer's tokenise-plus-embed steps were about 2.5× faster than EpiAgent's ([[10-Summaries/leroy-2025-atacformer|Atacformer]]).
- OmniReg-GPT predicted per-cell accessibility at AUROC 0.717 on Buenrostro 2018 and gave cell embeddings that clustered better than scBasset, SnapATAC, ArchR and chromVAR ([[10-Summaries/wang-2025-omnireg-gpt|OmniReg-GPT]]).

**Copy number from accessibility reads**

- Against same-cell ground truth from wellDA-seq, copy number inferred from scATAC reads (10-Mb sliding windows, Satpathy-style method) correlated with directly measured CNAs at only median Pearson R = 0.47 in MDA-MB-231, with many false-positive events ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).
- The same ATAC-inferred copy number resolved none of the DNA-defined subclonal structure in three breast tumours, and ATAC clustering recovered DNA superclones but not finer subclones ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).

## Contested points

- **Platform comparability.** PUMATAC benchmarking shows non-trivial systematic differences in peak calls and cell-type assignment across 10x, ddSEQ, HyDrop and s3-ATAC, so cross-platform meta-analysis needs platform-aware correction ([[10-Summaries/derop-2024-natbiotech|De Rop 2024]]).
- **Peak vs bin matrix.** Fixed-genomic-bin matrices avoid peak-calling bias but inflate feature count ([[10-Summaries/zhang-2024-snapatac2|SnapATAC2]]); peak-based matrices are more interpretable but sensitive to peak-call parameters, and ArchR instead uses a 500-bp tile matrix ([[10-Summaries/granja-2021-archr|ArchR]]).
- **Sparsity vs information content.** Only ~5–15% of accessible peaks fire per cell, and binarisation versus continuous count modelling remains a live methods debate (synthesis). Imputation is one response ([[10-Summaries/li-2021-scopen|scOpen]]; [[10-Summaries/xiong-2019-scale|SCALE]]), though whether imputation clarifies or hallucinates remains contested ([[10-Summaries/li-2021-scopen|scOpen]]).
- **Copy number from ATAC.** epiAneufinder recovers CNA clones from scATAC read depth ([[10-Summaries/ramakrishnan-2023-epianeufinder|epiAneufinder]]), but same-cell DNA ground truth shows ATAC-inferred copy number is noisy and misses subclones ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]); the two used different inference methods, so this is not a direct test of epiAneufinder (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/atac-seq|ATAC-seq]] — The bulk assay this single-cell method derives from.
> - `concept` [[30-Concepts/tn5-tagmentation|Tn5 tagmentation]] — The transposase chemistry that inserts adapters into open chromatin.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — The property scATAC-seq measures.
> - `concept` [[30-Concepts/chromvar|chromVAR]] — TF motif accessibility from sparse single-cell data.
> - `concept` [[30-Concepts/cistopic|cisTopic]] — LDA topic modelling for scATAC-seq.
> - `concept` [[30-Concepts/snapatac|SnapATAC]] — Bin-based scATAC-seq analysis.
> - `concept` [[30-Concepts/episcanpy|EpiScanpy]] — scATAC-seq and scBS-seq in the scanpy framework.
> - `concept` [[30-Concepts/scabc|scABC]] — Weighted k-medoids clustering for scATAC-seq.
> - `concept` [[30-Concepts/scatac-imputation|scATAC-seq imputation]] — Denoising and dropout recovery for sparse accessibility data.
> - `concept` [[30-Concepts/scopen|scOpen]] — Regularised NMF imputation.
> - `concept` [[30-Concepts/scale|SCALE]] — VAE + Gaussian mixture model for scATAC-seq.
> - `concept` [[30-Concepts/cut-and-tag|CUT&Tag]] — Antibody-tethered Tn5 for histone marks and TFs.
> - `concept` [[30-Concepts/scchic-seq|scChIC-seq]] — Single-cell chromatin immunocleavage.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Platforms and the analysis stack for single-cell accessibility.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Assays that pair accessibility with RNA, methylation, protein or genotype.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — Accessibility, histone marks and 3D genome structure.

## All sources on this page

> [!info]- 32 summaries cited here
> - [[10-Summaries/ashuach-2022-peakvi|Ashuach 2022]]
> - [[10-Summaries/bartosovic-2021-sccut-tag|Bartosovic 2021]]
> - [[10-Summaries/bartosovic-2022-nano-cut-tag|Bartosovic 2022]]
> - [[10-Summaries/bravo-2019-cistopic|Bravo González-Blas 2019]]
> - [[10-Summaries/buenrostro-2015-nature|Buenrostro 2015]]
> - [[10-Summaries/cao-2018-sci-car|Cao 2018]]
> - [[10-Summaries/chen-2025-epiagent|Chen 2025]]
> - [[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]
> - [[10-Summaries/cusanovich-2015-sciatac|Cusanovich 2015]]
> - [[10-Summaries/danese-2021-episcanpy|Danese 2021]]
> - [[10-Summaries/de-boer-2018-brockman|de Boer & Regev 2018]]
> - [[10-Summaries/derop-2024-natbiotech|De Rop 2024]]
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
> - [[10-Summaries/granja-2021-archr|Granja 2021]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/ji-2017-scrat|Ji 2017]]
> - [[10-Summaries/leroy-2025-atacformer|Atacformer 2025]]
> - [[10-Summaries/li-2021-scopen|Li 2021]]
> - [[10-Summaries/li-2025-scnanoatac-seq2|Li 2025]]
> - [[10-Summaries/luo-2024-scatac-benchmark|Luo 2024]]
> - [[10-Summaries/ma-2020-cell|Ma 2020]]
> - [[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]
> - [[10-Summaries/ramakrishnan-2023-epianeufinder|Ramakrishnan 2023]]
> - [[10-Summaries/schep-2017-chromvar|Schep 2017]]
> - [[10-Summaries/tayyebi-2024-cellspace|Tayyebi 2024]]
> - [[10-Summaries/wang-2024-wellda-seq|Wang 2024]]
> - [[10-Summaries/wang-2025-omnireg-gpt|OmniReg-GPT 2025]]
> - [[10-Summaries/xiong-2019-scale|Xiong 2019]]
> - [[10-Summaries/yadav-2025-scffpe-atac|Yadav 2025]]
> - [[10-Summaries/zamanighomi-2018-scabc|Zamanighomi 2018]]
> - [[10-Summaries/zhang-2024-snapatac2|Zhang 2024]]
> - [[10-Summaries/zhao-2024-scada|Zhao 2024]]
