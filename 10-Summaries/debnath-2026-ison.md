---
type: summary
title: "Debnath & Duren 2026 — Inference of spatial chromatin accessibility via integration of spatial transcriptomics and single-cell multi-omics data (ISON)"
source: "[[00-Sources/papers/Inference of spatial chromatin accessibility via integration of spatial transcriptomics and single-cell multi-omics data]]"
source_kind: paper
author: "Ishita Debnath, Zhana Duren (corresponding)"
published: 2026-06-04
ingested: 2026-08-13
doi: "10.1038/s41467-026-73948-7"
journal: "Nature Communications 17 (2026)"
tags: [ISON, spatial-ATAC-inference, KL-NMF, contrastive-VAE, LINGER, gene-regulatory-network, TF-activity, Alzheimers, imputation]
entities: ["[[zhana-duren]]"]
concepts: ["[[spatial-multiomics]]", "[[multimodal-integration-methods]]", "[[gene-regulatory-network]]", "[[imputation]]", "[[cis-regulatory-element]]", "[[transcription-factor-motif]]", "[[dimensionality-reduction]]", "[[scatac-imputation]]", "[[alzheimers-disease]]"]
topics: ["[[single-cell-multiomics]]", "[[computational-methods]]", "[[single-cell-atac-seq]]"]
---

**Citation:** Debnath & Duren (2026) — *Inference of spatial chromatin accessibility via integration of spatial transcriptomics and single-cell multi-omics data* — *Nature Communications* 17. [DOI](https://doi.org/10.1038/s41467-026-73948-7)

# Debnath 2026 — ISON

> Spatial multiome kits do not exist commercially, but spatial transcriptomics kits and single-cell multiome kits both do. ISON exploits that asymmetry: learn a shared embedding from **ST + sc-multiome**, push spatial RNA through the multiome's ATAC decoder, and get **inferred spatial chromatin accessibility** — then run [[gene-regulatory-network|GRN]] inference on the result. The counterintuitive claim is that the *inferred* accessibility is **more biologically interpretable than the directly measured** spatial ATAC, because the measurement is so sparse.

## Key claims

- **Two model variants; the linear one wins.** A joint KL-NMF (Poisson likelihood, shared regulatory-program matrices across ST/scRNA/scATAC, Laplacian regularisation penalising abrupt program change between neighbouring spots, plus modality-specific correction vectors for batch effects) and a contrastive joint VAE (two VAEs, RNA–ATAC pairs from the same cell as positives). **KL-NMF consistently outperforms the VAE** — P21 peak-wise PCC 0.23 vs 0.09, P22 0.15 vs 0.07 — and is adopted as the default.
- **Beats every available baseline**, none of which was designed for this task: CCA+KNN, MOFA, Tangram, RCTD, SPAGE, GIMVI. Gene-imputation methods were adapted by treating peaks as "missing genes"; RCTD by multiplying deconvolved cell-type proportions by cell-type-average accessibility.
- **Raw peak-wise correlations are modest and the authors say so.** 0.23 (P21) and 0.15 (P22) against raw spatial ATAC, attributed to severe dropout and sparsity in the measurement. Against MAGIC-imputed spatial ATAC the same predictions reach **0.69 and 0.63**. Spot-wise PCC is much higher — 0.56 and 0.64 raw, >0.9 for more than 93% of spots in the cross-dataset test.
- **Prediction beats measurement on regulatory-signal recovery.** Correlating gene expression with peak accessibility across spots, the expected distance-dependent decay is followed closely by ISON predictions but only weakly by the *observed* accessibility. Validated against external references: for *cis*-eQTL links, ISON-predicted ATAC gives AUPR 6% above random while experimental ATAC performs at random; for Hi-C contacts, ISON gives 15% above random versus 10% for experimental. The interpretation offered is denoising, not magic — but it does mean the inferred track is the better substrate for downstream regulatory analysis.
- **Robust to low gene coverage.** Subsampling P22 spatial RNA to 100–1,000 genes (18–180 expressed per spot) kept average peak-wise PCC above 0.4 even at 100 genes — relevant because imaging-based ST platforms measure small gene panels.
- **Robust across spot resolutions.** scDesign3 simulations varying cells per spot: overall PCC 0.55–0.70 for ISON vs 0.44–0.54 for SPAGE, a 20–30% improvement, with lower RMSE throughout.
- **Cross-dataset generalisation works.** Treating P21 spatial multiome as if it were sc-multiome (discarding coordinates) and predicting P22 spatial ATAC gave peak-wise PCC 0.65 / RMSE 0.18 and spot-wise PCC 0.97 / RMSE 0.49 against MAGIC-imputed truth, with residuals centred near zero.
- **TF activity at spot level, distinguishing within-family TFs** — capability the authors identify as unique to ISON and unavailable to approaches using accessibility alone, since motif-based methods cannot separate paralogues sharing a motif.
- **Applied to Alzheimer's disease data, it recovers disease- and age-specific spatially variable gene regulatory modules.**
- **Error structure is characterised rather than hidden.** Peaks and spots with higher total counts show larger RMSE but higher PCC; low-count features show the reverse. Peaks with greater spatial variability (Moran's *I*) are predicted more accurately — the biologically interesting features are the ones the model gets right.

## Methods / evidence

Benchmarking on 10x Genomics Alzheimer's and wild-type mouse brain sc-multiome plus spatial ATAC-RNA-seq mouse brain (P21/P22), with train/test splits constructed by partitioning spots because no dataset pairs spatial multiome with sc-multiome from the same tissue. Simulation via scDesign3. External validation against *cis*-eQTL links and Hi-C contacts. GRN reconstruction via LINGER (the same group's prior tool).

Weight: the validation design is constrained by data availability and the authors are transparent about it — splitting one spatial multiome dataset into pseudo-sc-multiome and pseudo-spatial halves is a workaround, not an independent test. The cross-dataset P21→P22 experiment is the closest thing to a genuine held-out evaluation.

## Surprising or load-bearing bits

- **"Our predicted accessibility recovers regulatory signal better than the measured accessibility"** is the paper's boldest claim and it is supported by two orthogonal external references (eQTL and Hi-C) rather than by internal metrics. If it holds, it inverts the usual assumption that measurement beats inference — at least in a sparsity regime this severe.
- **Linear beats deep, consistently.** The KL-NMF model outperforms the contrastive VAE across both datasets and both metrics. In a literature that defaults to deep generative models for integration ([[ashuach-2023-multivi|MultiVI]], [[cao-2022-glue|GLUE]], [[gong-2021-cobolt|Cobolt]]), this is a useful counterexample — and the Laplacian spatial-smoothness prior is probably doing work that a VAE has to learn from scratch.
- **Distinguishing TFs within a family** is a genuine capability gap in accessibility-only methods: [[schep-2017-chromvar|chromVAR]] and its successors score motifs, and paralogous TFs share motifs. Bringing expression into the same latent space breaks the tie.
- **Peak-wise vs spot-wise PCC differ enormously** (0.23 vs 0.56 on the same predictions) because they ask different questions — does this peak vary correctly across space, versus does this spot have the right accessibility profile. Reporting both is honest and rare.
- **The whole method is a bet against the hardware roadmap.** ISON exists because spatial multiome kits are unavailable; if [[cardilla-2025-spatial-methylome]]-style spatial epigenome assays commercialise, the motivation weakens. The authors frame it as broadening access rather than as a permanent substitute.
- Read against [[argelaguet-2021-integration-principles]]'s taxonomy, ISON is a **diagonal integration with a spatial anchor** — different modalities, different cells, bridged by a shared latent space and constrained by physical adjacency.

## Entities mentioned

- [[zhana-duren]] — corresponding author; also LINGER (GRN inference from sc-multiome).

## Concepts touched

- [[spatial-multiomics]] — computational substitution for a missing assay.
- [[multimodal-integration-methods]] — a linear NMF-based route that beats deep generative baselines here.
- [[gene-regulatory-network]] — spatially resolved GRNs as the downstream product.

## Connections to other sources

- Integration taxonomy this fits into: [[argelaguet-2021-integration-principles]]; method families in [[multimodal-integration-methods]].
- Deep generative comparators from the corpus: [[ashuach-2023-multivi]], [[cao-2022-glue]], [[gong-2021-cobolt]]; matrix-factorisation ancestor [[argelaguet-2020-mofa-plus]] (MOFA is a direct baseline here); anchor-based [[stuart-2021-natmethods]], [[hao-2024-seurat-v5]].
- Benchmarking context: [[xiao-2024-multiomics-benchmark]].
- Spatial assays it substitutes for or complements: [[zhao-2022-nature]] (slide-DNA-seq), [[cardilla-2025-spatial-methylome]], [[mo-2023-stam-seq]], [[10-Summaries/zhao-2022-nature]], [[vandereyken-2023-spatial-multiomics]].
- Accessibility-only TF-activity methods it improves on: [[schep-2017-chromvar]], [[bravo-2019-cistopic]], [[yuan-2022-scbasset]].
- GRN inference from multiome: [[bravo-2023-scenicplus]], [[kamimoto-2023-celloracle]], [[pliner-2018-cicero]].
- Alzheimer's context: [[miller-2022-nature]], [[kousi-2022-ad-mosaicism]].
- scATAC imputation and sparsity: [[scatac-imputation]], [[li-2021-scopen]], [[xiong-2019-scale]].

## Open questions

- **No dataset pairs spatial multiome with sc-multiome from the same tissue**, so every benchmark here is a split of one dataset or a cross-timepoint transfer. A genuine independent evaluation awaits such data.
- Absolute peak-wise PCC against *raw* measurement remains low (0.15–0.23); the strong numbers all use MAGIC-imputed ground truth, which risks circularity — both prediction and "truth" are smoothed.
- Predicted values systematically underestimate observed accessibility magnitude, preserving rank but not scale.
- Whether "inference beats measurement" survives on a less sparse spatial ATAC platform is the decisive untested question.

## Related

- [[argelaguet-2021-integration-principles]] · [[spatial-multiomics]] · [[multimodal-integration-methods]] · [[40-Topics/single-cell-multiomics]]
