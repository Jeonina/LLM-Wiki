---
type: summary
title: "Abascal et al. 2021 — NanoSeq: somatic mutation landscapes at single-molecule resolution"
source: "[[00-Sources/papers/Somatic mutation landscapes at single-molecule resolution]]"
source_kind: paper
author: "Federico Abascal, Luke M. R. Harvey, Emily Mitchell, Andrew R. J. Lawson, Stefanie V. Lensing, Peter Ellis, Andrew J. C. Russell, Raul E. Alcantara, Adrian Baez-Ortega, Henry Lee-Six, Tim H. H. Coorens, Michael Spencer Chapman, Iñigo Martincorena (corresponding), Peter J. Campbell (corresponding)"
published: 2021
ingested: 2026-05-18
ingest_depth: abstract+intro
doi: "10.1038/s41586-021-03477-4"
journal: "Nature"
tags: [NanoSeq, duplex-sequencing, somatic-mutation, single-molecule, ultra-low-frequency, Sanger, Martincorena-lab, Campbell-lab]
entities: []
concepts:
  - "[[30-Concepts/duplex-sequencing]]"
  - "[[30-Concepts/nanoseq]]"
  - "[[30-Concepts/somatic-mosaicism]]"
topics:
  - "[[40-Topics/duplex-sequencing]]"
  - "[[40-Topics/somatic-mosaicism]]"
---

**Citation:** Abascal et al. (2021) — *NanoSeq: somatic mutation landscapes at single-molecule resolution* — *Nature*. [DOI](https://doi.org/10.1038/s41586-021-03477-4)

# Abascal et al. 2021 — NanoSeq

> Thesis: standard duplex sequencing (Schmitt 2012, Kennedy 2014) is the gold standard for low-frequency somatic mutation detection, but its error rate (~10⁻⁷/base) is still dominated by DNA damage. NanoSeq combines **restriction enzyme fragmentation** with duplex consensus calling to push error rates to **<5 × 10⁻⁹/base** — single-molecule resolution for somatic mutations, applicable to non-dividing tissues (neurons, postmitotic cells) where colony-based methods cannot reach.

## Key claims (abstract + intro)

- **Sub-10⁻⁹/base error rate** — two orders of magnitude better than canonical duplex sequencing; enables somatic mutation calling from any cell population without single-cell isolation.
- **Restriction enzyme fragmentation** (rather than mechanical shearing) reduces end-related damage artifacts that limited classical duplex sequencing.
- **Apply to non-dividing tissues**: postmitotic neurons, smooth muscle, mature hepatocytes — cell types inaccessible to colony-expansion methods (Lee-Six 2018 lineage tracing).
- **Mutation burden quantification across tissues**: defines tissue-specific somatic mutation rates and spectra.

## Why this matters

NanoSeq is the **state-of-the-art bulk-tissue somatic mutation caller** and complements single-cell methods (scWGS, PTA, IDA) for cells that cannot be propagated or isolated. Frequently cited as the reference accuracy benchmark for duplex protocols.

## Note on ingest depth

Abstract + intro only; full PDF re-ingest will deepen quantitative error-rate modeling and tissue-comparison data.

---
**Source:** [DOI](https://doi.org/10.1038/s41586-021-03477-4) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33911273/)

## Related

- [[30-Concepts/duplex-sequencing]] · [[30-Concepts/nanoseq]] · [[30-Concepts/somatic-mosaicism]]
- [[10-Summaries/kennedy-2014-duplex-protocol]] · [[10-Summaries/nandi-2025-udseq]]
- [[40-Topics/duplex-sequencing]] · [[40-Topics/somatic-mosaicism]]
