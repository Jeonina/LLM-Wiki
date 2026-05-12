---
type: concept
title: Monovar
aliases: []
tags: [single-cell, variant-calling, software]
created: 2026-05-12
updated: 2026-05-12
---

# Monovar

> A single-cell SNV caller (Zafar et al. 2016) that integrates base count information across multiple cells to correct for uneven allele coverage caused by scWGA amplification bias. Assumes independent loci.

## Definition

Monovar treats each locus as independently sampled across all cells in the dataset; this multi-cell pooling helps calibrate genotype likelihoods when individual cells suffer amplification dropout.

## Why it matters

- One of the first single-cell SNV callers; reference benchmark for newer methods like SCcaller and SCOUT.
- Fails when minor clones or rare variants make multi-cell pooling unreliable.

## Related

- [[30-Concepts/scout-variant-caller]] · [[30-Concepts/sccaller]] · [[30-Concepts/scwga]] · [[40-Topics/scdna-seq]]
