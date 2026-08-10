---
type: summary
title: "Li & Durbin 2009 — Fast and accurate short read alignment with Burrows–Wheeler transform (BWA)"
source: "[[00-Sources/papers/Fast and accurate short read alignment with Burrows–Wheeler transform]]"
source_kind: paper
author: "Heng Li, Richard Durbin (corresponding)"
published: 2009-05-18
ingested: 2026-08-10
doi: "10.1093/bioinformatics/btp324"
journal: "Bioinformatics"
tags: [BWA, alignment, Burrows-Wheeler, FM-index, backward-search, infrastructure, gapped-alignment]
entities: ["[[heng-li]]"]
concepts: ["[[read-alignment]]", "[[mappability]]", "[[single-cell-variant-calling]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[computational-methods]]", "[[scdna-seq]]"]
---

**Citation:** Li & Durbin (2009) — *Fast and accurate short read alignment with Burrows–Wheeler transform* — *Bioinformatics* 25, 1754–1760. [DOI](https://doi.org/10.1093/bioinformatics/btp324)

# Li & Durbin 2009 — BWA

> The aligner that made human-scale resequencing routine. Instead of hashing reads or hashing the genome, BWA searches a **Burrows–Wheeler transform** of the reference, which lets exact repeats collapse onto a single path — so a read matching a repeat is aligned once, not once per copy. **10–20× faster than MAQ** at comparable accuracy, with gapped alignment for single-end reads and SAM output.

## Key claims

- **The problem in 2009**: an Illumina run produced 50–200 million reads of 32–100 bp. Hash-based aligners either scanned the whole genome per batch (flexible memory, high overhead) or indexed the genome in RAM (parallelizable but memory-hungry and sensitive to error rate).
- **The BWT insight.** Backward search over the BWT mimics top-down traversal of the reference's prefix trie **without materializing the trie**, counting exact occurrences of a length-*m* string in *O*(*m*) time **independent of genome size**. Because exact repeats collapse to one trie path, repetitive reads cost the same as unique ones — the stated reason BWT algorithms are efficient.
- **Inexact matching** is a bounded backtracking search: recursively enumerate SA intervals of substrings within *z* differences (mismatches *or* gaps) of the query, pruned by a precomputed array *D*(*i*) giving a lower bound on differences in the query prefix. The tighter *D*, the smaller the search space; a naive *D* = 0 makes the search exponential in *z*. *D* is computed in *O*(|*W*|) using the BWT of the **reversed** reference.
- **Gapped alignment for single-end reads** is the concrete capability MAQ lacked, and the reason BWA was needed for longer reads where indels occur frequently.
- Memory: BWT construction for the human genome via the BWT-SW algorithm needs **under 1 GB at peak**, against ~12 GB for the standard *n*⌈log₂*n*⌉-bit suffix-array construction.
- Supports both **base-space Illumina and colour-space SOLiD** reads, and emits **SAM** — pairing it with [[li-2009-samtools|SAMtools]] for everything downstream.
- Evaluated against simulation ground truth, on real paired-end data by the fraction mapped in consistent pairs, and by counting misalignments against a hybrid genome.

## Methods / evidence

Simulated reads with known true positions give a direct accuracy measure; consistent-pair fraction and hybrid-genome misalignment counts serve as reference-free checks on real data. Speed is compared head-to-head with MAQ.

## Surprising or load-bearing bits

- **Repeat collapsing is why the speed gain exists**, and it is also the origin of the multi-mapping problem every downstream tool inherits. A read that matches many places is cheap to find and impossible to place — which is why mappability filters appear in every pipeline in this wiki, and why [[meers-2019-seacr|SEACR]] has to explicitly discard blocks overlapping IgG artefacts at repeats.
- BWA plus SAM was designed as a **pair**: the aligner and the format were published within weeks of each other by the same author, which is how the modular alignment→analysis architecture arrived fully formed.
- The **memory result matters more than the speed result for single-cell work**: sub-1 GB indexing means thousands of per-cell alignments can be run in parallel on ordinary hardware. Shallow single-cell WGS ([[zahn-2017-dlp|DLP]], [[laks-2019-dlp-plus|DLP+]]) means many tiny alignment jobs, not one large one, so per-process footprint dominates.
- The *z*-difference model — a fixed edit-distance budget per read — is the assumption that later breaks down for long reads and highly divergent regions, and is why BWA-MEM's seed-and-extend approach superseded this algorithm for reads over ~100 bp. This paper describes `bwa aln`, not the `bwa mem` most pipelines use today.
- Hi-C read handling exposes the limitation directly: a chimeric ligation read spans two loci and needs **chimeric rescue** or two-step mapping, which pipelines like [[servant-2015-hicpro|HiC-Pro]] add on top rather than getting from the aligner.

## Entities mentioned

- [[heng-li]] — first author; also SAM/BAM ([[li-2009-samtools]]) and much of the field's alignment tooling.

## Concepts touched

- [[read-alignment]] — BWT/FM-index search is one of the two dominant alignment paradigms (the other being seed-and-extend hashing).
- [[mappability]] — repeat collapsing makes multi-mapping cheap to detect and unresolvable to place.

## Connections to other sources

- Output format and downstream toolkit: [[li-2009-samtools]]; variant calling: [[mckenna-2010-gatk]].
- Pipelines that wrap it: [[servant-2015-hicpro]] (two-step/chimeric mapping), [[durand-2016-juicer]].
- A modern successor optimized for chromatin data: [[zhang-2021-chromap]].
- Upstream read cleaning: [[chen-2018-fastp]].

## Open questions

- Nothing substantive is left open by the paper; the practical caveat is version drift — most current work uses BWA-MEM, whose algorithm is not the one described here, so citing this paper for a BWA-MEM pipeline is a common and quiet inaccuracy.

## Related

- [[li-2009-samtools]] · [[read-alignment]] · [[zhang-2021-chromap]] · [[computational-methods]]
