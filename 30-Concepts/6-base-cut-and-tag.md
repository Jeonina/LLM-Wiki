---
type: concept
title: 6-base-CUT&Tag
aliases: [6B-C&T, biomodal 6-base CUT&Tag]
tags: [CUT&Tag, methylation, 5mC, 5hmC, histone-modifications, biomodal]
created: 2026-05-12
updated: 2026-05-12
---

# 6-base-CUT&Tag

> A bulk method that profiles **G/A/T/C + 5mC + 5hmC** at the DNA fragments tethered to a specific histone modification by CUT&Tag. Uses biomodal's enzymatic 6-base-seq conversion chemistry on hairpin-tagmented DNA.

## Definition

Workflow: antibody-directed pA-Tn5 tagmentation with a uracil-containing hairpin mosaic-end adapter (ME2U) → USER digestion → 6-base-seq enzymatic conversion (biomodal duet evoC kit) → Illumina paired-end sequencing. Scar sequences from the digested hairpin identify valid double-tagmented (circularized) molecules.

## Why it matters

Reveals 5mC and 5hmC distributions at **specific** chromatin states (active vs primed vs poised enhancers) at the fragment level — invisible to whole-genome 6-base-seq because the relevant histone-mark fraction is too small.

## Examples

- mESCs: primed enhancers (H3K4me1-only) have highest 5mC (~13%) and 5hmC (~4%); active and poised enhancers have lower modifications. H3K4me1-derived 5mC/5hmC signatures classify enhancer functional states ([[10-Summaries/tavares-2026-6-base-cut-tag]]).

## Related

- [[30-Concepts/cut-and-tag]] · [[40-Topics/dna-methylation]] · [[30-Concepts/5hmc]] · [[40-Topics/histone-modifications]] · [[20-Entities/biomodal]]
