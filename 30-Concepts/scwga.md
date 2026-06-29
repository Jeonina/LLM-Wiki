---
type: concept
title: scWGA (single-cell whole-genome amplification)
aliases: [single-cell whole-genome amplification, single-cell WGA]
tags: [single-cell, scDNA-seq, amplification, methods]
created: 2026-05-11
updated: 2026-05-11
---

# scWGA (single-cell whole-genome amplification)

> The set of biochemical methods that amplify the ~6 pg of DNA in a single diploid human cell by hundreds- to thousands-fold to produce enough material for whole-genome sequencing. The central technical challenge of [[30-Concepts/scdna-seq]] — every scWGA chemistry introduces some combination of amplification bias, allelic dropout, and polymerase error that must be controlled.

## Definition

A diploid human cell contains ~6 pg of DNA — far below the input requirement of any sequencing platform. scWGA bridges that gap. Three method categories ([[10-Summaries/gawad-2016-scgenome-review]], [[10-Summaries/shao-2025-scDNA-mosaicism-review]]):

1. **PCR-based amplification** — random or degenerate priming + PCR. Methods: [[dop-pcr]], PicoPLEX, [[malbac]].
2. **Isothermal amplification** — Φ29 polymerase + random hexamer primers; exponential strand-displacement amplification. Methods: [[mda]], [[pta]].
3. **Tn5 transposon-based amplification** — tagmentation inserts adapters into the genome before linear or PCR amplification. Methods: LIANTI, [[dlp-plus]], [[meta-cs]].

## Why it matters

scWGA is **unavoidable** for most single-cell DNA applications because the genome is 20–50× larger than the transcriptome and each locus has only two molecules per cell ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). The choice of scWGA method dominates downstream data quality — different applications have different error tolerances.

**Quality metrics**:

- **Coverage**: fraction of the genome with at least one read (DOP-PCR ~25%, MDA ~70%, PTA ~95%).
- **Uniformity** (MAPD — median absolute pairwise difference): how evenly the genome is amplified (lower = better).
- **Allelic balance**: ratio of read depth between the two alleles at heterozygous sites (≥50% required for SNV detection without dropout).
- **Cell throughput**: 1–96 (plate-based) vs >10,000 (DLP+ microfluidic).
- **Cost per cell**: $5 (PTA v2) to $50 (MALBAC); MDA REPLI-g ~$10 ([[10-Summaries/shao-2025-scDNA-mosaicism-review]] Table 1).
- **Time**: 2.5h (PicoPLEX) to 21h (DLP+).

## Variants and refinements

- See individual concept pages: [[dop-pcr]], [[malbac]], [[mda]], [[pta]], [[dlp-plus]], [[meta-cs]], PicoPLEX, LIANTI.
- **Hybrid PCR + isothermal**: MALBAC, PicoPLEX use limited isothermal preamplification then PCR.
- **Multi-omic integration**: scWGA chemistry is shared across some multi-omic methods that pair DNA with RNA (G&T-seq uses MDA-or-PCR after analyte separation).

## Contested points

- The PCR vs isothermal vs Tn5 tradeoff has no universal answer — application-dependent. CNV detection favors uniform (PCR/Tn5) methods; SNV detection favors high-coverage (isothermal) methods.
- Whether the Tn5 line of methods will displace MDA/PTA at scale — DLP+ already does at very low coverage; for high-coverage applications PTA still dominates.

## Examples

- DOP-PCR aneuploidy detection in human cleavage-stage embryos (49% aneuploid; [[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- PTA achieving ~95% coverage of single human neurons for lineage reconstruction ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- META-CS as the only single-cell duplex-sequencing method, achieving <2.4 × 10⁻⁸ error rate.

## Related

- [[30-Concepts/scdna-seq]]
- [[mda]], [[pta]], [[malbac]], [[dop-pcr]], [[dlp-plus]], [[meta-cs]]
- [[30-Concepts/duplex-sequencing]]
- [[40-Topics/whole-genome-amplification]]
- [[40-Topics/scdna-seq]]
