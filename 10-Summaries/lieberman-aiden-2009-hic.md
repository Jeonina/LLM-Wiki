---
type: summary
title: "Lieberman-Aiden et al. 2009 — Comprehensive mapping of long-range interactions reveals folding principles of the human genome (Hi-C)"
source: "[[00-Sources/papers/Comprehensive Mapping of Long-Range Interactions Reveals Folding Principles of the Human Genome]]"
source_kind: paper
author: "Erez Lieberman-Aiden, Nynke L. van Berkum, Louise Williams, Maxim Imakaev, Tobias Ragoczy, Agnes Telling, Ido Amit, Bryan R. Lajoie, Peter J. Sabo, Michael O. Dorschner, ... Leonid A. Mirny, Eric S. Lander, Job Dekker (corresponding)"
published: 2009-10-09
ingested: 2026-08-10
doi: "10.1126/science.1181369"
journal: "Science"
tags: [Hi-C, founding-method, A-B-compartments, fractal-globule, chromosome-territories, proximity-ligation, 3C]
entities: []
concepts: ["[[single-cell-hi-c]]", "[[chromatin-compartments]]", "[[topologically-associating-domain]]", "[[chromatin-accessibility]]", "[[dnase-seq]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Lieberman-Aiden et al. (2009) — *Comprehensive mapping of long-range interactions reveals folding principles of the human genome* — *Science* 326, 289–293. [DOI](https://doi.org/10.1126/science.1181369)

# Lieberman-Aiden 2009 — Hi-C

> The founding assay of the 3D genome field. Crosslink, digest, fill 5′ overhangs with a **biotinylated** residue, ligate under dilution, shear, pull down the biotinylated junctions with streptavidin, sequence paired-end. Everything before it (3C, 4C, 5C) required choosing target loci; Hi-C is the first genome-wide, unbiased contact map.

## Key claims

- **The method.** Biotin fill-in at the restriction junction is the enabling trick — it marks ligation products so they can be purified away from the vast excess of non-informative DNA, turning proximity ligation into a sequencing-scale assay.
- Scale of the founding experiment, worth remembering: **one lymphoblastoid cell line (GM06990), two Illumina lanes, 8.4 million uniquely aligned read pairs**, of which 6.7 million were long-range contacts >20 kb. The contact matrix was built at **1 Mb** resolution.
- Reproducible across enzymes: HindIII replicate r = 0.990, NcoI r = 0.814 (P < 10⁻³⁰⁰ both).
- **Chromosome territories confirmed**: intrachromosomal contact probability *I_n(s)* decreases monotonically but stays far above interchromosomal contact even beyond 200 Mb. Small gene-rich chromosomes (16, 17, 19, 20, 21, 22) preferentially interact; gene-poor chromosome 18 does not — matching FISH placement near the periphery.
- **The A/B compartment discovery.** Normalizing by distance-expected contact reveals a plaid pattern; correlating interaction profiles sharpens it (71% of entries significant); PCA on the correlation matrix partitions each chromosome into two sets whose labels are **consistent across chromosomes**. The whole genome splits into two spatial compartments.
- Validated orthogonally by **3D-FISH**: four loci alternating between compartments on chromosome 14 show L3 closer to L1 than to L2, despite L2 lying between them in the linear sequence. Genome-wide, Hi-C read count correlates with FISH 3D distance (Spearman ρ = −0.916).
- **Compartment A = open chromatin**: correlates with gene density (ρ = 0.431), expression (ρ = 0.476), and most strongly **DNase I sensitivity (ρ = 0.651)**. Compartment B is more densely packed.
- Compartments are **cell-type-dependent**: K562 shares the overall structure but many loci switch, and switching tracks that cell type's own chromatin accessibility — even in a highly rearranged cancer karyotype.
- **The fractal globule.** Contact probability scales as *s*^−1 between ~500 kb and ~7 Mb. The equilibrium globule predicts *s*^−3/2; the fractal (crumpled) globule predicts *s*^−1, matching the observed −1.08. Monte Carlo ensembles of 500 each reproduced both scalings and confirmed the fractal globule is **knot-free**, so any locus can be unfolded and refolded — an attractive property for gene activation and the cell cycle.
- The resolution rule, stated at the outset: **improving resolution *n*-fold requires *n*² more reads.**

## Methods / evidence

Two restriction enzymes, biological replicates, two cell types, orthogonal 3D-FISH validation of both the compartment partition and the read-count-to-distance relationship, and polymer simulation to discriminate two competing physical models. For a founding methods paper this is an unusually complete validation design — the FISH work is what makes the compartment claim more than a pattern in a heatmap.

The authors also state the limit plainly: "we cannot rule out the possibility that other forms of regular organization might lead to similar findings."

## Surprising or load-bearing bits

- **The n² scaling rule governs everything downstream in this wiki.** It is why single-cell Hi-C is sparse by construction: a single cell contributes a fixed, small number of contacts, so per-cell resolution can never be bought with more cells — only pooling helps, and pooling destroys the single-cell question. Every method from [[nagano-2013-nature|Nagano 2013]] to [[ramani-2017-scihi-c|sciHi-C]] to [[tan-2018-science|Dip-C]] is negotiating with this inequality.
- Hi-C read count works as a **proxy for physical distance** (ρ = −0.916 against FISH). That is what licenses treating contact matrices as structural data rather than as an abstract statistic.
- The fractal globule's motivation is functional, not just descriptive: knot-free packing means folding is reversible. This is the physical basis for the mitotic/interphase interconversion later mapped in [[naumova-2013-mitotic-chromosome|Naumova 2013]] — which then shows the *mitotic* state is **not** a fractal globule (*s*^−0.5), so the fractal-globule description is interphase-specific.
- Compartments were found *before* TADs and at a coarser scale; the field's two-level vocabulary (compartments Mb-scale, TADs sub-Mb) is a direct consequence of this paper's 1 Mb binning versus [[dixon-2012-tads|Dixon 2012]]'s <100 kb binning. The features were always there — resolution revealed them.
- Compartment switching tracking cell-type-specific accessibility, in a rearranged cancer genome, is the earliest evidence that 3D compartmentalization is a *readout* of chromatin state rather than a fixed scaffold.

## Concepts touched

- [[chromatin-compartments]] — this is the founding source for A/B compartments and the PCA-based calling procedure still in use.
- [[single-cell-hi-c]] — the assay all single-cell variants adapt, and the source of their sparsity constraint.
- [[chromatin-accessibility]] — DNase sensitivity is the strongest correlate of compartment A.

## Connections to other sources

- Directly builds to [[dixon-2012-tads]] (sub-megabase domains at higher resolution) and [[naumova-2013-mitotic-chromosome]] (both compartments and TADs vanish in metaphase).
- Pipeline descendants: [[servant-2015-hicpro|HiC-Pro]], [[durand-2016-juicer|Juicer]], [[abdennur-2020-cooler|Cooler]].
- Single-cell descendants: [[nagano-2013-nature]], [[ramani-2017-scihi-c]], [[tan-2018-science]], [[lee-2019-natmethods]].
- The disease-interpretation layer built on this substrate: [[lupianez-2015-tad-disruption]], [[spielmann-2018-sv-3d-genome]].

## Open questions

- Whether the fractal globule describes chromatin in individual cells or only the population average was unanswerable in 2009 and is only partly settled now — [[ramani-2017-scihi-c]] finds per-cell scaling coefficients are far more disperse than shuffled controls.
- The paper's own caveat — other organizations could produce the same *P(s)* — has never been definitively closed.

## Related

- [[chromatin-compartments]] · [[dixon-2012-tads]] · [[naumova-2013-mitotic-chromosome]] · [[3d-genome]]
