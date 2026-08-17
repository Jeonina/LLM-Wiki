---
type: summary
title: "Song, Su & Zhang 2021 — scGCN is a graph convolutional networks algorithm for knowledge transfer in single cell omics"
source: "[[00-Sources/papers/scGCN is a graph convolutional networks algorithm for knowledge transfer in single cell omics]]"
source_kind: paper
author: "Qianqian Song, Jing Su, Wei Zhang (corresponding)"
published: 2021-06-22
ingested: 2026-08-17
doi: "10.1038/s41467-021-24172-y"
journal: "Nature Communications 12:3826"
tags: [scGCN, graph-convolutional-network, label-transfer, knowledge-transfer, cross-modality, cross-species, benchmark]
entities: []
concepts: ["[[cell-type-annotation]]", "[[multimodal-integration-methods]]", "[[batch-effect]]", "[[convolutional-neural-network]]", "[[clustering-algorithms]]"]
topics: ["[[computational-methods]]", "[[single-cell-atac-seq]]", "[[single-cell-multiomics]]"]
---

**Citation:** Song, Su & Zhang (2021) — *scGCN is a graph convolutional networks algorithm for knowledge transfer in single cell omics* — *Nature Communications* 12, 3826. [DOI](https://doi.org/10.1038/s41467-021-24172-y)

# Song 2021 — scGCN

> Existing label-transfer methods "extract shared information from individual cells but ignore higher-order relations between cells." scGCN's premise is that the **topology of the cell–cell graph** is itself transferable knowledge, and a graph convolutional network is the natural way to use it. Benchmarked across **30 datasets** spanning tissues, platforms, species, and **molecular layers** (RNA versus ATAC).

## Key claims

- **Three obstacles to knowledge transfer are named**: single-cell technical issues (dropout, dispersion); batch effects from operators, protocols, and technical variation (mRNA quality, pre-amplification efficiency, instrument settings); and intrinsic biological variance across tissues, species, and molecular layers.
- **Higher-order cell relations are the missing information.** Seurat v3 anchors, Conos, scmap and CHETAH all operate on cell-level similarity; GCNs propagate information over the graph, capturing topological structure that pairwise similarity discards.
- **Consistently superior accuracy across 30 datasets**, including the hardest transfer setting — **across molecular layers**, i.e. transferring labels from scRNA-seq to scATAC-seq.
- **The comparator set is the label-transfer state of the art of 2021**: Seurat v3 (anchor-based), Conos (joint graph from pairwise sample alignments), scmap (maximum-similarity to annotated reference), CHETAH (top-to-bottom classification tree).
- Delivered as an integrated Python workflow.

## Methods / evidence

Benchmarking on 30 single-cell omics datasets spanning tissues, species, sequencing platforms and molecular layers, against four established label-transfer methods.

Weight: 30 datasets is a broad evaluation for a tool paper, and the inclusion of cross-modality and cross-species transfer tests the hard cases. Self-benchmarked, as usual in this literature.

## Surprising or load-bearing bits

- **Cross-modality label transfer is the demanding test**, because RNA and ATAC do not share a feature space at all — the mapping runs through gene activity scores or similar proxies, each of which imposes assumptions. Any method that survives it is doing something more than feature matching. This is the same difficulty [[argelaguet-2021-integration-principles|diagonal integration]] names as the hardest case. (synthesis)
- **"Redefining cell types from scratch in every study" is the problem all of these tools address**, from a different angle than [[kang-2021-symphony|Symphony]]: Symphony freezes a reference embedding and localises queries in it; scGCN learns a transferable classifier over graph structure. Embedding-first versus classifier-first. (synthesis)
- **Graph neural networks arrive in single-cell analysis here**, and the same architectural family later powers [[xiong-2024-scghost|scGHOST]] (graph embedding for 3D genome) and [[park-2026-mintsc|MINTsC]]'s multilayer-network formulation — the graph view of single-cell data recurs across modalities. (synthesis)
- **Label transfer is annotation outsourcing**, and it inherits every bias of the source annotation. A wrong label in the reference propagates silently at scale — a risk none of these papers quantifies. (synthesis)

## Concepts touched

- [[cell-type-annotation]] — label transfer as graph-based semi-supervised learning.
- [[multimodal-integration-methods]] — cross-modality knowledge transfer without a shared feature space.

## Connections to other sources

- Direct comparators: [[butler-2018-seurat-cca]] and its v3 anchor successor; and Conos, scmap, CHETAH (not in corpus).
- Reference-mapping alternative: [[kang-2021-symphony]].
- Integration methods that build the shared space it transfers over: [[haghverdi-2018-mnn]], [[korsunsky-2019-harmony]], [[welch-2019-liger]], [[cao-2022-glue]].
- Cross-modality integration in the harder unpaired setting: [[cao-2022-glue]], [[argelaguet-2021-integration-principles]].
- scATAC analysis targets: [[fang-2021-snapatac]], [[granja-2021-archr]], [[zhang-2024-snapatac2]].
- Graph formulations elsewhere in the corpus: [[xiong-2024-scghost]], [[park-2026-mintsc]].
- Benchmark and best practices: [[xiao-2024-multiomics-benchmark]], [[heumos-2023-best-practices]], [[luo-2024-scatac-benchmark]].

## Open questions

- **How RNA→ATAC transfer handles the gene-activity-score assumption** is the crux and is not separated out; gene activity scores are a known weak link that [[hao-2024-seurat-v5|Seurat v5 bridge integration]] was later designed to avoid.
- No uncertainty quantification on transferred labels — a transferred annotation is returned with the same confidence as a directly measured one.
- Whether GCN performance depends on graph construction choices (k, distance metric) is not reported.

## Related

- [[kang-2021-symphony]] · [[cell-type-annotation]] · [[multimodal-integration-methods]] · [[40-Topics/computational-methods]]
