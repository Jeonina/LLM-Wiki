---
type: topic
title: Single-cell ATAC-seq
aliases: [scATAC-seq, single-cell chromatin accessibility]
tags: [scATAC, chromatin-accessibility, cis-regulatory, software, transcription-factors]
created: 2026-05-12
updated: 2026-10-12
paper_section: ["3.2"]
---

# Single-cell ATAC-seq

> scATAC-seq measures genome-wide chromatin accessibility in individual cells via Tn5 transposase preferential cutting at open chromatin. Per-cell data are extremely sparse (only ~0/1/2 reads possible per locus per diploid cell), so analysis methods aggregate signal across peaks sharing a motif, bin the genome into wider windows, or apply topic modeling — each trading off resolution, scalability and rare-cell-type sensitivity ([[10-Summaries/schep-2017-chromvar|chromVAR]]; [[10-Summaries/fang-2021-snapatac|SnapATAC]]; [[10-Summaries/bravo-2019-cistopic|cisTopic]]).

> [!abstract] 한눈에
> scATAC-seq는 Tn5가 열린 크로마틴을 잘라내는 위치로 세포마다 접근성을 읽지만, 한 locus에서 얻을 수 있는 read가 0–2개뿐이라 motif, window, topic 단위로 신호를 모아 분석한다 ([[10-Summaries/schep-2017-chromvar|chromVAR]]; [[10-Summaries/fang-2021-snapatac|SnapATAC]]). 최근에는 수백만 세포 규모의 scATAC atlas가 foundation model의 사전학습 데이터로 쓰이고 있다 ([[10-Summaries/leroy-2025-atacformer|Atacformer]]; [[10-Summaries/liu-2025-clm-access|CLM-access]]).

## Key points

- **Sparsity drives the analysis design.** Methods aggregate peaks sharing a TF motif ([[10-Summaries/schep-2017-chromvar|chromVAR]]), bin the genome into peak-free 5-kb windows ([[10-Summaries/fang-2021-snapatac|SnapATAC]]) or apply LDA topic modelling ([[10-Summaries/bravo-2019-cistopic|cisTopic]]).
- **Pseudo-bulked scATAC agrees with bulk.** It matches bulk ATAC-seq and additionally reveals within-population heterogeneity ([[10-Summaries/gur-2025-scatac-vs-bulk|Gur 2025]]).
- **Motif-based accessibility cannot separate paralogous TFs.** TFs in one family share motifs, so chromVAR-style scores conflate them; joint expression + accessibility modelling can tell them apart ([[10-Summaries/debnath-2026-ison|ISON]]; [[10-Summaries/yuan-2024-linger|LINGER]]).
- **scATAC atlases now pretrain foundation models.** Atacformer tokenises cells into 890k consensus regions ([[10-Summaries/leroy-2025-atacformer|Atacformer]]) and CLM-access pretrains on 2.8M cells over a 1.15M-cCRE reference ([[10-Summaries/liu-2025-clm-access|CLM-access]]).
- **The assay is reaching new sample types.** Long-read scNanoATAC-seq2 maps mouse preimplantation embryos ([[10-Summaries/li-2025-scnanoatac-seq2|Li 2025]]) and scFFPE-ATAC profiles archival FFPE tissue ([[10-Summaries/yadav-2025-scffpe-atac|scFFPE-ATAC]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — The assay: genome-wide accessibility in single cells from Tn5 insertions.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Whether DNA is open or nucleosome-bound; the underlying biological signal.
> - `concept` [[30-Concepts/tn5-tagmentation|Tn5 tagmentation]] — Simultaneous fragmentation and adapter insertion by Tn5; the enzymatic basis.
> - `concept` [[30-Concepts/chromvar|chromVAR]] — Bias-corrected TF-motif deviation scores aggregated across peaks.
> - `concept` [[30-Concepts/snapatac|SnapATAC]] — Peak-free 5-kb-window Jaccard clustering, scaled to atlas size.
> - `concept` [[30-Concepts/scatac-imputation|scATAC imputation]] — Recovering missing open-chromatin signal from very sparse count matrices.

## Assays, platforms and benchmarks

scATAC-seq descends from bulk [[30-Concepts/atac-seq]].

| Assay or study | Year | Platform or sample | Note |
|---|---|---|---|
| [[10-Summaries/mezger-2018-microfluidic-atac\|µATAC-seq]] | 2018 | ICELL8 nanowell array | High-throughput nanoliter scATAC ([[10-Summaries/mezger-2018-microfluidic-atac\|Mezger 2018]]) |
| [[10-Summaries/derop-2024-natbiotech\|PUMATAC]] | 2024 | Protocol comparison | Systematic benchmarking of scATAC protocols ([[10-Summaries/derop-2024-natbiotech\|De Rop 2024]]) |
| [[10-Summaries/li-2025-scnanoatac-seq2\|scNanoATAC-seq2]] | 2025 | Long-read; mouse preimplantation embryos | Accessibility atlas covering ZGA, lineage segregation, iXCI and repeats ([[10-Summaries/li-2025-scnanoatac-seq2\|Li 2025]]) |
| [[10-Summaries/yadav-2025-scffpe-atac\|scFFPE-ATAC]] | 2025 | Archival FFPE | Rescues damaged DNA by T7 in vitro transcription ([[10-Summaries/yadav-2025-scffpe-atac\|Yadav 2025]]) |
| [[10-Summaries/nichols-2025-scimetv3\|sciMET+ATAC]] | 2025 | iCell8 nanowells (s3-ATAC) | Methylation + ATAC co-assay and an iCell8 implementation of s3-ATAC ([[10-Summaries/nichols-2025-scimetv3\|Nichols 2025]]) |
| [[10-Summaries/gur-2025-scatac-vs-bulk\|Gur 2025]] | 2025 | Pseudo-bulked scATAC vs bulk ATAC | Same signal as bulk, plus within-population heterogeneity ([[10-Summaries/gur-2025-scatac-vs-bulk\|Gur 2025]]) |

## Clustering, embedding and dimensionality reduction

| Tool | Year | Input | Model | Note |
|---|---|---|---|---|
| [[10-Summaries/ji-2017-scrat\|SCRAT]] | 2017 | Aggregated features | GUI toolbox | Early tool for scATAC, scDNase and scChIP ([[10-Summaries/ji-2017-scrat\|Ji 2017]]) |
| [[10-Summaries/schep-2017-chromvar\|chromVAR]] ([[30-Concepts/chromvar]]) | 2017 | Peaks grouped by TF motif | Motif aggregation | TF interpretation under sparsity ([[10-Summaries/schep-2017-chromvar\|Schep 2017]]) |
| [[10-Summaries/zamanighomi-2018-scabc\|scABC]] ([[30-Concepts/scabc]]) | 2018 | — | Weighted k-medoids | ([[10-Summaries/zamanighomi-2018-scabc\|Zamanighomi 2018]]) |
| [[10-Summaries/de-boer-2018-brockman\|BROCKMAN]] | 2018 | Gapped k-mers, peak-free | PCA | Out-of-peak reads are informative ([[10-Summaries/de-boer-2018-brockman\|de Boer 2018]]) |
| [[10-Summaries/bravo-2019-cistopic\|cisTopic]] ([[30-Concepts/cistopic]]) | 2019 | — | LDA topic modelling | ([[10-Summaries/bravo-2019-cistopic\|Bravo González-Blas 2019]]) |
| [[10-Summaries/xiong-2019-scale\|SCALE]] ([[30-Concepts/scale]]) | 2019 | — | VAE + Gaussian mixture | Interpretable latent features; reveals batch effects ([[10-Summaries/xiong-2019-scale\|Xiong 2019]]) |
| [[10-Summaries/fang-2021-snapatac\|SnapATAC]] ([[30-Concepts/snapatac]]) | 2021 | 5-kb windows, peak-free | Jaccard similarity, Nyström | Scales to 1M cells ([[10-Summaries/fang-2021-snapatac\|Fang 2021]]) |
| [[10-Summaries/danese-2021-episcanpy\|EpiScanpy]] ([[30-Concepts/episcanpy]]) | 2021 | scATAC and scBS-seq | scanpy framework | Python framework for epigenomics ([[10-Summaries/danese-2021-episcanpy\|Danese 2021]]) |
| [[10-Summaries/ashuach-2022-peakvi\|PeakVI]] | 2022 | — | Bernoulli VAE | Batch-corrected latent space and calibrated single-region differential accessibility ([[10-Summaries/ashuach-2022-peakvi\|Ashuach 2022]]) |
| [[10-Summaries/tayyebi-2024-cellspace\|CellSpace]] | 2024 | Sequence k-mers | k-mer/cell embedding | Implicit batch mitigation ([[10-Summaries/tayyebi-2024-cellspace\|Tayyebi 2024]]) |

A comparison of computational methods for single-cell chromatin data is in [[10-Summaries/luo-2024-scatac-benchmark|Luo 2024]].

## Imputation, denoising and differential accessibility

See [[30-Concepts/scatac-imputation]] for the dropout-recovery landscape.

| Tool | Year | Model | Note |
|---|---|---|---|
| [[10-Summaries/li-2021-scopen\|scOpen]] ([[30-Concepts/scopen]]) | 2021 | Regularized NMF imputation | Lowest memory; Runx1 in kidney fibrosis ([[10-Summaries/li-2021-scopen\|Li 2021]]) |
| [[10-Summaries/tang-2024-sccase\|scCASE / scCASER]] | 2024 | Similarity-learning NMF | Enhances scCAS data, optionally with reference data ([[10-Summaries/tang-2024-sccase\|Tang 2024]]) |
| [[10-Summaries/zhao-2024-scada\|scaDA]] | 2024 | ZINB composite test with dispersion shrinkage | Differential accessibility ([[10-Summaries/zhao-2024-scada\|Zhao 2024]]) |

## Sequence models and foundation models

| Model | Year | Pretraining or input | Key result |
|---|---|---|---|
| [[10-Summaries/fu-2025-get\|GET]] | 2025 | Pseudobulk scATAC of 213 cell types | Predicts gene expression in unseen cell types from accessible peaks and their motif content ([[10-Summaries/fu-2025-get\|Fu 2025]]) |
| [[10-Summaries/hingerl-2025-scooby\|scooby]] | 2025 | 524 kb of sequence per cell, 10x Multiome | Predicts scATAC insertion profiles and scRNA coverage together; TF activity scores beat chromVAR and scBasset ([[10-Summaries/hingerl-2025-scooby\|Hingerl 2025]]) |
| [[10-Summaries/leroy-2025-atacformer\|Atacformer]] | 2025 | Fixed vocabulary of 890k consensus regions; raw fragment files and bulk BED files | Cell-line prediction accuracy 86% across more than 275 lines ([[10-Summaries/leroy-2025-atacformer\|LeRoy 2025]]) |
| [[10-Summaries/liu-2025-clm-access\|CLM-access]] | 2025 | 2.8M cells, patch tokens over a 1.15M-cCRE reference | Binarising peaks and predicting each masked peak are both required for training to work ([[10-Summaries/liu-2025-clm-access\|Liu 2025]]) |
| [[10-Summaries/wu-2025-epifoundation\|EpiFoundation]] | 2025 | ATAC-only encoder with paired RNA as the pretraining target | Fine-tuned per-gene Pearson 0.38–0.48 for expression vs about 0.16–0.20 for Signac Gene Activity ([[10-Summaries/wu-2025-epifoundation\|Wu 2025]]) |
| [[10-Summaries/chen-2025-epiagent\|EpiAgent]] | 2025 | scATAC-seq | Transformer foundation model with perturbation prediction and in silico cCRE knockout ([[10-Summaries/chen-2025-epiagent\|Chen 2025]]) |
| [[10-Summaries/fan-2026-gfetm\|GFETM]] | 2026 | Genome-foundation-model-enhanced topic model | Unseen-cell embedding, leave-one-chromosome-out peak imputation, cross-tissue/species/omic transfer (bioRxiv v3 full text) ([[10-Summaries/fan-2026-gfetm\|Fan 2026]]) |
| [[10-Summaries/kempynck-2026-crested\|CREsted]] | 2026 | scATAC atlases → sequence-to-accessibility models | Reads enhancer codes and designs synthetic enhancers; contribution scores, unlike raw accessibility, are robust to CNVs in tumour scATAC ([[10-Summaries/kempynck-2026-crested\|Kempynck 2026]]) |
| [[10-Summaries/li-2026-epizoo\|EpiZoo]] | 2026 | Sequence-aware scATAC | Labels human cortex cells from macaque references with 0.91 accuracy; places human- and macaque-specific cCREs on a conservation gradient ([[10-Summaries/li-2026-epizoo\|Li 2026]]) |

## Beyond accessibility: copy number, spatial inference and regulation

- **Copy number from scATAC.** epiAneufinder calls per-cell copy-number alterations from scATAC-seq read depth ([[10-Summaries/ramakrishnan-2023-epianeufinder|epiAneufinder]]).
- **Spatial accessibility by inference.** Where the assay is unavailable, ISON infers spatial chromatin accessibility from spatial transcriptomics plus single-cell multiome, and reports that the inference recovers regulatory signal better than sparse direct measurement ([[10-Summaries/debnath-2026-ison|ISON]]).
- **Separating within-family TFs.** Because paralogous TFs share motifs, [[30-Concepts/chromvar|chromVAR]]-style methods cannot separate them, whereas ISON's joint expression + accessibility model estimates spot-level TF activity that distinguishes TFs within the same family ([[10-Summaries/debnath-2026-ison|ISON]]). LINGER uses paired accessibility and expression for GRN inference and makes the same point: motif-based footprinting cannot distinguish within-family TFs that share a motif ([[10-Summaries/yuan-2024-linger|LINGER]]).
- **Label transfer across layers.** scGCN benchmarks RNA→ATAC label transfer among 30 datasets — the demanding case, since the two modalities share no feature space and the mapping must run through gene-activity scores ([[10-Summaries/song-2021-scgcn|scGCN]]).
- **Transfer to scCUT&Tag.** A 2026 review sets out where scATAC tooling (Signac, ArchR, SnapATAC) does and does not transfer to scCUT&Tag ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).

## Key people

- [[20-Entities/william-greenleaf]] — Greenleaf lab; scATAC-seq, chromVAR, µATAC-seq.
- [[20-Entities/jason-buenrostro]] — chromVAR co-author; foundational hematopoietic scATAC datasets.
- [[20-Entities/stein-aerts]] — Aerts lab; cisTopic, SCENIC.
- [[20-Entities/bing-ren]] — Ren lab; SnapATAC, atlas-scale scATAC.
- [[20-Entities/fabian-theis]] — Theis lab; EpiScanpy, scanpy.

## Open questions

- Three-dimensional accessibility (combined ATAC + Hi-C in single cells) is now possible but the analysis tooling has not caught up. (synthesis)
- Most scATAC-seq tools are built on peak coordinates from aggregate signal, which biases them toward abundant cell types; SnapATAC's peak-free approach is a partial solution, but the field is still mostly peak-anchored ([[10-Summaries/fang-2021-snapatac|SnapATAC]]). (synthesis)
- Motif-level TF activity conflates paralogous TFs; how much of published chromVAR-based TF interpretation would change under joint expression + accessibility models ([[10-Summaries/debnath-2026-ison|ISON]]; [[10-Summaries/yuan-2024-linger|LINGER]])? (synthesis)
- Note not yet written: "How to choose a scATAC-seq analysis tool" — chromVAR for TF interpretation, cisTopic for trajectory-rich data with regulatory programs, SnapATAC for atlas-scale or rare-cell-type discovery, EpiScanpy for scanpy-native multi-omics workflows. (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA is packaged with proteins along chromosomes, across fibers, haplotypes and cells.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Measuring two or more molecular modalities in the same single cell.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Post-translational histone marks that demarcate functional chromatin states.

## All sources on this page

> [!info]- 34 summaries cited here
> - [[10-Summaries/ashuach-2022-peakvi|Ashuach 2022]]
> - [[10-Summaries/bravo-2019-cistopic|Bravo González-Blas 2019]]
> - [[10-Summaries/chen-2025-epiagent|Chen 2025]]
> - [[10-Summaries/danese-2021-episcanpy|Danese 2021]]
> - [[10-Summaries/de-boer-2018-brockman|de Boer & Regev 2018]]
> - [[10-Summaries/debnath-2026-ison|Debnath 2026]]
> - [[10-Summaries/derop-2024-natbiotech|De Rop 2024]]
> - [[10-Summaries/fan-2026-gfetm|Fan 2026]]
> - [[10-Summaries/fang-2021-snapatac|Fang 2021]]
> - [[10-Summaries/fu-2025-get|GET 2025]]
> - [[10-Summaries/gur-2025-scatac-vs-bulk|Gur & Hughes 2025]]
> - [[10-Summaries/hingerl-2025-scooby|scooby 2025]]
> - [[10-Summaries/ji-2017-scrat|Ji 2017]]
> - [[10-Summaries/kempynck-2026-crested|CREsted 2026]]
> - [[10-Summaries/leroy-2025-atacformer|Atacformer 2025]]
> - [[10-Summaries/li-2021-scopen|Li 2021]]
> - [[10-Summaries/li-2025-scnanoatac-seq2|Li 2025]]
> - [[10-Summaries/li-2026-epizoo|EpiZoo 2026]]
> - [[10-Summaries/liu-2025-clm-access|CLM-access 2025]]
> - [[10-Summaries/luo-2024-scatac-benchmark|Luo 2024]]
> - [[10-Summaries/mezger-2018-microfluidic-atac|Mezger 2018]]
> - [[10-Summaries/nichols-2025-scimetv3|Nichols 2025]]
> - [[10-Summaries/ramakrishnan-2023-epianeufinder|Ramakrishnan 2023]]
> - [[10-Summaries/schep-2017-chromvar|Schep 2017]]
> - [[10-Summaries/song-2021-scgcn|Song 2021]]
> - [[10-Summaries/tang-2024-sccase|Tang 2024]]
> - [[10-Summaries/tayyebi-2024-cellspace|Tayyebi 2024]]
> - [[10-Summaries/wu-2025-epifoundation|EpiFoundation 2025]]
> - [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]
> - [[10-Summaries/xiong-2019-scale|Xiong 2019]]
> - [[10-Summaries/yadav-2025-scffpe-atac|Yadav 2025]]
> - [[10-Summaries/yuan-2024-linger|Yuan & Duren 2024]]
> - [[10-Summaries/zamanighomi-2018-scabc|Zamanighomi 2018]]
> - [[10-Summaries/zhao-2024-scada|Zhao 2024]]
