---
type: summary
title: "Li et al. 2009 — The Sequence Alignment/Map format and SAMtools"
source: "[[00-Sources/papers/The Sequence Alignment_Map format and SAMtools]]"
source_kind: paper
author: "Heng Li, Bob Handsaker, Alec Wysoker, Tim Fennell, Jue Ruan, Nils Homer, Gabor Marth, Goncalo Abecasis, Richard Durbin (corresponding), 1000 Genomes Project Data Processing Subgroup"
published: 2009-06-08
ingested: 2026-08-10
doi: "10.1093/bioinformatics/btp352"
journal: "Bioinformatics"
tags: [SAM, BAM, file-format, infrastructure, pileup, indexing, BGZF, 1000-Genomes]
entities: ["[[heng-li]]"]
concepts: ["[[read-alignment]]", "[[duplicate-marking]]", "[[single-cell-variant-calling]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[computational-methods]]", "[[scdna-seq]]"]
---

**Citation:** Li et al. (2009) — *The Sequence Alignment/Map format and SAMtools* — *Bioinformatics* 25, 2078–2079. [DOI](https://doi.org/10.1093/bioinformatics/btp352)

# Li 2009 — SAM/BAM and SAMtools

> A two-page paper that defined the interface every downstream genomics tool now depends on. Before SAM, each aligner emitted its own format and each analysis tool parsed a different one. SAM's contribution is **decoupling alignment from analysis**: one text format, one indexed binary equivalent, one toolkit.

## Key claims

- **SAM** is a TAB-delimited format with a `@`-prefixed header section and an alignment section of **11 mandatory fields** (QNAME, FLAG, RNAME, POS, MAPQ, CIGAR, MRNM, MPOS, ISIZE, SEQ, QUAL) plus arbitrary `TAG:TYPE:VALUE` optional fields.
- It is deliberately platform- and aligner-agnostic: single- and paired-end, mixed read types, colour-space SOLiD reads, and reads up to 128 Mbp, designed to scale to alignment sets of **10¹¹ bases or more** — the depth of one deeply resequenced human.
- **The extended CIGAR** adds four operations to the classical M/I/D: `N` (skipped reference bases, i.e. introns), `S` (soft clip), `H` (hard clip) and `P` (padding). These are what let one format express spliced, clipped, multi-part and padded alignments.
- The **RG tag plus `@RG` header lines** attach per-read provenance — origin, sequencing centre, library. This is the field that later carries cell/sample identity through multiplexed workflows.
- **BAM** is the binary equivalent, lossless with respect to SAM, compressed with **BGZF** — a zlib-compatible block library built specifically to allow fast random access into a compressed file. 112 Gbp of Illumina data occupied 116 GB (1.0 byte per input base), most of it base qualities.
- **Coordinate sorting plus indexing** — the UCSC binning scheme combined with linear indexing — retrieves alignments overlapping any region, usually in a single seek, so tools can stream over one locus without loading the file.
- **SAMtools** provides format conversion, sorting, merging, **PCR duplicate removal**, the pileup per-position representation, SNP and short-indel calling, and a text alignment viewer. Indexing the 112 Gbp example took 40 minutes in **under 30 MB of memory**.
- SAM was the release format of the **1000 Genomes Project**, which is how it became universal rather than merely proposed.

## Methods / evidence

This is a format-specification paper; the evidence is the design plus concrete performance figures on a 112 Gbp Illumina dataset (conversion ~10 h, indexing 40 min, <30 MB RAM). Two independent implementations existed at publication — one in C, one in Java, with slightly differing functionality.

## Surprising or load-bearing bits

- **BGZF is the quietly critical invention.** Compression that permits random access is what makes a 100 GB alignment file behave like a database instead of a tape. Every region-scoped genomics operation — per-bin read counting for CNV, per-cell extraction from a merged BAM, IGV browsing — inherits from that one design choice.
- **Duplicate removal being a first-class SAMtools utility** is what makes the amplification-free argument in [[zahn-2017-dlp|DLP]] operational: the reason "fragment first, then amplify" is a coherent strategy at all is that a standard tool can then remove exact-coordinate duplicates. Under WGA the same tool silently fails, because the duplicates no longer share coordinates.
- The **RG tag** is the hook that single-cell pipelines use for cell identity in merged BAMs — a per-read metadata slot designed for sequencing-centre bookkeeping, repurposed as the cell barcode carrier.
- The paper's stated aim — "separates the alignment step from downstream analyses, enabling a generic and modular approach" — is the reason the modern tool ecosystem is composable at all. Every method in this wiki that takes a BAM as input ([[mckenna-2010-gatk|GATK]], [[zhang-2008-macs|MACS]], [[servant-2015-hicpro|HiC-Pro]], CNV callers) exists downstream of this decision.
- Most of the file is base qualities — an observation that motivated the quality-binning and CRAM work that followed.

## Entities mentioned

- [[heng-li]] — first author; also the author of BWA ([[li-2009-bwa]]) and much of the field's alignment infrastructure.

## Concepts touched

- [[read-alignment]] — SAM is the canonical output representation.
- [[duplicate-marking]] — the operation whose validity depends on library chemistry.

## Connections to other sources

- Companion aligner from the same author: [[li-2009-bwa]].
- Consumers of the format in this corpus: [[mckenna-2010-gatk]], [[zhang-2008-macs]], [[servant-2015-hicpro]], [[zhang-2021-chromap]], [[durand-2016-juicer]].
- Duplicate-filtering argument that depends on it: [[zahn-2017-dlp]].

## Open questions

- Nothing substantive is left open by the paper itself. The relevant tension for this wiki is downstream: **duplicate removal semantics differ by protocol**, and SAMtools' coordinate-based definition is only correct for libraries fragmented before amplification.

## Related

- [[li-2009-bwa]] · [[read-alignment]] · [[mckenna-2010-gatk]] · [[computational-methods]]
