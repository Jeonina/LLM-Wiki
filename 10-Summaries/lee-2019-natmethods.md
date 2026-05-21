---
type: summary
title: "Lee 2019 — Simultaneous profiling of 3D genome structure and DNA methylation in single human cells (sn-m3C-seq)"
source: "[[00-Sources/papers/Simultaneous profiling of 3D genome structure and DNA methylation in single human cells]]"
aliases: ["sn-m3C-seq", "Lee 2019", "single-nucleus methyl-3C"]
tags: [sn-m3C-seq, 3D-genome, methylome, joint-assay, brain, Ecker-lab, Dixon-lab]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Lee et al. (2019) — *Simultaneous profiling of 3D genome structure and DNA methylation in single human cells (sn-m3C-seq)* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-019-0547-z)

Lee, Luo, Zhou and colleagues (Ecker / Dixon labs) introduced sn-m3C-seq, a joint single-nucleus assay that reads chromatin conformation (3C/Hi-C) and DNA methylation from the same DNA molecule. Nuclei are first crosslinked, restriction-digested and ligated in situ (canonical Hi-C chemistry through ligation), then FANS-sorted into 384-well plates and processed with bisulfite conversion + snmC-seq2 library chemistry. Because cytosine methylation is unaltered by 3C, the two layers are recoverable from the same fragment.

Applied to 4,238 single human prefrontal cortex nuclei, sn-m3C-seq generated joint readouts that cluster cells into 14 cortical cell types from the methylome alone, and reveals cell-type-specific chromatin conformation maps for each type. The two modalities are strongly cross-correlated within cells: cell types distinguished by methylation show distinct chromatin contact patterns at enhancer-promoter pairs, suggesting pervasive interaction between methylation programs and 3D genome architecture. Bulk m3C-seq libraries from mESCs validated the chemistry against conventional Hi-C and methylC-seq (SCC = 0.91, Pearson = 0.82 respectively).

## Why this matters

The founding single-nucleus joint methylome + 3D-genome assay. Demonstrates that two epigenetic layers of the locus state can be measured on the same molecule of DNA, not just in the same cell. Anchors §3.5 (3D genome organization), §2 (joint-assay table), and the methylome + 3C atlas of Liu 2023. Resolves the question of whether 3D-contact maps can be clustered to cell types in primary tissue (yes — and methylation does the clustering).

---
**Source:** [DOI](https://doi.org/10.1038/s41592-019-0547-z) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/31501549/)

---
**Source:** [DOI](https://doi.org/10.1038/s41592-019-0547-z) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/31501549/)

## Related

- sn m3C seq
- [[30-Concepts/single-cell-hi-c]]
- [[30-Concepts/joint-single-cell-multi-omics]]
- [[10-Summaries/liu-2023-mouse-brain-methylome-3d]]
- [[10-Summaries/luo-2018-snmc-seq2]]
- [[20-Entities/joseph-ecker]]
