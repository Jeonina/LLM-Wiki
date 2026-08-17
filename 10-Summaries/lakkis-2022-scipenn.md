---
type: summary
title: "Lakkis et al. 2022 — A multi-use deep learning method for CITE-seq and single-cell RNA-seq data integration with cell surface protein prediction and imputation (sciPENN)"
source: "[[00-Sources/papers/A multi-use deep learning method for CITE-seq and single-cell RNA-seq data integration with cell surface protein prediction and imputation - Nature Machine Intelligence]]"
source_kind: paper
author: "Justin Lakkis, Amelia Schroeder, Kenong Su, Michelle Y. Y. Lee, Alexander C. Bashore, Muredach P. Reilly, Mingyao Li (corresponding)"
published: 2022-10-27
ingested: 2026-08-17
doi: "10.1038/s42256-022-00545-w"
journal: "Nature Machine Intelligence 4:940–952"
tags: [sciPENN, CITE-seq, protein-prediction, imputation, censored-loss, partial-panel-overlap, uncertainty-quantification, label-transfer]
entities: []
concepts: ["[[cite-seq]]", "[[multimodal-integration-methods]]", "[[imputation]]", "[[batch-effect]]", "[[cell-type-annotation]]"]
topics: ["[[single-cell-multiomics]]", "[[computational-methods]]"]
---

**Citation:** Lakkis et al. (2022) — *A multi-use deep learning method for CITE-seq and single-cell RNA-seq data integration with cell surface protein prediction and imputation* — *Nature Machine Intelligence* 4, 940–952. [DOI](https://doi.org/10.1038/s42256-022-00545-w)

# Lakkis 2022 — sciPENN

> CITE-seq is expensive; scRNA-seq is not. If the RNA→protein relationship can be learned from a CITE-seq reference, protein expression can be **predicted for scRNA-seq data that never measured it**. sciPENN does that, plus four related tasks, and its distinctive engineering contribution is a **censored loss** that lets multiple CITE-seq datasets be merged even when their **antibody panels only partially overlap**.

## Key claims

- **Five capabilities in one model**: CITE-seq + scRNA-seq integration; protein prediction for scRNA-seq; protein imputation for CITE-seq; **uncertainty quantification** on those predictions and imputations; and cell-type label transfer from CITE-seq to scRNA-seq.
- **Partial panel overlap is the unsolved problem it targets.** Combining CITE-seq datasets is hard because protein panels differ. Seurat 4 cannot do it at all; totalVI "can do it in theory, [but] this problem has not been explored." The censored-loss approach handles proteins absent from a given dataset as censored rather than missing-at-random.
- **Speed is the competitive claim.** Both [[gayoso-2021-totalvi|totalVI]] and especially [[hao-2021-seurat-wnn|Seurat 4]] are described as computationally expensive; sciPENN "performs markedly faster than its peers" while being more accurate.
- **Uncertainty quantification distinguishes it** from the alternatives — a predicted protein value with no confidence estimate is hard to use downstream, and neither Seurat 4 nor totalVI provides one.
- **The motivation is scale economics**: as multi-modality datasets grow, methods that are both accurate *and* efficient become the bottleneck for practical use.

## Methods / evidence

Comprehensive evaluations spanning multiple datasets against totalVI and Seurat 4 across the prediction, imputation, and integration tasks.

Weight: a machine-learning venue paper, so the evaluation is task-metric-driven and thorough on those metrics. What it cannot establish is whether predicted protein is *biologically usable* — accuracy against held-out measurements is not the same as trustworthiness for discovery. (synthesis)

## Surprising or load-bearing bits

- **Predicting a modality you did not measure is now a genre**, and this corpus now contains four instances attacking it from different directions: sciPENN (RNA→protein by deep learning), [[kang-2021-symphony|Symphony]] (RNA→protein by reference mapping), [[biancalani-2021-tangram|Tangram]] (RNA→spatial chromatin via a paired assay), [[debnath-2026-ison|ISON]] (spatial RNA→spatial ATAC by joint embedding). The shared premise is that a reference dataset can substitute for an experiment. The shared risk is that the prediction reproduces the reference's structure rather than the query's biology. (synthesis)
- **Uncertainty quantification is the feature that makes prediction defensible.** Without it, an imputed protein value is indistinguishable from a measured one in the output matrix — and will be treated as such by every downstream analysis. sciPENN is the only method in this group that returns a confidence. (synthesis)
- **The censored-loss trick generalises** beyond antibody panels to any setting where datasets share only part of a feature space — different gene panels in targeted assays, different marks in histone profiling.
- **"totalVI could do it in theory but nobody tried"** is an unusually candid statement about the gap between a model's stated capability and its demonstrated one.

## Concepts touched

- [[cite-seq]] — protein prediction and imputation as a substitute for measurement.
- [[imputation]] — with uncertainty, across modalities rather than within one.

## Connections to other sources

- Direct comparators: [[gayoso-2021-totalvi]], [[hao-2021-seurat-wnn]].
- Cross-modality prediction cousins: [[kang-2021-symphony]], [[biancalani-2021-tangram]], [[debnath-2026-ison]].
- Label-transfer alternatives: [[song-2021-scgcn]], [[butler-2018-seurat-cca]].
- Deep generative integration relatives: [[ashuach-2023-multivi]], [[cao-2022-glue]].
- Taxonomy and benchmark: [[argelaguet-2021-integration-principles]], [[xiao-2024-multiomics-benchmark]].
- Assay context: [[cite-seq]], [[baysoy-2023-multiomics-landscape]].

## Open questions

- **Predicted protein is not measured protein**, and no paper in this group establishes when the substitution is safe for discovery rather than for annotation. (synthesis)
- The RNA→protein relationship is tissue- and state-dependent; transferring a model trained on PBMCs to solid tissue is untested here.
- How well the censored loss handles panels with *small* overlap (a few shared antibodies) versus large overlap is the practical question and is not broken out.

## Related

- [[gayoso-2021-totalvi]] · [[hao-2021-seurat-wnn]] · [[cite-seq]] · [[40-Topics/single-cell-multiomics]]
