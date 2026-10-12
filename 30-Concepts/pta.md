---
type: concept
title: PTA (Primary Template Amplification)
aliases: [Primary Template-directed Amplification]
tags: [scWGA, isothermal, Φ29, ResolveServices, method]
created: 2026-05-11
updated: 2026-10-12
---

# PTA (Primary Template Amplification)

> Isothermal [[scwga]] method that combines Φ29 polymerase with exonuclease-resistant chain terminators to produce short amplicons that favour priming from the native template rather than from amplified copies, giving **~95% genome coverage**, high uniformity and high allelic balance — the current gold standard for high-coverage scDNA-seq ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]). It is used in [[10-Summaries/swanson-2025-daf-seq|scDAF-seq]] and current Walsh-lab brain mosaicism studies ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]; [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

> [!abstract] 한눈에
> PTA는 Φ29 polymerase에 exonuclease 내성 terminator를 더해 증폭 산물을 짧게 끊고, 복사본이 아니라 원래 template에서 주로 복제가 일어나게 하는 scWGA 방법이다 ([[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]). MDA보다 coverage, 균일도, allelic balance가 모두 좋아 고심도 scDNA-seq의 표준이 되었지만, 그래도 세포마다 수천 개의 위양성이 남아 PTA 전용 caller가 필요하다 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]).

## Definition

Standard MDA permits Φ29 polymerase to extend exponentially from amplified products, which compounds amplification bias (synthesis). PTA introduces **exonuclease-resistant terminators** (chain-terminator-modified bases) that cap extension at short length ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). The terminators are alpha-thio ddNTPs whose exonuclease-resistant bond stops the polymerase removing them ([[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]). Since Φ29 prefers longer amplicon products, this biases priming toward the **native (primary) template** rather than amplified copies ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]).

Mechanistically this approaches **quasi-linear amplification** while remaining isothermal (unsourced on the original page; verify). The result: coverage ~95% and high allelic balance ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]), with MAPD 0.1–0.3 (comparable to bulk WGS at 0.1) (unsourced on the original page; verify).

Typical metrics: 2.5–10.5 h reaction time, $5/cell (v2) to $20/cell (v1) (unsourced on the original page; see the cost caveat under Contested points). PTA is commercial via ResolveServices/BioSkryb ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]; [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]).

## Why it matters

PTA simultaneously fixed three of MDA's failure modes — coverage, uniformity, and allelic balance — without sacrificing Φ29's low error rate ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]). It is now the default scWGA method for any application needing accurate SNV detection at low VAF (synthesis).

## Versions, tools and assays built on PTA

**Chemistry versions**

- **PTA v1** vs **v2** — v2 lower cost, comparable performance (unsourced on the original page; verify).

**Analysis tools designed for PTA data**

- **SCAN2** — variant caller designed for PTA data (somatic indels and SNVs) ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]).
- **HiScanner** — sets its smallest copy-number bin from PTA's short dropout events, allowing 100 kb bins ([[10-Summaries/zhao-2025-hiscanner|HiScanner]]).

**Assays and applications**

- **Walsh lab brain mosaicism studies** — using naturally accumulated mutations (~2–4 per cell division) as lineage markers ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **scDAF-seq** — pairs PTA with PacBio long reads, because PTA generates partially overlapping amplicons from the same haplotype-strand which can be merged into long consensus reads; each unique deamination pattern is preserved across overlapping PTA amplicons ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Pre-implantation genetic screening** — a preprint cited in Shao 2025 reports the first method to reliably capture SNVs, aneuploid chromosomes and mtDNA from single embryonic cells ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Joint genome + transcriptome via PTA** — ResolveOME and SMART-PTA (preprints) leverage primary template-directed amplification to read a cell's transcriptome alongside its clonal genome, an alternative to the nucleosome-depletion route of DEFND-seq ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).

## Evidence and examples

- With ordinary ddNTPs only 15.0% of reads mapped, against 97.9% with irreversible terminators ([[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]).
- In a same-individual comparison, PTA-amplified neurons gave ~10× fewer infant-neuron sSNV calls than MDA (26 vs 282 per neuron) and showed no artifact signature B; MDA carried an estimated ~550 SNV and 136 indel single-strand-dropout artifacts per genome ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]).
- With PTA + SCAN2 the neuronal rate is 16.5 sSNVs/year and ≥3 indels/year ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]).
- scDAF-seq consensus-read assembly reached an N50 of 34.5 kb in a single cell using PTA + PacBio HiFi ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- PTA's short dropout events (~10³ bp vs ~10⁵ bp for MDA) allow 100 kb bins in HiScanner, which called 614 mostly sub-3 Mb CNAs in 65 PTA neurons and oligodendrocytes ([[10-Summaries/zhao-2025-hiscanner|HiScanner]]).
- DEFND-seq's coverage uniformity is benchmarked against PTA ([[10-Summaries/olsen-2025-defnd-seq|DEFND-seq]]).
- Capturing SNVs, aneuploid chromosomes and mtDNA from single donor-embryo cells (preprint reference in [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

## Contested points

- **Cost trajectory.** PTA v1 ($20/cell) was originally pricier than MDA REPLI-g (~$10/cell), but **PTA v2 (~$5/cell) is reported as among the cheapest commercial scWGA chemistries**, undercutting MDA and MALBAC (~$50/cell) ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]] Table 1; the table is not rendered in the source clipping — verify against the PDF). Older comparisons that frame PTA as "the accurate-but-expensive option" are stale.
- **Cell number.** PTA's relative advantage at very low cell numbers (≤96) is largest; at higher cell counts DLP+ may be preferable despite lower coverage (unsourced on the original page; verify).
- **Precision is not enough.** Even at 99.9% germline precision, ~2,785 false-positive calls remain per cell, so PTA-specific callers are still needed ([[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/scwga|scWGA]] — Amplifying the ~6 pg of DNA in one cell for whole-genome sequencing.
> - `concept` [[30-Concepts/mda|MDA]] — Direct predecessor: isothermal Φ29 strand-displacement amplification.
> - `concept` [[30-Concepts/daf-seq|DAF-seq]] — Single-molecule chromatin footprinting; its single-cell version uses PTA for amplification.
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Technologies that read the DNA of single cells.
> - `hub` [[40-Topics/whole-genome-amplification|Whole-genome amplification]] — The chemistries that bridge single-cell DNA to sequencing input.

## All sources on this page

> [!info]- 7 summaries cited here
> - [[10-Summaries/gonzalez-pena-2021-pnas|Gonzalez-Pena 2021]]
> - [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]
> - [[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]
> - [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
> - [[10-Summaries/zhao-2025-hiscanner|Zhao 2025]]
