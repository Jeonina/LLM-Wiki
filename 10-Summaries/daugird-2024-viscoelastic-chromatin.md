---
type: summary
title: "Daugird et al. 2024 — Single-molecule lattice light-sheet imaging reveals viscoelastic chromatin environment"
source: "PubMed abstract / no local PDF (2026-05-15 ingest)"
source_kind: paper
author: "Timothy A. Daugird, Yu Shi, Katie L. Holland, Hosein Rostamian, Zhe Liu, Luke D. Lavis, Joseph Rodriguez, Brian D. Strahl, Wesley R. Legant (corresponding)"
published: 2024-05-16
ingested: 2026-05-15
ingest_depth: abstract-only
doi: "10.1038/s41467-024-48562-0"
journal: "Nature Communications"
tags: [imaging, single-molecule, lattice-light-sheet, nucleosome, viscoelastic, chromatin-mechanics, transcription, biophysics]
entities: []
concepts:
  - "[[30-Concepts/chromatin-mechanical-properties]]"
  - "[[30-Concepts/chromatin-phase-separation]]"
topics:
  - "[[40-Topics/chromatin-architecture]]"
---

# Daugird et al. 2024 — Viscoelastic chromatin environment via single-molecule LLSM

> Thesis: in live cells, biological processes happen with proteins diffusing through and binding to a nucleic-acid meshwork. Using **lattice light-sheet single-molecule imaging** correlated with super-resolution mapping of the local chromatin environment, the authors quantify how nucleosome diffusion and packing change with chromatin density — and find that **viscoelastic properties and interchromatin-space accessibility remain constant** across density regimes. Active processes (transcription) locally stabilize nucleosomes while preserving protein mobility. This is the cleanest live-cell measurement of chromatin biophysics at the level the LLPS literature predicts.

## Key claims (from abstract)

- **Correlative imaging**: simultaneous tracking of single proteins + super-resolution mapping of chromatin density, in live cells, via lattice light-sheet microscopy.
- **Density-dependent nucleosome dynamics**: nucleosomes show different diffusion and packing as chromatin density increases.
- **Constant viscoelasticity**: despite density changes, the **viscoelastic properties of the interchromatin space and its accessibility to free proteins remain constant** — the mesh tightens but the dissolved-phase mobility is preserved.
- **Active transcription locally stabilizes nucleosomes** while freely allowing nuclear-protein exchange. Reconciles the apparent paradox of "dense chromatin still permits TF dynamics."
- **Nuclear heterogeneity arises from both active and passive processes**; modeling different chromatin environments requires accounting for spatial location within the nucleus + active modification state.

## Why this matters for the wiki

- Provides the **measurement** counterpart to Gibson 2019's biophysical *model* — LLSM measures chromatin viscoelasticity in live cells where the LLPS prediction lives.
- Directly relevant to the **mechanical/viscoelastic sub-axis** of the structural-physical state in DNA locus state framework (the 3c gap).
- Frames transcription as a **mechanical** event, not just a chemical one — active genes locally rigidify nucleosome dynamics, opening a measurement modality orthogonal to ATAC-seq and DamID.

## Connections to other sources

- **Biophysical companion to** [[10-Summaries/gibson-2019-chromatin-llps]] (in-vitro LLPS prediction) and [[10-Summaries/ahn-2021-llps-cancer-looping]] (LLPS pathology). Daugird 2024 measures what those models predict.
- **Co-authored by Wesley Legant** — same group as Ahn 2021; recurring LLSM + chromatin biophysics line.
- **Adjacent**: [[10-Summaries/elliott-2025-naturebiotechnology]] DAF-seq describes per-fiber actuation heterogeneity at the molecular level; Daugird 2024 describes per-locus biophysics at the cellular level.

## Open questions (raised by this source)

- The "viscoelastic constancy" claim is surprising — does it hold under perturbation (heat shock, transcriptional inhibition, drug-induced condensate dissolution)?
- Is there a **single-cell phenotype** that can be derived from viscoelastic measurements (analogous to how scATAC-seq derives accessibility-based cell-type clusters)? If so, "biophysical state" becomes a distinct cell-state axis.
- How does transcription locally stabilize nucleosomes mechanistically — is it the elongating Pol II, the nascent RNA, or chromatin remodeler binding that matters?

## Note on ingest depth

Abstract-based summary. Full PDF re-ingest will quantify diffusion coefficients, viscosity scales, and the perturbation experiments referenced abstractly.

---
**Source:** [DOI](https://doi.org/10.1038/s41467-024-48562-0) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/38755200/) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11099156/)

## Related

- [[30-Concepts/chromatin-mechanical-properties]] · [[30-Concepts/chromatin-phase-separation]]
- [[10-Summaries/gibson-2019-chromatin-llps]] · [[10-Summaries/ahn-2021-llps-cancer-looping]] · [[10-Summaries/qi-zhang-2021-nucleoli-coalescence]]
- [[40-Topics/chromatin-architecture]]
