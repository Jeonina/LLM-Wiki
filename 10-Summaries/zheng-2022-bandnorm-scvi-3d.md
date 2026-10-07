---
type: summary
title: "Zheng, Shen & Keleş 2022 — Normalization and de-noising of single-cell Hi-C data with BandNorm and scVI-3D"
source: "[[00-Sources/papers/Normalization and de-noising of single-cell Hi-C data with BandNorm and scVI-3D]]"
source_quality: full
source_sha256: "52a635554956d594011f9c4abfcec3a770cf6f6577fd875351335e89dca04fc1"
source_kind: paper
author: "Ye Zheng, Siqi Shen, Sündüz Keleş (corresponding)"
published: 2022-10-17
ingested: 2026-10-07
doi: "10.1186/s13059-022-02774-z"
journal: "Genome Biology 23:222"
tags: [BandNorm, scVI-3D, scGAD, scHi-C, normalization, band-transformation, genomic-distance-bias, ZINB, variational-autoencoder, benchmark, Higashi, scHiCluster, scHiC-Topics, Harmony, Dip-C, Keles-lab]
entities: ["[[sunduz-keles]]"]
concepts: ["[[single-cell-hi-c]]", "[[hi-c-normalization]]", "[[imputation]]", "[[batch-effect]]", "[[dimensionality-reduction]]", "[[clustering-algorithms]]", "[[topologically-associating-domain]]", "[[chromatin-compartments]]", "[[dip-c]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]"]
---

**Citation:** Zheng, Shen & Keleş (2022) — *Normalization and de-noising of single-cell Hi-C data with BandNorm and scVI-3D* — *Genome Biology* 23:222. [DOI](https://doi.org/10.1186/s13059-022-02774-z)

# Zheng 2022 — BandNorm and scVI-3D

> The dominant bias in a single-cell contact matrix is **genomic distance** ("band bias"), so normalize band by band. BandNorm does the simplest possible version — divide each diagonal band in a cell by that cell's band total, then multiply back the across-cell average band total — and in a four-dataset benchmark it matches or beats elaborate imputation models for clustering, TAD recovery and significant-interaction recovery, in ~15 minutes. scVI-3D is the opposite end: a per-band zero-inflated negative binomial VAE (built on scvi-tools) that models depth, batch and dropout, and wins where BandNorm loses — **rare cell types and high sparsity**. The practical recipe is BandNorm first, scVI-3D once rare populations appear. A third contribution, scGAD (single-cell gene-associating-domain scores), reads gene-level structure out of normalized maps and recovers transcriptome-validated marker genes.

## Key claims

- **BandNorm formula**: C = (Y / L^{cv}) · α(v), where L^{cv} is cell *c*'s total in band *v* and α(v) the mean band total across cells. Removing within-cell distance bias and depth, then **adding back a common contact-decay curve**, is what lifts BandNorm above BandScale (the same without the add-back); the authors interpret this as up-weighting short-range bands, which carry most cell-type signal.
- **Eight methods benchmarked** — CellScale, BandScale, BandNorm, CellScale+CNN, scHiCluster, scHiC Topics, Higashi, scVI-3D — on *Ramani2017*, *Kim2020*, *Lee2019* and *Li2019*, scored by ARI (K-means, Louvain) and Silhouette (UMAP/t-SNE) in six settings. Median ranks: **BandNorm 2, scVI-3D 3, Higashi 3.5, scHiCluster 4**.
- **Dataset difficulty dominates**: almost all methods fail on *Li2019* (fewest cells; ARI 0.005–0.47); all but CellScale do best on *Kim2020* (ARI 0.35–0.91), where BandNorm, scVI-3D and scHiC Topics lead.
- **Brain sub-types**: in *Lee2019* (14 prefrontal-cortex cell types, 2 donors, 5 libraries), BandNorm, scHiCluster and Higashi separate excitatory from inhibitory neurons — which the original analysis reported scHi-C alone could barely do — and scVI-3D does so at 1 Mb and further refines sub-types at 100 kb. A single-library, batch-free subset reproduces this, so the gain is not just batch correction.
- **Competitor failure modes diagnosed**: scHiCluster's default filter (>5,000 off-diagonal contacts) would remove up to **88.4%** of *Kim2020* cells, and without it scHiCluster mixes low-depth cells; Higashi's low-depth problem is worse on *Kim2020*. Higashi produces blurry aggregate maps and **recurrent over-enriched off-diagonal blocks across all five cell types**, attributed to over-imputation from outlier cells; scHiCluster's maps are smoother still. Both inflate IMR90's similarity to other cell types relative to bulk, because neighbour-borrowing homogenizes poorly separated cells (IMR90 co-clusters with HFF).
- **Downstream fidelity versus bulk Hi-C** (*Kim2020*, true labels): median TAD-boundary recovery for GM12878 **85.71% (BandNorm), 66.67% (scVI-3D), 60% (Higashi), 60.87% (scHiCluster)**; HiCRep similarity to bulk highest for BandNorm, then scVI-3D and Higashi. Top-5,000 interacting pairs recovered against a Fit-Hi-C bulk gold standard (top 50,000) for GM12878: **93.34%, 86.32%, 63.66%, 69.26%** respectively — BandNorm leads in every cell line except IMR90 (<100 cells), where scVI-3D's zero-inflation and imputation keep accuracy high. Differential-interaction detection (TADcompare, diffHic, CHESS) is similar across all four.
- **Batch handling**: for BandNorm, Harmony beat SVA (which worsened results), removing the batch-correlated PC, and Seurat regression (which introduced new biases); Harmony was therefore applied to all methods lacking built-in correction. Afterward only scHiC Topics remained slightly batch-affected (iLISI, ARI).
- **Residual depth/sparsity effects** persist in UMAP/t-SNE of BandScale, scHiCluster, scHiC Topics, Higashi, CellScale+CNN and scVI-3D, but shape within-cluster layout rather than cluster separation; regressing out correlated PCs did not help and sometimes hurt.
- **scGAD**: GAD scores (within-gene contact relative to flanking regions, adapted from bulk tagHi-C) computed on BandNorm-normalized *Tan2021* Dip-C at 100 kb are higher for MALBAC-DT-defined marker genes, overlap significantly with transcriptome markers (Fisher's exact test), and flag markers whose expression is low or non-specific (e.g., *Agmo*, *Dock8*, *Entpd1* in microglia; *Ano4*, *Pde4b*, *Usp6nl* in mature oligodendrocytes, the latter supported by Allen Brain Atlas data).
- **Novel neonatal-neuron sub-clusters**: BandNorm yields a split (neuron I/II) not explained by tissue, age, sex or depth; 50 transcriptome marker genes have differential scGAD scores between the new sub-clusters versus none for the original Tan et al. split (which tracked age: 78.78% day-1, 68.8% day-7).
- **Runtime**: BandNorm ~15 min with little memory versus hours to more than a day for others (Table 2).

## Methods / evidence

Data binned at 1 Mb (chr1–22 + X; *Lee2019* also at 100 kb), diagonal excluded, cells with fewer than *x*/6 non-zero pairs per chromosome removed (*x* = chromosome size in Mb); at 100 kb cells >99.9% sparse excluded. scVI-3D fits each chromosome × band matrix separately with latent dimension 100 (the paper argues the 10–50 used in scRNA/scATAC is inadequate), uses multiHiCcompare-style progressive band pooling (best of five pooling strategies tested), filters cells with zero contacts in a band and imputes their embeddings as 0. A mixed model on *Lee2019* found a significant library-size × band interaction (BIC-preferred), motivating a merged cell-and-band size factor *d_cv*. Gold standards: bulk in situ Hi-C (GM12878, IMR90 from GSE63525; HAP1; 4DN H1ESC, HFF). Benchmarks repeated with unsupervised-cluster labels with the same conclusions.

Weight: a well-controlled benchmark by method developers who also designed the baselines; competitor versions are pinned by commit. All headline comparisons are at 1 Mb, a resolution at which CNN and spatial-dependence modelling are disadvantaged (acknowledged). Gold standard is aggregate bulk Hi-C, which rewards methods that preserve population structure, not single-cell variability. (synthesis)

## Surprising or load-bearing bits

- **The simplest method wins most comparisons.** A two-line scaling beats hypergraph neural networks and random-walk imputation on clustering stability and on bulk concordance; imputation earns its keep only under extreme sparsity or rarity. (synthesis)
- **Imputation can manufacture structure**: Higashi's recurring off-diagonal enrichments and the cross-cell-type homogenization of IMR90 are concrete, visualized cases of neighbour-borrowing artefacts — the risk the wiki's [[imputation]] page flags in the abstract. (synthesis)
- **Latent dimension 100**, not 10–50, is the recommended default for scHi-C — a transferable parameter fact.
- **Band-wise independence is assumed** in scVI-3D (no spatial dependence between adjacent locus pairs), justified at 200 kb–1 Mb but not at ≤10 kb.
- scGAD is restricted to protein-coding genes ≥100 kb because of resolution.

## Concepts touched

- [[hi-c-normalization]] — extends distance-stratified normalization to single cells; contrasts with marginal balancing (ICE).
- [[imputation]] — quantified failure modes of neighbour-based imputation in scHi-C; ZINB-VAE as an alternative.
- [[batch-effect]] — Harmony best of four correction strategies for scaled scHi-C.
- [[topologically-associating-domain]] / [[chromatin-compartments]] — recovery from aggregated single-cell maps as an evaluation axis.
- [[single-cell-hi-c]] · [[dimensionality-reduction]] · [[clustering-algorithms]] · [[dip-c]]

## Connections to other sources

- Benchmarked competitors: [[zhou-2019-schicluster]] (scHiCluster), [[zhang-2022-higashi]] (Higashi). This paper disputes Higashi's advantage on low-depth cells and documents over-imputation artefacts — a counterpoint to the Higashi summary's imaging-based validation.
- Benchmark datasets: [[ramani-2017-scihi-c]] (*Ramani2017*), [[lee-2019-natmethods]] (*Lee2019*, sn-m3C-seq); *Tan2021* uses Dip-C ([[tan-2018-science]] for the assay).
- Batch correction: [[korsunsky-2019-harmony]].
- Same lab, later: [[park-2026-mintsc]] (MINTsC, also distance-band modelling of scHi-C). Downstream consumers of imputed maps: [[yu-2021-snaphic]], [[xiong-2024-scghost]].
- Bulk normalization background: [[servant-2015-hicpro]], [[lieberman-aiden-2009-hic]].

## Open questions

- Does BandNorm's lead survive at kilobase resolution, where sparsity favours imputation and spatial dependence matters?
- Bulk-concordance metrics cannot reward true cell-to-cell structural variability; an imaging ground truth (as in Higashi) might rank methods differently. (synthesis)
- scGAD's background model ignores gene density; the authors expect to remove the 100 kb length limit only with higher-resolution data.

## Related

- [[single-cell-hi-c]] · [[hi-c-normalization]] · [[imputation]] · [[zhang-2022-higashi]] · [[zhou-2019-schicluster]] · [[sunduz-keles]] · [[40-Topics/3d-genome]]
