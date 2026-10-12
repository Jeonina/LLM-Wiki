---
type: concept
title: Single-cell Hi-C
aliases: [scHi-C, sciHi-C, sc3DG-seq]
tags: [3D-genome, Hi-C, chromatin-contacts, single-cell]
created: 2026-05-12
updated: 2026-10-12
---

# Single-cell Hi-C

> A family of methods (scHi-C, sciHi-C, Dip-C, sn-m3C, snHi-C, HiRES, scSPRITE, scNanoHi-C, Droplet Hi-C, GAGE-seq) that profile genome-wide chromatin contacts at single-cell resolution ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]; [[10-Summaries/dautle-2025-schic-review|Dautle 2025]]).

> [!abstract] 한눈에
> Single-cell Hi-C는 세포 하나하나에서 유전체 전체의 chromatin contact를 재는 방법들로, bulk Hi-C가 평균으로 지워 버린 TAD·compartment·loop의 세포 간 차이를 보여 준다 ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]). 다만 한 세포에서 얻는 contact가 가능한 contact의 1%도 안 될 만큼 희소해서, imputation을 할지, 세포를 replicate로 묶을지가 분석의 핵심 쟁점이다 ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]; [[10-Summaries/peng-2026-scdiagram|scDIAGRAM]]).

## Definition

- Most methods inherit the 3C/Hi-C ligation strategy (crosslink → restrict → ligate proximity-tagged fragments → sequence) and add per-cell partitioning (microfluidic, FACS plate-based, or combinatorial indexing) (synthesis).
- scSPRITE replaces ligation with split-pool barcoding of crosslinked spatial clusters ([[10-Summaries/arrastia-2022-scsprite|scSPRITE]]); scNanoHi-C uses long reads to capture multi-way contacts ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).
- Assay origin is bulk Hi-C ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]), whose *n*²-resolution rule is the source of the sparsity constraint every single-cell variant negotiates with ([[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]).
- The bulk reference for scHi-C is the in situ Hi-C map of GM12878, which needed 4.9 billion contacts to reach a 950 bp map resolution, defined as the smallest bin at which 80% of loci have ≥1,000 contacts ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]). Its in-nucleus ligation resembles the earlier single-cell Hi-C protocol ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

## Why it matters

- Single-cell Hi-C reveals cell-to-cell variability in TADs, A/B compartments and chromatin loops — variability that bulk Hi-C averages away ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]).
- That variability matters for lineage decisions, disease heterogeneity and cell-cycle dynamics of 3D architecture ([[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]).
- Some questions cannot be expressed in bulk Hi-C at all, such as multi-way contacts read as cliques in a multilayer network ([[10-Summaries/park-2026-mintsc|MINTsC]]).

## Protocols

[[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]] surveys the technology landscape, and [[10-Summaries/jiang-2026-stark-scnucleome|STARK]] benchmarks 15 sc3DG-seq methods ([[10-Summaries/jiang-2026-stark-scnucleome|STARK]]). A 2025 review counts 13 scHi-C protocols: eight that capture contacts only and five multi-omic ones (sn-m3C-seq, scMethyl Hi-C, HiRES, MUSIC, s3-GCC) ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]).

| Protocol | Partitioning / chemistry | Throughput and depth | Source |
|---|---|---|---|
| sciHi-C | Combinatorial indexing | 10,696 cells at ~8,000–9,000 contacts each | ([[10-Summaries/ramani-2017-scihi-c\|sciHi-C]]) |
| Droplet Hi-C | In situ Hi-C (DpnII/MboI/NlaIII digestion and ligation in fixed nuclei, then SDS histone removal), barcoded with the commercial 10x Genomics scATAC kit | ≥40,000 cells per experiment, ~10 h, 8 samples in parallel; mouse cortex median 175,021 unique read pairs per cell | ([[10-Summaries/chang-2025-droplet-hi-c\|Chang 2025]]) |
| scSPRITE | Split-pool barcoding of crosslinked spatial clusters, no ligation | Few contacts per cell, good cis/trans | ([[10-Summaries/arrastia-2022-scsprite\|scSPRITE]]; [[10-Summaries/dautle-2025-schic-review\|Dautle 2025]]) |
| scNanoHi-C | Whole ligation concatemers read on Oxford Nanopore PromethION, not pairwise junctions | Median contacts per cell 58,871 (~500 cells/run) to 464,844 (~24 cells/run); about half of concatemers high-order (cardinality ≥3) | ([[10-Summaries/li-2023-scnanohi-c\|scNanoHi-C]]) |
| Multi-omic scHi-C (LiMCA, snm3C-seq) | Sticky-end proximity ligation alongside a second modality | — | ([[10-Summaries/galasso-2026-map3c\|map3C]]) |

- Droplet Hi-C adds a droplet-microfluidic route alongside microwell and combinatorial-indexing single-cell Hi-C ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]). Its *cis*-long ratio in mouse cortex fell between Dip-C (lower) and sn-m3C-seq (higher) ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).
- sciHi-C supports in-silico cell-cycle sorting, and translocations are recoverable from contact structure ([[10-Summaries/ramani-2017-scihi-c|sciHi-C]]).
- Re-scoring public datasets on contacts per cell and cis/trans ratio, Nagano 2017 and scNanoHi-C did best among contact-only protocols; sci-Hi-C and scSPRITE gave few contacts with good cis/trans, and Dip-C gave average contacts with some of the lowest cis/trans ratios ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]).
- Multi-omic protocols did not differ significantly from contact-only ones on either metric (Wilcoxon–Mann–Whitney, P cutoff 0.05) ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]).

## Sparsity

- 5–10% linear genome coverage becomes **0.25–1% of possible contacts**, and coverage heterogeneity — not biology — is the leading factor driving clustering results ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).
- Clustering degrades below 25,000 contacts per cell and collapses at 5,000, which is below what indexing-based protocols deliver ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]).
- Typical datasets have a few hundred cells per type at ~1 million contacts per cell, far below the ~1 billion contacts used for bulk loop calling ([[10-Summaries/li-2022-snaphic2|SnapHiC2]]).
- Subcompartments resisted single-cell analysis for a coverage-arithmetic reason: bulk annotation needs ≥50M *trans* reads, and scHi-C has almost none even at pseudobulk ([[10-Summaries/xiong-2024-scghost|scGHOST]]).
- Imputation is therefore not optional for clustering-style analyses ([[10-Summaries/zhou-2019-schicluster|scHiCluster]]; [[10-Summaries/zhang-2022-higashi|Higashi]]).

## Computational methods

Three 2021–2026 methods extend scHi-C beyond clustering to per-feature calling, and share a common statistical move — **treat cells as replicates rather than as reads** ([[10-Summaries/yu-2021-snaphic|SnapHiC]]; [[10-Summaries/xiong-2024-scghost|scGHOST]]; [[10-Summaries/park-2026-mintsc|MINTsC]]).

| Tool | Task | Approach | Source |
|---|---|---|---|
| [[10-Summaries/zhou-2019-schicluster\|scHiCluster]] | Imputation, clustering | Convolution + random walk + top-20% selection | ([[10-Summaries/zhou-2019-schicluster\|scHiCluster]]) |
| [[10-Summaries/zhang-2022-higashi\|Higashi]] | Imputation, embedding | Hypergraph representation learning, sparse-native, borrowing across cells | ([[10-Summaries/zhang-2022-higashi\|Higashi]]) |
| [[10-Summaries/zhang-2022-fast-higashi\|Fast-Higashi]] | Embedding | Each chromosome's contact maps as a bin × feature × cell tensor, jointly decomposed (core-PARAFAC2), giving cell embeddings plus interpretable "meta-interactions" | ([[10-Summaries/zhang-2022-fast-higashi\|Fast-Higashi]]) |
| BandNorm / scVI-3D | Normalization, de-noising | Simple band-wise scaling (BandNorm); scVI-3D for rare cell types or high sparsity | ([[10-Summaries/zheng-2022-bandnorm-scvi-3d\|Zheng 2022]]) |
| [[10-Summaries/yu-2021-snaphic\|SnapHiC]] | Loops | Imputes each cell separately (random walk with restart), then paired *t*-tests across cells at each bin pair | ([[10-Summaries/yu-2021-snaphic\|SnapHiC]]) |
| SnapHiC2 | Loops (5 kb) | Sliding-window random walk with restart per cell; 3× faster with ~70% less memory than SnapHiC | ([[10-Summaries/li-2022-snaphic2\|SnapHiC2]]) |
| SnapHiC-G | Long-range enhancer–promoter interactions | Global background model | ([[10-Summaries/liu-2024-snaphic-g\|SnapHiC-G]]) |
| [[10-Summaries/xiong-2024-scghost\|scGHOST]] | Subcompartments | Embeds loci as graph nodes via constrained random walks over Higashi-imputed maps | ([[10-Summaries/xiong-2024-scghost\|scGHOST]]) |
| [[10-Summaries/park-2026-mintsc\|MINTsC]] | Multi-way interactions | Reads scHi-C as a multilayer network where a multi-way contact is a clique | ([[10-Summaries/park-2026-mintsc\|MINTsC]]) |
| scDIAGRAM | Compartments | Calls compartments from an individual matrix without imputation | ([[10-Summaries/peng-2026-scdiagram\|scDIAGRAM]]) |
| map3C | Processing multiomic scHi-C | Trims the restriction motif left at each sticky-end junction, which aligners multimap to both loci | ([[10-Summaries/galasso-2026-map3c\|map3C]]) |
| HiCFoundation | Enhancement | Fine-tuned from bulk Hi-C pretraining | ([[10-Summaries/wang-2026-hicfoundation\|HiCFoundation]]) |
| Evo2HiC | Resolution enhancement (bulk) | Sequence priors from a distilled DNA language model | ([[10-Summaries/fang-2025-evo2hic\|Evo2HiC]]) |
| SUCCEED | Contact-map prediction | Sequence model plus pseudobulk scATAC | ([[10-Summaries/sun-2026-succeed\|SUCCEED]]) |

## Evidence and examples

**Feature calling**

- Pseudobulk loop-calling approaches need >500–1,000 cells; SnapHiC calls 1,050–1,420 loops from 75 ([[10-Summaries/yu-2021-snaphic|SnapHiC]]).
- With 100 mESCs, SnapHiC-G retained 61% genome-wide power while all bulk callers and SnapHiC fell below 10% ([[10-Summaries/liu-2024-snaphic-g|SnapHiC-G]]).
- SnapHiC-G's advantage shrank in oligodendrocytes (1,038 cells, ~278 million pooled intrachromosomal contacts), where pseudo-bulk reaches bulk-like depth ([[10-Summaries/liu-2024-snaphic-g|SnapHiC-G]]).
- In single cells scNanoHi-C detects chromosome territories and 87.0% of compartment triplets, but TADs are much weaker: on average a TAD is seen in ≤60% of cells ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).
- Down-sampling Droplet Hi-C cortex neurons showed that compartment and insulation scores lose agreement below about 400 cells or 10 million long-range contacts per cell type; loop calling probably needs deeper data ([[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]).

**Embedding and normalization**

- Fast-Higashi separated cortical L2–3/L4/L5/L6 excitatory neurons from chromatin conformation alone and ran ~40× faster than 3DVI and ~9× faster than Higashi ([[10-Summaries/zhang-2022-fast-higashi|Fast-Higashi]]).
- In an eight-method benchmark across four scHi-C datasets, BandNorm ranked best overall (median rank 2), followed by scVI-3D (3), Higashi (3.5) and scHiCluster (4) ([[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]).
- BandNorm runs in about 15 minutes, against hours to more than a day for the alternatives ([[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]).
- **Systematic biases in imputed scHi-C are negligible**: normalisation against fragment size, GC content or mappability is unnecessary, unlike bulk Hi-C — sparsity apparently swamps the systematic biases ([[10-Summaries/yu-2021-snaphic|SnapHiC]]).

**Read processing**

- map3C resolved 77–79% of SNP haplotype conflicts versus 28–29% for random SNP removal ([[10-Summaries/galasso-2026-map3c|map3C]]).
- MAPQ filtering raised the snm3C-seq intra/inter contact ratio to 3.16 from ~1.0 with TAURUS-MH or YAP and lowered 3D-model restraint violations (median 0.004 vs 0.037–0.051) ([[10-Summaries/galasso-2026-map3c|map3C]]).

**Sequence and foundation models**

- Fine-tuned from bulk Hi-C pretraining, HiCFoundation enhanced scHi-C better than Higashi, scHiCluster and scVI-3D, and when applied to human WTC11 cells without retraining it beat scHiCluster by 35.9% in Pearson correlation ([[10-Summaries/wang-2026-hicfoundation|HiCFoundation]]).
- Sequence priors from a distilled DNA language model improved resolution enhancement of 1/16-downsampled bulk Hi-C across 177 species (Evo2HiC) ([[10-Summaries/fang-2025-evo2hic|Evo2HiC]]).
- SUCCEED plus pseudobulk scATAC from ≤200 cells predicted K562 Hi-C contact maps with only modest loss in insulation-score agreement ([[10-Summaries/sun-2026-succeed|SUCCEED]]).

**Applications**

- Cell-type labels in the brain applications come from methylation, independently of contacts ([[10-Summaries/luo-2017-snmc-seq|Luo 2017]]; [[10-Summaries/lee-2019-natmethods|Lee 2019]]).

## Contested points

- **Impute or not.** SnapHiC2 imputes each cell to call loops ([[10-Summaries/li-2022-snaphic2|SnapHiC2]]), while scDIAGRAM avoids imputation entirely for compartment calling, arguing that imputation (scHiCluster, Higashi) smooths away cell-specific heterogeneity ([[10-Summaries/peng-2026-scdiagram|scDIAGRAM]]).
- **Ligation may cap what scHi-C can see.** Arrastia et al. argue that ligation-based scHi-C is limited to about 10-Mb resolution per cell and under-captures inter-chromosomal and nuclear-body contacts; in their comparison, centromere-proximal and nucleolar contacts were undetectable even in ensemble scHi-C data, while scSPRITE detected them in single cells ([[10-Summaries/arrastia-2022-scsprite|scSPRITE]]).
- **Per cell type, not per cell.** SnapHiC, scGHOST and MINTsC all assume a homogeneous cell group and report features per *cell type*, not per cell; the single-cell formulation buys statistical power but does not yet deliver per-cell feature variability ([[10-Summaries/yu-2021-snaphic|SnapHiC]]; [[10-Summaries/park-2026-mintsc|MINTsC]]) (synthesis).
- **Protocol comparisons are not depth-matched.** The Dautle 2025 re-scoring of protocols was not matched for sequencing depth ([[10-Summaries/dautle-2025-schic-review|Dautle 2025]]) (synthesis).
- **Sequence-model routes are untested on single cells.** Evo2HiC is a possible but untested route for sparse scHi-C imputation ([[10-Summaries/fang-2025-evo2hic|Evo2HiC]]), and SUCCEED, a sequence-based alternative to sparse single-cell Hi-C, was evaluated only against bulk Hi-C ([[10-Summaries/sun-2026-succeed|SUCCEED]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/topologically-associating-domain|Topologically associating domain]] — Sub-megabase contact domains that vary between single cells.
> - `concept` [[30-Concepts/chromatin-compartments|Chromatin compartments]] — A/B compartments and subcompartments called from contact maps.
> - `hub` [[40-Topics/3d-genome|3D genome]] — Chromatin folding measured by bulk and single-cell contact assays.

## All sources on this page

> [!info]- 25 summaries cited here
> - [[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]
> - [[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]
> - [[10-Summaries/dautle-2025-schic-review|Dautle 2025]]
> - [[10-Summaries/fang-2025-evo2hic|Evo2HiC 2025]]
> - [[10-Summaries/galasso-2026-map3c|Galasso 2026]]
> - [[10-Summaries/hong-2025-sc3d-genome-review|Hong 2025]]
> - [[10-Summaries/jiang-2026-stark-scnucleome|Jiang 2026]]
> - [[10-Summaries/lee-2019-natmethods|Lee 2019]]
> - [[10-Summaries/li-2022-snaphic2|Li 2022]]
> - [[10-Summaries/li-2023-scnanohi-c|Li 2023]]
> - [[10-Summaries/lieberman-aiden-2009-hic|Lieberman-Aiden 2009]]
> - [[10-Summaries/liu-2024-snaphic-g|Liu 2024]]
> - [[10-Summaries/luo-2017-snmc-seq|Luo 2017]]
> - [[10-Summaries/park-2026-mintsc|Park 2026]]
> - [[10-Summaries/peng-2026-scdiagram|Peng 2026]]
> - [[10-Summaries/ramani-2017-scihi-c|Ramani 2017]]
> - [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]
> - [[10-Summaries/sun-2026-succeed|SUCCEED 2026]]
> - [[10-Summaries/wang-2026-hicfoundation|HiCFoundation 2026]]
> - [[10-Summaries/xiong-2024-scghost|Xiong 2024]]
> - [[10-Summaries/yu-2021-snaphic|Yu 2021]]
> - [[10-Summaries/zhang-2022-fast-higashi|Zhang 2022]]
> - [[10-Summaries/zhang-2022-higashi|Zhang 2022]]
> - [[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]
> - [[10-Summaries/zhou-2019-schicluster|Zhou 2019]]
