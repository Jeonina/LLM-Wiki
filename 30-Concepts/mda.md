---
type: concept
title: MDA (Multiple Displacement Amplification)
aliases: [Multiple Displacement Amplification, Φ29 amplification]
tags: [scWGA, isothermal, Φ29, method]
created: 2026-05-11
updated: 2026-10-07
---

# MDA (Multiple Displacement Amplification)

> Isothermal [[scwga]] method that uses Φ29 DNA polymerase with random hexamer primers to amplify the single-cell genome through strand-displacement at constant temperature. The first scWGA method to reach >70% genome coverage; the dominant method for ~15 years before [[pta]] superseded it for high-coverage applications.

## Definition

Φ29 polymerase has high processivity (>70 kb), low error rate (10⁻⁷–10⁻⁸ errors/base), and strand-displacement activity. Random hexamers prime the genome at thousands of sites; Φ29 extends from each primer, displacing downstream strands which become templates for further priming, producing exponential amplification at constant temperature (~30 °C). The chemistry was introduced in [[10-Summaries/dean-2002-mda|Dean et al. 2002]], who demonstrated <3-fold locus-to-locus bias vs. 4–6 orders of magnitude for PCR-based WGA — establishing MDA as the dominant scWGA approach for the subsequent 15+ years ([[10-Summaries/shao-2025-scDNA-mosaicism-review]], [[10-Summaries/gawad-2016-scgenome-review]]).

Typical metrics: coverage ~70–75%, MAPD low but variable, allelic balance low, ~11 h reaction time, $10/cell. Commercial kits widely available.

## Why it matters

MDA democratized [[40-Topics/scdna-seq]]: Φ29 polymerase enabled high-fidelity, high-coverage amplification at low cost. Most pre-2020 single-cell genome sequencing — including microbial dark matter discovery, the early human brain mosaicism studies, and the foundational cancer single-cell papers — used MDA.

**Limitations** (which motivated PTA and other successors):
- **Allelic imbalance and dropout** from exponential amplification — early-amplified loci dominate the read pool, suppressing the under-amplified allele.
- **Chimera formation** — strand displacement can join previously distant genome segments.
- **Coverage uniformity issues** especially at sub-Mb scales.

## Variants and refinements

- **Microfluidic MDA** (microliter → nanoliter volumes) — substantially improves uniformity and reduces contamination ([[10-Summaries/gawad-2016-scgenome-review]]).
- **MIDAS** (microwell displacement amplification system) — claimed near-bulk uniformity at single-cell scale.
- **Used in multi-omic methods**: G&T-seq applies MDA to the gDNA fraction after polyA separation ([[10-Summaries/vandereyken-2023-scmultiomics-review]]).
- **SCcaller** is the specific variant caller designed to handle MDA error patterns.

## Contested points

- Whether MDA is now obsolete for high-coverage applications given PTA — for cost-constrained studies MDA at $10/cell remains attractive vs PTA at $5–20/cell, but for low-VAF mosaicism PTA dominates.
- MDA's reproducibility across labs — uniformity is inconsistent, partly due to sensitivity to reaction conditions.

## Examples

- Original brain mosaicism studies (Lodato et al. 2015 — 84% coverage on neurons via MDA).
- Microbial dark-matter sequencing (TM7, TM6 phyla via microfluidic MDA).

## Added 2026-10-07

Haploid male X chromosomes revealed a median excess of 15 sSNVs and 3.7 indels per MDA X versus PTA from the same individual — single-strand-dropout artifacts that VAF-based filters cannot remove [[10-Summaries/luquette-2022-neuron-scan2-indels]]. Read-backed phasing (LiRA) flags MDA artifacts enriched for C>T and C>A, consistent with pre-amplification lesions [[10-Summaries/bohrson-2019-lira]].

Droplet MDA (dMDA) splits one cell's lysed DNA into ~50,000 Xdrop droplets so each droplet amplifies only one or a few fragments ([[10-Summaries/hard-2023-long-read-scwgs]]). In matched T-cell comparisons, 68.9% of reads fell in ≥200× regions after tube MDA versus 16.0% after dMDA, and genome-wide coverage SD was 2.46× higher for MDA ([[10-Summaries/hard-2023-long-read-scwgs]]). Partitioning removes inter-molecular chimeras in single-fragment droplets, but intramolecular chimeras remain: on average each HiFi read gave 2.7 separate alignments ([[10-Summaries/hard-2023-long-read-scwgs]]).


## Related

- [[10-Summaries/dean-2002-mda]] — founding paper
- [[scwga]]
- [[pta]] — direct successor.
- [[malbac]] — hybrid PCR/isothermal alternative.
- [[40-Topics/scdna-seq]]
- [[40-Topics/whole-genome-amplification]]
