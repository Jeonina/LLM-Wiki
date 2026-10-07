---
type: summary
title: "Argelaguet et al. 2018 — Multi-Omics Factor Analysis: a framework for unsupervised integration of multi-omics data sets"
source: "[[00-Sources/papers/Multi‐Omics Factor Analysis—a framework for unsupervised integration of multi‐omics data sets - Molecular Systems Biology.pdf]]"
source_quality: full
source_sha256: "2d7b93439f8f9da516cad52d3bf2ebe0195525a20d7361b42191b4a90b3fd209"
source_kind: paper
author: "Ricard Argelaguet, Britta Velten, Damien Arnol, Sascha Dietrich, Thorsten Zenz, John C Marioni, Florian Buettner (corresponding), Wolfgang Huber (corresponding), Oliver Stegle (corresponding)"
published: 2018-06-20
ingested: 2026-10-07
updated: 2026-10-07
doi: "10.15252/msb.20178124"
journal: "Molecular Systems Biology 14(6):e8124"
tags: [MOFA, factor-analysis, group-factor-analysis, multi-omics-integration, unsupervised, variational-bayes, CLL, scMT-seq]
entities: ["[[oliver-stegle]]"]
concepts: ["[[multimodal-integration-methods]]", "[[dimensionality-reduction]]", "[[imputation]]", "[[joint-single-cell-multi-omics]]"]
topics: ["[[single-cell-multiomics]]", "[[computational-methods]]"]
---

**Citation:** Argelaguet et al. (2018) — *Multi‐Omics Factor Analysis—a framework for unsupervised integration of multi‐omics data sets* — *Molecular Systems Biology* 14(6):e8124. [DOI](https://doi.org/10.15252/msb.20178124)

# Argelaguet 2018 — MOFA

> MOFA is a Bayesian group factor analysis model — described by the authors as a "versatile and statistically rigorous generalization of PCA to multi-omics data" — that decomposes M data matrices measured on the same (or partially overlapping) samples into one shared factor matrix **Z** and one sparse weight matrix **W**ᵐ per modality (Yᵐ = ZWᵐᵀ + εᵐ). Its point is interpretability: each factor's variance explained per modality tells you whether an axis of heterogeneity is shared across omics layers or private to one, and sparse loadings point at the driving features. The authors show this on 200 chronic lymphocytic leukaemia (CLL) patients with four incomplete data types (mutations, RNA, DNA methylation, ex vivo drug response), where MOFA recovers IGHV status and trisomy 12 as the top two axes, surfaces an oxidative-stress axis, and produces factors that predict time to next treatment; and on 87 mouse ES cells profiled by single-cell methylation + transcriptome (scM&T-seq), where two continuous factors trace naive → primed → differentiated states with coordinated methylation changes.

## Key claims

- **Model.** Yᵐ = ZWᵐᵀ + εᵐ with a standard-normal prior on factors Z and two-level sparsity on weights: an Automatic Relevance Determination (ARD) prior for view- and factor-wise sparsity (which factor is active in which view) plus a spike-and-slab prior for feature-wise sparsity. Inference is mean-field variational Bayes (ELBO); non-Gaussian data use Poisson (counts) or Bernoulli (binary) likelihoods via variational lower bounds; missing values (including whole missing assays) are handled natively.
- **Factor number is learned.** Factors are pruned during training below a user-set minimum fraction of variance explained; analyses here start at K = 25 and prune at 2% variance. The optimisation is non-convex, so results use 10–25 random restarts and keep the highest-ELBO model.
- **Simulations.** MOFA accurately reconstructed the latent dimension except with large numbers of factors or high proportions of missing values; non-Gaussian likelihoods improved fit for binary/count data. Against GFA and iCluster, those tended to infer redundant factors and were less accurate at recovering shared-factor activity patterns; MOFA was also more consistent across model instances.
- **Speed.** On the CLL data, training took 25 min with MOFA vs 34 h with GFA and 5–6 days with iCluster (Fig EV1).
- **CLL application (N = 200).** Inputs: mutations (D = 69, N = 200), mRNA (D = 5,000, N = 136), methylation (D = 4,248, N = 196), drug response (D = 310 = 62 drugs × 5 concentrations, N = 184); nearly 40% of samples lacked at least one omics type. MOFA found 10 factors that cumulatively explained 41% of drug-response, 38% of mRNA, 24% of methylation and 24% of mutation variance.
  - Factor 1 aligned with **IGHV** mutation status and Factor 2 with **trisomy 12** — together accounting for < 20% of variance. Factor 1 suggested more than a binary split: 3-means clustering gave LZ/IZ/HZ groups, consistent with proposed three-subgroup models, with loadings on known IGHV-associated genes and on drugs targeting the B-cell receptor pathway.
  - Factor 5 (mRNA + drug response) tagged oxidative-stress and senescence pathways, with top weights on **heat-shock protein** genes, and drugs with top weights related to oxidative stress (ROS, DNA damage, apoptosis) — an axis the authors call underappreciated in CLL. Factor 4 (9% of mRNA variance) suggested contamination by other cell types (T cells, monocytes); Factor 3 (11% of drug-response variance) captured general drug sensitivity.
  - **Outlier detection:** Factor 1 agreed with clinical IGHV status for 176 of 200 patients, classified 12 patients lacking a clinical IGHV label, and reassigned 12 others; of those, nine showed intermediate signatures and three were clearly discordant, confirmed as outliers by independent drug-response assays and whole-exome sequencing.
  - **Imputation:** MOFA beat feature-wise mean, SoftImpute and kNN imputation, and was more robust than GFA, both for missing values and for entirely missing assays (evaluated on the N = 121 complete-case subset by masking).
  - **Clinical prediction:** Factors 1, 7 and 8 were significantly associated with time to next treatment (Cox, FDR < 1%; N = 174, 96 uncensored). Factor 7 captured del17p and TP53 mutations plus oncogene methylation differences; Factor 8 related to WNT signalling. A multivariate Cox model on the 10 MOFA factors gave higher Harrell's C-index (~0.78 by Fig 4C) than PCA components from single modalities or the concatenated data, individual features, or MOFA factors from subsets of modalities.
- **Single-cell application (scMT).** 87 mESCs (16 in "2i" naive-state medium, 71 serum-grown primed) from Angermueller et al. 2016 with RNA (top 5,000 variable genes) and CpG methylation summarised at promoters, CpG islands and enhancers (top 5,000 variable CpG sites each). Three factors: Factor 1 shared across all modalities (7% of RNA variance, 53–72% of methylation variance) captured naive → primed transition (pluripotency markers Rex1/Zpf42, Tbx3, Fbxo15, Esrrb) coupled to genome-wide methylation change; Factor 2 (RNA-dominant) captured primed → differentiated (keratins, annexins); Factor 3 captured cellular detection rate (a technical covariate). Jointly, Factors 1 and 2 recovered a continuous differentiation trajectory, which clustering methods SNF and iCluster could not — they only separated subpopulations.
- **Limitations stated by the authors:** the model is linear and can miss strongly non-linear relationships; it lacks priors on feature relationships (pathways); zero-inflated (scRNA-seq) and binomial (splicing) likelihoods are not yet supported; and only point estimates of factors are used downstream.

## Methods / evidence

Generative-model simulations (M = 1–21 views, D = 100–10,000 features, K = 5–60 factors, 0–90% missing; 10 repeats per setting), a head-to-head simulation against GFA (K_true = 10, M = 3, N = 100, D = 5,000, 5% missing, one Gaussian/Bernoulli/Poisson view each), and two real applications: CLL data from Dietrich et al. 2018 (EGAS00001001746) and scM&T-seq data from Angermueller et al. 2016 (GSE74535). Downstream annotation uses variance decomposition (R² per factor per view), top-loading inspection and a parametric t-test gene-set enrichment (Reactome, BH FDR 1%). Software: R and Python implementation at github.com/bioFAM/MOFA, with the R package MOFAtools for annotation.

Weight: **high** as the defining description of the MOFA model, its priors and its stated limitations. The CLL biology (oxidative-stress factor, IGHV intermediate group) is hypothesis-generating, with partial orthogonal validation only for the IGHV outliers. The single-cell demonstration is small (87 cells, two modalities) and serves as a proof of concept rather than a single-cell-scale benchmark — scalability to large single-cell datasets is the gap MOFA+ later addresses ([[10-Summaries/argelaguet-2020-mofa-plus]]).

## Surprising or load-bearing bits

- The **R² variance-decomposition heat map** (factor × modality) is the defining MOFA output: it turns "is this signal shared across omics layers or private to one?" into a direct readout. This is what later work cites MOFA for. (synthesis)
- Missing assays are a core design target, not an afterthought: ~40% of CLL patients were incomplete, and MOFA can impute whole missing modalities from the shared factors.
- Methylation dominated the shared mESC factor (53–72% of variance) while RNA contributed only 7% to that same factor — the shared axis can be weak in one modality and still be detected because the model pools across views. (synthesis)
- Continuous factors recovered a differentiation trajectory that discrete multi-omics clustering (SNF, iCluster) could not.

## Entities mentioned

- [[oliver-stegle]] — co-corresponding last author (EMBL Heidelberg / EMBL-EBI affiliations listed).
- John C Marioni, Wolfgang Huber, Florian Buettner — co-authors (Huber and Buettner co-corresponding); no wiki entity pages.

## Concepts touched

- [[multimodal-integration-methods]] — founding paper of the factor-analysis / sample-space branch; contrasted against iCluster, GFA and SNF.
- [[dimensionality-reduction]] — a multi-view generalisation of PCA with sparse, interpretable loadings and automatic factor-number selection.
- [[imputation]] — imputes both individual values and whole missing assays via the shared factors.
- [[joint-single-cell-multi-omics]] — demonstrates coupled transcriptome–methylome variation in scM&T-seq data.

## Connections to other sources

- Successor: [[argelaguet-2020-mofa-plus]] adds stochastic variational inference and multi-group priors, addressing the scalability ceiling. Review by the same group: [[argelaguet-2021-integration-principles]], which frames MOFA as a CCA generalisation separating shared from modality-private variation — consistent with this paper's variance decomposition. (synthesis)
- Later application to scNMT-seq gastrulation data: [[argelaguet-2019-nature]]; scNMT-seq itself is cited as a single-cell multi-omics assay: [[clark-2018-scnmt-seq]], alongside G&T-seq [[macaulay-2015-gt-seq]].
- Later use with CUT&Tag + RNA: [[schwager-2026-onecell-cut-tag]] separates multiomic and epigenome-only factors, the same shared-vs-private logic. (synthesis)
- Contrasting integration families: [[welch-2019-liger]], [[hao-2021-seurat-wnn]], [[cao-2022-glue]], [[ashuach-2023-multivi]].

## Open questions

- The paper uses point estimates of factors downstream; how much would propagating posterior uncertainty change the CLL survival associations or outlier calls?
- Zero-inflated and binomial likelihoods were listed as future work — relevant for sparse single-cell methylation and accessibility data, where binary per-CpG calls are the norm. (synthesis)
- Factor 1's "intermediate" IGHV group: is it a biological continuum or a mixture artefact? The paper notes only "suggestive evidence" for a continuum.

## Related

- [[argelaguet-2020-mofa-plus]] · [[multimodal-integration-methods]] · [[dimensionality-reduction]] · [[imputation]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/computational-methods]]
