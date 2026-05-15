---
type: summary
title: "Danese et al. 2021 — EpiScanpy: unified scATAC-seq and scBS-seq in the scanpy framework"
source: "[[00-Sources/papers/EpiScanpy_ integrated single-cell epigenomic analysis]]"
source_kind: paper
author: "Anna Danese, Maria L. Richter, Kridsadakorn Chaichoompu, David S. Fischer, Fabian J. Theis, Maria Colomé-Tatché (corresponding)"
published: 2021-09-01
ingested: 2026-05-12
doi: "10.1038/s41467-021-25131-3"
journal: "Nature Communications"
tags: [scATAC-seq, scBS-seq, scanpy, Python, software, atlas-integration, Theis-lab]
entities:
  - "[[20-Entities/fabian-theis]]"
  - "[[20-Entities/maria-colome-tatche]]"
  - "[[20-Entities/anna-danese]]"
concepts:
  - "[[30-Concepts/episcanpy]]"
  - "[[30-Concepts/scanpy]]"
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/scbs-seq]]"
  - "[[30-Concepts/anndata]]"
  - "[[30-Concepts/chromatin-accessibility]]"
topics:
  - "[[40-Topics/single-cell-atac-seq]]"
  - "[[40-Topics/dna-methylation]]"
  - "[[40-Topics/single-cell-multiomics]]"
---

**Citation:** Danese et al. (2021) — *EpiScanpy: unified scATAC-seq and scBS-seq in the scanpy framework* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-021-25131-3)

# Danese et al. 2021 — EpiScanpy

> Thesis: Single-cell transcriptomics has the mature scanpy framework (clustering, manifold learning, trajectory inference, dataset integration). Single-cell epigenomics has scattered specialized tools but no unified Python framework. **EpiScanpy** ports the scanpy machinery to scATAC-seq and single-cell DNA methylation, generating AnnData objects with flexible feature spaces (peaks, windows, genes, promoters, enhancers, methylation calls), and benchmarks at or near the top of scATAC-seq cell-clustering accuracy.

## Key claims

- **Feature engineering**: count matrices over any genomic feature (peaks, windows, promoters, enhancers, custom .bed). For methylation, β-value per feature using only CpGs/CHs with coverage; explicit handling of "not observed" vs "not methylated."
- **Methylation feature spaces matter**: in prefrontal cortex neurons (Luo 2017 snmC-seq, 3,377 cells, 4.7% coverage), enhancer-level CpG methylation gives the cleanest cell-type separation (silhouette 0.41 vs 0.32 windows / 0.28 promoters / 0.09 gene bodies). **DNA methylation at non-genic regulatory elements is the strongest determinant of cell identity** in adult neurons.
- **scanpy ecosystem**: tSNE, UMAP, Louvain clustering, PAGA, diffusion pseudotime, BBKNN batch correction. Differential methylation/accessibility testing built in. Feature-to-gene assignment for cell-type annotation.
- **Atlas integration**: BBKNN-based joint embedding of multiple datasets (10X PBMC + Satpathy 63k blood cells; mouse brain across platforms).
- **Benchmark**: among 11 scATAC-seq methods using Chen et al. 2019 framework, EpiScanpy consistently in the top tier; only cisTopic outperforms on a single dataset; **most robust across datasets**.
- **Scalability**: 81k mouse atlas cells in 18 minutes / 14 GB RAM. Outperforms R-based cisTopic on memory; runtime comparable on small data, much better on large.

## Methods / evidence

Python package on top of scanpy / AnnData. Datasets: Luo 2017 brain snmC-seq, 10X PBMC scATAC, Satpathy blood scATAC, Cusanovich mouse atlas. Benchmarking framework from Chen et al. 2019.

## Surprising or load-bearing bits

- The **enhancer-methylation > gene-body-methylation** finding in adult neurons is a real biological insight, not just a method demonstration. It validates the focus of single-cell methylomics on intergenic regulatory elements.
- Building epigenomics on scanpy/AnnData is the right architectural choice: it gives EpiScanpy free access to the entire scanpy machine-learning toolbox and prepares the ground for multi-omics integration.

## Connections to other sources

- Direct comparison/competition with [[10-Summaries/cistopic-cis-regulatory-topic-modeling-on-single-cell-atac-seq-data]] (R, LDA-based) and [[10-Summaries/comprehensive-analysis-of-single-cell-atac-seq-data-with-snapatac]] (R, peak-free).
- Provides TF-motif interpretation via [[10-Summaries/chromvar-inferring-transcription-factor-associated-accessibility-from-single-cell-epigenomic-data]] (chromVAR).
- Conceptually adjacent to [[10-Summaries/unsupervised-clustering-and-epigenetic-classification-of-single-cells]] (scABC) but Python-based and more general.

## Open questions

- The Python-vs-R divide in single-cell epigenomics remains (R has cisTopic, Signac, ArchR; Python has EpiScanpy, snapATAC2). Cross-language interop is still imperfect.
- Methylation-specific imputation algorithms are not central to EpiScanpy; specialized methods (DeepCpG, Melissa) outperform on imputation tasks.

---
**Source:** [DOI](https://doi.org/10.1038/s41467-021-25131-3)
## Related

- [[40-Topics/single-cell-atac-seq]] · [[40-Topics/dna-methylation]] · [[30-Concepts/episcanpy]] · [[30-Concepts/scanpy]] · [[20-Entities/fabian-theis]]
