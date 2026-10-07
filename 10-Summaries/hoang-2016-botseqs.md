---
type: summary
title: "Hoang et al. 2016 — Genome-wide quantification of rare somatic mutations in normal human tissues using massively parallel sequencing (BotSeqS)"
source: "[[00-Sources/papers/Genome-wide quantification of rare somatic mutations in normal human tissues using massively parallel sequencing]]"
source_quality: full
source_sha256: "79151cbfd25446a3c2ec2db64d8b73dcb48db6d9e1f0a9943fee96343d16f3e8"
source_kind: paper
author: "Margaret L. Hoang, Isaac Kinde, Cristian Tomasetti, K. Wyatt McMahon, Thomas A. Rosenquist, Arthur P. Grollman, Kenneth W. Kinzler (corresponding), Bert Vogelstein (corresponding), Nickolas Papadopoulos"
published: 2016-08-30
ingested: 2026-10-07
doi: "10.1073/pnas.1607794113"
journal: "PNAS 113(35):9846-9851"
tags: [BotSeqS, bottleneck-sequencing, duplex-consensus, endogenous-barcodes, rare-somatic-mutations, normal-tissue, mtDNA, aging, mismatch-repair, aristolochic-acid, smoking, mutation-spectra]
entities: ["[[lawrence-loeb]]"]
concepts: ["[[nanoseq]]", "[[umi-molecular-barcoding]]", "[[mutational-signatures]]", "[[mitochondrial-heteroplasmy]]", "[[post-zygotic-variation]]", "[[duplicate-marking]]"]
topics: ["[[duplex-sequencing]]", "[[somatic-mosaicism]]", "[[brain-somatic-mosaicism]]"]
---

**Citation:** Hoang et al. (2016) — *Genome-wide quantification of rare somatic mutations in normal human tissues using massively parallel sequencing* — *PNAS* 113:9846–9851. [DOI](https://doi.org/10.1073/pnas.1607794113)

# Hoang 2016 — BotSeqS

> Rare somatic mutations private to single cells are invisible in bulk sequencing (Illumina sensitivity at best ~0.1%) and hard to call in single cells (amplification errors). **Bottleneck sequencing (BotSeqS)** adds one step to a PCR-free library: **dilute the adaptor-ligated library before PCR**, so a random sample of double-stranded molecules is each sequenced many times from both strands. Shear-point coordinates act as endogenous barcodes; a mutation counts only if present in ≥90% of both Watson and Crick families. The result is genome-wide, unbiased, duplex-grade rare-mutation quantification of nuclear and mitochondrial DNA together, applied across age, tissue, DNA-repair deficiency and carcinogen exposure.

## Key claims

- **Specificity and sensitivity.** False-positive rate 2.6 × 10⁻¹² per bp (from strand-discordant germline heterozygous calls); mutations at 6 × 10⁻⁸ per bp detectable with a small fraction of a HiSeq 2500 flow cell, and <10⁻⁹ estimated with a full flow cell. Without the both-strand requirement, nuclear prevalence was ~10-fold higher, driven by G→T artifacts.
- **Scale.** 44 libraries from normal tissues of 34 individuals; median 70 million clusters per library; median 45% of molecules had both strands represented; median 60,640 nuclear molecules per library ≈ 0.4% of the nuclear genome; 666 mtDNA and 876 nuclear rare mutations in total. Median 92% of variants were germline (removed using matched WGS; Sanger for two individuals). A two-ratio spike-in gave a 7.4-fold difference vs an intended 10-fold.
- **mtDNA vs nuclear.** In 25 controls: mtDNA 1.4 ± 1.3 × 10⁻⁵ vs nuclear 5.2 ± 3.5 × 10⁻⁷ mutations per bp; mtDNA ~25-fold higher on average (median ratio 26). mtDNA mutations were transition-dominated (89–97%) with heavy strand bias; transition:transversion ~15 in mtDNA vs ~1.1 nuclear.
- **Repair deficiency and mutagens raise nuclear (not mitochondrial) load.** *PMS2*⁻/⁻ colon: 6.6 ± 3.5 × 10⁻⁵ vs 5.1 ± 1.7 × 10⁻⁷ in age-matched controls (~130-fold) with altered spectrum. Kidney cortex of heavy smokers and aristolochic-acid-exposed individuals: 27- and 36-fold higher nuclear prevalence with altered spectra, but mtDNA prevalence and spectra unchanged; mito:nuclear ratio fell to a median 1.3 in exposed kidneys.
- **Age accumulation is tissue-specific.** Over the lifespan: colon +30-fold (mtDNA) and 6.1-fold (nuclear) over 91 years; kidney 19-fold and 6.5-fold over 64 years; brain frontal cortex 7.3-fold and 5.7-fold over 90 years. Colon exceeded brain in nuclear prevalence in young adults (5.5 vs 2.2 × 10⁻⁷) and old adults (1.1 × 10⁻⁶ vs 6.3 × 10⁻⁷), but not in children.
- **Normal-tissue spectra resemble their cancers.** Spectra differed between tissues even without known exposure (kidney vs colon significant in both genomes), and normal kidney and colon spectra were very similar to clear-cell renal and colorectal carcinoma spectra (PCA).

## Methods / evidence

PCR-free TruSeq libraries (34 ng–1 µg input; e.g. 10⁵-fold dilution for 500 ng), dilution titrated on MiSeq, HiSeq 2500 2×100 bp; families defined by fragment end coordinates; filters for well-mapped positions and clonal variants (present on both strands of >1 molecule). Validation is by internal consistency: technical/biological replicates (~2-fold range), expected age trends, repair-deficient and exposed positives, spectra consistent with matching cancers, spike-in.

Weight: elegant and specific, but coverage is tiny (~0.4% of the genome per library, hundreds of mutations total), and the authors concede artifacts cannot be formally excluded because each mutation is in one cell's DNA that no longer exists. Tissue cohorts are small (e.g. 3 per age group in brain).

## Surprising or load-bearing bits

- **Post-mitotic brain still accumulates nuclear mutations** (5.7-fold over 90 years). Because BotSeqS needs both strands mutated, damage-only explanations require repair to have fixed the lesion; the authors list dividing minority cells, replication-independent damage plus repair, or artifact. Single-neuron work later measured ~16–17 sSNVs/year per neuron ([[luquette-2022-neuron-scan2-indels]]), and LiRA's MDA-based rates were "generally consistent" with BotSeqS frontal-cortex numbers ([[bohrson-2019-lira]]).
- **Mutagens hit nuclear DNA but not mtDNA** — at odds with the textbook expectation that poorly repaired mtDNA should be most vulnerable; the authors offer masking by high baseline mtDNA mutation or organelle-specific damage chemistry.
- **"Cancer signatures" may be tissue signatures**: rare mutations in normal tissue already carry the spectrum of the cancers arising there. (The paper's interpretation.)
- The trick is pure library arithmetic: dilution, not new chemistry, buys duplex redundancy genome-wide. NanoSeq later adapted bottleneck dilution with additional chemistry to remove residual errors ([[abascal-2021-nanoseq]]). (synthesis — this clipping does not mention NanoSeq)

## Concepts touched

- [[nanoseq]] — BotSeqS is the bottleneck-dilution precursor to genome-wide duplex methods. (synthesis)
- [[umi-molecular-barcoding]] — endogenous (shear-point) barcodes instead of synthetic UMIs.
- [[mutational-signatures]] — tissue-specific normal spectra resembling cancer; AA signature (A:T→T:A) in nuclear, not mtDNA.
- [[mitochondrial-heteroplasmy]] — rare mtDNA point-mutation prevalence ~25× nuclear and transition-dominated.
- [[post-zygotic-variation]] — somatic burden across age and tissues.

## Connections to other sources

- Duplex-consensus lineage: [[kennedy-2014-duplex-protocol]] (Loeb lab duplex sequencing; the paper cites Loeb and coworkers as the only comparably sensitive method, but for predefined regions), [[abascal-2021-nanoseq]], [[bae-2023-codec]], [[zhang-2025-smaht-duplex-benchmark]], [[liu-2024-hidef-seq]].
- Used as orthogonal reference rate by [[bohrson-2019-lira]].
- Single-neuron mutation burden from single-cell WGS: [[lodato-2015-science]], [[lodato-2017-aging-neurons]], [[luquette-2022-neuron-scan2-indels]].
- Single-cell duplex context: [[50-Notes/single-cell-duplex-sequencing]]; review mention: [[hilal-2026-cardiac-somatic-review]].

## Open questions

- What drives nuclear mutation accumulation in largely post-mitotic cortex, and how much is in neurons vs dividing glia or immune cells?
- Why do aristolochic acid and smoking leave no mtDNA mark?
- With ~0.4% genome coverage per library, regional (gene, enhancer) analyses are out of reach — a gap later genome-wide duplex and single-cell methods address. (synthesis)

## Related

- [[40-Topics/duplex-sequencing]] · [[nanoseq]] · [[abascal-2021-nanoseq]] · [[bohrson-2019-lira]]
