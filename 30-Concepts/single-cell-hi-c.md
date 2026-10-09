---
type: concept
title: Single-cell Hi-C
aliases: [scHi-C, sciHi-C, sc3DG-seq]
tags: [3D-genome, Hi-C, chromatin-contacts, single-cell]
created: 2026-05-12
updated: 2026-10-08
---

# Single-cell Hi-C

> A family of methods (scHi-C, sciHi-C, Dip-C, sn-m3C, snHi-C, HiRES, scSPRITE, scNanoHi-C, Droplet Hi-C, GAGE-seq) that profile genome-wide chromatin contacts at single-cell resolution.

## Definition

Most methods inherit the 3C/Hi-C ligation strategy (crosslink → restrict → ligate proximity-tagged fragments → sequence) and add per-cell partitioning (microfluidic, FACS plate-based, or combinatorial-indexing). scSPRITE replaces ligation with split-pool barcoding of crosslinked spatial clusters ([[10-Summaries/arrastia-2022-scsprite]]); scNanoHi-C uses long reads to capture multi-way contacts.

## Why it matters

Reveals cell-to-cell variability in TADs, A/B compartments, and chromatin loops — variability that bulk Hi-C averages away. Critical for understanding lineage decisions, disease heterogeneity, and cell-cycle dynamics of 3D architecture.

## Examples

- See [[10-Summaries/hong-2025-sc3d-genome-review]] for the technology landscape.
- [[10-Summaries/jiang-2026-stark-scnucleome]] benchmarks 15 sc3DG-seq methods.

## Added 2026-08-10

Assay origin: [[10-Summaries/lieberman-aiden-2009-hic]], whose *n*²-resolution rule is the source of the sparsity constraint every single-cell variant negotiates with. High-throughput branch: [[10-Summaries/ramani-2017-scihi-c]] (combinatorial indexing, 10,696 cells at ~8,000–9,000 contacts each, in-silico cell-cycle sorting, translocations recoverable from contact structure).

The sparsity arithmetic: 5–10% linear genome coverage becomes **0.25–1% of possible contacts**, and coverage heterogeneity — not biology — is the leading factor driving clustering results ([[10-Summaries/zhou-2019-schicluster]]). Clustering degrades below 25,000 contacts per cell and collapses at 5,000 ([[10-Summaries/zhou-2019-schicluster]]), which is below what indexing-based protocols deliver. Imputation is therefore not optional: [[10-Summaries/zhou-2019-schicluster]] (convolution + random walk + top-20% selection) and [[10-Summaries/zhang-2022-higashi]] (hypergraph representation learning, sparse-native, borrowing across cells).


## Added 2026-10-07

With 100 mESCs, SnapHiC-G retained 61% genome-wide power while all bulk callers and SnapHiC fell below 10%; its advantage shrank in oligodendrocytes (1,038 cells, ~278 million pooled intrachromosomal contacts), where pseudo-bulk reaches bulk-like depth ([[10-Summaries/liu-2024-snaphic-g]]).

Sticky-end proximity ligation used by multiomic scHi-C (LiMCA, snm3C-seq) leaves one restriction motif at each junction that aligners multimap to both loci; map3C trims these spans, resolving 77–79% of SNP haplotype conflicts versus 28–29% for random SNP removal ([[10-Summaries/galasso-2026-map3c]]). MAPQ filtering raised the snm3C-seq intra/inter contact ratio to 3.16 from ~1.0 with TAURUS-MH or YAP and lowered 3D-model restraint violations (median 0.004 vs 0.037–0.051) ([[10-Summaries/galasso-2026-map3c]]).

Droplet Hi-C adds a droplet-microfluidic route alongside microwell and combinatorial-indexing single-cell Hi-C. It runs in situ Hi-C (DpnII/MboI/NlaIII digestion and ligation in fixed nuclei, then SDS histone removal) and barcodes the ligated nuclei with the commercial 10x Genomics scATAC kit ([[10-Summaries/chang-2025-droplet-hi-c]]). The protocol takes ~10 h, processes 8 samples in parallel and profiles ≥40,000 cells per experiment ([[10-Summaries/chang-2025-droplet-hi-c]]). Mouse cortex data had a median of 175,021 unique read pairs per cell, and the *cis*-long ratio fell between Dip-C (lower) and sn-m3C-seq (higher) ([[10-Summaries/chang-2025-droplet-hi-c]]).

Down-sampling Droplet Hi-C cortex neurons showed that compartment and insulation scores lose agreement below about 400 cells or 10 million long-range contacts per cell type. Loop calling probably needs deeper data ([[10-Summaries/chang-2025-droplet-hi-c]]).

Arrastia et al. argue that ligation-based scHi-C is limited to about 10-Mb resolution per cell and under-captures inter-chromosomal and nuclear-body contacts. In their comparison, centromere-proximal and nucleolar contacts were undetectable even in ensemble scHi-C data, while scSPRITE detected them in single cells ([[10-Summaries/arrastia-2022-scsprite]]).

scNanoHi-C reads whole ligation concatemers on Oxford Nanopore PromethION, not pairwise junctions. About half of its concatemers are high-order (cardinality ≥3), and median contacts per cell range from 58,871 (~500 cells/run) to 464,844 (~24 cells/run) ([[10-Summaries/li-2023-scnanohi-c]]). In single cells it detects chromosome territories and 87.0% of compartment triplets. TADs are much weaker: on average a TAD is seen in ≤60% of cells ([[10-Summaries/li-2023-scnanohi-c]]).

Fast-Higashi represents each chromosome's contact maps as a bin × feature × cell tensor and jointly decomposes them (core-PARAFAC2), giving cell embeddings plus interpretable "meta-interactions"; it separated cortical L2–3/L4/L5/L6 excitatory neurons from chromatin conformation alone and ran ~40× faster than 3DVI and ~9× faster than Higashi ([[10-Summaries/zhang-2022-fast-higashi]]).

Two computational stances on sparsity: SnapHiC2 imputes each cell by sliding-window random walk with restart to call 5 kb loops, 3× faster with ~70% less memory than SnapHiC ([[10-Summaries/li-2022-snaphic2]]), while scDIAGRAM avoids imputation entirely for compartment calling, arguing that imputation (scHiCluster, Higashi) smooths away cell-specific heterogeneity ([[10-Summaries/peng-2026-scdiagram]]). Typical datasets have a few hundred cells per type at ~1 million contacts per cell, far below the ~1 billion contacts used for bulk loop calling ([[10-Summaries/li-2022-snaphic2]]).

In an eight-method benchmark across four scHi-C datasets, the simple BandNorm scaling ranked best overall (median rank 2), followed by scVI-3D (3), Higashi (3.5) and scHiCluster (4) ([[10-Summaries/zheng-2022-bandnorm-scvi-3d]]). BandNorm runs in about 15 minutes, against hours to more than a day for the alternatives ([[10-Summaries/zheng-2022-bandnorm-scvi-3d]]). scVI-3D is recommended once rare cell types or high-sparsity settings appear ([[10-Summaries/zheng-2022-bandnorm-scvi-3d]]).

The bulk reference for scHi-C is the in situ Hi-C map of GM12878. It needed 4.9 billion contacts to reach a 950 bp map resolution, defined as the smallest bin at which 80% of loci have ≥1,000 contacts ([[10-Summaries/rao-2014-in-situ-hic]]). Its in-nucleus ligation resembles the earlier single-cell Hi-C protocol ([[10-Summaries/rao-2014-in-situ-hic]]).

A 2025 review counts 13 scHi-C protocols: eight that capture contacts only and five multi-omic ones (sn-m3C-seq, scMethyl Hi-C, HiRES, MUSIC, s3-GCC) ([[10-Summaries/dautle-2025-schic-review]]). The review re-scored public datasets on contacts per cell and cis/trans ratio. Among contact-only protocols, Nagano 2017 and scNanoHi-C did best. sci-Hi-C and scSPRITE gave few contacts with good cis/trans, and Dip-C gave average contacts with some of the lowest cis/trans ratios ([[10-Summaries/dautle-2025-schic-review]]). Multi-omic protocols did not differ significantly from contact-only ones on either metric (Wilcoxon–Mann–Whitney, P cutoff 0.05) ([[10-Summaries/dautle-2025-schic-review]]). This comparison was not matched for sequencing depth (synthesis).


## Added 2026-10-08 — sequence models & foundation models

- Sequence priors from a distilled DNA language model improved resolution enhancement of 1/16-downsampled bulk Hi-C across 177 species (Evo2HiC), a possible but untested route for sparse scHi-C imputation ([[10-Summaries/fang-2025-evo2hic]])
- SUCCEED plus pseudobulk scATAC from ≤200 cells predicted K562 Hi-C contact maps with only modest loss in insulation-score agreement, a sequence-based alternative to sparse single-cell Hi-C that was evaluated only against bulk Hi-C ([[10-Summaries/sun-2026-succeed]])
- Fine-tuned from bulk Hi-C pretraining, HiCFoundation enhanced scHi-C better than Higashi, scHiCluster and scVI-3D, and when applied to human WTC11 cells without retraining it beat scHiCluster by 35.9% in Pearson correlation ([[10-Summaries/wang-2026-hicfoundation]]).

## Related

- [[40-Topics/3d-genome]] · [[30-Concepts/topologically-associating-domain]] · [[30-Concepts/chromatin-compartments]] · [[40-Topics/3d-genome]]

## Added 2026-08-13

Three 2021–2026 methods extend scHi-C beyond clustering to per-feature calling, and share a common statistical move — **treat cells as replicates rather than as reads**.

- **Loops**: [[10-Summaries/yu-2021-snaphic|SnapHiC]] imputes each cell separately (random walk with restart), then paired *t*-tests across cells at each bin pair. Pseudobulk approaches need >500–1,000 cells; SnapHiC calls 1,050–1,420 loops from 75 ([[10-Summaries/yu-2021-snaphic]]).
- **Subcompartments**: [[10-Summaries/xiong-2024-scghost|scGHOST]] embeds loci as graph nodes via constrained random walks over Higashi-imputed maps. Subcompartments resisted single-cell analysis for a coverage-arithmetic reason — bulk annotation needs ≥50M *trans* reads, and scHi-C has almost none even at pseudobulk ([[10-Summaries/xiong-2024-scghost]]).
- **Multi-way interactions**: [[10-Summaries/park-2026-mintsc|MINTsC]] reads scHi-C as a multilayer network where a multi-way contact is a clique — a question bulk Hi-C cannot express at all ([[10-Summaries/park-2026-mintsc]]).

**Systematic biases in imputed scHi-C are negligible**: normalisation against fragment size, GC content, or mappability is unnecessary, unlike bulk Hi-C — sparsity apparently swamps the systematic biases ([[10-Summaries/yu-2021-snaphic]]).

**A shared unresolved dependency**: all three assume a homogeneous cell group and report features per *cell type*, not per cell. The single-cell formulation buys statistical power but does not yet deliver per-cell feature variability ([[10-Summaries/yu-2021-snaphic]]; [[10-Summaries/park-2026-mintsc]]). (synthesis)

Cell-type labels in the brain applications come from methylation, independently of contacts ([[10-Summaries/luo-2017-snmc-seq]]; [[10-Summaries/lee-2019-natmethods]]).
