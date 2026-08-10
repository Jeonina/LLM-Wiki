---
type: summary
title: "Hao et al. 2024 — Dictionary learning for integrative, multimodal and scalable single-cell analysis (Seurat v5)"
source: "[[00-Sources/papers/Dictionary learning for integrative, multimodal and scalable single-cell analysis]]"
source_kind: paper
author: "Yuhan Hao, Tim Stuart, Madeline H. Kowalski, Saket Choudhary, Paul Hoffman, Austin Hartman, Avi Srivastava, Gesmira Molla, Shaista Madad, Carlos Fernandez-Granda, Rahul Satija (corresponding)"
published: 2023-05-25
ingested: 2026-08-10
doi: "10.1038/s41587-023-01767-y"
journal: "Nature Biotechnology"
tags: [Seurat-v5, bridge-integration, dictionary-learning, atomic-sketch, reference-mapping, scalability, diagonal-integration, computational-tool]
entities: ["[[rahul-satija]]"]
concepts: ["[[multimodal-integration-methods]]", "[[joint-single-cell-multi-omics]]", "[[scatac-seq]]", "[[cut-and-tag]]", "[[scbs-seq]]", "[[cite-seq]]", "[[pseudo-bulk]]"]
topics: ["[[single-cell-multiomics]]"]
---

**Citation:** Hao et al. (2024) — *Dictionary learning for integrative, multimodal and scalable single-cell analysis* — *Nature Biotechnology* 42, 293–304. [DOI](https://doi.org/10.1038/s41587-023-01767-y)

# Hao 2024 — bridge integration (Seurat v5)

> Reference atlases are built from scRNA-seq, so epigenomic datasets cannot be mapped onto them without assuming that accessibility (or inverse methylation) predicts expression — an assumption that fails exactly where it matters. **Bridge integration** removes it: use a multiomic dataset as a dictionary whose individual *cells* are the atoms, reconstruct each unimodal dataset as a weighted combination of those atoms, and the relationship between modalities is **learned rather than assumed**.

## Key claims

- The gene-activity-score workaround — summing ATAC signal over gene bodies, or inverting methylation — makes "strict biological assumptions (for example, that accessible chromatin is associated with active transcription) that may not always hold true, particularly when analyzing cellular transitions or developmental trajectories."
- **The dictionary-learning inversion is the idea**: classically, dictionary atoms are *features*; here each **cell** in the multiomic bridge is an atom. Two datasets measuring completely different features are each reconstructed in terms of the same atoms, and are therefore comparable. Graph-Laplacian eigendecomposition reduces atom count to eigenvector count for tractability.
- Modular by design: the transformation is the contribution; the final alignment step is compatible with Harmony, mnnCorrect, Seurat, Scanorama or scVI.
- **scATAC → scRNA reference** (297,627-cell BMMC Azimuth reference, 35 annotated states; 10x multiome bridge of 32,368 cells): recovers subpopulations invisible to unsupervised scATAC analysis — CD14/CD16 monocytes, CD56^bright/dim NK, CD8/MAIT, and **ILCs (0.15%) and AXL⁺SIGLEC6⁺ ASDCs (0.10%) never previously identified in scATAC data** — each validated by differential accessibility at canonical loci (e.g. an ASDC-specific peak in *SIGLEC6*).
- Handles query-is-a-subset correctly: CD34⁺-enriched fractions map only to HSC/progenitor states.
- **Cross-modality trajectory analysis**: 236 loci where accessibility *leads* expression along myeloid differentiation, e.g. the *MPO* upstream regulatory region opens in LMPPs while expression appears in GMPs. KEGG enrichment for cell cycle and DNA replication, interpreted as priming for rapid cell-cycle entry — and derived from modalities measured in **separate experiments**.
- **Bridge requirements are stated concretely**: ~50 cells per cell type in the bridge suffices; performance survives substantial compositional differences between bridge and query; bridge quality can be degraded heavily (86% RNA UMI downsampling, 70% ATAC fragment downsampling) before integration suffers.
- **The failure mode is well-behaved.** Removing all pDCs from the bridge dropped pDC annotation from 94.4% to 83.5% — but average prediction score for those cells fell from **0.907 to 0.514**, i.e. the method reports low confidence when its assumptions are violated. Reproduced for B cells, CD8 T cells and CD14 monocytes.
- Benchmarks: outperforms MultiVI and Cobolt (neither matched ASDCs) and bridge-free CCA/LIGER, with the **largest gains on rare cell types**. Runtime 0.8 h vs Cobolt 3.3 h vs MultiVI 15.7 h.
- Generalizes across modalities: histone marks via a Paired-Tag bridge (H3K27ac, H3K27me3, H3K4me1 all integrate, highest Jaccard/classification scores); **DNA methylation** via an snmC2T-seq bridge onto an Allen Brain Atlas reference, where reference annotation relabelled three unsupervised "L6" clusters as near-projecting vs L6b excitatory neurons; and **CyTOF** (5.17M cells) via a CITE-seq bridge, enabling inference of intracellular protein levels (FOXP3 in Tregs, KLRG1 in effector T cells, granzyme B depletion in MAIT cells) and annotation of 0.024% ILCs by correct CD25⁺CD127⁺CD161⁺CD56⁻ phenotype.
- **Atomic sketch integration** for scale: sketch ~5,000 cells per dataset as atoms, learn per-dataset dictionary representations (parallelizable), integrate only the atoms, then reconstruct the full datasets. Leverage-score sampling avoids needing PCA on the full data. 19 lung datasets / 1,525,710 cells integrated **in 55 minutes on one core**; 3.46M PBMC transcriptomes plus 5.17M CyTOF cells = 8.6M profiles.
- Community-scale payoff: pulmonary ionocytes (0.047%) were annotated in only 6 of 19 lung studies independently but found in **17 of 19** after integration, and 116 markers were identified from pseudobulk differential expression — and **random downsampling instead of leverage-score sketching fails to integrate them at all**.

## Methods / evidence

Ground-truth benchmarking against 10x multiome and Paired-Tag datasets where the true cross-modality cell correspondence is known; robustness characterized by systematic bridge downsampling, cell-type depletion and compositional perturbation; runtime and metric comparisons against three method classes.

The depletion experiment is the most valuable piece: it establishes that the method's confidence score is diagnostic, not decorative.

## Surprising or load-bearing bits

- **Reference mapping finds cell types unsupervised analysis of the same data cannot.** ILCs and ASDCs at ~0.1% were present in the scATAC data all along. This inverts the usual reading of an epigenomic dataset's resolution: the limit was the analysis, not the assay.
- **The 50-cells-per-type bridge guideline is directly actionable for experimental design** — it says how much multiome to run alongside a large single-modality experiment, and the answer is "not much." Combined with the tolerance to low bridge quality, this makes a small multiome run a cheap insurance policy on a large scATAC or scCUT&Tag study.
- The accessibility-leads-expression result recovers a temporal ordering across modalities **measured in different cells** — the payoff [[argelaguet-2021-integration-principles|Argelaguet 2021]] describes as diagonal integration's promise, delivered here with a bridge that removes the assumption.
- Methylation-modality mapping matters for this wiki specifically: [[luo-2018-snmc-seq2|snmC-seq]] data annotated against a transcriptomic brain reference means single-cell methylomes inherit expertly curated cell ontologies rather than inventing their own.
- Atomic sketch integration reframes scale: the expensive step touches only atoms, so "community-wide" integration stops being a compute problem. And **sketching method choice is load-bearing** — random downsampling loses the rare populations that motivate the exercise.
- CyTOF integration means the bridge does not need to be sequencing-based on both sides.

## Entities mentioned

- [[rahul-satija]] — corresponding author; Seurat/Azimuth/WNN lineage, also [[zhang-2022-sccut-tag-pro]].

## Concepts touched

- [[multimodal-integration-methods]] — bridge integration is the assumption-free diagonal method this page needs.
- [[joint-single-cell-multi-omics]] — reframes joint assays as *bridges* rather than end products, which changes why you run them.

## Connections to other sources

- Solves the diagonal-integration problem posed in [[argelaguet-2021-integration-principles]]; benchmarked against [[ashuach-2023-multivi|MultiVI]], [[gong-2021-cobolt|Cobolt]], [[welch-2019-liger|LIGER]].
- Sibling to [[zhang-2022-sccut-tag-pro]] from the same lab — both use a shared modality to bridge experiments, one via protein, one via a multiomic dictionary.
- Query modalities drawn from [[granja-2021-archr]]/[[stuart-2021-natmethods|Signac]]-style scATAC, [[kaya-okur-2019-cut-and-tag|CUT&Tag]], [[luo-2018-snmc-seq2|snmC-seq]].
- Bridges available in this corpus: [[ma-2020-share-seq|SHARE-seq]], [[cao-2018-sci-car|sci-CAR]], [[clark-2018-scnmt-seq|scNMT-seq]], Paired-Tag.

## Open questions

- Bridge integration needs a multiomic assay **pairing the query modality with RNA**. For modalities with no such assay — single-cell Hi-C, most scDNA-seq — there is no bridge, and the method does not apply. That is the structural limit for this wiki's core modality.
- Whether the ~50-cells-per-type rule holds for sparser modalities (scBS, scCUT&Tag) as it does for ATAC is untested here.
- Confidence scores drop appropriately when a type is missing from the bridge, but no threshold is recommended for deciding a query cell is genuinely unmapped.

## Related

- [[argelaguet-2021-integration-principles]] · [[zhang-2022-sccut-tag-pro]] · [[multimodal-integration-methods]] · [[single-cell-multiomics]]
