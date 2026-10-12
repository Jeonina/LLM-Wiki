---
type: concept
title: Lineage tracing
aliases: [cell lineage tracing, lineage reconstruction, lineage tracing with somatic mutations, somatic lineage tracing, mutation-based lineage tracing]
tags: [development, lineage, single-cell, somatic-mutation, phylogeny]
created: 2026-05-11
updated: 2026-10-12
---

# Lineage tracing

> Reconstruction of the developmental ancestry of cells in a tissue — which cells descend from which progenitor, and when each lineage diverged; in humans, where engineered markers cannot be used, **endogenous somatic mutations** accumulating at ~2–4 per cell division serve as natural lineage barcodes recoverable by [[40-Topics/scdna-seq]] ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

> [!abstract] 한눈에
> Lineage tracing은 어떤 세포가 어떤 전구세포에서 나왔고 언제 갈라졌는지를 재구성하는 일이다. 사람에서는 세포 분열마다 쌓이는 체세포 변이나 mtDNA 변이를 자연 barcode로 쓰고, 모델 생물에서는 CRISPR recorder 같은 인공 barcode를 쓴다 ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]; [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [종양 계통수 시뮬레이터](../60-Explainers/cancer-clonal-evolution.html)
>
> [단일세포 계통 추적](../60-Explainers/single-cell-lineage-tracing.html)
>
> [체세포 모자이크](../60-Explainers/somatic-mosaicism.html)
<!-- /explainer-links -->

## Definition

There are two strategies:

1. **Engineered markers** (model organisms): fluorescent reporters, Cre recombinase, CRISPR-introduced scarring (GESTALT, scGESTALT, ScarTrace). Powerful, but they require genetic manipulation and are not applicable to humans.
2. **Endogenous mutation accumulation** (humans and model organisms): natural somatic SNVs and structural variants accumulating at known rates serve as cellular barcodes, detected post hoc by single-cell genome sequencing ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]; [[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]).

The modern taxonomy splits approaches into prospective vs retrospective and static vs evolvable barcodes ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).

## Why it matters

Lineage tracing answers questions inaccessible to bulk sequencing:

- When did the progenitors of brain region X diverge from region Y?
- Which adult tissue cells descend from which embryonic clone?
- What is the clonal architecture of a tumor, and how did it evolve?

In humans, lineage tracing from endogenous mutations is one of the major motivations for [[40-Topics/scdna-seq]] advancement ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).

## Approaches

| Approach | Marker | Readout | Notes | Source |
|---|---|---|---|---|
| Synthetic static barcodes | Lentiviral, recombinase or transposase barcodes | — | Prospective; see [[30-Concepts/crispr-lineage-recording]] for evolvable recorders | ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review\|Rodriguez-Fraticelli 2026]]) |
| Expressed lentiviral barcodes (LARRY) | Random 28-mer in an eGFP 3′ UTR | scRNA-seq | Links early transcriptional state to later clonal fate | ([[10-Summaries/weinreb-2020-larry\|LARRY]]) |
| Evolvable CRISPR recorders | Heritable Cas9 edits | — | Inference side supplied by Cassiopeia | ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review\|Rodriguez-Fraticelli 2026]]; [[10-Summaries/jones-2020-cassiopeia\|Cassiopeia]]) |
| Endogenous mtDNA variants | Somatic mtDNA mutations | ATAC-seq or scRNA-seq, no enrichment step | See [[30-Concepts/mitochondrial-lineage-tracing]] | ([[10-Summaries/ludwig-2019-mtdna-lineage-tracing\|Ludwig 2019]]) |
| Bulk colony or microdissection | Somatic point mutations | Sequencing many clonal colonies; phylogeny from shared variants | — | ([[10-Summaries/lee-six-2018-hsc-dynamics\|Lee-Six 2018]]) |
| Single-cell whole genome | Somatic SNVs, indels, CNVs | scDNA-seq with PTA amplification and duplex validation | Slower but unbiased; preferred when lineage markers are unknown a priori | ([[10-Summaries/luquette-2025-pta-duplex-mosaicism\|Luquette 2025]]) |
| Targeted sequencing of lineage-informative loci | Known informative variants | Targeted panel | Cheaper; allows thousands of cells (e.g. leukemia lineage studies) | ([[10-Summaries/shao-2025-scDNA-mosaicism-review\|Shao 2025]]) |
| Copy number rather than point mutations | Single-cell CNA profiles | scDNA-seq | Minimal event distance; explicitly abandons the infinite-sites assumption that aneuploid genomes violate | ([[10-Summaries/wang-2021-medalt\|MEDALT]]) |
| Combined with single-cell phenotype | Any of the above | scRNA-seq, surface protein | Maps lineage onto cell type — the "phenotypic association" capability | ([[10-Summaries/evrony-2021-scDNA-applications-review\|Evrony 2021]]) |
| Multimodal genotype + state | Somatic variants | DEFND-seq, SDR-seq | Feeds the phylogenetic-inference algorithms reviewed by Wang et al. | ([[10-Summaries/olsen-2025-defnd-seq\|DEFND-seq]]; [[10-Summaries/lindenhofer-2025-sdr-seq\|SDR-seq]]; [[10-Summaries/wang-2026-multimodal-lineage-computational\|Wang 2026]]) |

Methylation epimutations are a further endogenous marker; see [[30-Concepts/methylation-clones-epimutation]].

### Retrospective tracing from somatic mutations

Every cell division carries some probability of introducing a unique SNV, indel or CNV that is inherited by daughter cells, so deep sequencing of clonal expansions recovers a phylogeny ([[10-Summaries/coorens-2021-nature|Coorens 2021]]; [[10-Summaries/lee-six-2018-hsc-dynamics|Lee-Six 2018]]). This works in any human tissue but requires sensitive variant calling, PTA plus duplex, for sparse expansions ([[10-Summaries/luquette-2025-pta-duplex-mosaicism|Luquette 2025]]).

For endogenous mutation-based tracing in humans, the workflow typically:

- Performs [[scwga]] (often [[pta]]) + scWGS on a sample of cells.
- Identifies lineage-informative variants (those shared among subsets of cells).
- Genotypes those variants in a larger panel of cells via targeted sequencing.
- Reconstructs a phylogenetic tree.

Tree-building algorithms for per-cell variant matrices include SCITE ([[10-Summaries/jahn-2016-scite|SCITE]]), SiFit ([[10-Summaries/zafar-2017-sifit|SiFit]]) and SCARLET ([[10-Summaries/satas-2020-scarlet|SCARLET]]); see [[30-Concepts/phylogenetic-inference]].

## Evidence and examples

**Established applications of somatic-mutation phylogenies**

- Human developmental phylogeny ([[10-Summaries/coorens-2021-nature|Coorens 2021]]).
- Hematopoietic stem cell dynamics ([[10-Summaries/lee-six-2018-hsc-dynamics|Lee-Six 2018]]).
- Cancer clonal evolution from copy-number lineages ([[10-Summaries/wang-2021-medalt|MEDALT]]).
- Mapping human cortical neuron lineage with PTA-based scWGS to track the timing of brain-region divergence ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- Identifying the divergence of inhibitory vs excitatory neuron progenitors in development ([[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]).
- Leukemia clonal evolution by targeted sequencing of driver loci in thousands of cells.

**Endogenous mtDNA barcodes**

- mtDNA is a 16.6 kb genome with a 10–100× higher mutation rate than nuclear DNA and 100–1,000s of copies per cell, so variants drift to high heteroplasmy and become robustly detectable at shallow depth ([[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]).
- ATAC-seq covers mtDNA at 3,380-fold per million mapped reads with no enrichment step ([[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]).
- Against a constructed 65-subclone tree, mtDNA variants gave 96% MRCA accuracy between first-generation clones and 79% within sub-clones, and against lentiviral barcodes an AUROC of 0.96 ([[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]).
- mtDNA variants **outperform scRNA-inferred CNVs as a clonality measure** ([[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]).

**Expressed barcodes linking state to fate**

- Across >300,000 haematopoietic cells, LARRY sister cells shared fate far more than transcriptionally similar cells (70% identical fate combinations in split wells vs 22% by chance), implying a heritable fate bias not captured by scRNA-seq ([[10-Summaries/weinreb-2020-larry|LARRY]]).
- The best early fate prediction from expression was 60% in vitro and 51% in vivo ([[10-Summaries/weinreb-2020-larry|LARRY]]).

## Contested points

- **Missing data distorts trees.** Lineage trees from low-coverage scWGA suffer from missing-data artifacts that distort topology; Jaccard distance (binary) is favored by the Quake group, and model-based clustering with EM is an alternative.
- **Missing data is not one thing.** In recorder-based tracing it splits into *heritable* dropout (a resection removing a target site, or silencing — itself lineage information, shared by descendants) and *stochastic* dropout (failed capture — noise); treating them identically discards signal and manufactures false relationships ([[10-Summaries/jones-2020-cassiopeia|Cassiopeia]]). The same distinction plausibly applies to scWGA allelic dropout, and no source in this corpus makes it there (synthesis).
- **Homoplasy is the hard floor.** If the same character state arises independently in two branches, no inference algorithm can separate shared ancestry from convergence; the fix is assay design — more possible states per site — not better trees ([[10-Summaries/jones-2020-cassiopeia|Cassiopeia]]).
- **The clock is uncertain.** The mutation rate per division is itself uncertain by ~2× across tissues.

## Related

> [!cards]
> - `concept` [[30-Concepts/crispr-lineage-recording|CRISPR lineage recording]] — Prospective, evolvable recorders that accumulate heritable Cas9 edits.
> - `concept` [[30-Concepts/phylogenetic-inference|Phylogenetic inference]] — Reconstructing a cell-division tree from heritable markers.
> - `concept` [[30-Concepts/mitochondrial-lineage-tracing|Mitochondrial lineage tracing]] — Somatic mtDNA mutations as natural barcodes.
> - `concept` [[30-Concepts/methylation-clones-epimutation|Methylation clones and epimutation]] — Heritable CpG methylation changes as endogenous lineage markers.
> - `concept` [[30-Concepts/scwga|scWGA]] — Amplifying a single cell's genome for whole-genome sequencing.
> - `concept` [[30-Concepts/pta|PTA]] — Primary template amplification, the usual scWGA for somatic lineage work.
> - `concept` [[30-Concepts/scdna-capabilities-framework|scDNA-seq capabilities framework]] — Fidelity, co-presence and phenotypic association.
> - `hub` [[40-Topics/scdna-seq|Single-cell DNA sequencing]] — Technologies that interrogate the DNA of single cells.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one organism.
> - `hub` [[40-Topics/single-cell-lineage-tracing|Single-cell lineage tracing]] — Methods and algorithms that reconstruct the ancestry of individual cells.

## All sources on this page

> [!info]- 16 summaries cited here
> - [[10-Summaries/coorens-2021-nature|Coorens 2021]]
> - [[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]
> - [[10-Summaries/jahn-2016-scite|Jahn 2016]]
> - [[10-Summaries/jones-2020-cassiopeia|Jones 2020]]
> - [[10-Summaries/lee-six-2018-hsc-dynamics|Lee-Six 2018]]
> - [[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]
> - [[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]
> - [[10-Summaries/luquette-2025-pta-duplex-mosaicism|Luquette 2025]]
> - [[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]
> - [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]
> - [[10-Summaries/satas-2020-scarlet|Satas 2020]]
> - [[10-Summaries/shao-2025-scDNA-mosaicism-review|Shao 2025]]
> - [[10-Summaries/wang-2021-medalt|Wang 2021]]
> - [[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]
> - [[10-Summaries/weinreb-2020-larry|Weinreb 2020]]
> - [[10-Summaries/zafar-2017-sifit|Zafar 2017]]
