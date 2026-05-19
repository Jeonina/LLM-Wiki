---
type: concept
title: SMRT-Tag
aliases: [single-molecule real-time sequencing by tagmentation]
tags: [PacBio, tagmentation, low-input, Ramani-lab]
created: 2026-05-12
updated: 2026-05-12
---

# SMRT-Tag

> A low-input PacBio HiFi library-preparation method (Nanda et al. 2024) that uses Tn5 transposition with hairpin PacBio adapters to make exonuclease-resistant circular molecules from as little as 40 ng of DNA (~7,000 cells).

## Definition

Tn5 with hairpin-loaded adapters tagments native DNA at low concentrations to generate ≥1 kb fragments. Gap repair (Phusion + Taq ligase) seals the 9-nt Tn5 gaps; exonuclease digestion enriches circularized molecules for PacBio sequencing.

## Why it matters

- ~90–99% reduction in PacBio DNA input requirements.
- Comparable variant-calling and CpG-methylation accuracy to ligation-based PacBio at matched coverage.
- Enables clinical-biopsy-scale PacBio sequencing.

## Examples

- HG002 trio variant calling; CpG methylation against bisulfite reference ([[10-Summaries/abdulhay-2020-samosa]]).

## Related

- [[30-Concepts/samosa-tag]] · [[30-Concepts/samosa]] · [[30-Concepts/pacbio]] · [[30-Concepts/tn5-tagmentation]] · [[40-Topics/long-read-sequencing]]
