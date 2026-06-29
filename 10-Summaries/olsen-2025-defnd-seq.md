---
type: summary
title: "Olsen et al. 2025 — DEFND-seq: scalable joint RNA + DNA from single nuclei"
source: "[[00-Sources/papers/Scalable co-sequencing of RNA and DNA from individual nuclei]]"
source_kind: paper
author: "Timothy R. Olsen, Pranay Talla, Romella K. Sagatelian, Julia Furnari, Jeffrey N. Bruce, Peter Canoll, Shan Zha, Peter A. Sims (corresponding)"
published: 2025-02-12
ingested: 2026-06-02
doi: "10.1038/s41592-024-02579-x"
journal: "Nature Methods"
tags: [single-cell-multiomics, DNA-RNA-coassay, nucleosome-depletion, 10x-genomics, CNV, SNV, glioblastoma, Sims-lab]
entities:
  - "[[20-Entities/peter-a-sims]]"
concepts:
  - "[[30-Concepts/defnd-seq]]"
  - "[[30-Concepts/joint-single-cell-multi-omics]]"
  - "[[30-Concepts/tn5-tagmentation]]"
  - "[[30-Concepts/structural-variants]]"
  - "[[30-Concepts/single-cell-variant-calling]]"
concepts_secondary:
  - "[[40-Topics/scdna-seq]]"
  - "[[30-Concepts/combinatorial-indexing]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[40-Topics/scdna-cancer-applications]]"
---

**Citation:** Olsen et al. (2025) — *Scalable co-sequencing of RNA and DNA from individual nuclei* — *Nature Methods*. [DOI](https://doi.org/10.1038/s41592-024-02579-x)

# Olsen et al. 2025 — DEFND-seq

> Thesis: Existing joint single-cell DNA+RNA co-assays (G&T-seq, DR-seq, SIDR, Simul-seq) are plate-based and low-throughput; sci-L3 is scalable but low-coverage and demonstrated only on cell lines. **DEFND-seq** (DNA and Expression Following Nucleosome Depletion) deplete nucleosomes with lithium diiodosalicylate (LAND), then runs nuclei through the *stock 10x Genomics Multiome (ATAC+GEX) kit* without modification — turning a chromatin-accessibility platform into a high-throughput genome+transcriptome co-assay, validated on cell lines and fresh/archival glioblastoma.

## Key claims

- Repurposing insight: feeding nucleosome-depleted nuclei into the 10x snATAC/Multiome kit yields whole-genome snDNA-seq instead of accessibility, because removing nucleosomes makes Tn5 tagment the genome uniformly rather than only open chromatin.
- LAND (lithium diiodosalicylate) beats crosslink+SDS (xSDS): LAND libraries are more complex, scale near-linearly to 125k reads/nucleus, have low TSS enrichment (uniform coverage), lowest coverage CV (~1.1), and yield full-length cDNA (xSDS truncates cDNA to ~786 bp).
- DEFND-seq coverage uniformity (100-kb CV 0.6; 1-Mb CV 0.38) is comparable to dedicated scDNA methods (PTA, MDA, PicoPlex) but at >200× fewer reads per cell — and none of those co-sequence RNA.
- Mixed-species (human U87 + mouse 3T3, 7,900 nuclei) gave 5.2% collision rate; RNA and DNA species-assignments are concordant per cell. Outperforms sci-L3 on unique transcripts and fragments at matched depth.
- Glioblastoma application links genotype to phenotype: focal *EGFR* amplification tracks with one transformed subclone, focal *PDGFRA* amplification with an OPC-like/proneural RNA cluster — recapitulating the classic TCGA PDGFRA–proneural association at single-cell resolution. All transformed clusters carry *MDM2* amplification.
- Detects somatic SNVs (e.g., *EGFR* p.D1082N, *MAP2K3* p.D24N) by combining DEFND-seq with patient germline WGS; works on >4-year cryopreserved tissue. Cross-platform SNV calling (Illumina ∩ Element Aviti) found a subclonal *PREX1* p.T1469M.

## Methods / evidence

LAND protocol adapted from Vitak et al.; all downstream steps use commercial 10x Multiome reagents. Library cost ~US$0.56/cell; scalable to ~40k nuclei/chip, >100k with SNP/hashtag demultiplexing. snDNA processed with a custom Cell-Ranger-mimicking pipeline (github.com/simslab/dna10x) + SnapATAC2 for CNV tiles; SNVs via GATK Mutect2.

## Surprising or load-bearing bits

- The whole method is "use the accessibility kit, but delete the chromatin first" — a reframing that gives broad accessibility (huge 10x install base) without new hardware. The euploid BJ-fibroblast benchmark (no aneuploidy, long doubling) is the clean noise control.
- Proliferating cells (flagged by RNA) have higher DNA coverage CV from ongoing replication — a built-in cell-cycle readout from the joint data.
- Multiplet rate is higher than 10x specs suggest (nuclear aggregation), partially correctable by SNP/RNA/DNA-based demultiplexing.

## Entities mentioned

- [[20-Entities/peter-a-sims]] — corresponding author (Columbia).
- Shendure, van Oudenaarden lineage of co-assays cited as predecessors.

## Concepts touched

- [[30-Concepts/defnd-seq]] — method defined here.
- [[30-Concepts/joint-single-cell-multi-omics]] — high-throughput droplet DNA+RNA entry.
- [[30-Concepts/tn5-tagmentation]] — uniform genomic tagmentation after nucleosome depletion.

## Connections to other sources

- Scales up the plate-based [[10-Summaries/macaulay-2015-gt-seq]] (G&T-seq) and [[10-Summaries/dey-2015-dr-seq]] (DR-seq) concept to droplets.
- Benchmarked against PTA ([[10-Summaries/gonzalez-pena-2021-pnas]]) for coverage; complementary to GoT ([[10-Summaries/nam-2019-got]]) which reads mutations only in mRNA.
- Cited as a key joint WGS+RNA method by both lineage-tracing reviews ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review]], [[10-Summaries/wang-2026-multimodal-lineage-computational]]).
- Compared to SDR-seq ([[10-Summaries/lindenhofer-2025-sdr-seq]]): DEFND-seq is whole-genome (sparse, high ADO) vs SDR-seq targeted (dense, low ADO).

## Open questions

- Residual chromatin structure may bias transposase accessibility and thus CNV/SNV calling — flagged as needing study.
- Genome-wide ADO is high; targeted amplification on the gDNA library could boost per-locus genotyping (the SDR-seq trade-off).

---
**Source:** [DOI](https://doi.org/10.1038/s41592-024-02579-x)
## Related

- [[40-Topics/single-cell-multiomics]] · [[30-Concepts/defnd-seq]] · [[30-Concepts/joint-single-cell-multi-omics]] · [[20-Entities/peter-a-sims]]
