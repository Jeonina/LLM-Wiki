---
type: summary
title: "Ludwig et al. 2020 — mtscATAC-seq: massively parallel single-cell mtDNA genotyping + chromatin profiling"
source: "[[00-Sources/papers/Massively parallel single-cell mitochondrial DNA genotyping and chromatin profiling]]"
source_kind: paper
author: "Leif S. Ludwig, Christoph Muus, Satyen H. Gohil, Tongtong Zhao, Zachary Chiang, Karin Pelka, Jeffrey M. Verboon, Wendy Luo, Elena Christian, Daniel Rosebrock, Gad Getz, Genevieve M. Boland, Fei Chen, Jason D. Buenrostro, Nir Hacohen, Catherine J. Wu, Martin J. Aryee, Aviv Regev, Vijay G. Sankaran (corresponding)"
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

**Citation:** Ludwig et al. (2020) — *mtscATAC-seq: massively parallel single-cell mtDNA genotyping + chromatin profiling* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-020-0645-6)

# Ludwig et al. 2020 — mtscATAC-seq

> Thesis: mitochondrial DNA contains naturally occurring heteroplasmic variants that can serve as **clonal lineage barcodes** without genetic engineering. mtscATAC-seq adapts the 10x scATAC-seq protocol to retain mitochondria during permeabilization, enabling simultaneous mtDNA genotyping and nuclear chromatin accessibility from the same cell at scale.

## Key claims (abstract + intro)

- **Protocol modification**: replaces standard NP-40 detergent with a milder one that **preserves mitochondrial outer membrane**, allowing mtDNA to be co-amplified and sequenced with the Tn5-accessible nuclear DNA in the same droplet.
- **mtDNA heteroplasmy = natural barcode**: cell-to-cell variation in mtDNA variants provides clonal lineage information for somatic clones without CRISPR/Cas9 engineering — usable in primary human samples.
- **Two readouts per cell**: (i) mtDNA variant genotype at heteroplasmic positions; (ii) genome-wide chromatin accessibility for cell-type identification + regulatory state.
- Applied to colorectal cancer, CLL, and CD8 T cells — recovers clonal hierarchies that align with independent genetic markers.

## Why this matters

Opens the mtDNA lineage-tracing branch of single-cell genomics at scale. Anchors the **mitochondrial heteroplasmy** concept cluster in the wiki alongside Lareau 2020 (further mtDNA tracing), Hsieh 2026 (lifespan mtDNA mosaicism), and downstream methods (scMitoMut).

## Note on ingest depth

Abstract + introduction only; full PDF re-ingest will deepen quantitative mtDNA coverage statistics and lineage-tree reconstruction methodology.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-020-0645-6) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32788666/)

## Related

- [[30-Concepts/mitochondrial-heteroplasmy]] · [[30-Concepts/mitochondrial-lineage-tracing]] · [[30-Concepts/scatac-seq]]
- [[10-Summaries/hsieh-2026-mtdna-mosaicism]]
- [[40-Topics/single-cell-multiomics]] · [[40-Topics/somatic-mosaicism]]
