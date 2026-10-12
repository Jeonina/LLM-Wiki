---
type: concept
title: MDA (Multiple Displacement Amplification)
aliases: [Multiple Displacement Amplification, Φ29 amplification]
tags: [scWGA, isothermal, Φ29, method]
created: 2026-05-11
updated: 2026-10-12
---

# MDA (Multiple Displacement Amplification)

> Isothermal [[scwga]] method that uses Φ29 DNA polymerase with random hexamer primers to amplify the single-cell genome through strand-displacement at constant temperature. The first scWGA method to reach >70% genome coverage; the dominant method for ~15 years before [[pta]] superseded it for high-coverage applications ([[10-Summaries/dean-2002-mda|Dean 2002]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

> [!abstract] 한눈에
> MDA는 Φ29 polymerase와 random hexamer로 단일 세포 유전체를 일정한 온도에서 strand-displacement 방식으로 증폭하는 scWGA 방법이며, PTA가 나오기 전까지 15년 넘게 주류였다 ([[10-Summaries/dean-2002-mda|Dean 2002]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). 지수적 증폭 때문에 allelic imbalance, dropout, chimera, 증폭 artifact가 생기는 것이 핵심 한계다 ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]; [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 WGA 시뮬레이터](../60-Explainers/wga-simulator.html)
<!-- /explainer-links -->

## Definition

Φ29 polymerase has high processivity (>70 kb), low error rate (10⁻⁷–10⁻⁸ errors/base), and strand-displacement activity. Random hexamers prime the genome at thousands of sites; Φ29 extends from each primer, displacing downstream strands which become templates for further priming, producing exponential amplification at constant temperature (~30 °C). The chemistry was introduced by Dean et al. 2002, who demonstrated <3-fold locus-to-locus bias vs. 4–6 orders of magnitude for PCR-based WGA ([[10-Summaries/dean-2002-mda|Dean 2002]]) — establishing MDA as the dominant scWGA approach for the subsequent 15+ years ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]).

Typical metrics: coverage ~70–75%, MAPD low but variable, allelic balance low, ~11 h reaction time, $10/cell. Commercial kits widely available.

## Why it matters

MDA democratized [[40-Topics/scdna-seq]]: Φ29 polymerase enabled high-fidelity, high-coverage amplification at low cost. Most pre-2020 single-cell genome sequencing — including microbial dark matter discovery, the early human brain mosaicism studies, and the foundational cancer single-cell papers — used MDA.

### Limitations

These motivated PTA and other successors:

- **Allelic imbalance and dropout** from exponential amplification — early-amplified loci dominate the read pool, suppressing the under-amplified allele.
- **Chimera formation** — strand displacement can join previously distant genome segments.
- **Coverage uniformity issues**, especially at sub-Mb scales.
- **Amplification artifacts that look like mutations** — single-strand-dropout sSNVs and indels that VAF-based filters cannot remove ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]), and C>T / C>A artifacts consistent with pre-amplification lesions ([[10-Summaries/bohrson-2019-lira|LiRA]]).

## Variants and refinements

- **Microfluidic MDA** (microliter → nanoliter volumes) — substantially improves uniformity and reduces contamination ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]).
- **MIDAS** (microwell displacement amplification system) — claimed near-bulk uniformity at single-cell scale.
- **Droplet MDA (dMDA)** — splits one cell's lysed DNA into ~50,000 Xdrop droplets so each droplet amplifies only one or a few fragments ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).
- **Use in multi-omic methods** — G&T-seq applies MDA to the gDNA fraction after polyA separation ([[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]).
- **Dedicated variant calling** — SCcaller is the variant caller designed to handle MDA error patterns.

## Evidence and examples

- Original brain mosaicism studies (Lodato et al. 2015 — 84% coverage on neurons via MDA).
- Microbial dark-matter sequencing (TM7, TM6 phyla via microfluidic MDA).
- Haploid male X chromosomes revealed a median excess of 15 sSNVs and 3.7 indels per MDA X versus PTA from the same individual ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]).
- Read-backed phasing (LiRA) flags MDA artifacts enriched for C>T and C>A ([[10-Summaries/bohrson-2019-lira|LiRA]]).
- In matched T-cell comparisons, 68.9% of reads fell in ≥200× regions after tube MDA versus 16.0% after dMDA, and genome-wide coverage SD was 2.46× higher for MDA ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).
- Partitioning in dMDA removes inter-molecular chimeras in single-fragment droplets, but intramolecular chimeras remain: on average each HiFi read gave 2.7 separate alignments ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).

## Contested points

- **Is MDA obsolete for high coverage?** For cost-constrained studies MDA at $10/cell remains attractive vs PTA at $5–20/cell, but for low-VAF mosaicism PTA dominates.
- **Reproducibility across labs.** Uniformity is inconsistent, partly due to sensitivity to reaction conditions.

## Related

> [!cards]
> - `concept` [[30-Concepts/scwga|scWGA]] — Biochemical methods that amplify the ~6 pg of DNA in one cell for whole-genome sequencing.
> - `concept` [[30-Concepts/pta|PTA]] — Direct successor; terminator-limited amplification with ~95% coverage.
> - `concept` [[30-Concepts/malbac|MALBAC]] — Hybrid PCR/isothermal alternative with better uniformity.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — Technologies that interrogate the DNA of single cells.
> - `hub` [[40-Topics/whole-genome-amplification|Whole-genome amplification]] — Methods that bridge single-cell DNA to sequencing input requirements.

Founding paper: [[10-Summaries/dean-2002-mda|Dean 2002]].

## All sources on this page

> [!info]- 7 summaries cited here
> - [[10-Summaries/bohrson-2019-lira|Bohrson 2019]]
> - [[10-Summaries/dean-2002-mda|Dean 2002]]
> - [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]
> - [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]
> - [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/vandereyken-2023-scmultiomics-review|Vandereyken 2023]]
