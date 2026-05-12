---
type: summary
title: "Hunt et al. 2022 — scTEM-seq: cheap single-cell global methylation via SINE Alu amplicons"
source: "[[00-Sources/papers/scTEM-seq_ Single-cell analysis of transposable element methylation to link global epigenetic heterogeneity with transcriptional programs]]"
source_kind: paper
author: "Kooper V. Hunt, Sean M. Burnard, Ellise A. Roper, Danielle R. Bond, Matthew D. Dun, Nicole M. Verrills, Anoop K. Enjeti, Heather J. Lee (corresponding)"
published: 2022-04-06
ingested: 2026-05-12
doi: "10.1038/s41598-022-09765-x"
journal: "Scientific Reports"
tags: [DNA-methylation, transposable-elements, SINE-Alu, AML, decitabine, single-cell, multi-omics]
entities:
  - "[[20-Entities/heather-lee]]"
  - "[[20-Entities/kooper-hunt]]"
concepts:
  - "[[30-Concepts/sctem-seq]]"
  - "[[30-Concepts/dna-methylation]]"
  - "[[30-Concepts/transposable-elements]]"
  - "[[30-Concepts/bisulfite-sequencing]]"
  - "[[30-Concepts/decitabine]]"
  - "[[30-Concepts/viral-mimicry]]"
topics:
  - "[[40-Topics/dna-methylation]]"
  - "[[40-Topics/single-cell-multiomics]]"
---

# Hunt et al. 2022 — scTEM-seq

> Thesis: Genome-wide single-cell bisulfite sequencing (scBS-seq) costs ~20M reads/cell to recover ~10–40% genomic coverage. Most experiments only need a **global methylation estimate**, not per-locus calls. **scTEM-seq** targets high-copy SINE Alu repetitive elements via bisulfite-PCR amplification, yielding accurate global methylation estimates from ~20k reads/cell — three orders of magnitude cheaper than scBS-seq. Combined with G&T-seq for parallel transcriptome readout, it links global methylation heterogeneity to specific gene-expression programs in AML cells under hypomethylating-agent treatment.

## Key claims

- SINE Alu methylation in single-cell BS data correlates with genome-wide CpG methylation at *R*²=0.91 (in colorectal cancer scBS-seq reference data). LINE-1 also works but lower yield; SINE Alu wins because of higher copy number.
- scTEM-seq uses 28 second-generation indexed primers per pool; up to 18,432 cells multiplexable. Yields 1,000–6,000 unique Alu sites per cell at 14k–37k raw reads.
- Applied to KG1a and HL60 AML cell lines treated with decitabine (DAC, a hypomethylating agent): untreated cells uniformly highly methylated (~85%); DAC-treated cells **heterogeneously demethylated** (29–69%, mean 42%).
- Parallel scRNA-seq (G&T-seq) on the same cells: 60 genes correlate with global methylation level, including upregulation of *IFI44L* (interferon response) and *HLA-A*. Gene ontology enrichment for translation initiation, leukocyte-mediated immunity, and interspecies interaction — consistent with **viral-mimicry** activation by retrotransposon expression upon methylation loss.
- A subgroup of DAC-treated cells coordinately upregulates many TE families (LINE-1, SINE Alu, ERVs). Notably, TE-upregulating cells are **indistinguishable from non-responders by global methylation alone**, implying that methylation loss is necessary but not sufficient for viral mimicry — other factors (e.g., SETDB1, TF availability) gate the response.

## Methods / evidence

G&T-seq separates gDNA from RNA per cell. gDNA → bisulfite conversion → Alu-targeted PCR with indexed primers → Illumina MiSeq. Parallel SMART-seq2 on the RNA fraction. Bulk PBAT libraries for comparison. Validation against published scBS-seq.

## Surprising or load-bearing bits

- The cost-of-information argument is the structural insight: per-locus methylation calls are expensive and most signal is global. SINE Alu acts as **a 1000-cell-equivalent methylome microscope at 0.1% the per-cell cost**.
- The viral-mimicry response is **decoupled from raw methylation loss**: response heterogeneity is downstream of methylation, suggesting clinical response prediction for HMAs (azacitidine, decitabine) needs more than methylation measurement.

## Connections to other sources

- Direct conceptual comparison to [[10-Summaries/simultaneous-single-cell-analysis-of-5mc-and-5hmc-with-simple-seq]] (SIMPLE-seq), [[10-Summaries/high-throughput-single-cell-dna-methylation-and-chromatin-accessibility-co-profiling-with-splicool-seq]] (SpliCOOL-seq), and other single-cell methylation methods reviewed in [[10-Summaries/zachary-2013-naturereviewsgenetics]] and [[10-Summaries/yilei-2025-naturereviewsgenetics]].
- The viral-mimicry framing connects DNA methylation directly to chromatin architecture and innate immunity — overlaps with [[40-Topics/chromatin-architecture]].

## Open questions

- Locus-specific resolution lost. For studies requiring promoter-level methylation, scBS-seq or SIMPLE-seq is needed.
- Generalization beyond AML: would scTEM-seq detect interesting heterogeneity in solid tumors with subtler methylation differences?

## Related

- [[40-Topics/dna-methylation]] · [[30-Concepts/transposable-elements]] · [[30-Concepts/decitabine]] · [[30-Concepts/viral-mimicry]] · [[20-Entities/heather-lee]]
