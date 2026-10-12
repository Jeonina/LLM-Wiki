---
type: concept
title: Chromatin mechanical properties
aliases: [chromatin viscoelasticity, chromatin mechanics, chromatin rigidity, chromatin elasticity, chromatin fluidity]
tags: [biophysics, viscoelastic, mechanics, locus-state, polymer]
created: 2026-05-15
updated: 2026-10-12
---

# Chromatin mechanical properties

> The mechanical, viscoelastic and biophysical state of chromatin — rigidity, elasticity, fluid-like versus gel-like behaviour, condensation, and the mesh through which nuclear proteins diffuse — treated as the mechanical sub-axis of DNA locus state ([[10-Summaries/daugird-2024-viscoelastic-chromatin|Daugird 2024]]; [[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]).

> [!abstract] 한눈에
> 염색질의 강성, 탄성, 유체성, 응축 정도 같은 역학 상태는 서열이나 histone mark와 별개로 locus를 조절하는 변수다. 살아 있는 세포에서는 전사가 nucleosome을 국소적으로 안정화하고 lamin이 없어지면 3D 구조의 세포 간 변동이 커지지만, 이 축을 single-cell 수준에서 측정한 데이터는 아직 드물다 ([[10-Summaries/daugird-2024-viscoelastic-chromatin|Daugird 2024]]; [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).

## Definition

Chromatin mechanics covers how stiff, elastic or fluid chromatin is, how condensed it is, and the mesh through which nuclear proteins diffuse (synthesis). A locus's mechanical context — stiff heterochromatin floor, soft euchromatin droplet, or a condensate confined to a nuclear body — is a regulatory variable distinct from sequence and chromatin marks (synthesis).

The page places this within a three-part structural-physical locus state (synthesis):

1. **3D contact state** — Hi-C-based interaction maps.
2. **Spatial positioning state** — lamina, NAD or speckle contact via DamID and related methods.
3. **Mechanical / viscoelastic state** — the subject of this page.

## Why it matters

- The same DNA sequence with the same histone marks can behave differently if the surrounding chromatin is more or less viscoelastic; transcription-factor residence times, condensate stability and loop-formation kinetics all depend on local mechanics (synthesis).
- Transcription is a mechanical event, not only a chemical one: active transcription locally stabilizes nucleosomes while free-protein mobility is preserved ([[10-Summaries/daugird-2024-viscoelastic-chromatin|Daugird 2024]]).
- Losing the lamin anchor raises cell-to-cell structural variability, which is predicted to make transcription noisier ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]).

## Measurement methods

| Method | What it measures | Single-cell? | Source |
|---|---|---|---|
| Lattice light-sheet single-molecule imaging | Nucleosome diffusion, viscoelastic properties of the interchromatin space | Live single cells | ([[10-Summaries/daugird-2024-viscoelastic-chromatin\|Daugird 2024]]) |
| Optical / magnetic tweezers | Chromatin-fibre elastic modulus, force–extension | Bulk fibres | (synthesis) |
| Polymer modelling from Hi-C | Predicted viscoelastic regimes from contact data | Per cell with scHi-C | ([[10-Summaries/qi-zhang-2021-nucleoli-coalescence\|Qi & Zhang 2021]]) |
| Microrheology (tracer particles) | Mesh size, viscosity gradients | Single cells, indirect | (synthesis) |
| FRAP / single-molecule tracking | Protein residence times in chromatin domains | Live cells | (synthesis) |

## Properties under this umbrella

- **Viscoelasticity** — combined viscous (energy-dissipating) and elastic (energy-storing) behaviour; chromatin is viscoelastic across multiple timescales (synthesis).
- **Rigidity** — heterochromatin tends to be stiffer than euchromatin, and lamin-tethered chromatin is the rigid backbone (synthesis); see [[nuclear-lamina]].
- **Condensation** — local density is modulated by linker histone H1, nucleosome spacing and acetylation status ([[10-Summaries/gibson-2019-chromatin-llps|Gibson 2019]]).
- **Fluid-like behaviour / phase separation** — see [[30-Concepts/chromatin-phase-separation]].
- **Entropic confinement** — the chromatin mesh constrains condensate coalescence ([[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]).

## Evidence and examples

- Lamin depletion increases chromatin conformational heterogeneity at nearly all genomic separations ([[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]); see [[conformational-heterogeneity]].
- Active transcription locally stabilizes nucleosomes while preserving free-protein mobility ([[10-Summaries/daugird-2024-viscoelastic-chromatin|Daugird 2024]]).
- In a Hi-C-parameterized polymer model, the viscoelastic chromatin network creates an entropic barrier (~7 k_B T) that arrests nucleolus coalescence ([[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]).

## Open questions

- **Coverage is uneven across the three sub-axes.** Single-cell coverage is strongest for 3D contact state, growing for spatial positioning, and sparse for mechanical state (synthesis); see [[topologically-associating-domain]] and [[40-Topics/3d-genome]].
- **Is local viscoelasticity actually variable?** Daugird 2024 found that the viscoelastic properties and accessibility of the interchromatin space stay constant across chromatin densities ([[10-Summaries/daugird-2024-viscoelastic-chromatin|Daugird 2024]]), which sits uneasily with the premise that loci differ because their surrounding chromatin is more or less viscoelastic (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromatin-phase-separation|Chromatin phase separation]] — Liquid-like condensation of chromatin and its readers.
> - `concept` [[30-Concepts/nuclear-lamina|Nuclear lamina]] — The rigid peripheral anchor for heterochromatin.
> - `concept` [[30-Concepts/conformational-heterogeneity|Conformational heterogeneity]] — A metric for cell-to-cell 3D-genome variability.
> - `concept` [[30-Concepts/topologically-associating-domain|Topologically associating domain]] — Contact domains in the 3D contact sub-axis.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromatin folding, contacts and nuclear positioning.

## All sources on this page

> [!info]- 4 summaries cited here
> - [[10-Summaries/daugird-2024-viscoelastic-chromatin|Daugird 2024]]
> - [[10-Summaries/gibson-2019-chromatin-llps|Gibson 2019]]
> - [[10-Summaries/mali-2025-conformational-heterogeneity|Mali 2025]]
> - [[10-Summaries/qi-zhang-2021-nucleoli-coalescence|Qi & Zhang 2021]]
