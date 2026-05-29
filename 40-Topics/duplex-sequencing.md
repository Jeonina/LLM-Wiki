---
type: topic
title: Duplex sequencing
aliases: [DS, duplex-seq, ultra-accurate sequencing]
tags: [sequencing, error-correction, somatic-mutation, mutational-signatures]
created: 2026-05-12
updated: 2026-05-19
---

# Duplex sequencing

> Duplex sequencing (DS) is a family of NGS methods that tag both strands of an input dsDNA molecule with complementary UMIs, sequence each strand independently, and call a base only when both strands agree at that position ([[10-Summaries/schmitt-2012-pnas]]; [[10-Summaries/kennedy-2014-duplex-protocol]]). This yields error rates below 10⁻⁸ per base — sufficient to detect somatic mutations at any allele fraction ([[10-Summaries/schmitt-2012-pnas]]) — and underpins modern mosaicism, mutational-signature, and aging-genome biology ([[10-Summaries/abascal-2021-nanoseq]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Core concepts

- [[30-Concepts/duplex-sequencing]] — the strand-consensus principle
- [[30-Concepts/umi-molecular-barcoding]] — random-yet-complementary tag adapters
- [[30-Concepts/mutational-signatures]] — patterns of trinucleotide-context substitutions revealing mutagenic exposures
- [[30-Concepts/codec]], [[30-Concepts/nanoseq]], [[30-Concepts/hidef-seq]] — leading second-generation duplex protocols

## Key entities

- [[20-Entities/lawrence-loeb]] — Loeb lab; original DS protocol
- [[20-Entities/ludmil-alexandrov]] — Alexandrov lab; UDSeq + mutational-signature framework
- [[20-Entities/tim-coorens]] — Coorens lab; SMaHT benchmark co-lead
- [[20-Entities/smaht-network]] — Somatic Mosaicism across Human Tissues consortium

## Sources, by sub-theme

### Foundational protocol
- [[10-Summaries/schmitt-2012-pnas]] — Schmitt/Loeb 2012 PNAS. Original duplex sequencing method.
- [[10-Summaries/kennedy-2014-duplex-protocol]] — Kennedy et al. 2014, Nature Protocols. The reference DS bench protocol (Loeb lab).

### Newer chemistries with lower input
- [[10-Summaries/nandi-2025-udseq]] — Nandi/Alexandrov 2025. UDSeq: ~2.5×10⁻⁹/bp from 100 pg.
- [[10-Summaries/bae-2023-codec]] — CODEC quadruplex-adaptor strategy.
- [[10-Summaries/abascal-2021-nanoseq]] — NanoSeq nuclear-genome DS protocol.

### Cross-method benchmarking
- [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] — Zhang/Coorens 2025. SMaHT benchmark of six methods (CODEC, CompDuplex-seq, HiDEF-seq, NanoSeq, ppmSeq, VISTA-seq).

### Single-cell + duplex validation
- [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] — Luquette/Walsh 2025. Uses DS to validate PTA-scDNA-seq mutation calls.
- [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] — companion paper, SMaHT PTA pipeline.
- [[10-Summaries/kriz-2025-duplex-multiome]] — Kriz 2025. Duplex-Multiome: duplex consensus integrated into 10x Multiome (point mutations + chromatin + RNA per nucleus).

### Reviews
- [[10-Summaries/evrony-2021-scDNA-applications-review]] — Evrony 2021 mosaicism + accuracy review.
- [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — Shao 2025 NRG; classifies the four duplex implementation strategies.

## Synthesized notes

_Future synthesis target_: "Duplex vs scDNA-seq complementarity" — duplex captures population mutation rates and signatures from bulk DNA; scDNA-seq captures clonality and lineage. The methods don't compete; they layer (synthesis based on [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] + [[10-Summaries/abascal-2021-nanoseq]]).

## Open questions

- **Single-cell duplex** is not yet practical: DS needs both strands of one molecule, but scWGA loses strand identity ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). [[meta-cs]] is the only single-cell-compatible variant so far. Duplex-Multiome solves it for mtDNA + nuclear point-mutation calling via 10x library ([[10-Summaries/kriz-2025-duplex-multiome]]).
- Will the convergence of mutation-rate estimates across methods (shown in the SMaHT benchmark) hold when applied to harder tissues like brain or aging muscle ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]])?

## Related

- [[40-Topics/somatic-mosaicism]] · [[40-Topics/scdna-seq]] · [[40-Topics/long-read-sequencing]]
