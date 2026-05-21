---
type: summary
title: "Zhang et al. 2025 — SMaHT duplex-seq benchmark: six methods, concordant mutation rates"
source: "[[00-Sources/papers/Benchmarking of duplex sequencing approaches to reveal somatic mutation landscapes]]"
source_kind: paper
author: "Yang Zhang, Vinayak V. Viswanadham, ... Diane Shao, Christopher A. Walsh, Gilad D. Evrony, Chenghang Zong, Tim H. H. Coorens (corresponding)"
published: 2025-12-15
ingested: 2026-05-12
doi: "10.64898/2025.12.12.692823"
journal: "bioRxiv (preprint)"
tags: [duplex-sequencing, benchmarking, SMaHT-network, mutational-signatures, somatic-mosaicism]
entities:
  - "[[20-Entities/tim-coorens]]"
  - "[[20-Entities/diane-d-shao]]"
  - "[[20-Entities/christopher-walsh]]"
  - "[[20-Entities/gilad-evrony]]"
  - "[[20-Entities/chenghang-zong]]"
  - "[[20-Entities/smaht-network]]"
concepts:
  - "[[30-Concepts/duplex-sequencing]]"
  - "[[30-Concepts/codec]]"
  - "[[30-Concepts/nanoseq]]"
  - "[[30-Concepts/hidef-seq]]"
  - "[[30-Concepts/mutational-signatures]]"
  - "[[30-Concepts/somatic-mosaicism]]"
topics:
  - "[[40-Topics/duplex-sequencing]]"
  - "[[40-Topics/somatic-mosaicism]]"
---

**Citation:** Zhang et al. (2025) — *SMaHT duplex-seq benchmark: six methods, concordant mutation rates* — *bioRxiv (preprint)*. [DOI](https://doi.org/10.64898/2025.12.12.692823)

# Zhang et al. 2025 — SMaHT duplex-seq benchmark: six methods, concordant mutation rates

> Thesis: The SMaHT (Somatic Mosaicism across Human Tissues) Network put six duplex-sequencing technologies through a head-to-head benchmark using identical reference samples (cord blood, a tumor/normal cell-line mixture, and homogenates from six human tissues). **Genomic footprint, sensitivity, and cost differ substantially across methods, but estimated mutation rates and signatures are highly concordant** — meaning the field can pool data across platforms when the question is mutational burden or signatures, but should pick deliberately when the question is method-specific (e.g., cfDNA fragmentomics or single-cell).

## Key claims

- Six methods benchmarked: **CODEC**, **CompDuplex-seq** (CompDup), **HiDEF-seq**, **NanoSeq**, **ppmSeq**, **VISTA-seq**. Each shows a distinct profile across (a) genomic footprint, (b) sensitivity per Gb sequenced, and (c) cost per duplex base.
- Despite chemistry differences, **mutation-rate estimates and 96-channel SBS signatures are highly concordant** across methods on the same samples.
- Combined with ultra-deep WGS, duplex methods detect mutations beyond the clonally-expanded fraction that WGS variant callers can see — capturing the true mosaicism distribution, including singleton variants that exist in one cell.
- Provides a foundation for **interpreting cross-platform data in SMaHT** and beyond. Implicit guidance: pick the method by experimental constraint (input DNA, target region, cost), not by accuracy alone, since accuracy converges.

## Methods / evidence

Cross-platform comparison on three reference sample types using each lab's published protocol. Common bioinformatics through duplex-call consensus. The benchmark relies on each method being run by the lab that developed it — minimizing implementation variance.

## Surprising or load-bearing bits

- The concordance result is the load-bearing finding. It legitimizes meta-analysis across SMaHT papers using different duplex platforms — important because individual tissue cohorts use whichever method their lab developed.
- Six methods in one consortium also signals that **duplex sequencing has matured into a stable methodology** with multiple converged implementations rather than a single winning chemistry.

## Connections to other sources

- Companion paper to [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] (same SMaHT consortium, single-cell side rather than bulk-duplex side). Together they define what SMaHT calls a "comprehensive view" — duplex for population mutation rates, scDNA-seq for clonality.
- The methodological-axis framing aligns with [[10-Summaries/shao-2025-scDNA-mosaicism-review]]: duplex protection is the answer to scWGA single-strand dropout but is not yet itself single-cell.
- Cites the founding paper [[10-Summaries/kennedy-2014-duplex-protocol]] (Kennedy 2014).

## Open questions

- Benchmark does not include UDSeq ([[10-Summaries/nandi-2025-udseq]]); cross-comparison is open.
- Single-cell duplex remains the holy grail; this benchmark is bulk/pseudo-bulk.

---
**Source:** [DOI](https://doi.org/10.64898/2025.12.12.692823)
## Related

- [[40-Topics/duplex-sequencing]] · [[30-Concepts/codec]] · [[30-Concepts/nanoseq]] · [[30-Concepts/hidef-seq]] · [[20-Entities/smaht-network]]
