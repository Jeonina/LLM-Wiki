---
type: summary
title: "Shipony 2020 — Long-range single-molecule mapping of chromatin accessibility in eukaryotes (SMAC-seq)"
source: "[[00-Sources/papers/Long-range single-molecule mapping of chromatin accessibility in eukaryotes]]"
aliases: ["Shipony 2020", "SMAC-seq", "single-molecule chromatin accessibility"]
tags: [SMAC-seq, single-molecule, m6A, nanopore, accessibility, long-read, Greenleaf-lab, Stanford]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Shipony et al. (2020) — *Long-range single-molecule mapping of chromatin accessibility in eukaryotes (SMAC-seq)* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-019-0730-2)

Shipony, Marinov, Swaffer, Sinnott-Armstrong, Skotheim, Kundaje and Greenleaf (Stanford) developed **SMAC-seq** (Single-Molecule long-read Accessible Chromatin mapping sequencing assay), which uses **EcoGII** N6-methyladenosine (m6A) methyltransferase to mark open chromatin combined with CpG/GpC 5mC methyltransferases (M.CviPI, M.SssI), followed by Oxford Nanopore long-read sequencing to read out methylation status base-by-base on individual chromatin fibers.

By combining m6A and CpG/GpC marks, SMAC-seq achieves a theoretical accessibility resolution of ~3 bp in all model organisms — substantially better than CpG-only or GpC-only methods which suffer from sparse dinucleotide spacing in some genomes. SMAC-seq footprints individual nucleosome positions, transcription-factor occupancy, and the **coordination of accessibility states at distal regulatory elements on the same molecule** — a capability that short-read DNase-seq, ATAC-seq, and NOMe-seq fundamentally cannot deliver.

## Why this matters

Conceptual ancestor of Fiber-seq (Stergachis 2020) which substitutes Hia5 m6A methyltransferase and adds PacBio readout. SMAC-seq established the principle that long-read methylation footprinting can resolve the *coordination* of multiple regulatory elements on a single fiber, not just their independent accessibility levels. Anchors §3.2 (single-molecule footprinting family: SMF, SAMOSA, SMAC, Fiber-seq, HiDef-seq) and supports the review's emphasis on phased multi-element observation as a distinct capability that bulk and short-read single-cell methods both lack.

---
**Source:** [DOI](https://doi.org/10.1038/s41592-019-0730-2) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32042188/)

---
**Source:** [DOI](https://doi.org/10.1038/s41592-019-0730-2) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32042188/)

## Related

- [[10-Summaries/andrewb-2020-science]]
- [[10-Summaries/abdulhay-2020-samosa]]
- swanson 2025 stamseq
- [[30-Concepts/single-molecule-footprinting]]
