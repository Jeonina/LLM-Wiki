---
type: summary
title: "Tu et al. 2021 — SCOUT: single-cell genotyping using local-territory base counts"
source: "[[00-Sources/papers/Accurate single-cell genotyping utilizing information from the local genome territory]]"
source_kind: paper
author: "Kailing Tu, Keying Lu, Qilin Zhang, Wei Huang, Dan Xie (corresponding)"
published: 2021-02-22
ingested: 2026-05-12
doi: "10.1093/nar/gkab106"
journal: "Nucleic Acids Research"
tags: [scDNA-seq, variant-calling, SNV, allele-dropout, intra-tumor-heterogeneity, software]
entities:
  - "[[20-Entities/dan-xie]]"
  - "kailing tu"
concepts:
  - "[[30-Concepts/scout-variant-caller]]"
  - "[[30-Concepts/monovar]]"
  - "[[30-Concepts/sccaller]]"
  - "[[30-Concepts/allele-dropout]]"
  - "[[30-Concepts/scwga]]"
  - "[[40-Topics/somatic-mosaicism]]"
topics:
  - "[[40-Topics/scdna-seq]]"
  - "[[40-Topics/whole-genome-amplification]]"
---

**Citation:** Tu et al. (2021) — *SCOUT: single-cell genotyping using local-territory base counts* — *Nucleic Acids Research*. [DOI](https://doi.org/10.1093/nar/gkab106)

# Tu et al. 2021 — SCOUT

> Thesis: Existing single-cell SNV callers (Monovar, SCcaller, SCAN-SNV) lean on **external data** — matched bulk samples or other cells in the experiment — to calibrate allele-dropout and amplification bias. This fails for minor clones and rare variants where the external data is unreliable. **SCOUT** instead borrows information from **adjacent genomic loci within the same cell** (the "local genome territory"), assuming that neighboring SNVs share amplification context. A four-class statistical model classifies each candidate locus as homozygous, heterozygous, intermediate (amplification-imbalanced), or low-major-allele (potential allele dropout).

## Key claims

- **Statistical model**: each locus *s* has latent state *Z_s* ∈ {0,1,2,3} for {homozygous, heterozygous, intermediate, low-major-allele}. Multinomial likelihood over the four ranked allele counts. Smoothing over adjacent loci within a 30 kb window using local linear fitting. Exponential distance weighting (μ chosen so SNVs 10 kb away have weight ½).
- **Initialization** uses hierarchical clustering of major-allele frequencies within 30-kb segments (Ward, Euclidean distance) to seed homozygous vs heterozygous labels.
- Allele-dropout (ADO) flag is raised if a locus is in a 30-kb region with no heterozygous loci or >40% error-flagged loci.
- **Performance**: 2.0–77.5% F1 improvement over GATK, SCcaller, and Monovar across real and simulated datasets, even when SCcaller is given external heterozygous calls.
- **Speed**: 400% average acceleration over alternatives via 2-Mb genome partitioning and multiprocessing. Linear time in sequence length.

## Methods / evidence

Real scDNA-seq from MDA-amplified Xiao Dong et al. (IL-11, IL-12) with unamplified clonal-bulk benchmark (IL-1c). Simulated datasets via downsampling. Comparisons to GATK 4.1.1.0, SCcaller 2.0.0, Monovar.

## Surprising or load-bearing bits

- The conceptual insight is **using local genomic context as an internal control** when external context is unreliable. This is the inverse of the SCcaller/SCAN-SNV philosophy. For minor clones, the within-cell signal is the only reliable signal.
- The 400% speedup is significant — single-cell genotyping at population scale is often I/O- and compute-bound rather than algorithmically interesting, so engineering matters.

## Connections to other sources

- One of the "what comes after MDA-bias correction" papers; competes with Monovar (Zafar et al. 2016) and SCcaller (Dong et al. 2017).
- Pre-PTA paper; the PTA era of scWGA ([[10-Summaries/shao-2025-scDNA-mosaicism-review]], [[10-Summaries/luquette-2025-pta-duplex-mosaicism]]) somewhat reduces but does not eliminate the need for SCOUT-style callers — amplification bias still exists.
- Connects to [[40-Topics/somatic-mosaicism]] tooling stack — alongside [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] which validates DS at the bulk level, SCOUT validates calls at the cell level.

## Open questions

- Not benchmarked against modern PTA-tuned callers (e.g., SCAN2). The 2021 comparator set is now somewhat stale.
- No support for indels or structural variants.

---
**Source:** [DOI](https://doi.org/10.1093/nar/gkab106)
## Related

- [[40-Topics/scdna-seq]] · [[30-Concepts/scwga]] · [[30-Concepts/allele-dropout]] · [[40-Topics/somatic-mosaicism]]
