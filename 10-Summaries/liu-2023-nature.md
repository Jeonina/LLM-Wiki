---
type: summary
title: "Liu 2023 — Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain"
aliases: ["snmC-seq3 brain atlas", "snm3C-seq atlas", "Liu 2023"]
tags: [snmC-seq3, snm3C-seq, methylation, 3D-genome, brain-atlas, BICCN, joint-assay]
created: 2026-05-13
updated: 2026-05-13
sources: ["Hanqing_2023_Nature.pdf"]
---

Liu, Zeng, Zhou and colleagues (Ecker lab) generated the most comprehensive single-cell DNA-methylation and chromatin-conformation atlas of a mammalian brain: 301,626 single-nucleus methylomes (snmC-seq3) and 176,003 joint methylome + 3C contact maps (snm3C-seq) from 117 dissected regions across 18 coronal slices of the adult C57BL/6 mouse brain.

Methylome-based iterative clustering produced 4,673 cell groups grouped into 274 subclasses, validated against companion BICCN transcriptome and ATAC-seq data and registered to the Allen Common Coordinate Framework. The atlas identifies 2.6 million differentially methylated regions (DMRs) as candidate regulatory elements, demonstrates cell-type- and region-specific patterns of both CpG (mCG) and non-CpG (mCH) methylation, and validates spatial methylation diversity by MERFISH-based in situ transcriptomics.

The snm3C-seq joint assay reads methylome and chromatin conformation from the same nucleus, revealing that chromatin-conformation diversity at functionally important neuronal genes is highly correlated with methylation and transcription changes. The dataset enabled construction of cell-type-specific regulatory networks linking TFs, DMRs and target genes, and showed that intragenic methylation and conformation patterns predict alternative isoform usage (validated against whole-brain SMART-seq2). Resources are accessible at mousebrain.salk.edu.

## Why this matters

The current state-of-the-art demonstration that two epigenetic modalities (methylome + 3D genome) can be read jointly from the same single cell at brain-atlas scale, and that the joint readout resolves regulatory biology unavailable to either modality alone. Anchors §2 (locus-state joint-assay), §3.3 (methylation), §3.5 (3D genome), §5 (atlas applications). Demonstrates that "joint reading of two layers of the locus state at scale" is no longer aspirational.

## Related

- [[30-Concepts/snmC-seq-family]]
- [[30-Concepts/sn-m3C-seq]]
- [[30-Concepts/joint-single-cell-multi-omics]]
- [[40-Topics/brain-atlases]]
- [[10-Summaries/chongyuan-2018-naturecommunications]]
- [[20-Entities/joseph-ecker]]
