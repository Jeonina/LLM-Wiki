---
type: summary
title: "Hsieh 2026 — Single-cell multi-omic analysis of mitochondrial mutational mosaicism and dynamics"
aliases: ["Hsieh 2026", "scmtMPM", "scwMSS", "POLG mtDNA mosaicism"]
tags: [mtDNA, scmtATAC-seq, POLG, mitochondrial-mosaicism, heteroplasmy, Ludwig-lab, Lareau-lab, Charite-Berlin]
created: 2026-05-13
updated: 2026-05-13
sources: ["Yuhsin_2026_NatureCommunications.pdf"]
---

**Citation:** Hsieh et al. (2026) — *Single-cell multi-omic analysis of mitochondrial mutational mosaicism and dynamics* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-026-70399-y)

Hsieh, Kautz, Nitsch, Giguelay, Liebold, Dimitrova, Castillo, Jungen, Zsurka, Trombly, Schuelke, Kunz, Lareau and Ludwig (Charité Berlin, BIH, MSKCC) introduced two single-cell mtDNA metrics derived from mitochondrial single-cell ATAC-seq (mtscATAC-seq, Lareau 2021): (i) **scmtMPM** — single-cell mtDNA mutations per million base pairs, capturing per-cell mutational load; (ii) **scwMSS** — heteroplasmy-weighted mitochondrial-local-constraint-aware score, capturing functional impact of mtDNA mosaicism.

Validation system: HEK293 cell lines carrying the **POLG D274A** mutation — a proofreading-deficient mitochondrial DNA polymerase γ that hypermutates mtDNA. Two POLG-D274A clones (KI36, KI2) show a ~15-fold increase in detected mtDNA variants (9656 and 11407 variants per cell vs ~620 in controls), with C→T-transition-dominated signature indicating replication error as the primary driver. Pathogenic and truncating mtDNA variants are present at sub-threshold heteroplasmy in POLG cells, consistent with active negative selection.

Applied to PBMCs from healthy donors and mitochondriopathy patients, the framework reveals constrained mutations in complex I and previously unrecognized cell-level heterogeneity of mtDNA mutational landscapes. Also identified MGME1-deficiency-linked downregulation in POLG cells via differentially-accessible-gene analysis (1198/3113 down-regulated DAGs in KI36/KI2) — connecting nuclear chromatin response to mtDNA stress via the cGAS-STING pathway.

## Why this matters

A 2026 entrant in mtDNA-mosaicism methodology that pushes beyond MAESTER (Miller 2022, mtDNA-from-scRNA) by quantifying *load and constraint* per cell, not just variant identity. The POLG-D274A line is a useful "calibrator" model for mtDNA-mosaicism methods. Anchors §3.1 (mtDNA variant detection), §4 (computational metrics for mosaicism quantification), and §5 (mitochondrial disease + neurological applications). Direct connection to our review's framing: scwMSS treats mtDNA as a *locus-state* axis (heteroplasmy + constraint) rather than a binary lineage barcode.

---
**Source:** [DOI](https://doi.org/10.1038/s41467-026-70399-y) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/41839886/)

---
**Source:** [DOI](https://doi.org/10.1038/s41467-026-70399-y) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/41839886/)

## Related

- [[10-Summaries/lareau-2021-natbiotech]]
- [[10-Summaries/miller-2022-maester]]
- [[30-Concepts/mtDNA-lineage-tracing]]
