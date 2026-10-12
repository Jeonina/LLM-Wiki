---
type: concept
title: DLP+ (DNA Transposition Single-cell Library Preparation)
aliases: [DLP+, DLP-plus]
tags: [scWGA, Tn5, microfluidics, high-throughput, method]
created: 2026-05-11
updated: 2026-10-12
---

# DLP+ (DNA Transposition Single-cell Library Preparation)

> Tn5-based [[scwga]] method implemented in a microfluidic format that trades per-cell coverage for very high cell throughput (>10,000 cells per run), used for large-scale single-cell CNV and chromosomal phylogenetics where many cells are more informative than deep per-cell coverage ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/zahn-2017-dlp|Zahn 2017]]).

> [!abstract] 한눈에
> DLP+는 Tn5로 단일 세포 DNA를 바로 tagmentation하는 microfluidic 방법으로, 세포당 coverage는 매우 낮지만 한 번에 10,000개가 넘는 세포를 읽어 CNV와 염색체 수준 계통 분석에 쓰인다 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). 깊이 대신 세포 수를 늘리는 이 전략의 근거는 원조 DLP 논문에 정리되어 있다 ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).

## Definition

DLP+ uses Tn5 transposase to tagment nuclear DNA, inserting Illumina-compatible adapters directly into the genome of single cells in microfluidic compartments; the tagmented fragments are then PCR-amplified ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). Imaging-based microscopy QC provides real-time ploidy and quality checks (synthesis). The output is very low per-cell coverage across thousands of cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

Typical metrics: very low coverage per cell, moderate MAPD, allelic balance that typically captures one allele (low per-cell depth), >10,000 cells per run, ~21 h, not commercially available (synthesis; throughput from [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

[[10-Summaries/zahn-2017-dlp|Zahn 2017]] is the original DLP. Its argument is mechanistic: WGA copies templates as long molecules that are fragmented *afterwards*, so one region yields multiple inserts with non-overlapping coordinates that cannot be duplicate-filtered; DLP fragments first, so every PCR copy is an exact duplicate and every retained read represents a unique template ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).

## Why it matters

- For CNV-centric questions at scale (clonal evolution in tumours, chromosomal mosaicism in development, large-cohort aneuploidy screening), DLP+ delivers far more cells per run than PTA or MDA ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). Each cell contributes shallow but uniform CNV information; in aggregate the dataset enables sub-megabase phylogenetic resolution and detection of rare clonal subpopulations (synthesis).
- The original paper's economics argument (6,000 cells at 0.05× for the price of ten at 30×, giving ~0.05% subclone sensitivity) is the clearest statement of the breadth/depth trade in this corpus ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- Tn5 tagmentation has a useful side effect: **specific overlap patterns of tagmentation events can be used to distinguish allelic states of each genomic region**, which gives additional validation for depth-based CNV calls beyond what MDA or PTA can offer ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

## Related Tn5-based methods

| Method | What it does | Throughput / coverage | Source |
|---|---|---|---|
| DLP (original) | Fragment-first tagmentation without preamplification | 782 cells at 0.07–0.12× each | ([[10-Summaries/zahn-2017-dlp\|Zahn 2017]]) |
| DLP+ | Microfluidic Tn5 tagmentation with imaging QC | >10,000 cells per run at very low per-cell coverage | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| LIANTI | Linear amplification via transposon insertion | High coverage (80–85%) | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| [[meta-cs\|META-CS]] | Duplex-sequencing variant of Tn5-based scWGA | — | see [[meta-cs]] |

## Evidence and examples

**Founding DLP**

- 782 cells at 0.07–0.12× each; 64 merged cells reach 94.5–96.8% breadth, and 48 merged cells match a true bulk genome in uniformity ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- Cost was ~$0.50 per cell against ~$15 per cell for DOP-PCR protocols ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).

**Cohorts and benchmarks**

- Large-scale single-cell CNV phylogenetics has been done in breast cancer and other solid tumours, with chromosomal mosaicism patterns detected across thousands of cells per sample ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]; [[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- At cohort scale, DLP+ produced 100,054 single-cell genomes (median depth 0.060 per cell) from 70 HGSOC samples, retaining 30,260 tumour genomes after QC that included two-rater review of nozzle images for doublets and optical cell-size readouts used to validate per-cell WGD calls ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- The earlier DLP+ HGSOC cell-line data (891 cells) serve as a real-data benchmark for SNV lineage-tree inference ([[10-Summaries/zhang-2025-scistree2|ScisTree2]]).
- The same OV2295 DLP+ cell lines (890 cells, 0.1–0.4×) are a benchmark for haplotype-specific copy-number calling, where CNRein, SIGNALS, CHISEL and Alleloscope disagreed most on WGD status ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]).

## Contested points

- **Essentially CNV-only.** Per-cell coverage is so low that SNV detection is unreliable ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]) (synthesis).
- **Tn5 insertion bias.** Preferred insertion sites can affect uniformity at fine scale, though the high cell throughput averages this out for population-level conclusions (synthesis).
- **Artifactual fragment pairs.** DLP+ libraries contain fragment pairs that share a start or end coordinate but differ in length; they survive standard deduplication, outnumber opposite-orientation pairs nearly 10:1, make up under 1% of fragments, and inflate overlap counts ([[10-Summaries/wesley-2026-songbird|Songbird]]). Songbird and ASCENT both remove them ([[10-Summaries/wesley-2026-songbird|Songbird]]).
- **Coverage ceiling.** Because adapters pair at random, the maximum possible coverage is half the cell's ploidy ([[10-Summaries/wesley-2026-songbird|Songbird]]).
- **WGD calls disagree.** On OV2295 DLP+ data the four haplotype-specific callers disagreed most on WGD status ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/scwga|scWGA]] — Amplifying the ~6 pg of DNA in one diploid cell enough to sequence it.
> - `concept` [[30-Concepts/meta-cs|META-CS]] — Tn5-based duplex-sequencing sibling method for single cells.
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Umbrella for technologies that read the DNA of single cells.
> - `hub` [[40-Topics/whole-genome-amplification|Whole-genome amplification]] — The chemistries that bridge single-cell DNA to sequencing input.

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/ivanovic-2025-cnrein|Ivanovic & El-Kebir 2025]]
> - [[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/wesley-2026-songbird|Wesley 2026]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
> - [[10-Summaries/zhang-2025-scistree2|Zhang 2025]]
