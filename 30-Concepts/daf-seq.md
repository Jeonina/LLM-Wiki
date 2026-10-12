---
type: concept
title: DAF-seq (Deaminase-Assisted single-molecule chromatin Fiber sequencing)
aliases: [DAF-seq, scDAF-seq]
tags: [single-molecule, single-cell, chromatin, deaminase, footprinting, method]
created: 2026-05-07
updated: 2026-10-12
---

# DAF-seq (Deaminase-Assisted single-molecule chromatin Fiber sequencing)

> Single-molecule chromatin footprinting method that uses the dsDNA cytidine deaminase **SsDddA** to stencil protein occupancy as C→T sequence changes, which, unlike methylation marks, **survive DNA amplification** and so enable a single-cell extension (scDAF-seq) covering up to 99% of an individual cell's genome ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).

> [!abstract] 한눈에
> DAF-seq는 deaminase로 열린 DNA의 C를 T로 바꿔 단백질이 앉은 자리를 서열 변화로 기록하는 single-molecule footprinting이며, 이 표지는 증폭 뒤에도 남기 때문에 한 세포 유전체의 최대 99%를 읽을 수 있다 ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]). 아직 lymphoblastoid 세포 12개에서만 보였고, 세포 수와 비용을 늘릴 수 있는지는 열린 문제다 ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).

## Definition

SsDddA (a *Simiaoa sunii* DddA variant, expressed in *E. coli*) deaminates accessible cytidines in nuclei to uridine; subsequent PCR or whole-genome amplification converts these to thymidine, producing C→T changes on the top strand and G→A changes on the bottom strand of accessible DNA ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]). Nucleosome- and TF-protected DNA escapes deamination, so the deamination pattern along a fiber is a **near-nucleotide-resolution footprint of protein occupancy** ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).

## Why it matters

- **Marks that survive amplification.** Prior single-molecule chromatin footprinting methods (notably [[fiber-seq]] and other methyltransferase stencilers) lose their marks during DNA amplification, so they are stuck as bulk assays covering ~0.001% of a single cell's genome ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]). Deamination produces *sequence* changes, not modifications, so it survives amplification; this is the change that makes chromosome-scale single-cell single-molecule chromatin profiling possible ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Genotype and chromatin from the same fiber.** Top and bottom strands are distinguished by C→T versus G→A patterns, so haplotype phasing from a single C/T heterozygous variant works directly ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]). This is a different solution to the single-cell genotype–phenotype linking problem that [[got]] and [[got-cha]] address with droplet barcoding (synthesis).

## Operational modes

| Mode | Workflow | Depth / coverage | Source |
|---|---|---|---|
| Targeted DAF-seq | Bulk single-molecule assay with PCR enrichment of chosen loci | >25,000× single-molecule depth; resolves TF cooperativity, haplotype-specific actuation and low-VAF mosaic variant impact | ([[10-Summaries/swanson-2025-daf-seq\|Swanson 2025]]) |
| scDAF-seq | SsDddA-treated single cells sorted by FACS, amplified by primary template-directed amplification (PTA), sequenced on PacBio | ~99% of the mappable autosomal genome per cell; consensus reads with N50 up to 34.5 kb | ([[10-Summaries/swanson-2025-daf-seq\|Swanson 2025]]) |
| FOODIE (short-read counterpart) | DddB deamination after Tn5 tagmentation; cooperativity measured only for footprint pairs within one fragment | — | ([[10-Summaries/he-2024-foodie\|FOODIE]]) |

- **Reaction conditions.** 4 μM SsDddA for 10 min was optimal across the NAPA and WASF1 promoter benchmarks ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Deamination pattern as UMI.** In scDAF-seq each unique deamination pattern serves as a per-fiber UMI, which enables consensus-read assembly ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Enzyme choice matters for cooperativity.** FOODIE rejected a processive deaminase because correlated conversion would mimic cooperativity ([[10-Summaries/he-2024-foodie|FOODIE]]).

## Evidence and examples

- **NAPA promoter cooperativity.** Thermodynamic analysis identified a 180,000× cooperative binding interaction between elements 1 and 2 ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **SLC39A4 eQTL mechanism.** The rs2280838-T haplotype increases liver expression by altering nucleosome positioning over the promoter, visible as a chromatin epiallele only at single-molecule resolution ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Low-VAF mosaic variant.** A 1.5% VAF CC→TT mutation in a COLO829 BL/T mixture ablates a CTCF binding element, with chromatin loss visible only on the variant reads ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Pervasive plasticity.** Regulatory-element actuation differs by ~63% between cells and by ~61% between the two haplotypes within the same cell ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).

## Contested points

- **Cell throughput.** scDAF-seq sequenced 12 cells (eight at median 12 Gb, two at ~22 Gb, one at 91 Gb, one at 133 Gb); whether the method scales to hundreds or thousands of cells is unclear ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Cost.** Each deeply sequenced cell consumed ~91–133 Gb of PacBio HiFi data, so the economics of cohort-scale studies are not established ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).
- **Generalisation.** Generalisation to primary tissue is not yet demonstrated; all scDAF-seq cells profiled are GM24385 lymphoblastoid ([[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/fiber-seq|Fiber-seq]] — Methodological ancestor; m6A methyltransferase stenciling, bulk only.
> - `concept` [[30-Concepts/single-molecule-footprinting|Single-molecule footprinting]] — Assays that mark accessible DNA on individual fibers and read them with long reads.
> - `concept` [[30-Concepts/chromatin-actuation|Chromatin actuation]] — An element being open and bound on a specific fiber, as DAF-seq measures it.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Whether DNA is open or nucleosome-bound; the underlying signal.
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Droplet-scale alternative for linking sequence to chromatin in single cells.
> - `concept` [[30-Concepts/got|GoT]] — Droplet-based linking of somatic genotype to the single-cell transcriptome.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA is packaged along fibers, haplotypes and cells.

People: [[20-Entities/elliott-g-swanson|Elliott G. Swanson]] · [[20-Entities/andrew-b-stergachis|Andrew B. Stergachis]].

## All sources on this page

> [!info]- 2 summaries cited here
> - [[10-Summaries/he-2024-foodie|He 2024]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
