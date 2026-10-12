---
type: concept
title: SDR-seq
aliases: [SDR-seq, single-cell DNA–RNA sequencing, targeted scDNA-scRNA]
tags: [single-cell-multiomics, DNA-RNA-coassay, Tapestri, variant-phenotyping, targeted]
created: 2026-06-02
updated: 2026-10-12
---

# SDR-seq

> A targeted droplet method that profiles up to 480 combined genomic DNA loci and genes in the same single cell, using in-situ reverse transcription followed by multiplexed PCR on the **Tapestri** platform — enabling per-cell variant zygosity linked to gene expression ([[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]).

> [!abstract] 한눈에
> SDR-seq는 Tapestri droplet에서 최대 480개의 gDNA locus와 유전자를 한 세포에서 함께 증폭해, 세포별 변이 zygosity를 유전자 발현과 연결하는 targeted 방법이다 ([[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]). whole-genome droplet co-assay와 달리 allelic dropout이 10% 미만이어서 noncoding 변이를 원래 자리에서 직접 볼 수 있다 ([[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]).

## Definition

SDR-seq (single-cell DNA–RNA sequencing) fixes cells (glyoxal, which avoids nucleic-acid crosslinking), performs in-situ RT with custom poly(dT) primers adding UMI + sample barcode + capture sequence, then runs targeted multiplexed PCR over gDNA and RNA amplicons in Tapestri droplets; distinct R2/R2N overhangs let the two libraries be sequenced separately ([[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]).

## Why it matters

- Whole-genome droplet co-assays have >96% allelic dropout, making per-cell zygosity impossible; SDR-seq's targeted depth recovers ~90% of alleles (ADO <10%), comparable to targeted Tapestri scDNA ([[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]).
- It directly assays noncoding variants in their endogenous context — where most disease-associated variants lie — rather than approximating their effect with CRISPRi ([[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]).

## How it compares

| Compared with | Difference | Source |
|---|---|---|
| [[30-Concepts/defnd-seq\|DEFND-seq]] | SDR-seq is targeted and low-ADO, the complement to whole-genome, high-ADO DEFND-seq | ([[10-Summaries/lindenhofer-2025-sdr-seq\|Lindenhofer 2025]]) |
| [[30-Concepts/got\|GoT]] | GoT reads mutations only in mRNA; SDR-seq extends its logic to direct gDNA readout, including noncoding loci | ([[10-Summaries/lindenhofer-2025-sdr-seq\|Lindenhofer 2025]]) |
| PTA-based plate methods | ~100× higher cell throughput | ([[10-Summaries/lindenhofer-2025-sdr-seq\|Lindenhofer 2025]]) |

## Evidence and examples

- SDR-seq detected variants at ~0.15% frequency ([[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]).
- It resolved that *combinations* of *POU5F1* 3′UTR variants differ in expression effect from single variants ([[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]).
- In primary B-cell lymphoma, variant clustering revealed clonal structure and showed that cells with higher mutational burden have elevated B-cell-receptor signaling and antiapoptotic expression ([[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/joint-single-cell-multi-omics|Joint single-cell multi-omics]] — Assays that measure several molecular layers in the same cell.
> - `concept` [[30-Concepts/defnd-seq|DEFND-seq]] — Whole-genome droplet DNA + RNA co-assay; high ADO.
> - `concept` [[30-Concepts/got|GoT]] — Genotyping of transcriptomes: mutations read from mRNA.
> - `concept` [[30-Concepts/allele-dropout|Allele dropout]] — Loss of one allele during amplification; what targeted depth reduces.
> - `concept` [[30-Concepts/single-cell-variant-calling|Single-cell variant calling]] — Calling SNVs and genotypes from single-cell DNA.
> - `concept` [[30-Concepts/umi-molecular-barcoding|UMI / molecular barcoding]] — Unique molecular identifiers added during in-situ RT.
> - `entity` [[20-Entities/lars-steinmetz|Lars Steinmetz]] — Corresponding author of SDR-seq.
> - `entity` [[20-Entities/oliver-stegle|Oliver Stegle]] — Co-author of SDR-seq.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multiomics]] — Joint measurement of several layers in one cell.
> - `hub` [[40-Topics/scdna-cancer-applications|scDNA-seq in cancer applications]] — Clonal structure and genotype–phenotype links in tumours.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]
