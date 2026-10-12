---
type: concept
title: SCALE (scATAC-seq analysis)
aliases: [SCALE, Single-Cell ATAC-seq analysis via Latent feature Extraction]
tags: [scATAC-seq, deep-learning, VAE, gaussian-mixture-model, imputation]
created: 2026-06-02
updated: 2026-10-12
---

# SCALE (scATAC-seq analysis via Latent feature Extraction)

> A deep generative method that models sparse scATAC-seq data by combining a **variational autoencoder (VAE)** with a **Gaussian Mixture Model (GMM)** prior over the latent space, supporting visualization, clustering, and denoising/imputation from interpretable latent features ([[10-Summaries/xiong-2019-scale|Xiong 2019]]).

> [!abstract] 한눈에
> SCALE은 VAE의 latent space에 Gaussian mixture prior를 두어 희소한 scATAC-seq 데이터를 clustering하고 imputation하는 deep generative 방법이다 ([[10-Summaries/xiong-2019-scale|Xiong 2019]]). 발표 당시에는 clustering 성능이 가장 좋았지만, 이후 PeakVI·scOpen·scCASE 등의 benchmark에서는 더 새로운 방법에 밀렸다 ([[10-Summaries/ashuach-2022-peakvi|PeakVI]]; [[10-Summaries/li-2021-scopen|scOpen]]; [[10-Summaries/tang-2024-sccase|scCASE]]).

## Definition

SCALE encodes each cell into a 10-dimensional latent variable on a GMM manifold (encoder 3200-1600-800-400; single-layer Bernoulli decoder), trained by maximizing the evidence lower bound = reconstruction term + KL divergence to the GMM ([[10-Summaries/xiong-2019-scale|Xiong 2019]]). The GMM prior gives a tighter posterior than a single-Gaussian VAE (e.g. scVI), which underfits sparse near-binary data ([[10-Summaries/xiong-2019-scale|Xiong 2019]]).

## Why it matters

- Demonstrated that scRNA-seq imputers (scVI) actively harm scATAC-seq analysis by making misclassified cells *less* similar to their true types — motivating ATAC-specific tooling ([[10-Summaries/xiong-2019-scale|Xiong 2019]]).
- The GMM yields disentangled latent dimensions that map onto biological cell types *and* can flag technical batch effects (plate-specific features), which can then be excluded from embedding ([[10-Summaries/xiong-2019-scale|Xiong 2019]]).

## How it compares

| Benchmark | Data | Result for SCALE | Source |
|---|---|---|---|
| Original paper | Six mixture datasets | Best overall clustering (ARI/NMI/F1) vs scABC, SC3, scVI, cisTopic (TF-IDF and Cicero compared only for visualization) | ([[10-Summaries/xiong-2019-scale\|Xiong 2019]]) |
| scOpen | scATAC imputation | A leading deep-learning entry; scOpen reports higher AUPR and lower memory | ([[10-Summaries/li-2021-scopen\|scOpen]]) |
| PeakVI | scATAC | Especially sensitive to library-size effects and weaker than PeakVI at separating sorted cell types, though good at mixing batches | ([[10-Summaries/ashuach-2022-peakvi\|PeakVI]]) |
| EpiAgent | scATAC | EpiAgent benchmarks above SCALE on clustering metrics | ([[10-Summaries/chen-2025-epiagent\|EpiAgent]]) |
| scCASE | scCAS enhancement | Used as a baseline and outperformed on clustering metrics; as a GPU-based method it uses less CPU memory than CPU tools | ([[10-Summaries/tang-2024-sccase\|scCASE]]) |
| scHPTM benchmark | Single-cell histone PTM datasets (<12,000 cells) | Not competitive with LSI-based methods; gained 21% from coverage-based cell filtering | ([[10-Summaries/raimundo-2023-schptm-benchmark\|Raimundo 2023]]) |

See [[30-Concepts/scatac-imputation]] for the wider imputation landscape.

## Evidence and examples

- Separated Epcam+ tumor from CD45+ immune cells in Pi-ATAC breast-tumor data from chromatin alone, comparable to the protein-indexed experimental method ([[10-Summaries/xiong-2019-scale|Xiong 2019]]).
- Imputation raised chromVAR significant motifs from 52 to 105 in forebrain data, recovering Mafb/Hoxd9 and MGE-pathway TFs ([[10-Summaries/xiong-2019-scale|Xiong 2019]]).

## Open questions

- **Does SCALE's weakness shrink with more cells?** On scHPTM data the benchmark authors conjecture that VAE methods could catch up at larger cell numbers ([[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]).
- **The original ranking has not held.** SCALE ranked first in its own paper but below newer methods in every later benchmark here; the comparisons use different datasets and metrics, so they are not directly comparable (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scatac-imputation|scATAC imputation]] — Recovering missing open-chromatin signal in sparse scATAC-seq.
> - `concept` [[30-Concepts/scopen|scOpen]] — Regularized-NMF imputation and denoising for scATAC-seq.
> - `concept` [[30-Concepts/cistopic|cisTopic]] — LDA topic modelling of cells and regulatory regions.
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Genome-wide chromatin accessibility in single cells via Tn5.
> - `concept` [[30-Concepts/chromvar|chromVAR]] — Bias-corrected TF-motif deviation scores per cell.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Analysis methods for sparse per-cell accessibility data.
> - `entity` [[20-Entities/qiangfeng-cliff-zhang|Qiangfeng Cliff Zhang]] — Tsinghua computational biology lab; senior author of SCALE.

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/ashuach-2022-peakvi|Ashuach 2022]]
> - [[10-Summaries/chen-2025-epiagent|Chen 2025]]
> - [[10-Summaries/li-2021-scopen|Li 2021]]
> - [[10-Summaries/raimundo-2023-schptm-benchmark|Raimundo 2023]]
> - [[10-Summaries/tang-2024-sccase|Tang 2024]]
> - [[10-Summaries/xiong-2019-scale|Xiong 2019]]
