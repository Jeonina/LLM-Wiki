---
type: summary
title: "Ludwig & Bintu 2019 — Mapping chromatin modifications at the single cell level"
source: "[[00-Sources/papers/Mapping chromatin modifications at the single cell level]]"
source_quality: full
source_sha256: "11f24d89f7d41a762a1c5a810636d6d3998edff7a4e4754358f01eecff48fccb"
source_kind: paper
author: "Connor H. Ludwig, Lacramioara Bintu (corresponding)"
published: 2019-06-27
ingested: 2026-10-07
doi: "10.1242/dev.170217"
journal: "Development 146(12):dev170217"
tags: [review, single-cell-epigenomics, histone-modifications, DNA-methylation, scChIP-seq, scCUT&Tag, scChIC-seq, scChIL-seq, Co-ChIP, EpiTOF, scBS-seq, scRRBS, scMAB-seq, scAba-seq, scCGI-seq, scNOMe-seq, scNMT-seq, live-cell-reporters, 5hmC]
entities: []
concepts: ["[[chip-seq]]", "[[cut-and-tag]]", "[[chic-seq]]", "[[cut-and-run]]", "[[tn5-tagmentation]]", "[[bisulfite-sequencing]]", "[[scbs-seq]]", "[[5hmc]]", "[[nome-seq]]", "[[scnmt-seq]]", "[[sctrio-seq]]", "[[pacbio]]", "[[oxford-nanopore]]", "[[epigenetic-memory]]", "[[lineage-tracing]]", "[[joint-single-cell-multi-omics]]"]
topics: ["[[histone-modifications]]", "[[dna-methylation]]", "[[single-cell-multiomics]]"]
---

**Citation:** Ludwig & Bintu (2019) — *Mapping chromatin modifications at the single cell level* — *Development* 146:dev170217. [DOI](https://doi.org/10.1242/dev.170217)

# Ludwig 2019 — single-cell chromatin-modification review

> A 2019 snapshot of how histone and DNA modifications are measured in single cells, organised around a five-metric yardstick — **complexity, accuracy, throughput, efficiency and portability** — and spanning sequencing (scChIP-seq, scCUT&Tag, scChIC-seq, scChIL-seq; scRRBS, scBS-seq, scMAB-seq, scAba-seq, scCGI-seq), single-nucleosome and mass-cytometry methods (Co-ChIP, single-molecule decoding, EpiTOF), and **live-cell reporters**. Its central judgement: genome-wide single-cell methods are good at **classifying cell types**, while single-locus live reporters give **mechanism**; nothing yet maps many modifications at many loci over time.

## Key claims

- **Why ChIP doesn't scale down**: crosslinking artefacts, sonication needing hundreds of thousands to millions of cells, MNase over-digestion reducing reads, and low-affinity, lot-variable antibodies. Engineered readers and mintbodies are proposed alternatives (only anti-H3K9ac and anti-H4K20me1 mintbodies existed).
- **scChIP-seq (Drop-ChIP)** was the first multi-locus single-cell histone method: ~100 cells per assay and 500–10,000 unique reads per cell; it found three H3K4me2-associated states in serum-grown mESCs.
- **In situ methods (scChIL-seq, scCUT&Tag, scChIC-seq)** avoid chromatin solubilisation and are simpler, higher-throughput and cheaper, but Tn5-based ones **convolve accessibility with the mark**: bulk ChIP vs ChIL-seq correlations for H3K27me3 were r = 0.26–0.31; MNase-based scChIC-seq for H3K27me3 was less biased (r = 0.67).
- **Co-occurring marks.** Co-ChIP profiled 70 modification pairs (14 primary × 5 secondary) on single nucleosomes, finding H3K9me1 + H3K27ac at super-enhancers; single-molecule imaging plus on-slide sequencing reads combinations per nucleosome. Neither is single-cell genome-wide because nucleosomes are not grouped by cell. EpiTOF measures up to 60 targets per cell (global levels only) and showed immune-cell histone-modification variability rising with age.
- **Bisulfite limits**: 5mC and 5hmC are indistinguishable; conversion degrades ~90% of input DNA; complexity loss hampers mapping. scRRBS reaches a theoretical maximum ~10% of CpGs; scBS-seq (PBAT) gives fivefold more CpG information than scRRBS at equal depth. scM&T-seq can theoretically reach 48.4% of CpGs versus ~1% for RRBS-based scMT-seq and scTrio-seq.
- **Beyond 5mC.** scMAB-seq (M.SssI pre-methylation) maps 5fC/5caC and showed their dilution through zygotic replication; scAba-seq maps 5hmC (~10% detection efficiency) and revealed per-chromosome strand bias of 5hmC, allowing sister-cell identification; scCGI-seq (methylation-sensitive restriction) covers 72.7% of CGIs per cell.
- **Third-generation sequencing is single-molecule, not single-cell**: SMRT reliably detects 6mA but not 5mC/5hmC on genomic DNA (500× coverage needed to tell 5hmC from 5mC); nanopore 5mC/5hmC detection reached 80–97% single-pass on test oligos, with reads up to 2.2 Mb.
- **Joint assays**: scNOMe-seq and scCOOL-seq (GpC accessibility + CpG methylation); scM&T-seq, scMT-seq, scTrio-seq (methylation + RNA; scTrio-seq adds CNV at 10-Mb resolution); scNMT-seq (all three) found methylation and accessibility become more negatively correlated through differentiation.
- **Epigenetic lineage tracing** can exploit either stable maintenance (5mC via DNMT1; persistent H3K4me2 at smooth-muscle promoters in atherosclerotic cells) or deliberate non-maintenance (5hmC partitioned between sister cells).
- **Caution on reference data**: cultured cell types resemble each other epigenetically more than their tissues of origin, so using in vitro bulk data to interpret sparse single-cell reads from primary samples risks misclassification.

## Methods / evidence

Narrative review with a qualitative scoring table (Table 1) and complexity plots (number of modifications × number of loci × resolution). No new data; quantitative claims are drawn from the cited primary papers. Note: Crossref lists two authors (Ludwig, Bintu); the clipping header also names Allon Klein and Barbara Treutlein, apparently not as authors.

Weight: useful as a 2019 map and for its framing of metrics; superseded on specifics by later high-throughput and multi-target methods that postdate it, e.g. [[janssens-2023-scicut-tag]], [[gopalan-2022-multi-cut-and-tag]], [[bartosovic-2022-nano-cut-tag]]. (synthesis)

## Surprising or load-bearing bits

- **Tn5's accessibility bias is flagged here as a structural flaw** of tagmentation-based histone profiling, years before bulk benchmarks quantified the same effect against ENCODE. (synthesis)
- **5hmC's lack of maintenance becomes a feature** — strand-biased 5hmC identifies sister cells, the mirror image of using stable 5mC as a clonal mark.
- **"Single-molecule ≠ single-cell"** is a crisp distinction that still matters for long-read epigenomics claims.
- The review's own internal slip — bivalency is defined as H3K4me3 + H3K27me3, but the applications section cites H3K4me3 and H3K9me3 as the co-occurring opposing pair — should be read against the primary papers. (synthesis)

## Concepts touched

- [[chip-seq]], [[cut-and-tag]], [[chic-seq]], [[cut-and-run]] — the single-cell histone toolkit as of 2019 and its accessibility biases.
- [[tn5-tagmentation]] — accessibility bias of Tn5-based histone mapping.
- [[bisulfite-sequencing]] / [[scbs-seq]] — PBAT, scRRBS, coverage figures.
- [[5hmc]] — scAba-seq, strand bias, scMAB-seq for 5fC/5caC.
- [[nome-seq]] / [[scnmt-seq]] / [[sctrio-seq]] — joint methylation assays.
- [[epigenetic-memory]] / [[lineage-tracing]] — modification maintenance as a lineage record.

## Connections to other sources

- Primary methods reviewed and present in the wiki: [[rotem-2015-drop-chip]], [[kaya-okur-2019-cut-and-tag]], [[ku-2019-scchic-seq]], [[guo-2013-scrrbs]], [[smallwood-2014-natmethods]], [[clark-2017-scbs-seq-protocol]], [[luo-2017-snmc-seq]], [[mulqueen-2018-sci-met]], [[pott-2017-elife]], [[hou-2016-sctrio-seq]], [[clark-2018-scnmt-seq]], [[macaulay-2015-gt-seq]], [[flusberg-2010-smrt-methylation]].
- Background cited: [[bernstein-2006-bivalent-chromatin]], [[buenrostro-2015-nature]], [[cusanovich-2015-sciatac]], [[klemm-2019-chromatin-accessibility-review]], [[schubeler-2015-methylation-review]], [[roadmap-2015-111-epigenomes]].
- Later quantification of the CUT&Tag accessibility/recall issue: [[abbasova-2025-cut-tag-encode-benchmark]].
- Methylation as a clonal record, later demonstrated with engineered barcodes: [[li-2023-darlin]]; and exploited for lineage inference: [[scherer-2025-nature]].

## Open questions

- The authors' "ideal method" — many modifications, many loci, plus expression and structure, over time and space — remains open; their proposed route is multiplexed imaging (Oligopaints, MERFISH, seqFISH) as time-lapse endpoints.
- How much of single-cell histone signal is accessibility rather than the mark itself, and does MNase-based tethering fully escape it?
- Causality: programmable epigenome editing is proposed to move from correlation to cause.

## Related

- [[40-Topics/histone-modifications]] · [[40-Topics/dna-methylation]] · [[cut-and-tag]] · [[scnmt-seq]]
