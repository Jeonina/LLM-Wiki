---
type: summary
title: "Peter 2024 — Single chromatin fiber profiling and nucleosome position mapping in the human brain"
source: "[[00-Sources/papers/Single chromatin fiber profiling and nucleosome position mapping in the human brain]]"
aliases: ["Peter 2024 brain Fiber-seq", "brain Fiber-seq"]
tags: [Fiber-seq, brain, nucleosome-positioning, single-molecule, m6A, FACS-NeuN, Akbarian-lab, Stergachis-lab, Mt-Sinai]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Peter et al. (2024) — *Single chromatin fiber profiling and nucleosome position mapping in the human brain* — *CellReportsMethods*. [DOI](https://doi.org/10.1016/j.crmeth.2024.100911)

Peter, Agarwal, Watanabe, Kassim, Wang, Lambert, Javidfar, Evans, Dawson, Fridrikh, Girdhar, Roussos, Nageshwaran, Tsankova, Sebra, Vollger, Stergachis, Hasson and Akbarian (Mt Sinai, UW, JPVAMC) adapted **Fiber-seq** (Stergachis 2020) to **FACS-sorted NeuN+ neuronal and NeuN− non-neuronal nuclei from human brain tissue**. The protocol uses amplification-free m6A-methyltransferase (Hia5) tagging of extranucleosomal DNA in situ, followed by long-read PacBio Sequel II/Revio sequencing of ~10 kb chromatin fibers.

Key brain-specific capabilities: (i) genome-scale long-read nucleosomal-position mapping in neurons (no prior method existed for brain); (ii) single-molecule TF-footprinting in cell-type-resolved nuclei; (iii) haplotype-specific chromatin patterns identified via heterozygous-SNP read phasing; (iv) cis-aligned multiple regulatory elements on individual fibers — capturing the coordination of distal enhancer-promoter accessibility states on the same molecule; (v) accessible chromatin at ~20,000 sites in retrotransposons and other repeats unmappable by short-read epigenomics.

## Why this matters

Brain-specific application of Fiber-seq that bridges single-molecule footprinting (§3.2) to brain-somatic-mosaicism research (§5). The cell-type-resolved (NeuN+/−) FACS-sorted approach gives population-level resolution adequate for neuronal vs glial chromatin questions, while preserving the per-molecule coordination information that distinguishes Fiber-seq from short-read scATAC-seq. Anchors §3.2 (Fiber-seq applications to disease tissue) and §5 (neuroscience applications — chromatin-level mosaicism analogue of scWGS brain studies). Methodological lineage: Stergachis 2020 founding Fiber-seq → Peter 2024 brain adaptation → likely future single-nucleus Fiber-seq.

---
**Source:** [DOI](https://doi.org/10.1016/j.crmeth.2024.100911) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/39631398/)

## Related

- [[10-Summaries/andrewb-2020-science]]
- [[10-Summaries/bohaczuk-2024-targeted-fiberseq]]
- [[10-Summaries/shipony-2020-smac]]
- [[20-Entities/andrew-b-stergachis]]
- [[40-Topics/brain-somatic-mosaicism]]
