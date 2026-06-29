---
type: topic
title: Single-cell lineage tracing
aliases: [lineage tracing, clonal tracing, cell phylogeny, fate mapping]
tags: [lineage-tracing, clonal-analysis, phylogenetics, development, cancer-evolution]
created: 2026-06-02
updated: 2026-06-02
---

# Single-cell lineage tracing

> Methods and algorithms that reconstruct the ancestry of individual cells — which cell came from which — to study development, ageing, regeneration, and cancer evolution at clonal and phylogenetic resolution.

The field organizes along two axes ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]): **prospective** (engineered synthetic barcodes) vs **retrospective** (naturally accumulated somatic variants), and **static** (one immutable label per clone) vs **evolvable** (labels that keep mutating to build phylogenies). A recurring tension is **phylogenetic signal vs cell-state phenotyping**: nuclear-SNV scWGS gives the best trees but poor phenotyping, while mtDNA and epimutation profiling trade phylogenetic depth for higher throughput and richer molecular state ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Core concepts

- [[30-Concepts/lineage-tracing]] — umbrella concept.
- [[30-Concepts/crispr-lineage-recording]] — prospective evolvable barcodes (Cas9/base/prime editing).
- [[30-Concepts/phylogenetic-inference]] — algorithms that turn markers into cell-division trees.
- [[30-Concepts/lineage-tracing-somatic-mutations]] — retrospective tracing from nuclear SNVs/CNVs.
- [[30-Concepts/mitochondrial-lineage-tracing]] — mtDNA-based clonal tracing.
- [[30-Concepts/methylation-clones-epimutation]] — clonally heritable DNA-methylation epimutations.
- [[40-Topics/clonal-hematopoiesis]] — the central ageing/cancer biology payoff.

## Key entities

- [[20-Entities/alejo-rodriguez-fraticelli]] — clonal hematopoiesis; lead author of the 2026 technology review.
- [[20-Entities/zheng-hu]] — single-cell cancer evolution; PhyloVelo; lead author of the 2026 computational review.
- [[20-Entities/jay-shendure]] — CRISPR/prime-editing molecular recording.
- [[20-Entities/alexander-van-oudenaarden]] — foundational synthetic + natural tracing methods.
- [[20-Entities/caleb-lareau]], [[20-Entities/leif-ludwig]] — mtDNA lineage tracing.
- [[20-Entities/tim-coorens]] — somatic-mutation phylogenetics in human tissues.

## Sources, by sub-theme

### Review pairs (Nature Reviews Genetics 2026)

- [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]] — Rodriguez-Fraticelli & Parreno: the *technology* toolbox (synthetic + natural barcodes).
- [[10-Summaries/wang-2026-multimodal-lineage-computational]] — Wang, He & Hu: the *computational* toolbox (phylogenetics, fate mapping, ancestral states, integrative learning).

### Methylation / epimutation tracing

- [[10-Summaries/chen-2025-methyltree]] — MethylTree: clonal reconstruction from whole-genome methylation.
- [[10-Summaries/scherer-2025-nature]] — somatic epimutations / EPI-clone for blood ageing.

### Mitochondrial tracing

- [[10-Summaries/ludwig-2020-mtscatac-seq]] — mtscATAC-seq.
- [[10-Summaries/miller-2022-maester]] — MAESTER; mtDNA variants from scRNA-seq.
- [[10-Summaries/sun-2025-scmitomut]] — scMitoMut mtDNA variant calling.

### Somatic-mutation phylogenies (human tissue)

- [[10-Summaries/lee-six-2018-hsc-dynamics]] — HSC population dynamics from scWGS phylogenies.
- [[10-Summaries/coorens-2021-nature]] — extensive human developmental phylogenies.

### Joint genotype + state (enabling multimodal tracing)

- [[10-Summaries/olsen-2025-defnd-seq]] — DEFND-seq: scalable whole-genome + RNA.
- [[10-Summaries/lindenhofer-2025-sdr-seq]] — SDR-seq: targeted DNA + RNA with clonal/variant structure.
- [[10-Summaries/nam-2019-got]] — GoT: genotype + transcriptome.

## Open questions

- Is loss of clonality a biomarker of, or a mechanism driving, organismal ageing? ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]])
- Do driver-less clonal expansions reflect positive selection or neutral drift? ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]])
- Can lineage data's temporal/heritable structure supply the causal constraints that correlation-based "virtual cell" foundation models lack? ([[10-Summaries/wang-2026-multimodal-lineage-computational]])
- Methylome reportedly beats ATAC and RNA for clonal inference against ground-truth barcodes — how general is this? ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]])
