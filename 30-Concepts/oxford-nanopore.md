---
type: concept
title: Oxford Nanopore Technologies
aliases: [ONT, nanopore sequencing]
tags: [long-read, sequencing, direct-RNA, methylation]
created: 2026-05-12
updated: 2026-10-07
---

# Oxford Nanopore Technologies (ONT)

> A long-read sequencing platform that threads native single DNA or RNA molecules through nanopores embedded in a membrane, reading sequence directly from changes in ionic current ("squiggles") as bases pass through. No amplification required; modifications detectable directly.

## Definition

ONT instruments range from portable MinION/Flongle to PromethION. Read lengths routinely 10–100 kb; ultra-long reads reach >1 Mb. Accuracy improved from ~85% (R7) to >99% (R10.4.1). Adaptive sampling enables real-time read selection.

## Why it matters

- Direct detection of 5mC, 5hmC, 6mA, 4mC via current-signature modeling (Nanopolish → Dorado/Remora).
- Telomere-to-telomere genome assemblies (CHM13).
- Real-time targeted sequencing via adaptive sampling enables HRR-focused experiments.

## Examples

- [[10-Summaries/mo-2023-stam-seq]] uses ONT adaptive sampling for plant centromere/telomere/rDNA epigenomics.
- [[10-Summaries/liu-2025-nanopore-lscc-svs]] uses ONT for somatic SV detection.
- [[10-Summaries/liu-2025-long-read-epigenome-review]] reviews ONT epigenomics.

## Added 2026-10-07

Nanopore long-read scATAC (scNanoATAC-seq2) yields allele-tagging rates of 96.8% in C57×CAST and 47% in C57×DBA embryos, enabling allele-specific accessibility analysis of imprinting and X inactivation at single-cell resolution ([[10-Summaries/li-2025-scnanoatac-seq2]]).

Nanopore read length enables single-cell multi-way 3D genome profiling. scNanoHi-C sequences ~3-kb amplicons of Hi-C concatemers on PromethION R9.4.1 at ~USD 3 per cell when ~500 cells share a run ([[10-Summaries/li-2023-scnanohi-c]]).

SPLONGGET couples 10x Genomics barcoding with Nanopore sequencing, retaining all tagmentation fragments so that one single-cell library yields whole-genome coverage, chromatin accessibility and full-length transcripts; the DNA library spans 200 bp to >10 kb, which Nanopore reads independent of fragment length, giving 79–93% of the genome at ≥5× per time-point library versus 6% for the same library read with short reads. Applied to one paediatric B-ALL across four time points, it reports parallel CD19 immune-escape evolution (preprint) ([[10-Summaries/pancikova-2025-splongget]]).


## Related

- [[40-Topics/long-read-sequencing]] · [[30-Concepts/pacbio]] · [[30-Concepts/nanopore-adaptive-sampling]] · [[40-Topics/long-read-sequencing]]
