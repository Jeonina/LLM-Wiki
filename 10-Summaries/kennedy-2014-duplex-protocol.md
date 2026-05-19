---
type: summary
title: "Kennedy et al. 2014 — Duplex Sequencing: detecting ultralow-frequency mutations"
source: "[[00-Sources/papers/Detecting ultralow-frequency mutations by Duplex Sequencing]]"
source_kind: paper
author: "Scott R. Kennedy, Michael W. Schmitt, Edward J. Fox, Brendan F. Kohrn, Jesse J. Salk, Eun Hyun Ahn, Marc J. Prindle, Kawai J. Kuong, Jiang-Cheng Shen, Rosa-Ana Risques, Lawrence A. Loeb (corresponding)"
published: 2014-10-09
ingested: 2026-05-12
doi: "10.1038/nprot.2014.170"
journal: "Nature Protocols"
tags: [duplex-sequencing, protocol, low-frequency-mutations, Loeb-lab, NGS-error-correction]
entities:
  - "[[20-Entities/lawrence-loeb]]"
  - "[[20-Entities/scott-kennedy]]"
concepts:
  - "[[30-Concepts/duplex-sequencing]]"
  - "[[30-Concepts/umi-molecular-barcoding]]"
  - "[[30-Concepts/somatic-mosaicism]]"
topics:
  - "[[40-Topics/duplex-sequencing]]"
  - "[[40-Topics/somatic-mosaicism]]"
---

**Citation:** Kennedy et al. (2014) — *Duplex Sequencing: detecting ultralow-frequency mutations* — *Nature Protocols*. [DOI](https://doi.org/10.1038/nprot.2014.170)

# Kennedy et al. 2014 — Duplex Sequencing: detecting ultralow-frequency mutations

> Thesis: Standard NGS has an inherent error rate of ~1 per 100–1,000 bases that blinds it to subclonal mutations below ~1% VAF. Duplex Sequencing (DS) tags both strands of every input dsDNA molecule with a random-yet-complementary 12 nt UMI, sequences PCR-amplified families of each strand into Single-Strand Consensus Sequences (SSCS), then **only calls a mutation when it is present in both strands** as a Duplex Consensus Sequence (DCS). This drives error rates below 5×10⁻⁸ per base — a >10,000-fold improvement.

## Key claims

- DS adapter design: ligate adapters carrying random 12-nt single-stranded tags to dsDNA; PCR-amplify both labeled strands; group reads into tag families; compare the two complementary SSCS to form a DCS. Damage- and polymerase-error events appear in only one strand and are dropped.
- Demonstrated mutation frequency of 2.5×10⁻⁶ in M13 bacteriophage and as low as 5×10⁻⁸ in human nuclear DNA. mtDNA mutation frequency in brain tissue is 10–100× lower than previously reported using single-strand methods — contradicting the free-radical aging hypothesis and arguing prior measurements were PCR artifacts.
- DS rescues damaged/FFPE DNA: only ~2× change in mutation frequency between fixed and unfixed paired samples, because complementary damage artifacts are vanishingly rare on opposing strands.
- Cost is the limitation: ~40 raw reads needed per single DCS, so DS is best for targeted regions <1 Mb (mtDNA, viral genomes, gene panels) or requires deep sequencing budgets. Targeted capture works (SureSelectXT), but PCR-based enrichment is incompatible because melting destroys strand complementarity.

## Methods / evidence

Step-by-step Nature Protocols paper. Library prep follows standard Illumina (sonication, end repair, dA-tailing, ligation, optional capture, PCR) with two critical modifications: bead-only size selection (no gel melting) and 20× molar excess of degenerate-tag adapters. Computational pipeline: BWA + custom Python (`tag_to_header.py`, `ConsensusMaker.py`, `DuplexMaker.py`) to build SSCS then DCS. Peak family size of 6 is optimal.

## Surprising or load-bearing bits

- The reframing of mtDNA mutation biology by removing strand-asymmetric artifacts is the load-bearing scientific result. The paper has been cited as evidence that "oxidative-damage mutations increase with age" was an artifact of single-strand methods that scored damage-induced lesions as mutations.
- Tagmentation is **incompatible** with DS because it uses an invariant transposon sequence, so neither molecule barcoding nor strand discrimination is possible. This is the structural reason later duplex methods (CODEC, NanoSeq, ppmSeq, HiDEF-seq) had to invent new ways to mark strands.

## Connections to other sources

- Direct ancestor of the methods compared in [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] (SMaHT benchmark) and the UDSeq protocol in [[10-Summaries/nandi-2025-udseq]].
- The framing of duplex methods as "the answer to scWGA's single-strand dropout problem" is sharpened by [[10-Summaries/diane-2025-naturereviewsgenetics]] (~70k ssDNA lesions per cell per day argue for duplex protection).
- Sets the stage for population-scale somatic-mosaicism measurement: [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] uses DS to validate PTA-based scDNA-seq mutation calls.

## Open questions

- DS is single-cell-incompatible (needs both strands of one molecule, scWGA loses them). The cost of moving to duplex chemistry at single-cell scale remains the dominant open problem.

---
**Source:** [DOI](https://doi.org/10.1038/nprot.2014.170)
## Related

- [[30-Concepts/duplex-sequencing]] · [[30-Concepts/umi-molecular-barcoding]] · [[40-Topics/duplex-sequencing]] · [[40-Topics/somatic-mosaicism]]
