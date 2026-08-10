---
type: summary
title: "Naumova et al. 2013 — Organization of the mitotic chromosome"
source: "[[00-Sources/papers/Organization of the Mitotic Chromosome]]"
source_kind: paper
author: "Natalia Naumova, Maxim Imakaev, Geoffrey Fudenberg, Ye Zhan, Bryan R. Lajoie, Leonid A. Mirny, Job Dekker (corresponding)"
published: 2013-11-08
ingested: 2026-08-10
doi: "10.1126/science.1236083"
journal: "Science"
tags: [mitotic-chromosome, Hi-C, 5C, cell-cycle, polymer-modeling, loop-extrusion-precursor, compartments, TAD-loss, epigenetic-memory]
entities: []
concepts: ["[[single-cell-hi-c]]", "[[chromatin-compartments]]", "[[topologically-associating-domain]]", "[[epigenetic-memory]]", "[[replication-timing]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Naumova et al. (2013) — *Organization of the mitotic chromosome* — *Science* 342, 948–953. [DOI](https://doi.org/10.1126/science.1236083)

# Naumova 2013 — the two folding states

> 5C and Hi-C across the cell cycle reveal that the genome has exactly **two** three-dimensional states: a cell-type-specific, locus-specific interphase organization (compartments, TADs), and a **homogeneous, locus-independent, cell-type-invariant metaphase state**. Polymer simulation rejects hierarchical coiling models and identifies the metaphase chromosome as a linearly ordered, axially compressed array of consecutive ~80–120 kb chromatin loops.

## Key claims

- Early-G₁, mid-G₁ and S-phase 5C interaction patterns on chromosome 21 are highly correlated with each other and with nonsynchronous cells (Spearman r > 0.67). **Mitotic patterns are not** (r < 0.27). Two states, not a continuum.
- In metaphase, A/B **compartmentalization disappears genome-wide** — eigenvector decomposition finds no alternating profile, and preferential interactions by GC content or interphase chromatin marks are lost.
- **TAD signal collapses too.** Residual TAD-like variation is attributable to the ~15% non-mitotic contamination in nocodazole-arrested cultures; a 98%-synchrony dataset shows further loss. Not a crosslinking artifact — 4-fold lower formaldehyde gives the same result.
- Metaphase maps are near-identical across HeLa S3, K562 and primary HFF1 fibroblasts, while their interphase compartment locations differ. Metaphase folding is universal.
- Contact probability *P(s)* ~ s^−0.5 from 100 kb to 10 Mb, then a sharp fall-off at ~10 Mb, for every chromosome regardless of length. Interpretation: linear order above 10 Mb (consecutive regions occupy consecutive longitudinal positions), spatially mixed ~10 Mb "layers" below.
- s^−0.5 sits **between** the fractal globule (s^−1, segregated) and equilibrium globule (s^0, fully mixed) — intermediate mixing, so neither classic polymer state describes metaphase.
- Model discrimination: hierarchical coiling/looping models decay far too steeply (contacts too local); scaffold-attraction-only and non-consecutive-loop models also fail. **Consecutive loops** of 80 kb (with scaffold) or 120 kb (scaffold-free) reproduce the data, matching independent loop-size estimates of 30–90 kb and 83 ± 29 kb.
- Proposed two-stage mechanism: (I) linear compaction into consecutive loops — explicitly attributed to loop-extruding SMC complexes, citing Alipour & Marko — producing a ~5 µm prophase-like chromatid, then (II) homogeneous axial compression of the loop-base backbone.
- Cell-to-cell variability in loop position and size is **required** to reproduce the homogeneous population-average maps.

## Methods / evidence

5C at ~25 kb primer spacing on chromosome 21 across early-G₁, mid-G₁, S, and nocodazole-arrested prometaphase; genome-wide Hi-C in mid-G₁ and mitosis for three cell types; ICE normalization (which also corrects the HeLa karyotype's copy-number bias); Langevin-dynamics polymer simulation of 128,000 monomers (~600 bp each, 10 nm fiber) with topoisomerase-II-like strand passage permitted.

Controls are thorough: nocodazole 3/7/12 h give similar Hi-C; low-formaldehyde replicate; high-synchrony replicate; results robust to 10 nm vs 30 nm fiber assumptions. The model comparison is the paper's real contribution — it is a falsification exercise, and hierarchical models are the casualty.

Caveat the authors name: this is the *final folded state*; folding pathway and initial conformations are unknown, so equilibrium models were used.

## Surprising or load-bearing bits

- **The epigenetic-memory problem stated sharply.** If compartments *and* cell-type-invariant TADs are both absent in mitosis, higher-order chromatin structure cannot itself be the carrier of epigenetic memory — it must be rebuilt de novo in early G₁, presumably templated by histone marks, DNA methylation, and mitotically retained proteins ("bookmarking"). This directly constrains what [[epigenetic-memory]] can mean: the memory is in the marks, not the fold.
- The loop-extrusion mechanism is proposed here as the *inference from contact-probability shape*, years before extrusion was imaged. A polymer-physics argument anticipated the mechanism.
- **Irregularity is required, not tolerated.** Classical models assumed regular solenoids and fixed loop lengths; this model needs stochastic loop positions and partial mixing. The authors note their mechanism is robust to chromosome size, composition, and genomic rearrangement precisely because it is local and sequence-agnostic — which matters for aneuploid and structurally rearranged genomes ([[cancer-clonal-evolution]]).
- The paper closes by naming **single-cell Hi-C** as the needed next step — this corpus's [[nagano-2013-nature|Nagano 2013]] appeared the same year.

## Concepts touched

- [[chromatin-compartments]] — compartments are an interphase-only phenomenon; this is the source for that boundary condition.
- [[topologically-associating-domain]] — TADs are also interphase-only, which reframes the boundary function demonstrated in [[lupianez-2015-tad-disruption]] as something re-established every cycle rather than permanently installed.
- [[epigenetic-memory]] — supplies the negative result that forces mark-based (not structure-based) inheritance models.
- [[single-cell-hi-c]] — the population-average homogeneity here is explicitly attributed to per-cell loop variability, which is the motivating hypothesis for single-cell 3D genomics.

## Connections to other sources

- Same-year companion in this wiki: [[nagano-2013-nature]] (single-cell Hi-C), which asks whether interphase structure is per-cell reproducible.
- Rejects the interphase fractal-globule reading of [[lieberman-aiden-2009-hic|Lieberman-Aiden 2009 (Hi-C)]] for mitosis specifically — different state, different polymer model.
- [[tan-2018-science|Dip-C]] and [[lee-2019-natmethods|sn-m3C-seq]] inherit the cell-cycle confound this paper makes unavoidable: a single-cell Hi-C dataset containing mitotic cells is mixing two structurally unrelated states.
- Relevant to [[liu-2023-mouse-brain-methylome-3d]] and [[hong-2025-sc3d-genome-review]].

## Open questions

- If mitotic chromosomes are structurally identical across cell types, **can any 3D-genome measurement distinguish cell identity in a mitotic cell?** For single-cell 3D methods applied to proliferating tissue (tumors, progenitors), this is a hard limit on cell-type assignment from contact maps alone — not addressed by any source here.
- What re-establishes compartments in early G₁, and how fast? Open in this corpus.
- Whether loop positions are truly random per cell or drawn from a constrained set of sequence elements — the authors explicitly say their resolution cannot rule out the latter.

## Related

- [[chromatin-compartments]] · [[nagano-2013-nature]] · [[lupianez-2015-tad-disruption]] · [[3d-genome]]
