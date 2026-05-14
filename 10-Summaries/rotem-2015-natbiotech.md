---
type: summary
title: "Rotem 2015 — Single-cell ChIP-seq reveals cell subpopulations defined by chromatin state (Drop-ChIP)"
aliases: ["Drop-ChIP", "Rotem 2015", "scChIP-seq founding paper"]
tags: [scChIP-seq, Drop-ChIP, histone-modifications, microfluidics, Bernstein-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Assaf_2015_NatureBiotechnology.pdf"]
---

Rotem, Ram, Shoresh and colleagues (Bernstein / Weitz labs) introduced Drop-ChIP, the founding single-cell ChIP-seq method, combining drop-based microfluidics with DNA barcoding to acquire single-cell histone-modification profiles in mixed populations.

The chemistry: single cells are encapsulated in $\sim$50-µm droplets with lysis buffer and micrococcal nuclease, which preferentially digests accessible linker DNA. A second microfluidic merge introduces one of $\sim$1,152 unique barcoded oligonucleotide adaptors per nucleosome-containing drop, ligating the barcode to chromatin fragments. Drops are then pooled, immunoprecipitated in bulk against H3K4me2 or H3K4me3 with carrier chromatin, and sequenced. The barcode partitions the reads back into per-cell profiles.

Applied to mES cells, embryonic fibroblasts, and EML hematopoietic progenitors, Drop-ChIP recovered $\sim$1,000 marked promoters/enhancers per cell — sparse but sufficient to cluster cells by chromatin state and to identify three subpopulations of mES cells with distinct pluripotency-enhancer and polycomb-target activity reflecting differentiation priming. The signal was orthogonal to single-cell gene-expression heterogeneity, revealing chromatin-state structure that scRNA-seq does not see.

## Why this matters

The first published single-cell ChIP-seq method, predating CUT\&Tag-based single-cell histone-modification profiling. Established that chromatin-state heterogeneity exists within transcriptionally similar populations — a finding later confirmed and extended by scCUT\&Tag (Bartosovic 2021), sciCUT\&Tag, scChIC-seq, and nano-CT. Anchors §3.4 (chromatin state) as the founding method of the field.

---
**Source:** [DOI](https://doi.org/10.1038/nbt.3383) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/26458175/)

## Related

- [[30-Concepts/scchip-seq]]
- [[30-Concepts/histone-modifications]]
- [[20-Entities/bradley-bernstein]]
- [[10-Summaries/marek-2021-naturebiotechnology]]
