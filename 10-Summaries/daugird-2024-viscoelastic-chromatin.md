---
type: summary
title: "Daugird et al. 2024 — Correlative single-molecule lattice light-sheet imaging reveals nucleosome-chromatin dynamics"
source: "[[00-Sources/papers/Correlative single molecule lattice light sheet imaging reveals the dynamic relationship between nucleosomes and the local chromatin environment]]"
source_kind: paper
author: "Timothy A. Daugird, Yu Shi, Katie L. Holland, Hosein Rostamian, Zhe Liu, Luke D. Lavis, Joseph Rodriguez, Brian D. Strahl, Wesley R. Legant (corresponding)"
published: 2024-05-16
ingested: 2026-05-18
ingest_depth: full-intro+results
doi: "10.1038/s41467-024-48562-0"
journal: "Nature Communications"
tags: [imaging, single-molecule, lattice-light-sheet, nucleosome, viscoelastic, chromatin-mechanics, transcription, fractal-dimension, biophysics, Legant-lab]
entities: []
concepts:
  - "[[30-Concepts/chromatin-mechanical-properties]]"
  - "[[30-Concepts/chromatin-phase-separation]]"
topics:
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Daugird et al. (2024) — *Correlative single-molecule lattice light-sheet imaging reveals nucleosome-chromatin dynamics* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-024-48562-0)

# Daugird et al. 2024 — viscoelastic chromatin in live cells

> Thesis: live-cell **lattice light-sheet single-molecule imaging** of fluorescently tagged nucleosomes (HaloTag-H2B) simultaneously with the local chromatin environment shows that **nucleosomes diffuse and pack differently across chromatin densities, yet the viscoelastic properties and accessibility of the interchromatin space remain constant**. The differences in nucleosome behavior arise from **active processes** (transcription) that locally stabilize nucleosomes, not from passive crowding. This is the cleanest live-cell measurement of chromatin biophysics at the scale where LLPS theory operates.

## Verbatim key claims (from source body)

- **Method + central finding** (Abstract):
  > "We present an imaging platform to simultaneously visualize **single protein dynamics together with the local chromatin environment in live cells**. ... nucleosomes display **differential diffusion and packing arrangements as chromatin density increases** whereas the **viscoelastic properties and accessibility of the interchromatin space remain constant**."

- **Active vs passive separation** (Abstract):
  > "Our results support a model wherein **transcription locally stabilizes nucleosomes while simultaneously allowing for the free exchange of nuclear proteins**. ... nuclear heterogeneity arises from both active and passive processes."

- **Nucleosome motion ↔ chromatin density correlation** (Results):
  > "On average, **nucleosomes in denser CDCs display a slower apparent diffusion coefficient** ... showed significant differences in nucleosome motion across CDCs (two-sided Spearman coefficient = −0.344, p-value < 1E-5)."

- **Viscoelastic constancy of interchromatin space** (Results "The interchromatin space displays similar viscoelastic properties regardless of chromatin density"):
  > "We found **no apparent dependence in either the apparent diffusion coefficient or the anomalous alpha exponent on chromatin density classes** ... This indicates that, for a non-interacting free diffusing particle of ~2.6 nm size, **different chromatin density classes display similar viscoelastic properties**."
  > "We also found that the anomalous alpha exponent is about 0.8, which is close to what one would expect for **diffusion in purely viscous liquid** (anomalous alpha exponent of one)."

- **Fractal-like nucleosome organization** (Results):
  > "Consistent with previous reports, G(r) measurements of nucleosomes across the entire nucleus indicated linear scaling regimes, indicative of clustering along a continuum of spatial scales ... This power law like behavior is consistent with a **fractal-like organization of nucleosomes**, with the power law exponent corresponding to a fractal dimension."

- **Fractal dimension scales with density** (Results):
  > "The lowest density CDC 1 had a **fractal dimension of 2.14 ± 0.25** whereas the highest density CDC 7 had a fractal dimension of **2.85 ± 0.09**."

- **Nuclear periphery is biophysically distinct** (Results "The nuclear periphery represents a distinct biophysical environment"):
  > "The dependence between nucleosome motion and chromatin density is **almost entirely lost at the nuclear periphery** ... the nuclear periphery represents a unique environment that places distinct constraints on nucleosome motion ... nucleosomes in similarly compacted chromatin regions at the periphery vs. the nuclear interior display unique diffusive behaviors."

## Why this matters for the wiki

- **Direct measurement counterpart** to Gibson 2019's LLPS model: provides the in-vivo viscoelastic numbers (anomalous α ≈ 0.8, fractal dimension 2.14–2.85 across density classes) that the polymer-physics literature predicts.
- **Mechanical sub-axis anchor**: best verbatim source for "rigidity, condensation, elasticity, and fluid-like behavior" in the locus-state framework. Direct phrase match: "viscoelastic properties and accessibility of the interchromatin space remain constant".
- **Connects to spatial-positioning sub-axis**: nuclear periphery (LAD region, lamina contacts) has *distinct* biophysical environment — bridges to Rooijers 2019 scDam&T-seq findings on lamina-contact heterogeneity.
- **Connects to transcription axis**: active transcription = mechanical event (locally stabilizes nucleosomes). Reconciles "dense chromatin still permits TF dynamics" paradox.

## Methods / evidence (from text)

- **Cell system**: Cos7 cells stably expressing HaloTag-H2B at ~4.4% of endogenous H2B; HaloTag-Janelia Fluor 549 (chromatin context) + photoactivatable JF646 (single nucleosome tracking).
- **Imaging**: lattice light-sheet microscopy; lateral precision 24 ± 9 nm, axial 137 ± 59 nm; 2-color simultaneous 3D imaging.
- **Tracking criterion**: localizations linked into trajectories if <400 nm displacement between 20-ms frames; filters out free-diffusing H2B.
- **Chromatin density classes (CDCs)**: 7 classes via expectation-maximization on intensity histograms; validated by BIC + AIC.
- **Viscoelastic probe**: HaloTag-NLS (inert, ~2.6 nm) used to measure interchromatin space biophysics.
- **Biophysical model**: extended Rouse polymer model with fractal nucleosome organization and viscoelastic medium.

## Open questions

- The "viscoelastic constancy" claim is surprising — does it hold under perturbation (heat shock, transcriptional inhibition, drug-induced condensate dissolution)?
- Is there a **single-cell phenotype** that can be derived from viscoelastic measurements (analogous to scATAC-derived clusters)? If so, "biophysical state" becomes a distinct cell-state axis.
- The nuclear periphery's distinct biophysics (loss of density-motion coupling) needs mechanistic explanation — is it lamin-tethering or chromatin composition?

---
**Source:** [DOI](https://doi.org/10.1038/s41467-024-48562-0) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/38755200/) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11099156/)

## Related

- [[30-Concepts/chromatin-mechanical-properties]] · [[30-Concepts/chromatin-phase-separation]]
- [[10-Summaries/gibson-2019-chromatin-llps]] · [[10-Summaries/ahn-2021-llps-cancer-looping]] · [[10-Summaries/qi-zhang-2021-nucleoli-coalescence]] · [[10-Summaries/rooijers-2019-scdamt-seq]]
- [[40-Topics/chromatin-architecture]]
