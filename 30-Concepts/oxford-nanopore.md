---
type: concept
title: Oxford Nanopore Technologies
aliases: [ONT, nanopore sequencing]
tags: [long-read, sequencing, direct-RNA, methylation]
created: 2026-05-12
updated: 2026-05-12
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

- [[10-Summaries/single-molecule-targeted-accessibility-and-methylation-sequencing-of-centromeres-telomeres-and-rdnas-in-arabidopsis]] uses ONT adaptive sampling for plant centromere/telomere/rDNA epigenomics.
- [[10-Summaries/nanopore-sequencing-unveils-somatic-structural-variations-as-biomarkers-in-laryngeal-squamous-cell-carcinoma-genomes]] uses ONT for somatic SV detection.
- [[10-Summaries/profiling-the-epigenome-using-long-read-sequencing]] reviews ONT epigenomics.

## Related

- [[30-Concepts/long-read-sequencing]] · [[30-Concepts/pacbio]] · [[30-Concepts/nanopore-adaptive-sampling]] · [[40-Topics/long-read-sequencing]]
