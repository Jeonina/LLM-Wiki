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

- [[dna-methylation]]
- [[long-read-sequencing]] — direct methylation detection alternative.
- [[40-Topics/dna-methylation]]
