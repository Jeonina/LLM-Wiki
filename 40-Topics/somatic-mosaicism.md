---
type: topic
title: Somatic mosaicism
aliases: [somatic mosaicism, mosaicism, post-zygotic mosaicism]
tags: [mosaicism, genetics, development, aging, post-zygotic]
created: 2026-05-11
updated: 2026-06-29
---

# Somatic mosaicism

> The presence of genetically distinct lineages of cells within a single organism, all derived from one zygote ([[10-Summaries/forsberg-2017-mosaicism-review]]). Every human is a mosaic — accumulating ~2–4 SNVs per cell division throughout life ([[10-Summaries/forsberg-2017-mosaicism-review]]; [[10-Summaries/cagan-2022-nature]]) — but the clinical and biological consequences depend on the developmental timing and lineage of each mosaic mutation ([[10-Summaries/campbell-2015-mosaicism-review]]). Detecting, characterizing, and understanding these variants is the biological question driving most of the [[40-Topics/scdna-seq]] technology investment ([[10-Summaries/vijg-2020-cell]]), because they shape both normal physiology (aging, [[40-Topics/clonal-hematopoiesis|clonal hematopoiesis]] per [[10-Summaries/izzo-2024-got-cha]]) and disease (cancer per [[10-Summaries/shao-2025-scDNA-mosaicism-review]], neurodevelopmental disorders per [[10-Summaries/bizzotto-2022-brain-mosaicism-review]]).

## Definition

Mosaicism arises from any post-zygotic mutation that escapes correction and is propagated to a clone of daughter cells. With ~10¹⁶ mitoses required to build an adult human body and ~2–4 mutations per division, every cell carries some number of mosaic variants relative to the zygote ([[10-Summaries/forsberg-2017-mosaicism-review]]; [[10-Summaries/campbell-2015-mosaicism-review]]).

**Classes by lineage** ([[10-Summaries/campbell-2015-mosaicism-review]]):

- **Somatic-only**: variants confined to non-germline tissues, not transmissible.
- **Gonadal mosaicism**: variants in germline only, transmissible to multiple offspring (see [[30-Concepts/gonadal-mosaicism]] — recurrence risk).
- **Gonosomal mosaicism**: both somatic and germline — present in soma and gametes.

**Classes by variant type**:

- **SNVs and indels** — most numerous ([[10-Summaries/campbell-2015-mosaicism-review]]).
- **CNVs and structural variants** — largest genomic footprint per event ([[10-Summaries/campbell-2015-mosaicism-review]]).
- **Aneuploidy and chromosomal rearrangements** — most clinically severe in some contexts; up to 70% of week-1 embryos show ≥1 aneuploid blastomere ([[10-Summaries/campbell-2015-mosaicism-review]]).

Distinct from **chimerism** (cells from a different individual, via fertilization events) and **[[30-Concepts/microchimerism]]** (small numbers of foreign cells, e.g., maternal-fetal exchange) ([[10-Summaries/forsberg-2017-mosaicism-review]]).

## Why it matters

- **Confounds clinical genetics**: bulk DNA from one tissue can miss mosaic variants present in another tissue ([[10-Summaries/forsberg-2017-mosaicism-review]]).
- **Drives disease**: clonal hematopoiesis ([[10-Summaries/izzo-2024-got-cha]]), cancer ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]), neurodevelopmental disorders and mosaic syndromes ([[10-Summaries/bizzotto-2022-brain-mosaicism-review]]; [[10-Summaries/forsberg-2017-mosaicism-review]]).
- **Tracks development**: natural mutation accumulation serves as an endogenous lineage marker for [[30-Concepts/lineage-tracing]] in humans, where engineered markers are unethical ([[10-Summaries/coorens-2021-nature]]; [[10-Summaries/lee-six-2018-hsc-dynamics]]).
- **Pre-implantation screening**: aneuploidy in early embryos shapes IVF outcomes ([[10-Summaries/campbell-2015-mosaicism-review]]).
- **Universal in aged tissue**: detected in every solid organ examined to date ([[10-Summaries/cagan-2022-nature]]); the aged stem-cell milieu acts as the selective environment that determines which clones expand — see [[10-Summaries/kapadia-2024-stem-cell-aging|Kapadia & Goodell 2024]] for the stem-cell-aging framing ("adaptive oncogenesis") ([[10-Summaries/kapadia-2024-stem-cell-aging]]).

The biology motivated the methods: [[40-Topics/scdna-seq]] became technically tractable largely *because* of demand from mosaicism researchers — the Walsh lab, Vijg, Quake, and Evrony — who needed single-cell DNA resolution to detect what bulk could not (synthesis).

## Core concepts

### Foundations

- [[30-Concepts/post-zygotic-variation]] — broader unifying term.
- [[30-Concepts/microchimerism]] — distinct phenomenon (cells from a different individual).
- [[30-Concepts/developmental-mutation-timing]] — timing-to-tissue-distribution mapping.
- [[30-Concepts/gonadal-mosaicism]] — germline subclass; recurrence risk.

### Disease applications

- [[40-Topics/clonal-hematopoiesis]] — mosaic HSC expansions detectable in blood; cardiovascular and leukemia risk.
- [[30-Concepts/calr-mutation]], [[30-Concepts/jak2-v617f]] — MPN driver mosaic mutations.
- [[30-Concepts/myeloproliferative-neoplasm]] — clinical disease class.

### Methods enabling mosaicism research

- [[40-Topics/scdna-seq]] — single-cell DNA sequencing.
- [[30-Concepts/scwga]], [[30-Concepts/pta]] — high-coverage whole-genome amplification.
- [[40-Topics/duplex-sequencing]] — low-VAF variant detection.
- [[30-Concepts/lineage-tracing]] — endogenous mutations as lineage barcodes.

## Variants and refinements

- **[[40-Topics/clonal-hematopoiesis]]** — mosaic blood-cell clones expanding with age; drivers include DNMT3A, TET2, JAK2 V617F, and CALR ([[10-Summaries/izzo-2024-got-cha]]; [[10-Summaries/nam-2022-natgenet]]).
- **[[30-Concepts/developmental-mutation-timing]]** — the timing-of-mutation → tissue-distribution mapping that determines clinical phenotype ([[10-Summaries/bae-2017-pregastrulation-mutations]]).
- **Mosaic disease syndromes**: CHILD syndrome (first mitosis), Proteus syndrome (AKT1), hemimegalencephaly (PI3K–AKT–mTOR), and Pallister-Killian (i(12p)) ([[10-Summaries/forsberg-2017-mosaicism-review]]).

## Examples

- 40% of mid-gestation human prenatal neurons show complex CNV ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).
- Clonal hematopoiesis: JAK2V617F detectable in 1–10% of blood at the PCH stage decades before MPN ([[10-Summaries/izzo-2024-got-cha]]).
- CHILD syndrome's midline-demarcated phenotype is direct evidence of a first-mitosis mosaic mutation ([[10-Summaries/forsberg-2017-mosaicism-review]]).
- **Fetal-brain progenitors carry 200–400 mosaic SNVs/cell** at 15–21 weeks postconception, with mutation rate jumping ~3 orders of magnitude from pre-gastrulation to neurogenesis and the mutation spectrum shifting from CpG-deamination to oxidative damage ([[10-Summaries/bae-2017-pregastrulation-mutations]]).
- **~6% of human brains are hypermutable** (>101 detectable somatic SNVs), associated with age and cancer-implicated genes (NRAS, DNMT3A, TET2, MTOR, IDH2) — possibly precursor states for glioma decades before clinical diagnosis ([[10-Summaries/taejeong-2022-science]]).
- **ASD brains are enriched for somatic mutations creating MEIS TF binding motifs** in fetal-brain enhancer-like regions — a direct mosaic-mutation-to-enhancer causal pathway ([[10-Summaries/taejeong-2022-science]]).
- **Chromosome 16 trisomy is 13-fold enriched in mouse brain** (syntenic with human chr21), cell-type-specifically concentrated in oligodendrocyte precursor cells, Pons neurons, and pericytes ([[10-Summaries/mukamel-2025-aneuploidy-brain]]).

## Mosaicism × epigenome — an open synthesis gap (synthesis)

Most mosaicism literature treats epigenetic state as an *annotation* used to interpret a mosaic genotype's likely consequences (e.g., is the mutation in an enhancer? a promoter? a heterochromatic region?). Very little work to date has measured **both somatic mutation and epigenetic state in the same single cell** as a direct biological measurement (synthesis).

The methodological pieces exist:

- **CNV + methylome + transcriptome** in one cell: [[10-Summaries/hou-2016-sctrio-seq|scTrio-seq]] (Hou 2016) — the closest existing precedent. Demonstrated that CNVs drive proportional expression dosage but do *not* perturb DNA methylation in the same region, at single-cell resolution. Tumor-only; not applied to neuronal or developmental mosaicism ([[10-Summaries/hou-2016-sctrio-seq]]).
- **SNV + chromatin accessibility** in one cell: [[30-Concepts/got-cha]] ([[10-Summaries/izzo-2024-got-cha|Franco 2024]]) — the GoT–ChA assay co-captures targeted genomic mutations and accessibility. Applied to clonal-hematopoiesis JAK2/CALR but not to broader mosaicism contexts ([[10-Summaries/izzo-2024-got-cha]]).
- **DNA sequence + chromatin state on the same fiber**: [[30-Concepts/daf-seq]] ([[10-Summaries/swanson-2025-daf-seq|Elliott 2025]]) — single-cell single-molecule deamination footprinting. The low-VAF CC>TT CTCF-ablating variant in COLO829 is the prototype mosaic-mutation + epigenetic-state direct observation ([[10-Summaries/swanson-2025-daf-seq]]).
- **Methylation + accessibility + RNA in one cell** (no mutation): [[10-Summaries/clark-2018-scnmt-seq|scNMT-seq]] (Clark 2018) and [[10-Summaries/shen-2026-splicool-seq|SpliCOOL-seq]] (Shen 2026) ([[10-Summaries/clark-2018-scnmt-seq]]; [[10-Summaries/shen-2026-splicool-seq]]).
- **Mutation + accessibility + RNA in one cell** (closes the gap): [[10-Summaries/kriz-2025-duplex-multiome|Duplex-Multiome]] (Kriz 2025) — duplex consensus sequencing integrated into 10x Multiome ([[10-Summaries/kriz-2025-duplex-multiome]]).

What is missing in the literature, and what the wiki's planned review can articulate:

- No single-cell assay yet **jointly** measures somatic point mutations (the predominant mosaicism variant class) and chromatin/methylation state genome-wide. The closest are GoT-ChA (targeted) and DAF-seq (single-fiber, ~genome scale per cell but ≤12 cells deeply benchmarked) ([[10-Summaries/izzo-2024-got-cha]]; [[10-Summaries/swanson-2025-daf-seq]]).
- No systematic study yet asks **does a mosaic mutation perturb its own local epigenome at the single-cell level**? Bulk-tumor evidence is mixed (CNV doesn't affect methylation per scTrio-seq, but point mutations might) ([[10-Summaries/hou-2016-sctrio-seq]]).
- The neuro-mosaicism field (Walsh lab, Evrony, [[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto 2022]]) measures mutations cell-type-specifically but uses bulk epigenome annotations, not paired single-cell measurements ([[10-Summaries/bizzotto-2022-brain-mosaicism-review]]).

This is the gap PI Jeonina's review aims to articulate: **a DNA-centric framing where the locus is the unit and mutation + accessibility + methylation + 3D position are layers of the same per-cell state** (synthesis).

## Key entities

- [[20-Entities/christopher-walsh]] — brain mosaicism program.
- [[20-Entities/diane-d-shao]] — Walsh lab scDNA-seq review author.
- [[20-Entities/gilad-evrony]] — former Walsh postdoc; applications framework.
- [[20-Entities/lars-forsberg]] — health-and-disease mosaicism review author.
- [[20-Entities/jan-p-dumanski]] — Uppsala; co-author of the Forsberg/Dumanski review; LOY (loss of Y) mosaicism.
- [[20-Entities/james-lupski]] — clinical genetics of mosaicism; transmission risk.
- [[20-Entities/sara-bizzotto]] — Walsh lab; brain mosaicism review (Bizzotto/Walsh 2022).
- [[20-Entities/patrick-chinnery]] — mtDNA heteroplasmy single-cell biology.
- [[20-Entities/ludmil-alexandrov]] — mutational signatures and ultra-accurate duplex chemistry.
- [[20-Entities/tim-coorens]] — SMaHT duplex-seq benchmark; endogenous-mutation lineage tracing.
- [[20-Entities/manolis-kellis]] — single-cell mosaicism in AD.
- [[20-Entities/smaht-network]] — NIH consortium for somatic mosaicism atlas.

## Sources, by sub-theme

### Mosaicism biology and clinical implications

- [[10-Summaries/forsberg-2017-mosaicism-review]] — health-and-disease perspective; structural-variant-centric framing; ACE terminology; LOY as the most common human post-zygotic mutation.
- [[10-Summaries/campbell-2015-mosaicism-review]] — transmission genetics, developmental timing, lineage/variant-type classes.
- [[10-Summaries/cagan-2022-nature]] — mosaicism universal across aged solid organs.
- [[10-Summaries/vijg-2020-cell]] — somatic mutation accumulation and aging.
- [[10-Summaries/kapadia-2024-stem-cell-aging]] — stem-cell-aging / "adaptive oncogenesis" selective-environment framing.

### Methods reviews

- [[10-Summaries/shao-2025-scDNA-mosaicism-review]] — Shao 2025 NRG scDNA-seq toolkit for mosaicism research.
- [[10-Summaries/evrony-2021-scDNA-applications-review]] — applications framework.
- [[10-Summaries/bizzotto-2022-brain-mosaicism-review]] — Bizzotto & Walsh 2022, NRN brain mosaicism review.

### MPN as a tractable mosaicism disease model

- [[10-Summaries/nam-2019-got]] — CALR-mutated MPN.
- [[10-Summaries/izzo-2024-got-cha]] — JAK2V617F MPN and clonal hematopoiesis; GoT-ChA.
- [[10-Summaries/nam-2022-natgenet]] — clonal-hematopoiesis driver genetics.

### Duplex sequencing for low-VAF mutation detection

- [[10-Summaries/schmitt-2012-pnas]] — Schmitt/Loeb 2012. Original duplex sequencing.
- [[10-Summaries/kennedy-2014-duplex-protocol]] — Kennedy 2014 founding DS bench protocol.
- [[10-Summaries/nandi-2025-udseq]] — UDSeq 2025.
- [[10-Summaries/abascal-2021-nanoseq]] — NanoSeq nuclear-genome DS.
- [[10-Summaries/zhang-2025-smaht-duplex-benchmark]] — SMaHT cross-method benchmark.

### Single-cell mosaicism studies

- [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] — Luquette 2025: PTA + duplex validation, 102 nuclei from lung+colon of a 74-yo donor; companion PTA pipeline paper.
- [[10-Summaries/glynos-2023-mtdna-mosaicism]] — Glynos/Chinnery 2023: mouse mtDNA heteroplasmy variance increases through life.
- [[10-Summaries/kousi-2022-ad-mosaicism]] — Kousi/Kellis 2022: cell-type-specific AD mosaicism.
- [[10-Summaries/lodato-2017-aging-neurons]] — Lodato et al. 2018 aging-neuron mosaic mutation burden.
- [[10-Summaries/bae-2017-pregastrulation-mutations]] — Bae 2017: developmental mutation timing.
- [[10-Summaries/taejeong-2022-science]] — hypermutable brains, ASD MEIS-motif somatic enhancer mutations.
- [[10-Summaries/mukamel-2025-aneuploidy-brain]] — cell-type-specific aneuploidy enrichment in mouse brain.

### Structural-variant somatic mosaicism

- [[10-Summaries/liu-2025-nanopore-lscc-svs]] — nanopore SomaGauss-SV in LSCC; smoking × deletion-burden correlation.

### Mosaicism × single-cell multiomics

- [[10-Summaries/hou-2016-sctrio-seq]] — scTrio-seq: CNV + methylome + transcriptome in one cell.
- [[10-Summaries/swanson-2025-daf-seq]] — DAF-seq: DNA sequence + chromatin state on the same fiber.
- [[10-Summaries/clark-2018-scnmt-seq]] — scNMT-seq: methylation + accessibility + RNA in one cell.
- [[10-Summaries/shen-2026-splicool-seq]] — SpliCOOL-seq: multi-layer epigenome in one cell.
- [[10-Summaries/kriz-2025-duplex-multiome]] — Duplex-Multiome: mutation + accessibility + RNA in one cell.

## Synthesized notes

_None yet._

## Open questions

- **Single-cell duplex sequencing** — duplex needs both strands; scWGA loses strand identity. Closing this gap is the single biggest method gap ([[40-Topics/duplex-sequencing]] open questions).
- Tissue-specific mosaic mutation rates: high in skin (UV) and intestine (turnover); uncertain in many other tissues.
- The clinical actionable threshold (mosaic VAF, gene set) at which mosaicism becomes diagnostically actionable — still empirical ([[10-Summaries/forsberg-2017-mosaicism-review]]).
- Whether age-related mosaic accumulation *causes* aging-related disease or is a *biomarker* — the distinction matters for therapeutic strategies ([[10-Summaries/vijg-2020-cell]]; [[10-Summaries/cagan-2022-nature]]).
- IRE1-XBP1 as a therapeutic target in CALR-mutant clonal hematopoiesis ([[10-Summaries/nam-2019-got]] hypothesis) — no clinical validation in wiki yet.
- Why CALR's fitness advantage is differentiation-dependent in ET but already strong at the HSPC level in MF.
- Whether JAK2V617F chromatin priming in HSCs is causal for clonal expansion or downstream of it ([[10-Summaries/izzo-2024-got-cha]]).
- Pre-implantation genetic screening from a single embryo cell — preprint stage; awaiting clinical validation ([[10-Summaries/shao-2025-scDNA-mosaicism-review]]).

## Linked summaries (lint pass 2026-05-21)

- [[10-Summaries/ludwig-2020-mtscatac-seq]] — Ludwig 2020 — mtscATAC-seq: massively parallel mtDNA genotyping + chromatin in single cells.
- [[10-Summaries/oroak-2012-autism-targeted-seq]] — O'Roak 2012 — Multiplex targeted sequencing of recurrently mutated genes in ASD.
- [[10-Summaries/campbell-2015-mosaicism-review]] — Campbell 2015 — Somatic mosaicism: implications for disease and transmission (review).
- [[10-Summaries/mckenna-2016-science]] — McKenna 2016 — GESTALT: whole-organism lineage tracing by combinatorial genome editing.
- [[10-Summaries/forsberg-2017-mosaicism-review]] — Forsberg, Gisselsson & Dumanski 2017 NRG — structural-variant-centric framing of mosaicism; introduces ACE terminology; LOY as the most common human post-zygotic mutation.
- [[10-Summaries/hilal-2026-cardiac-somatic-review]] — Hilal, Arava & Choudhury 2026 — cardiovascular somatic-variation review; cardiomyocyte 4–30k SNVs/cell and CHIP→HFpEF/stroke links.
- [[10-Summaries/hsieh-2026-scmtmpm-scwmss]] — Hsieh 2026 — single-cell mtDNA mutational burden metrics (scmtMPM, scwMSS); negative selection at sub-threshold VAF.

## Related

- [[30-Concepts/post-zygotic-variation]]
- [[30-Concepts/microchimerism]]
- [[30-Concepts/developmental-mutation-timing]]
- [[30-Concepts/gonadal-mosaicism]]
- [[30-Concepts/lineage-tracing]]
- [[40-Topics/clonal-hematopoiesis]]
- [[40-Topics/scdna-seq]]
- [[30-Concepts/got-cha]]
- [[30-Concepts/daf-seq]]
- [[40-Topics/scdna-seq]]
- [[40-Topics/duplex-sequencing]]
- [[40-Topics/single-cell-multiomics]]

## Added 2026-08-13

HiDEF-seq ([[10-Summaries/liu-2024-hidef-seq]]) shifts the object of study one step upstream: from mutations to the **single-strand mismatches and damage that precede them**. Double-strand mutations are the endpoint of an interaction between lesion formation, DNA repair, and replication, so dsDNA signatures need not reflect the patterns of the originating events — and until 2024 no method could read those events, because every method amplified first.

Practical consequences for the corpus: single-strand burden estimates from duplex-family methods are inflated ~18-fold ([[10-Summaries/liu-2024-hidef-seq]]); and neuronal somatic SNV rates from MDA-era data were overestimated, revised to 15/year with PTA ([[10-Summaries/luquette-2021-scan2]]). (synthesis)
