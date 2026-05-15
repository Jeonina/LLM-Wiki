---
type: summary
title: "Kennedy 2014 — Detecting ultralow-frequency mutations by Duplex Sequencing (protocol)"
aliases: ["Kennedy 2014 duplex protocol", "Duplex Sequencing protocol Nat Protoc"]
tags: [Duplex-Sequencing, protocol, ultralow-frequency, single-strand-consensus, duplex-consensus, Loeb-lab]
created: 2026-05-13
updated: 2026-05-13
sources: ["Detecting ultralow-frequency mutations by Duplex Sequencing.md"]
---

**Citation:** Kennedy et al. (2014) — *Detecting ultralow-frequency mutations by Duplex Sequencing (protocol)* — *?*.

Kennedy, Schmitt, Fox et al. (Loeb lab; UW) provided the canonical Nature Protocols paper detailing the Duplex Sequencing (DS) workflow. Achieves <1 mutation in >10⁷ wild-type nucleotides via random-yet-complementary tagged adapters → ligation → PCR family grouping → single-strand consensus sequences (SSCS) → duplex consensus sequences (DCS). Suitable for <1 Mb genomic regions. Establishes the protocol-grade reference for the founding Schmitt 2012 method, including updated adapter design and computational pipeline (BWA → SAMtools → Picard → custom Python scripts).

## Why this matters

The protocol companion to Schmitt 2012 — cite when describing implementation details of duplex sequencing rather than the original concept. Already cited via `kennedy2014` bibkey.

---
**Source:** [Open paper](https://www.nature.com/articles/nprot.2014.170)
## Related

- [[10-Summaries/schmitt-2012-pnas]]
- [[10-Summaries/abascal-2021-nanoseq]]
- [[10-Summaries/bae-2023-codec]]
