---
type: concept
title: scWGA chemistries
aliases: [single-cell whole-genome amplification, scWGA chemistry, WGA methods]
tags: [scWGA, MDA, MALBAC, PTA, DOP-PCR, LIANTI, amplification]
created: 2026-05-19
updated: 2026-08-10
---

# scWGA chemistries

> The family of chemistries used to amplify femtogram quantities of single-cell DNA into nanogram-scale sequencing input. Different chemistries trade off coverage uniformity, allelic dropout, and error rate.

## The major chemistries

- **DOP-PCR** — first generation; degenerate oligonucleotide-primed PCR; high amplification bias ([[10-Summaries/gawad-2016-scgenome-review]]).
- **MDA (Multiple Displacement Amplification)** — phi29 polymerase + random hexamers; long products (>10 kb); first practical scWGA chemistry ([[10-Summaries/dean-2002-mda]]).
- **MALBAC** — quasi-linear preamplification + PCR exponential phase; lower bias than MDA, higher error rate ([[10-Summaries/gawad-2016-scgenome-review]]).
- **PicoPLEX / NEB-WGA** — proprietary hybrid chemistries.
- **LIANTI (Linear Amplification via Transposon Insertion)** — Tn5-based linear amplification; lower error rate ([[10-Summaries/chen-2017-lianti]]).
- **PTA (Primary Template-Directed Amplification)** — phi29 + exonuclease-resistant terminator nucleotides; most uniform coverage to date ([[10-Summaries/gonzalez-pena-2021-pnas]]).
- **META-CS / Tn5-duplex** — single-cell-compatible duplex sequencing variant ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Tradeoff space

Coverage uniformity ↑, allelic dropout ↓, error rate ↓ — but no chemistry wins on all three ([[10-Summaries/gawad-2016-scgenome-review]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Chronology anchors

- **DOP-PCR (1992)** — first general-purpose WGA; one partially degenerate primer, low-stringency priming then high-stringency tag-driven amplification. Its 4–6 orders of magnitude locus-to-locus bias is the baseline every later chemistry is measured against ([[10-Summaries/telenius-1992-dop-pcr]]; contrast in [[10-Summaries/dean-2002-mda]]).
- **MALBAC** — quasi-linear amplification by amplicon looping, framed for CNV rather than SNV work; early-cycle polymerase errors imprint on all downstream copies ([[10-Summaries/zong-2017-malbac-protocol]]).
- **Amplification-free is a separate branch, not a successor.** DLP+ opts out of WGA entirely via direct tagmentation, trading per-cell coverage for integer copy number, clean allele ratios and readable replication state across 51,926 cells ([[10-Summaries/laks-2019-dlp-plus]]).
- **The mechanistic argument against WGA, from the founding DLP paper.** WGA copies each template as long molecules that are fragmented *afterwards*, so one region yields multiple inserts with non-overlapping coordinates that **cannot be filtered as duplicates**; fragmenting first makes every PCR copy an exact duplicate and therefore removable ([[10-Summaries/zahn-2017-dlp]]). This single fact accounts for most of WGA's coverage pathology, and it generalizes: any protocol amplifying before fragmenting forfeits the distinction between duplicates and independent molecules (synthesis). Among the WGA chemistries, DOP-PCR gives the best uniformity and is the most CNA-amenable, but its coverage breadth **saturates** with deeper sequencing, so extra reads buy nothing and it remains unsuitable for SNVs ([[10-Summaries/zahn-2017-dlp]]). See [[30-Concepts/duplicate-marking]].
- The shared WGA artifact list — locus and allelic dropout, uneven amplification, chimeric molecules, base-copy errors — plus strand-aware alternatives (META-CS, SISSOR) is catalogued in [[10-Summaries/lim-2024-single-cell-omics-review]].

## Related

- [[30-Concepts/scwga]] · [[30-Concepts/pta]] · [[40-Topics/duplex-sequencing]]
- [[40-Topics/whole-genome-amplification]] · [[40-Topics/scdna-seq]]
- [[10-Summaries/telenius-1992-dop-pcr]] · [[10-Summaries/zong-2017-malbac-protocol]] · [[10-Summaries/laks-2019-dlp-plus]] · [[30-Concepts/dlp-plus]]
