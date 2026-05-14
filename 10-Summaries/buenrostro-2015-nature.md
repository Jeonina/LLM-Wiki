---
type: summary
title: "Buenrostro 2015 — Single-cell chromatin accessibility reveals principles of regulatory variation"
aliases: ["Buenrostro 2015 Nature", "scATAC-seq founding paper", "Fluidigm scATAC"]
tags: [scATAC-seq, accessibility, founding-method, Greenleaf-lab, Chang-lab, Stanford, regulatory-variation]
created: 2026-05-13
updated: 2026-05-13
sources: ["Jason_2015_Nature.pdf"]
---

Buenrostro, Wu, Litzenburger, Ruff, Gonzales, Snyder, Chang and Greenleaf (Stanford) reported the founding **single-cell ATAC-seq** method on a programmable microfluidics platform (Fluidigm C1). The protocol captures and tags individual cells on integrated fluidic circuits (IFCs), then performs Tn5 transposition and PCR with cell-identifying barcodes, producing scATAC-seq libraries from 254 individual GM12878 lymphoblastoid cells per run. Aggregate single-cell profiles reproduce ensemble DNase-seq (Pearson r = 0.80) and bulk ATAC-seq accessibility profiles.

Beyond the method, the paper reveals **principles of regulatory variation** by analyzing accessibility variance across 1,632 IFC chambers on ENCODE Tier-1 lines (H1-ESC, K562, GM12878) + EML1, HL-60, BJ, V6.5. Key findings: (i) accessibility variance is systematically associated with specific *trans-* and *cis-*elements; (ii) GATA1, GATA2, JUN, STAT2, BRG1/SMARCA4, p300 act as high-variance trans-factors; CTCF, SUZ12, ZNF143 act as general suppressors of accessibility variance (when not co-bound with cohesin); (iii) trans-factor *combinations* synergize to induce or suppress cell-to-cell variability; (iv) cis-variance patterns recapitulate 3D chromosome-compartment organization de novo from single-cell data.

## Why this matters

The founding scATAC-seq paper (parallel to Cusanovich 2015 sci-ATAC-seq); methodological ancestor of every later scATAC-seq protocol (10x Multiome, sci-ATAC-seq v3, etc.). Beyond the method, this paper establishes that **single-cell accessibility variance is itself a biologically informative signal**, not just noise — a principle our review's locus-state framework explicitly builds on. Anchors §3.2 (accessibility chemistries) and §5 (cancer biology applications). Existing `buenrostro2015` bibkey already present.

---
**Source:** [DOI](https://doi.org/10.1038/nature14590) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/26083756/)

## Related

- [[10-Summaries/cusanovich-2015-science]]
- [[10-Summaries/jin-2015-nature]]
- [[10-Summaries/buenrostro-2013-natmethods]]
- [[20-Entities/william-greenleaf]]
- [[30-Concepts/scatac-seq]]
