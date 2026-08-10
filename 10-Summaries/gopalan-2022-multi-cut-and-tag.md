---
type: summary
title: "Gopalan & Fazzio 2022 — Multi-CUT&Tag to simultaneously profile multiple chromatin factors (protocol)"
source: "[[00-Sources/papers/Multi-CUT&Tag to simultaneously profile multiple chromatin factors]]"
source_kind: paper
author: "Sneha Gopalan, Thomas G. Fazzio (corresponding)"
published: 2022
ingested: 2026-08-10
doi: "10.1016/j.xpro.2021.101100"
journal: "STAR Protocols"
tags: [Multi-CUT&Tag, barcoded-adapters, co-localization, protocol, multi-epitope, pA-Tn5, single-cell]
entities: []
concepts: ["[[multi-tag]]", "[[cut-and-tag]]", "[[tn5-tagmentation]]", "[[scchix-seq]]"]
topics: ["[[histone-modifications]]"]
---

**Citation:** Gopalan, S. & Fazzio, T. G. (2022) — *Multi-CUT&Tag to simultaneously profile multiple chromatin factors* — *STAR Protocols* 3, 101100. [DOI](https://doi.org/10.1016/j.xpro.2021.101100)

# Gopalan 2022 — Multi-CUT&Tag protocol

> The step-by-step protocol for the one modification that turns CUT&Tag from a one-target assay into a combinatorial one: **load pA-Tn5 with a different barcoded adapter for each antibody**, pre-conjugate antibody to its own barcoded transposome, then run them all in the same cells. Each read carries the identity of the epitope that placed it, so co-localization of different chromatin proteins at the same locus is read directly rather than inferred by overlaying separate experiments.

> ⚠️ **Source note.** This is the *STAR Protocols* companion to the primary paper — Gopalan, Wang, Harper, Garber & Fazzio, *Simultaneous profiling of multiple chromatin proteins in the same cells*, **Molecular Cell** 81, 4736–4746.e5 (2021). The primary paper carries the biological results and is **not currently bookmarked**; this clipping covers the front matter and the pA-Tn5 expression/purification and adapter-loading sections.

## Key claims

- Multi-CUT&Tag maps multiple chromatin proteins **in the same cells**, and — the stated advantage over parallel single-target runs — **directly detects co-localization of different epitopes at the same loci**.
- The method "is easily adapted for single-cell chromatin mapping."
- Validated antibody set: **H3K27me3, H3K27ac, and RNAPII phospho-Ser2**, in various combinations. That trio is chosen well — a repressive mark, an active-enhancer mark, and elongating polymerase — so the assay can ask whether repression and activation coincide on the same molecules.
- Demonstrated in mouse embryonic stem cells and trophoblast stem cells; expected to work across mammalian cells as CUT&Tag does.
- Prerequisites, in order: express and purify His-tagged pA-Tn5 in *E. coli*; prepare 5% digitonin; **load pA-Tn5 with adapters carrying a distinct barcode per antibody**; pre-form antibody–pA-Tn5 conjugates and remove unbound antibody and adapter.
- Purification detail from the protocol: TALON/His affinity, then — if purity is below ~70% by SDS-PAGE — a Q-Sepharose flow-through step followed by SP-Sepharose binding and HN₈₀₀TE elution. Final preparation 1.55 µg/µL (21.1 µM). Enzyme production alone is a **4-day** procedure.

## Methods / evidence

A protocol, so its weight is procedural rather than evidentiary. Two details are load-bearing for anyone judging feasibility:

1. **Pre-conjugation with washing away of unbound antibody and adapter is essential** — without it, barcodes would exchange between transposomes and epitope assignment would be meaningless. The barcode-to-epitope mapping is only as good as that purification step.
2. **Home-made pA-Tn5 is a hard requirement.** Commercial pA-Tn5 comes preloaded with standard adapters. Any lab wanting Multi-CUT&Tag must run a four-day protein prep with ion-exchange polishing — a real adoption barrier that partly explains why barcoded multi-epitope CUT&Tag has not displaced single-target scCUT&Tag.

## Surprising or load-bearing bits

- **This is the assay class that can actually test bivalency per molecule.** [[bernstein-2006-bivalent-chromatin|Bernstein 2006]] used sequential ChIP to show H3K4me3 and H3K27me3 on the same chromatin; [[rothbart-2014-histone-dna-language|Rothbart & Strahl]] report they sit on *adjacent histones within one nucleosome*. Barcoded co-tagmentation is the single-cell descendant of sequential ChIP — and the H3K27me3/H3K27ac pairing tested here is the closest available analogue of that question.
- Contrast with the computational alternative: [[zhang-2022-sccut-tag-pro|scCUT&Tag-pro]] *interpolates* six marks per cell and states plainly that its profiles "cannot be used to detect associations between multiple histone modifications within the same cell." Multi-CUT&Tag can, at the cost of fewer targets and much harder wet-lab work. **That is the real trade in this corner of the field**, and it is worth stating explicitly in a methods review.
- Only three antibodies are validated. Multiplexing depth here is 2–3 epitopes, not the six that scChromHMM assembles computationally.
- Direct realization of the closing prediction in [[kaya-okur-2019-cut-and-tag]]: "barcoding of adapters will allow for multiple epitopes to be simultaneously profiled in single cells."

## Concepts touched

- [[multi-tag]] — this is the protocol-level source; barcoded-adapter multiplexing is the defining mechanism.
- [[scchix-seq]] — the alternative route to two marks per cell (antibody-conjugate splitting plus computational deconvolution) rather than barcoded adapters.
- [[tn5-tagmentation]] — barcode loading is a property of the transposome, so multiplexing is free of extra reaction steps once conjugates exist.

## Connections to other sources

- Downstream of [[kaya-okur-2019-cut-and-tag]]; the multi-epitope branch of the CUT&Tag family alongside [[wu-2021-sccut-tag]] and [[zhang-2022-sccut-tag-pro]].
- [[yeung-2023-scchix-seq]] solves the same problem by a different mechanism; [[bartosovic-2022-nano-cut-tag]] adds a transcriptome instead of a second mark.
- The nuclease-based counterpart discussion lives at [[mnase-vs-tn5-chromatin]].
- Named as an existing method in [[heinz-2010-homer]]'s open-question about single-cell collaborative binding.

## Open questions

- **The primary Molecular Cell paper is not in this corpus** — co-localization statistics, single-cell demonstration data, and any bivalency result live there. Bookmarking it would close the largest gap this ingest exposed on the histone-modification side.
- How many epitopes can be barcoded before signal per target becomes unusable in single cells? Not addressed in the protocol.
- Whether antibody–transposome pre-conjugation biases which epitopes are accessible in dense chromatin — untested here.

## Related

- [[multi-tag]] · [[kaya-okur-2019-cut-and-tag]] · [[zhang-2022-sccut-tag-pro]] · [[mnase-vs-tn5-chromatin]]
