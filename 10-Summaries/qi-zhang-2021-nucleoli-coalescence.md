---
type: summary
title: "Qi & Zhang 2021 — Chromatin network retards nucleoli coalescence (polymer-LLPS coupling)"
source: "PubMed abstract / no local PDF (2026-05-15 ingest)"
source_kind: paper
author: "Yifeng Qi, Bin Zhang (corresponding)"
published: 2021-11-24
ingested: 2026-05-15
ingest_depth: abstract-only
doi: "10.1038/s41467-021-27123-9"
journal: "Nature Communications"
tags: [LLPS, nucleolus, nuclear-body, polymer-physics, Hi-C, simulation, NAD, biophysics, multi-droplet]
entities:
  - "[[20-Entities/bin-zhang]]"
concepts:
  - "[[30-Concepts/chromatin-phase-separation]]"
  - "[[30-Concepts/chromatin-mechanical-properties]]"
topics:
  - "[[40-Topics/chromatin-architecture]]"
  - "[[40-Topics/3d-genome]]"
---

# Qi & Zhang 2021 — Chromatin network retards nucleoli coalescence

> Thesis: nuclear bodies (nucleoli, speckles, Cajal bodies) are membraneless condensates often described as LLPS droplets, but classical phase-separation theory predicts they should coalesce into a single droplet — which doesn't match the observed **multi-droplet steady state** of nucleoli in somatic cells. The authors build a diploid-human-genome polymer model parameterized with Hi-C data, simulate nucleolar particles that interact specifically with **nucleolus-associated domains (NADs)**, and show that the **viscoelastic chromatin network arrests droplet coalescence**: as droplets fuse, the surrounding chromatin tightens, raising the entropic barrier and stabilizing the metastable multi-droplet state.

## Key claims (from abstract)

- **Polymer model** of diploid human genome parameterized with Hi-C contact data; nucleolar particles interact with NAD-tagged loci.
- Simulated coarsening dynamics, surface tension, and coalescence kinetics **quantitatively match experimental nucleolus measurements**.
- **Multi-droplet state is metastable**, not kinetically trapped at the level of individual droplets — separated from the single-droplet ground state by an **entropic barrier** from chromatin reorganization.
- **Mechanism**: as droplets coalesce, surrounding chromatin must rearrange; the viscoelastic mesh stretches under this rearrangement, creating a confining penalty that arrests coalescence.
- **Generalizable**: same nucleation + arrest mechanism may stabilize other nuclear bodies (speckles, Cajal bodies, paraspeckles) whose components interact with specific genomic domains.

## Why this matters for the wiki

- **Closes the loop between Gibson 2019 (chromatin can phase-separate) and the observed nuclear-body architecture (multiple stable droplets).** The piece that completes the LLPS picture for nuclear organization.
- **Mechanistic role for chromatin viscoelasticity** — same property measured live by Daugird 2024. The polymer-network *is* the stabilizing scaffold, not just a backdrop.
- **Hi-C → polymer model → biophysics pipeline** parallels [[10-Summaries/mali-2025-conformational-heterogeneity]] (Tolokh model with lamina-DamID constraints). Both papers use polymer simulations to extract biophysical predictions from contact maps.

## Connections to other sources

- **Biophysical companion** to [[10-Summaries/gibson-2019-chromatin-llps]] — Gibson shows chromatin LLPS exists; Qi & Zhang show the chromatin network constrains LLPS dynamics.
- **Mechanism for** [[10-Summaries/daugird-2024-viscoelastic-chromatin]] observations — viscoelastic constancy may be why nuclear-body architecture is stable over time scales.
- **Modeling parallel**: [[10-Summaries/mali-2025-conformational-heterogeneity]] — same Hi-C → polymer simulation → biophysics workflow, applied to single-cell heterogeneity rather than condensate stability.
- **Cancer analogue**: [[10-Summaries/ahn-2021-llps-cancer-looping]] — when oncogenic IDR fusions hijack LLPS, they may also subvert chromatin-network confinement.

## Open questions (raised by this source)

- **Single-cell test**: in scHi-C data, do cells with detected nucleolus-coalescence events show distinct local chromatin compaction? The C.H. metric ([[10-Summaries/mali-2025-conformational-heterogeneity]]) could quantify this.
- **Other nuclear bodies**: does the same arrest mechanism quantitatively explain speckle multiplicity? Different specific-binding domains (SRSF1 vs nucleolin) may give different entropic barriers.
- **Perturbation**: chromatin softening (HDAC inhibition, lamin knockdown) should *reduce* the entropic barrier and *increase* nuclear-body fusion. Testable.

## Note on ingest depth

Abstract-based. Full PDF re-ingest needed for the simulation parameters (LJ potential depths, time scales, comparison to experimental coarsening rates).

---
**Source:** [DOI](https://doi.org/10.1038/s41467-021-27123-9) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34819511/) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8613291/)

## Related

- [[30-Concepts/chromatin-phase-separation]] · [[30-Concepts/chromatin-mechanical-properties]]
- [[10-Summaries/gibson-2019-chromatin-llps]] · [[10-Summaries/daugird-2024-viscoelastic-chromatin]] · [[10-Summaries/mali-2025-conformational-heterogeneity]] · [[10-Summaries/ahn-2021-llps-cancer-looping]]
- [[40-Topics/chromatin-architecture]] · [[40-Topics/3d-genome]]
