---
type: summary
title: "Peng et al. 2026 — scDIAGRAM: detecting chromatin compartments from individual single-cell Hi-C matrix without imputation or reference features"
source: "[[00-Sources/papers/scDIAGRAM_ detecting chromatin compartments from individual single-cell Hi-C matrix without imputation or reference features]]"
source_quality: full
source_sha256: "c38c179b6c6870518a183d785193d4ff8ae16827befc2768846acc9cdae3d49a"
source_kind: paper
author: "Yongli Peng, Yujing Deng, Menghan Liu, Zhiyuan Liu, Ya-Hui Li, Xiang-Yu Zhao, Dong Xing, Jinzhu Jia, Hao Ge"
published: 2026-03-08
ingested: 2026-10-07
doi: "10.1093/bib/bbag096"
journal: "Briefings in Bioinformatics 27(2):bbag096"
tags: [scDIAGRAM, single-cell-Hi-C, A/B-compartments, change-point-detection, normalized-cut, graph-partitioning, MCMC, HiRES, AML, compartment-heterogeneity]
entities: []
concepts: ["[[30-Concepts/chromatin-compartments]]", "[[30-Concepts/single-cell-hi-c]]", "[[30-Concepts/imputation]]", "[[30-Concepts/hi-c-normalization]]", "[[30-Concepts/pseudo-bulk]]", "[[30-Concepts/cpg-island]]"]
topics: ["[[40-Topics/3d-genome]]", "[[40-Topics/chromatin-architecture]]", "[[40-Topics/computational-methods]]"]
---

**Citation:** Peng et al. (2026) — *scDIAGRAM: detecting chromatin compartments from individual single-cell Hi-C matrix without imputation or reference features* — *Briefings in Bioinformatics* 27(2):bbag096. [DOI](https://doi.org/10.1093/bib/bbag096)

# Peng 2026 — scDIAGRAM

> Existing single-cell compartment callers either borrow a reference feature (scA/B averages **CpG density** over Hi-C neighbours) or **impute** (scHiCluster within cell; Higashi/scGHOST across cells), and both can erase what is cell-specific. scDIAGRAM (single-cell compartments annotation by DIrect stAtistical modeling and GRAph coMmunity detection) works on **one cell's contact matrix alone**: a Bayesian **2D change-point model** (MCMC) segments the matrix into blocks, each segment becomes a graph node, and a **normalized cut** (spectral, second eigenvector) splits nodes into two compartments. CpG density is used only *afterwards* to decide which side is "A". The payoff the authors claim is preserved **cell-to-cell compartment heterogeneity** that tracks transcription.

## Key claims

- **Reference features leak into scA/B.** On a pseudo-bulk mouse-brain Ex1 matrix (chr7), scDIAGRAM matched cooltools PCA with 0.94 intersection / 0.84 Pearson versus 0.825 / 0.6 for scA/B. As downsampling deepens (1/400 to 1/3,200), **scA/B converges to the CpG signal** — a universal feature independent of the Hi-C data — while scDIAGRAM stays closer to bulk PCA, most visibly where CpG and bulk PCA disagree.
- **Imputation flattens heterogeneity.** On single-cell 3D imaging data downsampled to 250–10,000 contacts (chr2, 300 cells), scDIAGRAM beat scHiCluster on binary intersection (comparable on real-valued correlation) and outperformed scHiCluster, Higashi and scA/B on per-locus accuracy at 1,000 contacts (vs scHiCluster P = 7 × 10⁻⁸²). Its across-cell compartment variance was closer to the imaging ground truth, especially at variable loci; Higashi, which projects onto pseudo-bulk compartments, produced relatively homogeneous calls.
- **vs MaxComp** (distance-graph max-cut on imaging coordinates): broadly similar large-scale structure; MaxComp was more heterogeneous, scDIAGRAM closer to single-cell PCA — attributed to interaction- vs distance-based compartment definitions.
- **GM12878 (1 Mb)**: pooled scDIAGRAM compartments correlate 0.85 with bulk PCA (scA/B 0.6); A–A and B–B > A–B contacts; H3K36me3 separates A/B most strongly, H3K27me3 and H3K9me3 least. Variable loci are enriched for H3K27me3 (P = 6 × 10⁻⁵; Pearson 0.4 between compartment variance and H3K27me3).
- **Mouse brain (HiRES Hi-C + RNA)**: compartment variance shows a bimodal stable/variable split (scHiCluster shows high variance everywhere — "potential instability"); compartment sizes match bulk PCA better than scA/B or scHiCluster (which produce smaller domains). In Ex1 cells, ~60% of genes had a more active TSS compartment when transcribing (UMIs > 10) than when silent (UMIs < 1); variable-compartment regions show more transcriptional variability. *Erbb4* switches stable B → stable A from excitatory to inhibitory neurons with matching expression; *Npas3* shows a variable B → variable A switch. Validated on GAGE-seq (1,913 inhibitory-neuron markers mostly with elevated compartments).
- **Compsc-Ncut** (−log₂ of the optimal normalized-cut value) is proposed as a per-cell **compartment-strength** score; it decreases under matrix shuffling and tracks the expected cell-cycle trend where scA/B with a standard compartment score does not. Practical cutoff 17.3.
- **Embryos (HiRES, E7.0–E11.5, neural trajectory)**: compartment–expression correlation for stage markers is strong early (E7.0–7.5) and late (E9.5–E10+) but weak at E8.0–E8.5, consistent with ectoderm/mesoderm intermixing before E8.5. At *Efna5* (E8.0), scDIAGRAM follows bulk PCA while scA/B shows the opposite transition.
- **AML (new HiRES data, Peking University People's Hospital patients)**: AML and embryo datasets show significantly higher compartment variability than brain or GM12878. Between patients PT01 and PT03, RNA fold change of 70 marker genes correlated with compartment differences (Spearman r = 0.32, P = .003); *MPP7* shows a B→A switch with higher expression in PT01 — offered as a "novel biological prediction"; *CAMK1D* behaves similarly.

## Methods / evidence

Model: observed contacts Y = R × X with Bernoulli dropout R and Gaussian true counts X; parameters constant within each block between K change points; uniform prior over CP placements; Metropolis–Hastings sampling to approximate the MLE. CP detection on the raw matrix; graph partition on O/E-normalized data with expected values from a pseudo-bulk (BandNorm-inspired, cooltools). K chosen per dataset by stability (K from 10–200; stop when consecutive-K annotations correlate >0.8 and intersect >0.9); ~100 CPs at 100 kb, 20–40 at 1 Mb. Benchmarks: downsampled pseudo-bulk, FreeHi-C simulations, downsampled DNA-MERFISH-style imaging; comparators scA/B, scHiCluster+cooltools, Higashi (no neighbours), Hickit 3D models, MaxComp, scGHOST (subcompartments merged to A/B). Runtime comparable to scA/B and lower than other methods.

Weight: good on the specific failure modes (CpG leakage, imputation smoothing), where simulations give real ground truth. "Greater heterogeneity" is treated as better, which is only validated in the imaging simulation; in real data, extra variance could also be noise. Biological correlations (compartment ~ expression) are modest (e.g., 0.15–0.3 per chromosome for Ex1 vs astrocytes), and the AML findings rest on few patients.

## Surprising or load-bearing bits

- **At typical scHi-C depth, a CpG-guided caller mostly reports CpG density.** The paper shows this explicitly — a warning for any single-cell compartment result derived with scA/B. (synthesis)
- **Order matters: detect, then label.** Using CpG density only to orient the eigenvector keeps the reference out of the boundary calls; low |correlation| with CpG then flags cells with weak compartmentalization.
- **Heterogeneity tracks plasticity**: AML and embryonic cells vary more than neurons or a lymphoblastoid line — compartment variance as a candidate readout of chromatin plasticity. (synthesis)
- The approach is training-free and per-cell, contrasting with deep cross-cell models (Higashi, scGHOST) the authors call hard to interpret.

## Concepts touched

- [[chromatin-compartments]] — single-cell A/B calling without imputation; stable vs variable compartment loci; compartment strength per cell.
- [[single-cell-hi-c]] — dropout-aware block model for sparse matrices.
- [[imputation]] — argued to smooth away cell-specific variability (scHiCluster within cell; Higashi across neighbours).
- [[hi-c-normalization]] — pseudo-bulk expected for O/E in sparse cells (BandNorm-style).
- [[cpg-island]] — CpG density as post hoc A/B orientation, not as a feature.

## Connections to other sources

- Methods compared: [[tan-2018-science]] (Dip-C, source of scA/B and Hickit), [[zhou-2019-schicluster]], [[zhang-2022-higashi]], [[xiong-2024-scghost]].
- Normalization inspiration: [[zheng-2022-bandnorm-scvi-3d]]; tooling: [[abdennur-2020-cooler]].
- Compartments origin: [[lieberman-aiden-2009-hic]]; single-cell Hi-C assays: [[nagano-2013-nature]], [[ramani-2017-scihi-c]].
- Review context: [[hong-2025-sc3d-genome-review]], [[dautle-2025-schic-review]].
- Same senior-author group (Dong Xing) built single-cell WGA chemistry: [[xing-2021-meta-cs]] (synthesis).

## Open questions

- Is extra single-cell variance signal or noise in real data? Only the imaging simulation can tell, and it lacks scHi-C-specific biases.
- K is fixed per dataset; cells with very different contact numbers may want different K.
- Within-block constant parameters ignore distance decay inside blocks; authors propose distance, GC and mappability covariates as extensions.
- MPP7 in AML is a hypothesis from two-patient comparisons.

## Related

- [[chromatin-compartments]] · [[zhang-2022-higashi]] · [[tan-2018-science]] · [[40-Topics/3d-genome]]
