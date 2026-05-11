---
type: concept
title: scDNA-seq (single-cell DNA sequencing)
aliases: [single-cell DNA sequencing, scDNAseq]
tags: [single-cell, scDNA-seq, methods]
created: 2026-05-11
updated: 2026-05-11
---

# scDNA-seq (single-cell DNA sequencing)

> Umbrella term covering technologies that interrogate the DNA of single cells — either by amplifying single-cell genomes ([[scwga]] + scWGS) or by reading single DNA molecules with strand-paired error correction ([[duplex-sequencing]]). Together these methods provide single-cell-level resolution of somatic genomic variation that bulk DNA sequencing cannot detect.

## Definition

scDNA-seq encompasses two methodological branches ([[10-Summaries/diane-2025-naturereviewsgenetics]]):

1. **scWGA + scWGS** — amplify the single-cell genome via [[scwga]] (DOP-PCR, MDA, PTA, MALBAC, LIANTI, DLP+ etc.) then perform standard short-read or long-read sequencing on the amplicon. Variants are assigned to specific cells but suffer from amplification-induced errors (allelic dropout, single-strand dropout, polymerase error).
2. **Single-molecule duplex sequencing** — barcode both Watson and Crick strands of bulk DNA and sequence them paired. Variants must agree across strands to be called. Achieves error rates as low as ~10⁻¹⁶ (HiDEF-seq). Most variants can be detected only at the per-molecule level, not assigned to specific cells — except [[meta-cs]] which performs duplex sequencing on single cells.

[[10-Summaries/gilad-2021-annualreviewofgenomicsandhumangenetics]] frames the scDNA-seq design space through three capabilities: **fidelity** (detecting low-mosaicism variants), **co-presence** (which variants co-occur in the same cell), **phenotypic association** (linking genotype to other modalities like RNA, chromatin, protein).

## Why it matters

The human genome is 20–50× larger than the transcribed or chromatin-accessible genomes, and each genomic locus has only two molecules per cell. So scDNA-seq requires either amplification (introducing errors) or single-molecule chemistry (sacrificing per-cell assignment). For two decades this was the major obstacle — scRNA-seq and scATAC-seq matured years ahead of scDNA-seq for this reason.

The biology questions scDNA-seq uniquely addresses:

- **Somatic mosaicism**: detection of low-VAF variants in single cells ([[10-Summaries/lars-2017-naturereviewsgenetics]], [[10-Summaries/ian-2015-trendsingenetics]]).
- **Lineage tracing in human tissue**: natural mutation accumulation (~2–4 per division) as endogenous lineage markers ([[10-Summaries/diane-2025-naturereviewsgenetics]]).
- **Pre-implantation genetic screening**: aneuploidy and CNV detection from single embryonic cells.
- **Cancer subclonal evolution**: joint detection of mutations and inference of clonal hierarchy.

## Variants and refinements

- **scWGA + scWGS branch** — [[mda]], [[pta]], [[malbac]], [[dop-pcr]], [[dlp-plus]], LIANTI, PicoPLEX.
- **Single-molecule branch** — duplex sequencing (BotSeqS, NanoSeq, CODEC, HiDEF-seq, SMM-seq), and [[meta-cs]] (single-cell duplex).
- **Multi-omic combinations** — paired with [[got]] (genotype + RNA), [[got-cha]] (genotype + chromatin), [[gt-seq]] (DNA + RNA via physical separation).

## Contested points

- The "fidelity vs co-presence vs phenotypic association" tradeoff ([[10-Summaries/gilad-2021-annualreviewofgenomicsandhumangenetics]]) means no single method is universally best.
- Per-cell coverage vs cell throughput: PTA peaks at ~384 cells, DLP+ at >10,000 cells with very different per-cell yields.
- Cost — duplex sequencing and PTA are both ~$5–20/cell, making cohort-scale studies still expensive.

## Examples

- Walsh lab tracking human cortical neuron lineages via [[pta]] of single neurons ([[10-Summaries/diane-2025-naturereviewsgenetics]]).
- 40% of mid-gestation human prenatal neurons harboring complex CNV (Diane 2025 preprint reference).
- 49% of single cells in human early cleavage-stage embryos shown aneuploid by DOP-PCR ([[10-Summaries/diane-2025-naturereviewsgenetics]]).

## Related

- [[scwga]]
- [[duplex-sequencing]]
- [[mda]], [[pta]], [[malbac]], [[dop-pcr]], [[dlp-plus]], [[meta-cs]]
- [[somatic-mosaicism]]
- [[lineage-tracing]]
- [[scdna-capabilities-framework]]
- [[40-Topics/scdna-seq]]
- [[40-Topics/whole-genome-amplification]]
