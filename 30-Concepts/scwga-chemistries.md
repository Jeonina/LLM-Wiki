---
type: concept
title: scWGA chemistries
aliases: [single-cell whole-genome amplification, scWGA chemistry, WGA methods]
tags: [scWGA, MDA, MALBAC, PTA, DOP-PCR, LIANTI, amplification]
created: 2026-05-19
updated: 2026-05-19
---

# scWGA chemistries

> The family of chemistries used to amplify femtogram quantities of single-cell DNA into nanogram-scale sequencing input. Different chemistries trade off coverage uniformity, allelic dropout, and error rate.

## The major chemistries

- **DOP-PCR** — first generation; degenerate oligonucleotide-primed PCR; high amplification bias ([[10-Summaries/gawad-2016-scgenome-review]]).
- **MDA (Multiple Displacement Amplification)** — phi29 polymerase + random hexamers; long products (>10 kb); first practical scWGA chemistry ([[10-Summaries/dean-2002-mda]]).
- **MALBAC** — quasi-linear preamplification + PCR exponential phase; lower bias than MDA, higher error rate ([[10-Summaries/gawad-2016-scgenome-review]]).
- **PicoPLEX / NEB-WGA** — proprietary hybrid chemistries.
- **LIANTI (Linear Amplification via Transposon Insertion)** — Tn5-based linear amplification; lower error rate ([[10-Summaries/chen-2017-lianti]]).
- **PTA (Primary Template-Directed Amplification)** — phi29 + exonuclease-resistant terminator nucleotides; most uniform coverage to date ([[10-Summaries/gonzalez-pena-2021-pnas]]).
- **META-CS / Tn5-duplex** — single-cell-compatible duplex sequencing variant ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Tradeoff space

Coverage uniformity ↑, allelic dropout ↓, error rate ↓ — but no chemistry wins on all three ([[10-Summaries/gawad-2016-scgenome-review]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Related

- [[30-Concepts/scwga]] · [[30-Concepts/pta]] · [[30-Concepts/duplex-sequencing]]
- [[40-Topics/whole-genome-amplification]] · [[40-Topics/scdna-seq]]
