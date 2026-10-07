---
type: concept
title: Tn5 tagmentation
aliases: [Tn5 transposition, tagmentation]
tags: [transposase, library-prep, ATAC-seq]
created: 2026-05-12
updated: 2026-10-07
---

# Tn5 tagmentation

> The simultaneous fragmentation and adapter-ligation of DNA by Tn5 transposase. A hyperactive Tn5 variant loaded with sequencing adapter–containing oligos cuts dsDNA and inserts the adapters in a single enzymatic reaction.

## Definition

Tn5 is an Escherichia coli transposase. Each transposition introduces a 9-nt gap into the target DNA and inserts the loaded adapter at both ends of the resulting fragment. Library prep that takes hours of fragmentation + ligation in conventional workflows takes ~30 minutes with Tn5.

## Why it matters

- Foundation of ATAC-seq (preferentially cuts open chromatin) and many low-input methods.
- Single-cell adaptable: pA-Tn5 enables CUT&Tag; concentration tuning enables size control in SMRT-Tag.
- Limitation: standard Tn5 libraries do not preserve strand pairing for [[40-Topics/duplex-sequencing]], although the Tn5-based META-CS achieves duplex calling in single cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Examples

- [[30-Concepts/atac-seq]], [[30-Concepts/cut-and-tag]], [[30-Concepts/smrt-tag]], [[30-Concepts/scicut-tag]], [[30-Concepts/micro-atac-seq]], [[30-Concepts/splicool-seq]].

## Added 2026-10-07

pA-Tn5's accessibility preference is visible even in targeted CUT&Tag: nearly all H3K27ac CUT&Tag regions fell in H3K27ac sites shared with ATAC peaks, and removing <100-bp fragments reduced H3K27ac reads in ATAC peaks from 29% to 20% [[10-Summaries/abbasova-2025-cut-tag-encode-benchmark]]. Earlier, bulk ChIP vs Tn5-based ChIL-seq correlations for H3K27me3 were only r = 0.26–0.31, versus r = 0.67 for MNase-based scChIC-seq [[10-Summaries/ludwig-2019-sc-chromatin-modifications-review]].

Tn5 can also fragment and barcode proximity-ligated chromatin. Droplet Hi-C runs SDS-treated in situ Hi-C nuclei through the 10x scATAC tagmentation workflow and reports minimal open-chromatin bias in the resulting contact data ([[10-Summaries/chang-2025-droplet-hi-c]]).

CoBATCH pre-assembles PA-Tn5 with well-specific barcoded adapters, so the cell barcode is introduced during antibody-tethered tagmentation itself ([[10-Summaries/wang-2019-cobatch]]). OneCell CUT&Tag uses commercial pA-Tn5 or in-house Nano-Tn5 inside single wells ([[10-Summaries/schwager-2026-onecell-cut-tag]]).

**Two distinct Tn5 biases.** Sequence-level cleavage preference and chromatin-level preference for accessible DNA are separable; the latter confounds antibody-targeted assays such as CUT&Tag and cannot be removed by sequence models alone ([[10-Summaries/hu-2026-patty]]). In sciMETv3, Tn5 loaded with fully methylated adapters is used for methylome indexing, and two sequential tagmentations (native, then after nucleosome disruption) split accessible from total DNA in sciMET+ATAC ([[10-Summaries/nichols-2025-scimetv3]]).

META-CS loads Tn5 with an equimolar mix of 16 transposon sequences, so each fragment carries two random tags. The tags act as fragment barcodes and reduce the amplification loss from intramolecular hairpins that form when both ends carry the same sequence. Strand identity comes from later primer-extension rounds, not from the tagmentation step itself ([[10-Summaries/xing-2021-meta-cs]]).

Tn5 tagmentation of nuclei yields fragments from ~35 bp to several kbp. Standard bead clean-ups, PCR and Illumina sequencing keep only the short ones, which is why ATAC libraries look enriched for open chromatin ([[10-Summaries/pancikova-2025-splongget]]). SPLONGGET retains all fragment sizes, giving DNA libraries of 200 bp to >10 kb that supply whole-genome coverage alongside the ATAC signal. Only reads under 1 kb are used for the accessibility analysis ([[10-Summaries/pancikova-2025-splongget]]).

Two Tn5 loadings with different adapter sets can split one nucleus's genome by chromatin state: in wellDA-seq, Tn5-1 tagments open chromatin in intact permeabilised nuclei, and Tn5-2 tagments the remaining DNA after in-well protease removal of chromatin, with modality-specific PCR separating the ATAC and DNA libraries ([[10-Summaries/wang-2024-wellda-seq]]).

## Related

- [[30-Concepts/atac-seq]] · [[30-Concepts/cut-and-tag]] · [[30-Concepts/smrt-tag]]
