---
type: concept
title: STAM-seq
aliases: [single-molecule targeted accessibility and methylation sequencing]
tags: [long-read, nanopore, plants, centromeres, adaptive-sampling]
created: 2026-05-12
updated: 2026-05-12
---

# STAM-seq

> A long-read chromatin-accessibility + methylation method for plants developed by Mo et al. 2023 (Zhai lab). Uses EcoGII 6mA labeling of accessible regions + nanopore sequencing + adaptive sampling to enrich highly repetitive regions (centromeres, telomeres, rDNAs).

## Definition

Workflow: nuclei isolation → EcoGII 6mA methylation → nanopore sequencing with adaptive sampling targeting HRRs ± 100 kb flanking. Modification-aware basecalling distinguishes 6mA (accessibility) from endogenous 5mC (methylation) on the same fiber.

## Why it matters

- 4.8× HRR enrichment via adaptive sampling without prior capture or amplification.
- Reveals strand-specific accessibility at *Arabidopsis* CEN180 centromeric repeats.
- First single-molecule chromatin map of plant centromeres, telomeres, and rDNAs.

## Examples

- [[10-Summaries/mo-2023-stam-seq]].

## Related

- [[30-Concepts/nanopore-adaptive-sampling]] · [[30-Concepts/highly-repetitive-regions]] · [[30-Concepts/samosa]] · [[30-Concepts/fiber-seq]] · [[40-Topics/long-read-sequencing]]
