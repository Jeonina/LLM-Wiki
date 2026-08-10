---
type: summary
title: "McKenna et al. 2010 — The Genome Analysis Toolkit (GATK): a MapReduce framework for NGS data"
source: "[[00-Sources/papers/The Genome Analysis Toolkit_ A MapReduce framework for analyzing next-generation DNA sequencing data]]"
source_kind: paper
author: "Aaron McKenna, Matthew Hanna, Eric Banks, Andrey Sivachenko, Kristian Cibulskis, Andrew Kernytsky, Kiran Garimella, David Altshuler, Stacey Gabriel, Mark Daly, Mark A. DePristo (corresponding)"
published: 2010-09-01
ingested: 2026-08-10
doi: "10.1101/gr.107524.110"
journal: "Genome Research"
tags: [GATK, variant-calling, MapReduce, framework, computational-tool, foundational-infrastructure, Broad-Institute]
entities: []
concepts: ["[[single-cell-variant-calling]]", "[[monovar]]", "[[sccaller]]"]
topics: ["[[mosaic-variant-calling]]"]
---

**Citation:** McKenna et al. (2010) — *The Genome Analysis Toolkit: a MapReduce framework for analyzing next-generation DNA sequencing data* — *Genome Research* 20, 1297–1303. [DOI](https://doi.org/10.1101/gr.107524.110)

# McKenna 2010 — GATK

> Not a variant caller — a **framework**. GATK separates the tedious, error-prone work of streaming and sharding BAM data from the analysis logic, exposing a small set of "traversals" (locus-based, read-based) that walkers consume via map/reduce. That separation is why the Broad could optimize one engine and get correctness, memory efficiency and automatic parallelization for every downstream tool at once.

## Key claims

- The bottleneck in 2010 was not algorithms but data-access engineering; a shared, optimized access layer removes a large development gap between sequencer output and results.
- Two traversal types cover the majority of analysis needs: **locus-based** (all reads spanning each reference base, plus reference-ordered data) and **read-based** (each read once, with its reference context).
- **Sharding** — multi-kilobase self-contained genomic chunks sized by the engine from BAM storage characteristics — is the mechanism enabling controlled memory use and parallelization, and it is deliberately agnostic to the filesystem or scheduler.
- Automatic shared-memory parallelization comes free to any walker implementing `TreeReducible`; the engine reassembles results in reference order.
- Demonstrations: an 83-line depth-of-coverage walker (used to expose MHC/HLA mapping dropouts in 1000 Genomes JPT samples) and a 57-line naïve Bayesian genotyper.
- The naïve genotyper on NA12878 chr1 called 315,202 variants, 81.70% in dbSNP, 99.76% concordance (99.84% at HapMap sites, 99.81% of homozygous variants correct) — good concordance but an honestly-reported false-positive problem, since 82% dbSNP falls short of the ~90% expected for a CEPH individual.
- 12 processors reduced the 863-minute single-processor chr1 genotyping to slightly over 1/12 the time, with no code change; distributed mode scaled out to 50 processors.

## Methods / evidence

Engineering paper with runtime benchmarks and a concordance evaluation on 1000 Genomes pilot data. The authors are candid that the demonstration genotyper is naïve and exists to show the framework, not to be used — the production multisample genotyper (later HaplotypeCaller lineage) is cited as in preparation. Evidence for the framework claim is adoption: within a year of development GATK already underpinned quality-score recalibration, indel realignment, HLA typing and multisample genotyping in both 1000 Genomes and TCGA.

## Surprising or load-bearing bits

- **Why this belongs in a single-cell wiki:** every single-cell variant caller in the corpus is defined by its relationship to GATK. [[monovar]], [[sccaller]], [[dou-2023-monopogen|Monopogen]] and the mosaic callers all inherit GATK's data model (BAM → pileup → posterior per site) while replacing its **diploid, uniform-coverage prior** — the assumption that WGA violates. Reading GATK is reading the null model those tools reject.
- The MapReduce framing is now historical (GATK4 moved to Spark), but the traversal abstraction persists and is why per-locus single-cell callers are cheap to write.
- The explicit statement that multi-locus traversals were *not implemented* and would cost memory foreshadows why haplotype-aware and phasing-based methods ([[zaccaria-2021-chisel|CHISEL]], linked-read approaches) needed separate engineering rather than a GATK walker.
- The depth-of-coverage MHC example is a nice early illustration of reference-bias-driven coverage dropout — the same class of artifact that [[highly-repetitive-regions]] handling still struggles with.

## Concepts touched

- [[single-cell-variant-calling]] — GATK is the bulk baseline; the single-cell field's contribution is amplification-aware likelihood models on top of this substrate.
- [[monovar]] / [[sccaller]] — both are explicitly framed as fixes to GATK-style calling under WGA.
- [[allele-dropout]] — the diploid prior GATK assumes is what ADO breaks.

## Connections to other sources

- Sits directly downstream of [[li-2009-samtools|SAMtools]] (the SAM/BAM format GATK builds on) and [[li-2009-bwa|BWA]].
- Rejected-as-inadequate-for-single-cells by [[zafar-2016-monovar]] and [[dong-2017-sccaller]]; used as a preprocessing/baseline step by nearly everything else, including [[luquette-2019-natcomm]] and the mosaic-calling benchmarks.
- [[heumos-2023-best-practices]] and [[gawad-2016-scgenome-review]] both position GATK as the assumed starting point.

## Open questions

- The corpus lacks a source stating *which* GATK version/mode current single-cell pipelines actually run (GATK4 HaplotypeCaller vs Mutect2 vs UnifiedGenotyper legacy) — a practical gap for a methods review.

## Related

- [[single-cell-variant-calling]] · [[zafar-2016-monovar]] · [[dong-2017-sccaller]] · [[mosaic-variant-calling]]
