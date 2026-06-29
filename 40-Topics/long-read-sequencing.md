---
type: topic
title: Long-read sequencing
aliases: [PacBio, Oxford Nanopore, ONT, HiFi, long-read]
tags: [sequencing, long-read, third-generation]
created: 2026-05-11
updated: 2026-06-29
---

# Long-read sequencing

> Third-generation sequencing technologies that read DNA molecules of kilobases to hundreds of kilobases in single contiguous reads — the two dominant platforms being **PacBio HiFi** (circular consensus, high accuracy) and **Oxford Nanopore (ONT)** — enabling direct detection of base modifications, phasing across long-range variants, and assembly across repeats that short-read sequencing cannot resolve.

Long-read sequencing is the enabling platform layer beneath several recent breakthroughs in this vault: single-molecule chromatin footprinting ([[fiber-seq]] per [[10-Summaries/andrewb-2020-science]]; [[daf-seq]] per [[10-Summaries/swanson-2025-daf-seq]]), direct methylation detection without bisulfite conversion ([[10-Summaries/fu-2025-longread-methylation]]; [[10-Summaries/liu-2025-long-read-epigenome-review]]), scDAF-seq chromosome-length consensus reads ([[10-Summaries/swanson-2025-daf-seq]]), and duplex sequencing variants like HiDEF-seq ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Platforms and how they work

- **PacBio HiFi (SMRT sequencing)**: a polymerase incorporates fluorescent nucleotides at the bottom of a zero-mode waveguide; pulse-width and inter-pulse duration during incorporation are altered by base modifications. Circular consensus sequencing (CCS) of the same molecule produces high-accuracy long reads (>99.9%) ([[10-Summaries/fu-2025-longread-methylation]]).
- **Oxford Nanopore (ONT)**: DNA threads through a protein nanopore; electrolytic current changes are interpreted by HMMs / CNNs to call bases — including modified bases that produce distinct current signatures ([[10-Summaries/fu-2025-longread-methylation]]).

### Platform variants and tooling

- **PacBio Revio** — current high-throughput HiFi platform ([[10-Summaries/fu-2025-longread-methylation]]).
- **ONT PromethION** — high-throughput nanopore platform; supports R10.4.1+ chemistry with higher accuracy ([[10-Summaries/fu-2025-longread-methylation]]).
- **Methylation callers**: Remora, primrose (PacBio); Megalodon, DeepMod (ONT) ([[10-Summaries/fu-2025-longread-methylation]]).

## Why it matters

- **No base conversion required** for methylation detection — sidesteps the three-base alignment problem of [[bisulfite-sequencing]] ([[10-Summaries/fu-2025-longread-methylation]]; [[10-Summaries/liu-2025-long-read-epigenome-review]]).
- **Direct detection of multiple modifications**: 5mC, 5hmC, 6mA, 4mC ([[10-Summaries/fu-2025-longread-methylation]]).
- **Phasing across long distances**: structural variants, repeat expansions, and imprinted regions become tractable, enabling phased / allele-specific methylation ([[10-Summaries/fu-2025-longread-methylation]]).
- **Single-molecule resolution** without amplification: native DNA is read directly, preserving any per-molecule information ([[10-Summaries/fu-2025-longread-methylation]]).
- **Access to highly repetitive regions** — centromeres, telomeres, and rDNAs become resolvable only with long reads ([[10-Summaries/liu-2025-long-read-epigenome-review]]).
- **Enabling platform for** [[fiber-seq]] (m6A footprinting via PacBio) and [[daf-seq]] (deaminase footprinting via PacBio + PTA) ([[10-Summaries/andrewb-2020-science]]; [[10-Summaries/swanson-2025-daf-seq]]).

## Core methods and concepts

- [[30-Concepts/oxford-nanopore]] — ONT platform.
- [[30-Concepts/pacbio]] — PacBio SMRT platform.
- [[30-Concepts/fiber-seq]] — m6A-based single-molecule chromatin footprinting (PacBio).
- [[30-Concepts/daf-seq]] — deaminase-based single-molecule chromatin footprinting (PacBio).
- [[40-Topics/duplex-sequencing]] — HiDEF-seq, SMM-seq are long-read duplex variants.
- [[30-Concepts/bisulfite-sequencing]] — short-read alternative that long-read methods supplant for methylation.
- [[40-Topics/dna-methylation]] — directly read without conversion via long-read base modification calling.
- [[30-Concepts/samosa]], [[30-Concepts/samosa-tag]], [[30-Concepts/smrt-tag]] — PacBio chromatin-accessibility methods.
- [[30-Concepts/stam-seq]] — plant nanopore chromatin + methylation method.
- [[30-Concepts/nanopore-adaptive-sampling]] — real-time read selection for targeted sequencing.
- [[30-Concepts/highly-repetitive-regions]] — centromeres, telomeres, rDNAs — accessible only with LRS.
- [[30-Concepts/structural-variants]], [[30-Concepts/somagauss-sv]] — somatic SV detection.
- [[30-Concepts/allele-specific-methylation]] — phased methylation via long reads.

## Key entities

- [[20-Entities/fritz-sedlazeck]] — long-read computational genomics.
- [[20-Entities/winston-timp]] — nanopore methylation pioneer.
- [[20-Entities/andrew-b-stergachis]] — Fiber-seq / DAF-seq developer (PacBio).
- [[20-Entities/elliott-g-swanson]] — DAF-seq co-first author.
- [[20-Entities/ana-conesa]] — long-read epigenome review.
- [[20-Entities/vijay-ramani]] — SAMOSA / SMRT-Tag / SAMOSA-Tag developer.
- [[20-Entities/jixian-zhai]] — STAM-seq plant epigenomics.
- [[20-Entities/jifeng-liu]] — nanopore somatic SV in head-and-neck cancer.
- [[20-Entities/dan-xie]] — SCOUT + SomaGauss-SV.

## Sources, by sub-theme

### Long-read methylation analysis

- [[10-Summaries/fu-2025-longread-methylation]] — Fu/Sedlazeck/Timp NRG computational long-read methylation analysis.
- [[10-Summaries/liu-2025-long-read-epigenome-review]] — Liu/Conesa 2025 NRG broader epigenome review (methylation + accessibility + 3D + transcriptomic LRS).

### Long-read single-molecule chromatin

- [[10-Summaries/andrewb-2020-science]] — Fiber-seq (Stergachis 2020).
- [[10-Summaries/swanson-2025-daf-seq]] — DAF-seq / scDAF-seq; uses PacBio HiFi to read DAF-seq deamination patterns at >25,000× depth on targeted loci.
- [[10-Summaries/nanda-2024-smrt-tag]] — SMRT-Tag (Ramani lab).
- [[10-Summaries/abdulhay-2020-samosa]] — SAMOSA (Ramani lab).
- [[10-Summaries/mo-2023-stam-seq]] — STAM-seq, plant HRRs.

### Long-read SV detection

- [[10-Summaries/liu-2025-nanopore-lscc-svs]] — SomaGauss-SV in LSCC.

### Long-read referenced in scDNA-seq context

- [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — HiDEF-seq and other long-read duplex methods; HiDEF-seq achieves ~7 × 10⁻¹⁶ error rate via PacBio circular consensus duplex sequencing.
- [[10-Summaries/nam-2019-got]] — Oxford Nanopore validation of GoT for distal loci.

## Synthesized notes

- [[50-Notes/regulatory-layers-overview]] — long-read methods read accessibility + methylation + 3D simultaneously on the same fiber.

## Open questions

- Cost per Gb at scale — still higher than short-read Illumina; gap closing but not closed (synthesis).
- Per-platform methylation calling accuracy varies and benchmarking lags chemistry development ([[10-Summaries/fu-2025-longread-methylation]]).
- Long-read single-cell methods — emerging but not yet routine; scDAF-seq is currently the most successful single-cell long-read application ([[10-Summaries/swanson-2025-daf-seq]]).

## Related

- [[bisulfite-sequencing]]
- [[40-Topics/dna-methylation]]
- [[40-Topics/duplex-sequencing]]
- [[fiber-seq]]
- [[daf-seq]]
- [[50-Notes/regulatory-layers-overview]]
