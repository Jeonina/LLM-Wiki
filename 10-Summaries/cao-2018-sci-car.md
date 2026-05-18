---
type: summary
title: "Cao 2018 — sci-CAR: Joint profiling of chromatin accessibility and gene expression in thousands of single cells"
aliases: [sci-CAR, Cao 2018, Cao sci-CAR]
tags: [sci-CAR, joint-assay, scATAC-seq, scRNA-seq, combinatorial-indexing, single-cell-multiomics]
created: 2026-05-12
updated: 2026-05-12
sources: ["00-Sources/papers/Joint profiling of chromatin accessibility and gene expression in thousands of single cells.md"]
---

**Citation:** Cao et al. (2018) — *sci-CAR: Joint profiling of chromatin accessibility and gene expression in thousands of single cells* — *?*. [DOI](https://doi.org/10.1126/science.aau0730)

# Cao et al. 2018 — sci-CAR

> Junyue Cao, Darren A. Cusanovich, Vijay Ramani, Delasa Aghamirzaie, Hannah A. Pliner, Andrew J. Hill, Riza M. Daza, Jose L. McFaline-Figueroa, Jonathan S. Packer, Lena Christiansen, … Jay Shendure, Cole Trapnell. *Science* **361**, 1380–1385 (Aug 2018). DOI: 10.1126/science.aau0730.

## Thesis

Before sci-CAR, joint single-cell profiling of chromatin accessibility + transcription required physical isolation of each cell, limiting throughput to a handful per experiment. **sci-CAR** combines single-cell combinatorial indexing for ATAC (sci-ATAC-seq) and RNA (sci-RNA-seq) into one pooled, split-pool workflow that scales to thousands of jointly profiled cells per run.

## Method (key steps)

1. Nuclei extracted (fixed or fresh), distributed to wells.
2. **First RNA index**: in-situ reverse transcription with a poly(T) primer carrying a well-specific barcode + UMI.
3. **First ATAC index**: in-situ Tn5 tagmentation with a barcoded transposase.
4. Pool all nuclei, redistribute by FACS to plates.
5. Lyse, split lysate into RNA-dedicated and ATAC-dedicated portions.
6. Amplify each with primers carrying a **second** well-specific barcode → each read carries two well-IDs that together identify the cell of origin.
7. Pool and sequence; pair RNA + ATAC reads from the same cell via the barcode pair.

## Key claims

1. **4,825 joint cells from a dexamethasone time course on A549 lung adenocarcinoma cells** (0 / 1 / 3 hr DEX) — captured glucocorticoid-receptor activation dynamics at both layers.
2. **11,296 joint cells from adult mouse kidney**, defining 14 cell-type clusters with distinct chromatin accessibility programs.
3. **Pseudotime alignment**: ATAC and RNA can be co-ordered along a single trajectory. Of 2,613 DE genes in the DEX series, 11 showed concordant promoter-accessibility + expression dynamics; many more showed accessibility changes with no detectable expression change at the depth tested.
4. **Cis-regulatory linking by covariance**: across 222 pseudocells in kidney, 1,260 distal peaks linked to 321 genes (median 3 peaks per gene). Permutation controls confirmed the links are not artifacts of regularized regression. Including linked distal sites improved expression prediction from accessibility by **fourfold** over promoter-only.
5. **Species-mixing validation**: 99% of HEK293T+NIH/3T3 mixed-well cells received concordant species labels from sci-RNA and sci-ATAC reads, confirming barcode pairing.

## Limitations the paper acknowledges

- ATAC arm is **~10× lower complexity** than RNA-only sci-ATAC-seq plates, due to using only half the lysate and buffer modifications.
- Joint matrices are **sparse**, especially on the ATAC side — initial clustering of cells by ATAC alone failed to recover the cell types that RNA found; recovery required RNA-defined pseudocell aggregation.
- Distal-site-to-gene links are **correlative**, covering a minority of DE/DA genes.

## Surprising / load-bearing

- The paper explicitly frames sci-CAR as the **template for future DNA-anchored joint assays** ("methylation plus transcripts, chromosome conformation plus transcripts, or DNA sequence plus transcripts"). Reads as the methodological scaffold the field then followed: 10x Multiome (commercial sci-CAR-style coassay), [[10-Summaries/scnmt-seq-enables-joint-profiling-of-chromatin-accessibility-dna-methylation-and-transcription-in-single-cells]] (NMT, three-modality), SHARE-seq (split-pool scaling).
- The promoter-accessibility-vs-expression correlation was **stronger in the dynamic DEX time series (rho=0.63) than in the static kidney cell-type comparison (rho=0.17)** — a methodologically important reminder that the chromatin-to-RNA causal axis is more visible in perturbation-response than in steady-state heterogeneity.

## Entities / concepts touched

[[chromatin-accessibility]] · [[scatac-seq]] · [[combinatorial-indexing]] · [[tn5-tagmentation]] · [[single-cell-multiomics]] · [[40-Topics/single-cell-multiomics]] · [[lung-adenocarcinoma]]

## Related summaries

- [[scnmt-seq-enables-joint-profiling-of-chromatin-accessibility-dna-methylation-and-transcription-in-single-cells]] — Clark scNMT-seq, three-modality but lower throughput.
- [[share-seq-reveals-chromatin-potential-nature-reviews-genetics]] — Ma SHARE-seq, split-pool scaling alternative.
- [[g-t-seq-parallel-sequencing-of-single-cell-genomes-and-transcriptomes]] — Macaulay G&T-seq, DNA + RNA joint (precursor of DNA-anchored joint assays).
- [[integrated-genome-and-transcriptome-sequencing-of-the-same-cell]] — Dey DR-seq, contemporaneous DNA+RNA joint method.

---
**Source:** [Open paper](https://www.science.org/doi/10.1126/science.aau0730)
## Related

- [[40-Topics/single-cell-multiomics]]
