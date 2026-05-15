---
type: summary
title: "Luo 2018 — Robust single-cell DNA methylome profiling with snmC-seq2"
aliases: [Luo 2018, snmC-seq2, Chongyuan 2018]
tags: [scbs-seq, dna-methylation, single-cell-methylome, snmC-seq, foundational, brain]
created: 2026-05-12
updated: 2026-05-12
sources: ["00-Sources/papers/Chongyuan_2018_NatureCommunications.pdf"]
---

**Citation:** Luo et al. (2018) — *Robust single-cell DNA methylome profiling with snmC-seq2* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-018-06355-2)

# Luo et al. 2018 — snmC-seq2

> Chongyuan Luo, Angeline Rivkin, Jingtian Zhou, Justin P. Sandoval, Laurie Kurihara, Jacinta Lucero, Rosa Castanon, Joseph R. Nery, António Pinto-Duarte, Brian Bui, Conor Fitzpatrick, Carolyn O'Connor, Seth Ruga, Marc E. Van Eden, David A. Davis, Deborah C. Mash, M. Margarita Behrens, **Joseph R. Ecker**. *Nature Communications* **9**, 3824 (2018). DOI: 10.1038/s41467-018-06355-2. Salk + Swift Biosciences + Zymo.

## Thesis

**snmC-seq2** is an improved single-nucleus methylcytosine sequencing protocol that supersedes the original snmC-seq with **better read mapping, fewer adapter-dimer artifacts, higher throughput, and increased library complexity**. The protocol changes (RP-H random primer, shrimp alkaline phosphatase dephosphorylation, 384-well DNA-binding plates, 8-plex Adaptase reactions) collectively make atlas-scale single-cell methylome profiling tractable. This is the chemistry that produced the BICCN mouse brain atlas that [[10-Summaries/eran-2025-neuron|Mukamel 2025]] then mined for somatic aneuploidy.

## Key changes vs original snmC-seq

1. **RP-H random primer** (5′-NNNNNNNN with H = A,T,C; excludes G) destabilizes primer-primer hybridization → significantly fewer adapter-dimer reads. Library complexity comparable.
2. **Shrimp alkaline phosphatase (SAP) dephosphorylation step** before Adaptase reaction → removes carryover dNTPs → eliminates aberrant base composition in reverse reads. R2 mapping rate improved (P = 2.4×10⁻⁵⁸).
3. **384-well DNA-binding plates** for bisulfite cleanup → 33% greater library complexity than 96-well silica columns (P = 9.2×10⁻¹⁰).
4. **8-plex sample multiplexing** (vs 4-plex in snmC-seq) for 3′-adaptor tagging → higher throughput per Adaptase reaction.

## Key claims

- Validated on human frontal cortex (Brodmann area 10).
- Adapter-dimer + short-insert reads reduced from ~22.6% (snmC-seq) to ~10% (snmC-seq2, P = 9.2×10⁻¹⁰).
- Library complexity and coverage uniformity both improved across cell types and tissue contexts.
- snmC-seq2 is the **default chemistry for single-cell methylome atlas projects** (BICCN, BRAIN Initiative).

## Surprising / load-bearing for the review

- This is **the methodological chassis behind the Liu 2021 mouse brain methylome atlas (598:120) and the Mukamel 2025 aneuploidy paper**. For the review's §3.3 (DNA Methylation Profiling), snmC-seq2 anchors the atlas-scale single-cell methylome lineage alongside scBS-seq, scRRBS, and sciMETv2.
- Connection to the **mosaicism × epigenome synthesis** ([[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]]): snmC-seq2's read distribution is what enables atlas-scale aneuploidy detection in [[eran-2025-neuron]]. snmC-seq2 is therefore an implicit prerequisite for the synthesis claim.

## Entities / concepts touched

[[scbs-seq]] · [[dna-methylation]] · [[bisulfite-sequencing]] · [[single-cell-multiomics]] · [[40-Topics/dna-methylation]]

## Related summaries

- [[hongshan-2013-genomeresearch]] — scRRBS, predecessor single-cell methylation method (Tang lab).
- [[eran-2025-neuron]] — Mukamel 2025: uses snmC-seq2 atlas data for aneuploidy detection.
- [[scnmt-seq-enables-joint-profiling-of-chromatin-accessibility-dna-methylation-and-transcription-in-single-cells]] — adds chromatin + RNA arms.

---
**Source:** [DOI](https://doi.org/10.1038/s41467-018-06355-2) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/30237449/)
