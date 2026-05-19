---
type: summary
title: "Clark 2018 — scNMT-seq: Joint chromatin accessibility, DNA methylation, and transcription in single cells"
source: "[[00-Sources/papers/scNMT-seq enables joint profiling of chromatin accessibility DNA methylation and transcription in single cells]]"
aliases: [Clark 2018, scNMT-seq, NMT-seq]
tags: [scNMT-seq, joint-assay, single-cell-multiomics, dna-methylation, chromatin-accessibility, NOMe-seq, foundational]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Clark et al. (2018) — *scNMT-seq: Joint chromatin accessibility, DNA methylation, and transcription in single cells* — *?*. [DOI](https://doi.org/10.1038/s41467-018-03149-4)

# Clark et al. 2018 — scNMT-seq

> Stephen J. Clark, Ricard Argelaguet, Chantriolnt-Andreas Kapourani, Thomas M. Stubbs, Heather J. Lee, Celia Alda-Catalinas, Felix Krueger, Guido Sanguinetti, Gavin Kelsey, John C. Marioni, Oliver Stegle, Wolf Reik. *Nature Communications* **9**, 781 (Feb 2018). DOI: 10.1038/s41467-018-03149-4.

## Thesis

First single-cell method that simultaneously profiles **three molecular layers — chromatin accessibility, DNA methylation, and the transcriptome — from the same cell**. scNMT-seq combines NOMe-seq chemistry (GpC methyltransferase M.CviPI labels accessible DNA) with scBS-seq and Smart-seq2 RNA, after physical DNA/RNA separation via G&T-seq logic. Validated on mouse ESCs and embryoid bodies; reveals dynamic coupling between epigenetic layers along differentiation.

## Mechanism

1. Single cell → mild lysis in M.CviPI buffer → 15 min 37°C **(GpC sites in accessible DNA become methylated; CpG endogenous methylation preserved because M.CviPI is GpC-specific)**.
2. Beads capture poly(A) RNA → Smart-seq2 cDNA arm.
3. Genomic DNA → bisulfite conversion → scBS-seq. After alignment, **A-C-G and T-C-G positions = endogenous CpG methylation; G-C-A/C/T positions = GpC accessibility**. G-C-G and C-C-G positions are discarded (ambiguous or off-target).
4. Output: per-cell methylome (~11M usable CpGs of 22M), per-cell accessibility (~15% GpC site coverage — higher than scATAC-seq's 9.4%), and full-length Smart-seq2 transcriptome.

## Key claims

- **Single-cell resolution captures known global associations**: methylation negatively correlated with both transcription and accessibility; accessibility positively correlated with transcription. Recapitulates bulk patterns at single-cell scale.
- **Locus-specific heterogeneity**: 89 introns, 47 gene-bodies show significant methylation-accessibility coupling at FDR < 0.1. Methylation–transcription coupling stronger than accessibility–transcription coupling in this dataset.
- **Base-resolution accessibility profiles**: by adapting BPRMeth, single-fiber accessibility profiles at TSSs are reconstructed at single-GpC resolution, revealing nucleosome positions (180–200 bp oscillation) and cell-to-cell heterogeneity in nucleosome placement.
- **Bivalent promoters show heterogeneous accessibility clusters** (both H3K4me3 and H3K27me3) — independent of expression level.
- **Coupling strengthens along differentiation**: as ESC → embryoid body cells progress in pseudotime, the negative correlation between DNA methylation and accessibility *increases* across nearly all genomic contexts. Argued as a possible step in lineage priming.

## Methods scope

- 70 EL16 mouse ESCs (61 passed QC, plus 3 scM&T-seq controls without M.CviPI).
- 43 E14 embryoid body cells (40 passed QC).
- BS-seq depth: ~16M PE reads/cell ESC; ~10M EB. RNA: 2.0M PE / 1.0M SE per cell.
- Bismark + HISAT2 + featureCounts pipeline.

## Surprising / load-bearing

- The single most important methodological claim: **GpC accessibility coverage from scNMT-seq exceeds scATAC-seq's** (~15% vs ~9.4%), and the resolution is set by GpC frequency (~1/16 bp), not fragment length (>100 bp in ATAC). For DNA-anchored joint-assay coverage in §4.6 of the review, scNMT-seq is the joint-assay benchmark for *methylation + accessibility + RNA* — the methylation arm distinguishes it from the SHARE-seq / sci-CAR / 10x Multiome lineage.
- **Builds directly on G&T-seq's DNA/RNA separation chemistry** and Smallwood's scBS-seq — making the Reik / Kelsey / Stegle group the dominant lineage for epigenetic+RNA joint assays, complementary to the Shendure / Trapnell sci-CAR lineage for accessibility+RNA scale-out.

## Entities / concepts touched

[[dna-methylation]] · [[chromatin-accessibility]] · [[bisulfite-sequencing]] · [[nome-seq]] · [[scbs-seq]] · [[single-cell-multiomics]] · [[20-Entities/heather-lee]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/dna-methylation]]

## Related summaries

- [[10-Summaries/macaulay-2015-gt-seq]] — DNA/RNA separation chemistry that scNMT-seq inherits.
- [[10-Summaries/cao-2018-sci-car]] — sci-CAR, scaled accessibility+RNA without methylation.
- [[10-Summaries/ma-2020-share-seq]] — SHARE-seq accessibility+RNA via split-pool.
- [[10-Summaries/hou-2016-sctrio-seq]] — scTrio-seq, alternative triple-omics with CNV instead of accessibility.
- [[10-Summaries/shen-2026-splicool-seq]] — SpliCOOL-seq, later scaling of methylation+accessibility.

---
**Source:** [Open paper](https://www.nature.com/articles/s41467-018-03149-4)
