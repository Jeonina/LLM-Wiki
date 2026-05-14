---
type: concept
title: Somatic mosaicism
aliases: [somatic mosaicism, mosaicism, post-zygotic mosaicism]
tags: [genetics, mosaicism, post-zygotic]
created: 2026-05-11
updated: 2026-05-14
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
- **Universal in aged tissue**: detected in every solid organ examined to date; aged stem cell milieu acts as the selective environment that determines which clones expand — see [[10-Summaries/kapadia-2024-stem-cell-aging|Kapadia & Goodell 2024]] for the stem-cell-aging framing ("adaptive oncogenesis").

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
- **Fetal-brain progenitors carry 200–400 mosaic SNVs/cell** at 15–21 weeks postconception, with mutation rate jumping ~3 orders of magnitude from pre-gastrulation to neurogenesis and mutation spectrum shifting from CpG-deamination to oxidative damage ([[10-Summaries/taejeong-2018-science]]).
- **~6% of human brains are hypermutable** (>101 detectable somatic SNVs), associated with age and cancer-implicated genes (NRAS, DNMT3A, TET2, MTOR, IDH2) — possibly precursor states for glioma decades before clinical diagnosis ([[10-Summaries/taejeong-2022-science]]).
- **ASD brains enriched for somatic mutations creating MEIS TF binding motifs** in fetal-brain enhancer-like regions — direct mosaic-mutation-to-enhancer causal pathway ([[10-Summaries/taejeong-2022-science]]).
- **Chromosome 16 trisomy 13-fold enriched in mouse brain** (syntenic with human chr21), cell-type-specifically concentrated in oligodendrocyte precursor cells, Pons neurons, and pericytes ([[10-Summaries/eran-2025-neuron]]).

## Mosaicism × epigenome — an open synthesis gap (synthesis)

Most mosaicism literature treats epigenetic state as an *annotation* used to interpret a mosaic genotype's likely consequences (e.g., is the mutation in an enhancer? a promoter? a heterochromatic region?). Very little work to date has measured **both somatic mutation and epigenetic state in the same single cell** as a direct biological measurement.

The methodological pieces exist:

- **CNV + methylome + transcriptome** in one cell: [[10-Summaries/single-cell-triple-omics-sequencing-reveals-genetic-epigenetic-and-transcriptomic-heterogeneity-in-hepatocellular-carcinomas|scTrio-seq]] (Hou 2016) — the closest existing precedent. Demonstrated that CNVs drive proportional expression dosage but do *not* perturb DNA methylation in the same region, at single-cell resolution. Tumor-only; not applied to neuronal or developmental mosaicism.
- **SNV + chromatin accessibility** in one cell: [[got-cha]] (Franco 2024) — the GoT–ChA assay co-captures targeted genomic mutations and accessibility. Applied to clonal-hematopoiesis JAK2/CALR but not to broader mosaicism contexts.
- **DNA sequence + chromatin state on the same fiber**: [[daf-seq]] (Elliott 2025) — single-cell single-molecule deamination footprinting. The low-VAF CC>TT CTCF-ablating variant in COLO829 is the prototype mosaic-mutation + epigenetic-state direct observation.
- **Methylation + accessibility + RNA in one cell** (no mutation): [[10-Summaries/scnmt-seq-enables-joint-profiling-of-chromatin-accessibility-dna-methylation-and-transcription-in-single-cells|scNMT-seq]] (Clark 2018) and [[10-Summaries/high-throughput-single-cell-dna-methylation-and-chromatin-accessibility-co-profiling-with-splicool-seq|SpliCOOL-seq]] (Yilei 2025).

What is missing in the literature, and what the wiki's planned review can articulate:

- No single-cell assay yet **jointly** measures somatic point mutations (the predominant mosaicism variant class) and chromatin/methylation state genome-wide. The closest is GoT-ChA (targeted) and DAF-seq (single-fiber, ~genome scale per cell but ≤12 cells deeply benchmarked).
- No systematic study yet asks **does a mosaic mutation perturb its own local epigenome at the single-cell level**? Bulk-tumor evidence is mixed (CNV doesn't affect methylation per scTrio-seq, but point mutations might).
- The neuro-mosaicism field (Walsh lab, Evrony, [[10-Summaries/single-cell-mosaicism-analysis-reveals-cell-type-specific-somatic-mutational-burden-in-alzheimer-s-dementia|Bizzotto 2024]]) measures mutations cell-type-specifically but uses bulk epigenome annotations, not paired single-cell measurements.

This is the gap PI Jeonina's review aims to articulate: **a DNA-centric framing where the locus is the unit and mutation + accessibility + methylation + 3D position are layers of the same per-cell state**.

## Related

- [[post-zygotic-variation]]
- [[microchimerism]]
- [[developmental-mutation-timing]]
- [[lineage-tracing]]
- [[clonal-hematopoiesis]]
- [[scdna-seq]]
- [[got-cha]]
- [[daf-seq]]
- [[40-Topics/somatic-mosaicism]]
- [[40-Topics/single-cell-multiomics]]
