---
type: summary
title: "Gayoso et al. 2021 — Joint probabilistic modeling of single-cell multi-omic data with totalVI"
source: "[[00-Sources/papers/Joint probabilistic modeling of single-cell multi-omic data with totalVI]]"
source_kind: paper
author: "Adam Gayoso, Zoë Steier, Romain Lopez, Jeffrey Regier, Kristopher L. Nazor, Aaron Streets, Nir Yosef (corresponding)"
published: 2021-02-15
ingested: 2026-08-17
doi: "10.1038/s41592-020-01050-x"
journal: "Nature Methods 18:272–282"
tags: [totalVI, CITE-seq, variational-inference, deep-generative-model, protein-background, scvi-tools, differential-expression]
entities: ["[[nir-yosef]]"]
concepts: ["[[multimodal-integration-methods]]", "[[cite-seq]]", "[[batch-effect]]", "[[dimensionality-reduction]]", "[[joint-single-cell-multi-omics]]"]
topics: ["[[single-cell-multiomics]]", "[[computational-methods]]"]
---

**Citation:** Gayoso et al. (2021) — *Joint probabilistic modeling of single-cell multi-omic data with totalVI* — *Nature Methods* 18, 272–282. [DOI](https://doi.org/10.1038/s41592-020-01050-x)

# Gayoso 2021 — totalVI

> The deep-generative answer to CITE-seq, and its distinguishing feature is not the neural network but the **protein background model**. Antibody counts contain a large ambient/non-specific component that RNA counts do not; totalVI separates protein signal into **background and foreground** as part of the generative model, so background correction happens jointly with everything else rather than as a preprocessing hack.

## Key claims

- **Sequential analysis biases the result.** The prevailing practice — cluster on RNA, then contextualise with protein post hoc — "biases the analysis to one modality and becomes increasingly inefficient as CITE-seq measurements expand to hundreds of proteins."
- **The two modalities have genuinely different noise.** RNA noise has a mature modelling literature (scVI and relatives); protein has a distinct bias — **background from ambient or non-specifically bound antibodies** — with no equivalent treatment. totalVI adds a protein model that separates the two components.
- **One latent space, many tasks.** Output is (a) each cell as a distribution in a 20-dimensional latent space encoding both modalities while controlling for their noise and batch effects, and (b) parameters of the distributions underlying the observed counts, explicitly accounting for sequencing depth, protein background, and batch. From this single representation come dimensionality reduction, dataset integration, background correction, gene–protein correlation estimation, and differential expression testing.
- **Integration works even with different antibody panels**, and a subset of the input datasets can be RNA-only — the scalability requirement the Human Cell Atlas creates as CITE-seq enters community atlases.
- **Validated on new data**: the authors generated CITE-seq on murine spleen and lymph node measuring up to **208 proteins**.
- **Batch is an optional categorical covariate**, so the model handles experimental batch and donor within the same machinery as everything else.

## Methods / evidence

New CITE-seq data (murine spleen and lymph node, up to 208 proteins) plus public datasets, evaluated across five analysis tasks. Implemented in scvi-tools.

Weight: evaluation is task-by-task rather than against a single ground truth, which is inherent to the problem — there is no gold-standard "correct" joint representation. The protein background separation is the claim most amenable to validation and is the one most reused.

## Surprising or load-bearing bits

- **Protein background is the modality-specific problem the field had been ignoring.** It is not noise in the statistical sense; it is a systematic additive component, and treating it as noise inflates apparent expression in every negative population. This is the CITE-seq analogue of the ambient-RNA problem, and totalVI is where it got a principled treatment. (synthesis)
- **A probabilistic representation, not a point estimate.** Each cell is a *distribution* in latent space — which is what makes downstream uncertainty-aware differential expression possible, and is the structural difference from [[hao-2021-seurat-wnn|WNN]]'s per-cell weights. (synthesis)
- **totalVI and WNN were published four months apart** solving the same CITE-seq problem from opposite methodological traditions: deep generative modelling versus nearest-neighbour graph weighting. [[lakkis-2022-scipenn|sciPENN]] then benchmarked against both and argued both are computationally expensive. (synthesis)
- **scvi-tools as infrastructure** — totalVI is one model in a framework that also produces [[ashuach-2023-multivi|MultiVI]], so the CITE-seq and RNA+ATAC problems share a codebase and a modelling philosophy.
- **"Different measured proteins" integration** is the capability [[lakkis-2022-scipenn|sciPENN]] says totalVI could do "in theory" but had not explored — an unusual case of a follow-up crediting an untested capability.

## Entities mentioned

- [[nir-yosef]] — corresponding author; scVI/scvi-tools line.

## Concepts touched

- [[cite-seq]] — the protein background/foreground decomposition.
- [[multimodal-integration-methods]] — deep generative vertical integration.

## Connections to other sources

- Same-problem contemporary from the anchor tradition: [[hao-2021-seurat-wnn]].
- Faster deep-learning competitor that benchmarks against both: [[lakkis-2022-scipenn]].
- Same framework, RNA+ATAC instead of RNA+protein: [[ashuach-2023-multivi]]; unpaired/diagonal counterpart [[cao-2022-glue]]; earlier factorisation approach [[argelaguet-2020-mofa-plus]].
- Taxonomy: [[argelaguet-2021-integration-principles]]; benchmark [[xiao-2024-multiomics-benchmark]].
- Batch-correction ancestors: [[haghverdi-2018-mnn]], [[korsunsky-2019-harmony]].
- Reference mapping that infers surface protein from a CITE-seq atlas: [[kang-2021-symphony]].
- A counterexample to the deep-generative default: [[debnath-2026-ison]] finds linear KL-NMF beats a contrastive VAE.

## Open questions

- **20 latent dimensions is a fixed choice** justified in a supplementary note; sensitivity to it is not foregrounded.
- Deep generative models are hard to audit — which part of the latent space encodes background versus biology is not directly interpretable, unlike a factor model such as [[argelaguet-2020-mofa-plus|MOFA+]]. (synthesis)
- Computational cost, flagged as a problem by [[lakkis-2022-scipenn]], is not quantified here.

## Related

- [[hao-2021-seurat-wnn]] · [[ashuach-2023-multivi]] · [[cite-seq]] · [[40-Topics/single-cell-multiomics]]
