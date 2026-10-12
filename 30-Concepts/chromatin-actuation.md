---
type: concept
title: Chromatin actuation
aliases: [actuation, fiber actuation]
tags: [chromatin, single-molecule]
created: 2026-05-07
updated: 2026-10-12
---

# Chromatin actuation

> The state of a regulatory element being **simultaneously open and bound** along a specific chromatin fiber, as measured at single-molecule resolution by deaminase or methyltransferase footprinting — a per-fiber refinement of [[chromatin-accessibility]] ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

> [!abstract] 한눈에
> chromatin actuation은 한 가닥의 chromatin fiber 위에서 조절 요소가 nucleosome 없이 열려 있으면서 TF가 결합한 상태를 뜻하며, 여러 fiber를 합산한 accessibility를 fiber 단위로 쪼갠 개념이다. scDAF-seq로 측정하면 두 세포 사이 차이(~63%)와 한 세포 안 두 haplotype 사이 차이(~61%)가 거의 같다 ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [염색질 구조 교재](../60-Explainers/chromatin-architecture.html)
<!-- /explainer-links -->

## Definition

In bulk and single-cell ATAC-seq, "accessible" is a count over many fibers. In single-molecule footprinting ([[daf-seq]], [[fiber-seq]]; see [[single-molecule-footprinting]]), each individual fiber either *is* or *is not* in a state where (a) the element is nucleosome-free and (b) the predicted TFs are bound. The latter state is **actuation** ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]] terminology).

scDAF-seq measures actuation per fiber, per haplotype, per cell — yielding the unit of analysis "is regulatory element X actuated on haplotype Y of cell Z?" ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

## Why it matters

Two findings from [[10-Summaries/swanson-2025-daf-seq|DAF-seq]] are only visible because actuation is measurable per fiber (see Evidence): pervasive plasticity between cells and haplotypes, and co-actuation of elements in ~100 kb domains.

## Levels of measurement

| Level | What it is | Source |
|---|---|---|
| Per-fiber actuation | Each long-read sequenced fiber gives a binary actuation call per element | ([[10-Summaries/swanson-2025-daf-seq\|DAF-seq]]) |
| Aggregated chromatin actuation | Averaged over fibers; recovers ATAC-like peak calls | ([[10-Summaries/swanson-2025-daf-seq\|DAF-seq]]) |
| Co-actuation | Joint actuation status of two elements on the same fiber | ([[10-Summaries/swanson-2025-daf-seq\|DAF-seq]]) |

## Evidence and examples

**Plasticity and co-actuation**

- **Pervasive plasticity.** ~63% of regulatory elements differ in actuation status between two random cells, and ~61% differ between haplotypes within the same cell ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]). The intra-cellular and inter-cellular numbers being comparable is a strong claim about how much of regulatory variability is stochastic per fiber rather than programmed per cell state or trans-environment ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).
- **Co-actuation in ~100 kb domains.** Pairs of regulatory elements on the same fiber are preferentially actuated together, with the distance dependence mirroring cohesin loops ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).
- Bulk Fiber-seq had already shown same-fiber co-actuation but was limited to 10–100 kb reads and confounded by trans-factor differences between cells; scDAF-seq controls for this with within-cell pseudo-codependency scores ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

**Haplotype-specific actuation**

- SLC39A4 promoter actuation in liver tissue is preferentially driven by the rs2280838-T haplotype via altered nucleosome positioning ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).
- COLO829T melanoma CC>TT mutation eliminates actuation only on the variant haplotype ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

## Contested points

- The framing assumes binary "actuated / not actuated" calls; the reality is graded (partial occupancy, transient binding). The thermodynamic ΔG analysis in [[10-Summaries/swanson-2025-daf-seq|DAF-seq]] handles this for TF cooperativity but not for the broader plasticity claims.
- Why intra-cell haplotype divergence (~61%) is nearly equal to inter-cell divergence (~63%) is **not mechanistically explained** in the paper ([[10-Summaries/swanson-2025-daf-seq|DAF-seq]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — The ensemble open/closed measure that actuation refines per fiber.
> - `concept` [[30-Concepts/daf-seq|DAF-seq]] — Deaminase footprinting that measures actuation per fiber, haplotype and cell.
> - `concept` [[30-Concepts/fiber-seq|Fiber-seq]] — m6A methyltransferase footprinting of single fibers.
> - `concept` [[30-Concepts/single-molecule-footprinting|Single-molecule footprinting]] — Assays that mark accessible DNA on individual fibers.
> - `hub` [[40-Topics/chromatin-architecture|Chromatin architecture]] — How DNA packaging varies across fibers, haplotypes and cells.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/swanson-2025-daf-seq|Swanson 2025]]
