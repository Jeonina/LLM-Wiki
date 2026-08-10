---
type: summary
title: "Zong 2017 — MALBAC for the analysis of DNA copy number variation (Neuromethods protocol chapter)"
source: "[[00-Sources/papers/Multiple Annealing and Looping-Based Amplification Cycles (MALBAC) for the Analysis of DNA Copy Number Variation]]"
source_kind: paper
author: "Chenghang Zong"
published: 2017
ingested: 2026-08-10
doi: "10.1007/978-1-4939-7280-7_7"
journal: "Neuromethods vol. 131 — Genomic Mosaicism in Neurons and Other Cell Types"
tags: [MALBAC, scWGA, copy-number-variation, protocol-chapter, quasi-linear-amplification]
entities: []
concepts: ["[[malbac]]", "[[scwga]]", "[[scwga-chemistries]]"]
topics: ["[[whole-genome-amplification]]", "[[brain-somatic-mosaicism]]"]
---

**Citation:** Zong, C. (2017) — *Multiple annealing and looping-based amplification cycles (MALBAC) for the analysis of DNA copy number variation* — in Frade & Gage (eds), *Genomic Mosaicism in Neurons and Other Cell Types*, Neuromethods 131. [DOI](https://doi.org/10.1007/978-1-4939-7280-7_7)

# Zong 2017 — MALBAC protocol chapter

> A protocol chapter from the originator of MALBAC, positioning quasi-linear amplification as the CNV-analysis chemistry of choice for single neurons: looping of amplicons suppresses the exponential runaway of PCR-based WGA, giving the flat coverage profile that copy-number binning depends on.

> ⚠️ **Source caveat.** The bookmarked clipping is a Springer Experiments landing page — abstract truncated at "Here we describe the recent progress in the…", no protocol body, reference list of three items. Mechanistic detail below is drawn from the chemistry as described across this wiki's corpus (principally [[chenghang-2012-science]]), not from this clipping.

## Key claims

- Genomes of even closely related cells differ; resolving that requires single-cell resolution — the framing premise the chapter shares with [[somatic-mosaicism]].
- MALBAC's semi-amplicon looping converts amplification from exponential to **quasi-linear**, which is the property that matters for CNV: uniform coverage per bin rather than uniform yield per molecule.
- The chapter's placement in a *neuronal mosaicism* volume signals the intended application: single-neuron CNV/aneuploidy calling.

## Methods / evidence

Protocol chapter, not a primary results paper — its evidentiary weight is procedural. For MALBAC's actual performance data (coverage uniformity, SNV false-positive rate, amplification-error signature) the wiki's load-bearing source is the original Science paper.

## Surprising or load-bearing bits

- The chapter's own reference list is telling: Dean 2001 (φ29 rolling circle), [[navin-2011-sns-tumor-evolution|Navin 2011]], and Evrony 2012 (single-neuron L1 retrotransposition) — i.e. MALBAC is framed as the bridge between WGA chemistry and the neuronal-mosaicism program.
- MALBAC's known asymmetry — good for CNV, poor for SNV because the first quasi-linear cycles imprint polymerase errors on all downstream copies — is the reason [[pta]] later re-engineered the same quasi-linear idea with terminators instead of looping.

## Concepts touched

- [[malbac]] — protocol-level source; reinforces the CNV-first framing.
- [[scwga-chemistries]] — MALBAC sits between [[mda]] and [[pta]] in the chronology.
- [[compounding-artifact]] — MALBAC's early-cycle error imprinting is the canonical example.

## Connections to other sources

- The primary source for MALBAC in this wiki is [[chenghang-2012-science]]; this chapter adds the protocol/application framing but no new data.
- Contrast with [[gonzalez-pena-2021-pnas|PTA]], which keeps quasi-linearity and drops the looping.
- Its neuronal framing connects to [[lodato-2015-science]] and [[mukamel-2025-aneuploidy-brain]].

## Open questions

- Whether MALBAC retains any niche now that PTA and preamplification-free tagmentation ([[dlp-plus]]) both outperform it on their respective axes — the corpus implies no, but no source states it directly.

## Related

- [[malbac]] · [[scwga-chemistries]] · [[chenghang-2012-science]] · [[whole-genome-amplification]]
