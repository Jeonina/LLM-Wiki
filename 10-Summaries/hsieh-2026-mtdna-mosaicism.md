---
type: summary
title: "Glynos et al. 2023 — single-cell mtDNA heteroplasmy: random drift drives life-long divergence"
source: "[[00-Sources/papers/High-throughput single-cell analysis reveals progressive mitochondrial DNA mosaicism throughout life]]"
source_kind: paper
author: "Angelos Glynos, Lyuba V. Bozhilova, Michele Frison, Stephen Burr, James B. Stewart, Patrick F. Chinnery (corresponding)"
published: 2023-10-26
ingested: 2026-05-12
doi: "10.1126/sciadv.adi4038"
journal: "Science Advances"
tags: [mitochondrial-DNA, heteroplasmy, single-cell, genetic-drift, aging, mtDNA-disease]
entities:
  - "[[20-Entities/patrick-chinnery]]"
  - "[[20-Entities/james-stewart]]"
concepts:
  - "[[30-Concepts/mitochondrial-heteroplasmy]]"
  - "[[30-Concepts/somatic-mosaicism]]"
  - "[[30-Concepts/kimura-distribution]]"
  - "[[30-Concepts/lineage-tracing]]"
topics:
  - "[[40-Topics/somatic-mosaicism]]"
  - "[[40-Topics/scdna-seq]]"
---

**Citation:** Glynos et al. (2023) — *single-cell mtDNA heteroplasmy: random drift drives life-long divergence* — *Science Advances*. [DOI](https://doi.org/10.1126/sciadv.adi4038)

# Glynos et al. 2023 — single-cell mtDNA heteroplasmy: random drift drives life-long divergence

> Thesis: Cell-to-cell variance in mitochondrial DNA heteroplasmy levels emerges prenatally and increases monotonically throughout life — even in non-dividing tissues — driven by random genetic drift acting through mtDNA turnover (relaxed replication), not vegetative segregation alone. Two pathogenic mt-tRNA mutations (m.5024C>T, m.5019A>G) segregate at different intrinsic rates, providing a clean explanation for clinical variability in mitochondrial disease.

## Key claims

- ~4,500 single cells genotyped via FACS + pyrosequencing from mouse models at E8.5, P0, P6, P100, and P365 across spleen (rapidly dividing) and brain (mostly post-mitotic).
- Bulk-tissue heteroplasmy is stable across organs (low variance), but **single-cell variance is huge and grows with age**: e.g., 0.4% homoplasmic at P0 → 9.1% homoplasmic at P365 for m.5024C>T.
- Single-cell heteroplasmy distributions **fit a two-parameter Kimura distribution** at every time point and tissue — i.e., the data are quantitatively consistent with random genetic drift, no selection required.
- Surprisingly, spleen (dividing) and brain (postmitotic) have **the same heteroplasmy variance trajectory**. Models that include only vegetative segregation predict a >6-fold spleen/brain difference. The data instead implicate mtDNA turnover (replication-independent destruction-and-resynthesis) as the dominant force — and imply brain mtDNA turnover may be faster than previously thought.
- Therapeutic counterintuition: **slowing mtDNA turnover** (rather than boosting copy number) may slow disease progression by slowing drift. The current strategy of boosting biogenesis could backfire if it accelerates turnover.

## Methods / evidence

FACS sorting of single cells (CD19+/− splenocytes; ACSA-1+, PSD95+, prominin-1+ brain cells) → single-cell pyrosequencing-based heteroplasmy assay (~2.8% mean absolute deviation). Two pathogenic mt-Ta mutations in C57BL/6J backgrounds. Cross-tissue + cross-time-point design. Kimura-distribution fits and Wright/turnover-adjusted variance modeling.

## Surprising or load-bearing bits

- The dominant force is mtDNA turnover, not cell division. This **reframes the cause of progressive mtDNA disease**: not "more divisions → more error" but "more destruction-and-resynthesis cycles → more drift."
- The drop in variance from P0 to P6 is anomalous and unexplained — possibly mitophagic clearance of embryonic mitochondria. Flagged as open question.

## Connections to other sources

- Single-cell mtDNA mosaicism is one strand of the broader mosaicism atlas synthesized in [[10-Summaries/bizzotto-2022-brain-mosaicism-review]] and [[10-Summaries/diane-2025-naturereviewsgenetics]].
- The Kimura-drift framing connects to lineage-tracing approaches: drift-driven heteroplasmy is the basis for [[30-Concepts/mitochondrial-lineage-tracing]] and the mtscATAC-seq/EMBLEM methods that exploit mtDNA mutation accumulation for human lineage reconstruction.
- Provides a counterpoint to selection-based explanations of clinical mtDNA disease heterogeneity.

## Open questions

- Why does heteroplasmy variance dip at P6? Mitophagic clearance of embryonic mitochondria is suggested but unproven.
- Only two mt-tRNA mutations tested in one gene (mt-Ta). Generalization to protein-coding or mt-rRNA mutations is open.

---
**Source:** [DOI](https://doi.org/10.1126/sciadv.adi4038)
## Related

- [[40-Topics/somatic-mosaicism]] · [[30-Concepts/mitochondrial-heteroplasmy]] · [[30-Concepts/kimura-distribution]]
