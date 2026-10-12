---
type: concept
title: chromVAR
aliases: [chromatin variability]
tags: [scATAC-seq, TF-motif, Greenleaf-lab, software]
created: 2026-05-12
updated: 2026-10-12
---

# chromVAR

> An R package that aggregates scATAC-seq signal across peaks sharing a TF motif, computes a bias-corrected deviation score per cell (controlling for GC content and mean accessibility), and outputs a robust TF-motif × cell matrix for clustering and de novo motif discovery ([[10-Summaries/schep-2017-chromvar|chromVAR]]).

> [!abstract] 한눈에
> chromVAR는 같은 TF motif를 가진 peak들의 접근성을 세포마다 합쳐 GC와 평균 접근성을 보정한 z-score로 바꾸고, 이렇게 해서 희소한 scATAC-seq 데이터를 motif × cell 행렬로 읽을 수 있게 한다 ([[10-Summaries/schep-2017-chromvar|chromVAR]]). 지금도 표준 TF 해석 도구로 쓰이지만, 미리 정한 peak와 7-mer에 의존한다는 점과 cell type 분리 성능은 다른 방법들과 비교해 비판을 받는다 ([[10-Summaries/de-boer-2018-brockman|BROCKMAN]]; [[10-Summaries/ashuach-2022-peakvi|PeakVI]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [scATAC-seq 희소성 시뮬레이터](../60-Explainers/single-cell-atac-seq.html)
<!-- /explainer-links -->

## Definition

chromVAR is a TF-motif accessibility tool from the Greenleaf lab ([[william-greenleaf]]) for sparse [[30-Concepts/scatac-seq]] data ([[10-Summaries/schep-2017-chromvar|chromVAR]]). For each motif it counts fragments in motif-containing peaks per cell, subtracts the expected count based on the cell average, then subtracts the mean deviation from GC- and accessibility-matched background peak sets and divides by the background SD ([[10-Summaries/schep-2017-chromvar|chromVAR]]). The result is a z-score per motif per cell, robust at ~10,000 fragments per cell, a typical scATAC yield ([[10-Summaries/schep-2017-chromvar|chromVAR]]).

## Why it matters

- It solves the per-locus sparsity problem of scATAC-seq by aggregating across many peaks per motif ([[10-Summaries/schep-2017-chromvar|chromVAR]]); see [[30-Concepts/transcription-factor-motif]].
- It identifies master regulators of haematopoiesis (HOXA9, SPI1, GATA1, TBX21) from sparse single-cell data ([[10-Summaries/schep-2017-chromvar|chromVAR]]).
- It is a standard downstream tool used with cisTopic, SnapATAC, EpiScanpy and scABC ([[10-Summaries/schep-2017-chromvar|chromVAR]]), and its motif × cell matrix supports [[30-Concepts/de-novo-motif-discovery]] ([[10-Summaries/schep-2017-chromvar|chromVAR]]).

## Uses and comparisons

| Context | What chromVAR did or how it compared | Source |
|---|---|---|
| AML patient stratification | Original application; see Evidence below | ([[10-Summaries/schep-2017-chromvar\|chromVAR]]) |
| Archival FFPE scATAC | chromVAR with JASPAR motifs used for TF enrichment on cell-type and condition-specific peaks | ([[10-Summaries/yadav-2025-scffpe-atac\|Yadav 2025]]) |
| PeakVI benchmark | Mixed batches best, but separated sorted cell types worse than PeakVI, cisTopic and LSA | ([[10-Summaries/ashuach-2022-peakvi\|PeakVI]]) |
| CellSpace bootstrap benchmark | CellSpace's embedding-based motif scores matched chromVAR on correlation with TF expression, and also gave a batch-mitigated embedding that chromVAR-based embeddings did not | ([[10-Summaries/tayyebi-2024-cellspace\|CellSpace]]) |
| BROCKMAN (developed concurrently) | Represents cells by gapped k-mers (k = 1–8) around all Tn5 insertions instead of predefined peaks | ([[10-Summaries/de-boer-2018-brockman\|BROCKMAN]]) |

## Evidence and examples

- In AML patient stratification, leukaemic stem cells are most similar to LMPPs while AML blasts cluster with monocytes, and SPI1 + CEBPA motifs distinguish stem-like from differentiated AML ([[10-Summaries/schep-2017-chromvar|chromVAR]]).
- In CellSpace's benchmark, 17 of 19 neurodevelopmental TFs had positive correlation between motif score and TF expression ([[10-Summaries/tayyebi-2024-cellspace|CellSpace]]).

## Contested points

- **Peak and k-mer dependence.** BROCKMAN argues that chromVAR's dependence on predefined peaks and ungapped 7-mers may reduce sensitivity to rare cell types and interpretability ([[10-Summaries/de-boer-2018-brockman|BROCKMAN]]).
- **Batch mixing versus cell-type separation.** chromVAR mixed batches best in PeakVI's benchmark but separated sorted cell types worse ([[10-Summaries/ashuach-2022-peakvi|PeakVI]]), while CellSpace reports that chromVAR-based embeddings were not batch-mitigated ([[10-Summaries/tayyebi-2024-cellspace|CellSpace]]); the two benchmarks use different data and metrics, so they are not direct contradictions (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scatac-seq|scATAC-seq]] — Single-cell chromatin accessibility by Tn5 transposition.
> - `concept` [[30-Concepts/transcription-factor-motif|Transcription factor motif]] — The sequence patterns chromVAR aggregates over.
> - `concept` [[30-Concepts/de-novo-motif-discovery|De novo motif discovery]] — Finding motifs without a predefined database.
> - `hub` [[40-Topics/single-cell-atac-seq|Single-cell ATAC-seq]] — Methods and analysis for single-cell chromatin accessibility.

## All sources on this page

> [!info]- 5 summaries cited here
> - [[10-Summaries/ashuach-2022-peakvi|Ashuach 2022]]
> - [[10-Summaries/de-boer-2018-brockman|de Boer & Regev 2018]]
> - [[10-Summaries/schep-2017-chromvar|Schep 2017]]
> - [[10-Summaries/tayyebi-2024-cellspace|Tayyebi 2024]]
> - [[10-Summaries/yadav-2025-scffpe-atac|Yadav 2025]]
