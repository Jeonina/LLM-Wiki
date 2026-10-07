---
type: summary
title: "Schmitt 2012 — Detection of ultra-rare mutations by next-generation sequencing (Duplex Sequencing)"
source: "[[00-Sources/papers/Detection of ultra-rare mutations by next-generation sequencing .pdf]]"
source_quality: full
source_sha256: "ed23135fee756e43bada63d6724b1bb5828f146311960c54fec7b1d3588eee9b"
source_kind: paper
author: "Michael W. Schmitt, Scott R. Kennedy, Jesse J. Salk, Edward J. Fox, Joseph B. Hiatt, Lawrence A. Loeb (corresponding)"
published: 2012-09-04
ingested: 2026-05-13
updated: 2026-10-07
doi: "10.1073/pnas.1208715109"
journal: "PNAS 109(36):14508–14513"
aliases: ["Schmitt 2012", "Duplex Sequencing", "founding duplex method"]
tags: [duplex-sequencing, error-correction, mutation-detection, mosaicism, Loeb-lab, founding-method, SSCS, DCS, DNA-damage, 8-oxo-G, mtDNA, M13mp2]
entities: ["[[20-Entities/lawrence-loeb]]", "[[20-Entities/scott-kennedy]]"]
concepts: ["[[30-Concepts/umi-molecular-barcoding]]", "[[30-Concepts/mitochondrial-heteroplasmy]]"]
topics: ["[[40-Topics/duplex-sequencing]]", "[[40-Topics/somatic-mosaicism]]"]
---

**Citation:** Schmitt et al. (2012) — *Detection of ultra-rare mutations by next-generation sequencing* — *PNAS* 109(36):14508–14513. [DOI](https://doi.org/10.1073/pnas.1208715109) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/22853953/)

# Schmitt 2012 — Duplex Sequencing

> Standard Illumina reads come from single strands, so an error made in the **first PCR cycle**, often by copying across a damaged base, is copied into every duplicate and survives any single-strand consensus. **Duplex Sequencing** ligates adapters carrying a random but **complementary double-stranded tag**, so the two strands of each original molecule produce two related read families (αβ and βα). Reads sharing a tag collapse into a **single-strand consensus sequence (SSCS)**; the two SSCSs of a duplex are then compared, and a base is kept only if both strands agree, giving a **duplex consensus sequence (DCS)**. On M13mp2 DNA the DCS mutation frequency (2.5 × 10⁻⁶) matches the value from genetic assays, while SSCS is still ~10-fold too high and dominated by damage signatures. The paper also turns that failure into a tool: single-strand-only mutations mark **DNA damage**. Applied to human brain mtDNA, DCS gives 3.5 × 10⁻⁵ and a transition-dominated spectrum with a D-loop hotspot.

## Key claims

- **Tag design.** One adapter strand carries 12 random nucleotides, which a polymerase copies to make a double-stranded "Duplex Tag"; adapters are then A-tailed, and sheared DNA is T-tailed. Each fragment gets a tag at each end (α and β), giving a 24-nt combined tag. Reads of the form αβ in read 1 pair with βα in read 2 from the partner strand. A 24-nt tag gives "up to 4²⁴ = 2.8 × 10¹⁴ distinct tag sequences".
- **Consensus rules.** An SSCS needs a family of "at least three duplicates" with the same base in "at least 90% of the members" at a position. In a DCS, a base is kept "only if the read data from each of the two strands matches perfectly".
- **M13mp2 error ladder.** Against a reference mutation frequency of 3.0 × 10⁻⁶ from LacZ genetic assays: standard Q30 analysis gives **3.8 × 10⁻³** (">99.9% of the apparent mutations … are erroneous"), SSCS gives **3.4 × 10⁻⁵** ("∼99% of sequencing errors are corrected" but "∼90% … are still artifacts"), and DCS gives **2.5 × 10⁻⁶**, "nearly identical" to the reference.
- **SSCS errors are DNA damage.** SSCS shows an excess of G→A/C→T and G→T/C→A changes (P < 10⁻⁶). Split by strand, SSCS has "a 15-fold excess of G→T mutations relative to C→A" and "an 11-fold excess of C→T … relative to G→A". The authors attribute G→T to **8-oxo-G** (polymerases insert A opposite it) and C→T to **cytosine deamination to uracil**. Adding H₂O₂ + Fe before library prep raised SSCS G→T further but "had no effect on the overall frequency or spectrum of DCS mutations".
- **DCS reads lower than the gold standard for damage-type changes.** DCS gives *fewer* G→T/C→A and C→T/G→A mutations than the LacZ reference (P < 0.01). The authors suggest the LacZ assay itself scores damage, because *E. coli* replication of a single M13 molecule can fix a single-strand lesion into a double-strand mutation.
- **Spike-in recovery.** In M13mp2 point-mutant mixtures, standard analysis could not identify variants below ~1/100. DCS at "∼20,000-fold final depth" recovered mutants "down to the lowest tested level of one mutant molecule per 10,000 wild-type molecules".
- **Human mtDNA (brain tissue).** Q30 gives 2.7 × 10⁻³, SSCS 1.5 × 10⁻⁴ and DCS **3.5 × 10⁻⁵**. The DCS value agrees with single-molecule PCR in colonic mucosa (5.9 ± 3.2 × 10⁻⁵) and with pedigree divergence estimates (3–5 × 10⁻⁵). SSCS showed "a 130-fold excess of G→T relative to C→A". DCS removed this bias and showed that transitions predominate, with "striking hypermutability" of the **D-loop** replication-origin region. The excess of A→G/T→C and G→A/C→T transitions matches earlier reports of heteroplasmy in human brain.
- **Theoretical error floor.** A DCS error needs complementary errors at the same position on both strands, so error ≈ P(strand 1) × P(strand 2) × 1/3 = (3.4 × 10⁻⁵)² × 1/3 = **3.8 × 10⁻¹⁰**, "a 10 million-fold improvement" over standard analysis. The authors expect the real floor to be lower, because damage-driven reciprocal mispairs are not equally likely.
- **Further uses.** The same tags allow single-molecule counting. Shear points alone could serve as a tag-free duplex check for specific mutations, but not at great depth. The method should carry over to "essentially any sequencing platform".

## Methods / evidence

Two oligonucleotides with non-complementary Y-shaped tails form the adapter; the randomized 12-mer is filled in by polymerase, then A-tailed. DNA is sheared, end-repaired, T-tailed, ligated, amplified for **18–20 PCR cycles**, and sequenced paired-end on an Illumina HiSeq 2000. Analysis: keep reads with a correctly placed tag; join the two 12-nt tags into one 24-nt tag; group into SSCS; pair complementary SSCSs into DCS. Substrates: M13mp2 phage DNA (untreated, oxidatively damaged with H₂O₂/FeSO₄, and a known-ratio spike-in mixture) and mtDNA from human brain tissue. Comparisons use two-sample t-tests. Read and base counts per stage are in Table S1, which is not in the source PDF.

Weight: a short founding methods paper. Accuracy is validated against one well-characterised substrate (M13mp2) and one human tissue sample, and the main human result (mtDNA frequency) is benchmarked only against literature values from other tissues and methods. The headline "<10⁻⁹" is a **calculated** floor, not a measurement: no experiment here sequences enough duplex bases to observe an error rate that low. The damage analysis (strand-split SSCS spectra plus the H₂O₂ experiment) is the most rigorous part. (synthesis)

## Limitations

**Authors' own:**
- The 3.8 × 10⁻¹⁰ floor assumes all mutational events are equally likely (the 1/3 factor). The authors say the real background should be lower, but it is not measured.
- Lesions or recurrent first-round PCR errors at the same position on both strands, giving complementary errors, would still pass DCS.
- Tag-free duplex calling from shear points is "limited by the finite number of possible shear points" and "will not be scalable" to great depth.
- The 24-nt tag uses up sequencing capacity; the authors suggest combining shear points with a shorter tag.

**Reviewer notes:**
- Efficiency is not reported in the main text. Each duplex needs ≥3 reads per strand family plus a recovered partner family, so most reads are spent on redundancy. Later work (UDSeq's Table 1) lists the original method as needing "~1 µg" and being limited to targeted panels ([[10-Summaries/nandi-2025-udseq]]). (synthesis)
- The human application is one mtDNA sample from brain tissue, with no replicate tissues or donors. The D-loop hotspot and spectrum are therefore illustrative, not population estimates. (synthesis)
- End repair and other library steps that fill in or copy both strands could, in principle, create complementary errors that DCS accepts. The paper does not test this; NanoSeq later addressed end-repair artefacts ([[10-Summaries/abascal-2021-nanoseq]]). (synthesis)

## Surprising or load-bearing bits

- **The gold standard was partly wrong.** DCS is *below* the LacZ reference for exactly the damage-type substitutions. The authors argue that the biological assay, not sequencing, overcounted, because *E. coli* replication fixes single-strand lesions.
- **Errors as signal.** SSCS-only G→T in excess of C→A is offered as a readout of **oxidative damage** in a sample. Single-strand damage later became its own measurement target in HiDEF-seq ([[10-Summaries/liu-2024-hidef-seq]]).
- **First-round PCR errors, not sequencing errors, set the floor for single-strand UMI methods.** The paper argues that Kinde et al.'s single-strand tag method (~20-fold gain) is "conceptually analogous" to SSCS and so equally exposed to damage-driven first-cycle errors.
- **mtDNA damage dominates single-strand artefacts:** the SSCS G→T excess is 130-fold in mtDNA against 15-fold in M13. This fits the expected oxidative load in mitochondria.

## Entities mentioned

- [[20-Entities/lawrence-loeb]] — corresponding author; Loeb lab, University of Washington.
- [[20-Entities/scott-kennedy]] — second author; later first author of the 2014 *Nature Protocols* version ([[10-Summaries/kennedy-2014-duplex-protocol]]).

## Concepts touched

- [[30-Concepts/umi-molecular-barcoding]] — complementary double-stranded UMIs that link the two strands of one molecule; also usable for absolute molecule counting.
- [[30-Concepts/mitochondrial-heteroplasmy]] — DCS frequency of 3.5 × 10⁻⁵ in brain mtDNA, transition-dominated, D-loop hotspot.
- [[40-Topics/duplex-sequencing]] — founding method: SSCS → DCS logic and the product-of-strand-errors floor.

## Connections to other sources

- Protocol version with practical guidance: [[10-Summaries/kennedy-2014-duplex-protocol]].
- Genome-scale successors: [[10-Summaries/hoang-2016-botseqs]] (bottleneck dilution, end-coordinate families), [[10-Summaries/abascal-2021-nanoseq]] (restriction fragmentation to remove end-repair errors), [[10-Summaries/bae-2023-codec]] (quadruplex adapters that physically join both strands), [[10-Summaries/maslov-2022-smm-seq]], and [[10-Summaries/nandi-2025-udseq]] (random fragmentation from 100 pg). UDSeq's comparison table calls this method "DupSeq" and puts its error rate at 2 × 10⁻⁷ per bp, far above the theoretical floor here ([[10-Summaries/nandi-2025-udseq]]).
- Single-strand damage as a measured quantity: [[10-Summaries/liu-2024-hidef-seq]].
- Used to validate single-cell calls: [[10-Summaries/wang-2014-nuc-seq]] used Duplex Sequencing to confirm rare single-cell mutations.
- Methods comparison: [[10-Summaries/zhang-2025-smaht-duplex-benchmark]].
- The single-cell incompatibility (duplex needs the original two strands; whole-genome amplification destroys them) is discussed in [[50-Notes/single-cell-duplex-sequencing]]. (synthesis)

## Open questions

- What is the *measured*, rather than calculated, DCS error rate of this original chemistry? Later estimates are much higher than 3.8 × 10⁻¹⁰ ([[10-Summaries/nandi-2025-udseq]]). Whether the gap comes from end repair, low efficiency, or how error was estimated is not resolved here. (synthesis)
- How much of the DCS mtDNA frequency of 3.5 × 10⁻⁵ is real in vivo mutation, and how much is double-strand damage or repair-fixed lesions? The paper cannot separate these. (synthesis)

## Related

- [[40-Topics/duplex-sequencing]] · [[kennedy-2014-duplex-protocol]] · [[abascal-2021-nanoseq]] · [[nandi-2025-udseq]] · [[20-Entities/lawrence-loeb]] · [[50-Notes/single-cell-duplex-sequencing]]
