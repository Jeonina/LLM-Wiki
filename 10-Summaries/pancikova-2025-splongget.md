---
type: summary
title: "Pančíková et al. 2025 — Long-read single-cell genome, transcriptome and open chromatin profiling links genotype to phenotypes (SPLONGGET)"
source: "[[00-Sources/papers/Long-read single-cell genome, transcriptome and open chromatin profiling links genotype to phenotypes]]"
source_kind: paper
author: "Alexandra Pančíková, Ruben Cools, Marios Eftychiou, Margo Aertgeerts, Joris Vande Velde, Heidi Segers, Jan Cools, Luuk Harbers, Jonas Demeulemeester (corresponding)"
published: 2025-09-09
ingested: 2026-10-07
doi: "10.1101/2025.09.08.674950"
journal: "bioRxiv (preprint)"
tags: [SPLONGGET, preprint, long-read, Oxford-Nanopore, 10x-Multiome, scDNA-seq, scATAC-seq, full-length-transcriptome, genotype-to-phenotype, B-ALL, CD19, CAR-T, immune-escape, structural-variants, CNA, stub]
entities: []
concepts: ["[[oxford-nanopore]]", "[[joint-single-cell-multi-omics]]", "[[scatac-seq]]", "[[structural-variants]]", "[[copy-number-variation]]", "[[single-cell-variant-calling]]", "[[intratumor-heterogeneity]]"]
topics: ["[[long-read-sequencing]]", "[[single-cell-multiomics]]", "[[scdna-cancer-applications]]", "[[hematopoietic-malignancies]]"]
---

**Citation:** Pančíková et al. (2025) — *Long-read single-cell genome, transcriptome and open chromatin profiling links genotype to phenotypes* — *bioRxiv* (preprint). [DOI](https://doi.org/10.1101/2025.09.08.674950)

# Pančíková 2025 — SPLONGGET (stub)

> **Source caveat:** the clipping in `00-Sources` contains only the bioRxiv reference list — no abstract, results or methods. This summary is limited to the abstract as deposited with Crossref for the DOI and to what the reference list shows about the toolchain; no numbers beyond those are reported. Re-clip the full text to complete it.

> Per the deposited abstract, **SPLONGGET** (Single-cell Profiling of LONG-read Genome, Epigenome, and Transcriptome) couples **10x Genomics barcoding with Oxford Nanopore sequencing** to profile genome, chromatin accessibility and **full-length transcriptomes** in thousands of single cells. The key design move is **retaining all tagmentation fragments** during library preparation, so the ATAC-style library also delivers whole-genome coverage; target enrichment supports single-cell genotyping, and the method stays backward-compatible with short-read workflows.

## Key claims (from the deposited abstract)

- Joint per-cell calling of **small variants, structural variants and copy-number alterations** alongside accessibility and full-length RNA.
- Applied to **paediatric B-cell acute lymphoblastic leukaemia**, it revealed clonal dynamics and phenotypic effects of somatic variants.
- **Parallel evolution of immune escape** at the CAR T-cell target ***CD19***: four distinct splice-site mutations plus loss of heterozygosity.
- Built from off-the-shelf kits; pitched for genetically heterogeneous samples — tumours and ageing normal tissues.

## Methods / evidence

Not available in the clipping. The reference list indicates the analysis stack draws on: minimap2, IsoQuant, BLAZE and Flexiplex (long-read barcode handling), UMI-tools, the nf-core framework and nf-core/scnanoseq plus a released `scdnalong` pipeline, SnapATAC2 and MACS for accessibility, Clair3-style deep-learning variant calling and ClairS-TO (tumour-only somatic SNVs), Severus (somatic SVs), LongPhase (phasing), and ASCAT-style allele-specific copy number. These are cited tools, not confirmed analysis steps.

Weight: preprint, single disease application as described; cannot be assessed further from this source.

## Surprising or load-bearing bits

- **Keeping "non-accessible" tagmentation fragments turns an accessibility assay into a genome assay** — a cheap route to per-cell genotype + chromatin state without a separate WGA step (synthesis from the abstract).
- Splice-site mutations as CD19 escape are exactly the class of variant that needs **full-length transcripts** in the same cell to interpret — the case for long reads here (synthesis).

## Concepts touched

- [[oxford-nanopore]] — long-read single-cell multiome library.
- [[joint-single-cell-multi-omics]] — genotype + accessibility + transcriptome in one cell.
- [[structural-variants]] / [[copy-number-variation]] — per-cell SV and CNA calling claimed.
- [[intratumor-heterogeneity]] — parallel evolution of CD19 escape alleles.

## Connections to other sources

- Genotype-to-phenotype single-cell assays it cites and extends: [[izzo-2024-got-cha]] (genotype + accessibility), [[lindenhofer-2025-sdr-seq]] (DNA–RNA), [[macaulay-2015-gt-seq]] (G&T-seq), [[nam-2019-got]].
- Long-read single-cell epigenomics: [[li-2024-scnanoseq-cut-tag]], [[liu-2025-long-read-epigenome-review]].
- Review context cited: [[vandereyken-2023-scmultiomics-review]]; analysis tools cited: [[zhang-2024-snapatac2]], [[zhang-2008-macs]], [[mckenna-2010-gatk]], [[heumos-2023-best-practices]], [[traag-2019-leiden]].

## Open questions

- All performance figures (cells per run, per-cell genome coverage, variant-calling sensitivity, accessibility quality vs short-read 10x Multiome) are unknown from this clipping.
- How allelic dropout and Tn5 insertion bias affect genotype calls from tagmentation fragments is not assessable here.

## Related

- [[oxford-nanopore]] · [[izzo-2024-got-cha]] · [[40-Topics/long-read-sequencing]] · [[40-Topics/single-cell-multiomics]]
