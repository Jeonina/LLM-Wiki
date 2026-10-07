---
type: concept
title: PTA (Primary Template Amplification)
aliases: [Primary Template-directed Amplification]
tags: [scWGA, isothermal, Φ29, ResolveServices, method]
created: 2026-05-11
updated: 2026-10-07
---

# PTA (Primary Template Amplification)

> Isothermal [[scwga]] method that combines Φ29 polymerase with exonuclease-resistant chain terminators to produce short amplicons that favor priming from the native template rather than from amplified copies. Result: **~95% genome coverage**, high uniformity, and high allelic balance — the current gold standard for high-coverage scDNA-seq, used in [[10-Summaries/swanson-2025-daf-seq|scDAF-seq]] and current Walsh-lab brain mosaicism studies.

## Definition

Standard MDA permits Φ29 polymerase to extend exponentially from amplified products, which compounds amplification bias. PTA introduces **exonuclease-resistant terminators** (chain-terminator-modified bases) that cap extension at short length ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]). Since Φ29 prefers longer amplicon products, this biases priming toward the **native (primary) template** rather than amplified copies.

Mechanistically this approaches **quasi-linear amplification** while remaining isothermal. The result: coverage ~95%, MAPD 0.1–0.3 (comparable to bulk WGS at 0.1), allelic balance high.

Typical metrics: 2.5–10.5 h reaction time, $5/cell (v2) to $20/cell (v1). Commercial via ResolveServices/BioSkryb.

## Why it matters

PTA simultaneously fixed three of MDA's failure modes — coverage, uniformity, and allelic balance — without sacrificing Φ29's low error rate. It is now the default scWGA method for any application needing accurate SNV detection at low VAF:

- **Walsh lab brain mosaicism studies** ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]) — using naturally accumulated mutations (~2–4 per cell division) as lineage markers.
- **scDAF-seq** ([[10-Summaries/swanson-2025-daf-seq]]) — PTA enables consensus-read assembly because each unique deamination pattern is preserved across overlapping PTA amplicons.
- **Pre-implantation genetic screening** (preprint cited in Diane 2025) — first method to reliably capture SNVs, aneuploid chromosomes, and mtDNA from single embryonic cells.

## Variants and refinements

- **PTA v1** vs **v2** — v2 lower cost, comparable performance.
- **SCAN2** — variant caller designed for PTA data (somatic indels and SNVs).
- Used in Tn5-based extensions: scDAF-seq specifically pairs PTA + PacBio long reads, because PTA generates partially overlapping amplicons from the same haplotype-strand which can be merged into long consensus reads.
- **Joint genome + transcriptome via PTA** — ResolveOME and SMART-PTA (preprints) leverage primary template-directed amplification to read a cell's transcriptome alongside its clonal genome, an alternative to the nucleosome-depletion route of DEFND-seq ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]]). DEFND-seq's coverage uniformity is benchmarked against PTA ([[10-Summaries/olsen-2025-defnd-seq]]).

## Contested points

- Cost trajectory — PTA v1 ($20/cell) was originally pricier than MDA REPLI-g (~$10/cell), but **PTA v2 (~$5/cell) is reported as among the cheapest commercial scWGA chemistries**, undercutting MDA and MALBAC (~$50/cell) ([[10-Summaries/shao-2025-scDNA-mosaicism-review]] Table 1; the table is not rendered in the source clipping — verify against the PDF). Older comparisons that frame PTA as "the accurate-but-expensive option" are stale.
- PTA's relative advantage at very low cell numbers (≤96) is largest; at higher cell counts DLP+ may be preferable despite lower coverage.

## Examples

- Capturing SNVs, aneuploid chromosomes, and mtDNA from single donor-embryo cells (Diane 2025 preprint reference).
- scDAF-seq consensus-read assembly reaching N50 of 34.5 kb in a single cell using PTA + PacBio HiFi ([[10-Summaries/swanson-2025-daf-seq]]).

## Added 2026-10-07

In a same-individual comparison, PTA-amplified neurons gave ~10× fewer infant-neuron sSNV calls than MDA (26 vs 282 per neuron) and showed no artifact signature B; MDA carried an estimated ~550 SNV and 136 indel single-strand-dropout artifacts per genome [[10-Summaries/luquette-2022-neuron-scan2-indels]]. With PTA + SCAN2 the neuronal rate is 16.5 sSNVs/year and ≥3 indels/year [[10-Summaries/luquette-2022-neuron-scan2-indels]].


PTA's terminators are alpha-thio ddNTPs whose exonuclease-resistant bond stops the polymerase removing them; with ordinary ddNTPs only 15.0% of reads mapped, against 97.9% with irreversible terminators ([[10-Summaries/gonzalez-pena-2021-pnas]]). Even so, 99.9% germline precision leaves ~2,785 false-positive calls per cell, so PTA-specific callers are still needed ([[10-Summaries/gonzalez-pena-2021-pnas]]).

## Related

- [[scwga]]
- [[mda]] — direct predecessor.
- [[40-Topics/scdna-seq]]
- [[daf-seq]] — uses PTA for single-cell amplification.
- [[40-Topics/whole-genome-amplification]]
