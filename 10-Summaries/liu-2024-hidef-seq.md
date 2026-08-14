---
type: summary
title: "Liu et al. 2024 — DNA mismatch and damage patterns revealed by single-molecule sequencing (HiDEF-seq)"
source: "[[00-Sources/papers/DNA mismatch and damage patterns revealed by single-molecule sequencing]]"
source_kind: paper
author: "Mei Hong Liu, Benjamin M. Costa, Emilia C. Bianchini, Una Choi, Rachel C. Bandler, … Uri Tabori, Jonathan E. Shoag, Gilad D. Evrony (corresponding)"
published: 2024-06-12
ingested: 2026-08-13
doi: "10.1038/s41586-024-07532-8"
journal: "Nature 630:752–761"
tags: [HiDEF-seq, single-strand-mismatch, DNA-damage, cytosine-deamination, mutational-signature, POLE, CMMRD, APOBEC3A, PacBio, amplification-free]
entities: ["[[gilad-evrony]]"]
concepts: ["[[hidef-seq]]", "[[mutational-signatures]]", "[[nanoseq]]", "[[pacbio]]", "[[meta-cs]]", "[[post-zygotic-variation]]", "[[compounding-artifact]]"]
topics: ["[[duplex-sequencing]]", "[[somatic-mosaicism]]", "[[long-read-sequencing]]", "[[scdna-seq]]"]
---

**Citation:** Liu et al. (2024) — *DNA mismatch and damage patterns revealed by single-molecule sequencing* — *Nature* 630, 752–761. [DOI](https://doi.org/10.1038/s41586-024-07532-8)

# Liu 2024 — HiDEF-seq

> Every mutation starts as a lesion on **one** strand. Every existing method — single-cell WGS, clonal expansion, microdissection, [[schmitt-2012-pnas|duplex sequencing]] — amplifies before reading, which either converts single-strand events into double-strand ones or manufactures fake ones. HiDEF-seq sequences **unamplified single molecules** on PacBio with enough passes per strand to call substitutions at single-molecule fidelity, and so reads the **precursor** lesions rather than the endpoint mutations. It then derives the first **single-strand mutational signatures** (named with an `ss` suffix) and shows they map onto known double-strand COSMIC signatures — resolving which chemical event initiated which mutation class.

## Key claims

- **Three engineering moves produce the fidelity.** (1) ~32 sequencing passes per strand on median 1.7 kb molecules, building a high-quality consensus per *strand* rather than per molecule; (2) elimination of in vitro artifacts via single-strand nick ligation plus either the [[abascal-2021-nanoseq|NanoSeq]] A-tailing approach or a no-A-tailing protocol for degraded post-mortem DNA; (3) a pipeline analysing only single-base substitutions — orthogonal to PacBio's dominant indel error mode — and analysing each strand separately so double- and single-strand events are distinguishable.
- **Estimated fidelity: <1 error per 3 × 10¹³ bp at ≥5 passes/strand, <1 per 1 × 10¹⁴ bp at ≥20 passes.** For dsDNA analysis the ≥5-pass threshold is used because it raises analysed molecules from 70% to 99.8%. For ssDNA analysis ≥20 passes are required, since duplex error correction is unavailable.
- **NanoSeq's single-strand calls are largely artifact — and HiDEF-seq shows it by direct comparison.** On nine samples profiled by both, dsDNA burdens and patterns agree, but HiDEF-seq measures **18-fold lower ssDNA call burdens** (5-fold lower for C>T only) with distinct patterns. Against [[meta-cs|Meta-CS]] single-cell duplex sequencing in cortical neurons, HiDEF-seq is ~13-fold lower (~4-fold for C>T only). The authors note NanoSeq's own developers suspected this.
- **Sperm is the fidelity stress test.** Sperm has the lowest dsDNA mutation burden of any accessible human cell type; HiDEF-seq's sperm burdens matched both a de novo mutation study and NanoSeq run on the same samples. Liver, kidney, blood, and cortical neurons showed the expected signatures and linear age accumulation.
- **Cancer predisposition syndromes validate the ssDNA calls biologically.** Across 17 samples from 8 syndromes, two showed elevated ssDNA burdens: ***POLE* PPAP at 2.6-fold** (95% CI 2.3–3.0) and **CMMRD at 1.6-fold** (95% CI 1.4–1.9). Purine ssDNA calls rose from ~20% (range 12–29%) in controls to ~61% (52–73%) in PPAP and ~33% (23–57%) in CMMRD.
- **SBS10ss is the first single-strand mismatch signature.** Extracted de novo from PPAP samples, dominated by **AGA>ATA (~15–20%)** and **AAA>ACA (~5–10%)**. Projected onto central-pyrimidine contexts it matches the de novo dsDNA signatures from the same samples at **cosine similarity 0.97**, and COSMIC SBS10c at 0.90. It accounts for 79% (70–91%) of ssDNA calls in PPAP.
- **Strand asymmetry resolves which base the polymerase actually misincorporated.** AGA>ATA versus its reverse complement TCT>TAT runs 73:10 across PPAP samples (χ², P < 0.0001), and AAA>ACA versus TTT>TGT runs 26:2. This is a **direct in vivo observation** that the *POLE* mutational context arises from C:dT rather than G:dA misincorporation — previously inferred only indirectly from replication-timing asymmetries in yeast and tumours, or from in vitro gap-filling assays that lack the replication and repair context.
- **Mismatch repair and proofreading interact, visibly.** Two hypermutating tumours (biallelic germline *PMS2* + somatic *POLE* exonuclease mutations) show ssDNA patterns distinct from proofreading-deficient-only samples — increased AG>AT flanked by 3′ C/G/T, and increased G>A, A>G, T>C — consistent with MMR being differentially efficient across mismatch types. A signature **SBS14ss** was extracted (cosine 0.73 to COSMIC SBS14 overall, 0.96 for C>A only).
- **A cytosine-deamination damage signature, SBS30ss\*,** is defined (the asterisk marks damage rather than mismatch). Damaged cytosines are mis-sequenced as thymines by the sequencer polymerase, which is what makes damage detectable at all. One tumour was excluded from analysis for a very high SBS30ss\* burden judged to have arisen ex vivo.
- **In mitochondria, the findings support a mutagenic mechanism operating primarily during replication.**

## Methods / evidence

134 samples across diverse tissues: sperm, liver, kidney, blood, cortical neurons, primary fibroblasts, LCLs, brain tumours, and post-mortem brain/spinal cord — including 17 samples from 8 cancer predisposition syndromes (NER, MMR, polymerase proofreading, BER defects). Cross-validation against NanoSeq on 9 matched samples. Restriction-enzyme fragmentation captures ~40% of the genome (random fragmentation possible but needs more input). De novo signature extraction with projection onto COSMIC.

Weight: the syndrome comparison is the load-bearing validation — it supplies an *a priori* expectation of elevated ssDNA events that the method meets. The sperm benchmark and the NanoSeq head-to-head are the fidelity evidence. The strand-asymmetry result is the strongest claim because it is a direct measurement replacing a chain of indirect inference.

## Surprising or load-bearing bits

- **The 192-trinucleotide spectrum is the conceptual innovation.** Standard 96-context signatures collapse a mutation onto its pyrimidine representation, discarding strand. Once you can read single strands, the pyrimidine/purine split is real information — and it is what lets you name the misincorporated nucleotide.
- **"Amplification masks the very thing you want to measure"** is the paper's structural argument, and it is the mirror image of the argument the wiki tracks in [[50-Notes/pta-inflection-point]]: there, better amplification bought accuracy; here, *no* amplification is the only route to a whole class of events.
- **HiDEF-seq puts a number on how much of NanoSeq's ssDNA signal is noise** (18×). Any prior single-strand claim from duplex-family methods should be re-read against this.
- **The exclusion of tumour 3 for ex vivo deamination** is a warning about sample handling: cytosine deamination accumulates after collection, so damage signatures are partly a logistics readout.
- **~5 passes suffices for dsDNA, ~20 for ssDNA** — a concrete design parameter: the ssDNA analysis costs roughly 4× the sequencing per molecule and forces shorter fragments (1.7 kb rather than 4.2 kb).
- **PacBio per-pass substitution fidelity is better than previously estimated**, an incidental finding with consequences beyond this assay.
- This is the one method in the corpus that measures the *rate* of DNA damage in vivo rather than the rate of mutation. The distinction — lesion vs fixed mutation — is where DNA repair lives.

## Entities mentioned

- [[gilad-evrony]] — corresponding author; also [[evrony-2021-scDNA-applications-review]].

## Concepts touched

- [[hidef-seq]] — this is the founding source for the concept page.
- [[mutational-signatures]] — extends the framework from 96 to 192 contexts and from mutations to lesions; introduces `ss` and `ss*` nomenclature.
- [[nanoseq]] — HiDEF-seq adopts NanoSeq's A-tailing artifact control while refuting its ssDNA calls.
- [[compounding-artifact]] — the amplification-masks-precursors argument.

## Connections to other sources

- Direct methodological comparison and partial ancestor: [[abascal-2021-nanoseq]].
- Duplex lineage this departs from: [[schmitt-2012-pnas]], [[kennedy-2014-duplex-protocol]], [[bae-2023-codec]].
- Single-cell duplex comparison: [[meta-cs]] concept; and [[luquette-2025-pta-duplex-mosaicism]], [[zhang-2025-smaht-duplex-benchmark]] for the duplex benchmarking context.
- Signature framework: [[alexandrov-2013-mutational-signatures]] (COSMIC dsDNA signatures this maps onto).
- Platform: [[pacbio]]; related long-read single-molecule assays [[andrewb-2020-science]] (Fiber-seq), [[nanda-2024-smrt-tag]].
- Aging and mosaicism context: [[vijg-2020-cell]], [[cagan-2022-nature]], [[lodato-2017-aging-neurons]].

## Open questions

- **True ssDNA burdens remain unknown** — the authors say so explicitly. Without duplex correction there is no way to calibrate absolute ssDNA call rates, only to compare between samples and methods.
- CMMRD samples had too few ssDNA calls to extract a signature; MMR-deficiency-alone single-strand patterns remain undescribed.
- The ~40% genome capture from restriction fragmentation biases which contexts are observable; random fragmentation is possible but was not used at scale here.
- Whether HiDEF-seq can be pushed to **single cells** — it currently needs bulk DNA input — is the obvious frontier, and would close the gap toward [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|per-cell lesion mapping]].

## Related

- [[abascal-2021-nanoseq]] · [[hidef-seq]] · [[mutational-signatures]] · [[40-Topics/duplex-sequencing]] · [[50-Notes/single-cell-duplex-sequencing]]
