---
type: summary
title: "Cao 2022 — Multi-omics single-cell data integration and regulatory inference with graph-linked embedding (GLUE)"
source: "[[00-Sources/papers/Multi-omics single-cell data integration and regulatory inference with graph-linked embedding]]"
aliases: ["Cao 2022 GLUE", "GLUE", "graph-linked unified embedding"]
tags: [GLUE, multi-omics-integration, deep-learning, graph-VAE, unpaired-integration, Gao-lab, PKU]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Cao et al. (2022) — *Multi-omics single-cell data integration and regulatory inference with graph-linked embedding (GLUE)* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-022-01284-4)

Cao and Gao (Peking University) developed **GLUE** (Graph-Linked Unified Embedding), a deep-learning framework for integrating **unpaired** multi-omics single-cell data (scRNA-seq + scATAC-seq + snmC-seq3 / sci-MET, etc.) that have distinct feature spaces. The key idea: build a *knowledge-based guidance graph* whose vertices are features (genes, ATAC peaks, methylation regions) and whose edges represent known regulatory interactions (e.g., a peak overlapping a gene body links the peak vertex to the gene vertex with a positive edge).

Each modality is encoded by a modality-specific variational autoencoder; cell embeddings from all modalities are aligned in a shared latent space via adversarial discriminator training that prevents modality-specific clustering. The guidance graph is also embedded (via a graph-VAE), and the feature embeddings constrain how the data decoders reconstruct each modality.

Benchmarked on three gold-standard paired datasets (SNARE-seq, SHARE-seq, 10x Multiome) and two unpaired datasets (Nephron, MOp). GLUE achieved the lowest FOSCTTM metric (cell-level alignment error) — 3.6× / 1.7× / 1.5× lower than the second-best method on SNARE-seq, SHARE-seq, 10x Multiome. Robust to 90% corruption of the guidance graph; scales to millions of cells.

## Why this matters

Computational anchor for §4 multimodal integration alongside MOFA (linear factor), Seurat-WNN (graph), MultiVI (VAE-only without guidance graph), and Cobolt. GLUE is distinguished by **explicit prior knowledge incorporation** via the guidance graph — making it the natural choice when the regulatory relationships between modalities are partially known (peak-to-gene mappings, CpG-to-gene mappings). Especially relevant for our review's locus-state framework: cross-modality interpretation is *exactly* the regulatory-inference task GLUE targets.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-022-01284-4) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35501393/)

## Related

- [[10-Summaries/argelaguet-2019-mofa]]
- [[10-Summaries/ashuach-2023-multivi]]
- [[10-Summaries/stuart-2021-signac]]
- [[30-Concepts/multimodal-integration-methods]]
