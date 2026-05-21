---
type: summary
title: "Bae 2022 — Analysis of somatic mutations in 131 human brains reveals aging-associated hypermutability"
source: "[[00-Sources/papers/Analysis of somatic mutations in 131 human brains reveals aging-associated hypermutability]]"
aliases: [Bae 2022, Taejeong 2022, BSMN 131-brain study, brain hypermutability]
tags: [somatic-mosaicism, neuro-mosaicism, BSMN, autism-spectrum-disorder, schizophrenia, tourette-syndrome, hypermutability, MEIS, foundational]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Bae et al. (2022) — *Analysis of somatic mutations in 131 human brains reveals aging-associated hypermutability* — *Science*. [DOI](https://doi.org/10.1126/science.abm6222)

# Bae et al. 2022 — Aging-associated hypermutability + ASD enhancer-motif mosaicism

> Taejeong Bae, Liana Fasching, Yifan Wang, Joo Heon Shin, Milovan Suvakov, Yeongjun Jang, Scott Norton, Caroline Dias, Jessica Mariani, Alexandre Jourdon, Feinan Wu, Arijit Panda, Reenal Pattni, Yasmine Chahine, Rebecca Yeh, Rosalinda C. Roberts, Anita Huttner, Joel E. Kleinman, Thomas M. Hyde, Richard E. Straub, Christopher A. Walsh, Brain Somatic Mosaicism Network, Alexander E. Urban, James F. Leckman, Daniel R. Weinberger, Flora M. Vaccarino\*, **Alexej Abyzov\***. *Science* **377**, 511–517 (29 July 2022). DOI: 10.1126/science.abm6222.

## Thesis

The largest brain-mosaicism cohort study to date: 131 human brains (44 neurotypical, 19 Tourette syndrome, 9 schizophrenia, 59 autism spectrum disorder), each sequenced to ≥200× from bulk cortex/striatum/hippocampus. Typical brain carries 10–60 detectable mosaic SNVs, but **~6% are "hypermutable"** (>101 SNVs). Hypermutability associates with **age**, **damaging mutations in cancer-implicated genes**, and **in vivo clonal expansions**. In ASD specifically, somatic mutations create **putative transcription-factor binding motifs (especially MEIS family) in enhancer-like regions** active in the developing brain — providing a direct mosaic-mutation-to-regulatory-element causal pathway for ASD risk.

## Method

1. 131 frozen postmortem brains, 1–2 regions each (cortex, striatum, hippocampus) from Yale, LIBD, Harvard.
2. Bulk WGS at ≥200× per region (some samples 620×).
3. Somatic-mutation discovery via the BSMN bulk-mutation calling workflow ([github.com/abyzovlab/bsmn-pipeline](https://github.com/abyzovlab/bsmn-pipeline)) distinguishing somatic from germline by frequency and population-database overlap.
4. For 8 brains, additional FACS-sorted cell fractions (NeuN+/Sox6+, NeuN+/Sox6−, NeuN−/Sox10+, NeuN−/Sox10−, CTIP2+/CTIP2−) for cell-lineage analysis.
5. Single-nucleus validation in 8 nuclei × 16 wells from brain NC7 striatal interneuron fraction (clonal-expansion validation).
6. Read-backed phasing assigns mutations to maternal/paternal haplotypes for ~20% of calls.
7. Structural-mutation calling via CNVpytor.

## Key claims

1. **~6% of brains are hypermutable** (>101 somatic mutations). Hypermutability rate **rises with age** (P = 8.2×10⁻³): 16% of brains >60 years old vs only 2% of those <40. Among older brains, hypermutability reaches ~3% prevalence at 95% confidence — frequent enough to be a real human-population phenomenon.

2. **Hypermutable brains overrepresent damaging mutations in cancer-implicated genes** (P = 2.4×10⁻³): NRAS (recurrent chr1:115258747 C>T, COSMIC ID COSV54736383), DNMT3A, GBE1, TET2, TENM3, ENDOU, IDH2, BCORL1. Suggests **incipient clonal expansion** in some brains — possibly precursor states of glioma/glioblastoma decades before clinical diagnosis. Brain LIBD82 carried aneuploidies (duplication of chr7, deletion of chr10) consistent with glioblastoma signatures in ~15% of hippocampal cells.

3. **Two mechanistically distinct hypermutability classes**:
   - **Clonal-expansion type**: brain NC7 (NRAS-mutant) shows the same mutations present in 8/8 striatal interneuron single nuclei (94% of bulk mutations validated at single-cell level), proving a clonal lineage. The expanded lineage originated in embryonic basal ganglia and populated cortex + striatum by interneuron migration.
   - **Possible intrinsic-hypermutability type**: brains TS9 and NC7 with damaging mutations in MTOR, TET2, DNMT3A, IDH2 — could be due to expanded lineage, or could be due to leaky DNA repair / increased mutation rate.

4. **Cell-lineage distribution is non-uniform across brain regions** in many brains. For ≥5 brains (out of 22 Yale + 13 LIBD with full fraction data), VAF in cortex > VAF in striatum or hippocampus (P = 5×10⁻⁴). Interpretation: founder population of cortex is allocated from fewer earlier lineages, so each cortical lineage frequency is higher on average. Alternatively, cortex has higher propensity for clonal expansion.

5. **ASD enhancer-motif finding** (the cohort's most consequential biological result):
   - ASD brain AN05983: validated splice mutation in **MTOR** (cancer + ASD-implicated; insulin/PI3K signaling).
   - Brain TS9 had high-VAF missense **ARHGEF6** mutation (X-linked intellectual disability, dendrite-orientation, cell-polarity gene; mouse knockout produces hippocampal abnormalities).
   - Across the ASD cohort: somatic mutations in non-hypermutable brains create **16 putative transcription-factor binding motifs in enhancer-like regions** active in fetal brain (P<10⁻⁴ by binomial test). Top-ranked: **MEIS1/MEIS2/MEIS3** binding sites. In normal brains, only 4 such mutations.
   - MEIS genes are homeodomain TFs that promote chromatin decompaction, cofactor HOX, regulate proliferation/growth/neurogenesis/patterning. MEIS2 specifically marks a cortical-interneuron subpopulation populating white matter. **Mutations creating MEIS binding sites could affect TF protein dosage and dysregulate gene-regulatory networks** during development → an ASD risk pathway.

6. **Somatic structural mutations**: ~7% of brains carry duplications (~5%) or deletions, mostly tandem duplications with sequence microhomologies at breakpoints (1–4 bp), suggesting replicative origin. Comparable across cohorts; functional consequence likely small.

## Surprising / load-bearing for the review

- **The age-hypermutability link is novel and matters for normal-aging biology**, not just disease. Combined with [[10-Summaries/kousi-2022-ad-mosaicism|Kousi/Kellis AD cell-type mosaicism]] and [[10-Summaries/luquette-2025-pta-duplex-mosaicism|Luquette/Walsh PTA+DS]], it triangulates that **brain mosaicism accumulates over the lifespan, with a long tail of hypermutable cases — and the accumulation has plausible cancer-precursor mechanism (clonal hematopoiesis-like expansion + cancer-gene mutations)**.

- **The ASD MEIS-motif finding** is the **direct mosaic-mutation-to-enhancer causal link** that the planned review's mosaicism × epigenome synthesis can cite. The mutations sit in chromatin-active enhancer-like regions (defined by fetal-brain epigenome reference), so the *interpretation* is bulk-epigenome-annotated — but the *measurement* is single-brain mosaic mutations at high-enough VAF to call from bulk WGS. This is exactly the bulk-epigenome-annotation methodology the [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|synthesis note]] flagged as the field's current default. The review can use this as the prototype "bulk-epigenome-annotated mosaicism" finding and contrast it with the single-cell joint measurements that would be needed to confirm the same locus is in an open-chromatin state *in the cells that carry the mutation*.

- **The clonal-expansion finding (NC7 NRAS) is methodologically the analog of clonal hematopoiesis in the brain**: same mutation, same gene class, same age-dependence, possibly same precursor-to-cancer trajectory. For the review's §5 cancer-evolution section, this is a clean human-brain CH-of-indeterminate-potential precedent.

- **First author Taejeong Bae** — same lab as [[10-Summaries/bae-2017-pregastrulation-mutations|Bae 2018]], same approach scaled from 3 brains/clonal-expansion to 131 brains/bulk-WGS. Two papers from the same lab now anchor the human-brain mosaicism timeline.

## Entities / concepts touched

[[somatic-mosaicism]] · [[clonal-hematopoiesis]] · [[autism-spectrum-disorder]] · [[mtor-pathway]] · [[developmental-mutation-timing]] · [[transcription-factor-motif]] · [[enhancer-states]] · [[20-Entities/alexej-abyzov]] · [[20-Entities/flora-vaccarino]] · [[20-Entities/christopher-walsh]] · [[20-Entities/peter-park]] · [[20-Entities/joseph-gleeson]] · [[40-Topics/somatic-mosaicism]]

## Related
- [[20-Entities/taejeong-bae]] — first/co-author on the foundational Bae et al. brain mosaicism papers (2018 pregastrulation-timing, 2022 NeuN-sorted neurons). summaries

- [[10-Summaries/bae-2017-pregastrulation-mutations]] — Bae 2018, foundational fetal-brain clonal-expansion paper from same lab.
- [[10-Summaries/kousi-2022-ad-mosaicism]] — Kousi/Kellis AD-specific cell-type-specific mosaic burden.
- [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] — Luquette/Walsh SMaHT 102-nucleus PTA + DS.
- [[10-Summaries/bizzotto-2022-brain-mosaicism-review]] — Bizzotto/Walsh 2022 NRN review.
- [[10-Summaries/izzo-2024-got-cha]] — GoT-ChA shows the analogous chromatin-priming-before-expression pathway in hematopoiesis; this paper's MEIS-motif finding asks whether a similar mechanism operates in ASD brain.
