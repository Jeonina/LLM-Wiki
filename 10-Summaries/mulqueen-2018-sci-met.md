---
type: summary
title: "Mulqueen et al. 2018 — Highly scalable generation of DNA methylation profiles in single cells (sci-MET)"
source: "[[00-Sources/papers/Highly scalable generation of DNA methylation profiles in single cells]]"
source_kind: paper
author: "Ryan M. Mulqueen, Dmitry Pokholok, Steven J. Norberg, Kristof A. Torkenczy, Andrew J. Fields, Duanchen Sun, John R. Sinnamon, Jay Shendure, Cole Trapnell, Brian J. O'Roak, Zheng Xia, Frank J. Steemers, Andrew C. Adey (corresponding)"
published: 2018-04-09
ingested: 2026-08-13
doi: "10.1038/nbt.4112"
journal: "Nature Biotechnology 36:428–431"
tags: [sci-MET, combinatorial-indexing, scWGBS, alignment-rate, cytosine-depleted-adaptors, collision-rate, NMF, cortex]
entities: ["[[andrew-adey]]", "[[jay-shendure]]", "[[cole-trapnell]]"]
concepts: ["[[combinatorial-indexing]]", "[[bisulfite-sequencing]]", "[[scbs-seq]]", "[[tn5-tagmentation]]", "[[doublet-detection]]", "[[dimensionality-reduction]]", "[[cell-type-annotation]]"]
topics: ["[[dna-methylation]]", "[[single-cell-multiomics]]", "[[scdna-seq]]"]
---

**Citation:** Mulqueen et al. (2018) — *Highly scalable generation of DNA methylation profiles in single cells* — *Nature Biotechnology* 36, 428–431. [DOI](https://doi.org/10.1038/nbt.4112)

# Mulqueen 2018 — sci-MET

> [[combinatorial-indexing|Combinatorial indexing]] applied to bisulfite sequencing, with one chemistry detail doing most of the work: **cytosine-depleted transposome adaptors**, which survive bisulfite treatment intact. The headline is not cell count but **alignment rate — 68 ± 8%, approaching bulk** — against the 25 ± 20% typical of one-cell-per-well scWGBS. Same information for a quarter of the sequencing cost.

## Key claims

- **Cytosine-depleted adaptors are what makes tagmentation compatible with bisulfite.** Standard Tn5 adaptors contain cytosines that bisulfite would convert, destroying the index. Depleting them lets the first index be installed by transposition into intact nuclei, before any conversion.
- **The second adaptor goes on after conversion, by random priming** — five rounds, as in classic [[clark-2017-scbs-seq-protocol|scBS-seq]]/PBAT. So sci-MET is a hybrid: indexed tagmentation front end, PBAT back end.
- **Alignment rate is the real gain: 68 ± 8%** in the three-cell-line experiment (59.9 ± 11.9% for mouse cortex). Prior scWGBS protocols ran at 25 ± 20%; the one prior study exceeding 50% did so by brute force with one well per cell for >6,000 cells. The authors attribute the improvement to transposase-based adaptor incorporation.
- **Nucleosome depletion method determines the collision rate.** Lithium-3,5-diiodosalicylate (LAND) gave a 22% barcode collision rate — unusable. Crosslinking + SDS (xSDS) gave **7.3%**, in line with other sci- protocols. Collision rate is tunable by nuclei per well.
- **3,282 single-cell libraries total**, across a GM12878-only 96 × 22 run (708 cells, 33.5% efficiency), a 40 × 22 three-cell-line run (691 cells, 78.5% efficiency), and a 96 × 10 mouse cortex run (606 cells). The `N × D` notation (wells in stage two × pre-indexed nuclei per well) is the throughput algebra.
- **Coverage per cell is low and that is the design.** Mean 403,265 unique aligned reads per cell in the best run; mappable CpG coverage 0.05–7.0% (mean 1.1 ± 0.9%). The authors state plainly that sci-MET produces *lower* per-cell coverage than other methods but sufficient coverage for cell-type discrimination — the intended goal of low-coverage, high-cell-count strategies.
- **Libraries were not near saturation**, so both deeper sequencing and more linear-amplification rounds should raise coverage.
- **Cell-type discrimination validated three ways.** NMF + tSNE over Ensembl Regulatory Build autosomal loci separated GM12878 / primary fibroblast / HEK293; each cluster's top-two correlations with public WGBS were the matching cell type. In mouse cortex, combining CH methylation over 100-kb windows with CG methylation over regulatory regions separated excitatory from inhibitory neurons by enrichment at published cortical DMRs.
- **Crosslinking did not impair bisulfite conversion**, judged by the appropriately low non-CG methylation rates — a concern the authors raise and dismiss with data.

## Methods / evidence

Three experiments (cell line, species-mix collision test, mouse cortex), 3,282 libraries. Validation is by correlation to published bulk WGBS and by enrichment at DMRs from prior snmC-seq work — i.e. the cell-type calls are anchored to [[luo-2017-snmc-seq]]'s reference DMRs rather than to an independent measurement in the same cells.

Weight: this is a Brief Communication; the biology is a demonstration, not a discovery. The methodological numbers (alignment rate, collision rate, efficiency) are the substance.

## Surprising or load-bearing bits

- **Alignment rate, not cell count, is the scaling bottleneck for scWGBS.** At 25% alignment you pay for four reads to get one. Fixing that is a 4× cost reduction that compounds with every other throughput gain — a less glamorous lever than cell count and a more consequential one.
- **The LAND-vs-xSDS collision result (22% vs 7.3%) is a reusable warning**: nucleosome depletion chemistry, an apparently upstream sample-prep choice, silently sets the doublet rate of a combinatorial-indexing experiment.
- **Efficiency varied 33.5% → 78.5% between runs** with no chemistry change noted — the protocol was not yet stable, which is what [[nichols-2022-scimet-v2|sciMETv2]] later addressed.
- **1.1% mean CpG coverage is an order of magnitude below [[clark-2017-scbs-seq-protocol|scBS-seq]]'s ~50%.** The two methods are not competing on the same axis: scBS-seq answers "what is this cell's methylome"; sci-MET answers "how many kinds of cell are here."
- Combining CH-over-100-kb-bins with CG-over-regulatory-regions as *two matrices merged through NMF* is an early instance of within-modality multi-feature integration, before that became standard practice.

## Entities mentioned

- [[andrew-adey]] — corresponding author; combinatorial-indexing epigenomics.
- [[jay-shendure]] — coauthor; originator of the sci- combinatorial indexing family.
- [[cole-trapnell]] — coauthor.

## Concepts touched

- [[combinatorial-indexing]] — extended to bisulfite chemistry via cytosine-depleted adaptors.
- [[scbs-seq]] — sci-MET's back end is PBAT random priming, inherited from this lineage.
- [[doublet-detection]] — collision rate as the combinatorial-indexing analogue of doublets.

## Connections to other sources

- Direct successor: [[nichols-2022-scimet-v2]].
- The indexing family it belongs to: [[cusanovich-2015-sciatac]] (sci-ATAC), [[jay-shendure]]'s sci- line; [[janssens-2023-scicut-tag]] applies the same logic to CUT&Tag.
- The scWGBS lineage it improves on: [[smallwood-2014-natmethods]], [[clark-2017-scbs-seq-protocol]], [[guo-2013-scrrbs]], [[guo-2015-scrrbs-protocol]].
- Plate-based contemporary with higher per-cell coverage: [[luo-2017-snmc-seq]], [[luo-2018-snmc-seq2]] — and the source of the DMRs used here for annotation.
- Droplet alternative that targets the same throughput axis: [[zhang-2023-drop-bs]].
- Analysis tools built for exactly this sparsity regime: [[kapourani-2021-scmet]], [[angermueller-2017-genomebiol]], [[desouza-2020-epiclomal]], [[kremer-2024-methscan]].

## Open questions

- **Efficiency instability (33.5% vs 78.5%) is unexplained** in the text.
- Whether the low per-cell coverage supports anything beyond cell typing — e.g. DMR discovery de novo rather than DMR *matching* — is not tested.
- The xSDS crosslinking step is incompatible with several downstream co-assays; whether sci-MET can be multiplexed with transcriptome or accessibility readouts is unaddressed.

## Related

- [[nichols-2022-scimet-v2]] · [[combinatorial-indexing]] · [[zhang-2023-drop-bs]] · [[40-Topics/dna-methylation]]
