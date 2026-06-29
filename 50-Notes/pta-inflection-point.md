---
type: note
title: "The PTA inflection point — when scDNA-seq became trustworthy"
aliases: [PTA inflection, MDA-to-PTA, scWGA chronology]
tags: [synthesis, scDNA-seq, PTA, MDA, scWGA, methods-chronology, somatic-mosaicism]
created: 2026-05-19
updated: 2026-06-29
sources: [
  "[[10-Summaries/dean-2002-mda]]",
  "[[10-Summaries/navin-2011-sns-tumor-evolution]]",
  "[[10-Summaries/gawad-2016-scgenome-review]]",
  "[[10-Summaries/chen-2017-lianti]]",
  "[[10-Summaries/lodato-2017-aging-neurons]]",
  "[[10-Summaries/bae-2017-pregastrulation-mutations]]",
  "[[10-Summaries/gonzalez-pena-2021-pnas]]",
  "[[10-Summaries/evrony-2021-scDNA-applications-review]]",
  "[[10-Summaries/taejeong-2022-science]]",
  "[[10-Summaries/kousi-2022-ad-mosaicism]]",
  "[[10-Summaries/luquette-2025-pta-duplex-mosaicism]]",
  "[[10-Summaries/mukamel-2025-aneuploidy-brain]]",
  "[[10-Summaries/kriz-2025-duplex-multiome]]",
  "[[10-Summaries/shao-2025-scDNA-mosaicism-review]]"
]
---

# The PTA inflection point — when scDNA-seq became trustworthy

> Around 2020-2021, single-cell DNA sequencing crossed a methodological threshold: **Primary Template-Directed Amplification (PTA)** displaced multiple displacement amplification (MDA) as the default chemistry for cohort-scale mosaicism studies ([[10-Summaries/gonzalez-pena-2021-pnas]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]). The change was not incremental — it shifted what scDNA-seq could be trusted to measure. Pre-PTA cohort studies relied on heavy bioinformatic correction (LiRA, SCAN-SNV) to extract usable signal from MDA's amplification artifacts ([[10-Summaries/evrony-2021-scDNA-applications-review]]). Post-PTA studies (BSMN-cohort, SMaHT-flagship, Duplex-Multiome) achieve direct per-cell mutation calling at sensitivity and precision that previously required matched bulk controls ([[10-Summaries/taejeong-2022-science]]; [[10-Summaries/luquette-2025-pta-duplex-mosaicism]]; [[10-Summaries/kriz-2025-duplex-multiome]]).

## Before PTA: the MDA era (2002-2020)

Multiple displacement amplification ([[10-Summaries/dean-2002-mda]]) used φ29 polymerase + random hexamers to amplify femtogram-scale single-cell DNA into nanogram quantities suitable for short-read sequencing. The chemistry was the only viable option for whole-genome single-cell DNA sequencing throughout the 2000s and 2010s ([[10-Summaries/gawad-2016-scgenome-review]]).

MDA enabled the foundational single-cell genomics studies — Navin's punctuated clonal evolution in breast cancer ([[10-Summaries/navin-2011-sns-tumor-evolution]]), Lodato's aging neuron mutation burdens ([[10-Summaries/lodato-2017-aging-neurons]]), Bae's pregastrulation vs neurogenesis mutation timing ([[10-Summaries/bae-2017-pregastrulation-mutations]]) — but at significant methodological cost ([[10-Summaries/gawad-2016-scgenome-review]]):

- **Coverage non-uniformity**: order-of-magnitude amplicon-to-amplicon depth variation ([[10-Summaries/gonzalez-pena-2021-pnas]]).
- **Allelic dropout**: 10-40% of heterozygous loci showed one-allele amplification only ([[10-Summaries/gawad-2016-scgenome-review]]).
- **Chimera formation**: random template switching produced ~1-10% chimeric reads ([[10-Summaries/gawad-2016-scgenome-review]]).
- **Allelic imbalance**: heterozygous variants frequently amplified at non-0.5 ratios ([[10-Summaries/gonzalez-pena-2021-pnas]]).
- **High false-positive rate** at low VAF — true somatic variants indistinguishable from amplification artifacts ([[10-Summaries/evrony-2021-scDNA-applications-review]]).

These limitations gave rise to a generation of **algorithmic compensations**: LiRA, SCAN-SNV, Monovar, SCcaller, MosaicForecast — all attempting to extract signal from MDA-amplified single-cell data via local allele-frequency models, matched-bulk priors, or ensemble classifiers ([[10-Summaries/evrony-2021-scDNA-applications-review]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]). The compensations worked but reduced effective sensitivity and complicated cross-study comparison ([[10-Summaries/evrony-2021-scDNA-applications-review]]).

The intermediate generation — MALBAC (2012), LIANTI ([[10-Summaries/chen-2017-lianti]]), DOP-PCR — improved on specific MDA shortcomings but never displaced it as the default chemistry ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## The PTA mechanism

[[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena et al. 2021]] modified the canonical MDA reaction by adding **irreversible-terminator dideoxynucleotides at low concentration**. The terminators stochastically halt amplification at short distances (~100 bp amplicons), forcing the reaction to operate on the *primary template* rather than on daughter amplicons. This converts MDA's exponential, error-propagating amplification into a **quasilinear, primary-template-restricted amplification** ([[10-Summaries/gonzalez-pena-2021-pnas]]).

The mechanistic consequence: errors do not compound across amplification cycles. Each region of the genome is amplified from the original cellular template, not from previously-amplified copies.

## After PTA: what changed empirically

Direct measurements from [[10-Summaries/gonzalez-pena-2021-pnas]]:

| Property | MDA | PTA |
|---|---|---|
| Coverage uniformity (chr1 depth tracks) | Order-of-magnitude variation | Near-flat |
| Allelic balance at heterozygous loci | Heavily skewed | ~0.5 |
| Per-cell genome coverage at ~30× | ~70-80% | **~95%** |
| Variant-calling FP rate at low VAF | High; requires LiRA/SCAN-SNV correction | Low; direct calling viable |
| Per-cell DNA input requirement | Higher | Reduced |

The most consequential shift: **direct SNV calling without allele-balance correction became feasible** ([[10-Summaries/gonzalez-pena-2021-pnas]]). This unblocked cohort-scale workflows that had been throttled by per-cell QC overhead.

## What PTA enabled

The post-2021 mosaicism literature is largely PTA-anchored:

- **[[10-Summaries/taejeong-2022-science|Bae 2022]]** — analysis of somatic mutations across 131 human brains; ~6% of brains identified as hypermutable (>101 SNVs/neuron) — possibly precursor states for glioma. PTA-enabled cohort.
- **[[10-Summaries/kousi-2022-ad-mosaicism|Kousi 2022]]** — cell-type-specific somatic mutational burden in Alzheimer's brains.
- **[[10-Summaries/mukamel-2025-aneuploidy-brain|Mukamel 2025]]** — aneuploidy atlas in mouse brain; cell-type-specific concentration of chr16 trisomy in oligodendrocyte precursors, Pons neurons, and pericytes.
- **[[10-Summaries/luquette-2025-pta-duplex-mosaicism|Luquette 2025 (SMaHT-flagship)]]** — 102 PTA-amplified nuclei from lung and colon of one 74-year-old donor, validated via bulk duplex sequencing; body-wide cellular ancestry from shared embryonic mutations.
- **[[10-Summaries/kriz-2025-duplex-multiome|Kriz 2025 (Duplex-Multiome)]]** — duplex consensus integrated into 10x Multiome; per-nucleus point mutations + chromatin + RNA at >51,400 nuclei scale. Built on the foundation PTA established.

The 2025 SMaHT and BSMN consortium efforts both use PTA as the default scWGA chemistry ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## What PTA did *not* solve

PTA improved coverage and reduced amplification noise but did not address two distinct problems:

1. **Per-cell sequencing cost** — PTA still produces a single library per cell that must be deeply sequenced (~30× per nucleus). Cohort scaling beyond ~10³ cells remains expensive ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
2. **Single-cell duplex fidelity** — PTA destroys strand identity, so true low-VAF variant detection still requires either bulk-duplex validation ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]) or a fundamentally different chemistry like Duplex-Multiome ([[10-Summaries/kriz-2025-duplex-multiome]]) — see [[50-Notes/single-cell-duplex-sequencing]] for that story.

The amplification problem and the strand-identity problem are orthogonal. PTA solved the first; Duplex-Multiome later solved the second from a different direction.

## Methodological lesson

The PTA inflection is a case study in how a single chemistry improvement can shift what an entire subfield can ask. Pre-PTA, the question "can we count somatic mutations per cell?" was answerable only with heavy caveats and matched-bulk controls. Post-PTA, that question is answerable directly; the field has moved on to "can we count mutations per cell-type, per developmental window, per regulatory context?" ([[10-Summaries/mukamel-2025-aneuploidy-brain]]; [[10-Summaries/taejeong-2022-science]]; [[10-Summaries/kriz-2025-duplex-multiome]]).

The pattern recurs in scDNA-seq history: foundational improvements in upstream chemistry (Tn5 enabling ATAC-seq, MDA enabling early scWGA, PTA enabling cohort mosaicism, Duplex-Multiome enabling joint mutation + epigenome) unlock orders-of-magnitude expansion in the questions the field treats as routine. Bioinformatic compensation is a stopgap, not a substitute (synthesis based on [[10-Summaries/evrony-2021-scDNA-applications-review]] + [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## What's next after PTA

Three plausible inflection points visible in the current literature:

1. **PTA + duplex fusion** — a chemistry that combines PTA's coverage uniformity with strand identity preservation. Not yet published; conceptually closest to META-CS but at PTA-grade uniformity ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
2. **High-throughput PTA on droplet platforms** — currently PTA is plate-based (~384 cells/run). A droplet-PTA hybrid would enable 10⁴-10⁵-cell cohort studies. No published implementation.
3. **PTA + joint-omic capture** — extending PTA-amplified DNA to co-capture transcriptome or chromatin from the same cell. Duplex-Multiome takes a different route but the PTA-anchored multi-omic remains open.

## Related

- [[40-Topics/scdna-seq]] · [[40-Topics/somatic-mosaicism]] · [[40-Topics/whole-genome-amplification]]
- [[30-Concepts/pta]] · [[30-Concepts/scwga]] · [[30-Concepts/scwga-chemistries]]
- [[50-Notes/single-cell-duplex-sequencing]] — the duplex-fidelity inflection that followed PTA
- [[50-Notes/droplet-vs-single-molecule-scdna]] — the breadth-depth tradeoff PTA partly bridges
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — the broader synthesis PTA + Duplex-Multiome enabled
- [[50-Notes/synthesis-targets]] — this note resolves the "PTA inflection point" target
