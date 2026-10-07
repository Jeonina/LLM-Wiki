---
type: summary
title: "Lareau, Ludwig et al. 2021 — mtscATAC-seq: massively parallel single-cell mtDNA genotyping + chromatin profiling"
aliases: ["Lareau 2021 mtscATAC-seq", "Ludwig 2020 mtscATAC-seq"]
source: "[[00-Sources/papers/Massively parallel single-cell mitochondrial DNA genotyping and chromatin profiling]]"
source_quality: full
source_sha256: "a6f46c5b5e0741e9ebc6bf6095877c8528d43077e0cb6fcddb57470eafa11673"
source_kind: paper
author: "Caleb A. Lareau, Leif S. Ludwig, Christoph Muus, Satyen H. Gohil, Tongtong Zhao, Zachary Chiang, Karin Pelka, Jeffrey M. Verboon, Wendy Luo, Elena Christian, Daniel Rosebrock, Gad Getz, Genevieve M. Boland, Fei Chen, Jason D. Buenrostro, Nir Hacohen, Catherine J. Wu, Martin J. Aryee, Aviv Regev, Vijay G. Sankaran (corresponding)"
published: 2020-08-12
ingested: 2026-05-18
ingest_depth: abstract+intro
doi: "10.1038/s41587-020-0645-6"
journal: "Nature Biotechnology"
tags: [mtDNA, mtscATAC-seq, mitochondrial-heteroplasmy, lineage-tracing, scATAC-seq, Sankaran-lab, Buenrostro-lab]
entities: []
concepts:
  - "[[30-Concepts/mitochondrial-heteroplasmy]]"
  - "[[30-Concepts/mitochondrial-lineage-tracing]]"
  - "[[30-Concepts/scatac-seq]]"
  - "[[30-Concepts/chromatin-accessibility]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[40-Topics/somatic-mosaicism]]"
---

**Citation:** Lareau, Ludwig et al. (2021; online 2020) — *Massively parallel single-cell mitochondrial DNA genotyping and chromatin profiling* — *Nature Biotechnology* 39:451–461. [DOI](https://doi.org/10.1038/s41587-020-0645-6)

> **Attribution corrected 2026-10-07:** first author is Caleb A. Lareau (co-first with Ludwig), who was missing from the author list. Published online 12 Aug 2020, issue April 2021. The slug `ludwig-2020-…` is kept so existing links resolve.

# Lareau, Ludwig et al. 2021 — mtscATAC-seq

> Thesis: mitochondrial DNA contains naturally occurring heteroplasmic variants that can serve as **clonal lineage barcodes** without genetic engineering. mtscATAC-seq adapts the 10x scATAC-seq protocol to retain mitochondria during permeabilization, enabling simultaneous mtDNA genotyping and nuclear chromatin accessibility from the same cell at scale.

## Key claims (abstract + intro)

- **Protocol modification**: adds formaldehyde fixation and omits digitonin and Tween-20 from the lysis/wash buffers, allowing mtDNA to be co-amplified and sequenced with the Tn5-accessible nuclear DNA in the same droplet.
- **mtDNA heteroplasmy = natural barcode**: cell-to-cell variation in mtDNA variants provides clonal lineage information for somatic clones without CRISPR/Cas9 engineering — usable in primary human samples.
- **Two readouts per cell**: (i) mtDNA variant genotype at heteroplasmic positions; (ii) genome-wide chromatin accessibility for cell-type identification + regulatory state.
- Applied to cells carrying a pathogenic mtDNA variant, to CLL and colorectal cancer, and to in vitro / in vivo human hematopoiesis — recovers clonal hierarchies that align with independent genetic markers.

## Why this matters

Opens the mtDNA lineage-tracing branch of single-cell genomics at scale. Anchors the **mitochondrial heteroplasmy** concept cluster in the wiki alongside Lareau 2020 (further mtDNA tracing), Hsieh 2026 (lifespan mtDNA mosaicism), and downstream methods (scMitoMut).

## Note on ingest depth

Abstract + introduction only; full PDF re-ingest will deepen quantitative mtDNA coverage statistics and lineage-tree reconstruction methodology.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-020-0645-6) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32788666/)

## Related

- [[30-Concepts/mitochondrial-heteroplasmy]] · [[30-Concepts/mitochondrial-lineage-tracing]] · [[30-Concepts/scatac-seq]]
- [[10-Summaries/glynos-2023-mtdna-mosaicism]]
- [[40-Topics/single-cell-multiomics]] · [[40-Topics/somatic-mosaicism]]
