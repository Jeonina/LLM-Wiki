---
type: topic
title: DNA methylation
aliases: [methylation topic, 5mC topic]
tags: [methylation, epigenetics]
created: 2026-05-11
updated: 2026-05-12
---

# DNA methylation

> Covalent modification of cytosine (predominantly 5-methylcytosine at CpG dinucleotides) that propagates through mitosis, contributes to cell identity, silences transposons, establishes imprints, and is dysregulated in cancer and aging. The wiki's methylation cluster covers the biology of methylation, the canonical measurement chemistries (bisulfite, long-read direct detection), and the enzymatic machinery (DNMT, TET).

## Core concepts

### Biology

- [[30-Concepts/dna-methylation]] — the modification itself.
- [[30-Concepts/cpg-island]] — unmethylated regulatory features.
- [[30-Concepts/dnmt]] — methyltransferase enzymes.
- [[30-Concepts/tet-enzymes]] — active demethylation pathway.
- [[30-Concepts/5hmc]] — oxidative intermediate / stable enhancer mark.
- [[30-Concepts/uhrf1]] — DNMT1 maintenance cofactor.
- [[30-Concepts/epigenetic-memory]] — heritable cell-type memory through methylation.
- [[30-Concepts/transposable-elements]] — silenced by methylation; [[30-Concepts/viral-mimicry]] when re-expressed.
- [[30-Concepts/epigenetic-aging]] — methylation clocks.
- [[30-Concepts/cancer-of-unknown-primary]] — methylation as tissue-of-origin classifier.

### Measurement

- [[30-Concepts/bisulfite-sequencing]] — standard short-read assay.
- [[30-Concepts/long-read-sequencing]] — direct methylation detection without conversion.
- [[30-Concepts/taps]] — bisulfite-free 5mC chemistry (TET + borane).
- [[30-Concepts/nome-seq]] — GpC methyltransferase for accessibility readout.
- [[30-Concepts/sctem-seq]] — single-cell SINE Alu methylation as global-methylation proxy.
- [[30-Concepts/simple-seq]] — single-cell 5mC + 5hmC joint at base resolution.
- [[30-Concepts/splicool-seq]] — single-cell 5mC + accessibility.
- [[30-Concepts/scepi2-seq]] — single-cell histone mark + 5mC.
- [[30-Concepts/6-base-cut-and-tag]] — 5mC + 5hmC at histone-marked fragments.

## Key entities

- [[20-Entities/alexander-meissner]] — foundational methylation development review.
- [[20-Entities/fritz-sedlazeck]] — long-read methylation analysis.
- [[20-Entities/winston-timp]] — nanopore methylation pioneer.
- [[20-Entities/chengqi-yi]] — bisulfite-free chemistry (SIMPLE-seq, hmC-CATCH).
- [[20-Entities/chun-xiao-song]] — TAPS chemistry inventor.
- [[20-Entities/heather-lee]] — scTEM-seq, single-cell methylation in AML.
- [[20-Entities/xiaoying-fan]] — SpliCOOL-seq high-throughput multi-omics.
- [[20-Entities/joseph-costello]] — glioma methylation, EPICUP classifier.
- [[20-Entities/shankar-balasubramanian]] — 6-base sequencing (biomodal evoC).
- [[20-Entities/biomodal]] — 6-base sequencing kits (5mC + 5hmC).

## Sources, by sub-theme

### Biology

- [[10-Summaries/zachary-2013-naturereviewsgenetics]] — Smith & Meissner foundational review.
- [[10-Summaries/dna-methylation-an-epigenetic-mark-of-cellular-memory-experimental-molecular-medicine]] — Kim/Costello 2017 epigenetic memory review.

### Computational analysis and long-read methods

- [[10-Summaries/yilei-2025-naturereviewsgenetics]] — long-read computational methylation analysis.
- [[10-Summaries/profiling-the-epigenome-using-long-read-sequencing]] — Liu/Conesa 2025 NRG review.

### Single-cell methylation methods

- [[10-Summaries/sctem-seq-single-cell-analysis-of-transposable-element-methylation-to-link-global-epigenetic-heterogeneity-with-transcriptional-programs]] — Hunt/Lee 2022 (scTEM-seq).
- [[10-Summaries/simultaneous-single-cell-analysis-of-5mc-and-5hmc-with-simple-seq]] — Bai/Yi 2024 (SIMPLE-seq).
- [[10-Summaries/high-throughput-single-cell-dna-methylation-and-chromatin-accessibility-co-profiling-with-splicool-seq]] — Shen/Fan 2026 (SpliCOOL-seq).
- [[10-Summaries/single-cell-multi-omic-detection-of-dna-methylation-and-histone-modifications-reconstructs-the-dynamics-of-epigenomic-maintenance]] — Geisenberger/van Oudenaarden 2025 (scEpi²-seq).

### Methylation + chromatin joint readouts

- [[10-Summaries/sequencing-dna-methylation-and-hydroxymethylation-at-co-occurring-chromatin-features]] — Tavares/Balasubramanian 2026 (6-base-CUT&Tag).

### Long-read methylation in repetitive regions

- [[10-Summaries/single-molecule-targeted-accessibility-and-methylation-sequencing-of-centromeres-telomeres-and-rdnas-in-arabidopsis]] — Mo/Zhai 2023 (STAM-seq, plant HRRs).

## Synthesized notes

_None yet._

## Open questions

- Methylation calling accuracy benchmarking across PacBio and ONT platforms — no community-standard benchmark.
- 5hmC: functional mark vs intermediate — unresolved.
- Single-cell methylation at scale — current methods are sparse; intersection with [[scdna-seq]] remains an open methodological frontier.
- Non-CpG methylation (mCpH) in adult tissues, especially brain — functional significance.
