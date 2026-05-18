---
type: summary
title: "Nichols 2022 — High-throughput robust scDNA methylation profiling with sciMETv2"
source: "[[00-Sources/papers/High-throughput robust single-cell DNA methylation profiling with sciMETv2]]"
aliases: ["Nichols Adey 2022 sciMETv2", "sciMETv2"]
tags: [sciMETv2, single-cell-methylome, combinatorial-indexing, sci-MET, Adey-lab, OHSU, high-throughput]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/High-throughput robust single-cell DNA methylation profiling with sciMETv2]]"
---

**Citation:** Nichols et al. (2022) — *High-throughput robust scDNA methylation profiling with sciMETv2* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-022-35374-3)

Nichols, O'Connell, Mulqueen et al. (Adey lab; OHSU) developed **sciMETv2**, a robust high-throughput single-cell DNA-methylation method based on combinatorial indexing. Two variants: sciMETv2.LA (Linear Amplification, high coverage) and sciMETv2.SL (Splint Ligation, rapid workflow). Improvements over sci-MET v1: ~15-fold higher coverage, standard sequencing recipes (no custom primers), minimal adapter contamination, multiple stopping points. Applied to primary human cortex, both versions identify distinct cell types using CH methylation patterns (neuron-specific), and the data integrate seamlessly with snmC-seq2 datasets. Demonstrates cell-type calling from **CG methylation alone**, important for non-neuronal tissues where CH is sparse.

## Why this matters

Operational complement to snmC-seq family (Luo 2018, Liu 2023) — sciMETv2 uses combinatorial indexing (sci-* lineage from Adey's PhD work) for high throughput, while snmC-seq uses PBAT chemistry. The two are competing/complementary methylation-throughput technologies. Anchors §3.3 (scDNA methylation methods) — important when surveying the methylation-assay landscape. Existing bibkey check needed; likely `nichols2022`.

## Related

- [[10-Summaries/luo-2018-snmc-seq2]]
- [[10-Summaries/liu-2023-mouse-brain-methylome-3d]]
- [[10-Summaries/cusanovich-2015-sciatac]]
- [[10-Summaries/clark-2018-scnmt]]
- [[20-Entities/andrew-adey]]

---
**Source:** [DOI](https://doi.org/10.1038/s41467-022-35374-3) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/36494343/)
