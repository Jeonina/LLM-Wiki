---
type: summary
title: "Guo et al. 2013 — scRRBS: single-cell methylome landscapes of mouse ESCs and early embryos"
source: "[[00-Sources/papers/Single-cell methylome landscapes of mouse embryonic stem cells and early embryos analyzed using reduced representation bisulfite sequencing]]"
source_kind: paper
author: "Hongshan Guo, Ping Zhu, Xinglong Wu, Xianlong Li, Lu Wen, Fuchou Tang (corresponding)"
published: 2013-12-02
ingested: 2026-05-18
ingest_depth: abstract+full-intro
doi: "10.1101/gr.161679.113"
journal: "Genome Research"
tags: [scRRBS, single-cell-methylome, reduced-representation-bisulfite, mESC, zygote, demethylation, Tang-lab, founding-method]
entities: []
concepts:
  - "[[30-Concepts/dna-methylation]]"
  - "[[30-Concepts/bisulfite-sequencing]]"
topics:
  - "[[40-Topics/dna-methylation]]"
---

**Citation:** Guo et al. (2013) — *scRRBS: single-cell methylome landscapes of mouse ESCs and early embryos* — *Genome Research*. [DOI](https://doi.org/10.1101/gr.161679.113)

# Guo et al. 2013 — scRRBS

> Thesis: bulk bisulfite sequencing averages away cell-to-cell methylation heterogeneity. **Reduced Representation Bisulfite Sequencing adapted to single cells (scRRBS)** captures up to **1.5 million CpG sites per cell** at single-base resolution. Applied to mouse ESCs, zygotes, and early embryos, scRRBS reveals **digitized methylation status** (fully methylated vs unmethylated) at individual CpGs in haploid sperm, and resolves **maternal vs paternal demethylation dynamics** in zygote pronuclei.

## Key claims (abstract + intro)

- **scRRBS chemistry**: MspI restriction + size selection → CpG-rich fragments → bisulfite conversion → PCR + Illumina. Adaptation to single-cell input retains ~1.5M CpGs per mESC.
- **Single-base resolution** methylation calling per cell.
- **Digitized binary readout** for haploid cells (sperm): each CpG is fully methylated or fully unmethylated — no intermediate.
- **Zygote pronuclei resolved**: maternal vs paternal demethylation kinetics tracked individually. **Genic regions demethylate faster than intergenic** in both pronuclei.
- Method established as a tool for studying **dynamic methylome landscapes** during embryonic development, somatic differentiation, and tumorigenesis.

## Why this matters

One of the **founding single-cell methylome methods** (alongside scBS-seq, Smallwood 2014). Anchors the early-embryo and developmental-methylation axes of the wiki. Established that single-cell methylation can be discrete (digitized) at sufficient depth — a key conceptual point for downstream methylation-lineage methods.

## Note on ingest depth

Abstract + full introduction read; full PDF re-ingest will deepen MspI cut-density analysis and pronuclei demethylation kinetics figures.

---
**Source:** [DOI](https://doi.org/10.1101/gr.161679.113) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/24179143/)

## Related

- [[30-Concepts/dna-methylation]] · [[30-Concepts/bisulfite-sequencing]] · [[30-Concepts/scbs-seq]] · [[30-Concepts/cpg-island]]
- [[10-Summaries/smallwood-2014-natmethods]] · [[10-Summaries/zachary-2013-naturereviewsgenetics]]
- [[40-Topics/dna-methylation]]
