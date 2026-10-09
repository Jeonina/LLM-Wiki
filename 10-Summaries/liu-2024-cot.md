---
type: summary
title: "Liu et al. 2024 — CoT: a transformer-based method for inferring tumor clonal copy number substructure from scDNA-seq data"
source: "[[00-Sources/papers/CoT_ a transformer-based method for inferring tumor clonal copy number substructure from scDNA-seq data]]"
source_quality: full
source_sha256: "b2910250e39daf6dce2c5f7fe8846c51fd2383c708bd61fba9581595c292b271"
source_kind: paper
author: "Furui Liu, Fangyuan Shi, Fang Du, Xiangmei Cao, Zhenhua Yu"
published: 2024-04-25
ingested: 2026-10-09
doi: "10.1093/bib/bbae187"
journal: "Briefings in Bioinformatics 25(3):bbae187"
tags: [CoT, scDNA-seq, copy-number, transformer, autoencoder, self-attention, clonal-substructure, GMM, HMM, rcCAE, SCOPE, SeCNV, SCICoNE, CHISEL, 10x-CNV, breast-cancer, per-dataset-training, genotype-layer-gap]
entities: []
concepts: ["[[copy-number-variation]]", "[[intratumor-heterogeneity]]", "[[clustering-algorithms]]", "[[dimensionality-reduction]]", "[[convolutional-neural-network]]", "[[single-cell-foundation-model]]"]
topics: ["[[40-Topics/scdna-seq]]", "[[40-Topics/cancer-clonal-evolution]]", "[[40-Topics/computational-methods]]", "[[40-Topics/sequence-models-and-foundation-models]]"]
---

**Citation:** Liu et al. (2024) — *CoT: a transformer-based method for inferring tumor clonal copy number substructure from scDNA-seq data* — *Briefings in Bioinformatics* 25(3):bbae187. [DOI](https://doi.org/10.1093/bib/bbae187)

# Liu 2024 — CoT

> **Clipping note:** the source is the full OUP web text. The two EM update equations (Eqs. 1–2) and the cluster indices in the dataset C/D-to-E mapping sentence did not survive the clip, and the supplementary figures and tables (including the attention-vs-convolution ablation) are only linked. No corresponding author is marked in the clipping.
>
> CoT (Copy number Transformer) uses a transformer autoencoder on single-cell DNA read counts to cluster cells into clones, then calls copy number jointly for the cells of each clone. Normalised bin counts for each cell (500 kb-scale bins, >5,000 bins genome-wide) are reshaped into a sequence of ⌈M/p⌉ tokens, each holding p consecutive bins. A six-layer self-attention encoder and a matching decoder are trained with MSE reconstruction. A GMM on the latent embeddings gives clones, and a clone-specific HMM (states up to 10 copies) estimates copy numbers. CoT is **trained from scratch on each dataset**. There is no pretraining corpus and no reuse across datasets. It is the nearest thing in this literature to a transformer on the scDNA genotype layer, and it shows the architecture alone does not make a foundation model.

## Key claims

- **Attention captures long-range copy-number structure better than convolution.** The authors argue that rcCAE's convolutional kernels capture local patterns, while self-attention links distant regions that share copy-number state. Replacing each attention module with a convolutional layer of similar parameter count lowered clustering accuracy (Supplementary Table 1).
- **Simulations: CoT keeps clustering accuracy as clone number grows.** There were 60 datasets: 200 cells each, ploidy 2, 3 or 4, 4, 9, 14 or 19 clones, five replicates, simulated with SCSsim at 0.02× coverage. On triploid data with 19 clones, median ΔK was −3 for rcCAE and 0 for CoT. On tetraploid data with 19 clones, mean ARI was 0.97 for rcCAE, 0.76 for Seurat, 0.72 for scTAG (given the true K) and 0.99 for CoT. Seurat at 19 clones had mean ARI 0.75, NMI 0.87 and median ΔK 5.
- **Simulations: copy-number accuracy.** On triploid data with nine clones, mean F-measure was 0.57 for SCOPE, 0.27 for SCICoNE, 0.89 for SeCNV, 0.92 for rcCAE and 0.97 for CoT. SCICoNE overestimated ploidy for most cells. SCOPE and SeCNV improved as clone number rose, which the authors attribute to more shared breakpoints. On small datasets (100 cells, 4 clones), SeCNV degraded on hyperploid data, SCOPE and SCICoNE misestimated ploidy, and CoT was the most robust.
- **Robust to hyperparameters.** Results were stable over bin sizes of 100–500 kb, latent dimensions d of 10–20 and chunk sizes p of 32–512 (Supplementary Figs. 4–12).
- **Real data: 10x Genomics breast tumour sections C, D and E** (1,254, 1,384 and 1,446 cells; 0.02–0.05× coverage), with CHISEL's clone labels as ground truth. CoT had the highest ARI and NMI on all three. On E, ARI was 0.945 for CoT, 0.687 for rcCAE, 0.885 for Seurat and 0.939 for scTAG. Copy-number F-measure against CHISEL calls was 0.84, 0.83 and 0.81 for CoT and 0.75, 0.73 and 0.78 for rcCAE. Only rcCAE could be compared, because per-cell BAMs were not available for the other methods.
- **Finer substructure than CHISEL on dataset E.** CoT found 8 clusters where the regrouped CHISEL labels had 5. These include a 4-cell hyperploid cluster split from the normal cells, and two pairs of subclones (ploidy 3.55 vs 3.50) that differ on chromosome 11 (copy number 4/2 vs 3/1 across p15.5–q23.1 / q23.1–q25). rcCAE did not resolve that difference.
- **scRNA-seq clustering tools are a poor fit for scDNA.** Seurat and scTAG underperform because scRNA tools assume independent features and select highly variable genes, whereas adjacent copy-number bins are correlated.

## Methods / evidence

Preprocessing follows rcCAE: read counts in fixed bins, GC and outlier correction, and library-size normalisation into an N × M matrix. This is reshaped to N × p × T with zero padding. There is **no input embedding layer**, and all sub-layers keep dimension p. The encoder has six identical layers (multi-head self-attention and feed-forward, each with residual connection and layer norm), followed by a d-dimensional fully connected latent layer. A fully connected layer restores the dimension before a decoder of the same structure, and an exponential output follows. Training uses Adam and MSE loss. Clustering is the rcCAE GMM approach with 100 random restarts. Copy-number calling fits a per-clone HMM on log-normalised read counts with Gaussian emissions, mean log(c_s/2) + o (o absorbs ploidy), parameters (π, A, σ, o) fitted by EM, and posterior-argmax states. Baselines are SCOPE, SCICoNE, SeCNV and rcCAE for CNAs, and Seurat and scTAG for clustering. CHISEL was excluded from benchmarking because it uses allele frequencies at ~5 Mb bins, but it supplies the real-data ground truth. Metrics are ARI, NMI and ΔK for clustering, and accuracy, balanced accuracy and macro F-measure for copy number. Hardware: one RTX 3090 GPU. Code: github.com/zhyu-lab/cot.

Weight: a focused methods paper with a reasonable simulation grid and one real tumour (three sections of the same 10x breast sample). The comparison to rcCAE, from the same group, is the main evidence. Many supporting results are in the supplement. No runtime or memory numbers appear in the main text. (synthesis)

## Limitations

**Authors' own:**
- CoT works on bins of hundreds of kilobases. Calling copy number in small bins (≤10 kb), which focal CNAs require, is unresolved because the data become very sparse and high-dimensional. A ZINB model is suggested.
- Global self-attention suits whole-cell features, but copy number is strongly correlated between adjacent bins, and those local patterns are not fully captured. A hybrid CNN-transformer is proposed.

**Reviewer notes:**
- The real-data "ground truth" is CHISEL's output. CHISEL itself uses allele information and joint analysis across sections. Where CoT splits CHISEL clusters (8 clusters vs 5 on dataset E), no orthogonal evidence confirms the extra clones are real. (synthesis)
- The model is **trained per dataset with an MSE reconstruction loss**, so embeddings from different runs live in different latent spaces. Cross-section clone matching (C/D to E) was done by comparing copy-number profiles, not in the embedding. (synthesis)
- The simulations use a single simulator, 200 cells and 0.02× coverage, and the real data come from one 10x platform. Ginkgo and HMMcopy-style pipelines and other single-cell platforms (DLP+, MALBAC, direct-library methods) are not compared. (synthesis)

## Surprising or load-bearing bits

- **Tokenisation by chunking bins.** CoT turns a >5,000-bin genome into ⌈M/p⌉ tokens of p raw bin values each, with no learned embedding and no positional encoding mentioned. This is a minimal way to fit scDNA read-depth profiles into a transformer, and it differs from gene-token or segment-token designs. (synthesis)
- **Clone-first, then call.** The gain in copy-number accuracy comes from pooling cells within a clone before the HMM. The attention model's job is only to produce good embeddings for clustering.
- **What it would take to make CoT a foundation model for single-cell DNA.** Three things are missing. First, a **pretraining corpus**: many scDNA datasets (10x CNV, DLP+, other WGA platforms) on a shared bin coordinate system and normalisation. Second, an objective that **transfers**: masked-bin or masked-segment prediction rather than per-dataset MSE reconstruction, so that weights and latent space carry over to new samples. Third, **evaluation of reuse**: frozen embeddings applied to unseen tumours, platforms and coverages. CoT's chunked-bin input could serve as a starting tokenisation. The bulk genotype FMs show the objectives exist, but no one has trained them on cells. (synthesis)

## Concepts touched

- [[copy-number-variation]] — joint clone-level HMM calling of single-cell copy number.
- [[intratumor-heterogeneity]] — clonal substructure in a breast tumour, including subclones that differ only on chromosome 11.
- [[clustering-algorithms]] — GMM on learned embeddings, compared with Seurat (graph clustering) and scTAG.
- [[dimensionality-reduction]] — the autoencoder latent space as the cell embedding, visualised by PCA.
- [[convolutional-neural-network]] — rcCAE and the convolution ablation as the local-pattern comparator.
- [[single-cell-foundation-model]] — an example of a transformer on scDNA that is *not* a foundation model, because it has no pretraining and no transfer. (synthesis)

## Connections to other sources

- The real data and ground-truth labels come from [[zaccaria-2021-chisel]] (10x breast tumour sections).
- CNA-calling baselines: [[wang-2020-scope]], [[kuipers-2025-scicone]] (the published SCICoNE). Ginkgo, [[garvin-2015-natmethods]], is cited but not benchmarked. Method landscape: [[mallory-2020-cna-review]].
- Downstream phylogeny from such clone profiles: [[kaufmann-2022-medicc2]]; see also [[phylogenetic-inference]]. (synthesis)
- Contrast with the bulk genotype FMs [[sidhom-2026-tessera]] and [[kong-2026-mutationprojector]], which are pretrained and reused frozen but take one bulk profile per tumour. CoT is single-cell but trained per dataset. Together they mark the two sides of the genotype-layer FM gap. (synthesis)

## Open questions

- Would pretraining a CoT-style encoder across many public scDNA datasets give embeddings that cluster unseen tumours without retraining? (synthesis)
- Does the proposed hybrid CNN-transformer recover focal CNAs at ≤10 kb bins?
- Are the extra CoT clusters on dataset E, such as the chromosome-11 subclones, supported by allele-specific or orthogonal data? (synthesis)

## Related

- [[40-Topics/scdna-seq]] · [[40-Topics/cancer-clonal-evolution]] · [[copy-number-variation]] · [[zaccaria-2021-chisel]] · [[single-cell-foundation-model]] · [[40-Topics/sequence-models-and-foundation-models]] · [[sidhom-2026-tessera]] · [[kong-2026-mutationprojector]]
