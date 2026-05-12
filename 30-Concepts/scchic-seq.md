---
type: concept
title: scChIC-seq
aliases: [single-cell chromatin immunocleavage]
tags: [histone-modifications, single-cell, MNase, Zhao-lab]
created: 2026-05-12
updated: 2026-05-12
---

# scChIC-seq

> A single-cell histone-modification profiling method that uses an antibody-MNase fusion (covalent or pA-MNase + Ab complex) to cut chromatin at target sites, then **selectively PCR-amplifies the small target fragments** for sequencing.

## Definition

Workflow: fix cells → bind antibody-MNase conjugate (or pA-MNase + Ab) → MNase digestion (Ca²⁺-triggered) → adaptor ligation → selective PCR amplification of short (target) fragments → size selection → sequencing.

## Why it matters

- Single-cell histone-modification profiling without ChIP. Avoids losses from immunoprecipitation.
- Works with formaldehyde fixation (unlike CUT&RUN), and supports either covalent Ab-MNase or pA-MNase strategies.
- Established the feasibility of single-cell chromatin-state profiling. Throughput ~285 cells/experiment.

## Examples

- Human WBCs profiled for H3K4me3 → identifies T cells, B cells, NK cells, monocytes by chromatin state alone ([[10-Summaries/single-cell-chromatin-immunocleavage-sequencing-scchic-seq-to-profile-histone-modification]]).

## Related

- [[30-Concepts/chic-seq]] · [[30-Concepts/cut-and-run]] · [[30-Concepts/cut-and-tag]] · [[30-Concepts/sortchic]] · [[40-Topics/histone-modifications]] · [[20-Entities/keji-zhao]]
