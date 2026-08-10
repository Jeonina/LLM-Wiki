---
type: concept
title: Trajectory Inference
aliases: [pseudotime, pseudotemporal ordering, lineage trajectory, RNA velocity]
tags: [trajectory, pseudotime, PAGA, Monocle, development]
created: 2026-08-10
updated: 2026-08-10
---

# Trajectory Inference

> Ordering cells along a continuous process — differentiation, dose response, disease progression — rather than partitioning them into discrete groups. A snapshot population is treated as a sampling of a process, with position along the manifold standing in for time.

## The problem with trees

Biological processes are usually **incompletely sampled**, so the data do not conform to a connected manifold and modelling them as a continuous tree "has little meaning" ([[wolf-2019-paga]]). Clustering-based tree algorithms additionally assume clusters conform to a connected tree topology, and rely on feature-space inter-cluster distances that are only locally valid ([[wolf-2019-paga]]).

## Graph abstraction

PAGA partitions a kNN graph and builds a coarse graph whose edge weights measure connectivity between partitions — modularity-like, treating groups as connected when inter-partition edges exceed random expectation — so weak edges can be discarded and **genuinely disconnected regions can be reported as disconnected** ([[wolf-2019-paga]]). Cells are then ordered within partitions by a random-walk distance from a root, and a PAGA path averages the ensemble of single-cell paths through those groups, which is what supplies statistical power ([[wolf-2019-paga]]).

## Topology claims are sampling claims

The disputed origin of basophils resolves differently in three hematopoiesis datasets: one supports a basophil-neutrophil-monocyte progenitor, one a shared erythroid-megakaryocyte-basophil progenitor, and the largest and most densely sampled shows **both trajectories** ([[wolf-2019-paga]]). Sampling density, not method, determined the answer (synthesis).

## At atlas scale

56 trajectories were identified across two million cells, many detectable only because of the depth of cellular coverage ([[cao-2019-moca]]).

## Trajectories as a reference frame

A perturbation's effect is interpretable only relative to the natural differentiation direction: the perturbation score compares a simulated knockout vector to the differentiation vector, with negative meaning the knockout blocks differentiation and positive meaning it promotes it ([[kamimoto-2023-celloracle]]).

## Caution

Proliferation and cell death are outside most trajectory frameworks, so phenotypes mediated by differential expansion rather than fate change are invisible ([[kamimoto-2023-celloracle]]).

## Related

- [[clustering-algorithms]] · [[dimensionality-reduction]] · [[lineage-tracing]] · [[computational-methods]]
