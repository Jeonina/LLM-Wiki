---
type: concept
title: scDNA-seq capabilities framework
aliases: [Evrony framework, fidelity-copresence-association framework]
tags: [framework, scDNA-seq]
created: 2026-05-11
updated: 2026-10-12
---

# scDNA-seq capabilities framework

> The Evrony / Hinch / Luo framework for organizing single-cell DNA sequencing applications around three core capabilities: **fidelity**, **co-presence**, and **phenotypic association**. Every scDNA-seq method possesses some subset of these capabilities, and every application is distinguished by which subset it requires ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]).

> [!abstract] 한눈에
> 이 framework는 scDNA-seq 응용을 fidelity, co-presence, phenotypic association이라는 세 가지 능력으로 나누고, 연구 질문이 어떤 능력을 요구하는지에 따라 방법을 고르게 한다 ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]). 다만 정성적인 틀이어서 능력을 수치로 매기는 기준은 아직 없다 (synthesis).

<!-- explainer-links -->
> [!tip] 📘 교재
> [단일세포 DNA 시퀀싱 입문](../60-Explainers/scdna-seq.html)
<!-- /explainer-links -->

## Definition

The framework names three capabilities ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]):

1. **Fidelity** — the ability to detect features (mutations, modifications, properties) at very low levels of mosaicism, below the error floor of bulk sequencing ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]). Critical for rare-variant detection, low-VAF clonal hematopoiesis, and mutational signatures in normal tissues (synthesis).
2. **Co-presence** — the ability to determine which variants co-occur in the same cell (or same molecule) ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]). Critical for clonal-lineage reconstruction, haplotype phasing of compound heterozygotes, and distinguishing trans vs cis configurations (synthesis).
3. **Phenotypic association** — the ability to link single-cell genotype to other single-cell phenotypic readouts (RNA expression, chromatin accessibility, surface protein, spatial location) ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]). Critical for the "what does this mutation do in this cell type?" class of questions (synthesis).

Different scDNA-seq technologies possess different subsets of the three capabilities, although scDNA-seq as a class is distinguished by its potential to achieve all three on a genome-wide scale ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]). Method choice should be driven by which capabilities the question requires ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]).

## Why it matters

- It separates **method properties** from **biological question** — a separation that older technology-organized reviews (e.g., [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]) collapse ([[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]).
- With the framework, a researcher can ask "I need fidelity but not co-presence" → duplex sequencing of bulk DNA; "I need all three" → [[got-cha]]-style genotype-phenotype methods (limited fidelity), [[daf-seq]]-style single-molecule methods (limited cell throughput), or paired duplex + RNA approaches still in development (synthesis).

## Methods by capability profile

| Method | Fidelity | Co-presence | Phenotypic association |
|---|---|---|---|
| [[mda]] / [[pta]] scWGA + scWGS | low–med | per-cell | none alone |
| [[40-Topics/duplex-sequencing\|Duplex sequencing]] (bulk) | high | per-molecule | none |
| [[meta-cs]] | high | per-cell | none alone |
| [[got]] | med | per-cell | RNA |
| [[got-cha]] | med | per-cell | chromatin |
| D&D-GoT-ChA ([[dd-seq]]) | med | per-cell | TF binding (+ accessibility) |
| [[resolveome]] | med–high (PTA) | per-cell | RNA (genome-wide genotype) |
| [[daf-seq]] (single-cell) | high | per-fiber | sequence + chromatin |

The capability ratings in this table are the wiki's own placement of each method, not scores given in the review (synthesis).

## Evidence and examples

- Walsh lab brain lineage tracing requires *fidelity + co-presence* (low-VAF mutations as lineage markers, per-cell assignment for tree reconstruction); PTA + scWGS satisfies this (synthesis).
- The [[10-Summaries/izzo-2024-got-cha|Izzo 2024]] JAK2V617F chromatin-priming finding requires *fidelity (detecting the mutation) + co-presence (per-cell) + phenotypic association (chromatin profile)*; GoT–ChA satisfies all three at moderate fidelity ([[10-Summaries/izzo-2024-got-cha|Izzo 2024]]).

## Contested points

- The framework is qualitative — no quantitative "fidelity score" exists (synthesis).
- "Phenotypic association" is becoming a continuum rather than binary as multi-omic methods mature (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/scwga|scWGA]] — Whole-genome amplification of a single cell's DNA, the step that sets fidelity for most scDNA-seq.
> - `concept` [[30-Concepts/got|GoT]] — Genotyping of transcriptomes: genotype plus RNA in the same cell.
> - `concept` [[30-Concepts/got-cha|GoT–ChA]] — Genotype plus chromatin accessibility in the same cell.
> - `concept` [[30-Concepts/daf-seq|DAF-seq]] — Single-molecule sequence plus chromatin, per fiber.
> - `concept` [[30-Concepts/dd-seq|D&D-seq]] — D&D-GoT-ChA: fidelity + co-presence + TF binding.
> - `concept` [[30-Concepts/resolveome|ResolveOME]] — Genome-wide genotype plus RNA: fidelity + co-presence + RNA.
> - `hub` [[40-Topics/scdna-seq|scDNA-seq]] — The single-cell DNA sequencing field as a whole.
> - `hub` [[40-Topics/duplex-sequencing|Duplex sequencing]] — High-fidelity bulk sequencing of both DNA strands.

## All sources on this page

> [!info]- 3 summaries cited here
> - [[10-Summaries/evrony-2021-scDNA-applications-review|Evrony 2021]]
> - [[10-Summaries/gawad-2016-scgenome-review|Gawad 2016]]
> - [[10-Summaries/izzo-2024-got-cha|Izzo 2024]]
