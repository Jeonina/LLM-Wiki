---
type: summary
title: "Macaulay & Voet 2014 — Single cell genomics: advances and future perspectives"
aliases: ["Macaulay Voet 2014", "scWGA review"]
tags: [review, scWGA, single-cell-genomics, methods]
created: 2026-05-13
updated: 2026-05-13
sources: ["Iain_2014_PLOSGenetics.pdf"]
---

Macaulay and Voet's 2014 review consolidated the state of single-cell whole-genome amplification methods circa 2014. Covers single-cell isolation strategies (manual micropipetting, FACS, microfluidics, LCM, sn-suspension sorting); WGA chemistries (DOP-PCR, MDA, MALBAC) and their failure modes (allelic dropout, preferential amplification, chimeric DNA molecules, GC-bias, nucleotide copy errors); and the downstream readouts those failures complicate (SV detection, CNV calling, B-allele fraction, base mutation report).

The review's central methodological point is that WGA artifacts dominate the scDNA-seq error budget and that no single chemistry minimizes all failure modes simultaneously — DOP-PCR gives uniform CNV-grade coverage at the cost of low-resolution sequence accuracy; MDA gives high coverage breadth but exponential amplification of early errors; MALBAC's quasilinear strategy reduces some bias at the cost of a characteristic C-to-T error profile. Method selection must match the downstream question.

## Why this matters

A foundational reference for the scWGA-chemistry landscape that subsequent work (PTA, LIANTI, Strand-seq) extended. Anchors §3.1 alongside the Shao 2025 update (Diane 2025 NRG review) and complements the Gawad 2016 NRG review. Both 2014- and 2025-vintage scWGA reviews are useful for the methods-comparison framing in §3.1.

## Related

- [[10-Summaries/diane-2025-naturereviewsgenetics]]
- [[10-Summaries/charles-2016-naturereviewsgenetics]]
- [[30-Concepts/scwga-chemistries]]
