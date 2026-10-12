---
type: concept
title: Allele dropout
aliases: [ADO, allelic dropout]
tags: [single-cell, scWGA, amplification-bias]
created: 2026-05-12
updated: 2026-10-12
---

# Allele dropout (ADO)

> A failure mode of single-cell whole-genome amplification (scWGA) in which one of the two parental alleles at a heterozygous locus fails to amplify, so a heterozygous variant appears homozygous in the sequencing data ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

> [!abstract] 한눈에
> Allele dropout은 single-cell 증폭 과정에서 heterozygous 위치의 두 allele 중 하나가 증폭되지 않아 변이가 homozygous처럼 보이는 현상이고, 실측 비율은 수 %에서 30% 안팎까지 넓게 퍼져 있다 ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]; [[10-Summaries/pellegrino-2018-tapestri|Pellegrino 2018]]). 증폭 화학(MDA보다 PTA)과 입력 copy 수로 줄일 수 있고, 남은 dropout은 caller와 계통 추론 모델이 명시적 변수로 다룬다 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/kang-2022-sieve|SIEVE]]; [[10-Summaries/kozlov-2022-cellphy|CellPhy]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [모자이크 변이 검출력 시뮬레이터](../60-Explainers/mosaic-variant-calling.html)
<!-- /explainer-links -->

## Definition

ADO arises during the earliest rounds of amplification, when one strand or one parental molecule fails to template polymerase extension; once the bias is established, it propagates through all subsequent cycles. A dropped allele gives a heterozygous site a 50% chance of a false-negative call ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

## Why it matters

- ADO is the primary source of false-negative SNV calls in scDNA-seq; Shao 2025 lists allelic dropout among scWGA errors with a 50% chance of a false negative ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- ADO rates in current single-cell data can be 50% or higher ([[10-Summaries/zhang-2025-scistree2|ScisTree2]]).
- ADO directly limits clone detection: **ADO >0.3 or fewer than 10 mutations per sample causes clone-number underestimation** ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).
- For copy-number calling, ADO looks like a single-copy loss in read depth, so the usable CNA resolution depends on the amplification chemistry ([[10-Summaries/zhao-2025-hiscanner|HiScanner]]).
- In long-read single-cell WGS, allelic dropout remains the limiting factor on sensitivity ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).

## Measuring ADO

| Approach | Example | What it does | Source |
|---|---|---|---|
| Several independent assays | [[10-Summaries/gawad-2014-all-clonal-origins\|Gawad 2014]] | Measures ADO four ways rather than assuming a literature value: TaqMan genotyping of 46 common-heterozygous loci, targeted resequencing of 96 such loci, wild-type-allele loss at called mutations, and the clone-inference model's own estimate of intraclonal dropout | ([[10-Summaries/gawad-2014-all-clonal-origins\|Gawad 2014]]) |
| Per-run spike-in | [[10-Summaries/pellegrino-2018-tapestri\|Pellegrino 2018]] | Droplet targeted scDNA-seq measures ADO in each run from a ~1% Raji spike-in at known heterozygous variants | ([[10-Summaries/pellegrino-2018-tapestri\|Pellegrino 2018]]) |
| Read-backed phasing | [[10-Summaries/bohrson-2019-lira\|LiRA]] | One read spanning a candidate site and a linked germline heterozygous SNP that shows the null haplotype suffices to call a mutation absent | ([[10-Summaries/bohrson-2019-lira\|LiRA]]) |
| BAF HMM at germline heterozygous SNPs | [[10-Summaries/zhao-2025-hiscanner\|HiScanner]] | A two-state HMM on BAF finds dropout events; the 95th percentile of their sizes sets the minimum CNA bin size | ([[10-Summaries/zhao-2025-hiscanner\|HiScanner]]) |
| EM over amplicon data | [[10-Summaries/sollier-2023-compass\|COMPASS]] | Infers per-variant dropout rates by EM in amplicon data | ([[10-Summaries/sollier-2023-compass\|COMPASS]]) |
| Coverage-independent chromatin readout | [[10-Summaries/pott-2017-elife\|scNOMe-seq]] | NOMe-seq recovers DNA whether or not it is accessible, so it can tell closed chromatin from read loss, which count-based scATAC-seq cannot | ([[10-Summaries/pott-2017-elife\|Pott 2017]]) |

## Modelling ADO in callers and phylogenies

| Tool | How ADO enters the model | Source |
|---|---|---|
| [[30-Concepts/scout-variant-caller\|SCOUT]] | Flags potential ADO loci based on local context | — |
| [[10-Summaries/kang-2022-sieve\|SIEVE]] | A hidden number-of-sequenced-alleles variable, identifiable only through coverage | ([[10-Summaries/kang-2022-sieve\|SIEVE]]) |
| [[10-Summaries/kozlov-2022-cellphy\|CellPhy]] | ADO rate (δ) is a free parameter, separate from the amplification/sequencing error rate (ε), estimated from the data | ([[10-Summaries/kozlov-2022-cellphy\|CellPhy]]) |
| [[10-Summaries/zhang-2025-scistree2\|ScisTree2]] | Implicitly, by taking per-cell genotype posterior probabilities as input | ([[10-Summaries/zhang-2025-scistree2\|ScisTree2]]) |
| [[10-Summaries/sollier-2023-compass\|COMPASS]] | Per-variant dropout rates inferred by EM | ([[10-Summaries/sollier-2023-compass\|COMPASS]]) |
| [[10-Summaries/leib-2026-dnt\|DNT]] (diploid DNA language model) | Encodes each heterozygous site as one allele-pair token, so single-cell ADO would enter as a false homozygous token; untested (synthesis) | ([[10-Summaries/leib-2026-dnt\|DNT]]) |

## Reducing ADO

- **Amplification chemistry.** MDA suffers high ADO rates; PTA's quasi-linear amplification reduces it substantially ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). See [[30-Concepts/mda]], [[30-Concepts/pta]] and [[30-Concepts/scwga]].
- **Even coverage is not enough.** LIANTI amplifies the genome evenly yet shows MDA-like allelic skew, whereas PTA greatly reduces dropout and skew ([[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]).
- **Input copy number.** Input copy number is the most direct lever on ADO: G2/M-sorted nuclei give four template copies per locus ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]).
- **Multi-omic sample handling.** The G&T-seq developers state that physically separating mRNA from gDNA "may contribute further to the problem of allelic dropout" ([[10-Summaries/macaulay-2016-gt-seq-protocol|Macaulay 2016]]).

## Evidence and examples

**Measured rates**

- In Gawad 2014, TaqMan genotyping and wild-type-allele loss concurred at 23–24% median ADO; resequencing read higher at 33%; after a 30% ADO filter the median fell to 20% ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).
- Primary patient samples ran modestly above the 15.6% ADO of an LCL control ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).
- G2/M-sorted nuclei dropped ADO to **9.73 ± 2.19%**, versus 7–46% in prior MDA work ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]).
- Droplet targeted scDNA-seq measured ADO at 8.7% ± 1.1% across nine heterozygous variants in six runs ([[10-Summaries/pellegrino-2018-tapestri|Pellegrino 2018]]).
- SIEVE estimated ADO rates on real data of 0.20 (CRC28 scWGS), 0.05 (TNBC16) and 0.10 (CRC48) ([[10-Summaries/kang-2022-sieve|SIEVE]]).
- G&T-seq saw no megabase-scale dropouts in normal cells ([[10-Summaries/macaulay-2016-gt-seq-protocol|Macaulay 2016]]).

**Dropout size and its effect on other calls**

- Mean dropout size was ~10³ bp in PTA versus ~10⁵ bp in MDA ([[10-Summaries/zhao-2025-hiscanner|HiScanner]]).
- In long-read single-cell WGS, sensitivity was 0.17 for SNVs and just above 0.20 for SVs, even though precision was high ([[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]).
- Read-backed absence calls are cheap because 98% of linked germline pairs show only concordant reads ([[10-Summaries/bohrson-2019-lira|LiRA]]).

**How well models recover ADO**

- SIEVE's ADO-calling F1 was 0.86–0.93 at medium/high simulated coverage quality but 0.10 at low quality, described as typical of current scDNA-seq ([[10-Summaries/kang-2022-sieve|SIEVE]]).
- In CellPhy simulations, ADO estimates were more variable than error estimates and tended to come out low (MSE 0.002–0.02); on clonal colonies with no amplification, the estimated ADO was zero, as it should be ([[10-Summaries/kozlov-2022-cellphy|CellPhy]]).
- ScisTree2 was robust to assumed ADO rates on HGSOC DLP+ data ([[10-Summaries/zhang-2025-scistree2|ScisTree2]]).

## Contested points

- **How high is ADO?** ScisTree2's authors put current ADO at 50% or higher ([[10-Summaries/zhang-2025-scistree2|ScisTree2]]), while direct measurements in this wiki range from 5% to 33% ([[10-Summaries/kang-2022-sieve|SIEVE]]; [[10-Summaries/pellegrino-2018-tapestri|Pellegrino 2018]]; [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]); the figures come from different chemistries and estimators, so they are not directly comparable (synthesis).
- **False negatives versus false positives.** ADO drives false negatives, but the Shao 2025 review names false positives as the dominant scWGA problem ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]); which error class matters more depends on the downstream question (synthesis).
- **Model estimates of ADO may be biased low.** CellPhy's simulated ADO estimates tended to come out low ([[10-Summaries/kozlov-2022-cellphy|CellPhy]]), and SIEVE's ADO calling collapses at low coverage quality ([[10-Summaries/kang-2022-sieve|SIEVE]]), so model-reported ADO rates on real data deserve caution (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scwga|scWGA]] — Biochemical methods that amplify the ~6 pg of DNA in a single cell; where ADO originates.
> - `concept` [[30-Concepts/mda|MDA]] — Isothermal Φ29 strand-displacement amplification; high ADO.
> - `concept` [[30-Concepts/pta|PTA]] — Φ29 with chain terminators for quasi-linear amplification; reduced ADO.
> - `concept` [[30-Concepts/scout-variant-caller|SCOUT]] — Single-cell SNV caller that flags potential ADO loci from local context.
> - `hub` [[40-Topics/whole-genome-amplification|Whole-genome amplification]] — The amplification chemistries and the artefacts they introduce.

## All sources on this page

> [!info]- 15 summaries cited here
> - [[10-Summaries/bohrson-2019-lira|Bohrson 2019]]
> - [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]
> - [[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]
> - [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]
> - [[10-Summaries/kang-2022-sieve|Kang 2022]]
> - [[10-Summaries/kozlov-2022-cellphy|Kozlov 2022]]
> - [[10-Summaries/leib-2026-dnt|DNT 2026]]
> - [[10-Summaries/macaulay-2016-gt-seq-protocol|Macaulay 2016]]
> - [[10-Summaries/pellegrino-2018-tapestri|Pellegrino 2018]]
> - [[10-Summaries/pott-2017-elife|Pott 2017]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/sollier-2023-compass|Sollier 2023]]
> - [[10-Summaries/wang-2014-nuc-seq|Wang 2014]]
> - [[10-Summaries/zhang-2025-scistree2|Zhang 2025]]
> - [[10-Summaries/zhao-2025-hiscanner|Zhao 2025]]
