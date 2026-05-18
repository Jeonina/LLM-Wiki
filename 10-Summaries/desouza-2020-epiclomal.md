---
type: summary
title: "de Souza 2020 — Epiclomal: Probabilistic clustering of sparse single-cell DNA methylation data"
source: "[[00-Sources/papers/Epiclomal_ Probabilistic clustering of sparse single-cell DNA methylation data]]"
aliases: ["de Souza 2020", "Epiclomal", "epiclonal methylation"]
tags: [Epiclomal, scBS-seq, methylation-clustering, missing-data-imputation, cancer-clones, Shah-lab, BC-Cancer]
created: 2026-05-13
updated: 2026-05-13
source: "[[00-Sources/papers/Epiclomal_ Probabilistic clustering of sparse single-cell DNA methylation data]]"
---

**Citation:** de Souza et al. (2020) — *Epiclomal: Probabilistic clustering of sparse single-cell DNA methylation data* — *PLOSComputationalBiology*. [DOI](https://doi.org/10.1371/journal.pcbi.1008270)

de Souza, Andronescu, Masud, Kabeer, Biele, Laks, Ye, Brimhall, Wang, Su, Hui, Cao, Wong, Moksa, Moore, Hirst, Aparicio and Shah (Western/BC Cancer/Memorial Sloan Kettering) developed **Epiclomal**, a probabilistic hierarchical-mixture-model framework that simultaneously clusters sparse single-cell DNA methylation data (scBS-seq) and imputes missing values. The model borrows statistical strength across cells and neighboring CpGs to handle the dominant feature of scBS-seq data: 80–95% missing CpGs per cell.

Validated on synthetic and published scBS-seq datasets, Epiclomal outperforms non-probabilistic methods (BackSPIN, Smallwood-style hierarchical clustering, Hou-style Pearson clustering, Mulqueen-style NMF+DBSCAN). Applied to newly-generated single-cell 5mCpG sequencing of breast-cancer xenograft samples (SA501 series), Epiclomal discovered sub-clonal methylation patterns ("epiclones") in aneuploid tumor genomes — epiclones can either match copy-number-defined clonal lineages *or* transcend them, revealing methylation-only sub-population structure invisible to CNV analysis.

## Why this matters

A key computational tool in the §4 methylation-analysis tool family: Epiclomal sits alongside Melissa (Kapourani 2019), scMET (Kapourani 2021), DeepCpG (Angermueller 2017), and PDclust (Hui 2018) as the principal scBS-seq clustering methods. The "epiclone" concept directly motivates §3.3's framing of methylation as a clonal-mosaicism axis that is *partially independent* of copy-number — anchoring the locus-state framework's argument that methylation carries independent information from genotype.

---
**Source:** [DOI](https://doi.org/10.1371/journal.pcbi.1008270) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32966276/)

## Related

- [[10-Summaries/smallwood-2014-natmethods]]
- [[10-Summaries/angermueller-2017-genomebiol]]
- [[10-Summaries/kapourani-2019-melissa]]
- [[10-Summaries/kapourani-2021-scmet]]
- [[30-Concepts/methylation-clones-epimutation]]
