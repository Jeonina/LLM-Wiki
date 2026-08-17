---
type: summary
title: "Biancalani et al. 2021 — Deep learning and alignment of spatially resolved single-cell transcriptomes with Tangram"
source: "[[00-Sources/papers/Deep learning and alignment of spatially resolved single-cell transcriptomes with Tangram]]"
source_kind: paper
author: "Tommaso Biancalani, Gabriele Scalia, Lorenzo Buffoni, … Xiaowei Zhuang, Evan Z. Macosko, Aviv Regev (corresponding)"
published: 2021-10-28
ingested: 2026-08-17
doi: "10.1038/s41592-021-01264-7"
journal: "Nature Methods 18:1352–1362"
tags: [Tangram, spatial-alignment, MERFISH, STARmap, smFISH, Visium, histology, SHARE-seq, mouse-brain]
entities: ["[[aviv-regev]]", "[[evan-macosko]]"]
concepts: ["[[spatial-multiomics]]", "[[multimodal-integration-methods]]", "[[imputation]]", "[[scrna-seq]]", "[[chromatin-accessibility]]"]
topics: ["[[single-cell-multiomics]]", "[[computational-methods]]"]
---

**Citation:** Biancalani et al. (2021) — *Deep learning and alignment of spatially resolved single-cell transcriptomes with Tangram* — *Nature Methods* 18, 1352–1362. [DOI](https://doi.org/10.1038/s41592-021-01264-7)

# Biancalani 2021 — Tangram

> Three spatial technologies, three complementary failures: sc/snRNA-seq profiles cells comprehensively but **loses position**; spatial transcriptomics keeps position but at **lower resolution and sensitivity**; targeted in-situ methods have both but are **limited in gene throughput**. Tangram's move is to **align sc/snRNA-seq onto whichever spatial measurement exists** — MERFISH, STARmap, smFISH, Visium, or even histological images — and let the dissociated data supply the genome-wide depth the spatial data lacks.

## Key claims

- **Platform-agnostic alignment** is the central design property. Tangram maps to five different spatial data types including histology, rather than being built for one.
- **Any sc/snRNA-seq input, including multimodal.** Applied to [[ma-2020-cell|SHARE-seq]] data, Tangram propagated the alignment to the paired chromatin measurement and thereby **revealed spatial patterns of chromatin accessibility** — spatial epigenomics inferred from spatial transcriptomics plus a paired assay.
- **A genome-wide, anatomically integrated spatial map at single-cell resolution** was reconstructed for the visual and somatomotor areas of healthy mouse brain.
- The motivating goal is stated as charting an organ's atlas by spatially resolving the *entire* single-cell transcriptome and relating cellular features to the **anatomical scale** — i.e. connecting molecular and anatomical levels of description.

## Methods / evidence

Deep-learning alignment applied across five spatial platforms; demonstration on mouse brain visual and somatomotor cortex; extension to SHARE-seq multimodal input.

Weight: breadth across platforms is the strongest evidence that the method is not overfit to one assay's quirks. As with all spatial-mapping methods, ground truth for "which cell was really here" is largely unavailable, so validation leans on anatomical plausibility and marker consistency.

## Surprising or load-bearing bits

- **Spatial chromatin accessibility by propagation, in 2021.** Because SHARE-seq measures RNA and ATAC in the same cell, aligning the RNA to space carries the ATAC along for free. This is the same objective [[debnath-2026-ison|ISON]] pursues five years later with a different method — and Tangram gets there via the paired assay rather than a learned cross-modality decoder. Worth citing together when discussing how the field substitutes computation for a missing spatial epigenome assay. (synthesis)
- **Aligning to a histological image** is the most surprising input. It implies the mapping can be driven by morphology alone where molecular spatial data is absent — cheap, and available retrospectively for archival tissue. (synthesis)
- **The three-way technology trade (resolution / sensitivity / gene throughput)** is the cleanest statement in the corpus of why spatial transcriptomics needed a computational layer at all, and it applies unchanged to spatial epigenomics today. (synthesis)
- **Author list spans the field's spatial infrastructure** — Zhuang (MERFISH), Macosko (Slide-seq, [[zhao-2022-nature|slide-DNA-seq]]), Buenrostro, Regev — which is why the platform coverage is so broad.
- Tangram later becomes a standard baseline: [[debnath-2026-ison|ISON]] benchmarks against it for spatial chromatin accessibility prediction.

## Entities mentioned

- [[aviv-regev]] — corresponding author.
- [[evan-macosko]] — coauthor; Slide-seq and slide-DNA-seq.

## Concepts touched

- [[spatial-multiomics]] — computational alignment as the bridge between dissociated and spatial data.
- [[imputation]] — genome-wide expression imputed at spatial positions from a dissociated reference.

## Connections to other sources

- Deconvolution-based alternative for the same problem: [[kleshchevnikov-2022-cell2location]].
- Later method that infers spatial *chromatin accessibility* without a paired spatial assay: [[debnath-2026-ison]], which uses Tangram as a baseline.
- Multimodal input used here: [[ma-2020-cell]] (SHARE-seq).
- Spatial DNA/genomic assays: [[zhao-2022-nature]] (slide-DNA-seq), [[andrewc-2020-science]] (in-situ genome sequencing), [[cardilla-2025-spatial-methylome]], [[mo-2023-stam-seq]].
- Spatial review context: [[vandereyken-2023-spatial-multiomics]].
- Integration taxonomy: [[argelaguet-2021-integration-principles]].
- Reference-mapping cousins that also infer unmeasured modalities: [[kang-2021-symphony]], [[lakkis-2022-scipenn]].

## Open questions

- **Ground truth for spatial assignment barely exists**, so accuracy claims across all methods in this class rest on internal consistency and anatomical plausibility. (synthesis)
- Histology-driven alignment is the least constrained input; how far it can be trusted without molecular spatial data is not characterised here.
- The SHARE-seq chromatin result is a demonstration on one dataset, not a validated spatial epigenome map.

## Related

- [[kleshchevnikov-2022-cell2location]] · [[debnath-2026-ison]] · [[spatial-multiomics]] · [[40-Topics/single-cell-multiomics]]
