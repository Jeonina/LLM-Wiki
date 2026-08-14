---
type: summary
title: "Luquette et al. 2021 — Ultraspecific somatic SNV and indel detection in single neurons using primary template-directed amplification (SCAN2)"
source: "[[00-Sources/papers/Ultraspecific somatic SNV and indel detection in single neurons using primary template-directed amplification]]"
source_kind: paper
author: "Lovelace J. Luquette, Michael B. Miller, Zinan Zhou, Craig L. Bohrson, Alon Galor, Michael A. Lodato, Charles Gawad, Jay West, Christopher A. Walsh, Peter J. Park"
published: 2021-05-01
ingested: 2026-08-13
doi: "10.1101/2021.04.30.442032"
journal: "bioRxiv (preprint; later Cell Genomics 2022)"
tags: [SCAN2, PTA, somatic-indel, single-cell-variant-calling, brain-mosaicism, mutation-rate, amplification-artifact]
entities: ["[[lovelace-luquette]]", "[[peter-park]]", "[[christopher-walsh]]", "[[charles-gawad]]", "[[jay-a-a-west]]"]
concepts: ["[[single-cell-variant-calling]]", "[[pta]]", "[[allele-dropout]]", "[[post-zygotic-variation]]", "[[compounding-artifact]]"]
topics: ["[[brain-somatic-mosaicism]]", "[[mosaic-variant-calling]]", "[[whole-genome-amplification]]", "[[computational-methods]]"]
---

**Citation:** Luquette et al. (2021) — *Ultraspecific somatic SNV and indel detection in single neurons using primary template-directed amplification* — *bioRxiv*. [DOI](https://doi.org/10.1101/2021.04.30.442032)

# Luquette 2021 — SCAN2

> The caller that pairs with [[pta|PTA]]. 76 single neurons amplified with PTA, plus **SCAN2** — the successor to [[luquette-2019-natcomm|SCAN-SNV]] extended to **indels**. Two headline numbers: the neuronal SNV accumulation rate is **revised down to 15 SNVs/year**, and somatic **indels accumulate at ≥2 per year per neuron** and may matter *more* for gene function than the SNVs do.

> **Source caveat:** the ingested clipping contains only the abstract and front matter — no figures, methods, or results text. Claims below are therefore limited to what the abstract states; the SCAN2 algorithm's internals are not recoverable from this source. The peer-reviewed version (Cell Genomics 2022) is not in the corpus.

## Key claims

- **PTA + SCAN2 detects both clonal and non-clonal somatic SNVs and indels** in single neurons. "Non-clonal" here means present in a single neuron only — the hardest case, because there is no second cell to corroborate the call and every candidate must be separated from amplification artifact on its own merits.
- **The age-related SNV accumulation rate is revised to 15 SNVs per year per neuron.** This is a *downward* revision of prior [[mda|MDA]]-era estimates, and the revision is attributed to artifacts in the older amplification chemistries — the authors state explicitly that they "identify artifacts in other amplification methods."
- **Somatic indels also increase with age, at ≥2 indels per year per neuron.** This is the first genome-wide single-neuron indel rate.
- **Indels may have a larger functional impact than SNVs in human neurons.** Frameshift and splice consequences per event are far more disruptive than a random substitution, so a 2:15 indel:SNV ratio does not translate to a 2:15 impact ratio.
- **Competing-interest disclosure is load-bearing:** two authors (Gawad, West) are cofounders/officers of BioSkryb, the manufacturer of the PTA kits used. This does not invalidate the results but is relevant when reading a paper whose central claim is that PTA is cleaner than the alternatives.

## Methods / evidence

76 single-neuron whole genomes amplified by PTA, with SCAN2 developed alongside. The abstract does not specify donor count, age range, brain region, or the validation strategy; those cannot be extracted from this source.

Weight to carry: the 15 SNVs/year figure is now the widely used neuronal value, but the source here is a preprint abstract. Any manuscript claim citing the number should cite the peer-reviewed version.

## Surprising or load-bearing bits

- **The rate revision is the real news, not the tool.** A field had converged on a neuronal mutation rate from MDA data; a cleaner chemistry moved the number. This is the cleanest example in the corpus of *chemistry determining a biological constant* — the same argument the wiki makes about [[50-Notes/pta-inflection-point|the PTA inflection point]].
- **Indels were essentially unmeasurable before PTA.** [[mda|MDA]]'s polymerase-slippage artifacts sit exactly on top of the indel signal, which is why prior single-neuron work reported SNVs only. Getting an indel rate at all is a chemistry result as much as an algorithm result.
- **SCAN2 sits in the middle of a three-paper arc from the same group**: [[luquette-2019-natcomm|SCAN-SNV]] (2019, MDA, SNVs only) → SCAN2 (2021, PTA, SNVs + indels) → [[luquette-2025-pta-duplex-mosaicism|PTA + duplex validation]] (2025, orthogonal confirmation). Each step removes one source of doubt.

## Entities mentioned

- [[lovelace-luquette]] — first author; author of the SCAN-SNV/SCAN2 caller line.
- [[peter-park]] — senior author; computational genomics.
- [[christopher-walsh]] — senior author; brain somatic mosaicism.
- [[charles-gawad]] — coauthor; BioSkryb cofounder (declared).
- [[jay-a-a-west]] — coauthor; BioSkryb CEO (declared).

## Concepts touched

- [[single-cell-variant-calling]] — SCAN2 is the PTA-native caller; extends the SCAN line to indels.
- [[pta]] — the amplification chemistry this caller is matched to.
- [[compounding-artifact]] — the paper's implicit argument: artifact in the chemistry propagates into a published biological rate.

## Connections to other sources

- Direct predecessor: [[luquette-2019-natcomm]] (SCAN-SNV, allelic-imbalance model, MDA).
- Direct successor: [[luquette-2025-pta-duplex-mosaicism]] (PTA + bulk duplex, 102 lung/colon nuclei).
- The chemistry: [[gonzalez-pena-2021-pnas]] (PTA founding paper).
- Revises the rate reported by [[lodato-2015-science]] and [[lodato-2017-aging-neurons]] (MDA-based single-neuron mutation accumulation).
- Same-cohort context: [[taejeong-2022-science]], [[miller-2022-nature]].
- Benchmarking context: [[ha-2023-natmethods]] shows low concordance between mosaic callers, which is the backdrop this tool arrives into.

## Open questions

- **The abstract does not say how indel calls were validated.** Given that indels are the artifact-richest class in any amplified library, the validation design is the single most important missing detail.
- Whether the 15 SNVs/year rate is uniform across neuron subtypes and brain regions is not addressed here.
- The peer-reviewed version should be ingested to replace this abstract-only summary.

## Related

- [[50-Notes/pta-inflection-point]] · [[luquette-2019-natcomm]] · [[pta]] · [[40-Topics/mosaic-variant-calling]]
