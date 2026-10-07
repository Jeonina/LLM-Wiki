---
type: concept
title: Transcription factor motif
aliases: [TF motif, position weight matrix, PWM, binding site]
tags: [transcription-factors, motif-analysis, regulatory-elements]
created: 2026-05-12
updated: 2026-10-07
---

# Transcription factor motif

> The DNA sequence pattern recognized and bound by a transcription factor, typically represented as a position weight matrix (PWM) or consensus sequence. Databases: JASPAR, cisBP, HOCOMOCO, TRANSFAC.

## Why it matters

- TF motif enrichment in accessible/methylated/marked regions identifies regulators of cell identity.
- [[30-Concepts/chromvar]] aggregates scATAC-seq signal by TF motif to extract robust per-cell TF activity.
- [[30-Concepts/cistopic]] reveals TF motif enrichment per topic.

## Added 2026-10-07

Aggregating single-cell accessibility across all sites of each TF motif is one of SCRAT's feature types for clustering and differential analysis of sparse regulome data [[10-Summaries/ji-2017-scrat]].

TF motifs can be scored per cell after training by embedding a motif's consensus k-mers into a learned k-mer/cell space, so motif choice does not bias the embedding ([[10-Summaries/tayyebi-2024-cellspace]]). The same space yielded 29 de novo motifs resembling haematopoietic CIS-BP motifs ([[10-Summaries/tayyebi-2024-cellspace]]).

GFETM groups k-mer and TF-motif features with CNNs as limited to short-range sequence context, and claims that post hoc attention analysis plus zero-shot inference of its genome-foundation-model embeddings captures cell-state TF activities instead of motif scanning ([[10-Summaries/fan-2026-gfetm]]). This is a stated claim; the supporting Results are not in the clipping ([[10-Summaries/fan-2026-gfetm]]).

## Related

- [[30-Concepts/chromvar]] · [[30-Concepts/de-novo-motif-discovery]] · [[30-Concepts/scatac-seq]] · [[40-Topics/single-cell-atac-seq]]
