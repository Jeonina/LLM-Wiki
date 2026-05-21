---
type: summary
title: "Liu et al. 2025 — Nanopore somatic SVs in laryngeal squamous cell carcinoma"
source: "[[00-Sources/papers/Nanopore Sequencing Unveils Somatic Structural Variations as Biomarkers in Laryngeal squamous cell carcinoma Genomes]]"
source_kind: paper
author: "Xuyan Liu, Lin Xia, ... Dan Xie, Jifeng Liu (corresponding)"
published: 2025-06-17
ingested: 2026-05-12
doi: "10.1101/2025.06.12.659252"
journal: "bioRxiv (preprint)"
tags: [nanopore, structural-variants, laryngeal-cancer, biomarkers, somatic, smoking, SomaGauss-SV]
entities:
  - "[[20-Entities/jifeng-liu]]"
  - "[[20-Entities/dan-xie]]"
  - "xuyan liu"
concepts:
  - "[[30-Concepts/somagauss-sv]]"
  - "[[30-Concepts/structural-variants]]"
  - "[[30-Concepts/long-read-sequencing]]"
  - "[[30-Concepts/oxford-nanopore]]"
  - "[[30-Concepts/laryngeal-squamous-cell-carcinoma]]"
topics:
  - "[[40-Topics/long-read-sequencing]]"
  - "[[40-Topics/somatic-mosaicism]]"
---

**Citation:** Liu et al. (2025) — *Nanopore somatic SVs in laryngeal squamous cell carcinoma* — *bioRxiv (preprint)*. [DOI](https://doi.org/10.1101/2025.06.12.659252)

# Liu et al. 2025 — Nanopore somatic SVs in laryngeal SCC

> Thesis: Laryngeal squamous cell carcinoma (LSCC) lacks reliable molecular biomarkers for early diagnosis and prognosis. Bulk short-read sequencing detects SNVs well but is poorly suited to large somatic structural variants (SVs) that are central to tumorigenesis. **SomaGauss-SV**, a new somatic-SV detection workflow on nanopore long-read sequencing data, achieves balanced precision and recall across five paired tumor-cell-line benchmarks. Applied to 15 paired LSCC tumor–blood samples, it reveals a comprehensive SV landscape, links smoking intensity to somatic deletion burden, and identifies a high-frequency simple-repeat expansion in 74% of patients that drives *TP53BP2* and *FBXO28* via spatial proximity.

## Key claims

- **SomaGauss-SV workflow**: somatic-SV detection from paired tumor-vs-normal nanopore long-read data. Balanced high precision and recall across five paired tumor cell-line datasets (benchmark).
- **15 paired LSCC samples**: comprehensive SV landscape including deletions, insertions, duplications, inversions, translocations.
- **Smoking-dose × somatic-deletion correlation**: significant positive correlation between somatic deletion burden and smoking intensity. Quantitative confirmation of a long-suspected etiologic link.
- **Simple-repeat-expansion hotspot**: a high-frequency somatic simple-repeat expansion observed in 20/27 (74.1%) of LSCC patients (extending the original 15-patient cohort). The expansion upregulates *TP53BP2* and *FBXO28* through **spatial proximity** (3D-genome contact) — i.e., the expanded repeat brings nearby genes into a more accessible chromatin neighborhood.
- Positions long-read sequencing + SomaGauss-SV as a tool for **biomarker discovery** in head-and-neck cancers.

## Methods / evidence

Nanopore long-read sequencing of 15 paired tumor-blood LSCC samples. Five paired tumor cell-line datasets for SomaGauss-SV benchmark vs alternative SV callers. RNA-seq for downstream gene-expression correlation. Hi-C or similar contact data used to validate spatial-proximity-mediated regulation of *TP53BP2*/*FBXO28*.

## Surprising or load-bearing bits

- The **smoking × deletion correlation** is a satisfying clinical-genomics result: tobacco mutagenesis is well-known to cause SNVs (SBS4 signature), but quantifying its effect on **structural** variant burden requires long reads, which this paper provides.
- The simple-repeat-expansion finding at 74% frequency is striking. Most repeat-expansion biology has been studied in inherited neurological disorders (HD, FRDA, FXTAS, C9ORF72); somatic repeat expansion as a cancer driver in 74% of an LSCC cohort is an under-studied territory.
- **Spatial-proximity gene regulation by repeat expansion** is mechanistically interesting: the expansion doesn't directly hit the gene but reorganizes local chromatin to drive expression.

## Connections to other sources

- A clinical application of the long-read SV-detection technologies reviewed in [[10-Summaries/fu-2025-longread-methylation]] (Fu/Sedlazeck/Timp 2025 long-read methylation review) and [[10-Summaries/liu-2025-long-read-epigenome-review]] (Liu/Conesa 2025).
- Connects somatic structural variation to [[40-Topics/somatic-mosaicism]] — extends the mosaicism story from SNVs (covered in [[10-Summaries/shao-2025-scDNA-mosaicism-review]] and [[10-Summaries/bizzotto-2022-brain-mosaicism-review]]) to SVs.
- The spatial-proximity-gene-regulation finding overlaps thematically with single-cell 3D-genome work in [[10-Summaries/hong-2025-sc3d-genome-review]].

## Open questions

- Preprint, not peer-reviewed. SomaGauss-SV tool code/release status unclear from the clipping.
- Spatial-proximity mechanism for *TP53BP2*/*FBXO28* activation needs orthogonal Hi-C/4C validation.
- Cohort is small (15 → 27 patients); replication and external cohort needed before clinical biomarker claims.

---
**Source:** [DOI](https://doi.org/10.1101/2025.06.12.659252)
## Related

- [[40-Topics/long-read-sequencing]] · [[30-Concepts/somagauss-sv]] · [[30-Concepts/structural-variants]] · [[40-Topics/somatic-mosaicism]]
