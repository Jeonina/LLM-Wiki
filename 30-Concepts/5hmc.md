---
type: concept
title: 5-hydroxymethylcytosine (5hmC)
aliases: [5hmC, hydroxymethylcytosine]
tags: [methylation, TET, demethylation, brain]
created: 2026-05-12
updated: 2026-05-12
---

# 5-hydroxymethylcytosine (5hmC)

> An oxidative intermediate generated when TET enzymes hydroxylate 5-methylcytosine. ~10–30× less abundant than 5mC in most tissues, but particularly enriched in brain. Both an **intermediate** in active DNA demethylation and a **stable epigenetic mark** with regulatory function at enhancers and active gene bodies.

## Definition

TET (1/2/3) enzymes oxidize 5mC → 5hmC → 5fC → 5caC. 5fC and 5caC are excised by thymine-DNA glycosylase for base-excision repair, completing demethylation. 5hmC itself, however, is stable enough to act as a regulatory mark in differentiated tissues.

## Why it matters

- Bisulfite sequencing **conflates 5mC and 5hmC** — both read as C. Methods that distinguish them (hmC-CATCH, AbaSI-based scAba-seq, [[30-Concepts/simple-seq]], [[30-Concepts/6-base-cut-and-tag]]) reveal divergent regulatory roles.
- 5hmC marks active regulatory elements (enhancers, transcribed gene bodies).
- Loss of 5hmC is associated with cancer (IDH-mutant glioma/AML reduce TET activity via α-KG depletion).
- TET1 mutant mice show adult-neurogenesis deficits and memory impairment.

## Variants and refinements

- Type-1 5hmCG = basal-level, not co-occurring with 5mCG.
- Type-2 5hmCG = co-occurring with 5mCG on the same molecule, associated with active demethylation regions ([[10-Summaries/bai-2024-simple-seq]]).

## Related

- [[30-Concepts/dna-methylation]] · [[30-Concepts/tet-enzymes]] · [[30-Concepts/simple-seq]] · [[30-Concepts/6-base-cut-and-tag]]
