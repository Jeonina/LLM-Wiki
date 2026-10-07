---
type: summary
title: "Nandi et al. 2025 — A Universal Duplex Sequencing Approach for Accurate Detection of Somatic Mutations (UDSeq)"
source: "[[00-Sources/papers/A Universal Duplex Sequencing Approach for Accurate Detection of Somatic Mutations.pdf]]"
source_quality: full
source_sha256: "206dc27b4082f7f282d66d880197e075e954864abba84da06ee0ccf45ca69bd2"
source_kind: paper
author: "Shuvro P. Nandi, Yuhe Cheng (co-first), Shams Al-Azzam, ... Mia Petljak, Silvia Balbo, Laurie G. Hudson, Ke Jian Liu, Jiri Zavadil, Joseph G. Gleeson, Ludmil B. Alexandrov (corresponding)"
published: 2025-09-16
ingested: 2026-05-12
updated: 2026-10-07
doi: "10.1101/2025.09.14.676103"
journal: "bioRxiv (preprint)"
aliases: ["UDSeq", "Universal Duplex Sequencing", "Nandi 2025"]
tags: [duplex-sequencing, UDSeq, low-input, mutational-signatures, Alexandrov-lab, random-fragmentation, xGen-UMI, DupCaller, sperm-benchmark, carcinogen-exposure, cross-species, preprint]
entities:
  - "[[20-Entities/ludmil-alexandrov]]"
  - "[[20-Entities/joseph-gleeson]]"
concepts:
  - "[[30-Concepts/mutational-signatures]]"
  - "[[30-Concepts/umi-molecular-barcoding]]"
  - "[[30-Concepts/nanoseq]]"
  - "[[30-Concepts/codec]]"
  - "[[30-Concepts/hidef-seq]]"
topics:
  - "[[40-Topics/duplex-sequencing]]"
  - "[[40-Topics/somatic-mosaicism]]"
---

**Citation:** Nandi, Cheng et al. (2025) — *A Universal Duplex Sequencing Approach for Accurate Detection of Somatic Mutations* — *bioRxiv* (preprint, posted 16 Sep 2025). [DOI](https://doi.org/10.1101/2025.09.14.676103)

# Nandi 2025 — UDSeq

> UDSeq is a library-prep recipe, not a new chemistry. It starts from the NanoSeq/BotSeqS bottleneck approach and changes three things: (1) **random enzymatic fragmentation** (NEBNext dsDNA Fragmentase or UltraShear) in place of sonication or HpyCH4V restriction, giving "≥95%" genome/exome coverage; (2) **IDT xGen cfDNA & FFPE UMI ligation on beads** for high conversion from as little as **100 pg**; (3) **qPCR quantification of UMI-ligated molecules** so that a set number of femtomoles (0.2 fmol for ~90× human WGS) goes into PCR. Mutations are called with the lab's **DupCaller**. Using sperm from eight men, the authors compare the regression intercept of mutations against age with intercepts from trio de novo studies, and infer an error of **~2.5 × 10⁻⁹ per bp**, similar to NanoSeqV1 and HiDEF-seq estimated the same way. The rest of the paper shows breadth: carcinogen signatures in unexpanded cell populations, UV-exposed mice and NNK-exposed rats, chicken and sheep tissues, and five organs from one 70-year-old donor.

## Key claims

- **Error rate from sperm.** UDSeq sperm samples (n = 8, ages 19–70) accumulate "1.58 SBSs per year", against 1.54 and 1.40 per year in two Icelandic trio studies. The intercept at age zero is "12.60" for UDSeq against 4.96 and 6.58 for the trio studies. The difference is read as "between 6 and 7.6 artifactual SBS per sequenced haploid sperm sample" of ~3 Gb, "approximately 2.5 × 10⁻⁹ errors per bp". The same method gives NanoSeqV1 (n = 7) "about 4.8 × 10⁻⁹" (against 5 × 10⁻⁹ in its original paper) and HiDEF-seq (n = 5) "4.3 × 10⁻⁹". The authors conclude the three are "effectively similar, with less than 5 mutations per billion sequenced base pairs". The sperm spectrum resembles SBS1 + SBS5 and matches paternal de novo mutations (cosine similarity 0.92).
- **Library conversion.** At 10 ng input, the xGen ligation gives "up to four times more femtomoles of usable library" than **NanoSeqV2** (p = 0.00022). The "fourfold" claim in the abstract is a comparison with NanoSeqV2 specifically, not with all prior duplex methods.
- **Coverage.** Random fragmentation gives "near-complete coverage (≥95%; comparable to bulk sequencing)" of genome and exome. NanoSeqV1 and CODEC-HpyCH4V reach ~30% and HiDEF-seq ~40%; NanoSeqV2 also has near-complete coverage. Fragmentase is cheaper but leaves overhangs that must be trimmed; UltraShear gives uniform fragments at higher reagent cost.
- **Comparison table (Table 1).** Minimum input and approximate error per bp: DupSeq ~1 µg, 2 × 10⁻⁷; BotSeqS 50 ng, 2 × 10⁻⁷; NanoSeqV1 50 ng, 5 × 10⁻⁹; NanoSeqV2 30 ng, 5 × 10⁻⁹; HiDEF-seq 500 ng–1.5 µg, 4 × 10⁻⁹; CODEC 2.5 ng, 1 × 10⁻⁷; CODEC-HpyCH4V 50 ng, 3 × 10⁻⁸; **UDSeq 100 pg, 2.5 × 10⁻⁹**.
- **Carcinogen signatures without clonal expansion.** Exposed cells were passaged once (no single-cell bottleneck), and DNA was then sequenced: HepG2 + 4NQO or aristolochic acid I, NOK + NNK, N/TERT-1 + solar-simulated UV. Profiles matched clonally expanded references (Fig. 2c cosine similarity: 4NQO 0.97, AA-I 0.98, NNK 0.95, UV 0.99), and AA-I matched COSMIC **SBS22a**. The workflow takes "as little as 15 days" against "60 days or more" for clonal expansion. At 100 pg input (4NQO, AA-I in HepG2), profiles matched those from 100 ng. Exome capture and a 127-gene pan-cancer panel reproduced AA-I (cosine similarity 0.98 to SBS22a) and 4NQO (0.94).
- **In vivo exposures.** SKH-1 hairless mice given ssUVR (14 kJ/m², ~0.5 minimal erythema dose, 3×/week for 30 weeks) had "105-fold and 6.5-fold higher mutational loads in the dorsal and ventral skin", with UV signatures absent in controls (n = 4 per group). F344 rats given NNK in drinking water (5 ppm, 15 weeks) had "4.7-fold higher" lung burden (p = 0.013 in the text, 0.010 in the Fig. 3 legend). The NNK pattern matched the cell-line NNK profile (cosine similarity 0.90).
- **Non-model organisms.** Chicken breast, pancreas and skin, and sheep kidney layers, showed SBS1/SBS5, plus **SBS18** (reactive oxygen species) in chicken skin. Sheep kidney cortex had "1.49-fold higher mutational burden than the medulla".
- **Healthy human organs (one 70-year-old donor).** Brain had the lowest burden, then kidneys, then liver. In Fig. 4a: left/right cortex 3.23/3.13 × 10⁻⁷ per bp (1,874/1,816 SBS per diploid genome), left/right kidney 3.89/4.43 × 10⁻⁷, liver 6.02 × 10⁻⁷ (3,494). All samples had SBS1/SBS5, **SBS40** appeared in both kidneys, and **SBS4** (tobacco) appeared only in liver, although "the smoking status of the donor was unavailable".

## Methods / evidence

Fragmentation to ~350 bp is tuned by sample type: 15 min for sperm and cell lines, 20 min for human tissue and mouse cell lines, 25 min for mouse and rat tissue. Then xGen cfDNA & FFPE UMI adapter ligation, with all steps on magnetic beads. qPCR quantification uses NEBNext Library Quant standards: 330 bp size correction, with 82 bp of adapter added to the TapeStation fragment length. PCR uses IDT UDI primers and Q5. For human WGS, 0.2 fmol and 15 cycles give ~90×, aiming at "~80% duplicated and ~20% unique reads"; mouse uses 0.15 fmol. Hybrid capture pools 6–8 samples per reaction with 500 ng of library each. Sequencing on NovaSeq 6000/X, 2×150 bp. Calling: BWA, GATK duplicate marking, then **DupCaller** v1.0.1, which builds sample-specific error profiles (trinucleotide context for SNVs, homopolymer length for indels) and uses a strand-aware probabilistic model with a matched normal. Signatures were analysed with SigProfilerMatrixGenerator/Assignment. Human tissues came from LIBD post-mortem donors. The full bench protocol (Supplementary Note 1) is referred to but is **not included in the source PDF**; the supplementary figure legends are included, the supplementary figure images are not.

Weight: a broad demonstration paper from one lab, with collaborators. The **error-rate claim rests on an intercept extrapolation** from 8 samples with wide uncertainty: in Fig. 1c the UDSeq intercept error bar spans roughly 5–20 SBS, and the trio intercepts themselves differ by 1.6 SBS. "~2.5 × 10⁻⁹" should therefore be read as order-of-magnitude parity with NanoSeq and HiDEF-seq, not as a ranking. The method uses no internal duplex error control, such as strand-discordance or spike-ins. Most application results are qualitative signature matches (cosine similarity) with n = 1–5 per condition. Cost-effectiveness rests on a projection (Supplementary Fig. 1d), and no head-to-head comparison on the same DNA was run except the conversion test against NanoSeqV2. (synthesis)

## Limitations

**Authors' own:**
- Like all short-read duplex methods, UDSeq is "not well-suited for detecting large structural variants, complex rearrangements, or copy number alterations"; the authors suggest combining it with long reads.
- The left–right kidney difference may reflect how much cortex versus medulla was captured from bulk tissue, not biology.
- The smoking status of the human donor was unavailable, so the SBS4 call in liver cannot be checked.

**Reviewer notes:**
- **Internal inconsistencies.** The text says "the left kidney exhibited more mutations than the right kidney", but Fig. 4a as rendered gives right kidney 4.43 × 10⁻⁷ against left 3.89 × 10⁻⁷. The text cites "Supplementary Figure 3a–c" for data whose legend is "Supplemental Figure 2". The NNK rat p-value differs between text and legend. Table 1's title says "BothSeq" for BotSeqS. (synthesis)
- **Cross-cell-line comparisons.** The "clonally expanded" references in Fig. 2c are mostly from *different* cell types (HFF, iPSC, BEAS-2B against HepG2 and NOK), so cosine similarities of 0.95–0.98 confirm the mutagen signature, not like-for-like equivalence. (synthesis)
- **Competing interests.** The corresponding author declares equity and income from Acurion (formerly io9), six UCSD US provisional applications, a European application, and a PCT application shared with the first author. The paper does not say which of these cover UDSeq. (synthesis)

## Surprising or load-bearing bits

- **Error rate defined against germline biology.** The authors calibrate error from sperm against trio de novo mutation rates, not from strand discordance or known-negative controls. The method can be applied to any duplex method's published sperm data, which is how NanoSeqV1 and HiDEF-seq were re-scored. It depends on trio-study intercepts that themselves differ by ~1.6 SBS. (synthesis)
- **Table 1 re-rates older methods.** It puts Duplex Sequencing ("DupSeq") and BotSeqS at ~2 × 10⁻⁷ per bp. The original papers reported a calculated <10⁻⁹ floor ([[10-Summaries/schmitt-2012-pnas]]) and a 2.6 × 10⁻¹² false-positive rate ([[10-Summaries/hoang-2016-botseqs]]).
- **The bottleneck is set by qPCR femtomoles.** Precise input into PCR, rather than a dilution series, sets the duplicate rate (~80% duplicated reads). This is the practical change that makes low input workable. (synthesis)
- **Clock-like and tissue signatures in a single donor**, including SBS40 in kidney and SBS4 in liver, at whole-genome resolution from bulk tissue without clonal expansion.

## Entities mentioned

- [[20-Entities/ludmil-alexandrov]] — corresponding author; designed the protocol with S.P.N.; the SigProfiler tools come from his lab, and DupCaller is from co-first author Yuhe Cheng (Cheng et al. 2025, ref. 57).
- [[20-Entities/joseph-gleeson]] — co-author; access to and analysis of human samples.

## Concepts touched

- [[30-Concepts/mutational-signatures]] — exposure signatures (SBS22a, UV, 4NQO, NNK), clock-like SBS1/SBS5, SBS18, SBS40 and SBS4 read from polyclonal populations.
- [[30-Concepts/umi-molecular-barcoding]] — commercial xGen UMI adapters in place of custom duplex tags.
- [[30-Concepts/nanoseq]] — direct baseline. UDSeq keeps NanoSeqV1's low error but uses random fragmentation; NanoSeqV2 is the conversion-efficiency comparator.
- [[30-Concepts/codec]] / [[30-Concepts/hidef-seq]] — comparators in Table 1 and the sperm re-analysis.
- [[30-Concepts/structural-variants]] / [[30-Concepts/copy-number-variation]] — explicitly out of scope for short-read duplex sequencing.

## Connections to other sources

- Lineage: [[10-Summaries/schmitt-2012-pnas]] → [[10-Summaries/kennedy-2014-duplex-protocol]] → [[10-Summaries/hoang-2016-botseqs]] → [[10-Summaries/abascal-2021-nanoseq]] → UDSeq. Other routes to the same goal: [[10-Summaries/bae-2023-codec]], [[10-Summaries/liu-2024-hidef-seq]], [[10-Summaries/maslov-2022-smm-seq]].
- Not among the six methods in [[10-Summaries/zhang-2025-smaht-duplex-benchmark]], so no independent cross-comparison exists yet.
- The introduction presents UDSeq as an alternative to single-cell WGS, citing amplification artefacts and allele dropout ([[10-Summaries/lodato-2015-science]], [[10-Summaries/dong-2017-sccaller]], [[10-Summaries/gonzalez-pena-2021-pnas]], [[10-Summaries/xing-2021-meta-cs]]). Single-cell duplex methods such as [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] give per-cell resolution that UDSeq does not. (synthesis)
- Signature framework: [[10-Summaries/alexandrov-2013-mutational-signatures]].

## Open questions

- Preprint; not yet peer-reviewed.
- How does UDSeq compare with NanoSeqV2, CODEC and others on the *same* DNA, using a common error metric (for example strand discordance or the SMaHT reference materials)? (synthesis)
- Does the ~80%-duplicate target hold at 100 pg, and how much duplex coverage does a 100 pg library actually give? The paper shows matching signature profiles at 100 pg but no coverage or burden numbers. (synthesis)
- Like all duplex methods, UDSeq needs both original strands, so it cannot be used directly on whole-genome-amplified single-cell DNA ([[50-Notes/single-cell-duplex-sequencing]]). (synthesis)

## Related

- [[40-Topics/duplex-sequencing]] · [[30-Concepts/mutational-signatures]] · [[30-Concepts/nanoseq]] · [[schmitt-2012-pnas]] · [[abascal-2021-nanoseq]] · [[10-Summaries/zhang-2025-smaht-duplex-benchmark]]
