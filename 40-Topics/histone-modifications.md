---
type: topic
title: Histone modifications
aliases: [chromatin marks, post-translational modifications, PTMs, single-cell chromatin, histone marks]
tags: [chromatin, epigenetics, H3K27me3, H3K4me3, CUT&Tag, ChIC, MNase, enhancers, promoters]
created: 2026-05-12
updated: 2026-08-10
---

# Histone modifications

> Post-translational modifications of histone tails — methylation, acetylation, ubiquitylation, phosphorylation — that demarcate functional chromatin states ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]).

Modifications occur predominantly on histone H3 and H4 lysines and arginines ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]). They are the substrate for cell-type-specific gene regulation: profile them and you know which regions are active, primed, repressed, or silenced ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]). Single-cell profiling of these marks emerged around 2019 with scChIC-seq ([[10-Summaries/ku-2019-scchic-seq]]) and scCUT&Tag ([[10-Summaries/bartosovic-2021-sccut-tag]]), and has rapidly expanded into multi-mark / multi-modal readouts (scChIX, scEpi², sciCUT&Tag/MulTI-Tag, 6-base-CUT&Tag) ([[10-Summaries/yeung-2023-scchix-seq]]; [[10-Summaries/geisenberger-2025-scepi2-seq]]; [[10-Summaries/janssens-2023-scicut-tag]]; [[10-Summaries/tavares-2026-6-base-cut-tag]]).

## Canonical mark → state mapping

- **H3K4me3**: active promoters ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]).
- **H3K4me1**: enhancers — alone = primed; + H3K27ac = active; + H3K27me3 = poised ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]; foundational partition established by [[10-Summaries/creyghton-2010-h3k27ac-enhancers]]).
- **H3K27ac**: active promoters and enhancers ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]); the discriminating mark separating active from inactive enhancers, with eRNA production specifically at H3K27ac+ regions ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]).
- **H3K36me3**: actively transcribed gene bodies ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]).
- **H3K27me3**: facultative heterochromatin (Polycomb-repressed) ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]); enriched at LAD borders in some cell types ([[10-Summaries/van-steensel-2017-lads-review]]).
- **H3K9me3**: constitutive heterochromatin ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]); the cLAD anchoring mark ([[10-Summaries/van-steensel-2017-lads-review]]).

## Redundancy with chromatin compartments

Histone marks are not independent of other regulatory axes:

- **H3K9me2/3 anchors LADs to the nuclear lamina** via G9a and SUV39H1/2 acting redundantly ([[10-Summaries/van-steensel-2017-lads-review]]).
- **H3K27me3 is enriched at LAD boundaries** in some cell types ([[10-Summaries/van-steensel-2017-lads-review]]).
- **H3K27ac and other active marks** co-localize with accessible chromatin and compartment A regions ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]).
- **DNA methylation is partially redundant with H3K9me3** at heterochromatic regions, but *not* at LADs, where CpG methylation is not enriched ([[10-Summaries/van-steensel-2017-lads-review]]).

## Examples

- LLPS-competent IDR fusions (NUP98-HOXA9) induce H3K27ac at off-target proto-oncogenes ([[10-Summaries/ahn-2021-llps-cancer-looping]]).
- Polycomb (H3K27me3) occupancy decoupled from gene expression in mouse embryoid bodies, profiled by EpiDamID ([[10-Summaries/rooijers-2019-scdamt-seq]]).
- scCUT&Tag profiles H3K4me3/H3K27me3 transitions during oligodendrocyte differentiation in mouse brain ([[10-Summaries/bartosovic-2021-sccut-tag]]).

## Methods, by lineage

- [[30-Concepts/chip-seq]] — bulk ancestor.
- [[30-Concepts/cut-and-run]] — antibody-tethered MNase (Skene/Henikoff).
- [[30-Concepts/cut-and-tag]] — antibody-tethered Tn5 (Kaya-Okur/Henikoff).
- [[30-Concepts/chic-seq]] — original chromatin immunocleavage (Schmid).
- [[30-Concepts/sortchic]] — FACS-integrated single-cell ChIC.
- [[30-Concepts/scchic-seq]], [[30-Concepts/scchix-seq]], [[30-Concepts/scicut-tag]], [[30-Concepts/scepi2-seq]], [[30-Concepts/6-base-cut-and-tag]], [[30-Concepts/multi-tag]] — single-cell variants.

## Key entities

- [[20-Entities/keji-zhao]] — Zhao lab; scChIC-seq.
- [[20-Entities/steven-henikoff]] — Henikoff lab; CUT&RUN, CUT&Tag, sciCUT&Tag, MulTI-Tag.
- [[20-Entities/alexander-van-oudenaarden]] — van Oudenaarden lab; sortChIC, scChIX-seq, scEpi²-seq.
- [[20-Entities/shankar-balasubramanian]] — Balasubramanian lab; 6-base-CUT&Tag.
- [[20-Entities/jake-yeung]] — Yeung; scChIX-seq.

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

### Enhancer / promoter biology
- [[10-Summaries/creyghton-2010-h3k27ac-enhancers]] — Creyghton 2010. H3K27ac discriminates active from poised enhancers.
- [[10-Summaries/ahn-2021-llps-cancer-looping]] — IDR-fusion-driven aberrant H3K27ac at oncogenes.
- [[10-Summaries/rooijers-2019-scdamt-seq]] — EpiDamID; Polycomb occupancy vs expression decoupling.

### Computational prediction
- [[10-Summaries/yin-2019-deephistone]] — Yin/Jiang 2019. CNN predicts 7 marks from DNA + DNase-seq.

### Bulk reference
- [[10-Summaries/klemm-2019-chromatin-accessibility-review]] — Bannister & Kouzarides-style canonical histone-marks review.
- [[10-Summaries/andrew-2011-cellresearch]] — Bannister & Kouzarides 2011 — Regulation of chromatin by histone modifications (review).

## Synthesized notes

- [[50-Notes/regulatory-layers-overview]] — histone marks as one of the four molecular regulatory layers.
- _Future_: MNase-based (sortChIC family) vs Tn5-based (CUT&Tag family) single-cell chromatin profiling — tradeoffs in nucleosome-positioning fidelity vs throughput (synthesis target).

## Open questions

- Per-cell sensitivity is the recurring constraint: scCUT&Tag yields ~1k–2k peaks per cell at standard depth, vs >24k peaks in bulk pooled ([[10-Summaries/bartosovic-2021-sccut-tag]]). How much can linear amplification or library optimization improve this?
- Active vs repressive mark mutual exclusivity at the single-cell level: bulk data show clean separation, but scChIX-seq results show **cell-type-specific** transitions at individual loci that bulk averages obscure ([[10-Summaries/yeung-2023-scchix-seq]]).
- How redundant are histone marks with LAD position? H3K9me2/3 anchors LADs ([[10-Summaries/van-steensel-2017-lads-review]]) — does any histone mark add information once you know LAD status?

## Additions — 2026-08-10 ingest

- **Bivalency** established in ES cells across 61 tiled regions, replicated in an independent line with a non-crosslinked MNase protocol (94/95 domains recovered) and confirmed on the same chromatin by sequential ChIP ([[10-Summaries/bernstein-2006-bivalent-chromatin]]); refined to adjacent histones within one nucleosome ([[10-Summaries/rothbart-2014-histone-dna-language]]).
- **The histone code is more complex than one-mark-one-domain**: PTMs at the histone–DNA interface act physically on nucleosome stability; >200 distinct modified H3.2 and H4 N-terminal forms exist; readers engage multivalently in *cis* and *trans*; and acyl-CoA-derived marks couple chromatin state to metabolic flux ([[10-Summaries/rothbart-2014-histone-dna-language]]).
- **Sequence predicts the ES-cell ground state**: H3K4me3 tracks CpG density (r_phi = 0.73) and H3K27me3 tracks conserved transposon-exclusion zones (r_phi = 0.69), with the correlation weakening in differentiated cells ([[10-Summaries/bernstein-2006-bivalent-chromatin]]).
- **Single-cell profiling**: CUT&Tag's founding paper ([[10-Summaries/kaya-okur-2019-cut-and-tag]]) → repressive-mark cell typing in tissue and tumors ([[10-Summaries/wu-2021-sccut-tag]]) → multimodal chromatin-state inference via surface protein ([[10-Summaries/zhang-2022-sccut-tag-pro]]) → barcoded multi-epitope co-localization ([[10-Summaries/gopalan-2022-multi-cut-and-tag]]).
- **Population reference**: 127 epigenomes on five core marks, a shared 15-state model, and the finding that enhancer-associated marks carry essentially all the GWAS tissue signal while H3K27me3 and H3K9me3 carry none ([[10-Summaries/roadmap-2015-111-epigenomes]]).
- **Enhancer priming** by collaborative lineage-determining TF binding, with HOMER as the tool built to find it ([[10-Summaries/heinz-2010-homer]]).

## Related

- [[40-Topics/chromatin-architecture]] · [[40-Topics/dna-methylation]] · [[40-Topics/single-cell-multiomics]]
- [[50-Notes/regulatory-layers-overview]]
- [[10-Summaries/bernstein-2006-bivalent-chromatin]] · [[10-Summaries/rothbart-2014-histone-dna-language]] · [[10-Summaries/kaya-okur-2019-cut-and-tag]] · [[10-Summaries/roadmap-2015-111-epigenomes]]
