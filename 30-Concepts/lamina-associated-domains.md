---
type: concept
title: Lamina-associated domains (LADs)
aliases: [LAD, LADs, lamina associated domain, fLAD, cLAD, facultative LAD, constitutive LAD]
tags: [nuclear-architecture, heterochromatin, H3K9me3, H3K27me3, lamina, single-cell, DamID]
created: 2026-05-15
updated: 2026-05-15
---

# Lamina-associated domains (LADs)

> **LADs** are large (~0.1–10 Mb) genomic regions that physically contact the **nuclear lamina** — the meshwork of intermediate-filament lamins (LMNA/B1/B2) lining the inner nuclear membrane. They cover roughly 35–40% of the mammalian genome, are gene-poor, A/T-rich, and transcriptionally repressed. Mapped originally by bulk DamID (van Steensel lab); resolved at single-cell level by scDamID (Kind 2015) and scDam&T-seq ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).

## Two flavors

| Type | Definition | Marks | Cell-type behavior |
|---|---|---|---|
| **cLAD (constitutive)** | High contact frequency across most cells of most lineages | H3K9me3 enriched | Stable, A/T-rich gene deserts |
| **fLAD (facultative)** | Cell-type-specific NL contact; variable across cells of same type | H3K27me3 enriched | Dynamic; release from NL ↔ transcriptional activation |

This distinction is **load-bearing**: single-cell analysis ([[10-Summaries/rooijers-2019-scdamt-seq]]) shows that the negative coupling between NL contact and transcription is concentrated in **low-CF fLADs**, not in cLADs. cLADs are inert heterochromatin floors; fLADs are the regulatable, transcription-relevant population.

## Measurement methods

- **DamID-seq** (bulk) — Dam-LMNB1 fusion → m6A at GATC near lamina → DpnI + sequencing.
- **scDamID** — single-cell version; FACS + 384-well; [[10-Summaries/de-luca-2021-scdamid-protocol|protocol]].
- **scDam&T-seq** — adds same-cell transcriptome via IVT linear amplification.
- **TSA-seq** — proximity labeling via biotin-tyramide radicals; orthogonal NL distance readout.
- **Microscopy / FISH** — direct spatial measurement; low-throughput per locus.

## Why locus state at the lamina matters

LAD attachment is one of the three principal axes of the **DNA locus state** framework (alongside genetic state and chromatin-mark state):

- **Genetic axis** — sequence variants, CNV, allelic state.
- **Epigenetic axis** — methylation, histone marks, accessibility.
- **Structural axis** — 3D contact, NL position, and biophysical properties. LADs sit at the intersection of 3D position (peripheral vs interior) and chromatin state (heterochromatic vs euchromatic).

Single-cell experiments collapse this into a measurable question: in a given cell, is this locus *at the lamina or in the nucleoplasm*, and how does that correlate with whether it is transcribed?

## Heterogeneity findings

- ~5–15% of LAD coverage in any given cell differs from the bulk-defined LAD map (Kind 2015) — even constitutive LADs detach stochastically.
- Detachment of fLADs from the NL precedes transcriptional activation; reattachment correlates with repression ([[10-Summaries/rooijers-2019-scdamt-seq]]).
- **Lamin depletion ↑ chromatin conformational heterogeneity** at nearly all genomic separations ([[10-Summaries/mali-2025-conformational-heterogeneity]]), supporting the lamina's role as a structural anchor.

## Related

- [[30-Concepts/nuclear-lamina]] · [[30-Concepts/damid]] · [[30-Concepts/scdamt-seq]] · [[30-Concepts/conformational-heterogeneity]]
- [[30-Concepts/histone-modifications]] (H3K9me3 vs H3K27me3 distinction) · [[30-Concepts/chromatin-compartments]] (B-compartment ≈ LAD)
- Sources: [[10-Summaries/rooijers-2019-scdamt-seq]] · [[10-Summaries/de-luca-2021-scdamid-protocol]] · [[10-Summaries/mali-2025-conformational-heterogeneity]]
