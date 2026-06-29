---
type: concept
title: Mitochondrial lineage tracing
aliases: [mtDNA lineage tracing, mtscATAC]
tags: [lineage-tracing, mtDNA, mosaicism]
created: 2026-05-12
updated: 2026-05-12
---

# Mitochondrial lineage tracing

> Using somatic mtDNA mutations — which accumulate at higher rates than nuclear DNA mutations and are present at hundreds-to-thousands of copies per cell — as natural barcodes for retrospective cell-lineage reconstruction in humans.

## Definition

mtDNA's high mutation rate and high copy number make it easier to detect somatic mutations from limited sequencing per cell. Methods include **mtscATAC-seq** (single-cell ATAC-seq with mtDNA recovery) and **EMBLEM** (epigenome and mitochondrial barcode of lineage from endogenous mutations).

## Why it matters

Provides a non-invasive, retrospective lineage system for human tissues where germline barcoding (CRISPR scarring) is unavailable. Particularly useful for hematopoietic clonal tracing where mtDNA mutations track cell lineages over decades.

## Examples

- Walker et al. 2020 NEJM used mtDNA mutations to track T-cell purifying selection.
- mtscATAC-seq used in clonal hematopoiesis studies; implemented in [[10-Summaries/ludwig-2020-mtscatac-seq]] and MAESTER ([[10-Summaries/miller-2022-maester]]); variant calling refined by scMitoMut ([[10-Summaries/sun-2025-scmitomut]]).

## Caveats

mtDNA's high copy number and random segregation between daughter cells mean only high-heteroplasmy variants persist robustly as labels, and some mutations may be under selection rather than neutral; hybridization capture recovers more variants but risks artifacts ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]). Despite few reliable variants per cell, mtDNA tracing succeeds when tissues undergo clonal expansion ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Related

- [[30-Concepts/lineage-tracing]] · [[30-Concepts/mitochondrial-heteroplasmy]] · [[40-Topics/somatic-mosaicism]] · [[30-Concepts/phylogenetic-inference]]
- [[40-Topics/somatic-mosaicism]] · [[40-Topics/single-cell-lineage-tracing]]
