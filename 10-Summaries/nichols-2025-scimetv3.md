---
type: summary
title: "Nichols et al. 2025 — Atlas-scale single-cell DNA methylation profiling with sciMETv3"
source: "[[00-Sources/papers/Atlas-scale single-cell DNA methylation profiling with sciMETv3]]"
source_quality: full
source_sha256: "38ee02aef074cc93d7bfcaec3d340d828b75be77755c9581d82827f333fcc173"
source_kind: paper
author: "Ruth V. Nichols, Lauren E. Rylaarsdam, Brendan L. O'Connell, Zohar Shipony, Nika Iremadze, Sonia N. Acharya, Andrew C. Adey (corresponding)"
published: 2025-01
ingested: 2026-10-07
doi: "10.1016/j.xgen.2024.100726"
journal: "Cell Genomics 5(1):100726"
tags: [sciMETv3, sciMET+ATAC, single-cell-methylation, combinatorial-indexing, bisulfite, EM-seq, enzymatic-conversion, Ultima-Genomics, target-capture, human-cortex, mCH, HMR, s3-ATAC]
entities: ["[[20-Entities/andrew-adey]]"]
concepts: ["[[30-Concepts/combinatorial-indexing]]", "[[30-Concepts/bisulfite-sequencing]]", "[[30-Concepts/tn5-tagmentation]]", "[[30-Concepts/joint-single-cell-multi-omics]]", "[[30-Concepts/chromatin-accessibility]]", "[[30-Concepts/nome-seq]]", "[[30-Concepts/cis-regulatory-element]]", "[[30-Concepts/batch-effect]]"]
topics: ["[[40-Topics/dna-methylation]]", "[[40-Topics/single-cell-multiomics]]", "[[40-Topics/single-cell-atac-seq]]"]
---

**Citation:** Nichols et al. (2025) — *Atlas-scale single-cell DNA methylation profiling with sciMETv3* — *Cell Genomics* 5(1):100726. [DOI](https://doi.org/10.1016/j.xgen.2024.100726)

# Nichols 2025 — sciMETv3

> sciMETv3 adds a **third tier of cell barcoding** — an *in situ* ligation of a well-specific, fully methylated adapter after indexed Tn5 tagmentation (a sci-ATAC-seq3-style step) — to the sciMETv2 workflow. Pre-indexing ×96 before conversion means each final well holds ~600–1,000 nuclei instead of 15–60, so atlas-scale libraries (one preparation produced >140,000 cells from human middle frontal gyrus; dilution capacity ~1 million) come from **seven 96-well plates and one column cleanup**, by one person in days, without FACS. The higher per-well input also makes **enzymatic (EM-seq) conversion** viable, and a double-tagmentation variant, **sciMET+ATAC**, adds chromatin accessibility from the same cells.

## Key claims

- **Throughput scales from ~1,000 to up to 10 million cells** in ~1,000-cell increments with the same molecular structure as sciMETv2 (so sciMET-cap capture still works). Prior atlas technologies needing one well per cell would require 1,302 (384-well) or 5,208 (96-well) plates for comparable ~500,000-cell scale.
- **Pilot**: human cortex (90%) + mouse brain (10%) mix; one final well gave 293 cells, mean 354,763 unique reads and 2.73 million cytosines covered per cell, 49.6% top-strand reads; zero doublets → **maximum doublet bound 3.4%**, cross-species crosstalk ≤1.2%.
- **Capture**: ~6,000 cells multiplexed in one Twist methylome capture gave 5,805 QC-passing cells, 6.2-fold enrichment (vs 7–10-fold for sciMET-cap), 27.7% on-target (vs 30–45%). Capture lowers global mCG (regulatory loci are hypomethylated) without affecting mCH; in brain, capture gains are smaller because mCH is genome-wide.
- **Enzymatic conversion**: 1,525 cells; insert size 163 ± 121 vs 78 ± 69 bp for bisulfite (2.1-fold). Combined with bisulfite-capture data **without bias correction**, clustering and cell-type proportions were comparable. But **TET2 over-converts methylated adapter cytosines** in the Illumina read-2/index-1 primer region (Sanger-confirmed), dropping clusters passing filter to <50% (vs >90%). Ultima Genomics sequencing, which does not use that primer region, sidesteps the problem.
- **Atlas run (four donors, BA46)**: Illumina NovaSeq plate → 44,840 cells, median 1.82 million cytosines, 13.98% duplicates; Ultima UG100 plate (six wafers) → 103,061 cells, median 2.58 million cytosines, 31.49% duplicates. Donors evenly represented; clustering driven by cell type, not individual. Mean non-reference allele frequency at conversion-insensitive transversions 50.01% ± 0.04% — minimal allelic bias. Coverage-matched 8,000-cell subsets from each platform integrate without batch correction; Ultima shows slightly lower mCG.
- **Regulatory biology**: across 31 clusters, 155,110 hypomethylated regions (HMRs); 42.0% unique to one cluster; 68.6% overlap ENCODE DNase HS sites. Promoter HMRs are shared (mean 17.5 clusters; only 7.8% cluster-unique) whereas enhancer HMRs are cell-type-specific (33.1% unique; mean 4.7 clusters).
- **sciMET+ATAC**: tagment native nuclei with one Tn5 index set (ATAC), then fix, disrupt nucleosomes and tagment again with another set (methylome). 4.79% of reads come from the ATAC round; 5,305 cells pass for both modalities; 147,176 peaks, 95.00% overlapping known accessible loci. TSS enrichment is low (5.2 vs ~10–20 typical) because spurious ATAC insertions become amplifiable after the second tagmentation. Methylation clusters were finer than ATAC clusters; ATAC peaks at promoters are uniformly hypomethylated, enhancer peaks variably methylated. Unlike NOMe-based co-assays, it works in brain/ESCs where endogenous non-CG methylation confounds GpC labelling.

## Methods / evidence

Workflow: ScaleBio fixation/nucleosome disruption → indexed Tn5 (methylated adapters) → *in situ* PNK + ligation of 96 methylated barcodes → pooling and dilution (~750 nuclei/well) → bisulfite (ScaleBio) or EM-seq conversion → reverse-adapter ligation → indexing PCR (Illumina, or Ultima with all indexes on one side for single-end reads). Analysis: unidex demultiplexing, premethyst (BSBolt alignment, dedup, call extraction), **Amethyst** (100-kb windows, IRLBA, coverage-bias regression, Rphenograph clustering), annotation by correlation to an Ecker-lab reference atlas, Harmony to merge platforms. A new s3-ATAC implementation on the iCell8 nanowell chip (9,101 cells, TSSe 5.6) plus an annotated ~37,000-cell reference was used to label the ATAC modality.

Weight: strong engineering paper with internal controls (species mixing, allele balance, platform matching). Depth per cell is lower than BRAIN Initiative atlases (authors acknowledge); biological findings (promoter vs enhancer HMR specificity) are confirmatory. Requires 250,000–1 million input nuclei. Conflict: corresponding author holds sciMET patents and advises Scale Biosciences; two authors are Ultima employees.

## Surprising or load-bearing bits

- **The bottleneck shifts from library prep to sequencing.** Libraries can now exceed what is reasonably sequenced; most diluted plates in the atlas run were banked unsequenced.
- **EM-seq's sequence-context bias bites the adapter, not the genome.** TET2 fails to protect some methylated cytosines in a specific adapter context — a platform-dependent failure mode easy to miss. (synthesis)
- **Short fragments limit allele-specific methylation** — conversion plus upfront tagmentation fragments DNA, a structural trade-off of all sciMET designs.
- **Co-assay as bridge, not standalone**: authors recommend sciMET+ATAC for a subset of cells to link methylation atlases to ATAC references, given its lower per-modality quality (nuclear rupture, ambient chromatin).

## Concepts touched

- [[combinatorial-indexing]] — three-tier sci design (tagmentation index × ligation index × PCR index) applied to methylation.
- [[bisulfite-sequencing]] — bisulfite vs enzymatic conversion compared head-to-head in single cells.
- [[tn5-tagmentation]] — Tn5 with fully methylated adapters; sequential tagmentation separates accessible from total DNA.
- [[joint-single-cell-multi-omics]] / [[chromatin-accessibility]] — sciMET+ATAC as an ATAC-based alternative to [[nome-seq]]-style accessibility.
- [[cis-regulatory-element]] — enhancer HMRs are the cell-type-specific methylation layer; promoters largely shared.

## Connections to other sources

- Lineage of the platform: [[mulqueen-2018-sci-met]] → [[nichols-2022-scimet-v2]] → [[acharya-2024-scimet-cap]] → this paper; analysis toolkit [[rylaarsdam-2025-amethyst]].
- Plate-based single-cell methylation it positions against: [[luo-2017-snmc-seq]], [[luo-2018-snmc-seq2]], [[liu-2023-mouse-brain-methylome-3d]]; droplet alternative [[zhang-2023-drop-bs]].
- Accessibility + methylation predecessors: [[clark-2018-scnmt-seq]] (NOMe-based), [[pott-2017-elife]].
- sci-ATAC lineage and tools: [[cusanovich-2015-sciatac]], [[zhang-2024-snapatac2]], [[korsunsky-2019-harmony]].

## Open questions

- Per-cell depth at atlas scale is limited by sequencing cost; will Ultima-class pricing make BRAIN-Initiative depth routine?
- Adapter redesign or modified bases needed for EM-seq on Illumina — unsolved.
- sciMET+ATAC nucleosome disruption is only 8-plex; scaling to 96-plex is "likely prohibitive".
- Input of 250,000–1 million nuclei excludes small clinical samples.

## Related

- [[nichols-2022-scimet-v2]] · [[rylaarsdam-2025-amethyst]] · [[20-Entities/andrew-adey]] · [[40-Topics/dna-methylation]]
