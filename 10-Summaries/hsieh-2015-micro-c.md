---
type: summary
title: "Hsieh et al. 2015 — Mapping Nucleosome Resolution Chromosome Folding in Yeast by Micro-C"
source: "[[00-Sources/papers/Mapping Nucleosome Resolution Chromosome Folding in Yeast by Micro-C.pdf]]"
source_kind: paper
author: "Tsung-Han S. Hsieh, Assaf Weiner, Bryan Lajoie, Job Dekker, Nir Friedman, Oliver J. Rando"
published: 2015-07
ingested: 2026-10-07
updated: 2026-10-07
doi: "10.1016/j.cell.2015.05.048"
journal: "Cell 162(1):108–119"
tags: [Micro-C, MNase, Hi-C, nucleosome-resolution, chromosomal-interaction-domains, CID, gene-compaction, yeast, 30-nm-fiber, tetranucleosome, RSC, cohesin-loader, Mediator, Rtt109, Ssu72, H4-tail]
entities: ["[[job-dekker]]"]
concepts: ["[[micro-c]]", "[[topologically-associating-domain]]", "[[chromatin-loop]]", "[[chromatin-compartments]]", "[[lamina-associated-domains]]", "[[chip-seq]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Hsieh et al. (2015) — *Mapping Nucleosome Resolution Chromosome Folding in Yeast by Micro-C* — *Cell* 162(1):108–119. [DOI](https://doi.org/10.1016/j.cell.2015.05.048)

# Hsieh 2015 — Micro-C

> Restriction-enzyme Hi-C leaves a "blind spot" between ChIP-seq/MNase-seq (~1–150 bp) and Hi-C (>1–4 kb), the scale of 30-nm fibres and yeast gene loops. **Micro-C** fills it by digesting crosslinked chromatin to **mononucleosomes with micrococcal nuclease** before proximity ligation, giving a nucleosome-by-nucleosome contact map of budding yeast (66,360 × 66,360 nucleosomes). The maps show **chromosomal interaction domains (CIDs)** of one to five genes, bounded at **promoters** of highly transcribed genes. **Gene compaction is anticorrelated with transcription** and is shaped by RSC, cohesin loading, Mediator, Rtt109 and the H4 tail. The authors find **no periodic 30-nm fibre**, but the data fit a sparse tri- or tetranucleosome motif. Their model is "gene crumples" (globules), not gene loops. (Re-ingested 2026-10-07 from the full PDF; the earlier clipping lacked the abstract and most Results.)

## Key claims

- **Method.** Yeast fixed with formaldehyde → MNase to >95% mononucleosomes → T4 polymerase end repair with biotin-dCTP/dATP fill-in → dilute ligation → exonuclease III removal of unligated biotin ends → ~250–350 bp gel selection → streptavidin pulldown → paired-end sequencing. Controls: no ligation, no crosslinking, and an *S. cerevisiae* × *K. lactis* chromatin mix before ligation, which showed **~10% spurious ligations** at the dilution used.
- **Complements Hi-C rather than replacing it.** Micro-C has much higher resolution than the earlier low-resolution yeast map, but captures long-range contacts poorly. Short-chromosome preference and weak telomere–telomere signal are recovered; centromere–centromere clustering is not.
- **CIDs in yeast.** Domains of ~4–50 nucleosomes appear with nested architecture. They are reproducible across 21 biological replicates, three wild-type backgrounds and *K. lactis* (unpublished), and are robust to MNase digestion level. CIDs range from zero to eight genes, with 45% spanning two or more. At ~2–10 kb they are one to two orders of magnitude smaller than mammalian TADs (~100 kb–1 Mb), so **domain size is conserved in gene number, not base pairs**. Yeast CIDs had not been seen before (Duan 2010); they had been seen in *Caulobacter*, flies and mammals but not in *Arabidopsis*.
- **Boundaries are promoters.** About 40% of boundary nucleosomes are +1 nucleosomes, against ~7% genome-wide. Boundaries are enriched for 5′ marks (H3K18ac highest, H3K4me3) and replication-independent H3 replacement. Strong boundaries sit upstream of more highly transcribed genes (Pol2 ChIP) and carry high RSC (Sth1) and cohesin-loader Scc2 binding.
- **Compaction vs. transcription.** An occupancy- and length-corrected gene compaction score is **anticorrelated with transcription (r = −0.56)**, but transcription explains only **31% of the variance**. Compaction also correlates with the repression mark H2AS129ph. In diamide stress (1.5 mM, 30 min), induced genes unfold and repressed ribosomal protein genes (RPGs) compact. Thiolutin (Pol II inhibition) makes highly transcribed genes, mainly RPGs, more compact (p < 6.4 × 10⁻⁵⁵).
- **Genetics of compaction.** Data from 700 deletion mutants suggested unusually compact genes are repressed by HDACs (Cyc8/Tup1, Sum1/Hst1), histone turnover factors (Rtt109, Asf1) and Mediator. The authors screened 24 mutants at low depth and sequenced 14 deeply:
  - *ssu72-2* (the "gene looping" CTD phosphatase): modest but significant global loss of compaction (KS p < 1.2 × 10⁻⁸).
  - *med1Δ*, *rtt109Δ* and *rpd3Δ*: decompaction. These effects are **not explained by transcription changes**; correlations with mRNA change are 0.17, 0.03 and −0.006.
  - RSC ts mutants (*sth1-2*, *rsc8-21*) and *scc2-4*: increased compaction, especially of RPGs, mirroring Pol II inhibition. *rnh201Δ* has only subtle gene-specific effects.
  - Histone mutants: partial deletion of the H4 N-terminal tail strongly reduces folding signal. H4K16Q has no global effect, which fits a genome that is mostly H4K16-acetylated already. H4R23A, which disrupts tetranucleosome stacking in vitro, keeps contacts up to the tetranucleosome scale but loses contacts beyond it.
- **No regular 30-nm fibre; tri-/tetranucleosome motif instead.** Contact decay shows **no periodicity**. N/N+2 pairs are nearly as common as N/N+1, especially after excluding IN–IN reads, which broadly supports two-start (zig-zag) models. But the excess N+4/N+6 expected from an extended zig-zag fibre is absent. This fits sparse, unstacked tetranucleosomes in vivo, or a technical limit of short-range formaldehyde crosslinking; the authors leave both open.
- **Gene crumples, not gene loops.** Most genes show contacts throughout the gene body rather than preferential +1 nucleosome to 3′-end contacts. Compaction also falls with transcription, the opposite of what reported gene loops predict.

## Methods / evidence

Mapping: 50-bp mates mapped separately to sacCer3 with bowtie2; the shortest fragment kept for multi-mapping pairs; duplicates removed; pairs assigned to the 66,360 nucleosomes for some analyses. IN–IN pairs, which are enriched for undigested dinucleosomes, are dropped except in Fig. 1C/S1. Regions with >10× the windowed interaction count (1.3% of the genome: rDNA, Ty elements) are masked. Counts are normalised to total unique fragments; occupancy correction had minimal effect. Boundary score = interactions of 500–10,000 bp crossing a position, with boundaries at local minima. Compaction score = log ratio of long-range (>300 bp) interactions to a k-nearest-neighbour Gaussian expectation given gene length and occupancy, using <300 bp counts as the occupancy proxy. Data: GEO GSE68016.

Weight: a single-organism methods paper with strong replication (20–21 wild-type replicates) and a genetic screen. Mutant effects are correlational for gene sets and partly confounded by transcription, which the authors test directly. The 30-nm conclusion is hedged by crosslinker reach.

## Surprising or load-bearing bits

- **Boundaries over secondary structure.** The authors speculate that boundary establishment drives chromosome folding, while folding inside each domain does not follow any regular secondary structure. Their perspective is a hierarchy: 10-nm beads on a string, then gene crumples separated by high-turnover promoters.
- **Mediator links to the mammalian cohesin story.** Mediator recruits cohesin in mouse ES cells, so Mediator's role in yeast compaction suggests domain compaction may be conserved. Rtt109 (H3K56ac, histone turnover) affecting global compaction is the newer finding.
- **Transcription explains only a third of compaction.** The 0.17/0.03/−0.006 mutant–mRNA correlations show that chromatin regulators shape folding beyond what transcription changes would predict.
- **MNase fragmentation removes restriction-site resolution variability**, which is why later mammalian Micro-C resolves fine loops and promoter contacts. (synthesis)

## Concepts touched

- [[micro-c]] — the founding method paper.
- [[topologically-associating-domain]] — yeast CIDs as gene-scaled TAD analogues; nested architecture; promoter boundaries.
- [[chromatin-loop]] — gene loops tested and not supported as the main yeast structure.
- [[chip-seq]] — histone-mark, Pol2, Sth1 and Scc2 ChIP data used to characterise boundaries.
- [[chromatin-compartments]] / [[lamina-associated-domains]] — higher levels listed in the framing; not measured.

## Connections to other sources

- Restriction-enzyme predecessors: [[lieberman-aiden-2009-hic]] (protocol basis), [[dixon-2012-tads]] (mammalian TADs it compares to).
- Same-lab (Dekker) and related 3D work: [[naumova-2013-mitotic-chromosome]].
- Single-molecule nucleosome-scale views that complement contact maps: [[abdulhay-2020-samosa]], [[andrewb-2020-science]] (Fiber-seq). (synthesis)
- Single-cell 3D genome context where Micro-C is mentioned: [[hong-2025-sc3d-genome-review]], [[park-2026-mintsc]].
- Pipeline compatibility: [[servant-2015-hicpro]].

## Open questions

- Is the missing N+4/N+6 signal biological (sparse tetranucleosomes) or technical (formaldehyde reach)? The proposed tests are alternative crosslinkers, multi-nucleosome ligation products and Micro-C on defined 30-nm templates.
- Micro-C misses centromere clustering and other long-range yeast contacts; multiscale views need Hi-C as well.
- Does gene-number scaling of domains hold in organisms such as *Arabidopsis*, where CIDs were not previously seen?
- What explains the ~69% of compaction variance not accounted for by transcription?

## Related

- [[micro-c]] · [[dixon-2012-tads]] · [[lieberman-aiden-2009-hic]] · [[topologically-associating-domain]] · [[40-Topics/3d-genome]]
