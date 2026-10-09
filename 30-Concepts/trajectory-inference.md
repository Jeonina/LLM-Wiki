---
type: concept
title: Trajectory Inference
aliases: [pseudotime, pseudotemporal ordering, lineage trajectory, RNA velocity]
tags: [trajectory, pseudotime, PAGA, Monocle, development]
created: 2026-08-10
updated: 2026-10-08
---

# Trajectory Inference

> Ordering cells along a continuous process — differentiation, dose response, disease progression — rather than partitioning them into discrete groups. A snapshot population is treated as a sampling of a process, with position along the manifold standing in for time.

## The problem with trees

Biological processes are usually **incompletely sampled**, so the data do not conform to a connected manifold and modelling them as a continuous tree "has little meaning" ([[wolf-2019-paga]]). Clustering-based tree algorithms additionally assume clusters conform to a connected tree topology, and rely on feature-space inter-cluster distances that are only locally valid ([[wolf-2019-paga]]).

## Graph abstraction

PAGA partitions a kNN graph and builds a coarse graph whose edge weights measure connectivity between partitions — modularity-like, treating groups as connected when inter-partition edges exceed random expectation — so weak edges can be discarded and **genuinely disconnected regions can be reported as disconnected** ([[wolf-2019-paga]]). Cells are then ordered within partitions by a random-walk distance from a root, and a PAGA path averages the ensemble of single-cell paths through those groups, which is what supplies statistical power ([[wolf-2019-paga]]).

## Topology claims are sampling claims

The disputed origin of basophils resolves differently in three hematopoiesis datasets: one supports a basophil-neutrophil-monocyte progenitor, one a shared erythroid-megakaryocyte-basophil progenitor, and the largest and most densely sampled shows **both trajectories** ([[wolf-2019-paga]]). Sampling density, not method, determined the answer (synthesis).

## At atlas scale

56 trajectories were identified across two million cells, many detectable only because of the depth of cellular coverage ([[cao-2019-moca]]).

## Trajectories as a reference frame

A perturbation's effect is interpretable only relative to the natural differentiation direction: the perturbation score compares a simulated knockout vector to the differentiation vector, with negative meaning the knockout blocks differentiation and positive meaning it promotes it ([[kamimoto-2023-celloracle]]).

## Caution

Proliferation and cell death are outside most trajectory frameworks, so phenotypes mediated by differential expansion rather than fate change are invisible ([[kamimoto-2023-celloracle]]).

## Added 2026-10-07

Clonal ground truth showed that population balance analysis, WaddingtonOT and FateID missed an early neutrophil/monocyte fate boundary in CD34⁺ progenitors (R < 0.26 vs 0.5 for held-out clonal data), while pseudotime ordering was validated: consistent forward velocity and sister-cell pseudotime correlation R ≥ 0.89 [[10-Summaries/weinreb-2020-larry]].

mist extends pseudotime-based differential testing to single-cell DNA methylation, modelling gene-level methylation as logit-normal with a degree-4 polynomial mean and stage-specific variance, and ranking genes by the minimised area between fitted trajectories ([[10-Summaries/duan-2026-mist]]). Its authors recommend inferring pseudotime from another modality to avoid double-dipping, and note that a single scalar pseudotime oversimplifies branching processes ([[10-Summaries/duan-2026-mist]]).

The 'lineage plot' of Farlik et al. places single-cell methylomes on two axes. The axes are mean methylation over region sets whose residuals (after regressing out control methylation and CpG content) are significantly positive or negative between treatment endpoints ([[10-Summaries/farlik-2015-scwgbs]]). It correctly positioned held-out intermediate time points and opposite-direction differentiations, though the authors note overfitting risk at the endpoints used for selection ([[10-Summaries/farlik-2015-scwgbs]]).

In transplanted mammary basal cells at day 4.5, H3K4me1-based diffusion pseudotime showed a continuous basal-to-luminal progression while RNA-based pseudotime showed a binary switch. Epigenomic and transcriptional remodelling were therefore not synchronized during fate conversion ([[10-Summaries/schwager-2026-onecell-cut-tag]]).

Bootstrap-supported Slingshot trajectories on archival FFPE scATAC gene-activity embeddings (branches recovered in 83–97.5% of 1000 bootstraps) were used to propose two epithelial paths from tumor center to invasive edge and two normal-B-to-tumor paths in follicular lymphoma relapse ([[10-Summaries/yadav-2025-scffpe-atac]]).


## Added 2026-10-08 — sequence models & foundation models

- Diffusion pseudotime on layer-aggregated scDNAm-GPT embeddings ordered human (280 cells) and mouse (240 cells) oocyte-to-blastocyst stages better than raw methylation ratios, even though the model was fine-tuned only on cell-type labels ([[10-Summaries/liang-2025-scdnam-gpt]]).

## Related

- [[clustering-algorithms]] · [[dimensionality-reduction]] · [[lineage-tracing]] · [[computational-methods]]
