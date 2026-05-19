---
type: summary
title: "Chen 2017 — Single-cell whole-genome analysis by Linear Amplification via Transposon Insertion (LIANTI)"
source: "[[00-Sources/papers/Single-cell whole-genome analyses by Linear Amplification via Transposon Insertion (LIANTI)]]"
aliases: [Chen 2017, LIANTI 2017, Chongyi 2017]
tags: [scWGA, LIANTI, foundational, scDNA-seq, linear-amplification, micro-CNV]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Chen et al. (2017) — *Single-cell whole-genome analysis by Linear Amplification via Transposon Insertion (LIANTI)* — *Science*. [DOI](https://doi.org/10.1126/science.aak9787)

# Chen et al. 2017 — LIANTI

> Chongyi Chen, Dong Xing, Longzhi Tan, Heng Li, Guangyu Zhou, Lei Huang, **X. Sunney Xie**. *Science* **356**, 189–194 (14 April 2017). DOI: 10.1126/science.aak9787. Harvard + Beijing.

## Thesis

**LIANTI** is a single-cell WGA method that combines **Tn5 transposition** with **T7 in-vitro transcription** for purely linear amplification (no exponential cycles). Achieves **97% genome coverage at 30× depth from a single BJ fibroblast** with **17% allele dropout** — outperforming MALBAC, MDA, DOP-PCR on uniformity (lowest CV across all bin sizes). Enables direct micro-CNV detection at ~10 kb resolution (vs ~1 Mb for prior methods) and reveals stochastic firing of DNA replication origins from cell to cell.

## Mechanism

1. Single cell lysed; gDNA randomly fragmented by Tn5 transposition with a **LIANTI transposon carrying a single-stranded T7 promoter loop**.
2. Gap-filling polymerase extends single-stranded T7 promoter loops into double-stranded T7 promoters at both ends of each fragment.
3. **In vitro transcription** by T7 RNA polymerase linearly amplifies each fragment into thousands of RNA copies.
4. Reverse transcription, RNase digestion, second-strand synthesis → barcoded LIANTI amplicons → library prep + sequencing.
5. **Linear amplification ratio: 1:0.7** vs exponential 8:1 for MALBAC — far closer to perfect uniformity.

## Key claims

- **97% genome coverage, 17% allele dropout**, lowest CV across all bin sizes (1 bp – 100 Mb). Power spectrum and Lorenz curves all favor LIANTI over MALBAC/MDA/DOP-PCR.
- **Micro-CNV detection at ~10 kb resolution** by digital counting of inferred fragment numbers (mapping reads to same start/end coordinates groups them as one original fragment). Detected a 57-kb 2-to-1 micro-CNV in a single BJ cell that bulk sequencing also showed but MALBAC/MDA/DOP-PCR could not resolve.
- **Genome-wide replication-origin firing in 11 single BJ cells synchronized in early S phase**: copy-number gains 2→3 and 3→4 detected at kilobase resolution. Replicon copy numbers correlate well with Repli-Seq (r ~0.5+) and DNase-Seq (r ~0.5+) but **off-diagonal signal between cells reveals stochastic origin firing** — different replicons fire in different cells.
- **C→T false-positive rate 5.4×10⁻⁶** for single-BJ-cell SNV detection — confirmed via UDG treatment that this is from **post-lysis cytosine deamination**, not amplification fidelity. Same artifact in MALBAC. **G→T is the second most frequent false positive**, likely from guanine oxidation to 8-hydroxyguanine.

## Surprising / load-bearing for the review

- **LIANTI is the methodological successor to MALBAC** for §3.1 WGA comparison. The linear-vs-exponential amplification axis is the key dimension to articulate.
- **The C→T-from-deamination artifact characterization is canonical**: every duplex-sequencing or single-cell mutation-calling paper since LIANTI cites this as the dominant false-positive class. For [[a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis|Luquette/Walsh PTA+DS]] and the duplex-sequencing topic page, LIANTI is the upstream reference.
- **Stochastic replication-origin firing** was previously inferred indirectly; LIANTI shows it cell-by-cell.

## Entities / concepts touched

[[scwga]] · [[malbac]] · [[mda]] · [[dop-pcr]] · [[tn5-tagmentation]] · [[allele-dropout]] · [[replication-timing]] · [[40-Topics/whole-genome-amplification]]

## Related summaries

- [[chenghang-2012-science]] — MALBAC, prior generation that LIANTI benchmarks against.
- [[a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis]] — Luquette/Walsh PTA+DS uses LIANTI's deamination characterization.
- [[charles-2016-naturereviewsgenetics]] — review citing this lineage.

---
**Source:** [DOI](https://doi.org/10.1126/science.aak9787) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28408603/)
