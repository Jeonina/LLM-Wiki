---
type: summary
title: "Schmitt 2012 — Detection of ultra-rare mutations by next-generation sequencing (Duplex Sequencing)"
aliases: ["Schmitt 2012", "Duplex Sequencing", "founding duplex method"]
tags: [duplex-sequencing, error-correction, mutation-detection, mosaicism, Loeb-lab, founding-method]
created: 2026-05-13
updated: 2026-05-13
sources: ["Michael_2012_PNAS.pdf"]
---

**Citation:** Schmitt et al. (2012) — *Detection of ultra-rare mutations by next-generation sequencing (Duplex Sequencing)* — *PNAS*. [DOI](https://doi.org/10.1073/pnas.1208715109)

Schmitt, Kennedy, Salk, Fox, Hiatt and Loeb (University of Washington) introduced **Duplex Sequencing**, the founding double-strand consensus method for ultra-rare mutation detection. The method tags both strands of a DNA duplex with a random, yet complementary, 12-nt sequence (Duplex Tag) before PCR amplification. Reads from each strand are grouped by their unique tag into single-strand consensus sequences (SSCS); reciprocal α/β tag pairs are then compared to generate a Duplex Consensus Sequence (DCS). A true mutation must appear at the same position on *both* strands; PCR errors and DNA-damage artefacts appear on only one strand and are filtered out.

Theoretical background error rate < 1 per 10^9 nucleotides — roughly five orders of magnitude better than standard NGS. Validated on M13mp2 DNA and applied to mitochondrial DNA from human cells, where the authors directly measured the frequency and pattern of random mutations.

## Why this matters

Founding methodological reference for all duplex-consensus mosaic-variant detection. Direct ancestor of NanoSeq (Abascal 2021) which extended duplex sequencing to whole-genome scale; conceptual ancestor of SMM-seq, BotSeqS, META-CS. Anchors §3.1's discussion of population-level duplex strategies as a complement to (rather than replacement for) single-cell WGS. The error-budget logic in Duplex Sequencing is foundational to understanding why scWGS variant calling needs different filters (LiRA, SCAN-SNV) — single cells don't get the duplex benefit.

---
**Source:** [DOI](https://doi.org/10.1073/pnas.1208715109) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/22853953/)

---
**Source:** [DOI](https://doi.org/10.1073/pnas.1208715109) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/22853953/)

## Related

- [[10-Summaries/kennedy-2014-natprotoc]]
- [[10-Summaries/abascal-2021-nature]]
- [[30-Concepts/duplex-consensus-sequencing]]
- [[20-Entities/lawrence-loeb]]
