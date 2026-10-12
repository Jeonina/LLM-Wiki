---
type: concept
title: DamID
aliases: [DNA adenine methyltransferase identification, scDamID]
tags: [protein-DNA-contact, m6A, GATC, DpnI, lamina, single-cell]
created: 2026-05-15
updated: 2026-10-12
---

# DamID (DNA adenine methyltransferase identification)

> **DamID** maps protein–DNA contacts by fusing a protein of interest (POI) to *E. coli* DNA adenine methyltransferase (Dam) and reading the m6A footprint the fusion leaves at nearby GATC sites; the signal is *cumulative*, integrating contact history over hours ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]).

> [!abstract] 한눈에
> DamID는 단백질에 Dam을 붙여 그 단백질 가까이의 GATC에 m6A 흔적을 남기고, 이를 DpnI로 잘라 읽는 방법이다. 항체와 crosslinking이 필요 없고 methylation이 시간에 따라 쌓이기 때문에 single cell에서도 신호가 충분하다 ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]; [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).

## Definition

The signal is *cumulative* (Dam keeps depositing methyl marks while expressed, integrating contact history over hours) and *amplifiable* (methylation-sensitive enzymes — DpnI cuts m6A-GATC, MboI cuts unmethylated GATC — discriminate marked from unmarked fragments) ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]). DamID was invented by Bas van Steensel (van Steensel 2000) and adapted to single cells by [[20-Entities/jop-kind|Kind]] in Kind 2013/2015 ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]; [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).

**Mechanism** ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]):

1. Express Dam–POI fusion (transient transfection or stable clone, with degron/inducible promoter for temporal control).
2. Dam methylates adenine of GATC motifs that come close to the POI in vivo → m6A-GATC.
3. Extract gDNA → digest with DpnI (cuts m6A-GATC only) → ligate universal adapter to blunt ends → PCR (or T7-IVT linear amplification) → sequence.
4. Untethered Dam is run in parallel as the accessibility-baseline control.

## Why it matters

- **No crosslinking, no antibody.** Avoids ChIP's two biggest failure modes (low-abundance protein detection, antibody specificity). Works on any protein you can fuse to Dam ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]).
- **Single-cell compatible.** Cumulative methylation accumulates enough signal per cell for 96-well-plate workflows; scDamID was the first practical single-cell genome–lamina mapping method ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]).
- **Multi-omic linear amplification.** Replacing PCR with T7-IVT (Rooijers 2019) enables co-amplification of cDNA and gDNA — backbone of [[30-Concepts/scdamt-seq|scDam&T-seq]] ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).

## Variants

| Variant | Scale | What it adds | Source |
|---|---|---|---|
| Bulk DamID / DamID-seq | Population | ChIP-seq-equivalent throughput | — |
| scDamID | Single cell, FACS + 384-well | Kind 2015; standard bench protocol | ([[10-Summaries/de-luca-2021-scdamid-protocol\|de Luca & Kind 2021 protocol]]) |
| [[30-Concepts/scdamt-seq\|scDam&T-seq]] | Single cell | Joint scDamID + CEL-Seq2 mRNA in one well | ([[10-Summaries/rooijers-2019-scdamt-seq\|Rooijers 2019]]) |
| CATaDa | — | Chromatin accessibility via untethered Dam (Aughey 2018) | — |
| TaDa | *Drosophila* tissue | Tissue-specific DamID via GAL4-UAS | — |

**Targets exemplified**

- LMNB1 — lamina contacts ([[30-Concepts/lamina-associated-domains|LADs]]); bulk lamina-DamID served, with bulk Hi-C, as training data for 3D chromosome models ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).
- RING1B (RNF2) — Polycomb-repressive complex 1 ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).
- CTCF, transcription factors, polymerase subunits — any Dam-tetherable protein ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]).

**Comparison to alternatives**

| Method | Antibody | Crosslink | Single-cell | Time resolution | Signal | Coverage |
|---|---|---|---|---|---|---|
| ChIP-seq | Required | Yes | Hard (scChIP) | Instant | Antibody-dep. | Genome-wide |
| ATAC-seq | No | No | Yes (scATAC) | Instant | Tn5 cuts | Accessible only |
| DamID | No | No | Yes (scDamID) | Cumulative (hours) | m6A footprint | Genome-wide |

## Evidence and examples

- Later tethered-enzyme methods position themselves against DamID's GATC-limited resolution: CUT&RUN uses antibody-tethered MNase with near base-pair footprints ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]), and DeChIC-seq uses an antibody-tethered deaminase whose TC-context edits survive WGA for single-cell use ([[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]).
- In a TRIP reporter test, Borzoi's sequence-based DNase predictions at insertion sites correlated with reporter expression (Spearman R = 0.58 for ARHGEF9) better than LMNB1 DamID, which the authors treat as a strong position-effect baseline ([[10-Summaries/linder-2025-borzoi|Borzoi]]).

## Contested points

- **Resolution vs antibody-free design.** DamID avoids antibodies and crosslinking ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]) but is limited to GATC sites, which antibody-tethered methods cite as their advantage ([[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]; [[10-Summaries/shi-2026-dechic-seq|DeChIC-seq]]) (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scdamt-seq|scDam&T-seq]] — Joint single-cell DamID and transcriptome in one well.
> - `concept` [[30-Concepts/lamina-associated-domains|Lamina-associated domains]] — The lamina contacts mapped by Dam-LMNB1.
> - `concept` [[30-Concepts/nuclear-lamina|Nuclear lamina]] — The nuclear-periphery structure DamID most often maps against.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Measured by untethered Dam as the baseline control.
> - `entity` [[20-Entities/jop-kind|Jop Kind]] — Developer of single-cell DamID.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Joint measurement of several layers in the same cell.

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]
> - [[10-Summaries/linder-2025-borzoi|Borzoi 2025]]
> - [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]
> - [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]
> - [[10-Summaries/shi-2026-dechic-seq|Shi 2026]]
> - [[10-Summaries/skene-2017-cut-and-run|Skene & Henikoff 2017]]
