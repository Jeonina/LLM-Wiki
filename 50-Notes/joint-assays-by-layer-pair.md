---
type: note
title: "Joint single-cell assays, organized by layer-pair"
aliases: [joint assays, layer-pair assays, joint-assay landscape, multi-layer single-cell assays]
tags: [synthesis, single-cell-multiomics, joint-assay, locus-state, review-paper-anchor]
created: 2026-06-26
updated: 2026-06-26
sources: [
  "[[10-Summaries/izzo-2024-got-cha]]",
  "[[10-Summaries/swanson-2025-daf-seq]]",
  "[[10-Summaries/chi-2026-dd-seq]]",
  "[[10-Summaries/marks-2023-resolveome]]",
  "[[10-Summaries/hou-2016-sctrio-seq]]",
  "[[10-Summaries/clark-2018-scnmt-seq]]",
  "[[10-Summaries/lee-2019-natmethods]]",
  "[[10-Summaries/kriz-2025-duplex-multiome]]"
]
---

# Joint single-cell assays, organized by layer-pair

> The [[50-Notes/regulatory-layers-overview|locus-state framework]] holds that regulatory layers are interdependent, not independent — a premise testable only when two or more layers are measured in the *same* cell (synthesis). This note catalogs joint single-cell assays by **which layer-pair they bridge**, ordered genotype-anchored first because genetic variation anchors the DNA-centric locus state (synthesis). It is the methodological-integration companion to [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] (the gap analysis) and the review's joint-assay subsection.

## By layer-pair

| Layer pair | Assay | Reads in one cell | Key demonstration |
|---|---|---|---|
| Genotype + accessibility | GoT-ChA | gDNA genotype (targeted) + accessibility | JAK2^V617F HSCs show cell-intrinsic chromatin priming before transcriptional change ([[10-Summaries/izzo-2024-got-cha]]) |
| Genotype + accessibility (single-molecule) | DAF-seq / scDAF-seq | Same-fiber DNA sequence + nucleosome architecture | A 1.5% VAF mosaic CC→TT variant ablates the local CTCF footprint on the fibers carrying it ([[10-Summaries/swanson-2025-daf-seq]]) |
| Genotype + protein occupancy (TF binding) | D&D-GoT-ChA | Targeted genotype + accessibility + TF binding | IDH2^R140Q T cells show disrupted CTCF binding vs wild-type ([[10-Summaries/chi-2026-dd-seq]]) |
| Genotype (genome-wide) + transcriptome | ResolveOME | PTA whole-genome SNV/CNV + full transcriptome | FLT3 mutation co-detected with AXL-pathway upregulation in quizartinib-resistant AML ([[10-Summaries/marks-2023-resolveome]]) |
| CNV + methylation + transcriptome | scTrio-seq | Copy number + methylome + transcriptome | CNVs drive expression dosage but not local methylation — layers partly decoupled ([[10-Summaries/hou-2016-sctrio-seq]]) |
| Methylation + accessibility (+ RNA) | scNMT-seq | Methylome + accessibility + transcriptome | Methylation–accessibility coupling strengthens along differentiation ([[10-Summaries/clark-2018-scnmt-seq]]) |
| Methylation + 3D conformation | sn-m3C-seq | Chromatin conformation + methylome | Joint structural + epigenetic cell-type resolution in human brain ([[10-Summaries/lee-2019-natmethods]]) |
| Genotype + accessibility + transcriptome | Duplex-Multiome | Duplex-corrected somatic SNVs + snATAC + snRNA per nucleus | See climax below ([[10-Summaries/kriz-2025-duplex-multiome]]) |

## Two structural observations

- The deamination-based single-molecule assays — DAF-seq ([[10-Summaries/swanson-2025-daf-seq]]) and the nanobody-tethered [[30-Concepts/dd-seq|D&D-seq]] used in D&D-GoT-ChA ([[10-Summaries/chi-2026-dd-seq]]) — write the regulatory readout directly into the DNA sequence, which is exactly what makes them composable with genotyping rather than mutually exclusive with it (synthesis).
- The configuration that most fully realizes the locus-state premise — genetic variation + a chromatin layer + the transcriptome in the same cell, at scale — has only recently become feasible ([[10-Summaries/kriz-2025-duplex-multiome]]).

## The climax: Duplex-Multiome

[[10-Summaries/kriz-2025-duplex-multiome|Duplex-Multiome]] integrates duplex consensus sequencing into the snATAC arm of the 10x Multiome workflow, reducing sequencing error >10,000-fold so somatic SNVs can be called accurately from the same nucleus that yields an accessibility profile and a transcriptome ([[10-Summaries/kriz-2025-duplex-multiome]]). Applied to >51,400 nuclei from postmortem human brain, it resolved cell-type-specific somatic mutation burdens and signatures — including in glia and rare neurons largely inaccessible to scWGS — and linked clonal somatic variants to expression changes in nearby genes in both neurotypical and ASD brains ([[10-Summaries/kriz-2025-duplex-multiome]]). It thereby demonstrates, within single nuclei and at population scale, the genotype-to-regulatory-consequence inference the locus-state framework anticipates (synthesis). It remains a bioRxiv preprint (peer-review pending as of 2026-06) ([[10-Summaries/kriz-2025-duplex-multiome]]).

## What no assay yet closes

No current assay closes the framework entirely (synthesis). Duplex-Multiome substitutes accessibility for DNA methylation, and the inherent conflict between bisulfite conversion and sequence-level variant calling means point mutations and genome-wide methylation cannot yet be read together in the same cell ([[10-Summaries/kriz-2025-duplex-multiome]]; [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]]). These joint assays narrow but do not eliminate the gap between the conceptual locus state and what is measurable — and because every added layer compounds data sparsity and modality-specific bias, they sharpen rather than resolve the computational problem of reconstructing integrated locus states (synthesis).

## Related

- [[50-Notes/regulatory-layers-overview]] — the layer definitions this note pairs
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — the gap analysis this note operationalizes
- [[30-Concepts/scdna-capabilities-framework]] — fidelity / co-presence / phenotypic-association lens on the same assays
- [[40-Topics/single-cell-multiomics]] — full method catalog
- [[30-Concepts/dd-seq]], [[30-Concepts/resolveome]], [[30-Concepts/got-cha]], [[30-Concepts/daf-seq]], [[30-Concepts/scnmt-seq]], [[30-Concepts/sctrio-seq]]
