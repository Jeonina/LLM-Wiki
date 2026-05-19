---
type: summary
title: "Swanson 2025 — DAF-seq: mapping single-cell diploid chromatin fiber architectures"
source: "[[00-Sources/papers/Mapping single-cell diploid chromatin fiber architectures using DAF-seq]]"
aliases: ["Swanson 2025 DAF-seq", "DAF-seq", "scDAF-seq"]
tags: [DAF-seq, scDAF-seq, single-molecule-footprinting, deaminase, SsdddA, cytidine-deaminase, haplotype-resolved, Stergachis-lab]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Swanson et al. (2025) — *DAF-seq: mapping single-cell diploid chromatin fiber architectures* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-025-02914-3)

Swanson, Mao, Mallory et al. (Stergachis lab; UW Seattle + WashU + Brotman Baty) developed **DAF-seq** (Deaminase-Assisted single-molecule chromatin Fiber sequencing), replacing the methyltransferase footprinting of Fiber-seq/SMAC-seq with a **cytidine deaminase (SsdddA)** that converts accessible cytosines to uracils (read as C→T mutations after amplification). Advantages: (i) near-nucleotide resolution; (ii) synchronous readout of single-molecule chromatin states + DNA sequence variants (germline or somatic) on the same fiber; (iii) the deamination pattern itself serves as a molecule-specific UMI, removing PCR-duplicate confusion. Single-cell variant **scDAF-seq** produces chromosome-length protein co-occupancy maps across 99% of each individual cell's mappable genome. Reveals 61% chromatin-actuation divergence between haplotypes within a cell and 63% between cells, and shows regulatory elements are preferentially co-actuated along the same fiber in a distance-dependent manner mirroring cohesin loops.

## Why this matters

State-of-the-art 2025 single-molecule footprinting method that **integrates somatic mosaicism detection with chromatin readout on the same molecule** — a fundamentally new capability for §3.3 (SMF) and §5 (somatic mosaicism applications). Major advance over Fiber-seq family: m6A-based footprints don't preserve sequence, so cannot detect SNVs on the footprinted molecule; DAF-seq's C→T conversion encodes both. Haplotype-resolved chromatin actuation at single-cell single-molecule resolution is unprecedented. Existing `swanson2025` bibkey present. Anchors the convergence of duplex/single-molecule scDNA and SMF — relevant to §6 future-perspectives discussion.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-025-02914-3) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/41339527/)

---
**Source:** [DOI](https://doi.org/10.1038/s41587-025-02914-3) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/41339527/)

## Related

- [[10-Summaries/shipony-2020-smac]]
- [[10-Summaries/lee-2020-nanonome]]
- [[10-Summaries/bohaczuk-2024-targeted-fiberseq]]
- [[10-Summaries/peter-2024-brain-fiberseq]]
- [[10-Summaries/doughty-2024-smf-tf]]
- [[20-Entities/andrew-stergachis]]
