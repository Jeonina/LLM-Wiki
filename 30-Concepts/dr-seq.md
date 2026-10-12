---
type: concept
title: DR-seq
aliases: [DR-seq, gDNA-mRNA sequencing, one-pot joint genome-transcriptome]
tags: [joint-assay, single-cell-multiomics, scDNA, scRNA-seq, quasilinear-amplification, method]
created: 2026-05-12
updated: 2026-10-12
---

# DR-seq (gDNA-mRNA sequencing)

> One-pot single-cell joint DNA + RNA assay that avoids physical separation by performing **MALBAC-style quasilinear amplification on both DNA and ssDNA cDNA simultaneously**, then splitting the sample for separate RNA (via IVT) and DNA (via PCR) library preparation ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]).

> [!abstract] 한눈에
> DR-seq는 한 세포의 gDNA와 cDNA를 분리하지 않고 한 tube에서 MALBAC 방식으로 함께 증폭한 뒤 나눠서 RNA와 DNA library를 만드는 one-pot 방법이다 ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]). 그 대가로 coding 영역의 DNA read는 gDNA인지 cDNA인지 구분할 수 없어 계산적으로 가려야 한다 ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]).

## Definition

Introduced by Dey et al. 2015 ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]). The protocol runs in four steps ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]):

1. The cell is lysed with a poly-T primer carrying cell-barcode + T7 promoter (Ad-1x); RT is performed in situ.
2. Seven rounds of quasilinear amplification with a random-8-mer adaptor (Ad-2) amplify both gDNA and cDNA together.
3. The sample is split: half → IVT-based RNA library (only T7-bearing cDNA amplicons transcribed); half → PCR-based DNA library.
4. **DNA reads from coding regions must be computationally masked** because they could come from either gDNA or cDNA.

## Why it matters

- **One-pot alternative to [[gt-seq|G&T-seq]]** — simpler workflow, less material loss, no physical separation step ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]).
- **Length-based identifiers (LBIs)**: the genomic priming position of the first Ad-2 amplicon serves as a [[umi-molecular-barcoding|UMI]] surrogate, reducing CV for ~80% of genes and matching CEL-seq with random-sequence UMIs ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]).

## Variants and refinements

- **DR-seq** itself is the one-pot design ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]); its amplification follows [[malbac|MALBAC]] within the wider [[scwga|scWGA]] family.
- Conceptual successor with three modalities: [[sctrio-seq|scTrio-seq]] (adds methylation).

## Evidence and examples

- Demonstrated that **DNA copy-number variation strongly drives expression** at single-cell resolution in SK-BR-3 breast cancer cells (CNV calls confirmed by DNA FISH at four loci, Kolmogorov–Smirnov *P* > 0.01 with FISH distributions) ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]).
- Observed an **inverse relationship between expression variability and copy number** — high-CV genes on low-copy regions, suggesting CNVs may drive expression-level variability ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]).

## Contested points

- Coding-region masking limits SNV detection from coding regions of the DNA half ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]).
- Quasilinear amplification GC bias is slightly higher than MALBAC alone ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/gt-seq|G&T-seq]] — Plate-based DNA+RNA method that physically separates mRNA from gDNA.
> - `concept` [[30-Concepts/malbac|MALBAC]] — Hybrid quasilinear pre-amplification with looping amplicons.
> - `concept` [[30-Concepts/scwga|scWGA]] — Methods that amplify the ~6 pg of DNA in a single cell for sequencing.
> - `concept` [[30-Concepts/umi-molecular-barcoding|UMI / molecular barcoding]] — Random tags that group reads by molecule of origin.
> - `concept` [[30-Concepts/sctrio-seq|scTrio-seq]] — Triple-omics successor adding the methylome.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Methods that measure two or more modalities in the same cell.
> - `hub` [[40-Topics/whole-genome-amplification|Whole-genome amplification]] — Chemistries that bridge single-cell DNA to sequencing input.

People: [[20-Entities/alexander-van-oudenaarden]].

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/dey-2015-dr-seq|Dey 2015]]
