---
type: summary
title: "Clark 2018 — scNMT-seq enables joint profiling of chromatin accessibility, DNA methylation and transcription in single cells"
source: "[[00-Sources/papers/scNMT-seq enables joint profiling of chromatin accessibility DNA methylation and transcription in single cells]]"
aliases: ["Clark 2018", "scNMT-seq", "single-cell NMT"]
tags: [scNMT-seq, joint-assay, methylation, accessibility, transcription, Reik-lab, Stegle-lab, Babraham, founding-method]
created: 2026-05-13
updated: 2026-05-13
---

**Citation:** Clark et al. (2018) — *scNMT-seq enables joint profiling of chromatin accessibility, DNA methylation and transcription in single cells* — *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-018-03149-4)

Clark, Argelaguet, Kapourani, Stubbs, Lee, Alda-Catalinas, Krueger, Sanguinetti, Kelsey, Marioni, Stegle and Reik (Babraham, EMBL-EBI, Sanger) developed **scNMT-seq**, the founding triple-omics method measuring DNA methylation, chromatin accessibility, and transcription in the *same* single cell. The protocol extends single-cell M&T-seq (Angermueller 2016) by treating the chromatin with a GpC methyltransferase (M.CviPI from NOMe-seq) before bisulfite conversion. This labels accessible chromatin as artificial GpC methylation, distinguishable from endogenous CpG methylation, while transcripts are captured in parallel by Smart-seq2.

Validation on differentiating mouse EL16 ESCs: 61 of 70 cells passed QC for all three modalities. Median coverage in a typical cell: 50% of promoters, 75% of gene bodies and 25% of active enhancers had ≥5 methylation-informative CpGs; chromatin accessibility was probed at ~85% of gene bodies and ~75% of promoters. Joint analysis revealed dynamic coupling between epigenomic layers during differentiation — methylation, accessibility and expression are linked but with distinct temporal kinetics.

## Why this matters

Founding triple-omics single-cell assay; the most-cited reference for "joint epigenome readout in single cells works." Anchors §3.3 (joint-methylome assays) and §3.2 (accessibility joint readouts), and is the natural predecessor of sn-m3C-seq (which substitutes 3D contact for transcription). Demonstrates the central technical principle reused across the field: methyltransferase-based labeling of accessibility is compatible with bisulfite chemistry.

---
**Source:** [DOI](https://doi.org/10.1038/s41467-018-03149-4) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/29472610/)

## Related

- [[10-Summaries/angermueller-2017-genomebiol]]
- [[10-Summaries/lee-2019-natmethods]]
- [[10-Summaries/pott-2017-elife]]
- [[30-Concepts/joint-methylome-assays]]
