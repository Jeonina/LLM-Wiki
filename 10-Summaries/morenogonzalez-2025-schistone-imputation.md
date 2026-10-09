---
type: summary
title: "Moreno-González et al. 2025 — A computational framework to dissect imputation strategies for single-cell histone modification data"
source: "[[00-Sources/papers/A computational framework to dissect imputation strategies for single-cell histone modification data]]"
source_quality: full
source_sha256: "9eaa438813868b52755be79e06db421fa3a6164c4202d8f19b9ff9344ce229df"
source_kind: paper
author: "Marta Moreno-González, Jeroen de Ridder, Jop Kind, Robin H. van der Weide (corresponding author not marked in clipping)"
published: 2025-12-29
ingested: 2026-10-09
doi: "10.1093/nargab/lqaf192"
journal: "NAR Genomics and Bioinformatics 7(4):lqaf192"
tags: [SCIBED, scHPTM, imputation, benchmark, sortChIC, scCUT&Tag, H3K4me3, H3K4me1, H3K27me3, H3K9me3, H3K27ac, H3K36me3, SIMIC, SiP, scImpute, scOpen, SCALE, SCALEX, cisTopic, MAGIC, in-silico-simulation, mouse]
entities: []
concepts: ["[[imputation]]", "[[single-cell-foundation-model]]", "[[cut-and-tag]]", "[[sortchic]]", "[[scatac-imputation]]", "[[scopen]]", "[[scale]]", "[[cistopic]]", "[[pseudo-bulk]]", "[[clustering-algorithms]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[40-Topics/histone-modifications]]", "[[40-Topics/sequence-models-and-foundation-models]]", "[[computational-methods]]", "[[single-cell-atac-seq]]"]
---

**Citation:** Moreno-González et al. (2025) — *A computational framework to dissect imputation strategies for single-cell histone modification data* — *NAR Genomics and Bioinformatics* 7(4):lqaf192. [DOI](https://doi.org/10.1093/nargab/lqaf192)

# Moreno-González 2025 — scHPTM imputation benchmark (SCIBED)

> **Version note:** the source is the full published article clipped from the OUP site, with Methods, Results, Discussion, figure captions and references. Equations (1)–(10) and all supplementary figures and tables are links or images and are not in the text.
>
> No imputation method has been built for single-cell histone PTM (scHPTM) data, so the authors ask whether scRNA-seq and scATAC-seq imputers transfer. They test 10 methods (SAVER, scImpute, kNN-smoothing, MAGIC, ALRA, scOpen, DCA, SCALE, SCALEX and cisTopic-impute) from five families: statistical models, smoothing, matrix factorisation, autoencoders and topic models. The data are **in silico datasets built from mouse bone-marrow sortChIC** (H3K4me1, H3K4me3, H3K9me3, H3K27me3) at 3 read depths × 10 noise levels, plus **real mouse-brain scCUT&Tag** (H3K4me3, H3K27ac, H3K27me3, H3K36me3). Methods are scored on three tasks: correlation to a pseudobulk ground truth, cell–cell similarity (a new metric, SIMIC) and signal in peaks (SiP). The answer is that **no method does all three**: scImpute is best for signal enrichment, scOpen and SCALEX for clustering, and scATAC-derived methods do best on narrow-peak marks. **No method in the benchmark is pretrained, uses DNA sequence, uses neighbouring bins or combines marks.** The authors list these as the missing pieces.

## Key claims

- **First imputation benchmark for scHPTM data.** The authors say imputation algorithms "are yet to be applied to scHPTM data" and that, to their knowledge, no cross-modality imputation method has been developed for it.
- **Depth dominates, noise second.** On in silico H3K4me3, most methods improved the overall score over non-imputed data at all depths and noise levels. Read depth was the main determinant of performance, and noise had a secondary effect.
- **Top overall on H3K4me3: SCALE, MAGIC, cisTopic** (first, second, third). No computational family beat the others on overall rank (Kruskal–Wallis P = 0.72). Methods built for scATAC did better than those built for scRNA (Wilcoxon signed-rank P < 0.05).
- **Narrow vs broad marks.** scATAC-based methods beat scRNA-based ones on H3K4me1 (P < 0.05). The effect was marginal for H3K27me3, which has narrow peaks and broad domains (P < 0.1), and absent for broad H3K9me3. Kruskal–Wallis P values for family differences were 0.72, 0.92 and 0.44 for H3K4me1, H3K9me3 and H3K27me3. The authors explain this with matrix structure: narrow-peak marks binned near peak width give sparse, ATAC-like matrices, while broad domains split into many correlated bins that neither ATAC nor RNA methods expect.
- **Imputation cannot rescue poor data.** SIMIC gains on H3K4me3 appeared mainly at mid depth (1,000 reads per cell) and dropped sharply at low depth or high noise. scOpen and ALRA lowered correlation to ground truth in high-depth, low-noise data, so imputing good data can make it worse.
- **Task-specific winners.** On H3K4me3 at mid depth and no added noise, SiP rose to about 0.80 with scImpute (k = 14) and about 0.67 with cisTopic, against 0.67 without imputation. scOpen led on cell–cell similarity across all four marks, beaten only by ALRA on H3K4me1 and H3K27me3. H3K9me3 imputation did worst on cell–cell similarity for all other methods.
- **Imputation bias by cluster size.** Most methods lowered SiP for large clusters and raised it for small ones. In a balanced simulation (89 cells per type), the size effect persisted for SAVER, scImpute, cisTopic and SCALEX.
- **Real scCUT&Tag: signal and clustering split.** On Bartosovic 2021 mouse brain (downsampled to about 1,000 reads per cell, 10-kb bins), KNN and scImpute kept H3K27me3 pseudobulk correlation with raw data high (0.86, 0.88), while SCALE, scOpen and cisTopic were lower (0.77, 0.76, 0.68). Only scImpute raised H3K4me3 enrichment over neuronal ChIP-seq peaks and lowered inter-cluster signal. Relative log2 SIMIC gains were SCALE 0.40 ± 0.19, SCALEX 0.44 ± 0.16, scOpen 0.44 ± 0.16, cisTopic 0.40 ± 0.17, KNN 0.38 ± 0.13 and scImpute 0.26 ± 0.18. cisTopic, SCALE, SCALEX and scOpen spread *Mbp* signal into non-oligodendrocyte clusters. "None of the applied methods were able to improve both signal and clustering."
- **Practical recipe (decision tree, Fig. 8).** If cell types are known in advance (screens, multimodal readouts), impute for signal enrichment (scImpute). Otherwise use scOpen or SCALEX to cluster, then build pseudobulks from the non-imputed data.

## Methods / evidence

**Data.** sortChIC mouse bone marrow from Zeller et al. 2023 (newer batch obtained by correspondence); filtered at ≥500 reads per cell (H3K4me1, H3K4me3) or ≥1,000 (H3K9me3, H3K27me3), and cells with unusually low zero fractions removed. 14 cell-type labels give pseudobulk ground truth. Simulation: expand pseudobulks to 50-kb genome-wide bins, add uniform noise at level l = 0–5 (plus l = 10 and 50 for H3K4me3 only, excluded from ranking), then downsample with Seurat SampleUMI to 10,000, 1,000 or 100 reads per cell. That gives 30 datasets per mark. scCUT&Tag mouse brain from GSE163532 (Bartosovic 2021), 9 clusters.

**Methods run** on an HPC node with a 30 GB / 48 h cap; failures scored 0. SAVER failed at low depth and completed only about 25% of high-depth runs; ALRA failed on very sparse data at the SVD step. scImpute was run with K = 4, 8 and 14 (13 for H3K9me3), kNN-smoothing with k = 3, 7, 15, SCALEX in RNA and ATAC modes, and cisTopic with 5–50 topics chosen by perplexity.

**Metrics.** (1) Per-cell Pearson correlation to the matched cell-type pseudobulk, median over cells. (2) SiP, the share of signal in hiddenDomains peak bins. (3) SIMIC: mean cell-type similarity of each cell's 10 nearest neighbours (top 5% variable bins, 1 − Pearson distance), divided by the expected similarity from abundance-weighted cosine similarity of pseudobulks. All metrics are computed on count matrices without dimensionality reduction or feature selection. Scores are min-max scaled per scenario, averaged across the three tasks and ranked by median, following Luecken et al. 2022. Released as the R package SCIBED (github.com/KindLab/SCIBED); simulated data on Zenodo (10.5281/zenodo.14205078).

Weight: a careful, transparent benchmark, but the ground truth is a simulation from one dataset with uniform noise, and the real-data check covers only the top methods on one scCUT&Tag dataset. (synthesis)

## Limitations

**Authors' own:**
- The noise model is uniform genome-wide noise. Much real scHPTM noise is open-chromatin bias, which is cell type-specific and hard to separate from true signal; uniform noise models only the non-cell-specific part.
- Variable performance makes it hard to recommend one method; the best choice depends on data and task, and imputed data should not be presented as conclusive.
- Current methods are not designed for scHPTM structure: no method uses neighbouring genomic bins, few use prior cell-type information (only scImpute does), and none integrates multiple marks or modalities.
- Some methods also do dimensionality reduction and clustering, but the authors scored raw or depth-normalised imputed matrices only, so method-specific embeddings were not assessed.

**Reviewer notes:**
- The method panel is 2015–2021-era scRNA/scATAC tools. No deep generative scHPTM-specific model, no sequence-aware model and no pretrained or foundation model was tested, so the benchmark measures transfer of borrowed tools, not the ceiling. (synthesis)
- The *Gbe1* and *Ebf1* loci are swapped between the Results text and the Fig. 6 caption, and the text calls *Gbe1* a B-cell fate transcription factor, which fits *Ebf1*. The locus-level claims in that paragraph should be read with care. (synthesis)
- Only mouse data, two protocols (sortChIC with MNase, scCUT&Tag with Tn5) and 50-kb or 10-kb bins. Human data, multi-mark single-cell assays and finer bins are untested. (synthesis)

## Surprising or load-bearing bits

- **The evidence for the histone foundation-model gap.** In a 2025 benchmark of scHPTM imputation, every method is a non-pretrained scRNA/scATAC tool, and the authors' wish list (use neighbouring bins, use cell-type priors, integrate marks) is exactly what a pretrained single-cell histone model would provide. (synthesis)
- **scATAC tools transfer only to narrow marks.** The narrow-vs-broad split is the concrete reason scATAC foundation models cannot simply be reused for H3K27me3 or H3K9me3. (synthesis)
- **Imputation can hurt.** On high-quality data, scOpen and ALRA lowered fidelity, and several methods erased cell-type specificity at *Mbp*. Imputed scHPTM tracks are not a safe substitute for raw data.
- **SIMIC** is a clustering metric that needs no dimensionality reduction or clustering parameters, comparable to scGraph.

## Concepts touched

- [[imputation]] — first systematic test of imputation on scHPTM data; task-dependent winners.
- [[single-cell-foundation-model]] — none exists for scHPTM; the authors' listed needs map onto what one would supply. (synthesis)
- [[cut-and-tag]] / [[sortchic]] — the two scHPTM protocols benchmarked.
- [[scatac-imputation]] — scATAC imputers (scOpen, SCALE, cisTopic) transfer best to narrow-peak marks.
- [[scopen]] / [[scale]] / [[cistopic]] — best for clustering (scOpen, SCALEX) and top overall on H3K4me3 (SCALE, cisTopic).
- [[pseudo-bulk]] — pseudobulks serve as ground truth, and the recommended workflow builds pseudobulks from non-imputed data after clustering.
- [[clustering-algorithms]] — SIMIC and KNN-based cluster prediction as evaluation.
- [[sequencing-depth-and-coverage]] — depth per cell is the main determinant of imputation performance.

## Connections to other sources

- Complements [[raimundo-2023-schptm-benchmark]], which benchmarked scHPTM processing pipelines (binning, embedding, feature selection); both find that scATAC habits transfer only partly and that feature selection hurts scHPTM. (synthesis)
- The real-data test uses [[bartosovic-2021-sccut-tag]]; the sortChIC data come from the Zeller/Yeung line of work ([[yeung-2023-scchix-seq]] is the companion multi-mark deconvolution method). (synthesis)
- The open-chromatin bias the authors leave out of their noise model is what [[hu-2026-patty]] corrects. (synthesis)
- [[wu-2026-sccut-tag-review]] makes the same argument that scCUT&Tag analysis inherits scATAC tooling that breaks for broad marks. (synthesis)
- Parallel imputation benchmark for single-cell methylation: [[liang-2026-scmeth-imputation-benchmark]]. (synthesis)
- Methods tested: [[li-2021-scopen]], [[xiong-2019-scale]], [[bravo-2019-cistopic]].
- Bulk counterpart: [[foroozandeh-2025-candi]] does self-supervised multi-assay imputation including histone marks, but only on bulk ENCODE data. (synthesis)

## Open questions

- Would a neighbouring-bin model (the authors suggest a hypergraph, as in scHi-C imputation) or a pretrained model across many scHPTM datasets beat scImpute and scOpen on both tasks at once? (synthesis)
- How do rankings change with a realistic open-chromatin noise model instead of uniform noise?
- Can multi-mark single-cell data (scChIX-seq, multi-CUT&Tag) support cross-mark imputation, as the authors propose?

## Related

- [[imputation]] · [[40-Topics/histone-modifications]] · [[40-Topics/sequence-models-and-foundation-models]] · [[single-cell-foundation-model]] · [[raimundo-2023-schptm-benchmark]] · [[cut-and-tag]] · [[foroozandeh-2025-candi]]
