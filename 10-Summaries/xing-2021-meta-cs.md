---
type: summary
title: "Xing et al. 2021 — Accurate SNV detection in single cells by transposon-based whole-genome amplification of complementary strands"
source: "[[00-Sources/papers/Accurate SNV detection in single cells by transposon-based whole-genome amplification of complementary strands]]"
source_quality: full
source_sha256: "cb157aa7c55933949fa43e62ac8a12981f0f59d2c39fab3e832f245ddc2880f7"
source_kind: paper
author: "Dong Xing, Longzhi Tan, Chi-Han Chang, Heng Li (corresponding), X. Sunney Xie (corresponding)"
published: 2021-02-15
ingested: 2026-10-07
doi: "10.1073/pnas.2013106118"
journal: "PNAS 118(8):e2013106118"
tags: [META-CS, scWGA, Tn5, complementary-strands, duplex-consensus, somatic-SNV, neurons, sperm, PBMC, ssDNA-damage, somatic-hypermutation, mutational-signatures]
entities: ["[[20-Entities/heng-li]]"]
concepts: ["[[meta-cs]]", "[[scwga]]", "[[scwga-chemistries]]", "[[tn5-tagmentation]]", "[[mda]]", "[[mutational-signatures]]", "[[replication-timing]]", "[[single-cell-variant-calling]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[whole-genome-amplification]]", "[[duplex-sequencing]]", "[[brain-somatic-mosaicism]]", "[[somatic-mosaicism]]", "[[scdna-seq]]"]
---

**Citation:** Xing et al. (2021) — *Accurate SNV detection in single cells by transposon-based whole-genome amplification of complementary strands* — *PNAS* 118:e2013106118. [DOI](https://doi.org/10.1073/pnas.2013106118)

# Xing 2021 — META-CS

> Single-cell SNV false positives come from polymerase errors and single-strand DNA damage — both of which sit on **one strand only**, while a true SNV sits on both. META-CS (multiplexed end-tagging amplification of complementary strands) exploits this: Tn5 tags each fragment with 2 of 16 transposon sequences, the fragments are melted, and two sequential primer-extension rounds label the forward and reverse strands separately, all in **one tube**. Calling an SNV only when **both strands agree** removes nearly all false positives, lets a variant be called from **as few as four reads**, and turns the discordant single-strand calls into a readout of ssDNA damage.

## Key claims

- **Strand labeling is specific**: on a synthetic ssDNA template, 4 discordant strands in 173,635 reads — a strand conversion rate of 2.3 × 10⁻⁵.
- **Strand filter makes calls threshold-robust.** Raising thresholds from a4s2 to a8s4 cut eHAP SNV counts ~2-fold (95→48); without the strand filter, a4s0→a8s0 cut them ~6.4-fold (11,153→1,754). After detection-efficiency adjustment, strand-filtered counts were nearly constant.
- **Kindred-cell validation (haploid eHAP clone):** day-5 cells had 50.9 ± 12.2% genome coverage and 9.5 ± 5.9 autosomal de novo SNVs per cell (70 ± 25 after correcting for 15.9 ± 6.1% strand-specific detection efficiency); 63 of 95 SNVs were C>A, Ti/Tv 0.27, unlike Q5 polymerase errors (Ti/Tv 0.89) or damage spectra (mainly C>T). Unfiltered (a4s0) calls had Ti/Tv 1.73. Day-13 cells had 231 ± 65 SNVs with an almost identical spectrum (r = 0.995).
- **Sperm validation:** 114 ± 45 germline SNVs per sperm (n = 19) from a donor in his late 50s, close to the ~92 (95% CI 80–105) predicted from family-trio data, with a trio-concordant spectrum (r = 0.93, Ti/Tv 1.46). A prior single-sperm study's Ti/Tv of 5.6 is attributed to WGA false positives.
- **FPR upper bound ~2.4 × 10⁻⁸** (70/2.9 Gb) for day-5 eHAP cells — an upper bound because in vitro de novo mutations are counted as FPs.
- **Neurons accumulate ~16 SNVs per year**: 379 ± 66 (19 y, n = 10), 871 ± 123 (49 y, n = 11), 1,304 ± 202 (76 y, n = 11) per PFC neuron — generally lower than previous studies, which the authors read as unrecognized FPs in other methods. Neuronal SNVs are mainly T>C and C>T, **depleted from late-replicating domains and enriched in transcribed regions**.
- **ssDNA damage readout:** calls with ALT on one strand and REF on the other increased significantly in the 76-year-old brain, mainly as G>T, consistent with guanine oxidation to 8-hydroxyguanine. These calls include WGA artifacts (e.g., 70 °C lysis), assumed constant across samples.
- **PBMCs (53 cells, same donor as sperm):** 1,494 ± 721 SNVs per cell, >10× the germline burden; spectrum mainly C>T, correlated with HSC spectra (r = 0.991), enriched in late-replicating domains — suggesting most PBMC SNVs arose in HSPCs.
- **Cell-type mutational patterns from single cells:** V(D)J recombination identified 15 B and 22 T cells; 4 B cells were SHM+ with higher SNV frequency. Excluding SHM+ B cells, other B cells and PBMCs had fewer SNVs than T cells. NMF gave three signatures: A (HSPC-like, r = 0.976), B (SHM+ B cells), C (T cells, scaling with T-cell SNV load). PCA on trinucleotide spectra separated neurons from blood cells and most T cells from B cells.

## Methods / evidence

Tn5 transposome loaded with an equimolar mix of 16 META transposons (multiple sequences avoid intramolecular hairpins when both ends carry the same tag); lysis, transposition, two strand-tagging extensions with exonuclease I clean-up between, and PCR, all in one tube. Most cells sequenced at **3–8×**, versus the 30–60× the authors say is common for single-cell SNV work. Reads preprocessed with premeta, aligned with **both BWA-MEM and minimap2** (smaller read count used, to suppress mapping FPs), piled up and called with lianti tools (≥4 total reads, ≥2 per strand, ALT allele balance ≥20%, gnomAD ≥1% removed, clustered calls within 100 bp removed). 133 single cells in total. Amplification success ~90% (e.g., 32 of 36 neurons).

Weight: the kindred-cell and sperm controls are a well-designed truth set for the FPR claim, but sensitivity is low — ~16% strand-specific detection efficiency means burdens are extrapolated by large correction factors (synthesis). The neuron data come from three individuals only, so the ~16/year slope rests on three points.

## Surprising or load-bearing bits

- **"Higher accuracy" and "lower cost" come together**: the strand filter is what allows calling from four reads, so accuracy is bought by chemistry rather than depth. This contradicts the general assumption that duplex-style methods cost more per cell (synthesis).
- **Not limited to diploid cells with heterozygous SNPs** — unlike in silico callers that depend on germline hSNP phasing, which the authors note still produce FPs when one strand fails to amplify. Useful for haploid or aneuploid (cancer) cells.
- **Neuron vs blood genomic distribution is opposite** (transcribed-region enrichment vs late-replication enrichment), a mechanistic split visible only with low-FP single-cell calls.
- **Polymerase choice limits the damage readout**: Q5 does not prefer uracil or inosine templates, so some damage classes are invisible; NEB Q5U is suggested.
- The carrier ssDNA and analysis code are shared with LIANTI (lh3/lianti), making META-CS the strand-aware successor in the same Xie/Li tool line (synthesis).

## Entities mentioned

- [[20-Entities/heng-li]] — co-corresponding author; developed the premeta/lianti analysis code used for calling.

## Concepts touched

- [[meta-cs]] — the primary source for the method (mechanism, FPR bound, validation).
- [[scwga]] / [[scwga-chemistries]] — a Tn5-based, strand-aware WGA; contrasts with MDA's C>T deamination artifact.
- [[tn5-tagmentation]] — multiplexed transposon tags as fragment barcodes and priming sites.
- [[mutational-signatures]] — NMF/SigProfiler signatures distinguishing T cells, SHM+ B cells and HSPC-derived cells.
- [[replication-timing]] — opposite late-replication enrichment in neurons vs PBMCs.
- [[sequencing-depth-and-coverage]] — calls from 3–8× per cell.

## Connections to other sources

- Successor chemistry to [[chen-2017-lianti]] (same carrier ssDNA, same lianti code base); META, the WGA it builds on (its ref. 10), is the same amplification used in Dip-C ([[tan-2018-science]], same core authors).
- **Echoes** [[luquette-2022-neuron-scan2-indels]]: PTA+SCAN2 revises the neuronal rate to 16.5 SNVs/year, close to META-CS's ~16/year, and both attribute higher earlier estimates to amplification artifacts; contrasts with MDA-era [[lodato-2017-aging-neurons]].
- **Disputed downstream by** [[liu-2024-hidef-seq]], which measures ssDNA call burdens ~13-fold lower than Meta-CS in cortical neurons — implying META-CS's single-strand "damage" calls are partly artifact.
- HSC comparison data from [[lee-six-2018-hsc-dynamics]].
- Duplex-sequencing context: [[kennedy-2014-duplex-protocol]], [[kriz-2025-duplex-multiome]], [[luquette-2025-pta-duplex-mosaicism]]; reviewed in [[shao-2025-scDNA-mosaicism-review]] and [[lim-2024-single-cell-omics-review]].

## Open questions

- What mutational process produces the T-cell-specific signature C is left open; memory-T-cell turnover is offered as one possibility.
- How SHM raises genome-wide (not just immunoglobulin-locus) mutation rates is stated as unclear.
- The ssDNA-damage calls cannot separate in vivo damage from lysis/WGA damage, and [[liu-2024-hidef-seq]] suggests the single-strand burden is overstated (synthesis).

## Related

- [[meta-cs]] · [[chen-2017-lianti]] · [[40-Topics/duplex-sequencing]] · [[40-Topics/whole-genome-amplification]] · [[40-Topics/brain-somatic-mosaicism]]
