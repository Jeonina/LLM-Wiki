---
type: summary
title: "Kriz 2025 — Cell-type-specific patterns and consequences of somatic mutation in development and aging brain (Duplex-Multiome)"
source: "[[00-Sources/papers/Cell-type-specific patterns and consequences of somatic mutation in development and aging brain]]"
aliases: [Kriz 2025, Duplex-Multiome, Andrea 2025, Walsh-Lee Duplex-Multiome]
tags: [somatic-mosaicism, joint-assay, duplex-sequencing, snATAC-seq, snRNA-seq, brain, foundational, gap-closing]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Kriz et al. (2025) — *Cell-type-specific patterns and consequences of somatic mutation in development and aging brain (Duplex-Multiome)* — *bioRxiv (preprint)*. [DOI](https://doi.org/10.1101/2025.05.30.656844)

# Kriz et al. 2025 — Duplex-Multiome

> Andrea J. Kriz, Shulin Mao, Diane D. Shao, Daniel A. Snellings, Rebecca E. Andersen, Guanlan Dong, Chanthia C. Ma, Hayley E. Cline, August Yue Huang\*, **Eunjung Alice Lee\***, **Christopher A. Walsh\***. *bioRxiv* 2025.05.30.656844 (1 June 2025). Boston Children's Hospital + Harvard Medical School + HHMI + Broad Institute.

## Thesis — the synthesis-gap-closing paper

**Duplex-Multiome integrates duplex consensus sequencing into the 10X Multiome platform** to jointly measure **somatic single-nucleotide variants (sSNVs), single-nucleus ATAC-seq, and single-nucleus RNA-seq from the same nucleus** — all three layers, point mutations included, genome-wide, at single-nucleus scale beyond ten cells. **This is the assay the [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|wiki's synthesis note]] previously claimed did not yet exist.** Applied to >51,400 nuclei from postmortem human brain, identifies cell-type-specific somatic mutation rates and signatures across all major brain cell types, directly discovers developmental cell lineage relationships, and shows clonal sSNVs correlated with nearby gene-expression changes in ASD and neurotypical brains.

## Mechanism

1. **Strand-tagging in snATAC-seq library construction**: introduce duplex-consensus barcoding into the 10x Multiome snATAC arm so both strands of each DNA molecule are independently sequenced and reconciled.
2. **Duplex consensus collapses sequencing error >10,000-fold** by requiring both strands to agree on each base call.
3. Per-nucleus output: (a) sSNV calls at duplex-grade accuracy, (b) chromatin accessibility peaks (standard snATAC), (c) gene-expression profile (standard snRNA-seq).
4. Cell-line mixing validation: 98%/2% cell-line mixture → identifies sSNVs present in **2% of cells with 92% precision** and recovers known sSNV mutational spectra; reveals unexpected subclonal lineages.
5. Human postmortem brain application: >51,400 nuclei across multiple individuals.

## Key claims

- **First single-cell assay covering all four wishlist criteria**: (i) point mutations (not just CNV/aneuploidy), (ii) genome-wide (not targeted), (iii) paired chromatin accessibility, (iv) paired RNA — all in the same nucleus, scaled to >50k nuclei.
- **Distinct mutation rates and spectra across neuronal and glial cell types** — first comprehensive view including cell types difficult to sample by scWGS (e.g., glia, rare neuron subtypes).
- **Directly identifies developmental cell lineage relationships** from shared sSNVs between cells — without requiring engineered lineage markers.
- **Clonal sSNVs in aged glia at increased rates** in some brains → glial clonal expansion in aging.
- **Clonal sSNVs correlate with nearby gene-expression changes** in both neurotypical and ASD individuals → direct evidence that somatic mutations causally affect cellular phenotype via expression dysregulation. **First single-cell, same-nucleus demonstration of this causal link** for genome-wide point mutations.
- Easily adoptable into the standard 10X Multiome protocol — no custom hardware.

## Why this paper rewrites the synthesis note

The previously-stated gap in [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] was: *"no single-cell assay covers all of (a) point mutations, (b) genome-wide, (c) with paired chromatin, (d) at scale beyond ~10 cells"*. Duplex-Multiome closes this gap as a published bioRxiv preprint (June 2025). The synthesis note must be revised to acknowledge:

- The gap is **methodologically closed** — though not yet peer-reviewed.
- The "DNA-centric mutation + epi + RNA at single-cell" novelty claim for the planned review **now has a direct precedent in this paper from Walsh + Lee labs at Boston Children's / Broad**.
- The review's novelty argument shifts: not "this assay doesn't exist", but **"this assay just emerged and needs a conceptual framework — the locus-state framing — to make sense of what it measures"**.
- This is a Walsh-lab paper. The [[20-Entities/christopher-walsh|Walsh lab]] continues to anchor the human-brain mosaicism field methodologically, paralleling the [[20-Entities/dan-a-landau|Landau lab]]'s anchor role in hematopoietic mosaicism via GoT-ChA.

## Surprising / load-bearing for the review

- **The most important paper in this entire wiki for the planned review's novelty argument.** It both validates the conceptual frame (yes, jointly measuring these layers matters) and forecloses the "no such assay exists" framing. The review must engage with it directly.
- The **2% precision finding** (sSNVs detected at 2% VAF with 92% precision) sets a quantitative bar for any future joint-assay method.
- The **ASD clonal-sSNV → nearby gene expression correlation** is the direct successor to [[10-Summaries/taejeong-2022-science|Bae 2022's]] MEIS-motif finding — same biological question, now answerable at single-nucleus resolution rather than bulk-epigenome-annotated.
- Pairs with [[10-Summaries/mukamel-2025-aneuploidy-brain|Mukamel 2025]]: that paper detected aneuploidy + methylation at atlas scale (415k cells, mouse); this paper detects SNV + chromatin + RNA at brain-region scale (51k nuclei, human). Together they bracket the current methodological frontier.

## Entities / concepts touched

[[somatic-mosaicism]] · [[duplex-sequencing]] · [[scatac-seq]] · [[single-cell-multiomics]] · [[autism-spectrum-disorder]] · [[20-Entities/christopher-walsh]] · [[20-Entities/diane-d-shao]] · [[40-Topics/somatic-mosaicism]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/duplex-sequencing]]

## Related summaries

- [[taejeong-2022-science]] — Bae 2022 ASD MEIS-motif (bulk-epi-annotated); Duplex-Multiome is the single-nucleus same-cell successor.
- [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] — Luquette/Walsh same lab, PTA+DS prior generation.
- [[mukamel-2025-aneuploidy-brain]] — Mukamel 2025 mouse-brain aneuploidy + methylation atlas-scale complement.
- [[izzo-2024-got-cha]] — GoT-ChA, targeted-locus precedent for joint SNV + chromatin.
- [[10-Summaries/hou-2016-sctrio-seq]] — scTrio-seq (CNV + methylation + RNA), CNV-only precedent.

## Caveats

- **bioRxiv preprint as of 2026-05-12 date — not peer reviewed**. The review should cite the bioRxiv DOI and acknowledge preprint status. If published in *Nature Methods* / *Cell* / *Nature* by review submission, citation should update.

---
**Source:** [DOI](https://doi.org/10.1101/2025.05.30.656844) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/40502142/)
