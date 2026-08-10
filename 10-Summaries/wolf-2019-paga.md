---
type: summary
title: "Wolf et al. 2019 — PAGA: graph abstraction reconciles clustering with trajectory inference"
source: "[[00-Sources/papers/PAGA_ graph abstraction reconciles clustering with trajectory inference through a topology preserving map of single cells]]"
source_kind: paper
author: "F. Alexander Wolf, Fiona K. Hamey, Mireya Plass, Jordi Solana, Joakim S. Dahlin, Berthold Göttgens, Nikolaus Rajewsky, Lukas Simon, Fabian J. Theis (corresponding)"
published: 2019-03-19
ingested: 2026-08-10
doi: "10.1186/s13059-019-1663-x"
journal: "Genome Biology"
tags: [PAGA, trajectory-inference, graph-abstraction, topology, Louvain, hematopoiesis, planaria, scanpy]
entities: ["[[fabian-theis]]"]
concepts: ["[[trajectory-inference]]", "[[clustering-algorithms]]", "[[dimensionality-reduction]]", "kNN graph", "[[trajectory-inference]]"]
topics: ["[[computational-methods]]", "[[single-cell-lineage-tracing]]"]
---

**Citation:** Wolf et al. (2019) — *PAGA: graph abstraction reconciles clustering with trajectory inference through a topology preserving map of single cells* — *Genome Biology* 20, 59. [DOI](https://doi.org/10.1186/s13059-019-1663-x)

# Wolf 2019 — PAGA

> Clustering assumes discrete groups; trajectory inference assumes a connected manifold. PAGA refuses the choice: partition the kNN graph, then build a coarse graph whose **nodes are partitions and whose edge weights are a statistical measure of connectivity** between them. Weak edges are discarded as noise, so the result shows both which regions are connected *and* which are genuinely disconnected.

## Key claims

- **The problem with tree-fitting.** Biological processes are usually **incompletely sampled**, so the data do not form a connected manifold and modelling them as a continuous tree "has little meaning." Clustering-based tree algorithms make the generally invalid assumption that clusters conform to a connected tree topology, and they rely on feature-space inter-cluster distances (e.g. Euclidean distance between cluster means) which quantify biological similarity only **locally** and break down for cluster-scale objects. Sampling-based fixes have had only limited success.
- **The connectivity statistic**, modularity-like: two partitions are connected if their number of inter-partition edges exceeds what is expected under random assignment. The weight reads as **confidence in the presence of an actual connection**, which is what licenses discarding low-weight edges as noise.
- **Multi-resolution by construction**: varying the partition resolution produces PAGA graphs at multiple scales, enabling hierarchical exploration. Partitions usually come from Louvain but can come from any clustering or from experimental annotation.
- **Averaging over path ensembles.** Tracing single-cell paths individually has too little statistical power; PAGA follows high-confidence paths through the abstracted graph and orders cells within each partition by a random-walk distance from a root cell, so a PAGA path averages all single-cell paths through those groups. The random-walk distance was extended to handle **disconnected graphs**.
- **PAGA-initialized manifold learning.** The near-free coarse embedding initializes UMAP or ForceAtlas2, giving embeddings **faithful to global topology** and converging about **six times faster**. The authors introduce a cost function, KL_geo, incorporating geodesic distance in both high-dimensional and embedding space, to quantify that faithfulness.
- **Consistency across four hematopoiesis datasets** of very different protocols and sizes (2,730 MARS-seq; 1,654 Smart-seq2; 44,802 10X; plus simulation). PAGA graphs recover known features — megakaryocyte/erythroid progenitor proximity, monocyte/neutrophil progenitor connection — and consistent sequential activation of erythroid (*Gata2*, *Gata1*, *Klf1*, *Epor*, *Hba-a2*), neutrophil (*Elane*, *Cepbe*, *Gfi1*) and monocyte (*Irf8*, *Csf1r*, *Ctsg*) markers.
- **The basophil-origin case is used as an honest test.** Whether basophils arise from a basophil-neutrophil-monocyte progenitor or a shared erythroid-megakaryocyte-basophil progenitor is disputed; PAGA on the Paul data shows the former, on Nestorowa the latter, and on the largest and most densely sampled dataset (Dahlin) **both trajectories** — the discrepancy attributed to insufficient sampling in the smaller studies.
- Also applied to whole adult planaria — the first reconstruction of lineage relations for an entire adult animal — and the zebrafish embryo; benchmarked on one million neurons.

## Methods / evidence

Four hematopoietic datasets across three protocols plus simulation, two whole-organism datasets, a million-cell computational benchmark, a purpose-built topology-faithfulness metric (KL_geo), and convergence-rate measurement against established manifold-learning cost functions.

## Surprising or load-bearing bits

- **Disconnection is treated as signal, not failure.** Every tree-fitting method must return a tree, so it will connect groups that are not connected. PAGA can return a graph with genuinely separate components — which is the correct answer whenever an experiment sampled discrete cell types rather than a continuous process, i.e. most experiments.
- **The basophil result is the model for how to report an ambiguous trajectory.** Rather than picking a topology, PAGA shows the ambiguity resolving with sampling density: the same method on three datasets gives three answers, and the largest dataset shows both branches. That is strong evidence that **trajectory topology claims are sampling-limited claims**, and a standing caution for every pseudotime figure in this corpus.
- **Using PAGA to initialize UMAP is the most widely adopted piece of this paper and the least discussed.** UMAP's layout depends on initialization; a random start can place globally distant populations adjacently. Seeding with the abstracted graph makes the global arrangement meaningful, not just the local neighbourhoods — directly relevant to [[mcinnes-2018-umap|UMAP's]] known weakness on global structure.
- **Averaging over ensembles of single-cell paths** is the statistical-power argument: a per-cell path is too noisy to interpret, and fitting a distribution over paths is intractable, so grouping first and averaging within groups is the tractable middle.
- The critique of Euclidean cluster-mean distances applies well beyond trajectory inference. Any method comparing clusters by centroid distance in an expression or PCA space inherits the same local-validity problem.

## Entities mentioned

- [[fabian-theis]] — corresponding author; the Scanpy ecosystem, of which PAGA is a core component.

## Concepts touched

- [[trajectory-inference]] — PAGA unifies it with clustering rather than treating them as alternatives.
- kNN graph — the shared substrate for clustering, trajectory and embedding.

## Connections to other sources

- Partitioning via [[traag-2019-leiden]] (Leiden, the improved successor to the Louvain algorithm used here).
- Embeddings it initializes: [[mcinnes-2018-umap]].
- Alternative trajectory framework on atlas-scale data: [[cao-2019-moca]] (Monocle 3).
- Upstream integration: [[korsunsky-2019-harmony]], [[hao-2024-seurat-v5]].

## Open questions

- **The connectivity threshold is a user choice.** Discarding "low-weight" edges converts a continuous confidence into a binary topology, and the paper gives a statistical interpretation but no principled cutoff — so the reported topology remains partly a parameter.
- Whether an inferred connection reflects a real differentiation transition or merely transcriptional similarity between unrelated states is not decidable from the graph alone; the basophil case shows this is a live concern rather than a theoretical one.

## Related

- [[trajectory-inference]] · [[traag-2019-leiden]] · [[mcinnes-2018-umap]] · [[single-cell-lineage-tracing]]
