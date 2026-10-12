---
type: concept
title: Lamina-associated domains (LADs)
aliases: [LAD, LADs, lamina associated domain, fLAD, cLAD, facultative LAD, constitutive LAD]
tags: [nuclear-architecture, heterochromatin, H3K9me3, H3K27me3, lamina, single-cell, DamID]
created: 2026-05-15
updated: 2026-10-12
---

# Lamina-associated domains (LADs)

> **LADs** are large, gene-poor, A/T-rich and transcriptionally repressed genomic regions (10 kb – 10 Mb, median ~0.5 Mb) that physically contact the **nuclear lamina**, the meshwork of intermediate-filament lamins (LMNA/B1/B2) lining the inner nuclear membrane ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).

> [!abstract] 한눈에
> LAD는 핵막 안쪽 lamina에 붙어 있는 큰 유전체 구간으로, 유전자가 적고 전사가 억제되어 있으며 한 세포 유형에서 유전체의 3분의 1 이상을 차지한다 ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]). Single-cell DamID로 보면 lamina 접촉은 세포마다 달라지고, 전사와의 음의 관계는 접촉 빈도가 낮은 fLAD에 몰려 있다 ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [3D 유전체 교재](../60-Explainers/3d-genome.html)
<!-- /explainer-links -->

## Definition

LADs cover more than one-third of the mouse and human genome in individual cell types ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]). Across an isogenic ESC → NPC → astrocyte lineage plus fibroblasts, a cell type has ~1,100–1,400 LADs of 40 kb to 15 Mb, covering ~40% of the genome and containing 13–18% of all genes at 5–10× lower median expression ([[10-Summaries/peric-hupkes-2010-lad-differentiation|Peric-Hupkes 2010]]). They were mapped originally by bulk DamID and resolved at the single-cell level by scDamID ([[10-Summaries/de-luca-2021-scdamid-protocol|de Luca 2021]]) and scDam&T-seq ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]). The canonical review is van Steensel & Belmont 2017 ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).

## Why it matters

LAD attachment is one principal axis of the **DNA locus state** framework, alongside genetic state and chromatin-mark state (synthesis; see [[50-Notes/regulatory-layers-overview]] for the structural-physical axis):

- **Genetic axis** — sequence variants, CNV, allelic state (synthesis).
- **Epigenetic axis** — methylation, histone marks, accessibility (synthesis).
- **Structural axis** — 3D contact, NL position and biophysical properties; LADs sit at the intersection of 3D position (peripheral vs interior) and chromatin state (heterochromatic vs euchromatic) (synthesis).

In single-cell experiments this becomes a measurable question: in a given cell, is this locus at the lamina or in the nucleoplasm, and how does that correlate with whether it is transcribed ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]])?

## Two flavors

| Type | Definition | Marks | Cell-type behavior |
|---|---|---|---|
| **cLAD (constitutive)** | High contact frequency across most cells of most lineages ([[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]]) | H3K9me3 enriched ([[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]]) | Stable, A/T-rich gene deserts; positions conserved mouse–human ([[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]]) |
| **fLAD (facultative)** | Cell-type-specific NL contact; variable across cells of the same type ([[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]]) | H3K27me3 enriched at boundaries ([[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]]) | Dynamic; release from NL ↔ transcriptional activation ([[10-Summaries/rooijers-2019-scdamt-seq\|Rooijers 2019]]) |

This distinction is **load-bearing**: single-cell analysis shows the negative coupling between NL contact and transcription is concentrated in **low-CF fLADs**, not in cLADs ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]). cLADs are inert heterochromatin floors; fLADs are the regulatable, transcription-relevant population (synthesis based on [[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]] + [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).

## Measurement methods

| Method | Principle | Resolution | Source |
|---|---|---|---|
| **DamID-seq** | Dam-LMNB1 fusion → m6A at GATC near the lamina → DpnI + sequencing | Bulk | ([[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]]; [[10-Summaries/de-luca-2021-scdamid-protocol\|de Luca 2021]]) |
| **scDamID** | Single-cell DamID; FACS into 96-well plates | Single cell; shows per-locus NL contact frequency varies cell to cell | ([[10-Summaries/de-luca-2021-scdamid-protocol\|de Luca 2021]]) |
| **scDam&T-seq** | Adds the same cell's transcriptome via IVT linear amplification | Single cell | ([[10-Summaries/rooijers-2019-scdamt-seq\|Rooijers 2019]]) |
| **TSA-seq** | Proximity labeling via biotin-tyramide radicals; orthogonal NL-distance readout | — | (synthesis; described as an alternative axis in [[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]]) |
| **Microscopy / FISH** | Direct spatial measurement | Low throughput per locus | ([[10-Summaries/van-steensel-2017-lads-review\|van Steensel 2017]]) |

## Anchoring mechanisms

- H3K9 methylation is the primary chromatin mark recruiting LADs to the NL; G9a (H3K9me2) and SUV39H1/2 (H3K9me3) act **redundantly**, and only triple knockdown peels the HBB LAD from the NL ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).
- NL proteins (lamins, LBR, emerin) also act redundantly; a mouse ES cell lamin triple-KO has a marginal effect on NL contacts ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).
- LADs occupy **Hi-C compartment B**, and NL contact maps and A/B-compartment maps are nearly identical at megabase scale ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).
- A subset of TAD boundaries coincides with LAD/non-LAD transitions ([[10-Summaries/dixon-2012-tads|Dixon 2012]]).
- NADs cover about 40% of the human genome and overlap LADs substantially; LADs can move to daughter-cell nucleoli after mitosis, so nucleolus and lamina may act as interchangeable heterochromatin scaffolds ([[10-Summaries/bersaglieri-2019-cells|Bersaglieri 2019]]).

## Evidence and examples

**Cell-to-cell heterogeneity**

- LAD nuclear position is partially randomized after each mitosis ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).
- ~15% of the genome, predominantly cLADs with <1 gene/Mb, acts as robust anchors contacting the NL in nearly every cell ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]).
- Within a single cell, NL contact of low-CF fLADs is associated with lower expression of their genes; this is an association, and temporal order and causality are not shown ([[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]).
- **Lamin depletion raises chromatin conformational heterogeneity** at nearly all genomic separations ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]), supporting the lamina's role as a structural anchor.

**Change across differentiation**

- LAD overlap between cell types is 73–87%, so the architecture is largely shared, with hundreds of gene-sized relocation events layered on it ([[10-Summaries/peric-hupkes-2010-lad-differentiation|Peric-Hupkes 2010]]).
- Replication timing correlates globally with LAD organization but does not follow the sharp LAD borders, so near boundaries it does not predict lamina contact ([[10-Summaries/peric-hupkes-2010-lad-differentiation|Peric-Hupkes 2010]]).

## Open questions

- **Is LAD membership binary?** The cLAD/fLAD distinction is categorical in the 2017 review, but single-cell DamID shows a continuous spectrum of contact frequencies; is cLAD-vs-fLAD a useful binary, or just the tails of one distribution ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]])? Peric-Hupkes et al. likewise call binary LAD classification an oversimplification: each locus has a probability of lamina contact, which population DamID cannot decompose into "some cells" versus "some of the time" ([[10-Summaries/peric-hupkes-2010-lad-differentiation|Peric-Hupkes 2010]]).
- **Size and coverage figures differ between sources.** The 2017 review gives 10 kb – 10 Mb and more than one-third of the genome ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]), while the 2010 differentiation maps give 40 kb – 15 Mb and ~40% ([[10-Summaries/peric-hupkes-2010-lad-differentiation|Peric-Hupkes 2010]]); the gap likely reflects cell types and calling thresholds rather than a real disagreement (synthesis).
- **Three-compartment competition.** Any heterochromatin compartment (NL, nucleolus, pericentromeric) may be sufficient for silencing ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]]); the nucleolar relocation of LADs after mitosis points the same way ([[10-Summaries/bersaglieri-2019-cells|Bersaglieri 2019]]). If true, mosaic mutations that shift a locus between compartments would *not* change regulation, but mutations that disrupt anchoring entirely would; the empirical test is missing (synthesis).
- **Laminopathies.** Does LBR / Lamin A/C redundancy mean laminopathies (HGPS, progeria) act through tissue-specific NL-protein composition rather than universal LAD disruption ([[10-Summaries/van-steensel-2017-lads-review|van Steensel 2017]])?

## Related

> [!cards]
> - `concept` [[30-Concepts/nuclear-lamina|Nuclear lamina]] — The meshwork of A- and B-type lamins and associated proteins that LADs contact.
> - `concept` [[30-Concepts/damid|DamID]] — Mapping protein–DNA contacts from the m6A footprint of a Dam fusion.
> - `concept` [[30-Concepts/scdamt-seq|scDam&T-seq]] — Protein–DNA contacts and transcriptome from the same single cell.
> - `concept` [[30-Concepts/conformational-heterogeneity|Conformational heterogeneity]] — A metric for cell-to-cell variability of 3D chromatin folding.
> - `concept` [[30-Concepts/chromatin-compartments|Chromatin compartments]] — A/B blocks; the B compartment closely matches LADs.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Histone marks, including the H3K9me3 vs H3K27me3 distinction.
> - `note` [[50-Notes/regulatory-layers-overview|Regulatory layers]] — The structural-physical axis among the axes of epigenome interpretation.

## All sources on this page

> [!info]- 7 summaries cited here
> - [[10-Summaries/bersaglieri-2019-cells|Bersaglieri & Santoro 2019]]
> - [[10-Summaries/de-luca-2021-scdamid-protocol|de Luca & Kind 2021]]
> - [[10-Summaries/dixon-2012-tads|Dixon 2012]]
> - [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]
> - [[10-Summaries/peric-hupkes-2010-lad-differentiation|Peric-Hupkes 2010]]
> - [[10-Summaries/rooijers-2019-scdamt-seq|Rooijers 2019]]
> - [[10-Summaries/van-steensel-2017-lads-review|van Steensel & Belmont 2017]]
