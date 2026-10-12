---
type: concept
title: Intratumor Heterogeneity
aliases: [intratumour heterogeneity, ITH, subclonal structure, clonal architecture]
tags: [cancer, clonal-evolution, subclones, single-cell]
created: 2026-08-10
updated: 2026-10-12
---

# Intratumor Heterogeneity

> Genetic and phenotypic variation between cells within one tumour. The reason single-cell cancer genomics exists, and — importantly — a quantity whose measured magnitude depends heavily on how many cells were sequenced ([[10-Summaries/xu-2012-single-cell-exome-kidney|Xu 2012]]; [[10-Summaries/zahn-2017-dlp|Zahn 2017]]; [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).

> [!abstract] 한눈에
> Intratumor heterogeneity는 한 종양 안의 세포들이 유전적·표현형적으로 서로 다른 정도이고, 측정되는 크기는 몇 개의 세포를 시퀀싱했는지에 크게 좌우된다 ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]; [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]). bulk 데이터는 비슷한 빈도의 clone을 구분하지 못하므로, 공존하는 여러 clone의 구조는 single-cell 데이터로만 드러난다 ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).

## Definition

Intratumor heterogeneity is genetic and phenotypic variation between cells within one tumour (synthesis). It appears at the karyotype level: 56% of cells in a chromosomally unstable lymphoma carried a unique karyotype, invisible to array CGH on the same tumour ([[10-Summaries/bakker-2016-aneufinder|AneuFinder]]); see [[chromosomal-instability]]. It also appears at the point-mutation level: in breast cancer, aneuploid rearrangements arise early and remain highly stable through clonal expansion, while point mutations accumulate gradually — **two clocks running at different speeds in the same tumour** ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]). Clonality survives at the copy-number level and fails at the point-mutation level in the same cells; no two single tumour cells are genetically identical ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]).

## Why it matters

- Mutations at different allele frequencies show different mutation spectra, read as selection during progression ([[10-Summaries/xu-2012-single-cell-exome-kidney|Xu 2012]]).
- Fitness-associated alterations can be identified from lineage structure and predict patient survival ([[10-Summaries/wang-2021-medalt|MEDALT]]).
- Bulk deconvolution cannot recover what pooling destroys — the clearest demonstration being minor clones absent from a merged genome built from the very cells that contain them ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- **Population recurrence does not predict the individual tumour.** A textbook ccRCC lacked both canonical drivers — no *VHL* coding mutation, *PBRM1* only at <4% allele frequency and no chromosome 3 LOH — while genes rarely mutated at the population level (*AHNAK*, *SRGAP3*) carried high-frequency mutant alleles ([[10-Summaries/xu-2012-single-cell-exome-kidney|Xu 2012]]). This is the argument for individual-level rather than panel-based molecular diagnosis (synthesis).

## Detection approaches

Detection is sampling-limited: what a study sees depends on its cells-versus-depth design ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]; [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).

| Design | Example | What it resolves | Source |
|---|---|---|---|
| Few cells, exome | [[10-Summaries/xu-2012-single-cell-exome-kidney\|Xu 2012]] | 17 cells in a ccRCC; diffuse diversity without subpopulations | ([[10-Summaries/xu-2012-single-cell-exome-kidney\|Xu 2012]]) |
| Depth per cell | [[10-Summaries/wang-2014-nuc-seq\|Wang 2014]] | 4–59 nuclei at 91% breadth; copy-number versus point-mutation clocks in the same cells | ([[10-Summaries/wang-2014-nuc-seq\|Wang 2014]]) |
| Cells per experiment, targeted loci | [[10-Summaries/gawad-2014-all-clonal-origins\|Gawad 2014]] | 1,479 cells; codominant clone architecture | ([[10-Summaries/gawad-2014-all-clonal-origins\|Gawad 2014]]) |
| Many shallow cells | [[10-Summaries/zahn-2017-dlp\|Zahn 2017]] | 6,000 cells at 0.05× give ~0.05% subclone sensitivity | ([[10-Summaries/zahn-2017-dlp\|Zahn 2017]]) |
| Bulk low-allele-fraction calling | [[10-Summaries/cibulskis-2013-mutect\|MuTect]] | Subclonal mutations in bulk, given sensitivity at low allele fraction | ([[10-Summaries/cibulskis-2013-mutect\|MuTect]]) |
| Single-cell phylogenies | [[10-Summaries/kang-2022-sieve\|SIEVE]], [[10-Summaries/zafar-2019-siclonefit\|SiCloneFit]] | Heterogeneity resolved cell by cell on a tree; migration histories when combined with MACHINA | ([[10-Summaries/kang-2022-sieve\|SIEVE]]; [[10-Summaries/zafar-2019-siclonefit\|SiCloneFit]]) |
| Per-cell copy-number calling | [[10-Summaries/ivanovic-2025-cnrein\|CNRein]], [[10-Summaries/liu-2024-cot\|CoT]] | Clones from per-cell copy-number profiles; evolution-aware calling limits spurious unique profiles | ([[10-Summaries/ivanovic-2025-cnrein\|CNRein]]; [[10-Summaries/liu-2024-cot\|CoT]]) |
| Karyotype from scATAC-seq | [[10-Summaries/ramakrishnan-2023-epianeufinder\|epiAneufinder]] | CNA heterogeneity inferred from chromatin-accessibility reads | ([[10-Summaries/ramakrishnan-2023-epianeufinder\|epiAneufinder]]) |
| ecDNA from single-cell Hi-C | [[10-Summaries/chang-2025-droplet-hi-c\|Droplet Hi-C]] | How ecDNA species are distributed and change within a tumour population | ([[10-Summaries/chang-2025-droplet-hi-c\|Chang 2025]]) |
| Same-cell DNA + ATAC | [[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]] | How tightly chromatin state tracks genotype across subclones | ([[10-Summaries/wang-2024-wellda-seq\|wellDA-seq]]) |

**Design rule for clone detection:** ~200 cells to detect a 1% clone, 75 for 2%, 50 for 4% — roughly 2–3 cells from a clone are needed to call it, and mutation count stops mattering above ~30 ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).

## Evidence and examples

**Sampling and sensitivity**

- **17 cells found no subclonal structure** in a clear cell renal carcinoma: PCA and neighbour-joining both showed diffuse diversity without discernible subpopulations, interpreted as fast malignant transition followed by passenger accumulation ([[10-Summaries/xu-2012-single-cell-exome-kidney|Xu 2012]]).
- **6,000 cells at 0.05× gives ~0.05% subclone sensitivity**, and costs the same as ten cells at 30× ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- Clones at 6% and 4% of a xenograft were resolvable in 296 cells, and were undetectable in the merged profile of the same libraries ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- MuTect detected 53.2% of AF-0.1 mutations at 30× versus 29.7% (Strelka), 16.8% (JointSNVMix) and 7.4% (SomaticSniper) at matched false-positive rates ([[10-Summaries/cibulskis-2013-mutect|MuTect]]).

**Clonal architecture**

- **Five of six childhood ALL patients had ≥2 clones each comprising ≥25% of cells.** Codominance, not one dominant clone with minor satellites, is the normal architecture — and bulk allele frequencies structurally cannot resolve it, because clones at similar frequency produce mutations at similar VAF ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).
- SIEVE recovered biopsy-matched clades in a 28-cell colorectal scWGS dataset ([[10-Summaries/kang-2022-sieve|SIEVE]]).
- Applied to two metastatic colorectal cancers, SiCloneFit with MACHINA inferred polyclonal single-source seeding from colon to liver (migration number 2, comigration 1) and a recurrent GATA1 mutation not reported by the original SCITE analysis ([[10-Summaries/zafar-2019-siclonefit|SiCloneFit]]).
- On real data CNRein's largest clone was 41 of 617 cells in DLP+ ovarian cancer OV2295 but 276 of 785 cells in 10x breast cancer S0; the authors relate this to extensive heterogeneity in high-grade serous ovarian cancer and punctuated evolution in breast cancer ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]).
- On 10x breast tumour section E, CoT resolved 8 clusters where the regrouped CHISEL labels had 5, including subclones that differ only on chromosome 11 ([[10-Summaries/liu-2024-cot|CoT]]).

**Heterogeneity in other layers**

- Karyotype clusters inferred from scATAC-seq of two basal cell carcinomas showed high CNA heterogeneity in one patient and low in the other, with cancer-associated fibroblasts falling into non-disomic clusters ([[10-Summaries/ramakrishnan-2023-epianeufinder|epiAneufinder]]).
- In GBM39 under erlotinib, *EGFR* ecDNA nearly disappeared, *MDM2* ecDNA appeared only in resistant cells, and *MYC* ecDNA boundaries became highly variable between cells ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).
- In 4.7% of cells in one Droplet Hi-C cluster, *MYC* and *EGFR* ecDNA co-occurred ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).
- Across 9 ER+ breast tumours, the correlation between subclone-pairwise CNA and ATAC distances ranged 0.43–0.99, about half being highly concordant ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).
- On average 82.27% of bins with differentially accessible chromatin hubs between subclones lay in subclonal CNA bins, whereas only 25.12% of subclonal CNA bins showed such hub changes ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).
- ROS, myogenesis, apoptosis and P53 programs were recurrently heritable along CNA lineages, while G2M checkpoint, coagulation, EMT and interferon-gamma response were recurrently plastic ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).

## Contested points

- **Few-cell and many-cell results are compatible.** The 17-cell ccRCC finding of no subclonal structure ([[10-Summaries/xu-2012-single-cell-exome-kidney|Xu 2012]]) and DLP's ~0.05% subclone sensitivity ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]) do not conflict; the resolution differs by two orders of magnitude (synthesis).
- **Codominance breaks the linear-succession model.** If the fittest clone always sweeps, two clones would not each hold a quarter of the tumour. What sustains the balance is unresolved; a *KRAS*-mutant clone coexisting with a *RAB27B*-mutant sibling hints at parallel adaptive peaks ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]) (synthesis).
- **Per-cell copy-number callers can overstate heterogeneity.** In simulations where 1000 cells had 490 distinct true profiles, SIGNALS and CHISEL each called a unique profile for every cell, while the evolution-aware CNRein called 565 ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]); see [[copy-number-variation]].
- **Extra clones need orthogonal confirmation.** No orthogonal data confirm the additional clones CoT resolves beyond the CHISEL labels ([[10-Summaries/liu-2024-cot|CoT]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromosomal-instability|Chromosomal instability]] — The rate of mis-segregation, as opposed to aneuploidy, the resulting state.
> - `concept` [[30-Concepts/copy-number-variation|Copy-number variation]] — Gains and losses of genomic segments; the most tractable single-cell readout.
> - `concept` [[30-Concepts/phylogenetic-inference|Phylogenetic inference]] — Reconstructing a cell-division tree from heritable markers.
> - `hub` [[40-Topics/cancer-clonal-evolution|Cancer clonal evolution]] — Somatic mutation and clonal selection reconstructed from bulk and single-cell DNA.

## All sources on this page

> [!info]- 14 summaries cited here
> - [[10-Summaries/bakker-2016-aneufinder|Bakker 2016]]
> - [[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]
> - [[10-Summaries/cibulskis-2013-mutect|Cibulskis 2013]]
> - [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]
> - [[10-Summaries/ivanovic-2025-cnrein|Ivanovic & El-Kebir 2025]]
> - [[10-Summaries/kang-2022-sieve|Kang 2022]]
> - [[10-Summaries/liu-2024-cot|Liu 2024 (Brief Bioinform)]]
> - [[10-Summaries/ramakrishnan-2023-epianeufinder|Ramakrishnan 2023]]
> - [[10-Summaries/wang-2014-nuc-seq|Wang 2014]]
> - [[10-Summaries/wang-2021-medalt|Wang 2021]]
> - [[10-Summaries/wang-2024-wellda-seq|Wang 2024]]
> - [[10-Summaries/xu-2012-single-cell-exome-kidney|Xu 2012]]
> - [[10-Summaries/zafar-2019-siclonefit|Zafar 2019]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
