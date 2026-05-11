---
type: concept
title: Somatic mosaicism
aliases: [somatic mosaicism, mosaicism, post-zygotic mosaicism]
tags: [genetics, mosaicism, post-zygotic]
created: 2026-05-11
updated: 2026-05-11
---

# Somatic mosaicism

> The presence of genetically distinct lineages of cells within a single organism derived from one zygote. Every human is mosaic — accumulating ~2–4 SNVs per cell division during life — but the clinical and biological consequences depend on the developmental timing and lineage of the mosaic mutation.

## Definition

Mosaicism arises from any post-zygotic mutation that escapes correction and is propagated to a clone of daughter cells. With ~10¹⁶ mitoses required to make an adult human body and ~2–4 mutations per division, every cell carries some number of mosaic variants relative to the zygote ([[10-Summaries/lars-2017-naturereviewsgenetics]], [[10-Summaries/ian-2015-trendsingenetics]]).

**Classes by lineage** ([[10-Summaries/ian-2015-trendsingenetics]]):

- **Somatic-only**: variants confined to non-germline tissues, not transmissible.
- **Gonadal mosaicism**: variants in germline only, transmissible to multiple offspring.
- **Gonosomal mosaicism**: both somatic and germline — present in soma and gametes.

**Classes by variant type**:

- **SNVs and indels** (most numerous).
- **CNVs and structural variants** (largest genomic footprint per event).
- **Aneuploidy and chromosomal rearrangements** (most clinically severe in some contexts; up to 70% of week-1 embryos show ≥1 aneuploid blastomere — [[10-Summaries/ian-2015-trendsingenetics]]).

Distinct from **chimerism** (cells from a different individual — fertilization events) and **[[microchimerism]]** (small numbers of foreign cells, e.g., maternal-fetal exchange).

## Why it matters

- **Confounds clinical genetics**: bulk DNA from one tissue can miss mosaic variants present in another tissue ([[10-Summaries/lars-2017-naturereviewsgenetics]]).
- **Drives disease**: clonal hematopoiesis, cancer, neurodevelopmental disorders (CHILD syndrome, Proteus syndrome, hemimegalencephaly, Pallister-Killian).
- **Tracks development**: natural mutation accumulation serves as endogenous lineage marker for [[lineage-tracing]] in humans where engineered markers are unethical.
- **Pre-implantation screening**: aneuploidy in early embryos shapes IVF outcomes.

The biology motivated the methods. [[scdna-seq]] became technically tractable largely *because* of demand from mosaicism researchers — Walsh lab, Vijg, Quake, Evrony — who needed single-cell DNA resolution to detect what bulk could not.

## Variants and refinements

- **[[clonal-hematopoiesis]]** — mosaic blood-cell clones expanding with age; drivers include DNMT3A, TET2, JAK2 V617F, CALR ([[10-Summaries/franco-2024-nature]]).
- **[[developmental-mutation-timing]]** — the timing-of-mutation → tissue-distribution mapping that determines clinical phenotype.
- **Mosaic disease syndromes**: CHILD syndrome (first mitosis), Proteus syndrome (AKT1), hemimegalencephaly (PI3K-AKT-mTOR), Pallister-Killian (i(12p)).

## Contested points

- The clinical actionable threshold (mosaic VAF) at which treatment decisions change — still empirical.
- Whether age-related mosaic accumulation *causes* aging or is a *biomarker* — distinction has therapeutic implications.

## Examples

- 40% of mid-gestation human prenatal neurons show complex CNV (Diane 2025 preprint reference).
- Clonal hematopoiesis: JAK2V617F detectable in 1–10% of blood at PCH stage decades before MPN ([[10-Summaries/franco-2024-nature]]).
- CHILD syndrome midline-demarcated phenotype as direct evidence of first-mitosis mosaic mutation.

## Related

- [[post-zygotic-variation]]
- [[microchimerism]]
- [[developmental-mutation-timing]]
- [[lineage-tracing]]
- [[clonal-hematopoiesis]]
- [[scdna-seq]]
- [[40-Topics/somatic-mosaicism]]
