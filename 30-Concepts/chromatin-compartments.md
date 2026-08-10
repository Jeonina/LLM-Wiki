---
type: concept
title: Chromatin compartments
aliases: [A/B compartments]
tags: [3D-genome, Hi-C, chromatin]
created: 2026-05-12
updated: 2026-08-10
---

# Chromatin compartments

> Large (~5–10 Mb) genomic blocks that preferentially associate with each other in 3D space. **A compartments** are gene-rich, transcriptionally active, early-replicating, and enriched for active histone marks. **B compartments** are gene-poor, repressed, late-replicating, and enriched for heterochromatin.

## Definition

Identified by principal-component analysis on Hi-C contact matrices. A and B compartments correspond to the two principal directions of the contact-matrix eigenvector. They can be further subdivided into A1, A2, B1–B4.

## Why it matters

- Compartment identity correlates with replication timing and chromatin state.
- Compartment switching marks cell-fate transitions.
- SnapATAC ([[10-Summaries/fang-2021-snapatac]]) shows that off-peak scATAC-seq reads correlate with A-compartment density — meaning compartment-level signal contributes to single-cell clustering even without explicit peak calls.

## Added 2026-08-10

[[10-Summaries/lieberman-aiden-2009-hic]] is the founding source: normalizing by distance-expected contact reveals a plaid pattern, correlating interaction profiles sharpens it, and PCA on the correlation matrix partitions each chromosome into two compartments with labels consistent genome-wide. Compartment A correlates with gene density (ρ = 0.431), expression (ρ = 0.476) and most strongly DNase I sensitivity (ρ = 0.651), and compartment identity switches between cell types in step with that cell type's own accessibility.

Compartments are now measurable per cell after imputation, with variability that correlates with transcriptional variability in 71% of 50 Mb windows ([[10-Summaries/zhang-2022-higashi]]); their presence or absence is also the discriminator between interphase and mitotic single cells ([[10-Summaries/ramani-2017-scihi-c]]).


## Related

- [[40-Topics/3d-genome]] · [[30-Concepts/topologically-associating-domain]] · [[30-Concepts/replication-timing]] · [[40-Topics/3d-genome]]
