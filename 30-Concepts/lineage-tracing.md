---
type: concept
title: Lineage tracing
aliases: [cell lineage tracing, lineage reconstruction, lineage tracing with somatic mutations, somatic lineage tracing, mutation-based lineage tracing]
tags: [development, lineage, single-cell, somatic-mutation, phylogeny]
created: 2026-05-11
updated: 2026-08-10
---

# Lineage tracing

> Reconstruction of the developmental ancestry of cells in a tissue — which cells descend from which progenitor, and when each lineage diverged. In humans, where engineered markers cannot be used, **endogenous somatic mutations** that accumulate at ~2–4 per cell division serve as natural lineage barcodes recoverable by [[40-Topics/scdna-seq]].

## Definition

Two strategies:

1. **Engineered markers** (model organisms): fluorescent reporters, Cre recombinase, CRISPR-introduced scarring (GESTALT, scGESTALT, ScarTrace). Powerful but require genetic manipulation — not applicable to humans.
2. **Endogenous mutation accumulation** (humans + model organisms): natural somatic SNVs and structural variants accumulating at known rates serve as cellular barcodes. Detected post-hoc by single-cell genome sequencing ([[10-Summaries/shao-2025-scDNA-mosaicism-review]], [[10-Summaries/evrony-2021-scDNA-applications-review]]).

For endogenous mutation-based tracing in humans, the workflow typically:
- Performs [[scwga]] (often [[pta]]) + scWGS on a sample of cells.
- Identifies lineage-informative variants (those shared among subsets of cells).
- Genotypes those variants in a larger panel of cells via targeted sequencing.
- Reconstructs a phylogenetic tree.

## Why it matters

Lineage tracing answers questions inaccessible to bulk sequencing:

- When did the progenitors of brain region X diverge from region Y?
- Which adult tissue cells descend from which embryonic clone?
- What is the clonal architecture of a tumor and how did it evolve?

In humans specifically, lineage tracing from endogenous mutations is one of the major motivations for [[40-Topics/scdna-seq]] advancement.

## Variants and refinements

- **Targeted sequencing of lineage-informative loci** — cheaper, allows thousands of cells (e.g., leukemia lineage studies cited in [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- **Whole-genome reconstruction** — slower but unbiased; preferred when lineage markers are unknown a priori.
- **Combined with single-cell phenotype** (scRNA-seq, surface protein) to map lineage onto cell type — the "phenotypic association" capability in [[10-Summaries/evrony-2021-scDNA-applications-review]].
- **Synthetic / prospective barcoding** — engineered static (lentiviral, recombinase, transposase) or evolvable CRISPR recorders that accrue heritable edits; the modern prospective vs retrospective and static vs evolvable taxonomy is laid out in [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]. See [[30-Concepts/crispr-lineage-recording]].
- **Multimodal / computational** — joint genotype + state assays (DEFND-seq [[10-Summaries/olsen-2025-defnd-seq]], SDR-seq [[10-Summaries/lindenhofer-2025-sdr-seq]]) feed phylogenetic-inference algorithms reviewed in [[10-Summaries/wang-2026-multimodal-lineage-computational]]. See [[30-Concepts/phylogenetic-inference]].

## Retrospective tracing from somatic mutations

Every cell division carries some probability of introducing a unique SNV, indel or CNV that is inherited by daughter cells, so deep sequencing of clonal expansions recovers a phylogeny. This works in any human tissue but requires sensitive variant calling — PTA plus duplex — for sparse expansions ([[10-Summaries/coorens-2021-nature]], [[10-Summaries/lee-six-2018-hsc-dynamics]], [[10-Summaries/luquette-2025-pta-duplex-mosaicism]]).

Three routes to the mutation calls:

- **Bulk colony or microdissection** — sequence many clonal colonies and infer the phylogeny from shared variants ([[10-Summaries/lee-six-2018-hsc-dynamics]]).
- **Single-cell** — scDNA-seq with PTA amplification and duplex validation ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]).
- **Copy number rather than point mutations** — minimal event distance over single-cell CNA profiles, which explicitly abandons the infinite-sites assumption that aneuploid genomes violate ([[10-Summaries/wang-2021-medalt]]).

Tree-building algorithms for per-cell variant matrices: SCITE ([[10-Summaries/jahn-2016-scite]]), SiFit ([[10-Summaries/zafar-2017-sifit]]), SCARLET ([[10-Summaries/satas-2020-scarlet]]); see [[30-Concepts/phylogenetic-inference]].

Established applications: human developmental phylogeny ([[10-Summaries/coorens-2021-nature]]), hematopoietic stem cell dynamics ([[10-Summaries/lee-six-2018-hsc-dynamics]]), and cancer clonal evolution ([[10-Summaries/wang-2021-medalt]]).

## Contested points

- Lineage trees from low-coverage scWGA suffer from missing-data artifacts that distort topology. Jaccard distance (binary) is favored by Quake group; model-based clustering with EM is an alternative.
- **Missing data is not one thing.** In recorder-based tracing it splits into *heritable* dropout (a resection removing a target site, or silencing — itself lineage information, shared by descendants) and *stochastic* dropout (failed capture — noise). Treating them identically discards signal and manufactures false relationships ([[10-Summaries/jones-2020-cassiopeia]]). The same distinction plausibly applies to scWGA allelic dropout, and no source in this corpus makes it there (synthesis).
- **Homoplasy is the hard floor.** If the same character state arises independently in two branches, no inference algorithm can separate shared ancestry from convergence; the fix is assay design — more possible states per site — not better trees ([[10-Summaries/jones-2020-cassiopeia]]).
- The mutation rate per division is itself uncertain by ~2× across tissues.

## Examples

- Mapping human cortical neuron lineage with PTA-based scWGS to track the timing of brain region divergence ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- Leukemia clonal evolution by targeted sequencing of driver loci in thousands of cells.
- Identifying inhibitory vs excitatory neuron progenitor divergence in development ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Endogenous mtDNA and engineered recorders

[[10-Summaries/ludwig-2019-mtdna-lineage-tracing]] is the founding source for endogenous mtDNA barcoding: a 16.6 kb genome with a 10–100× higher mutation rate than nuclear DNA and 100–1,000s of copies per cell, so variants drift to high heteroplasmy and become robustly detectable at shallow depth. ATAC-seq covers it at 3,380-fold per million mapped reads with no enrichment step. Validated against a constructed 65-subclone tree (96% MRCA accuracy between first-generation clones, 79% within sub-clones) and against lentiviral barcodes (AUROC 0.96), and it **outperforms scRNA-inferred CNVs as a clonality measure**.

[[10-Summaries/jones-2020-cassiopeia]] supplies the inference side for engineered Cas9 recorders, including the distinction between heritable and stochastic missing data and the recognition that homoplasy is the fundamental limit of any recorder.


## Related

- [[30-Concepts/crispr-lineage-recording]] · [[30-Concepts/phylogenetic-inference]] · [[30-Concepts/mitochondrial-lineage-tracing]] · [[30-Concepts/methylation-clones-epimutation]]
- [[30-Concepts/scwga]] · [[30-Concepts/pta]] · [[30-Concepts/scdna-capabilities-framework]]
- [[40-Topics/scdna-seq]] · [[40-Topics/somatic-mosaicism]] · [[40-Topics/single-cell-lineage-tracing]]
