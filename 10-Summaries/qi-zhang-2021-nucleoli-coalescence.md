---
type: summary
title: "Qi & Zhang 2021 — Chromatin network retards nucleoli coalescence"
source: "[[00-Sources/papers/Chromatin network retards nucleoli coalescence]]"
source_kind: paper
author: "Yifeng Qi, Bin Zhang (corresponding)"
published: 2021-11-24
ingested: 2026-05-18
ingest_depth: full-intro+results
doi: "10.1038/s41467-021-27123-9"
journal: "Nature Communications"
tags: [LLPS, nucleolus, nuclear-body, polymer-physics, Hi-C, simulation, NAD, entropic-barrier, multi-droplet, viscoelastic, Zhang-lab]
entities:
  - "[[20-Entities/bin-zhang]]"
concepts:
  - "[[30-Concepts/chromatin-phase-separation]]"
  - "[[30-Concepts/chromatin-mechanical-properties]]"
topics:
  - "[[40-Topics/chromatin-architecture]]"
  - "[[40-Topics/3d-genome]]"
---

**Citation:** Qi & Zhang (2021) — *Chromatin network retards nucleoli coalescence* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-021-27123-9)

# Qi & Zhang 2021 — chromatin network arrests nucleolus coalescence

> Thesis: classical LLPS theory predicts that nuclear bodies should coalesce into a single droplet (minimizing surface energy), yet nucleoli persist as **2–5 coexisting droplets** in somatic cells — defying classical predictions. Using a **diploid human genome polymer model parameterized with Hi-C data**, Qi & Zhang show that the **viscoelastic chromatin network creates an entropic barrier (~7 k_B T)** that arrests nucleolus coalescence. The chromatin-NAD attractive interactions facilitate droplet *nucleation* but the chromatin network's polymer topology *hinders* coalescence — a nucleation-and-arrest mechanism that generalizes to other nuclear bodies (paraspeckles, speckles).

## Verbatim key claims (from source body)

- **Problem statement** (Abstract):
  > "Nuclear bodies are membraneless condensates that may form via liquid-liquid phase separation. The **viscoelastic chromatin network could impact their stability and may hold the key for understanding experimental observations that defy predictions of classical theories**."

- **Method + key finding** (Abstract):
  > "Using a **diploid human genome model parameterized with chromosome conformation capture (Hi-C) data**, we study the thermodynamics and kinetics of nucleoli formation. Dynamical simulations predict the **formation of multiple droplets** for nucleolar particles that experience specific interactions with nucleolus-associated domains (NADs)."

- **Two-droplet metastability** (Abstract):
  > "Free energy calculations further support that a **two-droplet state, often observed for nucleoli in somatic cells, is metastable and separated from the single-droplet state with an entropic barrier**."

- **Mechanism** (Abstract):
  > "Our study suggests that nucleoli-chromatin interactions **facilitate droplets' nucleation but hinder their coarsening** due to the coupled motion between droplets and the chromatin network: as droplets coalesce, the **chromatin network becomes increasingly constrained**. Therefore, the chromatin network supports a **nucleation and arrest mechanism** to stabilize the multi-droplet state."

- **Quantitative entropic barrier** (Results):
  > "The two basins are separated from each other with a transition state at R_g ≈ 1.13 μm ... the merging of the droplets is kinetically constrained due to the presence of **a barrier that is ~7 k_B T in height**."

- **Coalescence dynamics** (Results):
  > "By plotting the normalized neck radius (2R(t)/R_0) with respect to the time, we obtained a power-law relationship with **exponent 0.51**. ... This exponent **agrees with the experimental value determined for nucleoli** and suggests that droplet coalescence proceeds in the low Reynolds number regime dominated by viscous effects from the outer fluid."

- **Slow coarsening due to sub-diffusion** (Results):
  > "Most of the clusters exhibit **sub-diffusion** and x²(t) ∝ Dt^(1/2). ... the **chromatin network could further reduce the exponent and slow down the Brownian diffusion dominated coarsening dynamics by hindering droplet coalescence through entropic barriers**."

- **Cross-validation with experiment** (Results):
  > "The abnormal diffusion and slower coarsening kinetics have been directly observed by Lee et al. as well when monitoring the coarsening dynamics of model condensates based on intrinsically disordered protein regions in the nucleus. In particular, they revealed a coarsening exponent of ~0.12, which is **close to the value shown in Fig. 5c**. The scaling exponent for nucleolar coarsening in vivo is also in **good agreement with the simulated value when considering short time kinetics before 5 min**."

- **Generalizable mechanism** (Abstract conclusion):
  > "The chromatin network supports a nucleation and arrest mechanism to stabilize the multi-droplet state for nucleoli **and possibly for other nuclear bodies**."

## Why this matters for the wiki

- **Closes the LLPS-architecture loop**: Gibson 2019 (chromatin can phase-separate) → this work (chromatin network *controls* phase separation kinetics). Together they form the biophysical foundation for nuclear body organization.
- **Quantitative anchor for "viscoelastic chromatin"** — provides the entropic-barrier number (~7 k_B T) and the coarsening exponent (~0.1) that connect chromatin mechanics to observable nuclear body dynamics.
- **Hi-C → polymer model → biophysics pipeline** parallels [[10-Summaries/mali-2025-conformational-heterogeneity]] (Tolokh model with lamina-DamID constraints). Both use polymer simulations to extract biophysical predictions from contact maps.
- **Generalizes to other nuclear bodies**: speckles, paraspeckles, Cajal bodies likely follow same nucleation-arrest mechanism with different NAD-equivalent chromatin attachment sites.

## Methods / evidence (from text)

- **Genome model**: diploid human genome (46 chromosomes) at 1-Mb resolution, three bead types (A/B compartments + C centromeric); interactions optimized to match GM12878 Hi-C contact probabilities via maximum entropy.
- **Nucleolar particles**: coarse-grained, with favorable interactions to other nucleolar particles AND to NADs (nucleolus-associated domains).
- **Simulations**: molecular dynamics, 20 million steps per run, 12 independent replicates per condition; longer than chromosome relaxation timescale.
- **Free-energy method**: umbrella sampling + temperature replica exchange along R_g reaction coordinate.
- **Coalescence kinetics**: tracked neck radius R(t) during droplet fusion events; power-law fits compared to experiment.
- **Coarsening pathway analysis**: Brownian-motion-induced coalescence (BMC) ≈ 76% of switching events; rest via diffusion-limited Ostwald ripening.

## Open questions

- **Single-cell test**: in scHi-C data, do cells with detected nucleolus-coalescence events show distinct local chromatin compaction? The C.H. metric ([[10-Summaries/mali-2025-conformational-heterogeneity]]) could quantify this.
- **Other nuclear bodies**: quantitative prediction of speckle vs paraspeckle vs Cajal body number from their specific chromatin attachments?
- **Perturbation test**: chromatin softening (HDAC inhibition, lamin knockdown) should *reduce* the entropic barrier and *increase* fusion. Direct experimental test missing.

---
**Source:** [DOI](https://doi.org/10.1038/s41467-021-27123-9) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34819511/) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8613291/)

## Related

- [[30-Concepts/chromatin-phase-separation]] · [[30-Concepts/chromatin-mechanical-properties]] · [[30-Concepts/conformational-heterogeneity]]
- [[10-Summaries/gibson-2019-chromatin-llps]] · [[10-Summaries/daugird-2024-viscoelastic-chromatin]] · [[10-Summaries/mali-2025-conformational-heterogeneity]] · [[10-Summaries/ahn-2021-llps-cancer-looping]]
- [[40-Topics/chromatin-architecture]] · [[40-Topics/3d-genome]]
