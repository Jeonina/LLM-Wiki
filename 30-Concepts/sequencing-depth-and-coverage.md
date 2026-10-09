---
type: concept
title: Sequencing Depth and Coverage
aliases: [coverage breadth, depth vs breadth, shallow sequencing]
tags: [coverage, depth, breadth, economics, study-design]
created: 2026-08-10
updated: 2026-10-08
---

# Sequencing Depth and Coverage

> **Depth** is how many times a base is read; **breadth** is what fraction of the genome is read at all. Single-cell study design is largely the problem of allocating a fixed sequencing budget between depth per cell and number of cells.

## The trade, quantified

Ten WGA cells at 30× costs the same as **6,000 amplification-free cells at 0.05×**, and the latter gives subclone detection sensitivity of ~0.05% ([[zahn-2017-dlp]]). For copy number, many cells shallow beats few cells deep; for per-cell SNVs the reverse holds, and shallow libraries explicitly cannot deliver complete single-cell genomes ([[zahn-2017-dlp]]).

Typical operating points in this corpus: 0.07–0.12× per cell for amplification-free WGS ([[zahn-2017-dlp]]); ~0.1× at ~100 kb resolution across tens of thousands of cells ([[wang-2021-medalt]]); a median of 671 UMIs per cell at ~5,000 raw reads for atlas-scale sci-RNA-seq3 ([[cao-2019-moca]]).

## Merging recovers breadth

64 amplification-free cells merge to 94.5–96.8% genome breadth, and 48 merged cells match a true bulk genome of the same depth in breadth and Lorenz uniformity ([[zahn-2017-dlp]]). Merged libraries support conventional SNV, LOH and breakpoint callers ([[zahn-2017-dlp]]) — but lose exactly the minor clones single cells exist to find ([[zahn-2017-dlp]]); see [[pseudo-bulk]].

## Coverage saturation is chemistry-dependent

DOP-PCR coverage breadth **saturates** with deeper sequencing, so extra reads buy nothing and the chemistry is unsuitable for SNVs ([[zahn-2017-dlp]]). Amplification-free libraries do not saturate, because every retained read is a unique template representation ([[zahn-2017-dlp]]); see [[duplicate-marking]].

## In two dimensions the arithmetic is harsher

Improving Hi-C resolution *n*-fold requires *n*² more reads ([[lieberman-aiden-2009-hic]]), so 5–10% linear genome coverage becomes 0.25–1% of possible contacts ([[zhou-2019-schicluster]]). Practical floors follow: single-cell Hi-C clustering degrades below 25,000 contacts and collapses at 5,000 ([[zhou-2019-schicluster]]), while combinatorial-indexing scHi-C delivers ~8,000–9,000 ([[ramani-2017-scihi-c]]).

## Peak calling has its own saturation logic

High-fold-enrichment peaks saturate early while lower-fold sites keep accruing with depth, so "have I sequenced enough?" is answerable only per fold-enrichment stratum ([[zhang-2008-macs]]).

## Added 2026-10-07

MuTect makes sensitivity an explicit function of depth and allele fraction: 95.6% at 30× for AF 0.2, 99.9% at 50×, 58.9% at AF 0.1 (30×), and 66.4% for AF 0.03 at 150× ([[10-Summaries/cibulskis-2013-mutect]]). Unfiltered false positives also rise with depth (6.7/Mb at 5× to 20.1/Mb at 30×) because power to call low-AF noise increases ([[10-Summaries/cibulskis-2013-mutect]]).

In sciMET-cap, the useful cost metric was unique CpGs per raw read, not percent on target. A higher wash temperature raised the on-target fraction but cut library complexity, leaving less information per cell ([[10-Summaries/acharya-2024-scimet-cap]]). The recommended depth is 200–275 thousand raw reads per cell for 5,000–10,000-cell datasets. That compares with about 2 million for non-capture single-cell methylation, 50–100 thousand for scRNA-seq and 75–125 thousand for scATAC-seq ([[10-Summaries/acharya-2024-scimet-cap]]).


## Added 2026-10-08 — sequence models & foundation models

- STRAND handles 1-180x read redundancy in exome BAMs by filtering reads eightfold and re-weighting rare positions in the loss, recovering reference next-token accuracy (56.04 -> 58.89%) ([[10-Summaries/ayanian-2025-strand]]).

## Related

- [[scwga-chemistries]] · [[pseudo-bulk]] · [[duplicate-marking]] · [[whole-genome-amplification]]
