---
type: summary
title: "Geisenberger et al. 2025 — scEpi²-seq: simultaneous single-cell histone marks and 5mC"
source: "[[00-Sources/papers/Simultaneous single-cell analysis of 5mC and 5hmC with SIMPLE-seq]]"
source_kind: paper
author: "Christoph Geisenberger, Jeroen van den Berg, Vincent van Batenburg, Buys de Barbanson, Anna Lyubimova, Joe Verity-Legg, Xiufei Chen, Yibin Liu, Chun-Xiao Song, Jeroen de Ridder, Alexander van Oudenaarden (corresponding)"
published: 2025-09-25
ingested: 2026-05-12
doi: "10.1038/s41592-025-02847-4"
journal: "Nature Methods"
tags: [single-cell, multi-omics, histone-modifications, DNA-methylation, TAPS, sortChIC, FUCCI, intestine]
entities:
  - "[[20-Entities/alexander-van-oudenaarden]]"
  - "[[20-Entities/christoph-geisenberger]]"
  - "[[20-Entities/chun-xiao-song]]"
concepts:
  - "[[30-Concepts/scepi2-seq]]"
  - "[[30-Concepts/sortchic]]"
  - "[[30-Concepts/taps]]"
  - "[[30-Concepts/histone-modifications]]"
  - "[[30-Concepts/dna-methylation]]"
  - "[[30-Concepts/replication-timing]]"
  - "[[30-Concepts/uhrf1]]"
topics:
  - "[[40-Topics/histone-modifications]]"
  - "[[40-Topics/dna-methylation]]"
  - "[[40-Topics/single-cell-multiomics]]"
---

**Citation:** Geisenberger et al. (2025) — *scEpi²-seq: simultaneous single-cell histone marks and 5mC* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-025-02847-4)

# Geisenberger et al. 2025 — scEpi²-seq

> Thesis: Single-cell methods exist for either DNA methylation or histone modifications, but bisulfite chemistry destroys the small CUT&Tag/ChIC fragments and prevents joint readout. **scEpi²-seq** swaps bisulfite for TAPS (which converts 5mC → uracil non-destructively) and combines it with sortChIC (pA-MNase tethered to histone-modification antibodies, FACS-sorted single cells) to deliver simultaneous histone + 5mC + nucleosome-positioning measurements per cell. Using RPE-1 FUCCI cells, this resolves DNA-methylation maintenance kinetics across the cell cycle; using mouse intestine, it dissects lineage-specific methylation within H3K27me3 domains.

## Key claims

- **Method**: pA-MNase + antibody (H3K9me3, H3K27me3, H3K36me3) → MNase digestion → in-plate barcoded adaptor ligation → TAPS conversion → IVT/RT/PCR. Yields chromatin cut-site map, nucleosome spacing (read-start distances), and CpG methylation calls — all from the same single cell.
- **Quality**: ~95% C→T conversion of CpG-methylated spike-ins. Fraction Reads in Peaks 0.72–0.88. >50,000 CpGs per cell on average. Pearson > 0.9 vs bulk WGBS at 10-kb bins; > 0.8 at single-CpG.
- **Chromatin-context-dependent methylation**: H3K36me3 regions are highly methylated (~50%); H3K27me3 and H3K9me3 regions are hypomethylated (8–10%) — consistent with the relative gene-body vs facultative-/constitutive-heterochromatin distinction.
- **Cell-cycle dynamics (RPE-1 FUCCI)**: methylation transiently drops during S-phase for each histone mark, with H3K9me3-marked late-replicating regions taking longest to recover (maintenance methylation extends into G1). **Nucleosome-covered DNA loses up to 12% methylation through S-phase, vs 4% at linker DNA** — nucleosomes block DNMT1 access.
- **Mouse intestine (H3K27me3 + 5mC)**: identifies absorptive, secretory (enteroendocrine + goblet), and immune (B/T/myeloid) cells; immune cells have lower H3K27me3 but higher 5mC than epithelial cells, suggesting **DNA methylation provides an additional repressive layer within facultative heterochromatin** that operates independently of PRC2.

## Methods / evidence

K562 and RPE-1 hTERT FUCCI cell lines + mouse small intestine (proximal/middle/distal). MNase-based pA-MNase chromatin profiling combined with TAPS chemistry. FACS plate-based sorting (384-well). Integration with scEdU-seq for replication timing. Three histone marks: H3K9me3, H3K27me3, H3K36me3.

## Surprising or load-bearing bits

- The **nucleosome-occupancy-blocks-DNMT1 mechanism** for delayed methylation maintenance is a clean single-cell-resolved result that links a longstanding in-vitro biochemistry observation (DNMT1 is blocked by nucleosomes) to in-vivo cell-cycle kinetics.
- The intestinal immune-cell finding is biologically interesting: lineage-specific gene regulation may use DNA methylation as an additive layer over PRC2/H3K27me3, rather than as an alternative.
- Replication timing dominates maintenance kinetics — not the specific histone mark per se. Late-replicating regions of all flavors recover methylation more slowly.

## Connections to other sources

- Closely related to [[10-Summaries/tavares-2026-6-base-cut-tag]] (6-base-CUT&Tag, also pairs histone marks with DNA modifications) but scEpi²-seq is single-cell vs bulk, and uses MNase vs Tn5.
- Builds directly on sortChIC (Zeller et al.). Complements MulTI-Tag / [[10-Summaries/janssens-2023-scicut-tag]] (sciCUT&Tag) for multi-mark single-cell chromatin profiling.
- Replication-timing analysis depends on scEdU-seq (van den Berg lab).
- The cell-cycle methylation-maintenance result complements [[10-Summaries/fu-2025-longread-methylation]] (long-read methylation review) and [[10-Summaries/kim-2017-methylation-memory-review]] (Kim/Costello 2017).

## Open questions

- TAPS doesn't distinguish 5mC from 5hmC, though 5hmC is ~30× less abundant. For tissues like brain where 5hmC matters, this conflation is a real limit.
- Throughput per experiment is plate-based (384-well); ~600–1,700 cells passing QC. Lower than Tn5-based methods.

---
**Source:** [DOI](https://doi.org/10.1038/s41592-025-02847-4)
## Related

- [[40-Topics/histone-modifications]] · [[30-Concepts/scepi2-seq]] · [[30-Concepts/sortchic]] · [[30-Concepts/taps]] · [[20-Entities/alexander-van-oudenaarden]]
