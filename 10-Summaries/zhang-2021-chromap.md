---
type: summary
title: "Zhang et al. 2021 — Fast alignment and preprocessing of chromatin profiles with Chromap"
source: "[[00-Sources/papers/Fast alignment and preprocessing of chromatin profiles with Chromap]]"
source_kind: paper
author: "Haowen Zhang, Li Song, Xiaotao Wang, Haoyu Cheng, Chenfei Wang, Clifford A. Meyer, Tao Liu, Ming Tang, Srinivas Aluru, Feng Yue, X. Shirley Liu, Heng Li (corresponding)"
published: 2021-11-12
ingested: 2026-08-10
doi: "10.1038/s41467-021-26865-w"
journal: "Nature Communications"
tags: [Chromap, alignment, minimizer, scATAC-seq, Hi-C, ChIP-seq, preprocessing, computational-tool, throughput]
entities: []
concepts: ["[[scatac-seq]]", "[[atac-seq]]", "[[single-cell-hi-c]]", "[[chip-seq]]", "[[umi-molecular-barcoding]]"]
topics: ["[[single-cell-atac-seq]]", "[[3d-genome]]"]
---

**Citation:** Zhang et al. (2021) — *Fast alignment and preprocessing of chromatin profiles with Chromap* — *Nature Communications* 12, 6566. [DOI](https://doi.org/10.1038/s41467-021-26865-w)

# Zhang 2021 — Chromap

> A minimizer-based aligner built on a single observation: chromatin assays need **read coordinates**, not base-level alignments. Dropping the variant-calling-grade alignment work and fusing alignment with adapter trimming, deduplication and barcode correction into one pass gives 10–68× speedups at equal downstream accuracy.

## Key claims

- The bottleneck in ChIP-seq/ATAC-seq/Hi-C pipelines is **alignment and preprocessing**, not analysis: BWA-MEM/Bowtie2 + SAMtools + Picard take hours to days while MACS2 peak calling takes minutes. Repeated I/O across sequential tools compounds the cost.
- Chromap's design differences from minimap2 (same lab): it considers **every** minimizer hit rather than chaining, uses **read-pair information to rescue** alignments lost to the minimizer frequency cap, and verifies candidates with a banded Myers bit-parallel edit-distance computation (SIMD-parallelized) instead of affine-gap dynamic programming.
- A **candidate cache** exploits the fact that chromatin signal is concentrated in a subset of the genome: candidate locations for frequent minimizer vectors are cached (hash table, N = 2,000,003 entries; count-min-sketch-style filter to avoid caching background noise). Reads from the same strand or nearby positions hit the same entry.
- Accuracy on simulated data: ~98% for 100/150 bp paired-end (comparable to BWA-MEM, Bowtie2); at 50 bp Chromap holds ~96% with BWA-MEM/Bowtie2 while minimap2, STAR and Accel-Align drop to 94.1–95.7%.
- CTCF ChIP-seq: 99.8% of Chromap alignments supported by BWA-MEM or Bowtie2; peaks overlap 99.8%; **fewest aligner-unique peaks** of all methods; between-aligner peak differences smaller than between biological replicates. Runtime <5 min end-to-end vs ~42 min for the next-fastest workflow.
- Hi-C (K562, ~1.4 billion fragments): compartment PC1 Pearson r = 0.995 and insulation-score r = 0.998 vs BWA-MEM; SCC between Chromap and BWA-MEM on the same replicate (0.998) far exceeds SCC between two biological replicates (0.945). 164 min vs **13× slower** for BWA-MEM + pairtools. Aligner-unique loops show equal CTCF enrichment at anchors — i.e. they are real, not artifacts.
- scATAC-seq (10k PBMC, ~758M reads): cell-type annotation NMI >0.96 vs CellRanger v2.0.0, **higher than the NMI between the two CellRanger versions**, and higher than between two 95%-downsampled replicates of the same data (0.888). Runtime <30 min vs 8 h (CellRanger v2.0.0, 16×) and 33 h (v1.2.0, 68×). Memory ~21 GB, stable with sequencing depth.

## Methods / evidence

Benchmarks against BWA-MEM, Bowtie2, minimap2, STAR (no-splicing) and Accel-Align on simulated WGS (50/100/150 bp, 0.1% error, Mason), ENCODE CTCF ChIP-seq, 4DN-standard Hi-C, and 10x scATAC-seq. Downstream validation via MACS2 peaks + ChIPseeker annotation, cooltools compartments/insulation, HiCCUPS loops, and MAESTRO + ArchR clustering.

The benchmarking discipline is worth noting: rather than asserting "the results are similar," they establish a **noise floor** — replicate-to-replicate variation, or version-to-version variation in the reference pipeline — and show the aligner-swap effect falls below it. That is the right way to argue a tool change is safe, and it is uncommon.

## Surprising or load-bearing bits

- **CellRanger version changes perturb scATAC clustering more than swapping the aligner does.** Deduplication criteria and other preprocessing choices matter more than alignment. For anyone comparing scATAC datasets processed at different times, the pipeline *version* is a bigger confounder than the aligner — a reproducibility hazard rarely stated this plainly.
- The candidate cache is a genuinely modality-specific optimization: it works *because* chromatin reads pile up in peaks. It would not help WGS. This is what "purpose-built for chromatin" means concretely.
- 68× over CellRanger v1.2.0 and 16× over v2.0.0 changes what is feasible — reprocessing a large scATAC atlas from FASTQ becomes an afternoon rather than a week, which matters when a reference genome or barcode whitelist changes.
- Chromap supports split alignment, so **one tool covers ChIP-seq, ATAC-seq, scATAC-seq and Hi-C** — relevant to this wiki's multi-modal pipelines where each modality otherwise brings its own aligner.
- MAPQ is not comparable across aligners (Accel-Align's 7 ≈ others' 30). A filtering threshold copied between pipelines is not the same filter.
- Heng Li is an author, as on BWA and minimap2 — this is the same lineage arguing against its own earlier tools for this use case.

## Concepts touched

- [[scatac-seq]] — Chromap is the fast path from FASTQ to fragments; upstream of [[granja-2021-archr|ArchR]], [[stuart-2021-natmethods|Signac]], [[zhang-2024-snapatac2|SnapATAC2]].
- [[single-cell-hi-c]] — split-alignment support and the pairs-format output put it upstream of [[abdennur-2020-cooler|Cooler]]-based single-cell 3D pipelines, where per-cell counts multiply the alignment burden.
- [[umi-molecular-barcoding]] — barcode correction is done inline with a posterior-probability model (≥90% threshold) using quality scores and observed barcode abundance.

## Connections to other sources

- Replaces the BWA-MEM ([[li-2009-bwa|Li & Durbin 2009 (BWA)]]) + SAMtools ([[li-2009-samtools|Li 2009 (SAMtools)]]) + Picard front end assumed by [[mckenna-2010-gatk|GATK]]-era workflows — but only for chromatin assays, explicitly not for variant calling.
- Feeds MACS2 ([[zhang-2008-macs|Zhang 2008 (MACS)]]) and the pipelines in [[granja-2021-archr]] / [[stuart-2021-natmethods]].
- Hi-C alternative to [[durand-2016-juicer|Juicer]]'s alignment stage and the 4DN/pairtools standard.
- [[heumos-2023-best-practices]] covers the preprocessing-choice sensitivity this paper quantifies.

## Open questions

- Chromap is not evaluated on **single-cell DNA** data (WGA-amplified genomes, uneven coverage) — the corpus's core modality. Whether its coordinate-only philosophy is safe there is untested, and almost certainly it is not, since scDNA-seq needs exactly the base-level alignment quality Chromap discards.
- Barcode correction is 10x-whitelist-specific; combinatorial-indexing protocols ([[combinatorial-indexing]]) are not covered.

## Related

- [[scatac-seq]] · [[durand-2016-juicer]] · [[granja-2021-archr]] · [[single-cell-atac-seq]]
