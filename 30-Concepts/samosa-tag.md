---
type: concept
title: SAMOSA-Tag
aliases: [SAMOSA by tagmentation]
tags: [PacBio, chromatin-accessibility, single-fiber, EcoGII, Ramani-lab]
created: 2026-05-12
updated: 2026-05-12
---

# SAMOSA-Tag

> A low-input single-molecule chromatin-accessibility method (Nanda et al. 2024) combining in-nucleus EcoGII methyltransferase footprinting (6mA marks accessible regions) with SMRT-Tag library preparation. Detects sequence + 5mC (CpG) + 6mA (accessibility) on the same PacBio fiber from 30k–50k nuclei.

## Definition

In-nucleus EcoGII methylation → SMRT-Tag tagmentation → PacBio HiFi sequencing. PacBio polymerase kinetics distinguish endogenous 5mC from exogenous 6mA, enabling multi-modal single-fiber readout.

## Why it matters

- Brings the [[30-Concepts/samosa]] single-molecule chromatin assay within reach of clinical samples (PDXs, biopsies).
- Resolves single-fiber CTCF binding and nucleosome positioning at the same loci where CpG methylation is also measured.
- Applied to prostate-cancer PDXs to reveal metastasis-associated global chromatin disorganization invisible to bulk ATAC-seq.

## Related

- [[30-Concepts/samosa]] · [[30-Concepts/smrt-tag]] · [[30-Concepts/fiber-seq]] · [[30-Concepts/single-molecule-footprinting]] · [[40-Topics/long-read-sequencing]] · [[20-Entities/vijay-ramani]]
