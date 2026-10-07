---
type: summary
title: "Arrastia et al. 2022 — Single-cell measurement of higher-order 3D genome organization with scSPRITE"
source: "[[00-Sources/papers/Single-cell measurement of higher-order 3D genome organization with scSPRITE]]"
source_quality: full
source_sha256: "ba5a51e30379154c7b5ec39cccbe3943f0e0d2e6e7a6bd2e1dd47ad4c064efaa"
source_kind: paper
author: "Mary V. Arrastia, Joanna W. Jachowicz, Noah Ollikainen, Matthew S. Curtis, Charlotte Lai, Sofia A. Quinodoz, David A. Selck, Rustem F. Ismagilov, Mitchell Guttman (corresponding)"
published: 2021-08-23
ingested: 2026-10-07
doi: "10.1038/s41587-021-00998-1"
journal: "Nature Biotechnology 40:64–73"
tags: [scSPRITE, SPRITE, split-pool-barcoding, multi-way-contacts, single-cell-3D-genome, TAD-heterogeneity, nuclear-bodies, nucleolus, nuclear-speckles, chromocenters, mESC, Nanog]
entities: []
concepts: ["[[sc-sprite]]", "[[multi-way-chromatin-interaction]]", "[[single-cell-hi-c]]", "[[topologically-associating-domain]]", "[[chromatin-compartments]]", "[[chromatin-loop]]", "[[combinatorial-indexing]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Arrastia et al. (2022) — *Single-cell measurement of higher-order 3D genome organization with scSPRITE* — *Nature Biotechnology* 40:64–73. [DOI](https://doi.org/10.1038/s41587-021-00998-1)

# Arrastia 2022 — scSPRITE

> Pairwise proximity ligation has a hard ceiling in a single cell: each DNA fragment can be ligated once per allele, so a four-fragment complex yields at most two pairwise contacts instead of the six it really contains. scSPRITE avoids ligation entirely. It runs **two stacked split-and-pool barcoding stages** — three rounds inside intact nuclei to mark *which cell* a fragment came from, then (after sonication releases crosslinked complexes onto beads) three more rounds to mark *which spatial cluster* it sat in. Every cluster of n reads contributes n-choose-2 contacts. On 1,000 mouse ES cells this gives an average of ~35 million pairwise contacts per cell, against ~375,000 for the scHi-C comparator. With that depth, nuclear-body hubs become visible in single cells, as do TADs. The TADs are present in most cells but individually variable, and some loci switch between mutually exclusive alternative structures.

## Key claims

- **Two-stage barcoding separates cell identity from spatial co-occurrence.** Reads sharing all six tags belong to one spatial cluster; reads sharing the first three (DPM, odd, even) belong to one nucleus. Three rounds of 96 give 96³ = 884,736 combinations, a 590-fold excess over the 1,500 nuclei used, which means fewer than one expected full-barcode collision.
- **Collision rate is measured empirically.** In a human (HEK293T) / mouse (mESC) mixing experiment only **3.4%** of cell barcodes contained reads from both species. The authors extrapolate a **~10%** total collision rate, since same-species collisions are invisible to this test.
- **Ensemble scSPRITE reproduces bulk SPRITE**: Pearson r = 0.92 genome-wide at 1 Mb, 0.97 on chr2 at 200 kb, and 0.95 at 40 kb across chr6:48–54 Mb. Ensemble TAD insulation scores correlate with Hi-C at r = 0.70.
- **Contacts per cell rise roughly 100-fold even though reads per cell fall about 10-fold** (scSPRITE vs. the scHi-C dataset in ref. 16): **34,992,080 vs. 375,470** pairwise contacts per cell from **83,318 vs. 751,172** reads per cell. Coverage is uniform across all 1-Mb bins in virtually all cells and across all 100-kb bins in more than 80% of cells.
- **Inter-chromosomal contacts are about 9× more abundant**: 54% of contacts per cell for scSPRITE against 6% for scHi-C. This is what lets the method see hubs organised around nuclear bodies.
- **Chromosome territories and compartments are near-universal per cell.** Territories are present in 95% of cells (fewer than 50 cells lack them, which the authors suggest may be mitotic). Detection scores were computed for 224 genome-wide A/B compartment-switch regions, and compartments are detectable in ~95% of cells. Compartment regions vary more between cells than territories do (mean score 0.03 vs. 0.08).
- **Nuclear-body hubs in single cells**:
  - *Nucleolar (NOR) contacts*: each pair is present in 38% of cells on average. Contact frequencies agree with DNA FISH plus nucleolin immunostaining at R² = 0.88.
  - *Speckle contacts*: present in 34% of cells on average.
  - *Pericentromeric (chromocenter) contacts*: present in 49% of cells on average. chr11 PCH pairs most often (80% of cells) and chr14 least often (30%).
  - The ensemble scHi-C data could not detect centromere-proximal or nucleolar contacts at all. It did detect speckle interactions, but its single-cell maps did not.
- **TADs exist in single cells but are heterogeneous.** 95% of cells have a positive average TAD score across all 2,602 ensemble TAD boundary regions. Looked at TAD by TAD, though, most are highly variable (65% of cells score <0 for the average TAD), and the variable TADs cluster in shared genomic regions.
- **Mutually exclusive structural states.** At chr4:38.5–43.6 Mb, one group of cells forms an alternative TAD that spans an ensemble A/B compartment boundary (199 of 379 covered cells), and in those cells the compartment calls themselves differ. The difference is not explained by cell cycle.
- **Long-range vs. short-range enhancer contacts are anti-correlated.**
  - *Nanog*: among 308 covered cells, 159 have the contact with the *Phc1* super-enhancer 300 kb away.
  - *Tbx3*: among 301 covered cells, 152 have the PcG-associated contact with *Lhx5* 760 kb away.
  - Cells with the long-range contact show short-range contacts about 3× less often (P < 0.001), and the long-range contacts cross an ensemble TAD border.
  - The two states occur at similar frequencies. Read depth and cell-cycle phase do not explain the split (KS test, n.s.).

## Methods / evidence

Cells are crosslinked with DSG plus formaldehyde, and DNA is digested in nuclei with HpyCH4V, a 4-bp blunt cutter that gives an average fragment of 823 bp. Nuclei are dA-tailed and go through three rounds of in-nucleus ligation barcoding, then are filtered through a 10-µm mesh. 1,500 nuclei are sonicated, the complexes are coupled to NHS beads, and three more rounds of bead split-pool barcoding follow. The authors sequenced 1.27 billion reads, of which 49.8% carried all six tags. Alignment used STAR to mm9 with RepeatMasker and mappability filtering. The 4,000 largest cell barcodes were taken; the top 3.4% were removed as likely doublets, and the top 1,000 by cluster count were kept. Clusters with more than 10,000 reads were dropped. Per-structure "detection scores" (observed intra-structure minus inter-structure contact fraction on binary matrices, normalised against 1,000 coordinate-shuffled structures) quantify whether each cell contains a given structure. Group differences are tested by bootstrap plus Welch's t-test. Cell-cycle phase was assigned with the ref. 16 parameters.

Weight: strong as a proof of principle, and its claims are internally controlled (mixing experiment, FISH concordance, read-depth and cell-cycle checks). But it covers one cell type (2i/LIF mESC, with a likely chr8 trisomy shown by ~33% excess reads) in one experiment of ~1,500 cells. The scHi-C comparison uses a single published dataset (ref. 16), so the contact-count advantage is a cross-study comparison, not a same-sample one. Only about one-third of cells have coverage at any given 40-kb locus pair, so locus-level heterogeneity calls rest on roughly 300 cells.

## Surprising or load-bearing bits

- **The "contacts per cell" advantage is partly definitional.** A cluster of n reads is counted as n(n−1)/2 pairwise contacts. Large clusters therefore inflate contact counts without adding independent spatial information, which is why clusters over 10,000 reads are discarded and downweighting by 2/n is used for ensemble TAD maps. Contact counts from SPRITE and ligation methods are not like-for-like units. (synthesis)
- **TAD heterogeneity is regional, not random.** Variable TADs co-localise in shared genomic regions, and in one such region an alternative TAD rewires local compartment identity. The ensemble TAD is then an average of distinct conformations, not a weak version of one. (synthesis)
- **Enhancer–promoter "choice" at *Nanog* and *Tbx3*.** Long- and short-range contacts appear to be competing alternatives in individual cells rather than simultaneous, and the two states are seen at about equal frequency even in 2i ground-state culture.
- **A small A-compartment detection bias**: 45% of observed reads fall in A compartments against 39% expected.
- **Throughput scales by the arithmetic of barcode rounds.** The recommended excess is 10–100× barcode combinations over cells. For example, 10,000 cells with 100,000 combinations gives fewer than one expected collision. No specialised equipment is required, which the authors frame as accessibility for "any molecular biology laboratory".

## Concepts touched

- [[sc-sprite]] — this is the primary method paper. Note that DNA is fragmented by restriction digestion (HpyCH4V), and sonication serves to release crosslinked complexes before bead barcoding.
- [[multi-way-chromatin-interaction]] — the quadratic-growth argument for why multi-way capture beats pairwise ligation in a single cell.
- [[single-cell-hi-c]] — the direct comparator; its limits on inter-chromosomal and nuclear-body contacts are quantified.
- [[topologically-associating-domain]] — evidence that TADs are present in most single cells but individually variable, with mutually exclusive alternative states.
- [[chromatin-compartments]] — compartments detected per cell; compartment identity can shift with alternative TAD states.
- [[chromatin-loop]] — enhancer–promoter contacts at *Nanog*/*Tbx3* behave as either/or states.
- [[combinatorial-indexing]] — split-pool cell barcoding performed in nuclei, followed by a second split-pool layer on beads.

## Connections to other sources

- Listed among the sc3DG technologies benchmarked by [[jiang-2026-stark-scnucleome]], which reports scSPRITE as having the highest average contacts per cell. That is consistent with this paper's own contacts-per-cell comparison.
- Multi-way assay context and corroboration: [[park-2026-mintsc]] uses SPRITE enrichment to validate inferred multi-way cliques.
- Single-cell TAD variability echoes the sliding/present-absent boundaries inferred by [[zhang-2022-higashi]] and the boundary fluctuation summarised in [[hong-2025-sc3d-genome-review]].
- Ligation-based single-cell 3D genome lineage: [[nagano-2013-nature]], [[ramani-2017-scihi-c]]. The bulk structures it recovers come from [[lieberman-aiden-2009-hic]] (compartments) and [[dixon-2012-tads]] (TADs, also mESC).
- Territories absent in some cells "might reflect … mitotic chromosomes", consistent with the metaphase loss of compartments and TADs in [[naumova-2013-mitotic-chromosome]].

## Open questions

- Whether the cell-to-cell TAD and enhancer-contact heterogeneity has functional consequences (for example on *Nanog* expression) is explicitly left open. No paired transcriptome was measured.
- Generalisation to tissues and tumours is proposed but not shown. All data are from one mESC line.
- How should contact counts be normalised across SPRITE-type and ligation-type methods for fair benchmarking, given that large clusters dominate n-choose-2 counts? (synthesis)
- The ~10% estimated total collision rate is only partly addressed by removing the top 3.4% of barcodes. Residual same-species doublets could add apparent "heterogeneity". (synthesis)

## Related

- [[sc-sprite]] · [[multi-way-chromatin-interaction]] · [[single-cell-hi-c]] · [[40-Topics/3d-genome]]
