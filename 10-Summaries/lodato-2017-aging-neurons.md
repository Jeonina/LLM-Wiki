---
type: summary
title: "Lodato et al. 2018 — Aging and neurodegeneration are associated with increased mutations in single human neurons"
aliases: []
source: "[[00-Sources/papers/Aging and neurodegeneration are associated with increased mutations in single human neurons]]"
source_quality: full
source_sha256: "4d11d35773117b7f31ff69e4d26f832c71855451d6d937fa75b927d301fdf4b7"
source_kind: paper
author: "Michael A. Lodato, Rachel E. Rodin, Craig L. Bohrson, Michael E. Coulter, Alison R. Barton, Minseok Kwon, Maxwell A. Sherman, Carl M. Vitzthum, Lovelace J. Luquette, Chandri N. Yandava, Peter Park, Christopher A. Walsh (corresponding)"
published: 2017-12-08
ingested: 2026-05-18
updated: 2026-10-07
doi: "10.1126/science.aao4426"
journal: "Science"
tags: [somatic-mosaicism, neurons, aging, neurodegeneration, single-neuron-WGS, MDA, LiRA, mutational-signatures, genosenium, Walsh-lab, Park-lab, Cockayne, xeroderma, nucleotide-excision-repair]
entities: ["[[20-Entities/christopher-walsh]]", "[[20-Entities/peter-park]]"]
concepts: ["[[30-Concepts/genosenium]]", "[[30-Concepts/post-zygotic-variation]]", "[[30-Concepts/mda]]", "[[30-Concepts/mutational-signatures]]", "[[30-Concepts/single-cell-variant-calling]]", "[[30-Concepts/compounding-artifact]]"]
topics: ["[[40-Topics/somatic-mosaicism]]", "[[40-Topics/brain-somatic-mosaicism]]", "[[40-Topics/mosaic-variant-calling]]"]
---

**Citation:** Lodato et al. (2018; online 2017) — *Aging and neurodegeneration are associated with increased mutations in single human neurons* — *Science* 359:555–559. [DOI](https://doi.org/10.1126/science.aao4426) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/29217584/)

> **Corrected 2026-10-07:** title had an inserted word ("somatic") and the year now follows the issue (2 Feb 2018), matching [[10-Summaries/bae-2017-pregastrulation-mutations]] from the same issue. Slug kept.

# Lodato et al. 2018 — somatic mutations accumulate in aging neurons

> Postmitotic human neurons, which do not replicate their DNA, still gain somatic SNVs **approximately linearly with age**, and gain them faster in early-onset neurodegeneration caused by nucleotide-excision-repair defects. The authors sequenced **159 single neurons** (MDA, 45X WGS) from prefrontal cortex (PFC) and hippocampal dentate gyrus (DG) of 15 neurologically normal individuals aged 4 months to 82 years and 9 individuals with Cockayne syndrome (CS) or xeroderma pigmentosum (XP), and called sSNVs with the linkage-based **LiRA** pipeline. They estimate **~23 sSNVs/year in PFC and ~40 sSNVs/year in DG**, a **~2.3–2.5-fold excess** in CS/XP neurons, and three mutational signatures: a replication-independent **clocklike Signature A**, a DG-enriched C>T **Signature B**, and an oxidative, DNA-repair-linked C>A **Signature C**. They name the age-related accumulation **genosenium**.

## Key claims

- **Cohort.** 91 PFC neurons from 15 normal individuals (0.4–82.7 years), 26 DG neurons from 6 of them, and 42 PFC neurons from 9 CS (*CSB*, 6 cases) or XP (*XPA* or *XPD*, 3 cases) individuals; Table 1 totals 24 cases, 133 PFC and 26 DG neurons, 159 neurons. The Fig. 3B caption instead counts "161 neurons".
- **Linear accumulation with age.** Genome-wide sSNV counts in normal neurons correlated with age (*P* = 2 × 10⁻⁵, mixed effects model), with some heterogeneity within individuals and age groups.
- **Regional rates.** Accumulation was significant in both PFC (*P* = 4 × 10⁻⁵) and DG (*P* = 2 × 10⁻⁷), with an "almost twofold" higher rate in DG (~40 sSNVs/year) than PFC (~23 sSNVs/year) (*P* = 8 × 10⁻⁴). In the six matched brains, two had significantly more DG sSNVs, three nominally more, and one nominally more in PFC.
- **DNA-repair disease.** CS neurons showed a ~2.3-fold and XP neurons a ~2.5-fold excess over the age-adjusted normal PFC rate (*P* = 0.006 for both). Progeroid neurons carried about as many sSNVs as aged normal PFC neurons, which the authors read as defective nucleotide excision repair accelerating aging through sSNV accumulation.
- **Spectrum shifts with age.** C>T was the majority class in the youngest PFC neurons and its fraction fell with age; T>C rose with age in PFC, possibly reflecting DNA damage linked to fatty-acid oxidation. Because C>T is also a known MDA artifact, the authors argue that its systematic age trend shows the C>T calls are "largely biological".
- **Genic and functional bias (as in Lodato 2015).** Normal-PFC sSNVs were enriched in coding exons, showed transcriptional strand bias, and were enriched in neural-function genes. Coincident-probability modelling suggested that linear sSNV accumulation gives an **exponential accumulation of biallelic deleterious coding mutations**, in line with classical mutation-theory-of-aging hypotheses (Szilard 1959).
- **Signature A — clocklike, replication-independent.** Mostly C>T and T>C; the only signature that rose with age (*P* = 1 × 10⁻¹¹), regardless of region or disease. It resembles COSMIC cancer Signature 5, so a "clocklike" process is active in postmitotic cells and does not depend on DNA replication.
- **Signature B — developmental, DG-specific.** Mostly C>T, not correlated with age overall (suggesting an early, perhaps prenatal, process), enriched in DG over PFC (*P* = 2 × 10⁻⁴), and rising with age in DG but not PFC (*P* = 0.04, difference in slopes). The authors note it may include C>T artifacts but argue the regional difference, which mirrors postnatal DG neurogenesis, shows a dominant biological component.
- **Signature C — oxidative / repair-deficient.** Defined by C>A, the class most tied to oxidative damage; enriched in CS (*P* = 0.016) and XP (*P* = 0.022) neurons and rising modestly with age in normal neurons (*P* = 0.04). An outlier PFC neuron from case 5087 had the highest sSNV rate in the dataset and a high Signature C share, which the authors take as evidence that single neurons in a normal brain can suffer "catastrophic oxidative damage".
- **Baseline at birth.** Within one year of birth, neurons already carry **~300 to 900 sSNVs**, which the authors match to the 200–400 sSNVs estimated in fetal progenitors at ≤20 weeks of gestation by the companion Bae et al. paper.
- **Robustness to C>T.** All signature associations held after removing every C>T call (fig. S11), so residual MDA C>T artifacts do not drive the main conclusions.

## Methods / evidence

Single neuronal nuclei (NIH NeuroBioBank postmortem tissue) were sorted by flow cytometry, lysed on ice under alkaline conditions to reduce lysis artifacts, amplified by MDA and sequenced to 45X. sSNVs were called with **LiRA** (Bohrson et al., then a bioRxiv preprint): only candidates **perfectly linked** in reads to a nearby heterozygous germline SNP are accepted, which separates double-stranded mutations from single-strand amplification errors. Because only **~20% of sSNVs** lie close enough to a germline SNP, genome-wide burden is a **model-based extrapolation** from that subset. Called sSNVs had alternate-allele frequencies matching germline SNVs (fig. S1), and counts were not systematically related to postmortem interval, storage time or coverage uniformity (fig. S2). Age effects were tested with mixed effects / mixed linear models; spectra with two-way ANOVA and Sidak correction; signatures by NMF on trinucleotide context. Detailed methods, PaSD-qc quality control and the full statistics are in the supplementary materials, which the clipping does not include.

Weight: the first direct single-neuron measurement of postnatal somatic mutation with age and in repair-deficient disease, with a clear dose-response by age and a well-chosen positive-control disease group. The absolute rates rest on MDA plus extrapolation from ~20% of the genome, and later PTA- and duplex-based work revised the PFC rate downward (see Connections). The trends and signatures are better supported than the absolute numbers. (synthesis)

## Limitations

**Authors' own:**
- C>T is a known MDA artifact; Signature B "may include technical artifacts". The authors address this with the age trend, the DG/PFC contrast and a reanalysis without any C>T calls.
- Genome-wide counts are extrapolated from the ~20% of sSNVs near germline SNPs.
- Only monogenic DNA-repair disorders were studied; "it will be important to define how other, more common causes of neurodegeneration may influence genosenium".

**Reviewer notes:**
- Small, uneven sampling: 3–20 neurons per individual, DG only in 6 brains, and only 3 XP cases. The DG-vs-PFC rate difference was significant within only 2 of 6 matched brains. (synthesis)
- The title's "neurodegeneration" means genetic CS/XP, not Alzheimer's or other common neurodegenerative disease, and CS/XP cases are mostly young children, so the age-adjusted excess depends on extrapolating the normal PFC regression to young ages. (synthesis)
- MDA single-strand-dropout artifacts later accounted for a substantial part of the MDA-era rate: SCAN2 reanalysis of MDA neurons gave 31/year falling to ~19/year after artifact correction, against 16.5/year with PTA ([[10-Summaries/luquette-2022-neuron-scan2-indels]]). (synthesis)

## Surprising or load-bearing bits

- **A clocklike mutation process without replication.** Signature A (≈ SBS5) rises with age in neurons that do not divide, so the "clock" is not a replication-error count. This is the claim later work most often cites.
- **Hippocampus ages its genome faster than cortex**, and the DG excess carries a signature (B) that tracks postnatal neurogenesis rather than age alone.
- **Coined "genosenium"** for the age-related accumulation of somatic mutations in normal tissue.
- **Exponential biallelic knockout argument:** linear SNV accumulation implies exponentially rising numbers of neurons with both copies of a gene disrupted, a mechanistic bridge from mosaicism to functional decline. It rests on modelling, not observation. (synthesis)
- **Per-neuron outliers** (case 5087) suggest heavy-tailed, cell-to-cell variation in oxidative damage within a single normal brain.

## Entities mentioned

- [[20-Entities/christopher-walsh]] — corresponding author; Walsh lab single-neuron sequencing programme.
- [[20-Entities/peter-park]] — co-senior computational lead; LiRA and signature analysis.

## Concepts touched

- [[30-Concepts/genosenium]] — the term is coined here for age-related accumulation of somatic mutations.
- [[30-Concepts/post-zygotic-variation]] — postnatal, postmitotic sSNVs on top of developmental mosaicism.
- [[30-Concepts/mda]] — MDA single-neuron WGS, with C>T artifacts handled by alkaline lysis, LiRA and C>T-free reanalysis.
- [[30-Concepts/mutational-signatures]] — NMF signatures A (clocklike, SBS5-like), B (DG/developmental C>T) and C (oxidative C>A).
- [[30-Concepts/single-cell-variant-calling]] — linkage-based calling (LiRA) and extrapolation from the phaseable subset.
- [[30-Concepts/compounding-artifact]] — the MDA-era rate later shown to be artifact-inflated.

## Connections to other sources

- **Companion paper:** [[10-Summaries/bae-2017-pregastrulation-mutations]] — same *Science* issue; fetal progenitor burden (200–400 sSNVs) that Lodato matches to its ~300–900 sSNVs in infant neurons.
- **Builds on:** [[10-Summaries/lodato-2015-science]] (exon enrichment, transcriptional strand bias, C>T from deamination) and [[10-Summaries/bohrson-2019-lira]] (the calling method, published later).
- **Revised by:** [[10-Summaries/luquette-2022-neuron-scan2-indels]] — PTA + SCAN2 give 16.5 sSNVs/year in PFC and attribute part of the MDA excess to single-strand dropout and Signature B artifacts. [[10-Summaries/xing-2021-meta-cs]] (~16/year) and [[10-Summaries/abascal-2021-nanoseq]] (bulk duplex) converge on the lower rate.
- **Successor callers from the same group:** [[10-Summaries/luquette-2019-natcomm]] (SCAN-SNV).
- **Clocklike signature context:** [[10-Summaries/alexandrov-2013-mutational-signatures]].
- **Disease extension:** [[10-Summaries/miller-2022-nature]] (Alzheimer's neurons), answering the paper's call to test common neurodegeneration.
- **Aging context:** [[10-Summaries/vijg-2020-cell]], [[10-Summaries/cagan-2022-nature]], [[10-Summaries/taejeong-2022-science]]; review in [[10-Summaries/bizzotto-2022-brain-mosaicism-review]]. Bulk-tissue comparator cited by the paper: [[10-Summaries/hoang-2016-botseqs]].

## Open questions

- How much of the DG excess and of Signature B survives in PTA or duplex data? (synthesis)
- Do common neurodegenerative diseases raise sSNV burden as CS/XP do, and through Signature C? The authors pose this; [[10-Summaries/miller-2022-nature]] is the follow-up.
- Is the predicted exponential rise in biallelic knockouts observable in single neurons? (synthesis)

## Related

- [[40-Topics/somatic-mosaicism]] · [[40-Topics/brain-somatic-mosaicism]] · [[30-Concepts/genosenium]] · [[30-Concepts/mda]] · [[30-Concepts/mutational-signatures]]
- [[10-Summaries/bae-2017-pregastrulation-mutations]] · [[10-Summaries/luquette-2022-neuron-scan2-indels]] · [[10-Summaries/kapadia-2024-stem-cell-aging]]
