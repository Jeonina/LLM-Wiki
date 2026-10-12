---
type: concept
title: DOGMA-seq
aliases: [DOGMA]
tags: [single-cell, multi-omics, scATAC-seq, scRNA-seq, surface-protein, method]
created: 2026-05-07
updated: 2026-10-12
---

# DOGMA-seq

> Multi-omic single-cell platform that simultaneously measures chromatin accessibility (scATAC-seq), gene expression (scRNA-seq), and cell-surface protein abundance (CITE-seq style antibody-derived tags) in the same cell; imputation-based integration with GoT–ChA extends it to four modalities ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

> [!abstract] 한눈에
> DOGMA-seq는 한 세포에서 chromatin accessibility, RNA, 표면 단백질을 함께 재는 trimodal 방법이다. GoT–ChA 데이터와 mitochondrial 변이·표면 단백질을 다리로 삼아 imputation으로 연결하면 genotype까지 네 modality를 얻지만, 이는 직접 co-capture가 아니다 ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Definition

A trimodal extension of scATAC + scRNA + protein measurement on droplet platforms, providing three orthogonal phenotype layers per cell. In [[10-Summaries/izzo-2024-got-cha|Izzo 2024]], DOGMA-seq is integrated with [[got-cha|GoT–ChA]] via imputation — using mitochondrial variants and surface protein patterns as bridges between cells profiled with GoT–ChA (genotype + chromatin) and DOGMA cells (chromatin + RNA + protein) — to recover **all four modalities** (genotype + chromatin + RNA + protein) per cell ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Why it matters

Each phenotype layer answers a different question: chromatin = regulatory potential, RNA = expressed program, protein = functional/lineage state. Integrated with genotype (via [[got-cha|GoT–ChA]]), DOGMA-seq turns single-cell genomics into a four-modality analysis where you can ask: *of cells with this mutation, which surface phenotype is enriched, what gene programs do they express, and which regulatory elements are open?* ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]])

## Variants

- **Imputation-based GoT–ChA + DOGMA integration** — uses mt-variants + surface proteins as bridges; not direct co-capture ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).
- **Direct trimodal DOGMA-seq** protocols exist independently of GoT–ChA.

## Evidence and examples

- JAK2V617F MPN samples profiled with GoT–ChA were extended via imputation to DOGMA modalities, enabling joint genotype × chromatin × RNA × surface-protein analysis ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Contested points

- The imputation bridge depends on having informative mitochondrial variants and discriminating surface proteins. Generalization to systems lacking both is unclear ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]] open question).

## Related

> [!cards]
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Droplet method capturing somatic genotype and chromatin accessibility from the same nucleus.
> - `concept` [[30-Concepts/chromatin-accessibility|Chromatin accessibility]] — Whether a region of DNA is open or closed to regulatory machinery.
> - `hub` [[40-Topics/single-cell-multiomics|Single-cell multi-omics]] — Methods that measure two or more modalities in the same cell.

## All sources on this page

> [!info]- 1 summaries cited here
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
