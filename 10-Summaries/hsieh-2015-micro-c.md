---
type: summary
title: "Hsieh et al. 2015 — Mapping Nucleosome Resolution Chromosome Folding in Yeast by Micro-C"
source: "[[00-Sources/papers/Mapping Nucleosome Resolution Chromosome Folding in Yeast by Micro-C]]"
source_kind: paper
author: "Tsung-Han S. Hsieh, Assaf Weiner, Bryan Lajoie, Job Dekker, Nir Friedman, Oliver J. Rando"
published: 2015-07
ingested: 2026-10-07
doi: "10.1016/j.cell.2015.05.048"
journal: "Cell 162(1):108–119"
tags: [Micro-C, MNase, Hi-C, nucleosome-resolution, chromosomal-interaction-domains, CID, yeast, 30-nm-fiber, RSC, cohesin-loader, Mediator, Rtt109]
entities: ["[[job-dekker]]"]
concepts: ["[[topologically-associating-domain]]", "[[chromatin-loop]]", "[[chromatin-compartments]]", "[[lamina-associated-domains]]", "[[chip-seq]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Hsieh et al. (2015) — *Mapping Nucleosome Resolution Chromosome Folding in Yeast by Micro-C* — *Cell* 162(1):108–119. [DOI](https://doi.org/10.1016/j.cell.2015.05.048)

# Hsieh 2015 — Micro-C

> Restriction-enzyme Hi-C leaves a "blind spot" between ~150 bp (ChIP-seq/MNase-seq) and ~1–4 kb (Hi-C fragment sizes). **Micro-C** fills it by fragmenting crosslinked chromatin into **mononucleosomes with micrococcal nuclease** before proximity ligation, giving a nucleosome-by-nucleosome contact map of budding yeast (66,360 × 66,360 nucleosomes). The maps reveal **chromosomal interaction domains (CIDs)** of roughly one to five genes, bounded mostly at promoters of highly transcribed genes / nucleosome-depleted regions, and **no periodic 30-nm-fibre signature** in vivo — leading to a "gene crumple" model in which boundaries, not regular secondary structure, organise the fibre.

## Key claims

- **Method.** Formaldehyde-fixed yeast → MNase to >95% mononucleosomes → end repair with biotinylated nucleotides → dilute ligation → exonuclease III removal of unligated biotin ends → ~250–350 bp gel selection → streptavidin pulldown → paired-end sequencing.
- **Spurious ligation measured**: mixing crosslinked chromatin from *S. cerevisiae* and *K. lactis* before ligation shows ~10% of interactions are spurious at the dilution used; unligated and uncrosslinked controls also run.
- **Complementary, not a replacement, for Hi-C**: Micro-C recovers short-chromosome preference and weak telomere–telomere contacts, but not centromere–centromere interactions; it is best for short-range fibre folding.
- **Yeast has self-associating domains.** "Boxes" of ~4–50 nucleosomes, nested, consistent across 21 biological replicates and three wild-type backgrounds (and in *K. lactis*, unpublished). CIDs span zero to eight genes, 45% encompass two or more genes; at ~2–10 kb they are one to two orders of magnitude smaller than mammalian TADs (~100 kb–1 Mb), so domain size appears conserved **in genes, not base pairs**.
- **Boundaries** are enriched at NDRs of promoters, especially highly transcribed genes and regions of rapid histone turnover, typically bound by RSC and the cohesin-loading complex; Micro-C's resolution localises boundary activity of highly transcribed genes specifically to their promoters.
- **Mutants (14 analysed).** Confirm roles for RSC and Ssu72; *med1Δ* and *rtt109Δ* loosen chromosome structure (Mediator; H3K56 acetyltransferase Rtt109), while *sth1*ᵗˢ and *scc2*ᵗˢ at restrictive temperature increase gene compaction; the H4 N-terminal tail also matters, and H4R23A causes subtle relaxation.
- **No regular 30-nm fibre.** No periodicity in short-range contacts; N/N+1 and N/N+2 products are similarly abundant (broadly supporting two-start models) without the excess of N+4/N+6 expected from a regular zig-zag fibre — consistent with sparse tri-/tetranucleosome motifs, though the authors note formaldehyde's short reach could hide such contacts.

## Methods / evidence

bowtie2 alignment to sacCer3 (50-bp mates mapped separately); duplicate pairs removed; IN–IN read pairs excluded (enriched for undigested dinucleosomes); 1.3% of genome (rDNA, Ty elements) masked as outliers; normalisation to total unique fragments (occupancy corrections had minimal effect). Boundary score = count of 500–10,000-bp interactions crossing a position, boundaries at local minima. Gene compaction score = log ratio of observed long-range (>300 bp) interactions to a kNN-Gaussian expectation given gene length and nucleosome occupancy. Data GEO GSE68016.

Weight: a single-organism (yeast) methods paper with many replicates and mutants; the clipping omits the highlights, abstract and several results sections (e.g., detailed mutant figures), so mutant effects here are taken from the Introduction and Discussion. The 30-nm conclusion is explicitly hedged by crosslinker limitations.

## Surprising or load-bearing bits

- **Boundaries over secondary structure**: the authors speculate that establishing boundaries is the driver of chromosome folding, with intra-domain folding not conforming to any regular secondary structure. (stated as speculation in the source)
- **Scaling by gene number** reconciles ~5-kb yeast CIDs with ~0.5-Mb mammalian TADs — a cross-species framing worth remembering when comparing domain calls across organisms.
- **Micro-C's MNase fragmentation** removes restriction-site-dependent resolution variability — the reason later mammalian Micro-C maps resolve fine loops and promoter contacts. (synthesis)

## Concepts touched

- [[topologically-associating-domain]] — yeast CIDs as gene-scaled TAD analogues; nested architecture.
- [[chromatin-loop]] — gene loops discussed but domains described as crumples/globules rather than loops.
- [[chromatin-compartments]] / [[lamina-associated-domains]] — higher levels of organisation listed in the framing; not measured here.

## Connections to other sources

- Restriction-enzyme predecessors: [[lieberman-aiden-2009-hic]], [[dixon-2012-tads]] (mammalian TADs it compares to).
- Same-lab (Dekker) and related 3D work: [[naumova-2013-mitotic-chromosome]].
- Single-molecule nucleosome-scale chromatin views complementing contact maps: [[abdulhay-2020-samosa]], [[andrewb-2020-science]] (Fiber-seq). (synthesis)
- Single-cell 3D genome context where Micro-C is mentioned: [[hong-2025-sc3d-genome-review]], [[park-2026-mintsc]].
- Pipeline compatibility: [[servant-2015-hicpro]].

## Open questions

- Is the missing N+4/N+6 periodicity biological (sparse tetranucleosomes) or technical (formaldehyde reach)? Alternative crosslinkers or multi-nucleosome ligation products are proposed tests.
- Micro-C misses centromere clustering and other long-range yeast contacts — combining with Hi-C needed for multiscale views.
- Whether gene-number scaling of domains holds broadly (e.g., *Arabidopsis*, where CIDs were not previously seen) is untested.

## Related

- [[dixon-2012-tads]] · [[lieberman-aiden-2009-hic]] · [[topologically-associating-domain]] · [[40-Topics/3d-genome]]
