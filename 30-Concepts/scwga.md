---
type: concept
title: scWGA (single-cell whole-genome amplification)
aliases: [single-cell whole-genome amplification, single-cell WGA]
tags: [single-cell, scDNA-seq, amplification, methods]
created: 2026-05-11
updated: 2026-10-12
---

# scWGA (single-cell whole-genome amplification)

> The set of biochemical methods that amplify the ~6 pg of DNA in a single diploid human cell by hundreds- to thousands-fold to produce enough material for whole-genome sequencing. The central technical challenge of [[40-Topics/scdna-seq]] — every scWGA chemistry introduces some combination of amplification bias, allelic dropout, and polymerase error that must be controlled ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

> [!abstract] 한눈에
> scWGA는 한 세포에 든 약 6 pg의 DNA를 시퀀싱할 수 있을 만큼 증폭하는 방법들이며, PCR 기반, isothermal, Tn5 기반의 세 갈래로 나뉜다 ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). 어떤 방법을 고르느냐가 coverage, 균일도, allelic balance를 좌우하므로 CNV와 SNV 중 무엇을 볼지에 따라 답이 달라진다 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 DNA 시퀀싱 입문](../60-Explainers/scdna-seq.html)
>
> [단일세포 WGA 시뮬레이터](../60-Explainers/wga-simulator.html)
<!-- /explainer-links -->

## Definition

A diploid human cell contains ~6 pg of DNA — far below the input requirement of any sequencing platform; scWGA bridges that gap (synthesis). There are three method categories ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]):

1. **PCR-based amplification** — random or degenerate priming + PCR. Methods: [[dop-pcr]], PicoPLEX, [[malbac]].
2. **Isothermal amplification** — Φ29 polymerase + random hexamer primers; exponential strand-displacement amplification. Methods: [[mda]], [[pta]].
3. **Tn5 transposon-based amplification** — tagmentation inserts adapters into the genome before linear or PCR amplification. Methods: LIANTI, [[dlp-plus]], [[meta-cs]].

## Why it matters

- scWGA is **unavoidable** for most single-cell DNA applications because the genome is 20–50× larger than the transcriptome and each locus has only two molecules per cell ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- The choice of scWGA method dominates downstream data quality, and different applications have different error tolerances ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

## Methods

| Method | Category | Genome coverage | Notes | Source |
|---|---|---|---|---|
| [[dop-pcr\|DOP-PCR]] | PCR-based | ~25% | Cost ~$20 | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| PicoPLEX | PCR-based (hybrid: limited isothermal preamplification, then PCR) | 35–45% | Fastest protocol, 2.5 h | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| [[malbac\|MALBAC]] | PCR-based (hybrid: limited isothermal preamplification, then PCR) | 55–60% | Cost up to $50 | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| [[mda\|MDA]] | Isothermal (Φ29) | ~70% | REPLI-g ~$10 | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| [[pta\|PTA]] | Isothermal (Φ29 + terminators) | ~95% | PTA v2 ~$5 | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| LIANTI | Tn5-based linear amplification | 80–85% | — | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| [[dlp-plus\|DLP+]] | Tn5-based, microfluidic | Very low per cell | >10,000 cells; 21 h | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| [[meta-cs\|META-CS]] | Tn5-based duplex | — | The only single-cell duplex-sequencing method | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |

Costs and times come from [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]] Table 1; the table is not rendered in the source clipping — verify against the PDF.

**Multi-omic integration.** scWGA chemistry is shared across some multi-omic methods that pair DNA with RNA: G&T-seq uses MDA-or-PCR after analyte separation (synthesis).

## Quality metrics

- **Coverage**: fraction of the genome with at least one read (DOP-PCR ~25%, MDA ~70%, PTA ~95%) ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Uniformity** (MAPD — median absolute pairwise difference): how evenly the genome is amplified (lower = better) (synthesis).
- **Allelic balance**: ratio of read depth between the two alleles at heterozygous sites (≥50% required for SNV detection without dropout) (synthesis).
- **Cell throughput**: 1–96 (plate-based) vs >10,000 (DLP+ microfluidic) ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Cost per cell**: $5 (PTA v2) to $50 (MALBAC); MDA REPLI-g ~$10; DOP-PCR ~$20 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]] Table 1; unverified against the PDF).
- **Time**: 2.5 h (PicoPLEX) to 21 h (DLP+) ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]] Table 1; unverified against the PDF).

## Evidence and examples

- DOP-PCR detected aneuploidy in human cleavage-stage embryos (49% aneuploid) ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- PTA achieves ~95% coverage of single human neurons for lineage reconstruction ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- META-CS, the only single-cell duplex-sequencing method, reaches a false-positive rate below 2.4 × 10⁻⁸ ([[10-Summaries/xing-2021-meta-cs|Xing 2021]]).

## Contested points

- The PCR vs isothermal vs Tn5 tradeoff has no universal answer — it is application-dependent: CNV detection favors uniform (PCR/Tn5) methods, SNV detection favors high-coverage (isothermal) methods (synthesis).
- Whether the Tn5 line of methods will displace MDA/PTA at scale is open: DLP+ already does at very low coverage, while for high-coverage applications PTA still dominates (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/mda|MDA]] — Φ29 strand-displacement amplification; medium coverage, low allelic balance.
> - `concept` [[30-Concepts/pta|PTA]] — Φ29 with terminators; ~95% coverage and the current gold standard.
> - `concept` [[30-Concepts/malbac|MALBAC]] — Looped-amplicon isothermal preamplification followed by PCR; historically the go-to for single-cell CNV.
> - `concept` [[30-Concepts/dop-pcr|DOP-PCR]] — Degenerate-primer PCR; low coverage, uniform, cheap.
> - `concept` [[30-Concepts/dlp-plus|DLP+]] — Tn5 microfluidic library prep for >10,000 cells at shallow depth.
> - `concept` [[30-Concepts/meta-cs|META-CS]] — Tn5-based single-cell duplex sequencing.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — The single-cell DNA sequencing field as a whole.
> - `hub` [[40-Topics/whole-genome-amplification|Whole-genome amplification]] — scWGA chemistries and their error profiles.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — High-fidelity sequencing of both DNA strands.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/xing-2021-meta-cs|Xing 2021]]
