---
type: topic
title: Somatic mosaicism
explainer: somatic-mosaicism
aliases: [somatic mosaicism, mosaicism, post-zygotic mosaicism]
tags: [mosaicism, genetics, development, aging, post-zygotic]
created: 2026-05-11
updated: 2026-10-12
paper_section: ["5.2"]
---

# Somatic mosaicism

> The presence of genetically distinct lineages of cells within a single organism, all derived from one zygote ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]). Every human is a mosaic, accumulating ~2–4 mutations per cell division ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]), but the clinical and biological consequences depend on the developmental timing and lineage of each mosaic mutation ([[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]). Detecting and characterizing these variants is the biological question driving most of the [[40-Topics/scdna-seq]] technology investment ([[10-Summaries/vijg-2020-cell|Vijg & Dong 2020]]), because they shape both normal physiology (aging, [[40-Topics/clonal-hematopoiesis|clonal hematopoiesis]]; [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]) and disease (cancer, [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; neurodevelopmental disorders, [[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto 2022]]).

> [!abstract] 한눈에
> 한 수정란에서 나온 세포라도 분열할 때마다 2–4개의 변이가 쌓여 모든 사람의 몸은 모자이크가 되며, 변이가 언제 어느 계통에서 생겼는지에 따라 영향이 달라진다 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]). 변이 검출은 PTA와 duplex 계열 방법으로 정확해졌지만, 같은 세포에서 체세포 변이와 chromatin·methylation 상태를 genome-wide로 함께 재는 방법은 아직 드물다 ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]; [[10-Summaries/kriz-2025-duplex-multiome|Duplex-Multiome]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [체세포 모자이크](../60-Explainers/somatic-mosaicism.html)
<!-- /explainer-links -->

## Key points

- **Every cell is a mosaic relative to the zygote.** More than 10¹⁶ cells are produced over a human lifetime ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]), and mutations accrue at ~2–4 per cell division ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- **Timing sets the phenotype, and the mutation rate changes through development.** The rate rises from ~1.3 SNVs per division before gastrulation to ~8.6 per division during neurogenesis, leaving 200–400 mosaic SNVs per fetal-brain progenitor ([[10-Summaries/bae-2017-pregastrulation-mutations|Bae 2018]]); timing determines tissue distribution and clinical phenotype ([[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]).
- **Mosaic mutations accumulate with age in every tissue examined.** Intestinal-crypt mutation rates scale inversely with lifespan across 16 mammals ([[10-Summaries/cagan-2022-nature|Cagan 2022]]), and ~6% of human brains are hypermutable ([[10-Summaries/taejeong-2022-science|Bae 2022]]).
- **Rate estimates depend on how errors are removed.** PTA revised neuronal SNV rates down to 16.5 per year from MDA-era estimates ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]), and HiDEF-seq showed duplex-family single-strand burdens are inflated ~18-fold ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]).
- **Mutation and epigenome are rarely measured in the same cell.** GoT–ChA is targeted ([[10-Summaries/izzo-2024-got-cha|GoT–ChA]]), DAF-seq is benchmarked on ≤12 cells deeply ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]), and Duplex-Multiome adds duplex SNV calls to 10x Multiome ([[10-Summaries/kriz-2025-duplex-multiome|Duplex-Multiome]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/post-zygotic-variation|Post-zygotic variation]] — Genetic changes acquired after fertilization; the unifying term for somatic and germline mosaic mutations.
> - `concept` [[30-Concepts/developmental-mutation-timing|Developmental mutation timing]] — How the timing of a post-zygotic mutation determines its tissue distribution and phenotype.
> - `concept` [[30-Concepts/gonadal-mosaicism|Gonadal mosaicism]] — Mosaic mutations in the germline that can recur in several offspring of an unaffected parent.
> - `concept` [[30-Concepts/lineage-tracing|Lineage tracing]] — Reconstructing cell ancestry, in humans from endogenous somatic mutations.
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Somatic genotype and chromatin accessibility from the same nucleus in 10x scATAC droplets.
> - `concept` [[30-Concepts/daf-seq|DAF-seq]] — Deaminase footprinting that records protein occupancy as C→T changes that survive amplification.

## Definition and classes

Mosaicism arises from any post-zygotic mutation that escapes correction and is propagated to a clone of daughter cells. With >10¹⁶ cells produced over a human lifetime (~3 × 10¹² in an adult body), every cell carries some number of mosaic variants relative to the zygote ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]); mutations accrue at ~2–4 per cell division ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]). [[30-Concepts/post-zygotic-variation]] is the broader unifying term ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]).

**Classes by lineage** ([[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]):

- **Somatic-only** — variants confined to non-germline tissues, not transmissible ([[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]).
- **Gonadal mosaicism** — variants in germline only, transmissible to multiple offspring; see [[30-Concepts/gonadal-mosaicism]] for recurrence risk ([[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]).
- **Gonosomal mosaicism** — present in both soma and gametes ([[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]).

**Classes by variant type:**

| Variant class | Note |
|---|---|
| SNVs and indels | Most numerous ([[10-Summaries/campbell-2015-mosaicism-review\|Campbell 2015]]) |
| CNVs and structural variants | Largest genomic footprint per event ([[10-Summaries/campbell-2015-mosaicism-review\|Campbell 2015]]) |
| Aneuploidy and chromosomal rearrangements | Most clinically severe in some contexts; up to 70% of week-1 embryos show ≥1 aneuploid blastomere ([[10-Summaries/campbell-2015-mosaicism-review\|Campbell 2015]]) |

Mosaicism is distinct from **chimerism** (cells from a different individual, via fertilization events) and from **[[30-Concepts/microchimerism]]** (small numbers of foreign cells, e.g. maternal–fetal exchange) ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]). [[30-Concepts/developmental-mutation-timing]] is the mapping from mutation timing to tissue distribution that determines clinical phenotype ([[10-Summaries/bae-2017-pregastrulation-mutations|Bae 2018]]).

## Why it matters

- **Confounds clinical genetics** — bulk DNA from one tissue can miss mosaic variants present in another tissue ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]).
- **Drives disease** — clonal hematopoiesis ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]), cancer ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]), neurodevelopmental disorders and mosaic syndromes ([[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto 2022]]; [[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]).
- **Tracks development** — natural mutation accumulation serves as an endogenous lineage marker for [[30-Concepts/lineage-tracing]] in humans, where engineered markers are unethical ([[10-Summaries/coorens-2021-nature|Coorens 2021]]; [[10-Summaries/lee-six-2018-hsc-dynamics|Lee-Six 2018]]).
- **Pre-implantation screening** — aneuploidy in early embryos shapes IVF outcomes ([[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]).
- **Universal in aged tissue** — somatic mutations accumulate in intestinal crypts across all 16 mammalian species examined, at rates scaling inversely with lifespan ([[10-Summaries/cagan-2022-nature|Cagan 2022]]); the aged stem-cell milieu acts as the selective environment that determines which clones expand ("adaptive oncogenesis") ([[10-Summaries/kapadia-2024-stem-cell-aging|Kapadia & Goodell 2024]]).

The biology motivated the methods: [[40-Topics/scdna-seq]] became technically tractable largely *because* of demand from mosaicism researchers — the Walsh lab, Vijg, Quake and Evrony — who needed single-cell DNA resolution to detect what bulk could not (synthesis).

## Concept map

- **Foundations** — [[30-Concepts/post-zygotic-variation]] (broader unifying term); [[30-Concepts/microchimerism]] (distinct phenomenon: cells from a different individual); [[30-Concepts/developmental-mutation-timing]] (timing-to-tissue-distribution mapping); [[30-Concepts/gonadal-mosaicism]] (germline subclass; recurrence risk).
- **Disease applications** — [[40-Topics/clonal-hematopoiesis]] (mosaic HSC expansions detectable in blood; cardiovascular and leukemia risk); [[30-Concepts/calr-mutation]] and [[30-Concepts/jak2-v617f]] (MPN driver mosaic mutations); [[30-Concepts/myeloproliferative-neoplasm]] (clinical disease class).
- **Methods** — [[40-Topics/scdna-seq]] (single-cell DNA sequencing); [[30-Concepts/scwga]] and [[30-Concepts/pta]] (high-coverage whole-genome amplification); [[40-Topics/duplex-sequencing]] (low-VAF variant detection); [[30-Concepts/lineage-tracing]] (endogenous mutations as lineage barcodes).

## Reviews

- [[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]] — health-and-disease perspective; structural-variant-centric framing; introduces ACE terminology; LOY as the most common human post-zygotic mutation.
- [[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]] — transmission genetics, developmental timing, lineage and variant-type classes.
- [[10-Summaries/vijg-2020-cell|Vijg & Dong 2020]] — somatic mutation accumulation and aging.
- [[10-Summaries/kapadia-2024-stem-cell-aging|Kapadia & Goodell 2024]] — stem-cell aging and the "adaptive oncogenesis" selective-environment framing.
- [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]] — scDNA-seq toolkit for mosaicism research (Nature Reviews Genetics).
- [[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]] — applications framework for scDNA-seq.
- [[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto & Walsh 2022]] — brain mosaicism review (Nature Reviews Neuroscience).
- [[10-Summaries/hilal-2026-cardiac-somatic-review|Hilal 2026]] — cardiovascular somatic-variation review; cardiomyocytes carry 4–30k SNVs per cell; CHIP linked to HFpEF and stroke.

## Development and lineage

| Study | System | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/bae-2017-pregastrulation-mutations\|Bae 2018]] | Human fetal brain, 15–21 weeks postconception | Mosaic SNVs in progenitors | 200–400 mosaic SNVs per cell; rate rises from ~1.3 SNVs per division before gastrulation to ~8.6 per division during neurogenesis (three orders of magnitude above the adult germline rate); spectrum shifts from CpG deamination to oxidative damage ([[10-Summaries/bae-2017-pregastrulation-mutations\|Bae 2018]]) |
| [[10-Summaries/coorens-2021-nature\|Coorens 2021]] | Normal tissues of three adults | 511 laser-capture microdissections, low-input WGS | Shared somatic mutations as natural lineage barcodes resolve embryonic patterning ([[10-Summaries/coorens-2021-nature\|Coorens 2021]]) |
| [[10-Summaries/lee-six-2018-hsc-dynamics\|Lee-Six 2018]] | Blood of one 59-year-old man | 140 clonally expanded HSPCs, WGS | Population dynamics of normal HSCs inferred from somatic mutations ([[10-Summaries/lee-six-2018-hsc-dynamics\|Lee-Six 2018]]) |
| [[10-Summaries/mckenna-2016-science\|McKenna 2016]] | Whole organism | GESTALT, combinatorial CRISPR barcodes | Engineered-barcode lineage tracing by cumulative genome editing — the synthetic contrast to endogenous mutations ([[10-Summaries/mckenna-2016-science\|McKenna 2016]]) |

## Brain mosaicism

| Study | System | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/taejeong-2022-science\|Bae 2022]] | 131 human brains | Bulk tissue, ≥200× | ~6% of brains are hypermutable (>101 detectable somatic SNVs), associated with age and cancer-implicated genes (NRAS, DNMT3A, TET2, MTOR, IDH2) — possibly precursor states for glioma decades before diagnosis; ASD brains are enriched for somatic mutations creating MEIS TF motifs in fetal-brain enhancer-like regions ([[10-Summaries/taejeong-2022-science\|Bae 2022]]) |
| [[10-Summaries/lodato-2017-aging-neurons\|Lodato 2018]] | Single human neurons | — | Mosaic mutation burden rises with aging and neurodegeneration ([[10-Summaries/lodato-2017-aging-neurons\|Lodato 2018]]) |
| [[10-Summaries/luquette-2022-neuron-scan2-indels\|Luquette 2022]] | Single human neurons | PTA | Neuronal somatic SNV rate revised to 16.5 per year, below MDA-era estimates ([[10-Summaries/luquette-2022-neuron-scan2-indels\|Luquette 2022]]) |
| [[10-Summaries/kousi-2022-ad-mosaicism\|Kousi 2022]] | Alzheimer's disease brains (ROSMAP) | Single-cell mosaicism analysis | Cell-type-specific increase in somatic mutation burden in AD ([[10-Summaries/kousi-2022-ad-mosaicism\|Kousi 2022]]) |
| [[10-Summaries/kriz-2025-duplex-multiome\|Kriz 2025]] | Developing and aging brain | Duplex-Multiome | Somatic SNVs called by duplex consensus in the same nuclei as snATAC and snRNA ([[10-Summaries/kriz-2025-duplex-multiome\|Kriz 2025]]) |
| [[10-Summaries/mukamel-2025-aneuploidy-brain\|Mukamel 2025]] | Adult mouse brain | snmC-seq methylomes reused for copy number | Chromosome 16 trisomy (syntenic with human chr21) is 13-fold enriched, concentrated in oligodendrocyte precursor cells and pons neurons (also midbrain, dentate gyrus, claustrum and retrosplenial cortex) ([[10-Summaries/mukamel-2025-aneuploidy-brain\|Mukamel 2025]]) |
| [[10-Summaries/oroak-2012-autism-targeted-seq\|O'Roak 2012]] | 2,446 ASD probands | MIP resequencing of 44 genes | Germline de novo burden in six genes (~1% of sporadic ASD) — a germline baseline for ASD mosaicism, not itself a mosaicism study ([[10-Summaries/oroak-2012-autism-targeted-seq\|O'Roak 2012]]) |

The neuro-mosaicism field (Walsh lab, Evrony, [[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto 2022]]) measures mutations cell-type-specifically but uses bulk epigenome annotations, not paired single-cell measurements ([[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto 2022]]). Shao 2025 reports that 40% of mid-gestation human prenatal neurons show complex CNV ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

## Aging and normal tissues

| Study | System | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/cagan-2022-nature\|Cagan 2022]] | Intestinal crypts, 16 mammals | Cross-species somatic mutation rates | Rates scale inversely with lifespan ([[10-Summaries/cagan-2022-nature\|Cagan 2022]]) |
| [[10-Summaries/hoang-2016-botseqs\|Hoang 2016]] | Normal human tissues | BotSeqS | Rare somatic mutation burden rises with age and is tissue-specific; mutagens raise nuclear but not mtDNA load ([[10-Summaries/hoang-2016-botseqs\|Hoang 2016]]) |
| [[10-Summaries/maslov-2022-smm-seq\|Maslov 2022]] | Human liver | SMM-seq, bulk | Private somatic SNVs; 0.34 vs 0.96 SNV/Mbp in young vs aged donors ([[10-Summaries/maslov-2022-smm-seq\|Maslov 2022]]) |
| [[10-Summaries/muyas-2024-scomatic\|Muyas 2024]] | Polyclonal normal tissues (heart, GTEx, sciATAC atlas) | SComatic on single-cell expression and accessibility data | Somatic mutation burdens and signatures mined without matched DNA ([[10-Summaries/muyas-2024-scomatic\|Muyas 2024]]) |
| [[10-Summaries/luquette-2025-pta-duplex-mosaicism\|Luquette 2025]] | Lung and colon of a 74-year-old donor | PTA + duplex validation, 102 nuclei | Companion to the PTA pipeline paper; details unverified against the clipped source ([[10-Summaries/luquette-2025-pta-duplex-mosaicism\|Luquette 2025]]) |
| [[10-Summaries/fischbach-2026-alphagenome-aging\|Fischbach 2026]] | Cagan 2022 colonic-crypt mutation catalogue | AlphaGenome predictions (preprint) | Predicted transcriptional effects far below the aging program, plus a CDS-depletion signature of purifying selection (12× for mouse indels); predictions never checked against measured effects ([[10-Summaries/fischbach-2026-alphagenome-aging\|Fischbach 2026]]) |

## Clonal hematopoiesis and MPN

MPN is a tractable mosaicism disease model: [[40-Topics/clonal-hematopoiesis]] is the expansion of mosaic blood-cell clones with age, with drivers including DNMT3A, TET2, JAK2 V617F and CALR ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]; [[10-Summaries/nam-2022-natgenet|Nam 2022]]).

| Study | System | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/nam-2019-got\|Nam 2019]] | CALR-mutated MPN | GoT (genotype + scRNA) | CALR's transcriptional impact depends on the progenitor's native identity; IRE1–XBP1 proposed as a target ([[10-Summaries/nam-2019-got\|Nam 2019]]) |
| [[10-Summaries/izzo-2024-got-cha\|Izzo 2024]] | JAK2V617F MPN and clonal hematopoiesis | GoT–ChA (genotype + scATAC) | JAK2V617F-mutant HSCs already show increased accessibility of canonical JAK2/STAT targets at the clonal-hematopoiesis stage, before overt MPN ([[10-Summaries/izzo-2024-got-cha\|Izzo 2024]]) |
| [[10-Summaries/nam-2022-natgenet\|Nam 2022]] | DNMT3A R882 clonal hematopoiesis | GoT + methylation multi-omics | Clonal-hematopoiesis driver genetics; DNMT3A R882 perturbs early progenitors through selective hypomethylation ([[10-Summaries/nam-2022-natgenet\|Nam 2022]]) |
| [[10-Summaries/gillman-2026-scarce\|Gillman 2026]] | Refractory coeliac disease, 4,858 lymphocytes | SCARCE, droplet single-cell multiomics | Recovered the four previously known T-cell drivers that passed filtering and placed them in specific T-cell subsets via surface markers ([[10-Summaries/gillman-2026-scarce\|Gillman 2026]]) |

## Mosaic syndromes

- CHILD syndrome's midline-demarcated phenotype reflects mutation timing relative to left–right axis determination ([[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]).
- Proteus syndrome (AKT1), hemimegalencephaly (PI3K–AKT–mTOR) and Pallister-Killian (i(12p)) are mosaic disease syndromes ([[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]).

## Mitochondrial mosaicism

| Study | Year | Input | Approach | Note |
|---|---|---|---|---|
| [[10-Summaries/glynos-2023-mtdna-mosaicism\|Glynos 2023]] | 2023 | Mouse single cells | mtDNA heteroplasmy | Heteroplasmy variance increases through life ([[10-Summaries/glynos-2023-mtdna-mosaicism\|Glynos 2023]]) |
| [[10-Summaries/ludwig-2020-mtscatac-seq\|mtscATAC-seq]] | 2021 | Single cells | mtDNA genotyping + chromatin | Massively parallel mtDNA genotyping with accessibility ([[10-Summaries/ludwig-2020-mtscatac-seq\|Lareau 2021]]) |
| [[10-Summaries/hsieh-2026-scmtmpm-scwmss\|Hsieh 2026]] | 2026 | mtscATAC-seq data | scmtMPM, scwMSS metrics | Single-cell mtDNA mutational burden; negative selection at sub-threshold VAF ([[10-Summaries/hsieh-2026-scmtmpm-scwmss\|Hsieh 2026]]) |

## Low-VAF and single-molecule detection

| Tool | Year | Input | Approach | Note |
|---|---|---|---|---|
| [[10-Summaries/schmitt-2012-pnas\|Duplex Sequencing]] | 2012 | Bulk DNA | Duplex consensus | Original duplex sequencing ([[10-Summaries/schmitt-2012-pnas\|Schmitt 2012]]) |
| [[10-Summaries/kennedy-2014-duplex-protocol\|Kennedy 2014]] | 2014 | Bulk DNA | Duplex consensus | Founding bench protocol ([[10-Summaries/kennedy-2014-duplex-protocol\|Kennedy 2014]]) |
| [[10-Summaries/hoang-2016-botseqs\|BotSeqS]] | 2016 | Bulk DNA | Bottleneck dilution, both-strand calls | Genome-wide rare-mutation quantification ([[10-Summaries/hoang-2016-botseqs\|Hoang 2016]]) |
| [[10-Summaries/abascal-2021-nanoseq\|NanoSeq]] | 2021 | Bulk DNA | Duplex | Nuclear-genome duplex sequencing ([[10-Summaries/abascal-2021-nanoseq\|NanoSeq]]) |
| [[10-Summaries/maslov-2022-smm-seq\|SMM-seq]] | 2022 | Bulk DNA | Single-molecule, rolling-circle copies | Bulk detection of private somatic SNVs ([[10-Summaries/maslov-2022-smm-seq\|SMM-seq]]) |
| [[10-Summaries/hard-2023-long-read-scwgs\|Hård 2023]] | 2023 | Single cells | Droplet MDA + long reads | 27 phased somatic SNVs plus one mtDNA heteroplasmy separate two T-cell clones; no somatic SVs or TRs found between the clones ([[10-Summaries/hard-2023-long-read-scwgs\|Hård 2023]]) |
| [[10-Summaries/liu-2024-hidef-seq\|HiDEF-seq]] | 2024 | Bulk DNA | Single-molecule, no amplification | Reads single-strand mismatches and damage that precede mutations; duplex-family single-strand burdens inflated ~18-fold ([[10-Summaries/liu-2024-hidef-seq\|HiDEF-seq]]) |
| [[10-Summaries/nandi-2025-udseq\|UDSeq]] | 2025 | Bulk DNA | Duplex | Universal duplex library prep ([[10-Summaries/nandi-2025-udseq\|UDSeq]]) |
| [[10-Summaries/zhang-2025-smaht-duplex-benchmark\|SMaHT benchmark]] | 2025 | Bulk DNA | Cross-method comparison | SMaHT duplex-sequencing benchmark ([[10-Summaries/zhang-2025-smaht-duplex-benchmark\|Zhang 2025]]) |
| [[10-Summaries/liu-2025-nanopore-lscc-svs\|SomaGauss-SV]] | 2025 | Paired tumour–blood | Nanopore long reads | Somatic SVs in LSCC; smoking correlates with deletion burden ([[10-Summaries/liu-2025-nanopore-lscc-svs\|Liu 2025]]) |

HiDEF-seq shifts the object of study one step upstream, from mutations to the **single-strand mismatches and damage that precede them**: double-strand mutations are the endpoint of lesion formation, DNA repair and replication, so dsDNA signatures need not reflect the originating events, and until 2024 no method could read those events because every method amplified first ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]). For the corpus, single-strand burden estimates from duplex-family methods are inflated ~18-fold ([[10-Summaries/liu-2024-hidef-seq|HiDEF-seq]]), and neuronal somatic SNV rates from MDA-era data were overestimated ([[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]) (synthesis).

## Mosaicism × epigenome: an open gap

Most mosaicism literature treats epigenetic state as an *annotation* used to interpret a mosaic genotype's likely consequences (is the mutation in an enhancer, a promoter, a heterochromatic region?). Very little work has measured **both somatic mutation and epigenetic state in the same single cell** as a direct biological measurement (synthesis). The methodological pieces exist:

| Assay | Year | Layers in one cell | Note |
|---|---|---|---|
| [[10-Summaries/hou-2016-sctrio-seq\|scTrio-seq]] | 2016 | CNV + methylome + transcriptome | Closest existing precedent; CNVs drive proportional expression dosage but do *not* perturb DNA methylation in the same region; tumour-only, not applied to neuronal or developmental mosaicism ([[10-Summaries/hou-2016-sctrio-seq\|Hou 2016]]) |
| [[10-Summaries/clark-2018-scnmt-seq\|scNMT-seq]] | 2018 | Methylation + accessibility + RNA (no mutation) | ([[10-Summaries/clark-2018-scnmt-seq\|Clark 2018]]) |
| [[10-Summaries/izzo-2024-got-cha\|GoT–ChA]] | 2024 | Targeted SNV + accessibility | Applied to clonal-hematopoiesis JAK2/CALR but not to broader mosaicism contexts; see [[30-Concepts/got-cha]] ([[10-Summaries/izzo-2024-got-cha\|Izzo 2024]]) |
| [[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]] | 2024 | CNA + chromatin accessibility | In two normal breasts 0.75% and 0.45% of cells were aneuploid, all LumSec with chr1q gain; chrX-loss T cells and pericytes in ER+ tumours; a genome-wide CNA (not SNV) instance of the pairing ([[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]]) |
| [[10-Summaries/bohaczuk-2024-targeted-fiberseq\|Targeted Fiber-seq]] | 2024 | Haplotype-phased sequence + chromatin on the same fiber | A somatically unstable DMPK CTG expansion of >1000 repeats ablates a putative SIX5 enhancer and halves CTCF occupancy (52% to 24% of fibers); a ~60-repeat allele shows no change ([[10-Summaries/bohaczuk-2024-targeted-fiberseq\|Bohaczuk 2024]]) |
| [[10-Summaries/swanson-2025-daf-seq\|DAF-seq]] | 2025 | DNA sequence + chromatin state on the same fiber | Single-cell single-molecule deamination footprinting; the low-VAF CC>TT CTCF-ablating variant in COLO829 is the prototype direct observation; see [[30-Concepts/daf-seq]] ([[10-Summaries/swanson-2025-daf-seq\|Swanson 2025]]) |
| [[10-Summaries/kriz-2025-duplex-multiome\|Duplex-Multiome]] | 2025 | Mutation + accessibility + RNA | Duplex consensus sequencing integrated into 10x Multiome; begins to close the single-cell duplex gap, within accessible chromatin ([[10-Summaries/kriz-2025-duplex-multiome\|Kriz 2025]]) |
| [[10-Summaries/shen-2026-splicool-seq\|SpliCOOL-seq]] | 2026 | Multi-layer epigenome (no mutation) | ([[10-Summaries/shen-2026-splicool-seq\|Shen 2026]]) |

What is missing:

- No single-cell assay yet **jointly** measures somatic point mutations (the predominant mosaicism variant class) and chromatin or methylation state genome-wide; the closest are GoT–ChA (targeted) and DAF-seq (single-fiber, ~genome scale per cell but ≤12 cells deeply benchmarked) ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]; [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- No systematic study yet asks whether **a mosaic mutation perturbs its own local epigenome at the single-cell level**; bulk-tumour evidence is mixed (CNV does not affect methylation per scTrio-seq, but point mutations might) ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]).
- The neuro-mosaicism field uses bulk epigenome annotations rather than paired single-cell measurements ([[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto 2022]]).

This is the gap the review this wiki supports aims to articulate: **a DNA-centric framing where the locus is the unit and mutation + accessibility + methylation + 3D position are layers of the same per-cell state** (synthesis). See [[40-Topics/single-cell-multiomics]].

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
- [[20-Entities/smaht-network]] — NIH consortium for a somatic mosaicism atlas.

## Open questions

- **Single-cell duplex sequencing** — duplex needs both strands, and scWGA loses strand identity, so this was the single biggest method gap (see [[40-Topics/duplex-sequencing]] open questions). Duplex-Multiome has begun to close it: it calls somatic SNVs by duplex consensus inside single nuclei, but only from accessible chromatin and sparsely per nucleus ([[10-Summaries/kriz-2025-duplex-multiome|Kriz 2025]]). Whether a genome-wide single-cell duplex method is possible remains open (synthesis).
- Tissue-specific mosaic mutation rates: high in skin (UV) and intestine (turnover); uncertain in many other tissues.
- The threshold (mosaic VAF, gene set) at which mosaicism becomes diagnostically actionable is still empirical ([[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]).
- Whether age-related mosaic accumulation *causes* aging-related disease or is a *biomarker* — the distinction matters for therapeutic strategies ([[10-Summaries/vijg-2020-cell|Vijg & Dong 2020]]; [[10-Summaries/cagan-2022-nature|Cagan 2022]]).
- IRE1–XBP1 as a therapeutic target in CALR-mutant clonal hematopoiesis is a hypothesis ([[10-Summaries/nam-2019-got|Nam 2019]]) with no clinical validation in the wiki yet.
- Why CALR's fitness advantage is differentiation-dependent in ET but already strong at the HSPC level in MF.
- Whether JAK2V617F chromatin priming in HSCs is causal for clonal expansion or downstream of it ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- Pre-implantation genetic screening from a single embryo cell is at preprint stage and awaits clinical validation ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

## Related

> [!cards]
> - `hub` [[40-Topics/clonal-hematopoiesis|Clonal hematopoiesis]] — Age-related mosaic expansion of an HSC clone carrying a recurrent somatic driver.
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Technologies that interrogate the DNA of single cells, by amplification or single-molecule reading.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — Strand-paired single-molecule sequencing for low-VAF mutation detection.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Two or more molecular modalities measured in the same single cell.

## All sources on this page

> [!info]- 46 summaries cited here
> - [[10-Summaries/abascal-2021-nanoseq|Abascal 2021]]
> - [[10-Summaries/bae-2017-pregastrulation-mutations|Bae 2018]]
> - [[10-Summaries/bizzotto-2022-brain-mosaicism-review|Bizzotto & Walsh 2022]]
> - [[10-Summaries/bohaczuk-2024-targeted-fiberseq|Bohaczuk 2024]]
> - [[10-Summaries/cagan-2022-nature|Cagan 2022]]
> - [[10-Summaries/campbell-2015-mosaicism-review|Campbell 2015]]
> - [[10-Summaries/clark-2018-scnmt-seq|Clark 2018]]
> - [[10-Summaries/coorens-2021-nature|Coorens 2021]]
> - [[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]
> - [[10-Summaries/fischbach-2026-alphagenome-aging|Fischbach 2026]]
> - [[10-Summaries/forsberg-2017-mosaicism-review|Forsberg 2017]]
> - [[10-Summaries/gillman-2026-scarce|Gillman 2026]]
> - [[10-Summaries/glynos-2023-mtdna-mosaicism|Glynos 2023]]
> - [[10-Summaries/hard-2023-long-read-scwgs|Hård 2023]]
> - [[10-Summaries/hilal-2026-cardiac-somatic-review|Hilal 2026]]
> - [[10-Summaries/hoang-2016-botseqs|Hoang 2016]]
> - [[10-Summaries/hou-2016-sctrio-seq|Hou 2016]]
> - [[10-Summaries/hsieh-2026-scmtmpm-scwmss|Hsieh 2026]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
> - [[10-Summaries/kapadia-2024-stem-cell-aging|Kapadia & Goodell 2024]]
> - [[10-Summaries/kennedy-2014-duplex-protocol|Kennedy 2014]]
> - [[10-Summaries/kousi-2022-ad-mosaicism|Kousi 2022]]
> - [[10-Summaries/kriz-2025-duplex-multiome|Kriz 2025]]
> - [[10-Summaries/lee-six-2018-hsc-dynamics|Lee-Six 2018]]
> - [[10-Summaries/liu-2024-hidef-seq|Liu 2024]]
> - [[10-Summaries/liu-2025-nanopore-lscc-svs|Liu 2025]]
> - [[10-Summaries/lodato-2017-aging-neurons|Lodato 2018]]
> - [[10-Summaries/ludwig-2020-mtscatac-seq|Lareau & Ludwig 2021]]
> - [[10-Summaries/luquette-2022-neuron-scan2-indels|Luquette 2022]]
> - [[10-Summaries/luquette-2025-pta-duplex-mosaicism|Luquette 2025]]
> - [[10-Summaries/maslov-2022-smm-seq|Maslov 2022]]
> - [[10-Summaries/mckenna-2016-science|McKenna 2016]]
> - [[10-Summaries/mukamel-2025-aneuploidy-brain|Mukamel 2025]]
> - [[10-Summaries/muyas-2024-scomatic|Muyas 2024]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
> - [[10-Summaries/nam-2022-natgenet|Nam 2022]]
> - [[10-Summaries/nandi-2025-udseq|Nandi 2025]]
> - [[10-Summaries/oroak-2012-autism-targeted-seq|O'Roak 2012]]
> - [[10-Summaries/schmitt-2012-pnas|Schmitt 2012]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/shen-2026-splicool-seq|Shen 2026]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
> - [[10-Summaries/taejeong-2022-science|Bae 2022]]
> - [[10-Summaries/vijg-2020-cell|Vijg & Dong 2020]]
> - [[10-Summaries/wang-2024-wellda-seq|Wang 2024]]
> - [[10-Summaries/zhang-2025-smaht-duplex-benchmark|Zhang 2025]]
