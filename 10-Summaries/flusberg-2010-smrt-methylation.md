---
type: summary
title: "Flusberg et al. 2010 — Direct detection of DNA methylation during single-molecule, real-time sequencing"
source: "[[00-Sources/papers/Direct detection of DNA methylation during single-molecule, real-time sequencing]]"
source_kind: paper
author: "Benjamin A. Flusberg, Dale R. Webster, Jessica H. Lee, Kevin J. Travers, Eric C. Olivares, Tyson A. Clark, Jonas Korlach, Stephen W. Turner (corresponding)"
published: 2010-05-09
ingested: 2026-08-10
doi: "10.1038/nmeth.1459"
journal: "Nature Methods"
tags: [SMRT, PacBio, polymerase-kinetics, IPD, bisulfite-free, 5hmC, 6mA, founding-method, single-molecule, long-read]
entities: []
concepts: ["[[pacbio]]", "[[smrt-tag]]", "[[5hmc]]", "[[bisulfite-sequencing]]", "[[highly-repetitive-regions]]", "[[allele-specific-methylation]]"]
topics: ["[[dna-methylation]]", "[[long-read-sequencing]]"]
---

**Citation:** Flusberg et al. (2010) — *Direct detection of DNA methylation during single-molecule, real-time sequencing* — *Nature Methods* 7, 461–465. [DOI](https://doi.org/10.1038/nmeth.1459)

# Flusberg 2010 — methylation from polymerase kinetics

> Base modifications slow the polymerase. In SMRT sequencing the arrival time and duration of each fluorescence pulse are already measured, so **methylation comes for free with the sequence** — no bisulfite, no chemical conversion, no separate library. And because the kinetic signatures differ between modifications, 5mC and 5hmC can in principle be told apart, which bisulfite cannot do at all.

## Key claims

- Two kinetic observables per incorporation: **IPD** (interpulse duration — nucleotide binding and translocation) and **pulse width** (everything after binding through fluorophore release). Both are intrinsic to SMRT sequencing and measuring them "does not adversely affect determination of primary DNA sequence."
- The bisulfite drawbacks this replaces, stated explicitly: costly and slow sample prep; harsh conditions **degrade DNA**; reduced sequence complexity constrains PCR primer design and complicates reference alignment; and — the fundamental one — **bisulfite cannot discriminate C from 5mC from 5hmC**.
- On synthetic templates with modifications spaced ≥11 bases apart, all three of 6mA, 5mC and 5hmC produce clear kinetic excursions. **6mA gives the strongest signal**: IPD ratios of 5–6× directly opposite the modified base, plausibly because the N6 position participates in base-pairing hydrogen bonds.
- The kinetic footprint is **spread over multiple positions, not just the modified base** — consistent with the modified base contacting the polymerase for several bases before and after occupying the active site. 5mC shows IPD increases 2, 3 and 6 bases downstream; 5hmC shows 2 and 6 but not 3; pulse-width excursions are more pronounced for 5hmC than 5mC.
- **Kinetic signatures are sequence-context-dependent** — the two methylated positions in otherwise identical templates gave different IPD patterns, and local sequence was the only difference. This is a general property, not an artifact.
- PCA over IPD and pulse width at multiple positions **separates C, 5mC and 5hmC** at the same site — the first demonstration that the three cytosine states are distinguishable during real-time sequencing.
- **Circular consensus sequencing rescues sensitivity.** Hairpin-adapted circular templates let a strand-displacing polymerase read the same molecule repeatedly; repeated IPD measurements follow a gamma distribution narrower than the underlying exponential. For 6mA the ROC area rises 0.80 → 0.92 → 0.96 after 1, 3 and 5 subreads; after five subreads **>85% of 6mA bases detected at ~5% false positive rate** (five subreads of a 199-base template ≈ 1,000 bases of read length).
- Genomic validation: a *C. elegans* fosmid grown in *dam*⁺ *E. coli* vs the same sample after whole-genome amplification (which erases modifications). GATC positions show ~4× higher mean IPD in *dam*⁺; 4-mer context heatmaps are otherwise highly similar between the two, with GATC the notable exception.
- Honest limitation: 6mA works at single-molecule resolution; **"for mC and hmC, enhancements of kinetic sensitivity will likely be required."**

## Methods / evidence

Synthetic 199-base circular templates identical except for modification status, mass-spectrometry-verified; *dam*⁺ genomic DNA with a WGA-erased matched control; ROC analysis over subread counts; PCA to combine multi-position kinetic features. The WGA control is the clean part of the design — same molecules, modifications removed, everything else constant.

Scale caveat stated plainly: arrays of 3,000 ZMWs on a prototype instrument, with commercial versions promising ~100× throughput.

## Surprising or load-bearing bits

- **This is the origin of modification-aware long-read sequencing**, the paradigm that now dominates: measure the physical signal the polymerase (or pore) already produces and infer the base modification from it. The nanopore equivalent arrives seven years later (Simpson 2017 (nanopore methylation) *(not bookmarked)*); today's PacBio 5mC and ONT modified-basecalling models are direct descendants.
- The two capabilities it opens are the ones bisulfite structurally cannot provide:
  1. **Methylation in repetitive regions** — the authors note "a substantial fraction of mC residues resides" there, and long reads plus no complexity reduction make it accessible. Connects to [[highly-repetitive-regions]] and [[transposable-elements]].
  2. **Phasing of methylation status between genomic positions** on the same molecule — single-molecule co-occurrence, which bulk bisulfite averages away. That is the same measurement axis [[single-molecule-footprinting]] methods ([[andrewb-2020-science|Fiber-seq]], [[shipony-2020-smac|SMAC]]) exploit for accessibility.
- **Context-dependence of the kinetic signature is the durable technical constraint.** It is why modification calling became a machine-learning problem trained per-context rather than a threshold rule, and why per-call accuracy still varies by sequence context in current basecallers.
- The 5mC/5hmC separation demonstrated here on synthetics was a genuine first, and it is the same discrimination that [[chen-2025-sctaps-sccaps-plus|scTAPS/scCAPS+]] achieves by enzymatic chemistry rather than kinetics. Two entirely different routes to the problem [[tahiliani-2009-tet1-5hmc|Tahiliani 2009]] created.
- WGA erasing methylation is used here as a *feature* (the control), but it is the same fact that makes amplification-based single-cell methods epigenetically blind — relevant to why [[dlp-plus]] and direct-tagmentation approaches matter for joint genome–epigenome work.

## Concepts touched

- [[pacbio]] — this is the founding source for kinetic modification detection on the platform.
- [[5hmc]] — first demonstration of sequencing-based C/5mC/5hmC discrimination.
- [[bisulfite-sequencing]] — the limitations enumerated here define what bisulfite-free methods exist to fix.
- [[smrt-tag]] — modern low-input SMRT applications inherit this readout.

## Connections to other sources

- Nanopore counterpart: Simpson 2017 (nanopore methylation) *(not bookmarked)*; long-read methylation computation reviewed in [[fu-2025-longread-methylation]] and [[liu-2025-long-read-epigenome-review]].
- Chemistry-based route to the same discrimination: [[chen-2025-sctaps-sccaps-plus]].
- Single-molecule co-occurrence measurement: [[andrewb-2020-science]], [[shipony-2020-smac]], [[lee-2020-nanonome]], [[altemose-2022-dimelo-seq]].
- Discovery context: [[tahiliani-2009-tet1-5hmc]] (5hmC exists, and no tool distinguishes it) — this paper is one of the first answers.
- Low-input SMRT for single cells: [[nanda-2024-smrt-tag]].

## Open questions

- **Single-cell** kinetic methylation detection was never achieved by this route — the sensitivity gap for 5mC/5hmC that the paper flags in 2010 is still why single-cell methylomes use conversion chemistry rather than kinetics.
- Whether kinetic detection of 5hmC at genomic (not synthetic-template) scale is achievable is unresolved in this corpus.
- De novo modification detection without a matched unmodified control was proposed, not demonstrated.

## Related

- Simpson 2017 (nanopore methylation) *(not bookmarked)* · [[pacbio]] · [[chen-2025-sctaps-sccaps-plus]] · [[long-read-sequencing]]
