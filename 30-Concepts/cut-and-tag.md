---
type: concept
title: CUT&Tag
aliases: [Cleavage Under Targets and Tagmentation]
tags: [histone-modifications, Tn5, Henikoff-lab, in-situ]
created: 2026-05-12
updated: 2026-05-12
---

# CUT&Tag

> An antibody-directed in-situ chromatin profiling method developed by Kaya-Okur/Henikoff (2019). Tethers a Tn5 transposase fused to protein A (pA-Tn5) to histone-modification-bound chromatin via primary + secondary antibody, then Mg²⁺-catalyzed tagmentation deposits sequencing adapters at target sites within intact nuclei.

## Definition

Workflow: light formaldehyde fixation → nuclei isolation → primary antibody → secondary antibody → pA-Tn5 binding → Mg²⁺-triggered tagmentation → SDS release → PCR with indexed primers → sequencing. The fusion protein remains bound to DNA after cleavage, so fragments are retained within intact cells — making the method single-cell-compatible.

## Why it matters

- Rapidly replacing ChIP-seq as the standard chromatin-profiling method.
- Single-cell-compatible (scCUT&Tag) and combinatorial-indexing-scalable (sciCUT&Tag).
- Underpins methods that profile DNA modifications at chromatin sites: [[30-Concepts/6-base-cut-and-tag]].

## Examples

- Standard reference: Kaya-Okur et al. 2019 *Nat Commun*.
- Single-cell scale: [[10-Summaries/janssens-2023-scicut-tag]] (sciCUT&Tag).
- DNA-modification extension: [[10-Summaries/tavares-2026-6-base-cut-tag]] (6-base-CUT&Tag).

## Related

- [[30-Concepts/cut-and-run]] · [[30-Concepts/chic-seq]] · [[30-Concepts/chip-seq]] · [[30-Concepts/tn5-tagmentation]] · [[40-Topics/histone-modifications]] · [[20-Entities/steven-henikoff]]
