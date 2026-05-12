---
type: concept
title: scATAC-seq
aliases: [single-cell ATAC-seq]
tags: [chromatin-accessibility, single-cell, ATAC, Tn5]
created: 2026-05-12
updated: 2026-05-12
---

# scATAC-seq

> Single-cell Assay for Transposase-Accessible Chromatin using sequencing. Profiles genome-wide chromatin accessibility in individual cells using hyperactive Tn5 transposase to insert sequencing adapters preferentially at open chromatin (regulatory elements).

## Definition

Workflow: lyse cells / isolate nuclei → Tn5 tagmentation → barcoded library prep → sequencing. Each cell yields ~1k–20k unique accessibility fragments. The diploid genome inherently caps per-locus reads at 2.

## Why it matters

- Maps cell-type-specific regulatory landscapes from heterogeneous tissue.
- Foundation for [[40-Topics/single-cell-atac-seq]] tooling: chromVAR, cisTopic, SnapATAC, EpiScanpy, scABC.

## Related

- [[30-Concepts/atac-seq]] · [[30-Concepts/tn5-tagmentation]] · [[30-Concepts/chromatin-accessibility]] · [[40-Topics/single-cell-atac-seq]]
