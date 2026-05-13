---
type: summary
title: "Jeong 2023 — Functional analysis of structural variants in single cells using Strand-seq (scNOVA)"
aliases: [Jeong 2023, scNOVA, Hyobin 2023, Strand-seq SV functional]
tags: [Strand-seq, structural-variants, single-cell, nucleosome-occupancy, scNOVA, CLL, method]
created: 2026-05-12
updated: 2026-05-12
sources: ["00-Sources/papers/Hyobin_2023_NatureBiotechnology.pdf"]
---

# Jeong et al. 2023 — scNOVA: SV functional characterization in single cells

> Hyobin Jeong, Karen Grimes, Kerstin K. Rauwolf, Peter-Martin Bruch, Tobias Rausch, Patrick Hasenfeld, Eva Benito, Tobias Roider, Radhakrishnan Sabarinathan, David Porubsky, Sophie A. Herbst, Büşra Erarslan-Uysal, Johann-Christoph Jann, Tobias Marschall, Daniel Nowak, Jean-Pierre Bourquin, Andreas E. Kulozik, Sascha Dietrich, Beat Bornhauser, Ashley D. Sanders, **Jan O. Korbel\***. *Nature Biotechnology* **41**, 832–844 (October 2023). DOI: 10.1038/s41587-022-01551-4. EMBL.

## Thesis

**scNOVA (single-cell nucleosome occupancy and genetic variation analysis)** uses [[strand-seq|Strand-seq]] data — which fragments DNA via MNase during library prep — to **simultaneously call structural variants AND infer gene expression activity from haplotype-aware nucleosome occupancy patterns in the same single cell**. Nucleosome occupancy in gene bodies is **inversely correlated with gene expression** (Spearman r up to –0.24), so MNase-fragmented Strand-seq read-density patterns serve as a "molecular phenotype" readout. Applied to CLL (Wnt-dysregulated subclones) and T-ALL (chromothripsis with c-Myb activation, Notch inhibitor targetable).

## Mechanism

1. **Strand-seq** library prep: BrdU labeling during one cell division → daughter cells inherit one labeled (Watson) and one unlabeled (Crick) strand per chromosome → MNase digestion of nuclear DNA → strand-specific single-cell libraries that resolve haplotypes.
2. **NO (nucleosome occupancy)** measured from read-density patterns: linker DNA between nucleosomes is digested, nucleosome-protected DNA survives → read counts in 80-bp bins around CTCF binding sites and gene bodies report nucleosome positioning.
3. **Haplotype-aware NO**: phased Strand-seq reads (~50% of NA12878 fragments) allow per-haplotype nucleosome occupancy → detects allele-specific SV effects.
4. **scNOVA framework** combines deep CNN + negative binomial GLM to predict gene-activity changes from NO in gene bodies across cells with different SVs.

## Key claims

- **NO at gene bodies inversely correlates with gene expression** (Spearman r = –0.24), comparable to scRNA-seq prediction power (AUC up to 0.93 in cell-type classification across LCL/RPE lines).
- **Haplotype-resolved gene-expression inference**: validates known X-chromosome inactivation in NA12878 (genes on Xi have higher NO).
- **CLL subclone with distinct Wnt-signaling dysregulation** identified via SV → NO → predicted expression cascade. Validated by RNA-seq.
- **T-ALL chromothripsis subclone with c-Myb activation** identified; targeting validated with Notch inhibitor in cell culture → demonstrates therapeutic implications of SV functional characterization.

## Surprising / load-bearing for the review

- **First single-cell method that infers gene-expression activity from DNA-only Strand-seq reads, without scRNA-seq**. For §3.1 (Strand-seq is part of the genotype-centric branch) and §4.6 (joint readout from same molecule), scNOVA extends Strand-seq's structural-variant detection to *functional* SV characterization without adding a second assay.
- Korbel lab is the **Strand-seq + scTRIP + scNOVA** lineage for single-cell SV analysis. Together with [[dlp-plus]] (Aparicio lab) and [[stam-seq]] (plant), they define the Strand-seq family.
- For §5 cancer applications, the CLL and T-ALL subclone-and-target findings show clinical translation potential of scNOVA.

## Entities / concepts touched

[[strand-seq|Strand-seq]] · [[scdna-seq]] · [[structural-variants]] · [[dlp-plus]] · [[chromatin-accessibility]] · [[40-Topics/single-cell-multiomics]]

## Related summaries

- [[a-comprehensive-view-of-somatic-mosaicism-by-single-cell-dna-analysis]] — related single-cell-DNA-mosaicism literature.
- [[harmonizing-single-cell-3d-genome-data-with-stark-and-scnucleome]] — STARK 3D genome.
