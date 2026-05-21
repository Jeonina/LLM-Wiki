---
type: concept
title: DOGMA-seq
aliases: [DOGMA]
tags: [single-cell, multi-omics, scATAC-seq, scRNA-seq, surface-protein, method]
created: 2026-05-07
updated: 2026-05-07
---

# DOGMA-seq

> Multi-omic single-cell platform that simultaneously measures chromatin accessibility (scATAC-seq), gene expression (scRNA-seq), and cell-surface protein abundance (CITE-seq style antibody-derived tags) in the same cell.

## Definition

A trimodal extension of scATAC + scRNA + protein measurement on droplet platforms. Provides three orthogonal phenotype layers per cell. In [[10-Summaries/izzo-2024-got-cha]], DOGMA-seq is integrated with [[got-cha]] via imputation — using mitochondrial variants and surface protein patterns as bridges between cells profiled with GoT–ChA (genotype + chromatin) and DOGMA cells (chromatin + RNA + protein) — to recover **all four modalities** (genotype + chromatin + RNA + protein) per cell.

## Why it matters

Each phenotype layer answers a different question: chromatin = regulatory potential, RNA = expressed program, protein = functional/lineage state. Integrated with genotype (via [[got-cha]]), DOGMA-seq turns single-cell genomics into a four-modality analysis where you can ask: *of cells with this mutation, which surface phenotype is enriched, what gene programs do they express, and which regulatory elements are open?*

## Variants and refinements

- **Imputation-based GoT–ChA + DOGMA integration** ([[10-Summaries/izzo-2024-got-cha]]) — uses mt-variants + surface proteins as bridges; not direct co-capture.
- Direct trimodal DOGMA-seq protocols exist independently of GoT–ChA.

## Contested points

- The imputation bridge depends on having informative mitochondrial variants and discriminating surface proteins. Generalization to systems lacking both is unclear ([[10-Summaries/izzo-2024-got-cha]] open question).

## Examples

- JAK2V617F MPN samples profiled with GoT–ChA were extended via imputation to DOGMA modalities, enabling joint genotype × chromatin × RNA × surface-protein analysis ([[10-Summaries/izzo-2024-got-cha]]).

## Related

- [[got-cha]]
- [[chromatin-accessibility]]
- [[40-Topics/single-cell-multiomics]]
