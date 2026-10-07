---
type: summary
title: "Maslov et al. 2022 — Single-molecule, quantitative detection of low-abundance somatic mutations by high-throughput sequencing"
source: "[[00-Sources/papers/Single-molecule, quantitative detection of low-abundance somatic mutations by high-throughput sequencing]]"
source_quality: full
source_sha256: "a47da4f84c694c911f3dd96fe4dc28e4c6e85747761c3203861d2dec324cfcb2"
source_kind: paper
author: "Alexander Y. Maslov, Sergey Makhortov, Shixiang Sun, Johanna Heid, Xiao Dong, Moonsook Lee, Jan Vijg (corresponding)"
published: 2022-04-08
ingested: 2026-10-07
doi: "10.1126/sciadv.abm3259"
journal: "Science Advances 8(14):eabm3259"
tags: [SMM-seq, duplex-sequencing, rolling-circle-amplification, pulse-RCA, UMI, somatic-SNV, bulk-DNA, aging, liver, ENU, mutational-signatures, SBS5, Vijg-lab]
entities: []
concepts: ["[[umi-molecular-barcoding]]", "[[mutational-signatures]]", "[[nanoseq]]", "[[post-zygotic-variation]]", "[[single-cell-variant-calling]]"]
topics: ["[[duplex-sequencing]]", "[[somatic-mosaicism]]", "[[mosaic-variant-calling]]"]
---

**Citation:** Maslov et al. (2022) — *Single-molecule, quantitative detection of low-abundance somatic mutations by high-throughput sequencing* — *Science Advances* 8:eabm3259. [DOI](https://doi.org/10.1126/sciadv.abm3259)

# Maslov 2022 — SMM-seq

> Somatic mutations in normal tissue are mostly unique to one cell, so in bulk DNA they are indistinguishable from sequencing errors. Duplex sequencing fixes that by requiring both strands to agree, but its error suppression is bounded by the **square** of the per-strand error probability. SMM-seq (single-molecule mutation sequencing) replaces "two strands" with "many independent copies of each strand": a hairpin adapter turns each fragment into a dumbbell, **linear rolling-circle amplification (pulse-RCA)** writes out many concatemerized, non-propagating copies of both strands, and only then is PCR used. Errors in any single RCA copy stay unique to that copy, so the theoretical error rate becomes P(E)^N rather than P(E)². The method recovers ENU-induced mutations in fibroblasts and reproduces, in bulk liver DNA, the age-related mutation increase the same lab had measured by single-cell sequencing.

## Key claims

- **Two-step library**: hairpin-like adapters (6-nt UMI in the stem, uracil in the loop) are ligated to both ends of AluI/MluCI-digested, end-repaired fragments, making a dumbbell; pulse-RCA with a thermostable strand-displacing polymerase then produces single-stranded concatemers of equally represented copies of both strands, separated by spacers that serve as PCR priming sites. The library is therefore **PCR duplicates of multiple independent RCA copies** of each original fragment.
- **Family-size cutoff set empirically at 7 reads per strand.** Raising the minimum strand-family size from 2 to 7 caused a statistically significant drop in apparent mutation frequency at each step — a >2-fold decrease (54% change) — with further increases giving no significant decline (<10% change). The excess was treated as artefact.
- **Both strands are still required.** Despite "virtually unlimited" per-strand base-calling accuracy, DNA-damage artefacts are expected on one strand only, so representatives of both strands are needed to reject them.
- **Induced mutations detected at sublethal mutagen doses.** In IMR90 fibroblasts 72 h after ENU, frequency rose from 0.21 ± 0.02 to 0.36 ± 0.04 SNV/Mbp at 25 μg/ml (*P* = 0.005) and to 0.54 ± 0.03 SNV/Mbp at 50 μg/ml (*P* = 9.7 × 10⁻⁵); ENU-specific T:A>A:T and T:A>C:G classes were >2× more represented than in controls. ~200 million positions per sample (~7% of the genome) qualified for calling.
- **Aging signal in liver matches the single-cell gold standard.** Re-analysing hepatocyte DNA from three young (5 months, 16 months, 18 years) and three aged donors (56, 61, 77 years) previously studied by the lab's single-cell approach, SMM-seq gave 0.34 ± 0.09 versus 0.96 ± 0.16 SNV/Mbp (*P* = 0.003), with ~770 million qualifying positions per sample (~26% of the genome). T:A>C:G rose from 16.2% to 29.1%.
- **De novo signatures**: NMF extracted S1 (increased in the aged group, *P* = 0.0134; cosine similarity 0.904 to SBS5, permutation *P* < 0.001) and S2 (dominant in the young; C:G>T:A and T:A>A:T rich; no substantial similarity to any COSMIC signature, origin unclear).
- The authors position SMM-seq as **less resource-demanding than single-cell sequencing and more accurate than Duplex-Seq-based approaches** (Duplex-Seq, BotSeqS, NanoSeq), and pair it with their Structural Variant Search (SVS) assay for comprehensive genome-integrity assessment.

## Methods / evidence

Calling filters: proper pairs, MAPQ ≥ 60, no secondary alignments; a position qualifies if covered by a UMI family with ≥7 reads from each strand **and** ≥20× in a parallel conventional library from the same DNA; all reads in the family must agree on a non-reference base; candidates are removed if in the sample's GATK HaplotypeCaller germline SNP list or dbSNP, or if the variant appears in any read of a different UMI family or in the conventional data. Frequency = variants / qualified positions. Input is diluted to ~8 amol (5 million molecules) per reaction, sized for 30 Gb of 150PE NovaSeq data per sample. Three biological replicates per condition; two-tailed *t* tests in Excel. Code on GitHub (msd-ru/SMM) and Zenodo.

Weight: a short methods paper. Validation is by **concordance with expected biology** (mutagen dose-response, ENU spectrum, age trend, SBS5) rather than by an orthogonal ground truth; no absolute error rate is measured, and there is no head-to-head run against NanoSeq or Duplex-Seq on the same DNA — the "more accurate than Duplex-Seq" claim rests on the P(E)^N argument. Two authors hold a pending patent and four are cofounders of SingulOmics Corp. (stated competing interests). n = 3 per age group.

## Surprising or load-bearing bits

- **The plateau at family size 7 is interpreted, not proven.** The authors read it as the point at which each strand family contains descendants of more than one RCA copy; copies of the same strand cannot be distinguished in the data, so N in P(E)^N is never observed directly. (synthesis)
- **Callable fraction is sample-dependent**: ~7% of the genome in IMR90 versus ~26% in liver. Restriction-enzyme fragmentation plus the ≥7-per-strand family requirement define what is sampled, which echoes NanoSeq's restriction-digest design. (synthesis)
- **Germline subtraction needs a conventional library from the same DNA** at ≥20× — SMM-seq is not a stand-alone assay. Conveniently, the uracil loop lets the same ligated product be USER-cleaved into an ordinary library.
- The young-liver signature S2 has no COSMIC match and its source is stated to be unclear; the paper says the signature results overall are "in good agreement with our previous findings" from the single-cell study, without specifying whether S2 itself was seen there.

## Concepts touched

- [[umi-molecular-barcoding]] — UMIs embedded in a hairpin stem define both the fragment family and the two strand sub-families.
- [[mutational-signatures]] — de novo NMF on bulk-derived somatic SNVs; aging-associated S1 ≈ SBS5.
- [[nanoseq]] — the strand-family-size-2 normalization baseline is taken from NanoSeq; SMM-seq is framed as surpassing its P(E)² bound.
- [[post-zygotic-variation]] — targets the private, non-clonal SNVs that clonal-expansion-based studies miss.

## Connections to other sources

- Duplex lineage it claims to improve on: [[schmitt-2012-pnas]], [[kennedy-2014-duplex-protocol]], [[abascal-2021-nanoseq]]; other single-molecule error-suppression routes: [[bae-2023-codec]] (quadruplex adaptor), [[liu-2024-hidef-seq]] (PacBio duplex), [[nandi-2025-udseq]].
- Catalogued as the "circularized, Illumina" duplex variant in [[shao-2025-scDNA-mosaicism-review]] and in the [[hilal-2026-cardiac-somatic-review]] toolbox context; cross-platform benchmarking of duplex methods in [[zhang-2025-smaht-duplex-benchmark]].
- Same lab's single-cell side: [[dong-2017-sccaller]] (SCcaller; the alignment/realignment pipeline is "as we described previously") and the aging-mutation framing in [[vijg-2020-cell]].
- Single-cell versus bulk-duplex trade-off: the paper explicitly positions the single-cell approach as the gold standard it is calibrated against (synthesis link to [[luquette-2025-pta-duplex-mosaicism]], which combines both).

## Open questions

- No measured error floor: how does SMM-seq compare with NanoSeq/CODEC on identical DNA, and is P(E)^N realised in practice?
- Is the 7-read family cutoff transferable across samples, sequencing depth and polymerase lots, or must it be re-derived per experiment?
- Indels and structural variants are out of scope (delegated to SVS).
- The wiki's [[40-Topics/long-read-sequencing]] page lists SMM-seq among long-read duplex variants, but the paper runs on Illumina NovaSeq 150PE — RCA concatemers are short-read sequenced. (tension)

## Related

- [[40-Topics/duplex-sequencing]] · [[nanoseq]] · [[abascal-2021-nanoseq]] · [[vijg-2020-cell]] · [[40-Topics/somatic-mosaicism]]
