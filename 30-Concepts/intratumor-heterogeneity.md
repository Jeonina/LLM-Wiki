---
type: concept
title: Intratumor Heterogeneity
aliases: [intratumour heterogeneity, ITH, subclonal structure, clonal architecture]
tags: [cancer, clonal-evolution, subclones, single-cell]
created: 2026-08-10
updated: 2026-10-07
---

# Intratumor Heterogeneity

> Genetic and phenotypic variation between cells within one tumour. The reason single-cell cancer genomics exists, and — importantly — a quantity whose measured magnitude depends heavily on how many cells were sequenced.

## Detection is sampling-limited

- **17 cells found no subclonal structure** in a clear cell renal carcinoma: PCA and neighbour-joining both showed diffuse diversity without discernible subpopulations, interpreted as fast malignant transition followed by passenger accumulation ([[xu-2012-single-cell-exome-kidney]]).
- **6,000 cells at 0.05× gives ~0.05% subclone sensitivity**, and costs the same as ten cells at 30× ([[zahn-2017-dlp]]). The two results are compatible; the resolution differs by two orders of magnitude (synthesis).
- Clones at 6% and 4% of a xenograft were resolvable in 296 cells, and were undetectable in the merged profile of the same libraries ([[zahn-2017-dlp]]).

## Karyotype-level heterogeneity

56% of cells in a chromosomally unstable lymphoma carried a unique karyotype, invisible to array CGH on the same tumour ([[bakker-2016-aneufinder]]); see [[chromosomal-instability]].

## Population recurrence does not predict the individual tumour

A textbook ccRCC lacked both canonical drivers — no *VHL* coding mutation, *PBRM1* only at <4% allele frequency and no chromosome 3 LOH — while genes rarely mutated at the population level (*AHNAK*, *SRGAP3*) carried high-frequency mutant alleles ([[xu-2012-single-cell-exome-kidney]]). This is the argument for individual-level rather than panel-based molecular diagnosis (synthesis).

## Consequences

- Mutations at different allele frequencies show different mutation spectra, read as selection during progression ([[xu-2012-single-cell-exome-kidney]]).
- Fitness-associated alterations can be identified from lineage structure and predict patient survival ([[wang-2021-medalt]]).
- Bulk deconvolution cannot recover what pooling destroys — the clearest demonstration being minor clones absent from a merged genome built from the very cells that contain them ([[zahn-2017-dlp]]).

## Added 2026-10-07

Applied to two metastatic colorectal cancers, SiCloneFit with MACHINA inferred polyclonal single-source seeding from colon to liver (migration number 2, comigration 1) and a recurrent GATA1 mutation not reported by the original SCITE analysis ([[10-Summaries/zafar-2019-siclonefit]]).

Karyotype clusters inferred from scATAC-seq of two basal cell carcinomas showed high CNA heterogeneity in one patient and low in the other, with cancer-associated fibroblasts falling into non-disomic clusters ([[10-Summaries/ramakrishnan-2023-epianeufinder]]).

Single-cell Hi-C can track how ecDNA species are distributed and change within a tumor population. In GBM39 under erlotinib, *EGFR* ecDNA nearly disappeared, *MDM2* ecDNA appeared only in resistant cells, and *MYC* ecDNA boundaries became highly variable between cells ([[10-Summaries/chang-2025-droplet-hi-c]]). In 4.7% of cells in one cluster, *MYC* and *EGFR* ecDNA co-occurred ([[10-Summaries/chang-2025-droplet-hi-c]]).

Detecting subclonal mutations in bulk requires sensitivity at low allele fraction: MuTect detected 53.2% of AF-0.1 mutations at 30× versus 29.7% (Strelka), 16.8% (JointSNVMix) and 7.4% (SomaticSniper) at matched false-positive rates ([[10-Summaries/cibulskis-2013-mutect]]). Single-cell phylogenies resolve the same heterogeneity cell by cell; SIEVE recovered biopsy-matched clades in a 28-cell colorectal scWGS dataset ([[10-Summaries/kang-2022-sieve]]).

Same-cell DNA + ATAC profiling of 9 ER+ breast tumours quantified how tightly chromatin state tracks genotype: the correlation between subclone-pairwise CNA and ATAC distances ranged 0.43-0.99 across tumours, about half being highly concordant ([[10-Summaries/wang-2024-wellda-seq]]). On average 82.27% of bins with differentially accessible chromatin hubs between subclones lay in subclonal CNA bins, whereas only 25.12% of subclonal CNA bins showed such hub changes ([[10-Summaries/wang-2024-wellda-seq]]). ROS, myogenesis, apoptosis and P53 programs were recurrently heritable along CNA lineages, while G2M checkpoint, coagulation, EMT and interferon-gamma response were recurrently plastic ([[10-Summaries/wang-2024-wellda-seq]]).

## Related

- [[chromosomal-instability]] · [[copy-number-variation]] · [[phylogenetic-inference]] · [[cancer-clonal-evolution]]

## Added 2026-08-13

Two 2014 papers made complementary design choices and reached complementary conclusions about clonal architecture.

**Depth per cell** ([[10-Summaries/wang-2014-nuc-seq]], 4–59 nuclei at 91% breadth): aneuploid rearrangements arise early and remain highly stable through clonal expansion, while point mutations accumulate gradually — **two clocks running at different speeds in the same tumour**. Clonality survives at the copy-number level and fails at the point-mutation level in the same cells; no two single tumour cells are genetically identical ([[10-Summaries/wang-2014-nuc-seq]]).

**Cells per experiment** ([[10-Summaries/gawad-2014-all-clonal-origins]], 1,479 cells at targeted loci): **five of six childhood ALL patients had ≥2 clones each comprising ≥25% of cells**. Codominance, not one dominant clone with minor satellites, is the normal architecture — and bulk allele frequencies structurally cannot resolve it, because clones at similar frequency produce mutations at similar VAF ([[10-Summaries/gawad-2014-all-clonal-origins]]).

Codominance breaks the linear-succession model: if the fittest clone always sweeps, two clones would not each hold a quarter of the tumour. What sustains the balance is unresolved; a *KRAS*-mutant clone coexisting with a *RAB27B*-mutant sibling hints at parallel adaptive peaks ([[10-Summaries/gawad-2014-all-clonal-origins]]). (synthesis)

**Design rule for clone detection**: ~200 cells to detect a 1% clone, 75 for 2%, 50 for 4% — roughly 2–3 cells from a clone are needed to call it, and mutation count stops mattering above ~30 ([[10-Summaries/gawad-2014-all-clonal-origins]]).
