---
type: concept
title: Lamina-associated domains (LADs)
aliases: [LAD, LADs, lamina associated domain, fLAD, cLAD, facultative LAD, constitutive LAD]
tags: [nuclear-architecture, heterochromatin, H3K9me3, H3K27me3, lamina, single-cell, DamID]
created: 2026-05-15
updated: 2026-08-10
---

# Lamina-associated domains (LADs)

> **LADs** are large genomic regions (10 kb – 10 Mb, median ~0.5 Mb) that physically contact the **nuclear lamina** — the meshwork of intermediate-filament lamins (LMNA/B1/B2) lining the inner nuclear membrane ([[10-Summaries/van-steensel-2017-lads-review]]). They cover >35% of the mammalian genome ([[10-Summaries/van-steensel-2017-lads-review]]), are gene-poor, A/T-rich, and transcriptionally repressed ([[10-Summaries/van-steensel-2017-lads-review]]). Mapped originally by bulk DamID and resolved at single-cell level by scDamID ([[10-Summaries/de-luca-2021-scdamid-protocol]]) and scDam&T-seq ([[10-Summaries/rooijers-2019-scdamt-seq]]). Canonical review: [[10-Summaries/van-steensel-2017-lads-review|van Steensel & Belmont 2017]].

## Two flavors

| Type | Definition | Marks | Cell-type behavior |
|---|---|---|---|
| **cLAD (constitutive)** | High contact frequency across most cells of most lineages ([[10-Summaries/van-steensel-2017-lads-review]]) | H3K9me3 enriched ([[10-Summaries/van-steensel-2017-lads-review]]) | Stable, A/T-rich gene deserts; positions conserved mouse-human ([[10-Summaries/van-steensel-2017-lads-review]]) |
| **fLAD (facultative)** | Cell-type-specific NL contact; variable across cells of same type ([[10-Summaries/van-steensel-2017-lads-review]]) | H3K27me3 enriched at boundaries ([[10-Summaries/van-steensel-2017-lads-review]]) | Dynamic; release from NL ↔ transcriptional activation ([[10-Summaries/rooijers-2019-scdamt-seq]]) |

This distinction is **load-bearing**: single-cell analysis ([[10-Summaries/rooijers-2019-scdamt-seq]]) shows the negative coupling between NL contact and transcription is concentrated in **low-CF fLADs**, not in cLADs. cLADs are inert heterochromatin floors; fLADs are the regulatable, transcription-relevant population (synthesis based on [[10-Summaries/van-steensel-2017-lads-review]] + [[10-Summaries/rooijers-2019-scdamt-seq]]).

## Measurement methods

- **DamID-seq** (bulk) — Dam-LMNB1 fusion → m6A at GATC near lamina → DpnI + sequencing ([[10-Summaries/van-steensel-2017-lads-review]]; [[10-Summaries/de-luca-2021-scdamid-protocol]]).
- **scDamID** — single-cell version; FACS + 384-well; reveals per-locus NL contact frequency varies cell-to-cell ([[10-Summaries/de-luca-2021-scdamid-protocol]]).
- **scDam&T-seq** — adds same-cell transcriptome via IVT linear amplification ([[10-Summaries/rooijers-2019-scdamt-seq]]).
- **TSA-seq** — proximity labeling via biotin-tyramide radicals; orthogonal NL distance readout (synthesis; described as alternative axis in [[10-Summaries/van-steensel-2017-lads-review]]).
- **Microscopy / FISH** — direct spatial measurement; low-throughput per locus ([[10-Summaries/van-steensel-2017-lads-review]]).

## Why locus state at the lamina matters

LAD attachment is one principal axis of the **DNA locus state** framework alongside genetic state and chromatin-mark state (synthesis; see [[50-Notes/regulatory-layers-overview]] for the structural-physical axis discussion):

- **Genetic axis** — sequence variants, CNV, allelic state.
- **Epigenetic axis** — methylation, histone marks, accessibility.
- **Structural axis** — 3D contact, NL position, and biophysical properties. LADs sit at the intersection of 3D position (peripheral vs interior) and chromatin state (heterochromatic vs euchromatic).

In single-cell experiments this collapses to a measurable question: in a given cell, is this locus *at the lamina or in the nucleoplasm*, and how does that correlate with whether it is transcribed ([[10-Summaries/rooijers-2019-scdamt-seq]])?

## Heterogeneity findings

- LAD nuclear position is partially randomized after each mitosis ([[10-Summaries/van-steensel-2017-lads-review]]).
- ~15% of the genome — predominantly cLADs with <1 gene/Mb — acts as robust anchors contacting the NL in nearly every cell ([[10-Summaries/van-steensel-2017-lads-review]]).
- Detachment of fLADs from the NL precedes transcriptional activation; reattachment correlates with repression ([[10-Summaries/rooijers-2019-scdamt-seq]]).
- **Lamin depletion ↑ chromatin conformational heterogeneity** at nearly all genomic separations ([[10-Summaries/mali-2025-conformational-heterogeneity]]), supporting the lamina's role as a structural anchor.

## Anchoring mechanisms

- H3K9 methylation is the primary chromatin mark recruiting LADs to the NL. G9a (H3K9me2) and SUV39H1/2 (H3K9me3) act **redundantly** — only triple knockdown peels the HBB LAD from the NL ([[10-Summaries/van-steensel-2017-lads-review]]).
- NL proteins (lamins, LBR, emerin) also act redundantly; mouse ES cell lamin triple-KO has marginal effect on NL contacts ([[10-Summaries/van-steensel-2017-lads-review]]).
- LADs occupy **Hi-C compartment B**, with NL contact maps and A/B-compartment maps nearly identical at megabase scale ([[10-Summaries/van-steensel-2017-lads-review]]).

## Added 2026-08-10

[[10-Summaries/peric-hupkes-2010-lad-differentiation]] supplies the canonical figures — ~1,100–1,400 LADs per cell type, 40 kb to 15 Mb, ~40% of the genome, containing 13–18% of all genes at 5–10× lower median expression — across an isogenic ESC → NPC → astrocyte lineage plus fibroblasts. LAD overlap between cell types is 73–87%, so the architecture is largely shared with hundreds of gene-sized relocation events layered on it.

Two claims worth carrying forward: **replication timing correlates globally with LAD organization but does not follow the sharp LAD borders**, so near boundaries it is not a predictor of lamina contact; and **binary LAD classification is an oversimplification** — each locus has a probability of lamina contact, which population DamID cannot decompose into "some cells" versus "some of the time" ([[10-Summaries/peric-hupkes-2010-lad-differentiation]]). A subset of TAD boundaries coincides with LAD/non-LAD transitions ([[10-Summaries/dixon-2012-tads]]).


## Related

- [[30-Concepts/nuclear-lamina]] · [[30-Concepts/damid]] · [[30-Concepts/scdamt-seq]] · [[30-Concepts/conformational-heterogeneity]]
- [[40-Topics/histone-modifications]] (H3K9me3 vs H3K27me3 distinction) · [[30-Concepts/chromatin-compartments]] (B-compartment ≈ LAD)
- Sources: [[10-Summaries/van-steensel-2017-lads-review]] · [[10-Summaries/rooijers-2019-scdamt-seq]] · [[10-Summaries/de-luca-2021-scdamid-protocol]] · [[10-Summaries/mali-2025-conformational-heterogeneity]]
- [[50-Notes/regulatory-layers-overview]] — the structural-physical axis

## Open questions

- The cLAD/fLAD distinction is *categorical* in the 2017 review, but single-cell DamID shows a continuous spectrum of contact frequencies. Is cLAD-vs-fLAD a useful binary, or just the tails of one distribution? ([[10-Summaries/van-steensel-2017-lads-review]])
- Three-compartment competition: any heterochromatin compartment (NL, nucleolus, pericentromeric) may be sufficient for silencing ([[10-Summaries/van-steensel-2017-lads-review]]). If true, mosaic mutations that shift a locus between compartments would *not* change regulation — but mutations that disrupt anchoring entirely would. Empirical test missing (synthesis).
- Does LBR / Lamin A/C redundancy mean laminopathies (HGPS, progeria) act through tissue-specific NL-protein composition rather than universal LAD disruption ([[10-Summaries/van-steensel-2017-lads-review]])?
