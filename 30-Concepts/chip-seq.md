---
type: concept
title: ChIP-seq
aliases: [chromatin immunoprecipitation sequencing]
tags: [chromatin, histone-modifications, transcription-factors, bulk]
created: 2026-05-12
updated: 2026-10-07
---

# ChIP-seq

> Chromatin immunoprecipitation sequencing. The bulk-cell standard for profiling protein-DNA interactions (histone marks, transcription factors). Cells are crosslinked, chromatin is fragmented (sonication), an antibody pulls down the target, immunoprecipitated DNA is sequenced.

## Definition

Workflow: formaldehyde crosslinking → chromatin shearing (sonication) → antibody pulldown → reverse crosslink → DNA purification → sequencing. Requires ~10⁶ cells per assay.

## Why it matters

- The reference method against which all newer chromatin-profiling methods (CUT&RUN, CUT&Tag, ChIC, scCUT&Tag) are benchmarked.
- ENCODE and Roadmap Epigenomics built genome-wide histone-mark maps via ChIP-seq.
- High input requirement limits scalability and single-cell adaptation; CUT&Tag is replacing ChIP-seq in many labs.

## Added 2026-10-07

**Origin.** The term "ChIP-Seq" was introduced for direct Solexa sequencing of ChIP DNA from native MNase-digested mononucleosomes (17 PCR cycles; >20 M 36-bp tags per run), applied to 20 histone methylations, H2A.Z, Pol II and CTCF in human CD4⁺ T cells ([[10-Summaries/barski-2007-histone-methylation-chip-seq]]). Note that this founding protocol used native (uncrosslinked) MNase chromatin for histone marks and crosslinked sonicated chromatin only for Pol II/CTCF ([[10-Summaries/barski-2007-histone-methylation-chip-seq]]).

**Enrichment compresses quantitative range.** In R1:MEF mixing series, ChIP-seq H3K4me3 signal tracked cell proportion with R² 0.70/0.84 and was flat at intermediate ratios, versus 0.89/0.94 for deaminase-based DeChIC-seq ([[10-Summaries/shi-2026-dechic-seq]]). CUT&RUN matched ORGANIC native ChIP dynamic range with ~10-fold fewer reads and outperformed crosslinked ChIP-seq on sensitivity/specificity ([[10-Summaries/skene-2017-cut-and-run]]).


## Related

- [[30-Concepts/cut-and-run]] · [[30-Concepts/cut-and-tag]] · [[30-Concepts/chic-seq]] · [[40-Topics/histone-modifications]] · [[30-Concepts/deephistone]]
