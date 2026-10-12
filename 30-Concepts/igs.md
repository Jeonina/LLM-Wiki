---
type: concept
title: IGS (In Situ Genome Sequencing)
aliases: [IGS, in situ genome sequencing, Payne IGS]
tags: [3d-genome, in-situ-sequencing, single-cell, spatial-genomics, method]
created: 2026-05-12
updated: 2026-10-12
---

# IGS (In Situ Genome Sequencing)

> Sequences DNA **directly inside fixed cells**, then matches each in-situ read to a high-quality ex-situ paired-end read of the same amplicon — yielding hundreds to thousands of genomic paired-end reads with (x, y, z) spatial coordinates per cell; the spatial-3D-DNA analog of what Hi-C / scHi-C measure as contact frequency ([[10-Summaries/andrewc-2020-science|Payne 2021]]).

> [!abstract] 한눈에
> IGS는 고정된 세포 안에서 DNA를 직접 읽고, 같은 amplicon의 ex-situ paired-end read와 짝지어 각 read에 핵 안의 (x, y, z) 좌표를 붙이는 방법이다 ([[10-Summaries/andrewc-2020-science|Payne 2021]]). 접촉 빈도만 주는 Hi-C와 달리 절대 위치를 주지만, 짝지어지지 않는 amplicon이 적지 않다 ([[10-Summaries/andrewc-2020-science|Payne 2021]]).

## Definition

IGS was introduced by Payne et al. 2021 and runs in three phases ([[10-Summaries/andrewc-2020-science|Payne 2021]]):

1. **In situ library construction**: [[tn5-tagmentation|Tn5 tagmentation]] inserts adapters at random genomic positions in fixed cells; fragments are circularized in place by hairpin ligation with a UMI ([[umi-molecular-barcoding]]), then clonally amplified by rolling-circle amplification → punctate ~400–500 nm amplicons ([[10-Summaries/andrewc-2020-science|Payne 2021]]).
2. **Multimodal sequencing**: 18 rounds of in-situ sequencing-by-ligation + 4-channel fluorescence imaging read each amplicon's UMI at its 3D spatial position. Amplicons are then dissociated → PCR → ex-situ Illumina paired-end sequencing reads the genomic insert ([[10-Summaries/andrewc-2020-science|Payne 2021]]).
3. **Computational integration**: probabilistic matching pairs each ex-situ paired-end read with its in-situ UMI/position via single-bit error correction ([[10-Summaries/andrewc-2020-science|Payne 2021]]).

## Why it matters

IGS gives **genome-wide DNA sequence + (x, y, z) position in the same nucleus**, which neither Hi-C nor DNA FISH nor scHi-C can do ([[10-Summaries/andrewc-2020-science|Payne 2021]]).

| Method | What it reads | Source |
|---|---|---|
| Hi-C | Contact frequency | ([[10-Summaries/andrewc-2020-science\|Payne 2021]]) |
| DNA FISH | Spatial position at a handful of loci | ([[10-Summaries/andrewc-2020-science\|Payne 2021]]) |
| [[single-cell-hi-c\|scHi-C]] | Single-cell contacts but no absolute position | ([[10-Summaries/andrewc-2020-science\|Payne 2021]]) |
| IGS | Genome-wide sequence plus (x, y, z) position per read | ([[10-Summaries/andrewc-2020-science\|Payne 2021]]) |

## Variants and refinements

- **IGS** ([[10-Summaries/andrewc-2020-science|Payne 2021]]).
- Methodological cousins, in spirit only (different chemistry): [[single-cell-hi-c]], [[dip-c]] and sn m3c seq, which measure chromatin conformation in single cells without absolute spatial coordinates ([[10-Summaries/andrewc-2020-science|Payne 2021]]).

## Evidence and examples

- IGS was applied to 106 PGP1 human fibroblasts and 113 mouse embryo cells (PN4 zygote, late 2-cell, early 4-cell) ([[10-Summaries/andrewc-2020-science|Payne 2021]]).
- 66% of resolvable amplicons were confidently matched in-situ ↔ ex-situ, giving hundreds (fibroblasts, median 328) to thousands (embryos, medians 1,074–3,909) of spatially located reads per nucleus ([[10-Summaries/andrewc-2020-science|Payne 2021]]).
- **Parent-of-origin chromosome territories** in the mouse zygote were distinguished via SNPs — direct imaging of maternal vs paternal pronuclei mixing during early development ([[10-Summaries/andrewc-2020-science|Payne 2021]]).
- **Epigenetic memory of chromosome positioning**: clonal daughter cells retain similar chromosome-territory arrangements ([[10-Summaries/andrewc-2020-science|Payne 2021]]).

## Contested points

- A 66% UMI matching rate means a substantial fraction of reads cannot be spatially localized ([[10-Summaries/andrewc-2020-science|Payne 2021]]).
- Throughput is image-acquisition-limited (18 rounds × multi-channel imaging per cell) (synthesis).
- IGS has so far been applied to fibroblasts and early embryos; primary-tissue generalization is not yet demonstrated (synthesis).

## Why the filename is misleading

The source file `AndrewC_2020_Science.pdf` is named for first author Andrew C. Payne, not Andrew B. Stergachis (who authored `AndrewB_2020_Science.pdf` = [[fiber-seq]]) ([[10-Summaries/andrewc-2020-science|Payne 2021]]). Despite the similar filename, IGS and Fiber-seq are methodologically unrelated ([[10-Summaries/andrewc-2020-science|Payne 2021]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — Per-cell chromatin contacts without absolute nuclear position.
> - `concept` [[30-Concepts/dip-c|Dip-C]] — Diploid single-cell 3D genome reconstruction from contacts.
> - `concept` [[30-Concepts/tn5-tagmentation|Tn5 tagmentation]] — Transposase insertion that builds the IGS in-situ library.
> - `concept` [[30-Concepts/umi-molecular-barcoding|UMI molecular barcoding]] — Molecular identifiers that link in-situ and ex-situ reads.
> - `concept` [[30-Concepts/fiber-seq|Fiber-seq]] — Unrelated single-molecule chromatin method with a similar source filename.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromatin folding measured by contact and imaging methods.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Measuring several molecular layers in the same cell.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/andrewc-2020-science|Payne 2021]]
