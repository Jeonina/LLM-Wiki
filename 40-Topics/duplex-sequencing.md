---
type: topic
title: Duplex sequencing
aliases: [DS, duplex-seq, ultra-accurate sequencing]
tags: [sequencing, error-correction, somatic-mutation, mutational-signatures]
created: 2026-05-12
updated: 2026-05-12
---

# Duplex sequencing

> Duplex sequencing (DS) is a family of NGS methods that tag both strands of an input dsDNA molecule with complementary UMIs, sequence each strand independently, and call a base only when both strands agree at that position. This yields error rates below 10⁻⁸ per base — sufficient to detect somatic mutations at any allele fraction — and underpins modern mosaicism, mutational-signature, and aging-genome biology.

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
- [[10-Summaries/detecting-ultralow-frequency-mutations-by-duplex-sequencing]] — Kennedy et al. 2014, Nature Protocols. The reference DS method (Loeb lab).

### Newer chemistries with lower input
- [[10-Summaries/a-universal-duplex-sequencing-approach-for-accurate-detection-of-somatic-mutations]] — Nandi/Alexandrov 2025. UDSeq: ~2.5×10⁻⁹/bp from 100 pg.

### Cross-method benchmarking
- [[10-Summaries/benchmarking-of-duplex-sequencing-approaches-to-reveal-somatic-mutation-landscapes]] — Zhang/Coorens 2025. SMaHT benchmark of six methods (CODEC, CompDuplex-seq, HiDEF-seq, NanoSeq, ppmSeq, VISTA-seq).

### Single-cell + duplex validation
- [[10-Summaries/a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis]] — Luquette/Walsh 2025. Uses DS to validate PTA-scDNA-seq mutation calls.

## Synthesized notes

None yet. A natural future note: "Duplex vs scDNA-seq complementarity" — duplex captures population mutation rates and signatures from bulk DNA; scDNA-seq captures clonality and lineage. The methods don't compete; they layer.

## Open questions

- **Single-cell duplex** is not yet practical: DS needs both strands of one molecule, but scWGA loses strand identity. Closing this gap is the field's main open challenge.
- Will the convergence of mutation-rate estimates across methods (shown in the SMaHT benchmark) hold when applied to harder tissues like brain or aging muscle?

## Related

- [[40-Topics/somatic-mosaicism]] · [[40-Topics/scdna-seq]] · [[40-Topics/long-read-sequencing]]
