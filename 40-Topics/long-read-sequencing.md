---
type: topic
title: Long-read sequencing
aliases: [PacBio, Oxford Nanopore, long-read]
tags: [sequencing, long-read, third-generation]
created: 2026-05-11
updated: 2026-05-19
---

# Long-read sequencing

> The enabling platform layer beneath several recent breakthroughs in this vault: single-molecule chromatin footprinting ([[fiber-seq]] per [[10-Summaries/andrewb-2020-science]]; [[daf-seq]] per [[10-Summaries/elliott-2025-naturebiotechnology]]), direct methylation detection without bisulfite conversion ([[10-Summaries/yilei-2025-naturereviewsgenetics]]; [[10-Summaries/liu-2025-longread-epigenome-review]]), scDAF-seq chromosome-length consensus reads ([[10-Summaries/elliott-2025-naturebiotechnology]]), and duplex sequencing variants like HiDEF-seq ([[10-Summaries/diane-2025-naturereviewsgenetics]]).

## Core concepts

- [[30-Concepts/long-read-sequencing]] — PacBio HiFi and Oxford Nanopore platforms.
- [[30-Concepts/oxford-nanopore]] — ONT platform.
- [[30-Concepts/pacbio]] — PacBio SMRT platform.
- [[30-Concepts/fiber-seq]] — m6A-based single-molecule chromatin footprinting (PacBio).
- [[30-Concepts/daf-seq]] — deaminase-based single-molecule chromatin footprinting (PacBio).
- [[30-Concepts/duplex-sequencing]] — HiDEF-seq, SMM-seq are long-read duplex variants.
- [[30-Concepts/bisulfite-sequencing]] — short-read alternative that long-read methods supplant for methylation.
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

- [[10-Summaries/yilei-2025-naturereviewsgenetics]] — Fu/Sedlazeck/Timp NRG computational long-read methylation analysis.
- [[10-Summaries/fu-2025-longread-methylation]] — Fu et al. detailed computational methylation analysis.
- [[10-Summaries/liu-2025-longread-epigenome-review]] — Liu/Conesa 2025 NRG broader epigenome review (methylation + accessibility + 3D + transcriptomic LRS).

### Long-read single-molecule chromatin

- [[10-Summaries/andrewb-2020-science]] — Fiber-seq (Stergachis 2020).
- [[10-Summaries/elliott-2025-naturebiotechnology]] — DAF-seq / scDAF-seq.
- [[10-Summaries/nanda-2024-smrt-tag]] — SMRT-Tag (Ramani lab).
- [[10-Summaries/abdulhay-2020-samosa]] — SAMOSA (Ramani lab).
- [[10-Summaries/mo-2023-stam-seq]] — STAM-seq, plant HRRs.

### Long-read SV detection

- [[10-Summaries/liu-2025-nanopore-lscc-svs]] — SomaGauss-SV in LSCC.
- [[10-Summaries/liu-2025-somagauss-lscc]] — SomaGauss-SV companion paper.

### Long-read referenced in scDNA-seq context

- [[10-Summaries/diane-2025-naturereviewsgenetics]] — HiDEF-seq and other long-read duplex methods.
- [[10-Summaries/anna-2019-nature]] — Oxford Nanopore validation of GoT for distal loci.

## Synthesized notes

_None yet._

## Open questions

- Cost per Gb at scale — still higher than short-read Illumina; gap closing but not closed (synthesis).
- Methylation calling accuracy benchmarking across platforms ([[10-Summaries/fu-2025-longread-methylation]]; [[10-Summaries/yilei-2025-naturereviewsgenetics]]).
- Long-read single-cell methods — emerging but not yet routine; scDAF-seq is currently the most successful single-cell long-read application ([[10-Summaries/elliott-2025-naturebiotechnology]]).

## Synthesized notes

- [[50-Notes/regulatory-layers-overview]] — long-read methods read accessibility + methylation + 3D simultaneously on the same fiber.
