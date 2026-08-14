---
type: summary
title: "Zhang et al. 2023 — Droplet-based bisulfite sequencing for high-throughput profiling of single-cell DNA methylomes (Drop-BS)"
source: "[[00-Sources/papers/Droplet-based bisulfite sequencing for high-throughput profiling of single-cell DNA methylomes]]"
source_kind: paper
author: "Qiang Zhang, Sai Ma, Zhengzhi Liu, Bohan Zhu, Zirui Zhou, Gaoshan Li, J. Javier Meana, Javier González-Maeso, Chang Lu (corresponding)"
published: 2023-08-03
ingested: 2026-08-13
doi: "10.1038/s41467-023-40411-w"
journal: "Nature Communications 14:4672"
tags: [Drop-BS, droplet-microfluidics, scWGBS, MNase, in-droplet-bisulfite, barcode-beads, prefrontal-cortex, mCH]
entities: ["[[chang-lu]]"]
concepts: ["[[bisulfite-sequencing]]", "[[scbs-seq]]", "[[combinatorial-indexing]]", "[[umi-molecular-barcoding]]", "[[cell-type-annotation]]", "[[pseudo-bulk]]"]
topics: ["[[dna-methylation]]", "[[scdna-seq]]", "[[brain-somatic-mosaicism]]"]
---

**Citation:** Zhang et al. (2023) — *Droplet-based bisulfite sequencing for high-throughput profiling of single-cell DNA methylomes* — *Nature Communications* 14, 4672. [DOI](https://doi.org/10.1038/s41467-023-40411-w)

# Zhang 2023 — Drop-BS

> The third throughput strategy for single-cell methylomes, after plates ([[luo-2017-snmc-seq|snmC-seq]]) and combinatorial indexing ([[mulqueen-2018-sci-met|sci-MET]]): **droplet microfluidics**, up to **10,000 cells in 2 days**. The non-obvious finding is that **bisulfite conversion inside droplets yields 9× more library** than the same conversion in bulk — the droplets are not just containers, they change the chemistry's yield.

## Key claims

- **Five steps, three microfluidic devices.** (1) Encapsulate single nuclei with MNase for lysis and fragmentation (~35 µm droplets, ~10% single-cell occupancy, <0.5% doublets); (2) generate barcode-bead droplets (~7.0% bead occupancy) and fuse them to the scDNA droplets by AC-driven dielectrophoresis (~80% fusion); (3) UV-release barcodes from photocleavable linkers and ligate to fragmented gDNA; (4) re-encapsulate for bisulfite conversion; (5) random priming and indexing PCR.
- **In-droplet bisulfite conversion increases library concentration 9-fold over bulk-tube conversion.** Conversion rate 99.0% against unmethylated lambda control. This is the paper's most reusable chemistry finding and is stated as a discovery rather than a design intent.
- **MNase digestion, not Tn5, does the fragmentation** — and the CaCl₂ concentration had to be optimised because over-digestion (<150 bp) loses fragments to bead selection while under-digestion starves the barcoding reaction. This is one of the few single-cell methylome protocols using MNase.
- **Throughput arithmetic**: ~3,000 scDNA droplets/s generated; barcode-droplet generation and fusion at ~132/s. Processing ~2,000 cells needs ~20,000 barcode beads and ~574,000 droplets, 1.3 h on-device (10 min + 36 min + 30 min), 2 days total.
- **Species mixing confirms low crosstalk**: 741 high-quality barcodes from a 1:1 GM12878/mouse mix, ~96% with >90% of reads to one genome (445 human, 266 mouse).
- **Cell lines cluster by methylome, not by depth.** GM12878/HEK293/MCF7 mixture (1,929 cells, ~16,157 unique reads/cell) gave three UMAP/Louvain clusters, confirmed by co-clustering with 300 known-identity cells. Cluster-average global mCG (50.5%, 68.2%, 63.0%) matched published bulk values (48%, 66%, 65%).
- **Brain profiling reproduces expected mCH biology.** Mouse PFC: 1,123 cells, ~23,932 unique reads/cell, ~58% mapping, 13,492 CpGs/cell, 11.4M CpGs merged; global mCG/CG 71.73%, mCH/CH 1.85%. Human PFC: 2,813 cells across two donors; mCG/CG 76.12%, mCH/CH 2.71% — versus ~1% mCH in the cell lines, matching the neuronal mCH literature.
- **Cell types called by CH methylation over 100-kb bins**, then labelled by CG methylation at published neuron-type CG-DMRs — the same two-step strategy as sci-MET, and again anchored on [[luo-2017-snmc-seq|snmC-seq]] reference DMRs. Mouse: 7 clusters (2 excitatory, 3 inhibitory, 2 non-neuronal). Human combined: 7 clusters (3 excitatory, 1 inhibitory, 3 non-neuronal), with cross-donor cluster correspondence verified.
- **637 pseudobulk DMRs** between human excitatory and inhibitory clusters, mapping to 594 genes including *SATB2*, *CAMK2A*, *PROX1*, *SV2C*, *GRIK3*, *SOX6*.
- **mCH stratifies by functional element**: CpG islands lowest, then promoters, then genic regions ≈ TFBS, all below the genome-wide average.

## Methods / evidence

Species-mixing purity test, three-cell-line mixture with spike-in ground truth, mouse PFC, and two post-mortem human PFC donors with cross-donor co-clustering. Validation is by concordance with published bulk methylomes and by DMR enrichment against snmC-seq references.

Weight: purity and throughput are well demonstrated. The biological findings are recapitulations of known cortical methylation biology — appropriate for a methods paper, but the assay has not yet been used to find something new.

## Surprising or load-bearing bits

- **The 9× in-droplet bisulfite yield is the finding most likely to transfer to other protocols.** Bisulfite is famously destructive; if confinement mitigates the loss, that is relevant to every low-input BS method, not only droplet ones.
- **Unevenness of reads per cell, not the mean, limits resolution.** The authors show clustering is driven by mCG level rather than read count, but note that spread in reads/cell widens clusters and "potentially decreases the resolution of various cell types when they are similar." This is the honest statement of the low-coverage regime's limit.
- **~16,000–41,000 unique reads per cell is 10–25× below [[luo-2017-snmc-seq|snmC-seq]]** and roughly at or below [[mulqueen-2018-sci-met|sci-MET]] levels. Drop-BS buys speed and operator-hours, not information per cell.
- **All three throughput strategies converge on the same annotation crutch**: cluster on mCH bins, then label against snmC-seq DMRs. None of the high-throughput methods can annotate cell types de novo from their own data — a dependency worth naming.
- **MNase in a droplet** is a chromatin-aware fragmentation choice in an assay that discards chromatin information. Whether nucleosome positioning biases which CpGs are recovered is not examined.

## Entities mentioned

- [[chang-lu]] — corresponding author; microfluidic epigenomics.

## Concepts touched

- [[bisulfite-sequencing]] — the in-droplet yield effect is a new fact about the chemistry.
- [[scbs-seq]] — Drop-BS is the droplet member of the scWGBS family.
- [[pseudo-bulk]] — cluster-merged reads for DMR calling, the standard move in sparse methylome data.

## Connections to other sources

- The three-way throughput comparison this paper defines itself against: [[smallwood-2014-natmethods]]/[[clark-2017-scbs-seq-protocol]] (tubes), [[luo-2017-snmc-seq]]/[[luo-2018-snmc-seq2]] (plates), [[mulqueen-2018-sci-met]]/[[nichols-2022-scimet-v2]] (combinatorial indexing).
- Reduced-representation alternative: [[guo-2013-scrrbs]], [[guo-2015-scrrbs-protocol]].
- Droplet precedents in other modalities that it cites as proof of concept: [[macosko-2015-drop-seq]] (RNA), [[pellegrino-2018-tapestri]] (DNA), [[buenrostro-2015-nature]]-lineage droplet ATAC, [[rotem-2015-drop-chip]] (ChIP), droplet CUT&Tag.
- Bisulfite-free chemistries that sidestep conversion damage entirely: [[chen-2025-sctaps-sccaps-plus]], [[bai-2024-simple-seq]].
- Analysis in this sparsity regime: [[kapourani-2021-scmet]], [[kremer-2024-methscan]], [[desouza-2020-epiclomal]].

## Open questions

- **Why in-droplet bisulfite conversion yields 9× more library is not explained** — confinement, reduced adsorption losses, and altered effective concentration are all candidates, none tested.
- Whether MNase fragmentation biases CpG recovery by nucleosome occupancy is unexamined.
- No comparison of *cost per informative CpG* across the three throughput strategies, which is the number a lab actually needs to choose between them.
- Drop-BS is DNA-methylation-only; whether the droplet workflow can co-capture transcriptome or accessibility (as [[clark-2018-scnmt-seq]] does at plate scale) is unaddressed.

## Related

- [[mulqueen-2018-sci-met]] · [[luo-2017-snmc-seq]] · [[clark-2017-scbs-seq-protocol]] · [[40-Topics/dna-methylation]]
