---
type: note
title: "Computational framework — how to structure the review's main section"
aliases: [computational framework structure, computation section outline, analysis framework scaffold]
tags: [synthesis, computational, integration, review-paper-anchor, draft]
created: 2026-06-29
updated: 2026-06-29
sources: [
  "[[10-Summaries/lahnemann-2021-natcomm]]",
  "[[10-Summaries/heumos-2023-best-practices]]",
  "[[10-Summaries/bi-2024-multiomics-review]]",
  "[[10-Summaries/wang-2023-multimodal-review]]",
  "[[10-Summaries/argelaguet-2020-mofa-plus]]",
  "[[10-Summaries/ashuach-2023-multivi]]",
  "[[10-Summaries/cao-2022-glue]]",
  "[[10-Summaries/gong-2021-cobolt]]",
  "[[10-Summaries/stuart-2021-natmethods]]",
  "[[10-Summaries/xiao-2024-multiomics-benchmark]]",
  "[[10-Summaries/luquette-2019-natcomm]]",
  "[[10-Summaries/schep-2017-chromvar]]",
  "[[10-Summaries/angermueller-2017-genomebiol]]"
]
---

# Computational framework — how to structure the review's main section

> **Draft scaffold** (not prose) for the manuscript's main section. The argument: the 5-layer frame that organized the *measurement* sections is the wrong skeleton for the *computational* section, because computation's job is to **reassemble** the layers, not keep them apart. Organize by analysis logic that climaxes in integration. (synthesis)

The frame-switch is itself the argument — open the section by inverting the layer frame explicitly, then keep the 5 layers visible only as *inputs* (the matrix below), not as the section's spine. (synthesis)

---

## Why not mirror the 5 layers (the case to make in the opening paragraph)

- **Repetition.** Preprocessing, feature definition, dimensionality reduction, and clustering are nearly identical across all five layers — writing them per-layer means saying the same thing five times ([[10-Summaries/heumos-2023-best-practices]]; [[10-Summaries/lahnemann-2021-natcomm]]). (synthesis)
- **The punchline is cross-layer.** Integration methods (MOFA+, MultiVI, GLUE, Cobolt, Seurat WNN) exist precisely to *undo* the layer separation; a per-layer structure cannot contain its own climax ([[30-Concepts/multimodal-integration-methods]]; [[10-Summaries/bi-2024-multiomics-review]]). (synthesis)
- **The layers are not independent.** A region's state in one layer predicts the others, so treating them as parallel silos misrepresents the biology ([[50-Notes/regulatory-layers-overview]]). (synthesis)

## Proposed section structure

### 1. The shared computational substrate (cover once)

The pipeline common to every layer — state it once, then point back to it. The dominant cross-layer challenge is **sparsity / dropout**: single-cell matrices are extremely sparse and near-binary in the epigenomic layers ([[10-Summaries/lahnemann-2021-natcomm]]).

- Data structures & ecosystems: AnnData / Scanpy and the epigenomic fork EpiScanpy ([[30-Concepts/anndata]]; [[30-Concepts/scanpy]]; [[10-Summaries/danese-2021-episcanpy]]).
- Feature-matrix construction, normalization, dimensionality reduction, clustering, batch correction — the steps that recur across layers ([[10-Summaries/heumos-2023-best-practices]]).
- Pseudobulk aggregation as the bridge to bulk-derived ground truth ([[30-Concepts/pseudo-bulk]]).

### 2. Layer-specific inference (compact — one paragraph each, this is where the 5 layers legitimately reappear)

Only the genuinely *distinct* computational problem per layer; the matrix below carries the rest.

- **Genetic variation** — amplification error + allelic dropout demand specialized callers: Monovar, SCcaller, SCAN2, MosaicHunter/MosaicForecast, DeepMosaic ([[30-Concepts/single-cell-variant-calling]]; [[10-Summaries/zafar-2016-monovar]]; [[10-Summaries/dong-2017-sccaller]]; [[10-Summaries/luquette-2019-natcomm]]; [[10-Summaries/dou-2020-mosaicforecast]]; [[10-Summaries/yang-2023-deepmosaic]]); benchmarking shows low concordance across callers ([[10-Summaries/ha-2023-natmethods]]; [[10-Summaries/valecha-2022-scsnv-review]]). CNV from shallow coverage (SCOPE, CHISEL) and tree inference from imperfect genotype matrices (SCITE, SiFit, SCARLET, MEDICC2) ([[10-Summaries/wang-2020-scope]]; [[10-Summaries/zaccaria-2021-chisel]]; [[30-Concepts/phylogenetic-inference]]; [[10-Summaries/jahn-2016-scite]]; [[10-Summaries/kaufmann-2022-medicc2]]).
- **Chromatin accessibility** — feature-definition ambiguity (peaks vs bins vs k-mers), binarization, then TF-motif aggregation (chromVAR), topic models (cisTopic), and imputation/denoising (scOpen, SCALE); sequence-based CNNs (scBasset) are the deep-learning frontier ([[10-Summaries/schep-2017-chromvar]]; [[10-Summaries/bravo-2019-cistopic]]; [[30-Concepts/scatac-imputation]]; [[10-Summaries/li-2021-scopen]]; [[10-Summaries/xiong-2019-scale]]; [[10-Summaries/yuan-2022-scbasset]]); see the scATAC tool benchmark ([[10-Summaries/luo-2024-scatac-benchmark]]).
- **DNA methylation** — extreme sparsity (single-figure % CpG coverage/cell) drives imputation (DeepCpG, Melissa), variance-aware modeling (scMET), and probabilistic clustering (Epiclomal) ([[10-Summaries/angermueller-2017-genomebiol]]; [[10-Summaries/kapourani-2019-melissa]]; [[10-Summaries/kapourani-2021-scmet]]; [[10-Summaries/desouza-2020-epiclomal]]).
- **Histone modifications** — low coverage per mark; the distinctive problem is deconvolving multiplexed marks measured in one cell (scChIX) ([[10-Summaries/yeung-2023-scchix-seq]]).
- **3D genome** — contact-matrix sparsity; imputation and embedding of single-cell contact maps, haplotype-resolved reconstruction ([[10-Summaries/hong-2025-sc3d-genome-review]]; [[10-Summaries/jiang-2026-stark-scnucleome]]).

### 3. Cross-layer integration (the spine / climax)

Organize by the integration **topology**, which is inherently cross-layer (so it cannot be repetitive) ([[30-Concepts/multimodal-integration-methods]]):

- **Vertical (paired)** — modalities measured in the same cell; the problem is within-cell alignment ([[10-Summaries/bi-2024-multiomics-review]]).
- **Horizontal (unpaired)** — same modality across cell populations, anchored on shared genomic features ([[10-Summaries/wang-2023-multimodal-review]]).
- **Diagonal (unpaired)** — different modalities *and* different cells, no anchor — the hardest case, where batch correction risks erasing biology ([[10-Summaries/bi-2024-multiomics-review]]).

Cross these with the three method families ([[10-Summaries/wang-2023-multimodal-review]]): matrix factorization (MOFA+ — [[10-Summaries/argelaguet-2020-mofa-plus]]), manifold/anchor (Seurat WNN — [[10-Summaries/stuart-2021-natmethods]]), and deep generative models (MultiVI, GLUE, Cobolt — [[10-Summaries/ashuach-2023-multivi]]; [[10-Summaries/cao-2022-glue]]; [[10-Summaries/gong-2021-cobolt]]). Anchor the comparison on an integration benchmark ([[10-Summaries/xiao-2024-multiomics-benchmark]]).

### 4. The frontier (forward-looking close)

- **No method jointly reads all layers**, and no framework yet interprets mutation + epigenome + RNA at the locus level — the wiki's central open problem ([[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]]; [[50-Notes/joint-assays-by-layer-pair]]). (synthesis)
- **Ground-truth scarcity** is the binding constraint on benchmarking every layer-specific and integration method ([[10-Summaries/lahnemann-2021-natcomm]]). (synthesis)
- **Foundation/sequence models** (scBasset today) as the emerging direction toward layer-agnostic representation ([[10-Summaries/yuan-2022-scbasset]]). (synthesis)

---

## The task × layer matrix (the section's recurring visual)

Carry this as a figure/table so the 5 layers stay visible as *inputs* while the prose follows the task axis. (synthesis)

| Computational task | Genetic | Accessibility | Methylation | Histone | 3D |
|---|---|---|---|---|---|
| Feature definition | variants/CNV bins | peaks / bins / k-mers | CpG / tiles | mark bins | contact bins |
| Dominant noise problem | ADO + amp error | sparsity, binarization | extreme sparsity | low coverage/mark | matrix sparsity |
| Imputation/denoising | — | scOpen, SCALE | DeepCpG, Melissa | — | contact imputation |
| Specialized inference | Monovar, SCAN2, MosaicForecast; SCITE/MEDICC2 | chromVAR, cisTopic | scMET, Epiclomal | scChIX deconvolution | Dip-C-style reconstruction |
| Integration | — shared: MOFA+ / WNN / MultiVI / GLUE / Cobolt across all layers → — |

The bottom row is the point: integration is *not* per-layer — it is the one row that spans the whole table. (synthesis)

## Open questions for the section

- Whether to treat **variant calling** as "computation" (this section) or fold it into the genetic measurement section — it straddles both. (synthesis)
- How much **deep-learning / foundation-model** coverage the venue wants vs. classical methods. (synthesis)
- Whether the **3D layer** earns equal computational depth given the wiki's thinner tool coverage there. (synthesis)

## Related

- [[50-Notes/regulatory-layers-overview]] — the 5-layer measurement frame this section deliberately inverts
- [[50-Notes/joint-assays-by-layer-pair]] — the wet-lab side of integration (which assay bridges which pair)
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — the locus-state framework gap this section builds toward
- [[30-Concepts/multimodal-integration-methods]] — the integration taxonomy used in §3
- [[30-Concepts/single-cell-variant-calling]] · [[30-Concepts/scatac-imputation]] · [[30-Concepts/phylogenetic-inference]]
