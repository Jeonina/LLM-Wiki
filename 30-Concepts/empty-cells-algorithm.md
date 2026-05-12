---
type: concept
title: EmptyCells algorithm
aliases: []
tags: [3D-genome, quality-control, single-cell, barcode-filtering]
created: 2026-05-12
updated: 2026-05-12
---

# EmptyCells algorithm

> A filtering algorithm for sc3DG-seq data that distinguishes barcodes corresponding to real cells from empty-droplet or low-quality barcodes. Uses Monte Carlo simulation against an empty-barcode null distribution.

## Definition

Analogous to the EmptyDrops algorithm in scRNA-seq. Filters cells based on contact count + statistical separation from an empty-barcode null model.

## Why it matters

Critical first-pass QC for high-throughput sc3DG-seq experiments where many barcodes contain little signal.

## Related

- [[30-Concepts/stark]] · [[30-Concepts/sscce]] · [[30-Concepts/single-cell-hi-c]] · [[40-Topics/3d-genome]]
