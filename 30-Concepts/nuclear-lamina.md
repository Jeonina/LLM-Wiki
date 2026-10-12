---
type: concept
title: Nuclear lamina
aliases: [NL, lamina, nuclear envelope lamina, lamin meshwork]
tags: [nuclear-architecture, lamin, LMNB1, LMNA, laminopathy, peripheral-heterochromatin]
created: 2026-05-15
updated: 2026-10-12
---

# Nuclear lamina

> The **nuclear lamina** is a dense meshwork of intermediate-filament proteins — A-type (LMNA, LMNC) and B-type (LMNB1, LMNB2) lamins plus associated proteins (LBR, BAF, emerin, LAP2β, LEM-domain proteins) — that lines the inner nuclear membrane. It provides mechanical support to the nucleus, anchors heterochromatin to the periphery via [[30-Concepts/lamina-associated-domains|LADs]], and is a node in mechanotransduction.

> [!abstract] 한눈에
> Nuclear lamina는 내핵막 안쪽을 덮는 lamin 단백질 그물망으로, 핵을 기계적으로 지지하고 억제된 chromatin(LAD)을 핵 가장자리에 붙잡아 둔다. 가장자리 위치와 전사 억제의 관계는 통계적 연관일 뿐이고, 단일세포에서는 그 결합이 facultative LAD(fLAD)에만 한정된다 ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).

## Definition

The genome–NL contact axis is one of the three pillars of **DNA locus state** (alongside sequence/genetic and chromatin-mark/epigenetic states) (synthesis):

- *Peripheral position* ≈ B-compartment ≈ heterochromatin ≈ low transcription.
- *Interior position* ≈ A-compartment ≈ euchromatin ≈ active transcription.

But this association is statistical, not deterministic; the cell-to-cell variability of NL contact at fLADs is what scDamID and scDam&T-seq are designed to measure ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]; [[10-Summaries/de-luca-2021-scdamid-protocol|de Luca 2021]]).

## Why it matters

- **Mechanical scaffold**: lamin stiffness determines nuclear shape and resists mechanical stress; LMNA mutations cause progerin (HGPS) and other laminopathies.
- **Genome organizer**: tethers transcriptionally repressed chromatin (cLADs especially) to the periphery; loss of lamina integrity de-compartmentalizes the genome.
- **Spatial gene regulation**: peripheral position correlates with repression for many genes, but the single-cell lamina–transcription coupling is an association, restricted to facultative LADs (fLADs) rather than constitutive cLADs ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).
- **Mechanotransduction**: lamin-A links cytoskeletal force (LINC complex) to chromatin organization.

## Measurement

| Method | What it gives | Source |
|---|---|---|
| [[30-Concepts/damid\|DamID]] (Dam-LMNB1) | Genome–NL contact mapping | — |
| scDamID / scDam&T-seq | Single-cell variants; scDam&T-seq adds the transcriptome of the same cell | ([[10-Summaries/de-luca-2021-scdamid-protocol\|de Luca 2021]]; [[10-Summaries/rooijers-2019-scdamt-seq\|Rooijers 2019]]) |
| TSA-seq | Proximity-labeling via tyramide radicals; gives continuous NL distance, not just binary contact | — |
| ChIP-seq for lamins | Bulk version; limited by lamin epitope accessibility | — |
| Microscopy / 3D-FISH | Direct spatial measurement | — |

## Lamina contacts and compartments

- Hi-C subcompartments differ in lamina association: B2 is enriched at the nuclear lamina (1.8×) and at NADs (4.6×), B3 is lamina-enriched (1.6×) but strongly NAD-depleted (76×), and A1/A2 are depleted at the lamina ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).
- Nucleolar hubs detected by SPRITE are largely inter-chromosomal, unlike lamina contacts ([[10-Summaries/bersaglieri-2019-cells|Bersaglieri 2019]]).

## Evidence and examples

Lamin depletion phenotypes:

- Loss of chromosome territories (Ulianov 2019, mammals; Bondarenko 2020, fly).
- Increased chromatin **conformational heterogeneity** at nearly all genomic separations ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).
- Predicted transcriptional noise increase — testable via scDam&T-seq or scNMT-seq in lamin-knockdown vs WT ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).
- Disease consequence: muscular dystrophies, neuropathies, premature aging (HGPS), lipodystrophies — laminopathies.

## Open questions

- **NAD placement in B subcompartments.** A review places 74% of NADs in B2/B3 heterochromatin, while Rao 2014 reports B3 as strongly NAD-depleted and B2 NAD-enriched; the figures agree only if most NADs fall in B2 ([[10-Summaries/bersaglieri-2019-cells|Bersaglieri 2019]]; [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/lamina-associated-domains|Lamina-associated domains (LADs)]] — Genome regions in contact with the lamina.
> - `concept` [[30-Concepts/damid|DamID]] — Dam-fusion methylation mapping of protein–DNA contacts.
> - `concept` [[30-Concepts/scdamt-seq|scDam&T-seq]] — Joint single-cell lamina contacts and transcriptome.
> - `concept` [[30-Concepts/conformational-heterogeneity|Conformational heterogeneity]] — Cell-to-cell variability metric that rises on lamin depletion.
> - `concept` [[30-Concepts/chromatin-compartments|Chromatin compartments]] — A/B compartments and their subcompartments.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromatin folding, compartments and contacts.

## All sources on this page

> [!info]- 5 summaries cited here
> - [[10-Summaries/bersaglieri-2019-cells|Bersaglieri & Santoro 2019]]
> - [[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]
> - [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]
> - [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]
> - [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]
