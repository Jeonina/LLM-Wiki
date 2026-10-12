---
type: concept
title: Chromatin phase separation (LLPS)
aliases: [LLPS, liquid-liquid phase separation, chromatin condensate, nuclear condensate, biomolecular condensate]
tags: [biophysics, LLPS, condensate, IDR, histone-tail, BRD4, nucleolus, locus-state]
created: 2026-05-15
updated: 2026-10-12
---

# Chromatin phase separation (LLPS)

> Liquid–liquid phase separation (LLPS) is the demixing of a homogeneous solution into two coexisting liquid phases through multivalent weak interactions; in the nucleus it organizes chromatin into membraneless condensates and is tuned by histone modifications, the disordered regions of reader proteins and the surrounding chromatin mesh ([[10-Summaries/gibson-2019-chromatin-llps|Gibson 2019]]; [[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]).

> [!abstract] 한눈에
> LLPS는 약한 다가 상호작용으로 용액이 두 액체 상으로 나뉘는 현상이고, 핵 안에서는 histone tail, H1, acetylation, BRD4 같은 reader가 염색질 condensate의 형성과 해체를 조절한다 ([[10-Summaries/gibson-2019-chromatin-llps|Gibson 2019]]). NUP98-HOXA9 같은 IDR 융합 단백질은 LLPS로 CTCF와 무관한 loop를 만들어 암을 일으키지만, LLPS를 single-cell 수준에서 직접 읽는 방법은 아직 거의 없다 ([[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]).

## Definition

LLPS is the demixing of a homogeneous solution into two coexisting liquid phases, driven by multivalent weak interactions (synthesis). In the nucleus it organizes chromatin into membraneless condensates — transcriptional hubs, heterochromatin foci, nucleoli and speckles — and is sensitive to histone modifications, the intrinsically disordered regions (IDRs) of reader proteins, and the surrounding chromatin polymer mesh ([[10-Summaries/gibson-2019-chromatin-llps|Gibson 2019]]; [[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]; [[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]).

LLPS sits on the biophysical / mechanical sub-axis of DNA locus state, a regulatory layer parallel to genetic sequence and chromatin marks (synthesis). That structural-physical axis has three sub-axes (synthesis):

1. **3D contact** (Hi-C, scHi-C, Dip-C) — pairwise distances in the polymer.
2. **Spatial positioning** (DamID, scDam&T-seq) — peripheral versus interior position, lamina contacts.
3. **Mechanical / phase-separation state** — chromatin viscoelasticity, condensate residency, LLPS competence; this concept. See [[30-Concepts/chromatin-mechanical-properties]].

## Why it matters

- **Subnuclear organization.** Nucleoli, splicing speckles, Cajal bodies and paraspeckles are LLPS condensates whose composition and stability depend on chromatin context (synthesis).
- **3D-genome consequence.** LLPS can induce CTCF-independent chromatin loops, a class of loops distinct from the cohesin/CTCF mechanism ([[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]); see [[topologically-associating-domain]] and [[40-Topics/3d-genome]].
- **Cancer mechanism.** Oncogenic IDR fusions hijack LLPS to gain super-enhancer-like binding and rewire 3D architecture, shown for NUP98-HOXA9 ([[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]); EWS-FLI1 is a candidate (synthesis).
- **Mechanical coupling.** Chromatin viscoelasticity confines and stabilizes condensates, which explains the multi-droplet steady state of nuclear bodies ([[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]).

## How chromatin phase-separates

| Driver | Effect on condensates | Source |
|---|---|---|
| Histone tails (especially unmodified) | Drive nucleosomal-array LLPS at physiologic salt | ([[10-Summaries/gibson-2019-chromatin-llps\|Gibson 2019]]) |
| Linker histone H1 | Promotes phase separation | ([[10-Summaries/gibson-2019-chromatin-llps\|Gibson 2019]]) |
| Inter-nucleosome linker length | Tunes droplet density | ([[10-Summaries/gibson-2019-chromatin-llps\|Gibson 2019]]) |
| Acetylation by p300 | Dissolves chromatin droplets; links LLPS to [[40-Topics/histone-modifications]] | ([[10-Summaries/gibson-2019-chromatin-llps\|Gibson 2019]]) |
| Bromodomain readers (BRD4) of acetylated chromatin | Form a new phase, immiscible with unmodified chromatin droplets, which mimics nuclear chromatin subdomains | ([[10-Summaries/gibson-2019-chromatin-llps\|Gibson 2019]]) |
| IDR-containing transcription factors (NUP98 fusions, FUS; also EWS and hypoxia-responsive ZHX2) | Phase-separate with chromatin to alter transcription and 3D structure | ([[10-Summaries/ahn-2021-llps-cancer-looping\|Ahn 2021]]); EWS and ZHX2 (synthesis) |

## Single-cell measurement (frontier)

The mechanical / phase-separation sub-axis is the youngest measurement frontier, and single-cell readouts are still scarce (synthesis).

- **In live cells**, lattice light-sheet single-molecule imaging measures viscoelasticity and nucleosome diffusion ([[10-Summaries/daugird-2024-viscoelastic-chromatin|Daugird 2024]]).
- **In silico from Hi-C**, polymer models with LLPS-competent particles extract biophysical predictions ([[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]; [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).
- **Per-fibre chromatin actuation**: in DAF-seq two cells differ in ~63% of regulatory-element actuation states ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]), which is consistent with stochastic LLPS-driven actuation events (synthesis).

## Evidence and examples

- The FG-repeat IDR of NUP98 is necessary and sufficient for phase-separated nuclear puncta, leukaemic transformation and broad super-enhancer-like binding by NUP98-HOXA9 ([[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]).
- Swapping the FG-IDR for the LLPS-forming IDR of FUS reproduced puncta, transformation and enhanced genome-wide binding ([[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]).
- Of the loops specific to wild-type NUP98-IDR/HOXA9, 91% of anchors overlapped chimera binding but only 31% overlapped a CTCF site ([[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]).
- Hyperacetylated chromatin bound by BRD4 forms a phase immiscible with unmodified chromatin droplets ([[10-Summaries/gibson-2019-chromatin-llps|Gibson 2019]]).

## Open questions

- **Loop formation was tested only for the NUP98 IDR.** The FUS-swap chimera was not tested for loops ([[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]), so the claim that LLPS competence alone drives CTCF-independent looping rests on one IDR (synthesis).
- **DAF-seq does not test LLPS.** The link between DAF-seq's ~63% inter-cell actuation divergence and LLPS is this page's interpretation; the source reports the divergence without proposing a mechanism ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]) (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromatin-mechanical-properties|Chromatin mechanical properties]] — Rigidity, viscoelasticity and condensation as a locus-state sub-axis.
> - `concept` [[30-Concepts/topologically-associating-domain|Topologically associating domain]] — Contact domains shaped by cohesin/CTCF and, sometimes, condensates.
> - `hub` [[40-Topics/histone-modifications|Histone modifications]] — Marks such as acetylation that tune chromatin condensates.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromatin folding, contacts and nuclear positioning.

## All sources on this page

> [!info]- 6 summaries cited here
> - [[10-Summaries/ahn-2021-llps-cancer-looping|Ahn 2021]]
> - [[10-Summaries/daugird-2024-viscoelastic-chromatin|Daugird 2024]]
> - [[10-Summaries/gibson-2019-chromatin-llps|Gibson 2019]]
> - [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]
> - [[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
