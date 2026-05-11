---
type: concept
title: Chromatin actuation
aliases: [actuation, fiber actuation]
tags: [chromatin, single-molecule]
created: 2026-05-07
updated: 2026-05-07
---

# Chromatin actuation

> The state of a regulatory element being **simultaneously open and bound** along a specific chromatin fiber, as measured at single-molecule resolution by deaminase or methyltransferase footprinting — a per-fiber refinement of [[chromatin-accessibility]].

## Definition

In bulk and single-cell ATAC-seq, "accessible" is a count over many fibers. In single-molecule footprinting ([[daf-seq]], [[fiber-seq]]), each individual fiber either *is* or *is not* in a state where (a) the element is nucleosome-free and (b) the predicted TFs are bound. The latter state is **actuation** ([[10-Summaries/elliott-2025-naturebiotechnology]] terminology).

scDAF-seq measures actuation per fiber, per haplotype, per cell — yielding the unit of analysis "is regulatory element X actuated on haplotype Y of cell Z?"

## Why it matters

Two findings from [[10-Summaries/elliott-2025-naturebiotechnology]] are only visible because actuation is measurable per fiber:

1. **Pervasive plasticity.** ~63% of regulatory elements differ in actuation status between two random cells. ~61% differ between haplotypes within the same cell. The intra-cellular and inter-cellular numbers being comparable is a strong claim about how much of regulatory variability is stochastic per fiber rather than programmed per cell state or trans-environment.
2. **Co-actuation in ~100 kb domains.** Pairs of regulatory elements on the same fiber are preferentially actuated together, with the distance dependence mirroring cohesin loops. This is the first chromosome-length single-molecule confirmation of a long-suspected pattern.

## Variants and refinements

- **Per-fiber actuation** — each long-read sequenced fiber gives a binary actuation call per element.
- **Aggregated chromatin actuation** — averaged over fibers; recovers ATAC-like peak calls.
- **Co-actuation** — joint actuation status of two elements on the same fiber.

## Contested points

- The framing assumes binary "actuated / not actuated" calls; the reality is graded (partial occupancy, transient binding). The thermodynamic ΔG analysis in [[10-Summaries/elliott-2025-naturebiotechnology]] handles this for TF cooperativity but not for the broader plasticity claims.
- Why intra-cell haplotype divergence (~61%) is nearly equal to inter-cell divergence (~63%) is **not mechanistically explained** in the paper.

## Examples

- SLC39A4 promoter actuation in liver tissue is preferentially driven by the rs2280838-T haplotype via altered nucleosome positioning ([[10-Summaries/elliott-2025-naturebiotechnology]]).
- COLO829T melanoma CC>TT mutation eliminates actuation only on the variant haplotype ([[10-Summaries/elliott-2025-naturebiotechnology]]).

## Related

- [[chromatin-accessibility]]
- [[daf-seq]]
- [[fiber-seq]]
- [[single-molecule-footprinting]]
- [[40-Topics/chromatin-architecture]]
