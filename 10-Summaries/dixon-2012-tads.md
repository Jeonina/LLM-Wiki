---
type: summary
title: "Dixon et al. 2012 — Topological domains in mammalian genomes identified by analysis of chromatin interactions"
source: "[[00-Sources/papers/Topological domains in mammalian genomes identified by analysis of chromatin interactions]]"
source_kind: paper
author: "Jesse R. Dixon, Siddarth Selvaraj, Feng Yue, Audrey Kim, Yan Li, Yin Shen, Ming Hu, Jun S. Liu, Bing Ren (corresponding)"
published: 2012-04-11
ingested: 2026-08-10
doi: "10.1038/nature11082"
journal: "Nature"
tags: [TAD, topological-domains, directionality-index, CTCF, insulator, founding-paper, conservation, Hi-C]
entities: ["[[bing-ren]]"]
concepts: ["[[topologically-associating-domain]]", "[[chromatin-compartments]]", "[[lamina-associated-domains]]", "[[replication-timing]]", "[[transposable-elements]]", "[[cis-regulatory-element]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Dixon et al. (2012) — *Topological domains in mammalian genomes identified by analysis of chromatin interactions* — *Nature* 485, 376–380. [DOI](https://doi.org/10.1038/nature11082)

# Dixon 2012 — topological domains

> Push Hi-C resolution below 100 kb and a new feature appears: **highly self-interacting megabase blocks with abrupt boundaries** — visible as triangles on the contact map. Dixon named them topological domains, showed they are pervasive, cell-type-stable and conserved between mouse and human, and identified what marks their boundaries: CTCF, housekeeping genes, tRNAs and SINEs.

## Key claims

- **>1.7 billion Hi-C read pairs** across mouse ES cells, human ES cells, human IMR90 fibroblasts and mouse cortex — the depth that made sub-megabase structure visible where [[lieberman-aiden-2009-hic|1 Mb binning]] could not resolve it.
- **The directionality index** is the methodological contribution: a per-bin statistic quantifying upstream-vs-downstream interaction bias, which swings sharply at domain edges. **52% of the genome** has a directionality index not expected by chance (1% FDR). A Hidden Markov model on that index calls the domains.
- **2,200 topological domains in mouse ES cells, median 880 kb, covering ~91% of the genome.** Intra-domain contact exceeds inter-domain contact, and FISH probes within a domain are closer in nuclear space than probes at matched genomic distance across a boundary.
- **Boundaries behave like classical insulators.** Strong CTCF enrichment; the experimentally validated *Hoxa* insulator coincides with a boundary in both mouse and human; and H3K9me3 segregates sharply at boundaries in differentiated cells. Critically, the boundaries are present in pluripotent cells *before* the heterochromatin appears — so **domains pre-mark where heterochromatin spreading will stop, rather than being a consequence of it**.
- **Domains are related to but independent of** A/B compartments, LADs, replication timing zones and LOCK domains; a subset of boundaries mark LAD/non-LAD, A/B and early/late-replication transitions.
- **Stability across cell types, dynamism within.** Most boundaries are shared between cell types. 9,888 dynamic interacting regions were found between mouse ES and cortex, enriched for differentially expressed genes — **20% of all genes with a ≥4-fold expression change sit at dynamic interacting loci** — yet **>96% of dynamic interactions occur within the same domain**. The scaffold is fixed; the wiring inside it changes.
- **Evolutionary conservation**: 53.8% of human boundaries are boundaries in mouse and 75.9% of mouse boundaries are boundaries in human, versus 21.0% and 29.0% expected at random (P < 2.2 × 10⁻¹⁶).
- **CTCF is necessary-ish but nowhere near sufficient**: only **15% of CTCF binding sites** fall within boundary regions. Boundaries are additionally enriched for active-promoter marks, TSSs, GRO-seq signal, **housekeeping genes** and **tRNA genes** — while enhancer-associated H3K4me1 and H3K9me3 are not enriched or are depleted. Boundaries with both CTCF and a housekeeping gene account for **nearly one-third** of all boundaries.
- Alu/B1 and B2 **SINE retrotransposons** are enriched at boundaries in both species.

## Methods / evidence

Hi-C across four cell types with normalization for known biases; validation against prior 3C, 5C and FISH datasets, including recovery of a known cell-type-specific *Phc1* interaction and correlation with 2D-FISH distances; replicate-reproducible directionality index and HMM domain calls; liftOver-based cross-species boundary comparison with a random-expectation baseline.

Limitation the authors state directly: they "cannot determine if the differences in domain calls between cell types is due to noise in the data or to biological phenomena, such as a change in the strength of the boundary region" — the honest version of the cell-type-invariance claim.

## Surprising or load-bearing bits

- **The 15% CTCF figure is the most cited-past detail here.** CTCF binds tens of thousands of sites; only a small minority sit at boundaries. Boundary identity is combinatorial — CTCF *plus* transcriptional activity — which is why later CTCF-depletion experiments disrupt insulation without abolishing domains, and why [[spielmann-2018-sv-3d-genome|deleting a boundary's CTCF sites alone]] at *Sox9* had no major effect.
- **Housekeeping genes and tRNAs as boundary elements** reframes domain formation as partly a *consequence of transcription* rather than purely of architectural protein binding — the transcription-as-insulator idea imported from yeast and *Drosophila*.
- **Domains precede heterochromatin.** This is the strongest causal-direction evidence in the paper and it argues the domain structure is instructive, not descriptive.
- The **stable-scaffold / dynamic-interior** model resolves an apparent contradiction with earlier reports of cell-type-specific conformations, and it is the reason patient fibroblasts can report on developmental regulatory events ([[lupianez-2015-tad-disruption]]).
- **Naming**: this paper says "topological domains"; the companion Nora et al. paper on the X-inactivation centre says "topologically associating domains (TADs)". The acronym that stuck came from the companion.
- SINEs at boundaries connects genome organization to transposon biology — retrotransposition remodels CTCF site distribution across lineages.

## Entities mentioned

- [[bing-ren]] — corresponding author; the Hi-C-based regulatory-genomics program continues through [[zhu-2020-multimodal-power-of-many]].

## Concepts touched

- [[topologically-associating-domain]] — this is the founding source; the directionality-index/HMM call is one of the two operational definitions in use (the other being [[durand-2016-juicer|Arrowhead]]).
- [[lamina-associated-domains]] / [[replication-timing]] — related but independent domain organizations; a subset of boundaries mark their transitions.
- [[transposable-elements]] — SINE enrichment at boundaries.

## Connections to other sources

- Built directly on [[lieberman-aiden-2009-hic]]; the resolution increase is what revealed the feature.
- Causal disease demonstration: [[lupianez-2015-tad-disruption]]; clinical taxonomy: [[spielmann-2018-sv-3d-genome]].
- TADs shown to be interphase-only in [[naumova-2013-mitotic-chromosome]].
- LAD comparison draws on [[peric-hupkes-2010-lad-differentiation]].
- Single-cell tests of domain invariance: [[nagano-2013-nature]], [[ramani-2017-scihi-c]], [[tan-2018-science]].

## Open questions

- Whether cell-type-specific boundary calls are biology or noise — flagged by the authors, unresolved here.
- The claim that boundaries are "largely invariant" is a population statement. Per-cell boundary presence, and whether a boundary is a probabilistic barrier, is the single-cell question this paper cannot address.

## Related

- [[lieberman-aiden-2009-hic]] · [[topologically-associating-domain]] · [[lupianez-2015-tad-disruption]] · [[3d-genome]]
