---
type: topic
title: Histone modifications
aliases: [chromatin marks, post-translational modifications, PTMs, single-cell chromatin]
tags: [chromatin, epigenetics, H3K27me3, H3K4me3, CUT&Tag, ChIC, MNase]
created: 2026-05-12
updated: 2026-05-12
---

# Histone modifications

> Post-translational modifications of histone tails (methylation, acetylation, ubiquitylation, phosphorylation) demarcate functional chromatin states — active promoters (H3K4me3), enhancers (H3K4me1/H3K27ac), gene bodies (H3K36me3), facultative heterochromatin (H3K27me3), constitutive heterochromatin (H3K9me3). Single-cell profiling of these marks emerged around 2019 with scChIC-seq and scCUT&Tag, and has rapidly expanded into multi-mark / multi-modal readouts (scChIX, scEpi², sciCUT&Tag/MulTI-Tag, 6-base-CUT&Tag).

## Core concepts

- [[30-Concepts/histone-modifications]] — the marks and their biological meaning
- [[30-Concepts/chip-seq]] — bulk ancestor
- [[30-Concepts/cut-and-run]] — antibody-tethered MNase (Skene/Henikoff)
- [[30-Concepts/cut-and-tag]] — antibody-tethered Tn5 (Kaya-Okur/Henikoff)
- [[30-Concepts/chic-seq]] — original chromatin immunocleavage (Schmid)
- [[30-Concepts/sortchic]] — FACS-integrated single-cell ChIC
- [[30-Concepts/scchic-seq]], [[30-Concepts/scchix-seq]], [[30-Concepts/scicut-tag]], [[30-Concepts/scepi2-seq]], [[30-Concepts/6-base-cut-and-tag]], [[30-Concepts/multi-tag]] — single-cell variants

## Key entities

- [[20-Entities/keji-zhao]] — Zhao lab; scChIC-seq
- [[20-Entities/steven-henikoff]] — Henikoff lab; CUT&RUN, CUT&Tag, sciCUT&Tag, MulTI-Tag
- [[20-Entities/alexander-van-oudenaarden]] — van Oudenaarden lab; sortChIC, scChIX-seq, scEpi²-seq
- [[20-Entities/shankar-balasubramanian]] — Balasubramanian lab; 6-base-CUT&Tag
- [[20-Entities/jake-yeung]] — Yeung; scChIX-seq

## Sources, by sub-theme

### Foundational single-cell methods
- [[10-Summaries/single-cell-chromatin-immunocleavage-sequencing-scchic-seq-to-profile-histone-modification]] — Ku/Zhao 2019. First single-cell ChIC.

### Multiplexing histone marks within a cell
- [[10-Summaries/scchix-seq-infers-dynamic-relationships-between-histone-modifications-in-single-cells]] — Yeung/van Oudenaarden 2023. Two marks per cell with computational deconvolution.
- [[10-Summaries/scalable-single-cell-profiling-of-chromatin-modifications-with-scicut-tag]] — Janssens/Henikoff 2023. Combinatorial indexing CUT&Tag at 40k cells/chip; MulTI-Tag for multi-epitope.

### Coupled histone + DNA modification readouts
- [[10-Summaries/single-cell-multi-omic-detection-of-dna-methylation-and-histone-modifications-reconstructs-the-dynamics-of-epigenomic-maintenance]] — Geisenberger/van Oudenaarden 2025. scEpi²-seq: sortChIC + TAPS.
- [[10-Summaries/sequencing-dna-methylation-and-hydroxymethylation-at-co-occurring-chromatin-features]] — Tavares/Balasubramanian 2026. 6-base-CUT&Tag: 5mC + 5hmC + histone mark per fragment.

### Computational prediction
- [[10-Summaries/deephistone-a-deep-learning-approach-to-predicting-histone-modifications]] — Yin/Jiang 2019. CNN predicts 7 marks from DNA + DNase-seq.

## Synthesized notes

None yet. Natural note: "MNase-based (sortChIC family) vs Tn5-based (CUT&Tag family) single-cell chromatin profiling" — tradeoffs in nucleosome-positioning fidelity vs throughput.

## Open questions

- Per-cell sensitivity is the recurring constraint: scCUT&Tag yields ~1k–2k peaks per cell at standard depth, vs >24k peaks in bulk pooled. How much can linear amplification or library optimization improve this?
- Active vs repressive mark mutual exclusivity at the single-cell level: bulk data show clean separation, but scChIX-seq results show **cell-type-specific** transitions at individual loci that bulk averages obscure.

## Related

- [[40-Topics/chromatin-architecture]] · [[40-Topics/dna-methylation]] · [[40-Topics/single-cell-multiomics]]
