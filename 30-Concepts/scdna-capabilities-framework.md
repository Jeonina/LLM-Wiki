---
type: concept
title: scDNA-seq capabilities framework
aliases: [Evrony framework, fidelity-copresence-association framework]
tags: [framework, scDNA-seq]
created: 2026-05-11
updated: 2026-06-26
---

# scDNA-seq capabilities framework

> The Evrony / Hinch / Luo framework for organizing single-cell DNA sequencing applications around three core capabilities: **fidelity**, **co-presence**, and **phenotypic association**. Every scDNA-seq method possesses some subset of these capabilities, and every application is distinguished by which subset it requires ([[10-Summaries/evrony-2021-scDNA-applications-review]]).

## Definition

**1. Fidelity** — the ability to detect features (mutations, modifications, properties) at very low levels of mosaicism, below the error floor of bulk sequencing. Critical for rare-variant detection, low-VAF clonal hematopoiesis, mutational signatures in normal tissues.

**2. Co-presence** — the ability to determine which variants co-occur in the same cell (or same molecule). Critical for clonal-lineage reconstruction, haplotype phasing of compound heterozygotes, distinguishing trans vs cis configurations.

**3. Phenotypic association** — the ability to link single-cell genotype to other single-cell phenotypic readouts (RNA expression, chromatin accessibility, surface protein, spatial location). Critical for the "what does this mutation do in this cell type?" class of questions.

No method achieves all three at genome-wide scale. Method choice should be driven by which capabilities the question requires.

## Why it matters

It separates **method properties** from **biological question** — a separation that older technology-organized reviews (e.g., [[10-Summaries/gawad-2016-scgenome-review]]) collapse. With the framework, a researcher can ask "I need fidelity but not co-presence" → duplex sequencing of bulk DNA; "I need all three" → [[got-cha]]-style genotype-phenotype methods (limited fidelity), [[daf-seq]]-style single-molecule methods (limited cell throughput), or paired duplex + RNA approaches still in development.

## Variants and refinements

Methods organized by capability profile:

| Method | Fidelity | Co-presence | Phenotypic association |
|---|---|---|---|
| [[mda]] / [[pta]] scWGA + scWGS | low–med | per-cell | none alone |
| [[30-Concepts/duplex-sequencing]] (bulk) | high | per-molecule | none |
| [[meta-cs]] | high | per-cell | none alone |
| [[got]] | med | per-cell | RNA |
| [[got-cha]] | med | per-cell | chromatin |
| D&D-GoT-ChA ([[dd-seq]]) | med | per-cell | TF binding (+ accessibility) |
| [[resolveome]] | med–high (PTA) | per-cell | RNA (genome-wide genotype) |
| [[daf-seq]] (single-cell) | high | per-fiber | sequence + chromatin |

## Contested points

- The framework is qualitative — no quantitative "fidelity score" exists.
- "Phenotypic association" is becoming a continuum rather than binary as multi-omic methods mature.

## Examples

- Walsh lab brain lineage tracing requires *fidelity + co-presence* (low-VAF mutations as lineage markers, per-cell assignment for tree reconstruction). PTA + scWGS satisfies this.
- [[10-Summaries/izzo-2024-got-cha]] JAK2V617F chromatin-priming finding requires *fidelity (detecting the mutation) + co-presence (per-cell) + phenotypic association (chromatin profile)*. GoT–ChA satisfies all three at moderate fidelity.

## Related

- [[30-Concepts/scdna-seq]]
- [[30-Concepts/duplex-sequencing]]
- [[scwga]]
- [[got]], [[got-cha]], [[daf-seq]]
- [[dd-seq]] — D&D-GoT-ChA (fidelity + co-presence + TF binding)
- [[resolveome]] — genome-wide genotype + RNA (fidelity + co-presence + RNA)
- [[40-Topics/scdna-seq]]
