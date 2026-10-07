---
type: summary
title: "Acharya et al. 2024 — sciMET-cap: high-throughput single-cell methylation analysis with a reduced sequencing burden"
source: "[[00-Sources/papers/sciMET-cap_ high-throughput single-cell methylation analysis with a reduced sequencing burden]]"
source_quality: full
source_sha256: "7082866f9a90b8b40cf22065c2428836e7028b226d55cce0e6f4cb8f7b8297d4"
source_kind: paper
author: "Sonia N. Acharya, Ruth V. Nichols, Lauren E. Rylaarsdam, Brendan L. O'Connell, Theodore P. Braun, Andrew C. Adey (corresponding)"
published: 2024-07-10
ingested: 2026-10-07
doi: "10.1186/s13059-024-03306-7"
journal: "Genome Biology 25:186"
tags: [sciMET-cap, sciMETv2, hybrid-capture, targeted-methylation, combinatorial-indexing, bisulfite, DMR, PBMC, human-cortex, sequencing-cost]
entities: ["[[20-Entities/andrew-adey]]"]
concepts: ["[[bisulfite-sequencing]]", "[[combinatorial-indexing]]", "[[tn5-tagmentation]]", "[[sequencing-depth-and-coverage]]", "[[pseudo-bulk]]", "[[dimensionality-reduction]]", "[[clustering-algorithms]]", "[[cpg-island]]"]
topics: ["[[dna-methylation]]", "[[single-cell-multiomics]]"]
---

**Citation:** Acharya et al. (2024) — *sciMET-cap: high-throughput single-cell methylation analysis with a reduced sequencing burden* — *Genome Biology* 25:186. [DOI](https://doi.org/10.1186/s13059-024-03306-7)

# Acharya 2024 — sciMET-cap

> sciMETv2 solved the *throughput* problem of single-cell methylation (combinatorial indexing amortises bisulfite conversion over many cells per well) but not the *sequencing* problem: genome-wide methylomes need ~2–6 million raw reads per cell to reach the 300–500 thousand CpGs required for cell-type assignment. sciMET-cap bolts an **off-the-shelf post-bisulfite hybrid-capture panel** (Twist Human Methylome Panel, ~123 Mbp of regulatory regions) onto the pooled sciMETv2 library. Cells are clustered on the enriched, cell-type-variable regions; the ~70% of reads that fall **off target** are then aggregated per cluster into near-complete pseudo-bulk methylomes for genome-wide DMR calling. Result: comparable human-cortex clustering from ~350 M reads versus ~7 billion without capture.

## Key claims

- **The bottleneck is reads, not cells.** sciMETv2 typically needs two to six million raw reads per cell, because at least 300–500 thousand CG dinucleotides must be captured per cell for cell-type assignment. RRBS-style targeting misses much of the putative regulatory space; post-conversion hybrid capture of pooled, barcoded libraries does not.
- **Capture enriches 7–8-fold and raises CpGs per raw read.** In the PBMC test (same input library, all conditions downsampled to 350 M raw read pairs), unique CG sites per cell rose from a median 93,676 (no capture) to 134,432–139,006 (capture), even though unique aligned reads fell (213,723 noCap vs 154,192–175,255 capture) through lost library complexity. In brain, capture gave 1.29 unique CG sites per raw read versus 0.75 without.
- **Capture does not distort methylation calls.** Site-level Pearson correlations ≥0.96 across all conditions (on-target ≥0.97, off-target ≥0.93; top-25% GC bins ≥0.97, bottom-25% ≥0.91), and no Watson/Crick or conversion-direction strand bias.
- **Protocol tweaks barely matter.** A custom blocker against the Tn5 mosaic-end sequence (present in sciMETv2 but not standard bisulfite libraries) made no difference. A 67 °C wash raised aligned-read enrichment (median 10.1-fold, 40.1% on target vs 9.3/36.0% and 9.4/37.5%), but the advantage vanished on unique reads (7.1-fold vs 7.4 and 7.7) because complexity loss was worse — so **standard wash conditions maximise information per cell**.
- **Target windows only work after capture.** Without capture, clustering on the capture-panel windows gave 4 PBMC clusters versus 6 on 50-kbp genome tiles. With capture, the target windows gave 7–8 clusters, while 50-kbp tiles gave 5 for every condition.
- **More and truer DMRs.** At matched reads, PBMC DMRs on target-window clustering were 20,346–23,832 (capture) vs 694 (no capture); on 50-kbp clustering 2,497–9,984 vs 1,164. stdBlock recovered the largest share of the DMRs found in the pooled deep "allData" set with the fewest condition-specific calls; the no-capture control recovered a minority. Marker-gene promoters showed cluster-specific patterns only in capture data.
- **Off-target reads make near-complete cluster methylomes.** In a 5,952-cell PBMC dataset (14 clusters: monocytes, B, NK, T with CD4/CD8 branches, labelled via promoter methylation and BLUEPRINT sorted-cell WGBS), a median 96.0% of 1,500-bp windows reached ≥10 CpG coverage per cluster, yielding 195,483 DMRs from ~1.7 billion raw reads on a benchtop sequencer. The abstract states genome-wide DMR calling works for clusters as small as 115 cells.
- **Brain: CG over targets resolves what CH cannot.** On the deep sciMETv2.LA middle-frontal-gyrus library (927 cells; median 5.5 M raw reads and 1.67 M unique CG sites per cell; 6.98 billion reads total), capture at 339 M reads gave 10 clusters on CG target windows vs 4 without capture; CH clustering gave 7 for both. **Only CG target-window methylation separated excitatory from inhibitory neurons**.
- **Single-flowcell experiments become realistic.** One sciMETv2.SL preparation on a second cortex donor, one capture, one NextSeq 2000 P3 flowcell (~1.2 billion reads): 6,123 cells, 12 clusters, 64,774 DMRs — though per-cluster coverage was lower, so the authors recommend more depth or more cells for highly heterogeneous tissues.
- **Recommended budget: 200–275 thousand raw reads per cell** for 5,000–10,000-cell datasets — still above scRNA-seq (50–100 thousand) or scATAC-seq (75–125 thousand), but an order of magnitude below the ~2 million recommended for non-capture single-cell methylation.

## Methods / evidence

Controlled design: one PBMC sciMETv2.SL library (1,915 cells; median 489,303 raw reads and 283,317 unique CGs per cell; 1.13 billion raw reads) split into three capture conditions plus a no-capture control, all downsampled to identical raw read counts, plus a deep pooled reference ("allData"; median 551,685 unique CGs per cell). Brain comparison reuses the previously published deep sciMETv2.LA cortex library (from [[nichols-2022-scimet-v2]]) with downsampled capture and no-capture arms of ~340 M reads. Processing: unidex demultiplexing, BSBolt alignment, SVD (irlba) → UMAP → Phenograph (Louvain) clustering; DMRs by MethylKit on 1,500-bp windows sliding 500 bp, each cluster against the aggregate of all other clusters.

Weight: the matched-read-count design is clean and the "same input library" control removes biological confounders. But evaluation is internal — cluster counts and DMR counts, judged against the authors' own deeper data and marker genes, with no independent ground truth beyond BLUEPRINT bulk profiles. Cluster count from Louvain at fixed parameters is a weak proxy for resolution. Only human (the panel is human-only) and only two tissues. The senior author holds patents on and equity in the commercialised sciMETv2 technology (Scale Biosciences), and Twist/Scale supplied reagents — declared in the paper.

## Surprising or load-bearing bits

- **The design is "cluster on targets, call DMRs on everything".** Capture is only ~28–31% on target (43% including 200-bp "shadow" coverage), so most reads land genome-wide — and that "waste" is what makes pooled cluster methylomes near-complete. Low capture efficiency is turned into a feature. (synthesis)
- **Single-cell capture is half as efficient as bulk.** Bulk libraries reach ~12–18-fold enrichment versus 7–8-fold here; neither custom blockers nor stringent washing closed the gap, and the authors speculate short sciMET inserts or probe affinity are the cause. Per-cell high-coverage targeted methylation is therefore still out of reach.
- **Capture enrichment and library complexity trade off directly** — the wash67 condition shows that a better on-target fraction can mean *less* information per cell. The right metric is unique CpGs per raw read, not % on target. (synthesis)
- **CH methylation is not enough even in brain.** The excitatory/inhibitory split appeared only from CG over regulatory targets, which cuts against the habit of clustering neurons on CH alone.
- Small internal inconsistencies: the panel is described as 123 Mbp in Results and 125 Mbp in Discussion/Methods, and the DMR q-value cutoff as ≤1e−5 in Results versus ≤0.0001 in Methods.

## Concepts touched

- [[bisulfite-sequencing]] — post-conversion hybrid capture applied to a single-cell bisulfite library.
- [[combinatorial-indexing]] — the barcoded pooled library is what makes one capture reaction serve thousands of cells.
- [[tn5-tagmentation]] — the Tn5 mosaic-end sequence in sciMETv2 adapters prompted the (unnecessary) custom blocker.
- [[sequencing-depth-and-coverage]] — unique CpGs per raw read as the cost-efficiency metric; 200–275 thousand reads/cell target.
- [[pseudo-bulk]] — per-cluster aggregation of off-target reads into near-complete methylomes for DMR calling.
- [[cpg-island]] — the capture panel targets CpG islands and shores, tissue-specific DMRs and enhancers.
- [[dimensionality-reduction]] / [[clustering-algorithms]] — SVD → UMAP → Louvain (Phenograph) on windowed methylation.

## Connections to other sources

- Direct extension of [[nichols-2022-scimet-v2]] (sciMETv2.LA/.SL, which supplies the brain library re-used here) and of the original [[mulqueen-2018-sci-met]].
- Plate-based single-cell methylomes it positions against: [[smallwood-2014-natmethods]], [[clark-2017-scbs-seq-protocol]], [[luo-2018-snmc-seq2]] (whose bisulfite chemistry sciMETv2 adapts), and the brain atlas [[liu-2023-mouse-brain-methylome-3d]].
- RRBS as the restriction-based alternative to capture: [[guo-2013-scrrbs]].
- Other routes to cheaper or richer single-cell methylation: [[chen-2025-sctaps-sccaps-plus]] (bisulfite-free), [[shen-2026-splicool-seq]] (split-pool methylation + accessibility).

## Open questions

- Can longer-insert sciMET libraries or re-designed probes reach bulk-level (12–18-fold) enrichment, enabling per-cell rather than per-cluster analysis of targeted loci?
- The panel is human-only; how much of the gain transfers to mouse or other species once panels exist?
- Panel regions were chosen from bulk methylome literature — do they systematically miss rare-cell-type-specific DMRs that genome-wide tiling would catch? Off-target aggregation partly answers this, but only for clusters already resolved. (synthesis)
- How do the 115-cell minimum cluster size and the recommended 200–275 thousand reads/cell interact in highly heterogeneous tissues like the second cortex dataset?

## Related

- [[nichols-2022-scimet-v2]] · [[andrew-adey]] · [[combinatorial-indexing]] · [[40-Topics/dna-methylation]]
