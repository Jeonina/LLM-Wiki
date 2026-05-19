---
type: concept
title: Nanopore adaptive sampling
aliases: [ReadFish, ReadUntil]
tags: [long-read, ONT, targeted-sequencing]
created: 2026-05-12
updated: 2026-05-12
---

# Nanopore adaptive sampling

> A real-time read-selection feature of Oxford Nanopore sequencers that compares the first few hundred bases of each emerging read to a target reference, then **rejects unwanted reads** by reversing the pore voltage so the molecule is ejected. The pore is then available for the next molecule.

## Definition

Implemented via tools like ReadFish, ReadUntil, and ONT's native Dorado. Targeted regions are typically specified as a BED file or list of contigs.

## Why it matters

- Targeted sequencing without library-prep capture: enriches for regions of interest without PCR or hybridization.
- Particularly useful for highly repetitive regions where capture probes can't be uniquely designed.

## Examples

- [[10-Summaries/mo-2023-stam-seq]] (STAM-seq) uses adaptive sampling for plant HRRs.

## Related

- [[30-Concepts/oxford-nanopore]] · [[30-Concepts/highly-repetitive-regions]] · [[30-Concepts/stam-seq]] · [[40-Topics/long-read-sequencing]]
