---
type: summary
title: "Xiao 2025 — Tracking single-cell evolution using clock-like chromatin accessibility loci (EpiTrace)"
aliases: ["Xiao 2025", "EpiTrace", "ClockDML"]
tags: [EpiTrace, ClockDML, mitotic-clock, scATAC-seq, lineage-tracing, chromatin-accessibility, Zhang-lab, Wuhan]
created: 2026-05-13
updated: 2026-05-13
sources: ["Yu_2025_NatureBiotechnology.pdf"]
---

Xiao, Jin, Ju, Fu, Wang, Yu, Chen, Qian, Wang and Zhang (Wuhan / Hong Kong UST / Peking-Tsinghua) developed **EpiTrace**, a method that infers single-cell mitotic age from scATAC-seq data using **clock-like differential-methylation loci** (ClockDML) — genomic regions whose DNA-methylation state drifts predictably with cell division. The central observation: as cells undergo mitosis, the heterogeneity of chromatin accessibility on clock-like loci is *reduced*, providing a measurable molecular clock.

The method: identify 126,420 ClockDML in the human genome by bisulfite capture sequencing of CpG islands across donors of different ages; profile the same loci's accessibility from scATAC-seq via a hidden Markov model with diffusion-smoothing to reduce single-cell sparseness; refine the reference set by iteration to maximize age-correlation. EpiTrace tracks cell-age in single cells, concords with known developmental hierarchies, and correlates with DNAm-based clocks at population scale.

Applications shown: hematopoiesis trajectory recovery, organ-development tracing, tumor-biology mitotic-age inference (cancer vs normal), and cortical gyrification timing. Important conceptual claim: chromatin-accessibility-based age inference is **independent of DNAm** — they are correlated but not causally linked in either direction; the same clock-like loci carry a parallel accessibility signal that exists "in species without active DNA methylation."

## Why this matters

A 2025 entrant in the lineage-tracing / cell-age space that complements mutation-based (LiRA, SCAN-SNV), epimutation-based (EPI-Clone, MethylTree), and mtDNA-based (MAESTER) approaches. The novelty is using **scATAC-seq alone** for mitotic-age inference — making the assay compatible with chromatin-state cohorts that lack methylation data. Anchors §3.3 (methylation/epimutation-based clocks; EpiTrace is the chromatin-axis sibling), §4 (computational lineage-tracing tools), and §5 (development + cancer applications).

---
**Source:** [DOI](https://doi.org/10.1038/s41587-024-02241-z) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/38724668/)

---
**Source:** [DOI](https://doi.org/10.1038/s41587-024-02241-z) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/38724668/)

## Related

- [[10-Summaries/scherer-2025-nature]]
- [[10-Summaries/chen-2025-methyltree]]
- [[30-Concepts/methylation-clones-epimutation]]
