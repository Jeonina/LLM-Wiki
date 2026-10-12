---
type: concept
title: MALBAC (Multiple Annealing and Loop-based Amplification Cycles)
aliases: [Multiple Annealing and Loop-based Amplification Cycles]
tags: [scWGA, hybrid, PCR-based, method]
created: 2026-05-11
updated: 2026-10-12
---

# MALBAC (Multiple Annealing and Loop-based Amplification Cycles)

> Hybrid [[scwga]] method that performs limited isothermal pre-amplification with random + common-sequence primers, generating amplicons that loop on themselves and prevent further pre-amplification; the loops then serve as templates for PCR. It trades coverage for uniformity against [[mda]] and was historically the go-to method for single-cell CNV detection ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]; [[10-Summaries/zong-2017-malbac-protocol|Zong 2017]]).

> [!abstract] 한눈에
> MALBAC은 짧은 등온 pre-amplification으로 만든 amplicon이 스스로 loop를 이루어 재증폭되지 않게 한 뒤 PCR로 증폭하는 hybrid scWGA 방법이다. MDA보다 coverage는 낮지만 균일도가 높아 single-cell CNV 검출에 오래 쓰였다 ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]; [[10-Summaries/zong-2017-malbac-protocol|Zong 2017]]).

## Definition

MALBAC primers carry a common sequence at one end and random nucleotides at the other ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]). The common sequence is 27 nt of G/A/T only, followed by eight variable 3′ nucleotides ([[10-Summaries/zong-2017-malbac-protocol|Zong 2017]]). After isothermal random priming and extension, the common-sequence ends of the resulting amplicons are complementary, so they fold into hairpin loops ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]). Looped amplicons cannot be re-primed as templates, which limits the bias from repeated amplification of early-amplified loci ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]). Five quasi-linear looping cycles (0/65/94/58 °C, Bst polymerase) precede standard PCR on the looped amplicons ([[10-Summaries/zong-2017-malbac-protocol|Zong 2017]]).

Typical metrics: coverage 55–60%, uniformity better than MDA, allelic balance moderate, ~4 h reaction time, $50/cell.

## Why it matters

- **Uniformity beats coverage for CNV.** For single-cell CNV detection, MALBAC's uniformity outweighs its lower coverage, because read-depth-based CNV callers need uniform sampling, not deep per-base coverage ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]).
- **It carried early cancer studies.** Many early single-cell cancer studies used MALBAC for clonal-evolution mapping ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]).
- **It has a narrowing niche.** It is now largely superseded by [[pta]] for high-coverage applications, but remains in use for cost-sensitive CNV-only workflows.

## Variants

- **Microfluidic MALBAC** — improved uniformity over tube-volume reactions ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]).

## Evidence and examples

- Used historically for single-cell CNV phylogenetics in breast cancer and CLL studies (cited in [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]). Navin et al. 2011 predates MALBAC and used single-nucleus sequencing ([[10-Summaries/navin-2011-sns-tumor-evolution|Navin 2011]]).
- Used to capture SNVs in circulating tumour cells with high uniformity.
- The Quake group's MDA-vs-MALBAC benchmark at the *E. coli* single-cell level found microfluidic-volume MDA and MALBAC had comparable bias; in microliter volumes MDA bias depended on gain while MALBAC was gain-independent ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]). The conclusion was that method choice should match the specific question ([[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]).

## Contested points

- **Coverage figures disagree.** The MALBAC chapter reports ~85% (up to 93%) genome coverage at ~25× against 72% for MDA ([[10-Summaries/zong-2017-malbac-protocol|Zong 2017]]), while this page's coverage figure (55–60%, from a review) is lower; depth and definition may differ.
- **ADO may be understated.** MALBAC's ADO rate of ~21% was sometimes calculated only on covered sites, masking true false-negative rates.

## Related

> [!cards]
> - `concept` [[30-Concepts/scwga|scWGA]] — Biochemical methods that amplify the ~6 pg of DNA in one cell for whole-genome sequencing.
> - `concept` [[30-Concepts/mda|MDA]] — Pure-isothermal Φ29 alternative with higher coverage but lower uniformity.
> - `concept` [[30-Concepts/pta|PTA]] — Terminator-limited isothermal amplification that largely supersedes MALBAC for high coverage.
> - `concept` [[30-Concepts/dop-pcr|DOP-PCR]] — Adjacent PCR-based method; PicoPLEX is another.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — Technologies that interrogate the DNA of single cells.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]
> - [[10-Summaries/navin-2011-sns-tumor-evolution|Navin 2011]]
> - [[10-Summaries/zong-2017-malbac-protocol|Zong 2017]]
