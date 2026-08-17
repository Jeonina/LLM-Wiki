---
type: summary
title: "Shahryary et al. 2020 — AlphaBeta: computational inference of epimutation rates and spectra from high-throughput DNA methylation data in plants"
source: "[[00-Sources/papers/AlphaBeta_ computational inference of epimutation rates and spectra from high-throughput DNA methylation data in plants]]"
source_kind: paper
author: "Yadollah Shahryary, Aikaterini Symeonidi, Rashmi R. Hazarika, Johanna Denkena, Talha Mubeen, Brigitte Hofmeister, Thomas van Gurp, Maria Colomé-Tatché, Koen J. F. Verhoeven, Gerald Tuskan, Robert J. Schmitz, Frank Johannes (corresponding)"
published: 2020-10-06
ingested: 2026-08-17
doi: "10.1186/s13059-020-02161-6"
journal: "Genome Biology 21:260"
tags: [AlphaBeta, epimutation-rate, pedigree, mutation-accumulation-lines, molecular-clock, tree-age-dating, Arabidopsis, poplar, neutral-accumulation]
entities: ["[[maria-colome-tatche]]"]
concepts: ["[[methylation-clones-epimutation]]", "[[epigenetic-aging]]", "[[epigenetic-memory]]", "[[lineage-tracing]]", "[[bisulfite-sequencing]]"]
topics: ["[[dna-methylation]]", "[[computational-methods]]", "[[single-cell-lineage-tracing]]"]
---

**Citation:** Shahryary et al. (2020) — *AlphaBeta: computational inference of epimutation rates and spectra from high-throughput DNA methylation data in plants* — *Genome Biology* 21, 260. [DOI](https://doi.org/10.1186/s13059-020-02161-6)

# Shahryary 2020 — AlphaBeta

> Where somatic mutations accumulate too slowly to time short intervals, **spontaneous epimutations** — stochastic gains and losses of DNA methylation — accumulate fast enough to act as a clock. AlphaBeta estimates their **forward and backward rates** (hence the name: α and β) from **pedigree-structured** methylation data, and delivers three findings that make epimutations usable as a lineage marker: they accumulate **neutrally** genome-wide, they originate **mainly during somatic development**, and they can **age-date trees**.

## Key claims

- **A pedigree is the required design.** Rates are estimable only when the genealogical relationships between the sampled methylomes are known — mutation-accumulation lines (clonal or sexual) or, for perennials, the branching structure of a long-lived individual.
- **Two rate parameters, not one.** Methylation gain and loss are separate stochastic processes with different rates, and estimating both is what "spectra" means here. A single "epimutation rate" would be a misleading summary.
- **Neutral accumulation at the genome-wide scale** — no evidence of selection acting on the bulk of spontaneous epimutations, which is precisely the property a molecular clock requires.
- **Somatic, not germline, origin.** Epimutations arise mainly during somatic development, which reframes them from a transgenerational-inheritance curiosity into a **somatic lineage record**.
- **Trees can be age-dated from their methylomes.** Applied to long-lived perennials, the accumulated epimutations act as a clock — a striking demonstration of the practical consequence.
- Works on both transgenerationally heritable epimutations (in mutation-accumulation lines) and somatic epimutations (in perennials).

## Methods / evidence

Method applied to published and newly generated pedigree-based methylation datasets spanning clonal and sexually derived mutation-accumulation lines and long-lived perennials.

Weight: **plants only**. Every result here is from plant systems, where methylation biology, transgenerational inheritance, and somatic development all differ substantially from mammals. The framework transfers; the rate estimates do not.

## Surprising or load-bearing bits

- **This is where the epimutation clock was quantified**, and the mammalian methylation-lineage-tracing literature ([[scherer-2025-nature|EPI-Clone]], [[chen-2025-methyltree|MethylTree]]) rests on the same premise — stochastic, neutral, heritable methylation changes as a barcode — arriving at it independently and later. Plants got there first, and with an explicit rate model. (synthesis)
- **"Somatic, not germline" is the finding that makes it a lineage tool.** If epimutations arose mainly in the germline they would mark individuals; arising somatically, they mark **cell lineages within an individual** — exactly what is needed for tracing. (synthesis)
- **Neutrality is a testable prerequisite, and it was tested.** Human epimutation-clock methods generally assume neutrality; AlphaBeta demonstrates it in its system. Whether it holds in mammalian tissue under selection is a live question that the human papers largely assume rather than establish. (synthesis)
- **Forward and backward rates being separate** matters for clock calibration: an equilibrium is reached when gains balance losses, which caps how far back the clock can read. The same saturation problem constrains [[gabbutt-2025-evoflux|fluctuating CpGs]] in human cancer.
- **Age-dating trees from methylomes** is the kind of result that travels — it is the plant analogue of inferring a human clone's age from its epigenetic state.

## Entities mentioned

- [[maria-colome-tatche]] — coauthor; computational epigenomics.

## Concepts touched

- [[methylation-clones-epimutation]] — the rate-estimation framework underlying epimutation-based lineage tracing.
- [[epigenetic-aging]] — epimutation accumulation as a molecular clock.

## Connections to other sources

- Mammalian descendants of the same premise: [[scherer-2025-nature]] (EPI-Clone, blood ageing), [[chen-2025-methyltree]] (MethylTree).
- Human cancer application of fluctuating methylation as a clock: [[gabbutt-2025-evoflux]].
- Methylation-clock and memory context: [[kim-2017-methylation-memory-review]], [[epigenetic-aging]], [[xiao-2025-epitrace]].
- Somatic-mutation clocks for comparison: [[coorens-2021-nature]], [[lee-six-2018-hsc-dynamics]], [[cagan-2022-nature]].
- Measurement substrate: [[bisulfite-sequencing]]; plant methylation context [[mo-2023-stam-seq]].
- Lineage-tracing reviews: [[rodriguez-fraticelli-2026-lineage-tracing-review]], [[wang-2026-multimodal-lineage-computational]].

## Open questions

- **Plant-to-mammal transfer is unestablished.** Plants lack a segregated germline and have different methylation maintenance machinery; whether the rate model and the neutrality finding hold in mammals is exactly the assumption the human epimutation-clock papers make. (synthesis)
- Bulk pedigree methylomes, not single cells — the single-cell version of this rate estimation is not addressed here.
- Clock saturation (when gain and loss reach equilibrium) bounds the readable time horizon; that bound is not quantified.

## Related

- [[scherer-2025-nature]] · [[chen-2025-methyltree]] · [[gabbutt-2025-evoflux]] · [[methylation-clones-epimutation]]
