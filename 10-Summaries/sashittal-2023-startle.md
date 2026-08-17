---
type: summary
title: "Sashittal et al. 2023 — Startle: a star homoplasy approach for CRISPR-Cas9 lineage tracing"
source: "[[00-Sources/papers/Startle_ A star homoplasy approach for CRISPR-Cas9 lineage tracing]]"
source_kind: paper
author: "Palash Sashittal, Henri Schmidt, Michelle Chan, Benjamin J. Raphael (corresponding)"
published: 2023-12-20
ingested: 2026-08-17
doi: "10.1016/j.cels.2023.11.005"
journal: "Cell Systems 14:1113–1121"
tags: [Startle, star-homoplasy, maximum-parsimony, non-modifiability, CRISPR-Cas9, metastasis, KP-tracer, lung-adenocarcinoma]
entities: []
concepts: ["[[crispr-lineage-recording]]", "[[lineage-tracing]]", "[[phylogenetic-inference]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[cancer-clonal-evolution]]", "[[computational-methods]]"]
---

**Citation:** Sashittal, Schmidt, Chan & Raphael (2023) — *Startle: a star homoplasy approach for CRISPR-Cas9 lineage tracing* — *Cell Systems* 14, 1113–1121. [DOI](https://doi.org/10.1016/j.cels.2023.11.005)

# Sashittal 2023 — Startle

> Standard phylogenetics can be applied to CRISPR barcodes, but it models the wrong process. The distinctive property of Cas9 editing is **non-modifiability**: once a target site is edited, the guide RNA no longer matches and the site can never change again. Startle encodes exactly this as the **star homoplasy** model — a character may mutate **at most once along any lineage**, but the same character state may arise independently in different lineages — and computes a maximum-parsimony tree under it.

## Key claims

- **Star homoplasy is the right constraint, and it is not standard.** Classical models either forbid homoplasy entirely (perfect phylogeny / infinite sites) or allow unrestricted repeated mutation (finite sites). Star homoplasy sits in neither camp: it permits the *same edit outcome* to appear convergently in unrelated lineages — which happens constantly in Cas9 systems because a handful of indel outcomes dominate — while forbidding a site from mutating twice down one lineage.
- **A combinatorial characterisation of star homoplasy phylogenies** is derived, and that characterisation is what makes the maximum-parsimony algorithm possible.
- **More accurate than existing methods on simulated lineage tracing data.**
- **On real data it finds parsimonious phylogenies with fewer metastatic migrations** in a mouse model of metastatic lung adenocarcinoma. This is the biologically consequential result: migration count is inferred *from* the tree, so a tree that requires fewer migrations changes the metastasis narrative.
- The stated motivation is that "the unique features of the CRISPR-Cas9 editing process motivate the development of specialized models" — the same argument [[el-kebir-2018-sphyr|SPhyR]] makes for cancer SNVs, applied to a different mutational process.

## Methods / evidence

Simulated lineage tracing data for accuracy benchmarking; real data from a mouse metastatic lung adenocarcinoma (KP-tracer lineage). The clipping captures highlights, summary and the opening of the introduction; detailed results are not included.

## Surprising or load-bearing bits

- **The evolutionary model is a property of the *recorder chemistry*, not of biology.** Non-modifiability exists because of how Cas9 and its guide RNA work. This is a genuinely different situation from cancer phylogenetics, where the model encodes a claim about tumour biology — here it encodes a claim about a piece of engineering, and is therefore much better justified. (synthesis)
- **Fewer migrations is a substantive reinterpretation.** Metastasis counts derived from lineage trees are only as good as the tree; a model mismatch inflates apparent convergent evolution, which reads as extra migration events. Startle's result implies prior migration estimates from CRISPR-traced tumours may be overstated. (synthesis)
- **Convergent edits are the core difficulty of CRISPR lineage tracing**, and every method in this batch attacks it differently: Startle by permitting homoplasy in a constrained way, [[gong-2022-dclear|DCLEAR]] by weighting distances, [[seidel-2026-sciphy|SciPhy]] and [[chu-2025-laml|LAML]] by modelling edit-outcome probabilities directly. (synthesis)
- **Raphael-lab lineage**: Startle and [[chu-2025-laml|LAML]] share authors (Schmidt, Raphael), and LAML explicitly positions Startle as the parsimony member of the non-probabilistic camp — accurate topologies, no branch times.

## Concepts touched

- [[crispr-lineage-recording]] — non-modifiability as the defining constraint, formalised as star homoplasy.
- [[phylogenetic-inference]] — a new evolutionary model with a combinatorial characterisation and parsimony algorithm.

## Connections to other sources

- Same-lab successor that adds time-resolved branch lengths: [[chu-2025-laml]].
- Parsimony predecessor for CRISPR barcodes: [[jones-2020-cassiopeia]].
- Distance-based DREAM winner: [[gong-2022-dclear]].
- Bayesian alternatives modelling edit probabilities: [[seidel-2022-tidetree]], [[seidel-2026-sciphy]].
- Recorder technology: [[mckenna-2016-science]].
- Cancer-phylogeny analogues of "pick the model that matches the mutational process": [[el-kebir-2018-sphyr]], [[zafar-2017-sifit]].
- Review context: [[rodriguez-fraticelli-2026-lineage-tracing-review]], [[wang-2026-multimodal-lineage-computational]].

## Open questions

- **Topology only** — no time-resolved branch lengths, so timing questions (when did migration happen) are out of reach; this is what LAML adds two years later.
- The clipping does not report how much of the accuracy gain comes from the model versus the parsimony criterion.
- Whether star homoplasy remains the right model for **sequential/prime-editing** recorders, where sites activate one another, is not addressed — [[seidel-2026-sciphy|SciPhy]] argues these need a different model again.

## Related

- [[chu-2025-laml]] · [[jones-2020-cassiopeia]] · [[crispr-lineage-recording]] · [[40-Topics/single-cell-lineage-tracing]]
