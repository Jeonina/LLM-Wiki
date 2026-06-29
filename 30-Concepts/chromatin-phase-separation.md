---
type: concept
title: Chromatin phase separation (LLPS)
aliases: [LLPS, liquid-liquid phase separation, chromatin condensate, nuclear condensate, biomolecular condensate]
tags: [biophysics, LLPS, condensate, IDR, histone-tail, BRD4, nucleolus, locus-state]
created: 2026-05-15
updated: 2026-05-15
---

# Chromatin phase separation (LLPS)

> **Liquid–liquid phase separation (LLPS)** is the demixing of a homogeneous solution into two coexisting liquid phases, driven by multivalent weak interactions. In the nucleus, LLPS organizes chromatin into membraneless condensates (transcriptional hubs, heterochromatin foci, nucleoli, speckles) and is sensitive to histone modifications, intrinsically disordered regions (IDRs) of reader proteins, and the surrounding chromatin polymer mesh. LLPS sits on the **biophysical / mechanical sub-axis of DNA locus state** — a regulatory layer parallel to genetic sequence and chromatin marks.

## How chromatin phase-separates

- **Histone tails** (especially when unmodified) drive nucleosomal-array LLPS at physiologic salt (Gibson 2019).
- **Linker histone H1** promotes phase separation; **inter-nucleosome linker length** tunes droplet density.
- **Acetylation (p300)** dissolves chromatin droplets.
- **Bromodomain readers (BRD4)** of acetylated chromatin form a *new* phase, immiscible with unmodified chromatin droplets → mimics nuclear chromatin subdomains.
- **IDR-containing transcription factors** (NUP98 fusions, FUS, EWS, hypoxia-responsive ZHX2) phase-separate with chromatin to alter transcription and 3D structure.

## Why it matters

- **Subnuclear organization**: nucleoli, splicing speckles, Cajal bodies, paraspeckles are LLPS condensates whose composition and stability depend on chromatin context.
- **3D-genome consequence**: LLPS can induce **CTCF-independent chromatin loops** ([[10-Summaries/ahn-2021-llps-cancer-looping]]) — a new class of loops distinct from the cohesin/CTCF mechanism.
- **Cancer mechanism**: oncogenic IDR fusions hijack LLPS to gain super-enhancer-like binding and rewire 3D architecture (NUP98-HOXA9, EWS-FLI1 candidates).
- **Mechanical coupling**: chromatin viscoelasticity confines and stabilizes condensates ([[10-Summaries/qi-zhang-2021-nucleoli-coalescence]]) — explains the multi-droplet steady state of nuclear bodies.

## Locus-state framing

The structural-physical axis of DNA locus state has three sub-axes:

1. **3D contact** (Hi-C, scHi-C, Dip-C) — pairwise distances in the polymer
2. **Spatial positioning** (DamID, scDam&T-seq) — peripheral vs interior, lamina contacts
3. **Mechanical / phase-separation state** — chromatin viscoelasticity, condensate residency, LLPS competence ← **this concept**

Sub-axis 3 is the youngest measurement frontier; single-cell readouts are still scarce.

## Single-cell LLPS measurement (frontier)

- **In live cells**: lattice light-sheet single-molecule imaging ([[10-Summaries/daugird-2024-viscoelastic-chromatin]]) measures viscoelasticity and nucleosome diffusion.
- **In silico from Hi-C**: polymer models with LLPS-competent particles ([[10-Summaries/qi-zhang-2021-nucleoli-coalescence]], [[10-Summaries/mali-2025-conformational-heterogeneity]]) extract biophysical predictions.
- **Per-fiber chromatin actuation** ([[10-Summaries/swanson-2025-daf-seq]]) — DAF-seq's 63% inter-cell actuation divergence is consistent with stochastic LLPS-driven actuation events.

## Related

- [[30-Concepts/chromatin-mechanical-properties]] · [[40-Topics/histone-modifications]] · [[30-Concepts/topologically-associating-domain]] · [[40-Topics/3d-genome]]
- Sources: [[10-Summaries/gibson-2019-chromatin-llps]] · [[10-Summaries/ahn-2021-llps-cancer-looping]] · [[10-Summaries/daugird-2024-viscoelastic-chromatin]] · [[10-Summaries/qi-zhang-2021-nucleoli-coalescence]]
