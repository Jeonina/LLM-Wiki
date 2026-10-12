---
type: topic
title: Long-read sequencing
explainer: long-read-sequencing
aliases: [PacBio, Oxford Nanopore, ONT, HiFi, long-read]
tags: [sequencing, long-read, third-generation]
created: 2026-05-11
updated: 2026-10-12
paper_section: ["3.2.1"]
---

# Long-read sequencing

> Third-generation sequencing technologies that read DNA molecules of kilobases to hundreds of kilobases in single contiguous reads — the two dominant platforms being **PacBio HiFi** (circular consensus, high accuracy) and **Oxford Nanopore (ONT)** — enabling direct detection of base modifications, phasing across long-range variants, and assembly across repeats that short-read sequencing cannot resolve ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]; [[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]).

> [!abstract] 한눈에
> Long-read 시퀀싱은 bisulfite 변환 없이 native DNA에서 5mC·5hmC·6mA·4mC를 직접 읽고, short read로는 닿지 않는 centromere·telomere·rDNA까지 읽어 낸다 ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]; [[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]). 단일 세포에서는 Fiber-seq·DAF-seq 같은 단일 분자 크로마틴 footprinting과 단일 세포 long-read WGS의 기반 플랫폼이 되었다 ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]; [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [Long-read 시퀀싱 교재](../60-Explainers/long-read-sequencing.html)
<!-- /explainer-links -->

## Key points

- **Methylation is read directly, without base conversion.** Native long reads detect 5mC, 5hmC, 6mA and 4mC and sidestep the three-base alignment problem of bisulfite sequencing ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).
- **Highly repetitive regions become resolvable.** Centromeres, telomeres and rDNAs are accessible only with long reads ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]).
- **Long reads carry single-molecule chromatin footprinting.** Fiber-seq (m6A, PacBio) and DAF-seq (deaminase, PacBio + PTA) depend on them, and scDAF-seq is currently the most successful single-cell long-read application ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]; [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Single-cell long-read WGS works but has a chimera problem.** PacBio HiFi WGS of single human cells after droplet MDA is strong for SNVs, indel-type SVs and tandem repeats, but chimeras make inversion and duplication calls unusable ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).
- **PacBio passes, not length, power duplex mutation calling.** HiDEF-seq builds per-strand consensus from ~32 passes on median 1.7 kb molecules ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/pacbio|PacBio]] — SMRT sequencing; circular consensus gives high-accuracy (>99.9%) HiFi reads.
> - `concept` [[30-Concepts/oxford-nanopore|Oxford Nanopore]] — DNA threads through a protein nanopore; current changes are decoded into bases, including modified bases.
> - `concept` [[30-Concepts/fiber-seq|Fiber-seq]] — m6A-based single-molecule chromatin footprinting read on PacBio.
> - `concept` [[30-Concepts/daf-seq|DAF-seq]] — Deaminase-based single-molecule chromatin footprinting read on PacBio.
> - `concept` [[30-Concepts/nanopore-adaptive-sampling|Nanopore adaptive sampling]] — Real-time read selection for targeted sequencing.
> - `note` [[50-Notes/regulatory-layers-overview|Regulatory layers overview]] — Long-read methods read accessibility, methylation and 3D contacts on the same fiber.

## Platforms and how they work

| Platform | Principle | Note |
|---|---|---|
| PacBio HiFi (SMRT) | A polymerase incorporates fluorescent nucleotides at the bottom of a zero-mode waveguide; pulse width and inter-pulse duration shift at modified bases | Circular consensus sequencing of the same molecule gives >99.9% accurate long reads ([[10-Summaries/fu-2025-longread-methylation\|Fu 2025]]) |
| Oxford Nanopore (ONT) | DNA threads through a protein nanopore; HMMs or CNNs decode the current changes | Modified bases produce distinct current signatures ([[10-Summaries/fu-2025-longread-methylation\|Fu 2025]]) |
| PacBio Revio | — | Current high-throughput HiFi platform (synthesis) |
| ONT PromethION | — | High-throughput nanopore platform; supports R10.4.1+ chemistry with higher accuracy (synthesis) |

Methylation callers: Jasmine and ccsmeth (PacBio); Nanopolish, DeepSignal, DeepMod2, Rockfish and Dorado (ONT) ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).

## Why it matters

- **No base conversion** for methylation detection — sidesteps the three-base alignment problem of [[bisulfite-sequencing]] ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]; [[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]). See [[30-Concepts/bisulfite-sequencing]], the short-read alternative long-read methods supplant, and [[40-Topics/dna-methylation]].
- **Several modifications at once**: 5mC, 5hmC, 6mA, 4mC ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).
- **Long-range phasing**: structural variants, repeat expansions and imprinted regions become tractable, enabling phased, [[30-Concepts/allele-specific-methylation|allele-specific methylation]] ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).
- **Single-molecule resolution without amplification**: native DNA is read directly, preserving per-molecule information ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).
- **[[30-Concepts/highly-repetitive-regions|Highly repetitive regions]]** — centromeres, telomeres and rDNAs — become resolvable only with long reads ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]).
- **Platform for chromatin footprinting**: [[fiber-seq]] (m6A footprinting via PacBio) and [[daf-seq]] (deaminase footprinting via PacBio + PTA) ([[10-Summaries/andrewb-2020-science|Stergachis 2020]]; [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).

Reviews: computational long-read methylation analysis ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]) and the broader long-read epigenome — methylation, accessibility, 3D and transcriptomic long-read sequencing ([[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]).

## Single-molecule chromatin on long reads

| Method | Year | Platform | Note |
|---|---|---|---|
| [[10-Summaries/andrewb-2020-science\|Fiber-seq]] | 2020 | PacBio | m6A methyltransferase stenciling of chromatin fibers ([[10-Summaries/andrewb-2020-science\|Stergachis 2020]]) |
| [[10-Summaries/abdulhay-2020-samosa\|SAMOSA]] | 2020 | PacBio | Single-molecule oligonucleosome footprinting, Ramani lab ([[10-Summaries/abdulhay-2020-samosa\|SAMOSA]]) |
| [[10-Summaries/mo-2023-stam-seq\|STAM-seq]] | 2023 | ONT, adaptive sampling | Accessibility + methylation in plant highly repetitive regions ([[10-Summaries/mo-2023-stam-seq\|STAM-seq]]) |
| [[10-Summaries/nanda-2024-smrt-tag\|SMRT-Tag / SAMOSA-Tag]] | 2024 | PacBio | Tagmentation for PacBio at 40 ng input, Ramani lab ([[10-Summaries/nanda-2024-smrt-tag\|SMRT-Tag]]) |
| [[10-Summaries/swanson-2025-daf-seq\|DAF-seq / scDAF-seq]] | 2025 | PacBio HiFi (+ PTA) | Reads deamination patterns at >25,000× depth on targeted loci; chromosome-length single-cell consensus reads ([[10-Summaries/swanson-2025-daf-seq\|Swanson 2025]]) |

Related concepts: [[30-Concepts/samosa]], [[30-Concepts/samosa-tag]], [[30-Concepts/smrt-tag]] (PacBio chromatin-accessibility methods), [[30-Concepts/stam-seq]] (plant nanopore chromatin + methylation) and [[30-Concepts/nanopore-adaptive-sampling]].

## Single-cell long-read genomics and multiomics

| Study | Year | Platform | Design | Key finding |
|---|---|---|---|---|
| [[10-Summaries/nam-2019-got\|GoT]] | 2019 | ONT | Validation of distal loci | Oxford Nanopore used to validate Genotyping of Transcriptomes at distal loci ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| [[10-Summaries/hard-2023-long-read-scwgs\|Hård 2023]] | 2023 | PacBio HiFi | Droplet MDA, genome-wide | First genome-wide long-read WGS of single human cells; strong for SNVs, indel-type SVs and TRs, but chimeras make inversion and duplication calls unusable ([[10-Summaries/hard-2023-long-read-scwgs\|Hård 2023]]) |
| [[10-Summaries/li-2023-scnanohi-c\|scNanoHi-C]] | 2023 | Nanopore | Concatemer sequencing | Single-cell Hi-C read as long concatemers ([[10-Summaries/li-2023-scnanohi-c\|scNanoHi-C]]) |
| [[10-Summaries/li-2024-scnanoseq-cut-tag\|scNanoSeq-CUT&Tag]] | 2024 | Nanopore | Single-cell CUT&Tag | Per-copy L1Hs chromatin states ([[10-Summaries/li-2024-scnanoseq-cut-tag\|scNanoSeq-CUT&Tag]]) |
| [[10-Summaries/li-2025-scnanoatac-seq2\|scNanoATAC-seq2]] | 2025 | Nanopore | Single-cell ATAC | Allele- and repeat-copy-resolved accessibility ([[10-Summaries/li-2025-scnanoatac-seq2\|scNanoATAC-seq2]]) |
| [[10-Summaries/pancikova-2025-splongget\|SPLONGGET]] | 2025 | ONT PromethION | 10x Multiome, targeted re-enrichment | Genome + accessibility + full-length transcriptome per cell; CD19 splice-site escape in B-ALL (preprint) ([[10-Summaries/pancikova-2025-splongget\|SPLONGGET]]) |

## Somatic mutations and structural variants

- **Duplex consensus from passes.** HiDEF-seq uses PacBio long reads not for length but for passes: ~32 independent passes per strand on median 1.7 kb molecules build a per-strand consensus good enough to call substitutions on unamplified single molecules ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]). It reaches an error rate of ~7 × 10⁻¹⁶ via PacBio circular-consensus duplex sequencing ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **PacBio fidelity is better than assumed.** Concordant dsDNA burdens were obtained at ≥5 passes rather than ≥20 ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).
- **The pass–length tradeoff.** ssDNA analysis needs ≥20 passes, which forces shorter fragments (1.7 kb rather than 4.2 kb) and roughly 4× the sequencing per molecule ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).
- **Not all duplex methods are long-read.** HiDEF-seq is a long-read (PacBio) duplex variant, whereas SMM-seq is sequenced on Illumina ([[10-Summaries/maslov-2022-smm-seq|Maslov 2022]]); see [[40-Topics/duplex-sequencing]].
- **Somatic SVs.** Nanopore SomaGauss-SV calling in laryngeal squamous cell carcinoma ([[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]); see [[30-Concepts/structural-variants]] and [[30-Concepts/somagauss-sv]].

## Key people

- [[20-Entities/fritz-sedlazeck]] — long-read computational genomics.
- [[20-Entities/winston-timp]] — nanopore methylation pioneer.
- [[20-Entities/andrew-b-stergachis]] — Fiber-seq / DAF-seq developer (PacBio).
- [[20-Entities/elliott-g-swanson]] — DAF-seq co-first author.
- [[20-Entities/ana-conesa]] — long-read epigenome review.
- [[20-Entities/vijay-ramani]] — SAMOSA / SMRT-Tag / SAMOSA-Tag developer.
- [[20-Entities/jixian-zhai]] — STAM-seq plant epigenomics.
- [[20-Entities/jifeng-liu]] — nanopore somatic SV in head-and-neck cancer.
- [[20-Entities/dan-xie]] — SCOUT + SomaGauss-SV.

## Open questions

- Cost per Gb at scale is still higher than short-read Illumina; the gap is closing but not closed (synthesis).
- Per-platform methylation calling accuracy varies, and benchmarking lags chemistry development ([[10-Summaries/fu-2025-longread-methylation|Fu 2025]]).
- Long-read single-cell methods are emerging but not yet routine; scDAF-seq is currently the most successful single-cell long-read application ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- Whole-genome amplification chimeras limit inversion and duplication calls in single-cell long-read WGS ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]); whether PTA- or amplification-free designs remove this is open. (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/dna-methylation|DNA methylation]] — 5-methylcytosine, read directly without conversion by long-read base-modification calling.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Single-molecule strategy that calls a base only when both strands agree.

## All sources on this page

> [!info]- 17 summaries cited here
> - [[10-Summaries/abdulhay-2020-samosa|Abdulhay 2020]]
> - [[10-Summaries/andrewb-2020-science|Stergachis 2020]]
> - [[10-Summaries/fu-2025-longread-methylation|Fu 2025]]
> - [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]
> - [[10-Summaries/li-2023-scnanohi-c|Li 2023]]
> - [[10-Summaries/li-2024-scnanoseq-cut-tag|Li 2024]]
> - [[10-Summaries/li-2025-scnanoatac-seq2|Li 2025]]
> - [[10-Summaries/liu-2024-hidef-seq|Liu 2024]]
> - [[10-Summaries/liu-2025-long-read-epigenome-review|Liu & Conesa 2025]]
> - [[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]
> - [[10-Summaries/maslov-2022-smm-seq|Maslov 2022]]
> - [[10-Summaries/mo-2023-stam-seq|Mo 2023]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
> - [[10-Summaries/nanda-2024-smrt-tag|Nanda 2024]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
