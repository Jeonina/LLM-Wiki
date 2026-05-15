---
type: concept
title: DamID
aliases: [DNA adenine methyltransferase identification, scDamID]
tags: [protein-DNA-contact, m6A, GATC, DpnI, lamina, single-cell]
created: 2026-05-15
updated: 2026-05-15
---

# DamID (DNA adenine methyltransferase identification)

> **DamID** maps protein–DNA contacts by fusing a protein of interest (POI) to *E. coli* DNA adenine methyltransferase (Dam) and reading the m6A footprint the fusion leaves at nearby GATC sites. The signal is *cumulative* (Dam keeps depositing methyl marks while expressed, integrating contact history over hours) and *amplifiable* (methylation-sensitive enzymes — DpnI cuts m6A-GATC, MboI cuts unmethylated GATC — discriminate marked from unmarked fragments). Invented by [[20-Entities/jop-kind|Kind]] and Bas van Steensel (van Steensel 2000) and adapted to single cells in Kind 2013/2015.

## Mechanism

1. Express Dam–POI fusion (transient transfection or stable clone, with degron/inducible promoter for temporal control).
2. Dam methylates adenine of GATC motifs that come close to the POI in vivo → m6A-GATC.
3. Extract gDNA → digest with DpnI (cuts m6A-GATC only) → ligate universal adapter to blunt ends → PCR (or T7-IVT linear amplification) → sequence.
4. Untethered Dam is run in parallel as the accessibility-baseline control.

## Why it matters

- **No crosslinking, no antibody.** Avoids ChIP's two biggest failure modes (low-abundance protein detection, antibody specificity). Works on any protein you can fuse to Dam.
- **Single-cell compatible.** Cumulative methylation accumulates enough signal per cell for 96-well-plate workflows; scDamID was the first practical single-cell genome–lamina mapping method.
- **Multi-omic linear amplification.** Replacing PCR with T7-IVT (Rooijers 2019) enables co-amplification of cDNA and gDNA — backbone of [[30-Concepts/scdamt-seq|scDam&T-seq]].

## Variants

- **Bulk DamID / DamID-seq** — population-scale, ChIP-seq-equivalent throughput.
- **scDamID** — single-cell, FACS + 384-well; Kind 2015, [[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021 protocol]].
- **scDam&T-seq** — joint scDamID + CEL-Seq2 mRNA in one well; Rooijers 2019.
- **CATaDa** — chromatin accessibility via untethered Dam (Aughey 2018).
- **TaDa** — tissue-specific DamID in *Drosophila* via GAL4-UAS.

## Targets exemplified

- LMNB1 — lamina contacts ([[30-Concepts/lamina-associated-domains|LADs]])
- RING1B (RNF2) — Polycomb-repressive complex 1
- CTCF, transcription factors, polymerase subunits — any Dam-tetherable protein

## Comparison to alternatives

| Method | Antibody | Crosslink | Single-cell | Time resolution | Signal | Coverage |
|---|---|---|---|---|---|---|
| ChIP-seq | Required | Yes | Hard (scChIP) | Instant | Antibody-dep. | Genome-wide |
| ATAC-seq | No | No | Yes (scATAC) | Instant | Tn5 cuts | Accessible only |
| DamID | No | No | Yes (scDamID) | Cumulative (hours) | m6A footprint | Genome-wide |

## Related

- [[30-Concepts/scdamt-seq]] · [[30-Concepts/lamina-associated-domains]] · [[30-Concepts/nuclear-lamina]] · [[30-Concepts/chromatin-accessibility]] · [[30-Concepts/single-cell-multiomics]]
- Sources: [[10-Summaries/rooijers-2019-scdamt-seq]] · [[10-Summaries/de-luca-2021-scdamid-protocol]] · [[10-Summaries/mali-2025-conformational-heterogeneity]]
