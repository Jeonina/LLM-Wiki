---
type: concept
title: SDR-seq
aliases: [SDR-seq, single-cell DNA–RNA sequencing, targeted scDNA-scRNA]
tags: [single-cell-multiomics, DNA-RNA-coassay, Tapestri, variant-phenotyping, targeted]
created: 2026-06-02
updated: 2026-06-02
---

# SDR-seq

> A targeted droplet method that profiles up to 480 combined genomic DNA loci and genes in the same single cell, using in-situ reverse transcription followed by multiplexed PCR on the **Tapestri** platform — enabling per-cell variant zygosity linked to gene expression ([[10-Summaries/lindenhofer-2025-sdr-seq]]).

## Definition

SDR-seq (single-cell DNA–RNA sequencing) fixes cells (glyoxal, which avoids nucleic-acid crosslinking), performs in-situ RT with custom poly(dT) primers adding UMI + sample barcode + capture sequence, then runs targeted multiplexed PCR over gDNA and RNA amplicons in Tapestri droplets; distinct R2/R2N overhangs let the two libraries be sequenced separately ([[10-Summaries/lindenhofer-2025-sdr-seq]]).

## Why it matters

- Whole-genome droplet co-assays have >96% allelic dropout, making per-cell zygosity impossible; SDR-seq's targeted depth recovers ~90% of alleles (ADO <10%), comparable to targeted Tapestri scDNA ([[10-Summaries/lindenhofer-2025-sdr-seq]]).
- Directly assays noncoding variants in their endogenous context — where most disease-associated variants lie — rather than approximating their effect with CRISPRi ([[10-Summaries/lindenhofer-2025-sdr-seq]]).
- ~100× higher cell throughput than PTA-based plate methods ([[10-Summaries/lindenhofer-2025-sdr-seq]]).

## How it compares

- **Targeted, low-ADO**, the complement to whole-genome high-ADO [[30-Concepts/defnd-seq]] ([[10-Summaries/lindenhofer-2025-sdr-seq]]).
- Extends genotyping-of-transcriptomes logic (GoT, which reads mutations only in mRNA) to direct gDNA readout including noncoding loci ([[10-Summaries/lindenhofer-2025-sdr-seq]]). See [[30-Concepts/got]].

## Examples

- Detected variants at ~0.15% frequency and resolved that *combinations* of *POU5F1* 3′UTR variants differ in expression effect from single variants ([[10-Summaries/lindenhofer-2025-sdr-seq]]).
- In primary B-cell lymphoma, variant clustering revealed clonal structure and showed cells with higher mutational burden have elevated B-cell-receptor signaling and antiapoptotic expression ([[10-Summaries/lindenhofer-2025-sdr-seq]]).

## Related

- [[30-Concepts/joint-single-cell-multi-omics]] · [[30-Concepts/defnd-seq]] · [[30-Concepts/got]] · [[30-Concepts/allele-dropout]] · [[30-Concepts/single-cell-variant-calling]] · [[30-Concepts/umi-molecular-barcoding]]
- [[40-Topics/single-cell-multiomics]] · [[40-Topics/scdna-cancer-applications]] · [[20-Entities/lars-steinmetz]] · [[20-Entities/oliver-stegle]]
