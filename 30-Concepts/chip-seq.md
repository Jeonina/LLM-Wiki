---
type: concept
title: ChIP-seq
aliases: [chromatin immunoprecipitation sequencing]
tags: [chromatin, histone-modifications, transcription-factors, bulk]
created: 2026-05-12
updated: 2026-05-12
---

# ChIP-seq

> Chromatin immunoprecipitation sequencing. The bulk-cell standard for profiling protein-DNA interactions (histone marks, transcription factors). Cells are crosslinked, chromatin is fragmented (sonication), an antibody pulls down the target, immunoprecipitated DNA is sequenced.

## Definition

Workflow: formaldehyde crosslinking → chromatin shearing (sonication) → antibody pulldown → reverse crosslink → DNA purification → sequencing. Requires ~10⁶ cells per assay.

## Why it matters

- The reference method against which all newer chromatin-profiling methods (CUT&RUN, CUT&Tag, ChIC, scCUT&Tag) are benchmarked.
- ENCODE and Roadmap Epigenomics built genome-wide histone-mark maps via ChIP-seq.
- High input requirement limits scalability and single-cell adaptation; CUT&Tag is replacing ChIP-seq in many labs.

## Related

- [[30-Concepts/cut-and-run]] · [[30-Concepts/cut-and-tag]] · [[30-Concepts/chic-seq]] · [[40-Topics/histone-modifications]] · [[30-Concepts/deephistone]]
