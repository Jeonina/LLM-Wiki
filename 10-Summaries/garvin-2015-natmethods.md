---
type: summary
title: "Garvin 2015 — Interactive analysis and assessment of single-cell copy-number variations (Ginkgo)"
source: "[[00-Sources/papers/Interactive analysis and assessment of single-cell copy-number variations]]"
aliases: ["Ginkgo", "Garvin 2015"]
tags: [computational, CNV, scDNA-seq, Ginkgo, web-tool, Wigler-lab, Schatz-lab]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Garvin et al. (2015) — *Interactive analysis and assessment of single-cell copy-number variations (Ginkgo)* — *Nature Methods*. [DOI](https://doi.org/10.1038/nmeth.3578)

Garvin, Aboukhalil, Kendall and colleagues (Wigler / Schatz labs, Cold Spring Harbor) introduced Ginkgo, an open-source web platform for single-cell copy-number variation analysis. Ginkgo handles the distinctive challenges of single-cell CNV calling: extremely low sequencing depth (<1×), WGA-induced read-count distortion, bad-bins from poorly-assembled genome regions, integer-level copy-number calling at single-cell resolution, and absent population structure that bulk CNV callers can leverage.

The pipeline: bin reads into genome-wide regions, perform GC-bias correction, segment, call integer copy number per bin, and visualize results in an interactive web interface with phylogenetic-tree construction. Ginkgo validated against five major scDNA-seq studies and benchmarked DOP-PCR, MDA, and MALBAC for CNV consistency; DOP-PCR was found to be the most consistent for CNV analysis at the time. Supports human, chimp, mouse, rat, and fly.

## Why this matters

A widely-used early single-cell CNV pipeline that established the read-binning + GC-correction + integer-segmentation approach now standard in DLP+/Strand-seq/scDNA workflows. Anchors §4 (computational framework, CNV branch). Complement to the SNV-calling tools (Monovar, SCAN-SNV, LiRA, ProSolo) — same data-quality problems, different downstream question.

---
**Source:** [DOI](https://doi.org/10.1038/nmeth.3578) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/26344043/)

## Related

- [[30-Concepts/single-cell-cnv]]
- [[10-Summaries/zafar-2016-natmethods]]
- [[10-Summaries/luquette-2019-natcomm]]
