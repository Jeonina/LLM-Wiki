---
type: summary
title: "Heinz et al. 2010 — Lineage-determining TFs prime cis-regulatory elements (HOMER founding paper)"
source: "[[00-Sources/papers/Simple Combinations of Lineage-Determining Transcription Factors Prime cis-Regulatory Elements Required for Macrophage and B Cell Identities]]"
source_kind: paper
author: "Sven Heinz, Christopher Benner, Nathanael Spann, Eric Bertolino, Yin C. Lin, Peter Laslo, Jason X. Cheng, Cornelis Murre, Harinder Singh, Christopher K. Glass (corresponding)"
published: 2010-05-28
ingested: 2026-08-10
doi: "10.1016/j.molcel.2010.05.004"
journal: "Molecular Cell"
tags: [HOMER, motif-discovery, ChIP-seq, enhancer-priming, collaborative-binding, H3K4me1, pioneer-factor, computational-tool]
entities: []
concepts: ["[[de-novo-motif-discovery]]", "[[transcription-factor-motif]]", "[[cis-regulatory-element]]", "[[enhancer-states]]", "[[chip-seq]]"]
topics: ["[[histone-modifications]]", "[[chromatin-architecture]]"]
---

**Citation:** Heinz et al. (2010) — *Simple combinations of lineage-determining transcription factors prime cis-regulatory elements required for macrophage and B cell identities* — *Molecular Cell* 38, 576–589. [DOI](https://doi.org/10.1016/j.molcel.2010.05.004)

# Heinz 2010 — collaborative binding, and HOMER

> Two papers in one. Biologically: cell-type-specific enhancer repertoires are set by **small collaborative sets of lineage-determining TFs** binding at closely spaced motifs, which displace nucleosomes and induce H3K4me1 — creating "primed" elements that a second tier of signal-dependent factors (LXR, TLR4-responsive) can later use. Methodologically: HOMER, the motif-discovery and ChIP-seq analysis suite, was written to support this study and became the field's default.

## Key claims

- PU.1 cistromes are largely cell-type-specific at distal sites (45,631 macrophage / 32,575 B-cell peaks; 17,130 shared) while >80% of promoter-proximal PU.1 sites are occupied equally in both — specificity lives in the distal compartment.
- Cell-type-specific PU.1 sites are co-enriched, within ~100 bp, for motifs of the *other* lineage-determining factors: C/EBP and AP-1 in macrophages, E2A/EBF/Oct in B cells — and each set is depleted at the opposite lineage's sites.
- The dependency is causal in both directions: PU.1 binding at B-lineage sites requires E2A (tamoxifen-inducible E47-ER gains 3,752 PU.1 sites in 6 h; a transactivation-domain-deleted mutant does not), and C/EBPβ binding collapses in PU.1⁻/⁻ myeloid progenitors and is restored on PU.1 induction.
- PU.1 binding **precedes and causes** H3K4me1: of 7,428 strongly induced PU.1 sites, 43% gain H3K4me1 by 24 h with the characteristic bimodal dip centered on the motif; 32% had pre-existing H3K4me1 and get remodeled; 25% gain nothing despite stable PU.1 — so PU.1 is necessary but not sufficient.
- MNase-seq shows nucleosome remodeling at 1 h: linker expansion over the PU.1 site and compression of flanking nucleosomes for ~1 kb.
- Second-tier factors are subordinate: 34% of LXRβ peaks lie within 100 bp of a PU.1 site and LXRβ recruitment at those sites is PU.1-dependent, while PU.1 cistrome and H3K4me1 are unchanged in LXRα/β double-knockout macrophages. 14 of 20 TLR4-response genes require PU.1 for induction.
- The logic generalizes: de novo motif analysis of distal H3K4me1 regions in ES cells, liver, CD4⁺ T cells and erythroid precursors recovers exactly the known lineage-determining factors for each (KLF4/OCT4/SOX2/Esrrβ in ES cells; Ets/Runx in T cells).

## Methods / evidence

ChIP-seq for PU.1, C/EBPα/β, Oct-2, LXRβ, H3K4me1, H3K4me3 across primary macrophages, splenic B cells, and staged B-progenitors (*E2A⁻ᐟ⁻*, *EBF⁻ᐟ⁻*, *Rag1⁻ᐟ⁻*); MNase-seq for nucleosome positions; inducible ER-fusion systems (PUER, E47-ER) for temporal ordering; transient reporter assays for enhancer function; microarray transcriptomes. The inducible systems are what convert correlation into sequence-of-events — this is the strongest part of the paper. Peak calling at 0.1% FDR **using HOMER**, which the methods section notes "in part was created to support this study."

## Surprising or load-bearing bits

- Only ~15% of PU.1 sites drove constitutive enhancer activity in reporter assays, but 10/11 LXR-PU.1 co-bound regions showed *ligand-dependent* activity. Primed ≠ active; the field's habit of equating open chromatin with function starts failing right here.
- The bimodal H3K4me1 dip over the motif is not a mark of "the enhancer center is unmarked" — MNase and DNase alignment show it reflects **absolute nucleosome positions**, the motif sitting in an expanded linker. This is the same physical picture that [[single-molecule-footprinting]] methods later resolve per-molecule.
- HOMER's origin as study infrastructure explains its design: it is a ChIP-seq-era peak-and-motif toolkit, and its known-motif library is still what [[schep-2017-chromvar|chromVAR]] and scATAC pipelines lean on decades of downstream.

## Concepts touched

- [[de-novo-motif-discovery]] / [[transcription-factor-motif]] — HOMER is the founding implementation for both pages.
- [[enhancer-states]] — supplies the *primed* state (H3K4me1, PU.1-bound, not yet active), complementing [[creyghton-2010-h3k27ac-enhancers|Creyghton 2010]]'s active/poised split via H3K27ac. The two 2010 papers together define the enhancer-state vocabulary this wiki uses.
- [[cis-regulatory-element]] — "proto-enhancer" / two-tier model.
- [[chromatin-accessibility]] — collaborative nucleosome displacement is the mechanistic account of what an ATAC peak *is*.

## Connections to other sources

- Direct companion to [[creyghton-2010-h3k27ac-enhancers]] (which this paper's reference list cites): H3K4me1 = primed, +H3K27ac = active.
- HOMER motif enrichment is the standard downstream step for [[buenrostro-2015-nature]]/[[cusanovich-2015-sciatac]]-style scATAC peaks, and the alternative to the deviation-based framing in [[schep-2017-chromvar]].
- The nucleosome-scale picture is what [[andrewb-2020-science]] and [[shipony-2020-smac]] measure directly on single molecules.
- [[mclean-2010-great|GREAT]] is the complementary tool for the *other* question about a distal peak set — which genes they regulate, rather than which factors bind them.

## Open questions

- Group III (25% of induced PU.1 sites gaining no H3K4me1) is unexplained — what distinguishes sites where a lineage factor binds but priming fails? Still open in the corpus.
- Whether collaborative binding is detectable *within single cells* (do both factors co-occupy the same molecule?) is exactly what multi-factor single-cell methods ([[multi-tag]], [[gopalan-2022-multi-cut-and-tag]]) were built to ask.

## Related

- [[creyghton-2010-h3k27ac-enhancers]] · [[de-novo-motif-discovery]] · [[enhancer-states]] · [[histone-modifications]]
