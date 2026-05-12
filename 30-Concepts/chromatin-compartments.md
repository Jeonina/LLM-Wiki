---
type: concept
title: Chromatin compartments
aliases: [A/B compartments]
tags: [3D-genome, Hi-C, chromatin]
created: 2026-05-12
updated: 2026-05-12
---

# Chromatin compartments

> Large (~5–10 Mb) genomic blocks that preferentially associate with each other in 3D space. **A compartments** are gene-rich, transcriptionally active, early-replicating, and enriched for active histone marks. **B compartments** are gene-poor, repressed, late-replicating, and enriched for heterochromatin.

## Definition

Identified by principal-component analysis on Hi-C contact matrices. A and B compartments correspond to the two principal directions of the contact-matrix eigenvector. They can be further subdivided into A1, A2, B1–B4.

## Why it matters

- Compartment identity correlates with replication timing and chromatin state.
- Compartment switching marks cell-fate transitions.
- SnapATAC ([[10-Summaries/comprehensive-analysis-of-single-cell-atac-seq-data-with-snapatac]]) shows that off-peak scATAC-seq reads correlate with A-compartment density — meaning compartment-level signal contributes to single-cell clustering even without explicit peak calls.

## Related

- [[30-Concepts/3d-genome]] · [[30-Concepts/topologically-associating-domain]] · [[30-Concepts/replication-timing]] · [[40-Topics/3d-genome]]
