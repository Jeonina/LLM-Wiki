---
type: concept
title: SCcaller
aliases: []
tags: [single-cell, variant-calling, software]
created: 2026-05-12
updated: 2026-05-12
---

# SCcaller

> A single-cell SNV caller (Dong et al. 2017) that uses information from adjacent **bulk-sample-derived heterozygous SNVs** to calibrate allele-dropout corrections in a target cell. Requires matched bulk data.

## Definition

Local heterozygous SNVs (from bulk) anchor the expected allele-balance pattern; deviations at candidate single-cell loci are scored against this anchor.

## Why it matters

- Improves on Monovar's independent-locus assumption by exploiting local linkage.
- Limited when matched bulk is unavailable or when the cell belongs to a minor clone whose heterozygous pattern differs from bulk.

## Related

- [[30-Concepts/scout-variant-caller]] · [[30-Concepts/monovar]] · [[30-Concepts/allele-dropout]] · [[40-Topics/scdna-seq]]
