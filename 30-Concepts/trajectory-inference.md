---
type: concept
title: Trajectory Inference
aliases: [pseudotime, pseudotemporal ordering, lineage trajectory, RNA velocity]
tags: [trajectory, pseudotime, PAGA, Monocle, development]
created: 2026-08-10
updated: 2026-10-12
---

# Trajectory Inference

> Ordering cells along a continuous process — differentiation, dose response, disease progression — rather than partitioning them into discrete groups. A snapshot population is treated as a sampling of a process, with position along the manifold standing in for time ([[10-Summaries/wolf-2019-paga|PAGA]]).

> [!abstract] 한눈에
> Trajectory inference는 한 시점에 채취한 세포들을 분화나 질병 진행 같은 연속적 과정 위에 배열하고, manifold 위의 위치를 시간의 대리 지표로 쓴다 ([[10-Summaries/wolf-2019-paga|PAGA]]). 추론된 topology는 방법보다 표본 밀도에 좌우되며, clonal ground truth로 검증하면 일부 fate 경계는 놓친다 ([[10-Summaries/wolf-2019-paga|PAGA]]; [[10-Summaries/weinreb-2020-larry|LARRY]]).

## Definition

Trajectory inference orders cells along a continuous process rather than partitioning them into discrete groups; a snapshot population is treated as a sampling of that process, with position along the manifold standing in for time ([[10-Summaries/wolf-2019-paga|PAGA]]).

## Why it matters

- A trajectory gives a reference frame for perturbations: a perturbation's effect is interpretable only relative to the natural differentiation direction ([[10-Summaries/kamimoto-2023-celloracle|CellOracle]]).
- At atlas scale, depth of cellular coverage makes trajectories detectable that would otherwise be missed: 56 trajectories were identified across two million cells ([[10-Summaries/cao-2019-moca|Cao 2019]]).
- Pseudotime can be carried into epigenomic layers, where it lets methylation or chromatin dynamics be tested along the same axis as expression ([[10-Summaries/duan-2026-mist|mist]]; [[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]).

## The problem with trees

- Biological processes are usually **incompletely sampled**, so the data do not conform to a connected manifold and modelling them as a continuous tree "has little meaning" ([[10-Summaries/wolf-2019-paga|PAGA]]).
- Clustering-based tree algorithms additionally assume clusters conform to a connected tree topology, and rely on feature-space inter-cluster distances that are only locally valid ([[10-Summaries/wolf-2019-paga|PAGA]]).

## Approaches

| Approach | Example | Input | What it does | Source |
|---|---|---|---|---|
| Graph abstraction | [[10-Summaries/wolf-2019-paga\|PAGA]] | kNN graph of cells | Partitions the kNN graph and builds a coarse graph whose edge weights measure connectivity between partitions — modularity-like, treating groups as connected when inter-partition edges exceed random expectation — so weak edges can be discarded and **genuinely disconnected regions can be reported as disconnected**; cells are ordered within partitions by a random-walk distance from a root, and a PAGA path averages the ensemble of single-cell paths through those groups, which supplies statistical power | ([[10-Summaries/wolf-2019-paga\|PAGA]]) |
| Atlas-scale trajectories | Monocle 3 in [[10-Summaries/cao-2019-moca\|Cao 2019]] | Two million cells (sci-RNA-seq3) | 56 trajectories, many detectable only because of the depth of cellular coverage | ([[10-Summaries/cao-2019-moca\|Cao 2019]]) |
| Bootstrap-supported Slingshot | [[10-Summaries/yadav-2025-scffpe-atac\|scFFPE-ATAC]] | Archival FFPE scATAC gene-activity embeddings | Branches recovered in 83–97.5% of 1000 bootstraps | ([[10-Summaries/yadav-2025-scffpe-atac\|scFFPE-ATAC]]) |
| Diffusion pseudotime on chromatin marks | [[10-Summaries/schwager-2026-onecell-cut-tag\|OneCell CUT&Tag]] | H3K4me1 profiles alongside RNA in the same cells | Pseudotime from the epigenome compared with pseudotime from RNA | ([[10-Summaries/schwager-2026-onecell-cut-tag\|Schwager 2026]]) |
| Diffusion pseudotime on model embeddings | [[10-Summaries/liang-2025-scdnam-gpt\|scDNAm-GPT]] | Layer-aggregated embeddings of single-cell methylomes | Orders developmental stages without time labels | ([[10-Summaries/liang-2025-scdnam-gpt\|scDNAm-GPT]]) |
| Lineage plot | [[10-Summaries/farlik-2015-scwgbs\|Farlik 2015]] | Single-cell methylomes | Two axes of mean methylation over region sets whose residuals (after regressing out control methylation and CpG content) are significantly positive or negative between treatment endpoints | ([[10-Summaries/farlik-2015-scwgbs\|Farlik 2015]]) |
| Pseudotime-based differential testing | [[10-Summaries/duan-2026-mist\|mist]] | Single-cell DNA methylation with a pseudotime | Models gene-level methylation as logit-normal with a degree-4 polynomial mean and stage-specific variance; ranks genes by the minimised area between fitted trajectories | ([[10-Summaries/duan-2026-mist\|mist]]) |
| Perturbation relative to a trajectory | [[10-Summaries/kamimoto-2023-celloracle\|CellOracle]] | Simulated knockout vector and differentiation vector | Perturbation score compares the two: negative means the knockout blocks differentiation, positive means it promotes it | ([[10-Summaries/kamimoto-2023-celloracle\|CellOracle]]) |

## Evidence and examples

**Validation against ground truth**

- Clonal ground truth showed that population balance analysis, WaddingtonOT and FateID missed an early neutrophil/monocyte fate boundary in CD34⁺ progenitors (R < 0.26 vs 0.5 for held-out clonal data) ([[10-Summaries/weinreb-2020-larry|LARRY]]).
- In the same data, pseudotime ordering was validated: consistent forward velocity and sister-cell pseudotime correlation R ≥ 0.89 ([[10-Summaries/weinreb-2020-larry|LARRY]]).
- Farlik's lineage plot correctly positioned held-out intermediate time points and opposite-direction differentiations ([[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]).

**Biological findings**

- The disputed origin of basophils resolves differently in three hematopoiesis datasets: one supports a basophil-neutrophil-monocyte progenitor, one a shared erythroid-megakaryocyte-basophil progenitor, and the largest and most densely sampled shows **both trajectories** ([[10-Summaries/wolf-2019-paga|PAGA]]).
- In transplanted mammary basal cells at day 4.5, H3K4me1-based diffusion pseudotime showed a continuous basal-to-luminal progression while RNA-based pseudotime showed a binary switch, so epigenomic and transcriptional remodelling were not synchronized during fate conversion ([[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]).
- Slingshot trajectories on FFPE scATAC were used to propose two epithelial paths from tumor center to invasive edge and two normal-B-to-tumor paths in follicular lymphoma relapse ([[10-Summaries/yadav-2025-scffpe-atac|scFFPE-ATAC]]).

**Foundation-model evidence**

- Diffusion pseudotime on layer-aggregated scDNAm-GPT embeddings ordered human (280 cells) and mouse (240 cells) oocyte-to-blastocyst stages better than raw methylation ratios, even though the model was fine-tuned only on cell-type labels ([[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT]]).

## Contested points

- **Topology claims are sampling claims.** In the basophil example, sampling density, not method, determined the answer (synthesis) ([[10-Summaries/wolf-2019-paga|PAGA]]).
- **Proliferation and death are invisible.** Proliferation and cell death are outside most trajectory frameworks, so phenotypes mediated by differential expansion rather than fate change are invisible ([[10-Summaries/kamimoto-2023-celloracle|CellOracle]]).
- **Double-dipping.** The mist authors recommend inferring pseudotime from another modality than the one being tested ([[10-Summaries/duan-2026-mist|mist]]).
- **A single scalar oversimplifies branching.** The mist authors note that one scalar pseudotime oversimplifies branching processes ([[10-Summaries/duan-2026-mist|mist]]).
- **Endpoint overfitting.** Farlik et al. note overfitting risk at the endpoints used to select the lineage-plot region sets ([[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]).
- **Fate-prediction methods disagree with clonal truth** even where pseudotime ordering holds up ([[10-Summaries/weinreb-2020-larry|LARRY]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/clustering-algorithms|Clustering algorithms]] — Partitioning cells into groups, usually by community detection on a kNN graph.
> - `concept` [[30-Concepts/dimensionality-reduction|Dimensionality reduction]] — Projecting single-cell measurements into a few coordinates for clustering and modelling.
> - `concept` [[30-Concepts/lineage-tracing|Lineage tracing]] — Reconstructing cell ancestry from natural or synthetic marks.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — The tool layer: aligners, callers, imputers, integrators and network inference.

## All sources on this page

> [!info]- 9 summaries cited here
> - [[10-Summaries/cao-2019-moca|Cao 2019]]
> - [[10-Summaries/duan-2026-mist|Duan 2026]]
> - [[10-Summaries/farlik-2015-scwgbs|Farlik 2015]]
> - [[10-Summaries/kamimoto-2023-celloracle|Kamimoto 2023]]
> - [[10-Summaries/liang-2025-scdnam-gpt|scDNAm-GPT 2025]]
> - [[10-Summaries/schwager-2026-onecell-cut-tag|Schwager 2026]]
> - [[10-Summaries/weinreb-2020-larry|Weinreb 2020]]
> - [[10-Summaries/wolf-2019-paga|Wolf 2019]]
> - [[10-Summaries/yadav-2025-scffpe-atac|Yadav 2025]]
