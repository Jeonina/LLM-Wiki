---
type: concept
title: Spatial Structure Capture Efficiency (SSCE)
aliases: [SSCE]
tags: [3D-genome, quality-control, single-cell-Hi-C, metric]
created: 2026-05-12
updated: 2026-05-12
---

# Spatial Structure Capture Efficiency (SSCE)

> A single-cell 3D-genome quality-control metric introduced in [[10-Summaries/harmonizing-single-cell-3d-genome-data-with-stark-and-scnucleome]] that integrates TAD recovery, compartment recovery, and loop signal into a unified score.

## Definition

SSCE penalizes cells with few contacts but rewards cells whose contacts span informative structural features. Complements contact-count metrics that bias toward shallow-data cells.

## Why it matters

Rescues "low-contact-count but high-structure-quality" cells that simple thresholding would discard. Important for sparse sc3DG-seq data where average contacts per cell can be <100k.

## Related

- [[30-Concepts/stark]] · [[30-Concepts/single-cell-hi-c]] · [[30-Concepts/topologically-associating-domain]] · [[40-Topics/3d-genome]]
