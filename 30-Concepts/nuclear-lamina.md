---
type: concept
title: Nuclear lamina
aliases: [NL, lamina, nuclear envelope lamina, lamin meshwork]
tags: [nuclear-architecture, lamin, LMNB1, LMNA, laminopathy, peripheral-heterochromatin]
created: 2026-05-15
updated: 2026-05-15
---

# Nuclear lamina

> The **nuclear lamina** is a dense meshwork of intermediate-filament proteins — A-type (LMNA, LMNC) and B-type (LMNB1, LMNB2) lamins plus associated proteins (LBR, BAF, emerin, LAP2β, LEM-domain proteins) — that lines the inner nuclear membrane. It provides mechanical support to the nucleus, anchors heterochromatin to the periphery via [[30-Concepts/lamina-associated-domains|LADs]], and is a node in mechanotransduction.

## Functional roles

- **Mechanical scaffold**: lamin stiffness determines nuclear shape and resists mechanical stress; LMNA mutations cause progerin (HGPS) and other laminopathies.
- **Genome organizer**: tethers transcriptionally repressed chromatin (cLADs especially) to the periphery; loss of lamina integrity de-compartmentalizes the genome.
- **Spatial gene regulation**: peripheral position correlates with repression for many genes, but causality is partial — release from NL is *permissive*, not sufficient, for activation ([[10-Summaries/rooijers-2019-scdamt-seq]]).
- **Mechanotransduction**: lamin-A links cytoskeletal force (LINC complex) to chromatin organization.

## Genome–lamina contacts as locus state

The genome–NL contact axis is one of the three pillars of **DNA locus state** (alongside sequence/genetic and chromatin-mark/epigenetic states):

- *Peripheral position* ≈ B-compartment ≈ heterochromatin ≈ low transcription.
- *Interior position* ≈ A-compartment ≈ euchromatin ≈ active transcription.

But this association is statistical, not deterministic; the cell-to-cell variability of NL contact at fLADs is what scDamID and scDam&T-seq are designed to measure.

## Lamin depletion phenotypes

- Loss of chromosome territories (Ulianov 2019, mammals; Bondarenko 2020, fly).
- Increased chromatin **conformational heterogeneity** at nearly all genomic separations ([[10-Summaries/mali-2025-conformational-heterogeneity]]).
- Predicted transcriptional noise increase — testable via scDam&T-seq or scNMT-seq in lamin-knockdown vs WT.
- Disease consequence: muscular dystrophies, neuropathies, premature aging (HGPS), lipodystrophies — laminopathies.

## Measurement

- **DamID** (Dam-LMNB1) — genome–NL contact mapping. [[30-Concepts/damid]]
- **scDamID / scDam&T-seq** — single-cell variants.
- **TSA-seq** — proximity-labeling via tyramide radicals; gives continuous NL distance, not just binary contact.
- **ChIP-seq for lamins** — bulk version; limited by lamin epitope accessibility.
- **Microscopy / 3D-FISH** — direct spatial measurement.

## Related

- [[30-Concepts/lamina-associated-domains]] · [[30-Concepts/damid]] · [[30-Concepts/scdamt-seq]] · [[30-Concepts/conformational-heterogeneity]]
- [[30-Concepts/chromatin-compartments]] · [[40-Topics/3d-genome]]
- Sources: [[10-Summaries/rooijers-2019-scdamt-seq]] · [[10-Summaries/de-luca-2021-scdamid-protocol]] · [[10-Summaries/mali-2025-conformational-heterogeneity]]
