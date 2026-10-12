---
type: concept
title: Sequencing Depth and Coverage
aliases: [coverage breadth, depth vs breadth, shallow sequencing]
tags: [coverage, depth, breadth, economics, study-design]
created: 2026-08-10
updated: 2026-10-12
---

# Sequencing Depth and Coverage

> **Depth** is how many times a base is read; **breadth** is what fraction of the genome is read at all. Single-cell study design is largely the problem of allocating a fixed sequencing budget between depth per cell and number of cells ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).

> [!abstract] 한눈에
> depth는 한 염기를 몇 번 읽었는지, breadth는 유전체의 몇 퍼센트를 한 번이라도 읽었는지를 뜻하고, single-cell 연구 설계는 정해진 시퀀싱 예산을 세포당 depth와 세포 수 사이에 나누는 문제다 ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]). copy number에는 얕게 많은 세포가, 세포별 SNV에는 깊게 적은 세포가 유리하며, Hi-C처럼 2차원 신호에서는 필요한 read가 해상도의 제곱으로 늘어난다 ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]; [[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 WGA 시뮬레이터](../60-Explainers/wga-simulator.html)
<!-- /explainer-links -->

## Definition

Depth counts how many reads cover a base; breadth is the fraction of the genome covered at all (synthesis). With a fixed budget, adding cells costs depth per cell and the reverse ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).

## Why it matters

- Ten WGA cells at 30× cost the same as **6,000 amplification-free cells at 0.05×**, and the latter give subclone detection sensitivity of ~0.05% ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- For copy number, many cells shallow beats few cells deep; for per-cell SNVs the reverse holds, and shallow libraries explicitly cannot deliver complete single-cell genomes ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).

## Typical operating points

| Assay | Depth per cell | Source |
|---|---|---|
| Amplification-free scWGS (DLP) | 0.07–0.12× | ([[10-Summaries/zahn-2017-dlp\|Zahn 2017]]) |
| Shallow scWGS across tens of thousands of cells | ~0.1×, at ~100 kb resolution | ([[10-Summaries/wang-2021-medalt\|MEDALT]]) |
| Atlas-scale sci-RNA-seq3 | Median 671 UMIs per cell at ~5,000 raw reads | ([[10-Summaries/cao-2019-moca\|Cao 2019]]) |
| sciMET-cap (capture single-cell methylation), 5,000–10,000-cell datasets | 200–275 thousand raw reads recommended | ([[10-Summaries/acharya-2024-scimet-cap\|sciMET-cap]]) |
| Non-capture single-cell methylation | About 2 million raw reads | ([[10-Summaries/acharya-2024-scimet-cap\|sciMET-cap]]) |
| scRNA-seq | 50–100 thousand raw reads | ([[10-Summaries/acharya-2024-scimet-cap\|sciMET-cap]]) |
| scATAC-seq | 75–125 thousand raw reads | ([[10-Summaries/acharya-2024-scimet-cap\|sciMET-cap]]) |
| Combinatorial-indexing scHi-C | ~8,000–9,000 contacts | ([[10-Summaries/ramani-2017-scihi-c\|Ramani 2017]]) |

## How depth behaves by data type

### Merging recovers breadth

- 64 amplification-free cells merge to 94.5–96.8% genome breadth, and 48 merged cells match a true bulk genome of the same depth in breadth and Lorenz uniformity ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- Merged libraries support conventional SNV, LOH and breakpoint callers ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]) — but lose exactly the minor clones single cells exist to find ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]); see [[pseudo-bulk]].

### Coverage saturation is chemistry-dependent

- DOP-PCR coverage breadth **saturates** with deeper sequencing, so extra reads buy nothing and the chemistry is unsuitable for SNVs ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- Amplification-free libraries do not saturate, because every retained read is a unique template representation ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]); see [[duplicate-marking]].

### In two dimensions the arithmetic is harsher

- Improving Hi-C resolution *n*-fold requires *n*² more reads ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]), so 5–10% linear genome coverage becomes 0.25–1% of possible contacts ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).
- Single-cell Hi-C clustering degrades below 25,000 contacts and collapses at 5,000 ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).

### Peak calling has its own saturation logic

- High-fold-enrichment peaks saturate early while lower-fold sites keep accruing with depth, so "have I sequenced enough?" is answerable only per fold-enrichment stratum ([[10-Summaries/zhang-2008-macs|MACS]]).

### Variant-calling sensitivity is a function of depth and allele fraction

- MuTect's sensitivity is 95.6% at 30× for AF 0.2, 99.9% at 50×, 58.9% at AF 0.1 (30×), and 66.4% for AF 0.03 at 150× ([[10-Summaries/cibulskis-2013-mutect|MuTect]]).
- Unfiltered false positives also rise with depth (6.7/Mb at 5× to 20.1/Mb at 30×) because power to call low-AF noise increases ([[10-Summaries/cibulskis-2013-mutect|MuTect]]).

### Capture assays: information per read, not on-target fraction

- In sciMET-cap, the useful cost metric was unique CpGs per raw read, not percent on target ([[10-Summaries/acharya-2024-scimet-cap|sciMET-cap]]).
- A higher wash temperature raised the on-target fraction but cut library complexity, leaving less information per cell ([[10-Summaries/acharya-2024-scimet-cap|sciMET-cap]]).

### Read redundancy in sequence-model training

- STRAND handles 1–180× read redundancy in exome BAMs by filtering reads eightfold and re-weighting rare positions in the loss, recovering reference next-token accuracy (56.04 → 58.89%) ([[10-Summaries/ayanian-2025-strand|STRAND]]).

## Contested points

- **Is every amplification-free read a unique template?** Zahn 2017 treats amplification-free reads as unique template representations ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]). A later DLP+ analysis qualifies this: a small set (under 1%) of artifactual same-start fragments remains after standard deduplication, and these must be removed before using fragment overlaps to estimate ploidy ([[10-Summaries/wesley-2026-songbird|Songbird]]).
- **Merging trades clones for breadth.** Pooling cells restores bulk-like breadth but discards the minor clones that motivated single-cell sequencing ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/scwga-chemistries|scWGA chemistries]] — Amplification methods whose coverage saturates or not with depth.
> - `concept` [[30-Concepts/pseudo-bulk|Pseudo-bulk]] — Aggregating single cells into a profile to recover depth and breadth.
> - `concept` [[30-Concepts/duplicate-marking|Duplicate marking]] — Removing PCR duplicates so reads reflect unique templates.
> - `hub` [[40-Topics/whole-genome-amplification|Whole-genome amplification]] — scWGA chemistries and their error profiles.

## All sources on this page

> [!info]- 11 summaries cited here
> - [[10-Summaries/acharya-2024-scimet-cap|Acharya 2024]]
> - [[10-Summaries/ayanian-2025-strand|STRAND 2025]]
> - [[10-Summaries/cao-2019-moca|Cao 2019]]
> - [[10-Summaries/cibulskis-2013-mutect|Cibulskis 2013]]
> - [[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]
> - [[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]
> - [[10-Summaries/wang-2021-medalt|Wang 2021]]
> - [[10-Summaries/wesley-2026-songbird|Wesley 2026]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
> - [[10-Summaries/zhang-2008-macs|Zhang 2008]]
> - [[10-Summaries/zhou-2019-schicluster|Zhou 2019]]
