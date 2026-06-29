---
type: note
title: "MNase vs Tn5 — two chemistries for single-cell histone profiling"
aliases: [MNase vs Tn5, scChIC vs scCUT&Tag, single-cell chromatin chemistry]
tags: [synthesis, histone-modifications, single-cell-chromatin, MNase, Tn5, methods-tradeoff]
created: 2026-05-19
updated: 2026-05-19
sources: [
  "[[10-Summaries/rotem-2015-drop-chip]]",
  "[[10-Summaries/ku-2019-scchic-seq]]",
  "[[10-Summaries/yeung-2023-scchix-seq]]",
  "[[10-Summaries/geisenberger-2025-scepi2-seq]]",
  "[[10-Summaries/bartosovic-2021-sccut-tag]]",
  "[[10-Summaries/bartosovic-2022-nano-cut-tag]]",
  "[[10-Summaries/janssens-2023-scicut-tag]]",
  "[[10-Summaries/tavares-2026-6-base-cut-tag]]",
  "[[10-Summaries/klemm-2019-chromatin-accessibility-review]]",
  "[[10-Summaries/klemm-2019-chromatin-accessibility-review]]"
]
---

# MNase vs Tn5 — two chemistries for single-cell histone profiling

> Single-cell histone-modification profiling splits cleanly into two chemistry lineages. **MNase-based methods** (Drop-ChIP, scChIC-seq, sortChIC, scChIX-seq, scEpi²-seq) use antibody-tethered micrococcal nuclease to cleave DNA at antibody-bound histone marks ([[10-Summaries/rotem-2015-drop-chip]]; [[10-Summaries/ku-2019-scchic-seq]]; [[10-Summaries/yeung-2023-scchix-seq]]). **Tn5-based methods** (scCUT&Tag, nano-CUT&Tag, sciCUT&Tag, MulTI-Tag, 6-base-CUT&Tag) tether hyperactive Tn5 transposase to antibodies and tagment in situ ([[10-Summaries/bartosovic-2021-sccut-tag]]; [[10-Summaries/bartosovic-2022-nano-cut-tag]]; [[10-Summaries/janssens-2023-scicut-tag]]; [[10-Summaries/tavares-2026-6-base-cut-tag]]). The two chemistries answer the same biological question — *which histone marks are present at which loci in which cells?* — but trade off **resolution, throughput, multiplexing, and modality compatibility** in different ways.

## The two chemistries

### MNase-tethered cleavage (Drop-ChIP → scChIC → sortChIC → scChIX → scEpi²)

The mechanism: a fusion protein of Protein A and micrococcal nuclease (pA-MNase) is targeted to antibody-bound nucleosomes; the MNase is activated by Ca²⁺ and digests exposed linker DNA flanking the bound nucleosome ([[10-Summaries/ku-2019-scchic-seq]]). Released nucleosomal fragments are recovered and sequenced.

Key properties:
- **Reads nucleosome-protected fragments** (~147 bp ± linker) — preserves nucleosome positioning information natively ([[10-Summaries/ku-2019-scchic-seq]]).
- **In-droplet or FACS-sorted single-cell compatibility** — Drop-ChIP via microfluidic encapsulation ([[10-Summaries/rotem-2015-drop-chip]]); scChIC-seq via sorted plates; sortChIC via FACS-integrated protocol; scEpi²-seq combines sortChIC with TAPS for joint mark + methylation ([[10-Summaries/geisenberger-2025-scepi2-seq]]).
- **Multi-mark deconvolution possible** — scChIX-seq incubates with two antibodies simultaneously, deconvolutes the mixed signal computationally to read two marks per cell ([[10-Summaries/yeung-2023-scchix-seq]]).
- **Throughput typically lower** than Tn5 — ~1k-10k cells per experiment for sortChIC; Drop-ChIP achieved ~10⁴ cells but at very low coverage per cell ([[10-Summaries/rotem-2015-drop-chip]]).

### Tn5-tethered tagmentation (CUT&Tag → scCUT&Tag → sciCUT&Tag → MulTI-Tag → 6-base-CUT&Tag)

The mechanism: a fusion of Protein A and hyperactive Tn5 transposase (pA-Tn5) loaded with sequencing adapters is targeted to antibody-bound chromatin; tagmentation inserts adapters in situ around the bound site without prior DNA fragmentation ([[10-Summaries/bartosovic-2021-sccut-tag]]).

Key properties:
- **Tagmented fragments include flanking adapter sequences immediately** — no separate library-prep step required, so per-cell library complexity is preserved ([[10-Summaries/bartosovic-2021-sccut-tag]]).
- **Compatible with droplet and combinatorial-indexing platforms** — scCUT&Tag on 10x Genomics ([[10-Summaries/bartosovic-2021-sccut-tag]]); sciCUT&Tag scales to 40k cells/chip via combinatorial indexing ([[10-Summaries/janssens-2023-scicut-tag]]).
- **Multi-mark per cell via different chemistries** — nano-CUT&Tag uses nanobodies for multi-epitope detection ([[10-Summaries/bartosovic-2022-nano-cut-tag]]); MulTI-Tag uses orthogonal Tn5 variants ([[10-Summaries/janssens-2023-scicut-tag]]); 6-base-CUT&Tag adds enzymatic 5mC/5hmC discrimination on the same fragments ([[10-Summaries/tavares-2026-6-base-cut-tag]]).
- **Throughput typically higher** — sciCUT&Tag ~40k cells/run; commercial 10x scCUT&Tag at thousands of cells routinely.

## Quantitative comparison

| Property | MNase-based | Tn5-based |
|---|---|---|
| Mechanism | Cleavage of accessible linker | Adapter insertion at bound sites |
| Fragment characteristics | Nucleosome-positioned ~147 bp | Variable, includes inter-nucleosomal regions |
| Nucleosome positioning fidelity | High (preserves boundaries) | Lower (Tn5 inserts within nucleosomes too) |
| Cells per experiment (best case) | ~10⁴ (Drop-ChIP, low coverage) / ~10³ (sortChIC, higher quality) | ~40k (sciCUT&Tag) / ~10⁴ (10x scCUT&Tag) |
| Peaks per cell at standard depth | ~hundreds-low thousands | ~1-2k (scCUT&Tag) |
| Multi-mark per cell? | scChIX deconvolutes 2 marks ([[10-Summaries/yeung-2023-scchix-seq]]) | MulTI-Tag, nano-CUT&Tag multiplex via epitope variants |
| Joint with methylation? | scEpi²-seq via TAPS ([[10-Summaries/geisenberger-2025-scepi2-seq]]) | 6-base-CUT&Tag via enzymatic 5mC/5hmC ([[10-Summaries/tavares-2026-6-base-cut-tag]]) |
| Bulk reference assay | ChIP-seq, ChIC-seq, CUT&RUN | CUT&Tag (Henikoff lab) |
| Sequence bias | MNase A/T preference | Tn5 GC preference ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]) |
| Compatible with FFPE? | Limited | Improving |

## What each chemistry is for

### MNase wins when:

- **Nucleosome positioning** is the readout — MNase cleavage cleanly delimits nucleosome boundaries ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]). Tn5 can insert *within* nucleosomes, smearing this information.
- **Multi-mark deconvolution from one library** — scChIX-seq's two-antibody mixing approach has no Tn5 equivalent ([[10-Summaries/yeung-2023-scchix-seq]]).
- **Joint with TAPS methylation** at the chromatin-fragment level — scEpi²-seq ([[10-Summaries/geisenberger-2025-scepi2-seq]]).

### Tn5 wins when:

- **Throughput at >10k cells** is required — sciCUT&Tag delivers 40k cells/run; sortChIC tops out an order of magnitude below ([[10-Summaries/janssens-2023-scicut-tag]]).
- **Droplet integration** with commercial 10x platforms — scCUT&Tag is the routine standard ([[10-Summaries/bartosovic-2021-sccut-tag]]).
- **Joint with scATAC**, scRNA, or surface protein on commercial multi-omic kits — Tn5-based methods plug into the 10x ecosystem; MNase-based methods do not ([[10-Summaries/bartosovic-2022-nano-cut-tag]]).
- **Multi-modal histone + DNA modification per fragment** — 6-base-CUT&Tag reads 5mC + 5hmC + histone mark on the same fragment ([[10-Summaries/tavares-2026-6-base-cut-tag]]). MNase + bisulfite would require separate libraries.

## Common limitations

Both chemistries share unsolved problems:

- **Per-cell sensitivity is the recurring bottleneck** — single cells contain only ~30 copies of each histone-marked region; antibody binding kinetics and enzyme efficiency limit recovery ([[10-Summaries/bartosovic-2021-sccut-tag]]). Both chemistries yield ~hundreds to low thousands of peaks per cell vs ~24k peaks in bulk pooled ([[10-Summaries/bartosovic-2021-sccut-tag]]).
- **Antibody specificity** is the upstream signal-quality determinant, identical for both chemistries.
- **Marks with low genomic abundance** (H3K9ac, H3K27me2) are harder to recover in single cells regardless of chemistry.

## The current frontier

Recent developments suggest the two chemistry lineages are **converging on multi-modal capability**:

- 6-base-CUT&Tag (Tn5 side) — fragment-level histone mark + 5mC + 5hmC ([[10-Summaries/tavares-2026-6-base-cut-tag]]).
- scEpi²-seq (MNase side) — chromatin mark + DNA methylation at single-cell scale via sortChIC + TAPS ([[10-Summaries/geisenberger-2025-scepi2-seq]]).
- scChIX-seq (MNase side) — two histone marks per cell via deconvolution ([[10-Summaries/yeung-2023-scchix-seq]]).
- nano-CUT&Tag (Tn5 side) — multi-epitope per cell via nanobody scaffold ([[10-Summaries/bartosovic-2022-nano-cut-tag]]).

Each lineage is trying to read more layers per cell. The chemistry choice has consequences for *which* additional layer is accessible (methylation via TAPS pairs more naturally with MNase; methylation via enzymatic 5mC/5hmC pairs with Tn5; droplet multi-omics is Tn5-only).

## Choice heuristic for researchers

For a histone-mark experiment in 2026, the chemistry choice should follow the *secondary* measurement requirement:

| Secondary requirement | Preferred chemistry | Example |
|---|---|---|
| None — single mark, max cells | Tn5 (sciCUT&Tag) | [[10-Summaries/janssens-2023-scicut-tag]] |
| Two histone marks per cell | MNase (scChIX-seq) | [[10-Summaries/yeung-2023-scchix-seq]] |
| Histone + DNA methylation per fragment | Tn5 (6-base-CUT&Tag) | [[10-Summaries/tavares-2026-6-base-cut-tag]] |
| Histone + accessibility + RNA on 10x | Tn5 (scCUT&Tag + Multiome) | [[10-Summaries/bartosovic-2022-nano-cut-tag]] |
| Multi-epitope per cell | Tn5 (nano-CUT&Tag, MulTI-Tag) | [[10-Summaries/bartosovic-2022-nano-cut-tag]]; [[10-Summaries/janssens-2023-scicut-tag]] |
| Joint with TAPS methylation | MNase (scEpi²-seq) | [[10-Summaries/geisenberger-2025-scepi2-seq]] |
| Nucleosome positioning fidelity | MNase | [[10-Summaries/ku-2019-scchic-seq]] |

The decision is rarely about MNase vs Tn5 in isolation; it is about which *second* readout the experiment needs.

## How this fits the wider regulatory-layers picture

Histone modifications are one of the four molecular regulatory layers ([[50-Notes/regulatory-layers-overview]]). The MNase/Tn5 chemistry choice determines which of the other three layers (methylation, accessibility, RNA) can be co-measured in the same cell:

- **MNase chemistries pair more naturally with methylation** (TAPS-based scEpi²-seq).
- **Tn5 chemistries pair more naturally with accessibility/RNA** (10x Multiome ecosystem) and **with enzymatic 5mC/5hmC** (6-base-CUT&Tag).

Neither chemistry yet reads all four layers per cell at scale. The closest is 6-base-CUT&Tag (histone + 5mC + 5hmC per fragment, bulk) and scEpi²-seq (histone + 5mC per cell, sorted plates) — neither at droplet-scale.

## Related

- [[40-Topics/histone-modifications]] · [[40-Topics/chromatin-architecture]] · [[40-Topics/single-cell-multiomics]]
- [[40-Topics/histone-modifications]] · [[30-Concepts/cut-and-tag]] · [[30-Concepts/cut-and-run]] · [[30-Concepts/chic-seq]]
- [[30-Concepts/scchic-seq]] · [[30-Concepts/scchix-seq]] · [[30-Concepts/scicut-tag]] · [[30-Concepts/scepi2-seq]] · [[30-Concepts/6-base-cut-and-tag]] · [[30-Concepts/multi-tag]]
- [[50-Notes/regulatory-layers-overview]] — histone marks as one of four layers
- [[50-Notes/droplet-vs-single-molecule-scdna]] — the parallel scale-vs-depth tradeoff for scDNA-seq
- [[50-Notes/synthesis-targets]] — this note resolves the "MNase vs Tn5" target
