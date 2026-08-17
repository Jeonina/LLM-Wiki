---
type: concept
title: CRISPR lineage recording
aliases: [evolvable barcodes, CRISPR recorder, molecular recording, synthetic evolvable barcodes]
tags: [lineage-tracing, CRISPR, synthetic-barcodes, phylogenetics, prime-editing, base-editing]
created: 2026-06-02
updated: 2026-06-02
---

# CRISPR lineage recording

> A class of *prospective, evolvable* synthetic lineage-tracing systems in which Cas9 (or relatives) progressively accumulates heritable edits in a transgenic reporter, so the order of edits reconstructs a cell-division phylogeny ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Definition

Inducible Cas9 plus single-guide RNAs generate double-strand breaks in a multi-target reporter cassette; error-prone repair (typically non-homologous end joining) writes a different sequence in each cell, and repeated cutting makes the barcode *evolvable* — accumulating new mutations over time to diversify the record ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]). Slightly mismatched guides tune editing rate for temporal resolution ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Why it matters

- Enables reconstruction of detailed phylogenetic trees — up to whole-organism scale — rather than just clonal grouping ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).
- Distinguished from *static* synthetic barcodes (one immutable label/cell) and from *retrospective* natural-variant tracing ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Variants and refinements

- **Diversity-boosting nucleases**: self-homing hgRNAs (self-targeting → enormous diversity, used for organism-wide trees); base editors (substitutions, not deletions); Cas12a (cuts outside its guide-recognized sequence) ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).
- **Writer fusions**: Cas9 + template-independent polymerase (TdT) adds insertions, used to trace fetal→adult HSC transition; prime-editing-based recording writes known "symbols," enabling probe-based spatial readout (PE-tracer) ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).
- **Cas9-independent**: T7-polymerase (TRACE) or SceI (SMALT) fused to cytidine deaminases for continuous editing ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).

## Contested points

- Original tandem-target reporters suffer inter-site deletions that collapse effective diversity, low reporter expression causing scRNA-seq dropout, and low editing efficiency leaving unedited cells ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]).
- Bioinformatic interpretation of sparse edits across many alleles is the main downstream bottleneck ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]); CRISPR-aware phylogenetic models (Cassiopeia, STARTLE) enforce edit irreversibility and model dropout ([[10-Summaries/wang-2026-multimodal-lineage-computational]]).

## Related

- [[30-Concepts/phylogenetic-inference]] · [[30-Concepts/lineage-tracing]]
- [[40-Topics/single-cell-lineage-tracing]] · [[20-Entities/jay-shendure]]

## Added 2026-08-17

Six sources ingested 2026-08-14 cover the reconstruction side of CRISPR recorders, and together they show a field where **the chemistry keeps outrunning the models**. (synthesis)

**The one clean benchmark.** The Allen Institute's **Cell Lineage Reconstruction DREAM Challenge** (2020) is the only blinded, organiser-scored comparison in this literature — three sub-challenges at 76 in-vitro trees of <100 cells, 1,000 cells in silico, and 10,000 cells in silico. [[10-Summaries/gong-2022-dclear|DCLEAR]] won sub-challenges 2 and 3, i.e. both *scale* tiers ([[10-Summaries/gong-2022-dclear]]). Every other tool paper in this area benchmarks itself.

**Model progression, driven by recorder generation:**

- **Plain Cas9 indels** → non-modifiability (an edited site can never change again) plus convergent edit outcomes → **star homoplasy** ([[10-Summaries/sashittal-2023-startle]]).
- **Advanced recorders (KP-tracer, intMEMOIR, CARLIN)** → add heritable missingness, mutation-rate decay, and heterogeneous per-site edit sets → **PMM** ([[10-Summaries/chu-2025-laml]]).
- **Prime-editing sequential recorders** → each insertion deactivates its site and activates the next, so **edit order is recorded** → sequential-insertion likelihood ([[10-Summaries/seidel-2026-sciphy]]). Prior analyses used UPGMA with custom distances, discarding order entirely.

Anyone choosing a tool must first ask which recorder generated the data. (synthesis)

**The distance metric matters more than expected.** Plain Hamming distance treats every state difference as equivalent, ignoring that a handful of indel outcomes dominate — so sharing a *rare* edit is far stronger evidence of shared ancestry than sharing a common one. Better metrics substantially outperform Hamming ([[10-Summaries/gong-2022-dclear]]); the probabilistic methods model the same information mechanistically as variable insert propensities ([[10-Summaries/seidel-2026-sciphy]]). (synthesis)

**Phylodynamics, and its price.** Bayesian frameworks in BEAST 2 estimate not just trees but population parameters — birth rate, death rate, sampling proportion ([[10-Summaries/seidel-2022-tidetree]]). Birth–death models are non-identifiable unless one rate is fixed, so every phylodynamic estimate rests on an externally supplied number ([[10-Summaries/seidel-2022-tidetree]]). MCMC cost is real: trees above 700 lineages were discarded during validation ([[10-Summaries/seidel-2022-tidetree]]), and [[10-Summaries/chu-2025-laml|LAML]] criticises the BEAST-based methods as built for older recorders and very computationally intensive.

**The method changes the answer.** SciPhy reports significant differences from UPGMA trees on the same data, "underscoring the impact of the reconstruction method on the inferred cellular relationships and growth dynamics" ([[10-Summaries/seidel-2026-sciphy]]) — the lineage-tracing equivalent of the caller-concordance problem in [[40-Topics/mosaic-variant-calling|mosaic variant calling]] ([[10-Summaries/ha-2023-natmethods]]). (synthesis)

**None of it transfers to human tissue.** Engineered recorders cannot be installed in humans, so human somatic lineage tracing is restricted to endogenous markers — somatic SNVs, [[mitochondrial-lineage-tracing|mtDNA]], or [[methylation-clones-epimutation|epimutations]] — at far lower mutation rates and with no controlled recording window. (synthesis)
