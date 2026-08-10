---
type: summary
title: "Traag, Waltman & van Eck 2019 — From Louvain to Leiden: guaranteeing well-connected communities"
source: "[[00-Sources/papers/From Louvain to Leiden_ guaranteeing well-connected communities]]"
source_kind: paper
author: "V. A. Traag, L. Waltman, N. J. van Eck (Centre for Science and Technology Studies, Leiden University)"
published: 2019-03-26
ingested: 2026-08-10
doi: "10.1038/s41598-019-41695-z"
journal: "Scientific Reports"
tags: [Leiden, Louvain, community-detection, clustering, modularity, CPM, algorithm, computational-tool]
entities: []
concepts: ["[[scanpy]]", "[[episcanpy]]", "[[k-medoids]], [[jaccard-similarity]]"]
topics: ["[[single-cell-multiomics]]", "[[single-cell-atac-seq]]"]
---

**Citation:** Traag, Waltman & van Eck (2019) — *From Louvain to Leiden: guaranteeing well-connected communities* — *Scientific Reports* 9, 5233. [DOI](https://doi.org/10.1038/s41598-019-41695-z)

# Traag 2019 — Leiden

> The Louvain algorithm — the default clustering method across single-cell genomics — can return communities that are **internally disconnected**, and iterating it makes this worse. Leiden adds a refinement phase that provably guarantees connectivity, converges to subset-optimal partitions, and runs faster.

## Key claims

- **The defect**: a node acting as a bridge within its community can be moved elsewhere, disconnecting the community it left. The remaining nodes may still be locally optimally assigned, so nothing repairs it — and once the network is aggregated, the disconnected community becomes a single node and can never be split.
- The problem is not the resolution limit. It occurs under CPM (which has no resolution limit) as well as modularity.
- **Empirically severe**: up to **25% badly connected** and up to **16% disconnected** communities. In first-iteration Louvain: 23% (Amazon), 16% (DBLP), 14% (Web UK) badly connected; ~1% disconnected typically, but >5% for the Web of Science network.
- **Iterating Louvain makes it worse.** The second iteration shows a large jump in disconnected communities — nearly tenfold in some networks, reaching 16% for DBLP — even though modularity increases. Iterating Louvain is "a double-edged sword: it improves the partition in some way, but degrades it in another way."
- Louvain's only guarantee in standard form is γ-separation (no communities can be merged); iterating adds node optimality. Neither implies connectivity.
- **Leiden adds a refinement phase** between local moving and aggregation: within each community of the coarse partition, nodes are merged into subcommunities, with the target community chosen *randomly* (probability increasing with quality gain, controlled by θ ≈ 0.01) rather than greedily. The aggregate network is built from the refined partition while the initial assignment comes from the unrefined one.
- Randomness is not decoration — the paper proves greedy merging cannot reach some optimal partitions, whereas randomized merging (still excluding quality-decreasing moves) can.
- Guarantee ladder: after each iteration, all communities are γ-separated **and γ-connected**; after a stable iteration, all nodes locally optimal and all communities subpartition-γ-dense; on convergence, all communities uniformly γ-dense and **subset optimal** (no subset can be moved).
- Unlike Louvain, Leiden can keep improving *after* a stable iteration.
- **Fast local move**: a queue visits only nodes whose neighbourhood changed, rather than re-sweeping all nodes.
- Speed: 2–20× faster on empirical networks (20× on Web UK, 11× on Web of Science); 10–100× on large benchmark networks. Worst benchmark case (μ = 0.9, n = 10⁷): Louvain ~2.5 days, Leiden <10 minutes.
- Honest detail: **in the first iteration Leiden has a higher badly-connected percentage than Louvain.** The advantage begins at iteration two and grows; convergence eliminates the problem.

## Methods / evidence

Formal proofs (relegated to supplementary), LFR-style benchmark networks (n = 10³–10⁷, ⟨k⟩ = 10, community size 50, varying mixing parameter μ), and six empirical networks (Amazon, DBLP, IMDB, Live Journal, Web of Science, Web UK). Badly-connected communities are counted by running Leiden on each Louvain community as a subnetwork — a **lower bound**, since failure to split does not prove a split is impossible.

## Surprising or load-bearing bits

- **Why this belongs in a single-cell wiki:** Leiden is the clustering step in Scanpy, Seurat, [[granja-2021-archr|ArchR]], [[zhang-2024-snapatac2|SnapATAC2]], [[stuart-2021-natmethods|Signac]], [[danese-2021-episcanpy|EpiScanpy]] and — per its own README — [[tickle-2019-infercnv|inferCNV]]'s tumor subclustering. When a paper says "cells were clustered at resolution 0.5," this is the algorithm and γ is that resolution.
- The authors' own consequence statement transfers directly: in biological networks "nodes in a community are often assumed to share similar functions," so badly connected communities "may lead to incorrect attributions of shared functionality." Substitute *cell type* for *function* and this is the single-cell failure mode — a cluster that is internally disconnected in the kNN graph is not one cell state.
- **A "cell type" from Louvain could be two populations connected only through cells outside the cluster.** Nothing in a UMAP would reveal this; the defect lives in the graph, not the embedding. This is a concrete argument for reporting the clustering algorithm, not just the resolution.
- The finding that iteration *aggravates* the problem is counterintuitive and matters because pipelines routinely iterate for stability.
- Both quality functions are resolution-parameterized, so **cluster count is a chosen quantity, not a discovered one** — the honest framing of "how many cell types are there."

## Concepts touched

- Underpins clustering in [[scatac-seq]], [[scbs-seq]] and [[single-cell-hi-c]] analysis alike — modality-agnostic, like [[mcinnes-2018-umap|UMAP]], and equally under-examined.
- Pairs with UMAP as the standard display/partition split: Leiden decides membership on the kNN graph, UMAP only draws it.
- [[jaccard-similarity]] — the edge weights in single-cell kNN graphs are typically Jaccard-refined, which changes what "well connected" means in practice.

## Connections to other sources

- Consumed by [[granja-2021-archr]], [[zhang-2024-snapatac2]], [[stuart-2021-natmethods]], [[hao-2024-seurat-v5]], [[danese-2021-episcanpy]], [[fang-2021-snapatac]].
- [[mcinnes-2018-umap]] is its display-layer counterpart; [[heumos-2023-best-practices]] covers clustering-parameter practice.
- The clustering-stability question recurs in [[luo-2024-scatac-benchmark]] and [[xiao-2024-multiomics-benchmark]].

## Open questions

- **Sparse binary epigenomic kNN graphs are not the networks benchmarked here** (Amazon, DBLP, web graphs). Whether the 14–25% badly-connected rate holds, is worse, or is milder on scATAC/scBS graphs is untested anywhere in this corpus — and it directly affects confidence in published cell-type calls.
- Neither benchmark nor empirical analysis addresses how connectivity guarantees interact with the very low graph density typical of single-cell epigenomic data.

## Related

- [[mcinnes-2018-umap]] · [[heumos-2023-best-practices]] · [[scanpy]] · [[single-cell-atac-seq]]
