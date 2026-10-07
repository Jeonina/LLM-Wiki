---
type: concept
title: NOMe-seq
aliases: [nucleosome occupancy and methylome sequencing, GpC methylation]
tags: [methylation, chromatin-accessibility, GpC, M.CviPI]
created: 2026-05-12
updated: 2026-10-07
---

# NOMe-seq

> Nucleosome Occupancy and Methylome sequencing. Uses the M.CviPI methyltransferase to deposit exogenous 5mC at accessible GpC dinucleotides, then bisulfite sequencing distinguishes endogenous CpG methylation from exogenous GpC methylation (= chromatin accessibility).

## Definition

GpC methylation marks open regions; CpG methylation is the endogenous epigenetic mark. Single read provides both readouts. Single-cell variants: scNOMe-seq, scCOOL-seq, scNMT-seq, [[30-Concepts/splicool-seq]].

## Why it matters

- Single-fiber co-measurement of accessibility and methylation.
- Foundation for the methyltransferase-based accessibility readouts used in [[30-Concepts/samosa]], [[30-Concepts/fiber-seq]] (EcoGII variant), and [[30-Concepts/stam-seq]].

## Added 2026-10-07

scNOMe-seq and scCOOL-seq read GpC methyltransferase footprints plus endogenous CpG methylation after scBS-seq; scCOOL-seq additionally yields CNV and ploidy in preimplantation embryos [[10-Summaries/ludwig-2019-sc-chromatin-modifications-review]]. Camellia-seq adds GpC accessibility to a lineage-barcode + RNA + methylation assay [[10-Summaries/li-2023-darlin]].

ATAC-based alternative: sciMET+ATAC encodes accessibility by Tn5 insertion rather than GpC methylation, avoiding the confound of endogenous non-CG methylation in brain and ESCs and giving enough per-cell accessibility signal for cell-level ATAC analysis ([[10-Summaries/nichols-2025-scimetv3]]).


## Related

- [[40-Topics/dna-methylation]] · [[30-Concepts/chromatin-accessibility]] · [[30-Concepts/splicool-seq]] · [[30-Concepts/fiber-seq]]
