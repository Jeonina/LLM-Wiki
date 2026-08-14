---
type: concept
title: Bisulfite sequencing
aliases: [BS-seq, WGBS, whole-genome bisulfite sequencing]
tags: [methylation, sequencing, method]
created: 2026-05-11
updated: 2026-05-11
---

# Bisulfite sequencing

> Standard short-read method for measuring DNA methylation. Sodium bisulfite converts unmethylated C → U → T (after PCR); methylated 5mC is protected. Sequencing the converted DNA reveals methylation status at base resolution. The dominant methylation assay for ~20 years but suffers from a structural alignment problem in repeats and structural variants.

## Definition

Sodium bisulfite treatment deaminates unmethylated cytosines to uracils, which become thymidines after PCR amplification. 5-methylcytosine resists bisulfite conversion. Sequenced reads are aligned to a reference where all cytosines are converted to thymidines (and vice versa for the reverse strand) — the **"three-base alignment problem"** ([[10-Summaries/fu-2025-longread-methylation]]).

Per-CpG methylation = count of unconverted C / total reads at the site.

## Why it matters

- Established the methylation field's resolution standard — per-base, genome-wide.
- ENCODE WGBS atlas, the Roadmap Epigenomics Consortium, and the BLUEPRINT consortium all built on bisulfite sequencing.

**Limitations** that motivated long-read alternatives:

- **Three-base alignment problem**: degrades mapping in repeats and structural variants — exactly the regions where methylation has key roles (transposon silencing).
- **DNA damage** from bisulfite treatment leads to incomplete conversion and fragment loss.
- **Enzymatic alternatives** (EM-seq, TAPS-seq) have similar genome-wide coverage with less DNA damage.

## Variants and refinements

- **WGBS** (whole-genome bisulfite sequencing) — covers all CpGs but expensive.
- **RRBS** (reduced representation bisulfite sequencing) — enriches CpG-rich regions; cheaper but lower CpG coverage.
- **EM-seq** — enzymatic methyl sequencing; replaces bisulfite with TET2 + APOBEC.
- **TAPS-seq** — TET-assisted pyridine borane sequencing.

## Contested points

- Whether bisulfite sequencing remains the gold standard given long-read direct methylation detection — for most applications, yes; for repeat-rich regions, no ([[10-Summaries/fu-2025-longread-methylation]]).

## Examples

- Roadmap Epigenomics methylation atlas — predominantly WGBS-derived.
- Cancer methylation biomarker assays (e.g., Cologuard methylation-based colorectal screening) — bisulfite-based.

## Related

- [[40-Topics/dna-methylation]]
- [[40-Topics/long-read-sequencing]] — direct methylation detection alternative.
- [[40-Topics/dna-methylation]]

## Added 2026-08-13

Three throughput strategies for single-cell bisulfite sequencing, and what each costs:

| Strategy | Per-cell CpG coverage | Throughput | Source |
|---|---|---|---|
| Tubes / plates ([[30-Concepts/scbs-seq|scBS-seq]], PBAT) | ~50% | tens–hundreds | ([[10-Summaries/clark-2017-scbs-seq-protocol]]) |
| Reduced representation (scRRBS) | ~1M CpGs, ~70% of CGIs, **consistent** across cells | tens–hundreds | ([[10-Summaries/guo-2015-scrrbs-protocol]]) |
| Plate + indexed random primers (snmC-seq) | 4.7–5.7% of genome | thousands | ([[10-Summaries/luo-2017-snmc-seq]]) |
| Combinatorial indexing (sci-MET) | mean 1.1% of CpGs | thousands | ([[10-Summaries/mulqueen-2018-sci-met]]) |
| Droplet (Drop-BS) | ~13,500 CpGs/cell | up to 10,000 in 2 days | ([[10-Summaries/zhang-2023-drop-bs]]) |

**Two chemistry findings worth carrying.** Cytosine-depleted transposome adaptors survive bisulfite treatment, which is what makes indexed tagmentation compatible with conversion ([[10-Summaries/mulqueen-2018-sci-met]]). And bisulfite conversion **inside droplets yields 9× more library** than the same conversion in bulk, at 99.0% conversion — unexplained, and potentially relevant to any low-input BS protocol ([[10-Summaries/zhang-2023-drop-bs]]).

**Alignment rate is an underrated bottleneck**: classic one-cell-per-well scWGBS runs at 25 ± 20%, meaning three of four reads are wasted; transposase-based adaptor incorporation lifts it to 68 ± 8% ([[10-Summaries/mulqueen-2018-sci-met]]).

**All high-throughput methods share an annotation dependency**: they cluster on mCH bins and then label clusters against snmC-seq reference DMRs, rather than annotating de novo from their own data ([[10-Summaries/mulqueen-2018-sci-met]]; [[10-Summaries/zhang-2023-drop-bs]]). (synthesis)
