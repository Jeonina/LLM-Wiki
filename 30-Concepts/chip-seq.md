---
type: concept
title: ChIP-seq
aliases: [chromatin immunoprecipitation sequencing]
tags: [chromatin, histone-modifications, transcription-factors, bulk]
created: 2026-05-12
updated: 2026-10-09
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


## Added 2026-10-08 — sequence models & foundation models

- ExPecto's expression models weighted predicted TF and histone ChIP-seq features over DNase features (P = 6.9e-25), suggesting accessibility alone carries less causal expression information ([[10-Summaries/zhou-2018-expecto]])
- ATGC-Gen turns 10 million ENCODE ChIP-seq rows (340 factors, 129 cell types) into a conditional benchmark of 55,830 variable-length examples over 62 factors, split by chromosome ([[10-Summaries/su-2025-atgc-gen]]).
- HiCFoundation-epi predicts six 1-kb epigenomic tracks (ATAC, DNase, CTCF, H3K4me3, H3K27ac, H3K27me3) from Hi-C alone, and zeroing contacts at 392 convergent-CTCF loops lowered the predicted CTCF anchor signal in 97.8% of cases ([[10-Summaries/wang-2026-hicfoundation]]).

## Added 2026-10-09 — foundation-model gap evidence

- In CANDI's input-ablation analysis, H3K27me3 and H3K9me3 tracks carried little information for imputing active marks, while H3K27ac and H3K4me3 were imputed with Pearson r > 0.8 in many cell types ([[10-Summaries/foroozandeh-2025-candi]])

## Related

- [[30-Concepts/cut-and-run]] · [[30-Concepts/cut-and-tag]] · [[30-Concepts/chic-seq]] · [[40-Topics/histone-modifications]] · [[30-Concepts/deephistone]]
