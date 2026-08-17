---
type: summary
title: "Seidel et al. 2026 — SciPhy: a Bayesian phylogenetic framework using sequential genetic lineage tracing data"
source: "[[00-Sources/papers/SciPhy_ A Bayesian phylogenetic framework using sequential genetic lineage tracing data]]"
source_kind: paper
author: "Sophie Seidel, Antoine Zwaans, Samuel Regalado, Junhong Choi, Jay Shendure, Tanja Stadler (corresponding)"
published: 2026-06-10
ingested: 2026-08-17
doi: "10.1038/s41467-026-73377-6"
journal: "Nature Communications 17 (2026)"
tags: [SciPhy, sequential-editing, prime-editing, ordered-insertions, BEAST2, phylodynamics, UPGMA, gastruloid, HEK293T]
entities: ["[[jay-shendure]]"]
concepts: ["[[crispr-lineage-recording]]", "[[lineage-tracing]]", "[[phylogenetic-inference]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[computational-methods]]"]
---

**Citation:** Seidel, Zwaans, Regalado, Choi, Shendure & Stadler (2026) — *SciPhy: a Bayesian phylogenetic framework using sequential genetic lineage tracing data* — *Nature Communications* 17. [DOI](https://doi.org/10.1038/s41467-026-73377-6)

# Seidel 2026 — SciPhy

> Prime-editing recorders write edits **in order** — each insertion deactivates the current site and activates the next — so the barcode records not just *which* edits happened but *when relative to each other*. Every existing analysis of such data used **UPGMA with custom distance metrics**, which discards the ordering entirely. SciPhy models sequential insertion mechanistically in BEAST 2 and jointly estimates time-scaled phylogenies and population dynamics.

## Key claims

- **Order is free information that was being thrown away.** Sequential recorders guarantee irreversible, ordered edit accumulation. UPGMA, being distance-based clustering, "only leverages pairwise distances between cells, ignoring all higher-order information," and is agnostic to editing properties like variable insert propensities and variable insertion rates.
- **The model**: stably integrated barcodes accumulate edits sequentially and irreversibly at a constant Cas9 nicking rate; subsequent pegRNA-mediated insertions occur with varying probabilities. A phylogenetic likelihood is derived for the probability of a barcode alignment given a phylogeny and SciPhy parameters, implemented in BEAST 2 with MCMC.
- **Beyond a tree, you get uncertainty and rates.** Compared with UPGMA, SciPhy additionally reports **uncertainty** on the tree and **proliferation rates** — the phylodynamic quantities that a point-estimate clustering cannot provide.
- **Consistently more accurate phylogenies** than existing methods on simulated and real data from a monoclonal HEK293T culture.
- **Time-varying population dynamics in development.** Applied to murine gastruloids (in vitro differentiation of a single mESC into a multicellular structure modelling early mammalian development), SciPhy models shifting growth rates over time.
- **The reconstruction method changes the biology you infer.** The authors report "significant differences between our lineage tree estimates and those obtained with UPGMA, underscoring the impact of the reconstruction method on the inferred cellular relationships and growth dynamics."
- **Complex editing dynamics govern both datasets** — the recording process is not a clean uniform clock, which is precisely why a mechanistic model beats a generic distance.

## Methods / evidence

Validation on simulated data, benchmarking against existing methods on simulated and real monoclonal HEK293T culture data, then application to murine gastruloids. Implemented in BEAST 2; code at github.com/azwaans/SciPhy.

Weight: the monoclonal culture is the right benchmark substrate (known, homogeneous starting point). The gastruloid analysis is the demonstration of the phylodynamic capability rather than an independently validated biological claim.

## Surprising or load-bearing bits

- **"The method changes the answer" is the most important sentence for anyone reading lineage-tracing biology.** If UPGMA and SciPhy disagree significantly on the same data, then published growth-dynamic conclusions drawn with UPGMA are method-dependent. This is the lineage-tracing equivalent of the caller-concordance problem in mosaic variant calling ([[ha-2023-natmethods]]). (synthesis)
- **The recorder chemistry keeps outrunning the models.** Startle modelled non-modifiability for standard Cas9; LAML added heritable missingness and heterogeneous sites; SciPhy adds sequential ordering for prime-editing recorders. Each new chemistry invalidates the previous evolutionary model. Anyone choosing a tool must first ask what recorder generated the data. (synthesis)
- **Direct continuation of [[seidel-2022-tidetree|TiDeTree]]** from the same authors — same BEAST 2 phylodynamic framework, new editing model. The critique [[chu-2025-laml|LAML]] made of TiDeTree (built for older recorders) is answered here by targeting the newest ones.
- **Shendure as coauthor** connects this to the combinatorial-indexing and recorder-engineering line ([[cusanovich-2015-sciatac]], [[mulqueen-2018-sci-met]]) — the people building the recorders are on the paper modelling them.

## Entities mentioned

- [[jay-shendure]] — coauthor; sequential/prime-editing recorder development.

## Concepts touched

- [[crispr-lineage-recording]] — sequential insertion recorders and why they need their own evolutionary model.
- [[phylogenetic-inference]] — Bayesian phylodynamics with a mechanistic editing likelihood.

## Connections to other sources

- Direct predecessor, same authors and framework: [[seidel-2022-tidetree]].
- Contemporary maximum-likelihood alternative for a different recorder generation: [[chu-2025-laml]].
- Non-probabilistic methods it outperforms: [[gong-2022-dclear]], [[jones-2020-cassiopeia]], [[sashittal-2023-startle]].
- Recorder lineage: [[mckenna-2016-science]] (GESTALT).
- Review context: [[rodriguez-fraticelli-2026-lineage-tracing-review]], [[wang-2026-multimodal-lineage-computational]].

## Open questions

- **How much of the accuracy gain comes from using edit order** versus from Bayesian inference generally is not separated in the abstract.
- MCMC cost relative to [[chu-2025-laml|LAML]]'s EM approach is unstated — the two 2025/2026 methods have not been compared head to head.
- Sequential recorders remain engineered systems; none of this transfers to human tissue, where lineage must be read from endogenous markers. (synthesis)

## Related

- [[seidel-2022-tidetree]] · [[chu-2025-laml]] · [[crispr-lineage-recording]] · [[40-Topics/single-cell-lineage-tracing]]
