---
type: concept
title: Gene Regulatory Network
aliases: [GRN, eGRN, regulon, eRegulon, network inference]
tags: [GRN, transcription-factors, enhancers, network-inference, perturbation]
created: 2026-08-10
updated: 2026-10-12
---

# Gene Regulatory Network

> The set of transcription-factor-to-target relationships that specify a cell's identity. Inferring one from single-cell data means solving two problems at once: which elements a TF acts through, and which of the possible edges are active in a given cell state (synthesis).

> [!abstract] 한눈에
> GRN은 transcription factor와 표적 유전자 사이의 조절 관계 집합이며, 최근 방법들은 edge의 방향을 motif 같은 서열 정보에서 얻고 발현은 어떤 edge가 활성인지 고르는 데만 쓴다 ([[10-Summaries/kamimoto-2023-celloracle|CellOracle]]; [[10-Summaries/bravo-2023-scenicplus|SCENIC+]]). 정확도는 여전히 낮은 기준선에서 출발하며, 예측된 결합이 실제 조절인지는 기능적 perturbation으로 아직 충분히 검증되지 않았다 ([[10-Summaries/yuan-2024-linger|LINGER]]).

## Definition

Coexpression alone cannot establish causality (synthesis). Current frameworks solve this by deriving edge direction from genomic sequence and using expression only to select active edges ([[10-Summaries/kamimoto-2023-celloracle|CellOracle]]; [[10-Summaries/bravo-2023-scenicplus|SCENIC+]]). Two structural limitations of prior approaches are named precisely ([[10-Summaries/yuan-2024-linger|LINGER]]):

- Co-expression methods (WGCNA, ARACNe, GENIE3) produce **undirected** edges — TF_A–TF_B cannot be oriented — and correlation is not causal regulation ([[10-Summaries/yuan-2024-linger|LINGER]]).
- Motif-based footprinting **cannot distinguish within-family TFs** that share a motif; only bringing expression into the model breaks the tie ([[10-Summaries/yuan-2024-linger|LINGER]]), an argument the same group repeats for spatial data ([[10-Summaries/debnath-2026-ison|ISON]]).

## Why it matters

- **The enhancer layer.** Only **49% of enhancers are predicted to regulate their most proximal gene** — the quantitative case against nearest-gene assignment ([[10-Summaries/bravo-2023-scenicplus|SCENIC+]]).
- **TF cooperativity becomes computable.** Representing target regions shows that top cell-type-specific TFs largely co-bind shared enhancers, which is not seen for TFs specific to different cell types ([[10-Summaries/bravo-2023-scenicplus|SCENIC+]]).
- **Networks see what expression does not.** *Gata1*'s mild phenotype in early granulocyte differentiation is recovered by the network but **cannot be inferred from its low expression there** — the strongest argument for network reasoning ([[10-Summaries/kamimoto-2023-celloracle|CellOracle]]).

## Inference frameworks

| Framework | Regulatory scaffold | Edge activity / weighting | Output | Source |
|---|---|---|---|---|
| [[10-Summaries/kamimoto-2023-celloracle\|CellOracle]] | **Base GRN** from scATAC peaks classified into promoters and enhancers (TSS database plus co-accessibility from [[10-Summaries/pliner-2018-cicero\|Cicero]]), scanned for TF-binding motifs | Cluster-wise regularized linear regression on scRNA-seq with Bayesian/bagging pruning | Cluster-wise GRNs usable as perturbation operators | ([[10-Summaries/kamimoto-2023-celloracle\|CellOracle]]; [[10-Summaries/pliner-2018-cicero\|Cicero]]) |
| [[10-Summaries/bravo-2023-scenicplus\|SCENIC+]] | Topics and differentially accessible regions as enhancer candidates; motif enrichment against a 32,765-motif collection | GRNBoost2 importance scoring, with direction of regulation from linear correlation | **eRegulons** — a TF with its target enhancers *and* genes | ([[10-Summaries/bravo-2023-scenicplus\|SCENIC+]]) |
| [[10-Summaries/yuan-2024-linger\|LINGER]] | TF–RE motif priors injected by **manifold regularisation** into a non-linear model | **Lifelong learning**: pre-load knowledge from atlas-scale external **bulk** data across diverse contexts, then adapt to the multiome at hand | Three network levels (cell-population, cell-type-specific, cell-level), each with *trans* (TF–TG), *cis* (RE–TG) and TF-binding (TF–RE) edges; TF self-regulation excluded as unmodellable without additional data | ([[10-Summaries/yuan-2024-linger\|LINGER]]) |

LINGER reframes GRN inference as a **data** problem rather than a modelling one: single-cell data supplies many cells but few *independent* data points, while the model has enormous numbers of parameters ([[10-Summaries/yuan-2024-linger|LINGER]]).

### Networks as operators

Propagating a **shift** in expression rather than an absolute value lets the network act as a linear operator on a perturbation, converting a static structure into an in-silico knockout simulator trained only on unperturbed data ([[10-Summaries/kamimoto-2023-celloracle|CellOracle]]).

### Sequence and foundation models

- GET's gene-by-motif importance matrix can be fed to LiNGAM causal discovery to propose TF–TF interactions ([[10-Summaries/fu-2025-get|GET]]).
- scDynOmics sizes its low-rank attention space by TF regulon count (no cell expressed more than 700 TFs) and uses Integrated-Gradients attribution to prioritise regulators ([[10-Summaries/yu-2026-scdynomics|scDynOmics]]).
- ChromBERT ranks key regulators by how far their fine-tuned embeddings shift between region sets with different outcomes ([[10-Summaries/yu-2026-chrombert|ChromBERT]]).

## Evidence and examples

- Benchmarked against ChIP-seq ground truth, network inference reaches AUROC 0.66–0.85 with promoter-only base networks and 0.73–0.91 with scATAC-derived ones ([[10-Summaries/kamimoto-2023-celloracle|CellOracle]]).
- Systematic in-silico screening ranked TFs such that **85% of the top 30 are reported regulators** of myeloid differentiation ([[10-Summaries/kamimoto-2023-celloracle|CellOracle]]).
- Prospective prediction of a *noto* loss-of-function phenotype in zebrafish was experimentally validated ([[10-Summaries/kamimoto-2023-celloracle|CellOracle]]).
- LINGER reports a **fourfold to sevenfold relative increase** in accuracy, against a field the paper itself describes as having been "only marginally better than random prediction" ([[10-Summaries/yuan-2024-linger|LINGER]]).
- LiNGAM on GET's importance matrix gave 25.2% precision for its top 1% of TF–TF pairs against STRING (random 5.6%), and led to a PAX5–NR2C2 interaction that was confirmed by BioID and strengthened by the B-ALL risk variant G183S ([[10-Summaries/fu-2025-get|GET]]).
- scDynOmics prioritised Pou5f1, Jdp2 and Mbd3 in a 48 h vs 52 h mESC transition, genes that DE analysis missed ([[10-Summaries/yu-2026-scdynomics|scDynOmics]]).
- On PBMC data, 37 of the 84 regulators ChromBERT ranked highest were already reported for the matching cell type ([[10-Summaries/yu-2026-chrombert|ChromBERT]]).

## Open questions

- **Binding is not regulation.** Predicted enhancer-gene links are validated against TF-binding ChIP-seq, not against functional perturbation of the enhancer ([[10-Summaries/bravo-2023-scenicplus|SCENIC+]]).
- **Motif families.** Motif-based assignment cannot distinguish family members sharing a motif ([[10-Summaries/bravo-2023-scenicplus|SCENIC+]]; [[10-Summaries/yuan-2024-linger|LINGER]]).
- **Error propagation.** A substantial minority of inferred edges are wrong at reported AUROCs, and how that error propagates through iterative signal propagation is uncharacterized ([[10-Summaries/kamimoto-2023-celloracle|CellOracle]]).
- **Relative gains on a weak baseline.** LINGER's fourfold to sevenfold improvement is relative to a weak baseline, which is the honest reading of the number (synthesis).
- **Most single cells are not independent.** Thousands of cells from one donor, tissue and state carry far less information than the cell count suggests ([[10-Summaries/yuan-2024-linger|LINGER]]). The same caution applies to every method that treats cells as statistical replicates, including [[10-Summaries/yu-2021-snaphic|SnapHiC]] and [[10-Summaries/park-2026-mintsc|MINTsC]] (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/cis-regulatory-element|Cis-regulatory element]] — Enhancers, promoters and other non-coding regions through which TFs act.
> - `concept` [[30-Concepts/enhancer-states|Enhancer states]] — Active, primed, poised and decommissioned enhancers defined by histone marks.
> - `concept` [[30-Concepts/transcription-factor-motif|Transcription factor motif]] — The sequence pattern a TF binds, the source of edge direction in base GRNs.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — The tool layer, including network-inference frameworks.

## All sources on this page

> [!info]- 10 summaries cited here
> - [[10-Summaries/bravo-2023-scenicplus|Bravo 2023]]
> - [[10-Summaries/debnath-2026-ison|Debnath 2026]]
> - [[10-Summaries/fu-2025-get|GET 2025]]
> - [[10-Summaries/kamimoto-2023-celloracle|Kamimoto 2023]]
> - [[10-Summaries/park-2026-mintsc|Park 2026]]
> - [[10-Summaries/pliner-2018-cicero|Pliner 2018]]
> - [[10-Summaries/yu-2021-snaphic|Yu 2021]]
> - [[10-Summaries/yu-2026-chrombert|Yu 2026 ChromBERT]]
> - [[10-Summaries/yu-2026-scdynomics|scDynOmics 2026]]
> - [[10-Summaries/yuan-2024-linger|Yuan & Duren 2024]]
