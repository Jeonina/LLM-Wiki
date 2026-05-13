---
type: summary
title: "Smallwood 2014 — Single-cell genome-wide bisulfite sequencing for assessing epigenetic heterogeneity (scBS-seq)"
aliases: ["scBS-seq founding paper", "Smallwood 2014"]
tags: [scBS-seq, methylation, bisulfite, single-cell, methylome, Reik-lab, Kelsey-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Sebastien_2014_NatureMethods.pdf"]
---

Smallwood, Lee, Angermueller and colleagues (Reik / Kelsey labs) introduced single-cell genome-wide bisulfite sequencing (scBS-seq), the founding genome-wide single-cell DNA methylome method. The chemistry adapts post-bisulfite adaptor tagging (PBAT) to single-cell input by performing bisulfite conversion first (fragmenting DNA simultaneously), then random-primed complementary-strand synthesis introduces sequencing adaptors. This ordering inverts the conventional bisulfite workflow and avoids the DNA-degradation-induced library loss that limits standard chemistries at single-cell input.

Applied to 12 metaphase-II oocytes, 12 2i-ESCs, and 20 serum-grown mESCs, scBS-seq measured methylation at up to 48.4% of CpGs per cell (mean $\sim$3.7 million CpGs covered, 17.7% of all CpGs at moderate sequencing depth). The data revealed substantial cell-to-cell methylation heterogeneity in serum-grown mESCs, including "2i-like" cells with hypomethylated naive-pluripotency signatures present within serum cultures — a heterogeneity that bulk WGBS averaging conceals.

## Why this matters

The founding genome-wide single-cell DNA methylome chemistry, parent to scRRBS, snmC-seq2/3, scNMT-seq, sn-m3C-seq, and the broader methylome family. Anchors §3.3 (DNA methylation) as the originating method against which all subsequent single-cell methylome protocols are benchmarked.

## Related

- [[30-Concepts/scbs-seq]]
- [[30-Concepts/dna-methylation]]
- [[10-Summaries/hongshan-2013-genomeresearch]]
- [[10-Summaries/chongyuan-2018-naturecommunications]]
- [[10-Summaries/liu-2023-nature]]
- [[20-Entities/wolf-reik]]
