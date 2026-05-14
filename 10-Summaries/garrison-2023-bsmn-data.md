---
type: summary
title: "Garrison 2023 — Genomic data resources of the Brain Somatic Mosaicism Network for neuropsychiatric diseases"
aliases: ["Garrison 2023", "BSMN data descriptor", "BSMN data resources"]
tags: [BSMN, data-descriptor, brain-mosaicism, ASD, schizophrenia, bipolar, FCD, Tourette, NIMH, consortium-resource]
created: 2026-05-13
updated: 2026-05-13
sources: ["Mckinzie_2023_ScientificData.pdf"]
---

Garrison and colleagues (BSMN consortium, NIMH-funded) describe the **Brain Somatic Mosaicism Network (BSMN)** genomic data resources for neuropsychiatric diseases — over 400 terabytes of data from 1,087 subjects, deposited at the NIMH Data Archive (NDA). The BSMN consortium spans nine disease-specific projects covering autism spectrum disorder (ASD), bipolar disorder (BP), focal cortical dysplasia (FCD), schizophrenia (SCZ), Tourette syndrome (TS), plus a tenth consortium-wide neurotypical reference brain (NRB; LIBD subject 5154) used to validate the somatic-SNV-calling best-practice workflow.

The data resources include: whole-genome sequencing (WGS, both conventional and high-coverage), whole-exome sequencing (WES), single-cell DNA sequencing (NeuN+ MDA), RNA-seq, and SLAV-seq targeting somatic LINE-1 retrotransposition events. The NRB workflow validation paper (Wang 2021) developed the consensus mosaic-SNV calling pipeline now used field-wide; the SNV gold-standard set on the NRB is the de-facto benchmark for mosaic-caller comparison (used by Ha 2023 benchmark).

## Why this matters

The reference data resource that underlies most post-2020 brain-mosaicism methodology papers. Anchors §5 (neuropsychiatric applications), §6 (limitations — data heterogeneity across institutions), and §4 (benchmarking — the BSMN NRB is the de-facto truth set). Important methodological note for the review: BSMN's best-practice workflow informs the consensus that mosaic-SNV calling requires deep WGS (≥250×), targeted validation, and combinatorial calling (MosaicForecast + DeepMosaic + MosaicHunter).

---
**Source:** [DOI](https://doi.org/10.1038/s41597-023-02645-7) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37985666/)

## Related

- [[10-Summaries/yang-2023-deepmosaic]]
- [[10-Summaries/mcconnell-2017-science]]
- [[10-Summaries/nishioka-2019-molpsych]]
- [[40-Topics/brain-somatic-mosaicism]]
