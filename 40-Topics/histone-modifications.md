---
type: topic
title: Histone modifications
aliases: [chromatin marks, post-translational modifications, PTMs, single-cell chromatin]
tags: [chromatin, epigenetics, H3K27me3, H3K4me3, CUT&Tag, ChIC, MNase]
created: 2026-05-12
updated: 2026-05-19
---

# Histone modifications

> Post-translational modifications of histone tails (methylation, acetylation, ubiquitylation, phosphorylation) demarcate functional chromatin states ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]) — active promoters (H3K4me3), enhancers (H3K4me1/H3K27ac), gene bodies (H3K36me3), facultative heterochromatin (H3K27me3), constitutive heterochromatin (H3K9me3) ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]; [[10-Summaries/van-steensel-2017-lads-review]] for H3K9me3/H3K27me3 anchoring roles). Single-cell profiling of these marks emerged around 2019 with scChIC-seq ([[10-Summaries/ku-2019-scchic-seq]]) and scCUT&Tag ([[10-Summaries/bartosovic-2021-sccut-tag]]), and has rapidly expanded into multi-mark / multi-modal readouts (scChIX, scEpi², sciCUT&Tag/MulTI-Tag, 6-base-CUT&Tag).

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
- [[10-Summaries/ku-2019-scchic-seq]] — Ku/Zhao 2019. First single-cell ChIC.
- [[10-Summaries/bartosovic-2021-sccut-tag]] — Bartošovič 2021. scCUT&Tag in tissue.
- [[10-Summaries/bartosovic-2022-nano-cut-tag]] — Bartošovič 2022. nano-CUT&Tag multi-modal.

### Multiplexing histone marks within a cell
- [[10-Summaries/yeung-2023-scchix-seq]] — Yeung/van Oudenaarden 2023. Two marks per cell with computational deconvolution.
- [[10-Summaries/janssens-2023-scicut-tag]] — Janssens/Henikoff 2023. Combinatorial indexing CUT&Tag at 40k cells/chip; MulTI-Tag for multi-epitope.

### Coupled histone + DNA modification readouts
- [[10-Summaries/geisenberger-2025-scepi2-seq]] — Geisenberger/van Oudenaarden 2025. scEpi²-seq: sortChIC + TAPS.
- [[10-Summaries/tavares-2026-6-base-cut-tag]] — Tavares/Balasubramanian 2026. 6-base-CUT&Tag: 5mC + 5hmC + histone mark per fragment.

### Computational prediction
- [[10-Summaries/yin-2019-deephistone]] — Yin/Jiang 2019. CNN predicts 7 marks from DNA + DNase-seq.

### Bulk reference
- [[10-Summaries/klemm-2019-chromatin-accessibility-review]] — Bannister & Kouzarides-style canonical histone-marks review.

## Synthesized notes

- [[50-Notes/regulatory-layers-overview]] — histone marks as one of the four molecular regulatory layers.
- _Future_: MNase-based (sortChIC family) vs Tn5-based (CUT&Tag family) single-cell chromatin profiling — tradeoffs in nucleosome-positioning fidelity vs throughput (synthesis target).

## Open questions

- Per-cell sensitivity is the recurring constraint: scCUT&Tag yields ~1k–2k peaks per cell at standard depth, vs >24k peaks in bulk pooled ([[10-Summaries/bartosovic-2021-sccut-tag]]). How much can linear amplification or library optimization improve this?
- Active vs repressive mark mutual exclusivity at the single-cell level: bulk data show clean separation, but scChIX-seq results show **cell-type-specific** transitions at individual loci that bulk averages obscure ([[10-Summaries/yeung-2023-scchix-seq]]).
- How redundant are histone marks with LAD position? H3K9me2/3 anchors LADs ([[10-Summaries/van-steensel-2017-lads-review]]) — does any histone mark add information once you know LAD status?

## Related

- [[40-Topics/chromatin-architecture]] · [[40-Topics/dna-methylation]] · [[40-Topics/single-cell-multiomics]]
