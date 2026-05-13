---
type: concept
title: IGS (In Situ Genome Sequencing)
aliases: [IGS, in situ genome sequencing, Payne IGS]
tags: [3d-genome, in-situ-sequencing, single-cell, spatial-genomics, method]
created: 2026-05-12
updated: 2026-05-12
---

# IGS (In Situ Genome Sequencing)

> Sequences DNA **directly inside fixed cells**, then matches each in-situ read to a high-quality ex-situ paired-end read of the same amplicon — yielding thousands of genomic paired-end reads with (x, y, z) spatial coordinates per cell. Spatial-3D-DNA analog of what Hi-C / scHi-C measure as contact frequency.

## Definition

Payne et al. 2021 ([[10-Summaries/andrewc-2020-science]]). Three phases:

1. **In situ library construction**: Tn5 tagmentation inserts adapters at random genomic positions in fixed cells; fragments are circularized in place by hairpin ligation with a UMI, then clonally amplified by rolling-circle amplification → punctate ~400–500 nm amplicons.
2. **Multimodal sequencing**: 18 rounds of in-situ sequencing-by-ligation + 4-channel fluorescence imaging read each amplicon's UMI at its 3D spatial position. Amplicons are then dissociated → PCR → ex-situ Illumina paired-end sequencing reads the genomic insert.
3. **Computational integration**: probabilistic matching pairs each ex-situ paired-end read with its in-situ UMI/position via single-bit error correction.

## Why it matters

- **Genome-wide DNA sequence + (x, y, z) position in the same nucleus** — neither Hi-C nor DNA FISH nor scHi-C can do this. Hi-C gives contact frequency, FISH gives spatial position at a handful of loci, scHi-C gives single-cell contacts but no absolute position.
- Applied to 106 PGP1 human fibroblasts + 113 mouse embryo cells (PN4 zygote, late 2-cell, early 4-cell) — 66% of resolvable amplicons confidently matched in-situ ↔ ex-situ, giving thousands of spatially-located paired-end reads per cell.
- **Parent-of-origin chromosome territories** in mouse zygote distinguished via SNPs — direct imaging of maternal vs paternal pronuclei mixing during early development.
- **Epigenetic memory of chromosome positioning**: clonal daughter cells retain similar chromosome-territory arrangements.

## Variants and refinements

- **IGS** ([[10-Summaries/andrewc-2020-science]]).
- Methodological cousin (in spirit only — different chemistry): [[single-cell-hi-c]], [[dip-c]], [[sn-m3c-seq]] (chromatin conformation in single cells without absolute spatial coordinates).

## Contested points

- 66% UMI matching rate means a substantial fraction of reads cannot be spatially localized.
- Throughput is image-acquisition-limited (18 rounds × multi-channel imaging per cell).
- Currently applied to fibroblasts and early embryos; primary-tissue generalization not yet demonstrated.

## Why the filename is misleading

The source file `AndrewC_2020_Science.pdf` is named for first author Andrew C. Payne, not Andrew B. Stergachis (who authored `AndrewB_2020_Science.pdf` = [[fiber-seq]]). Despite the similar filename, IGS and Fiber-seq are methodologically unrelated.

## Related

- [[3d-genome]]
- [[single-cell-hi-c]]
- [[dip-c]]
- [[tn5-tagmentation]]
- [[umi-molecular-barcoding]]
- [[40-Topics/3d-genome]]
- [[40-Topics/single-cell-multiomics]]
