---
type: summary
title: "Pellegrino 2018 — High-throughput single-cell DNA sequencing of acute myeloid leukemia tumors with droplet microfluidics"
source: "[[00-Sources/papers/High-throughput single-cell DNA sequencing of acute myeloid leukemia tumors with droplet microfluidics.pdf]]"
source_quality: full
source_sha256: "ec60e69227af0db01b1d62580fa29d5216e623254b9b7d45d3e51457f2ffde41"
source_kind: paper
author: "Maurizio Pellegrino, Adam Sciambi, Sebastian Treusch (co-first), Robert Durruthy-Durruthy, Kaustubh Gokhale, Jose Jacob, Tina X. Chen, Jennifer A. Geis, William Oldham, Jairo Matthews, Hagop Kantarjian, P. Andrew Futreal, Keyur Patel, Keith W. Jones, Koichi Takahashi, Dennis J. Eastburn (corresponding)"
published: 2018
ingested: 2026-05-13
doi: "10.1101/gr.232272.117"
journal: "Genome Research 28:1345–1352"
aliases: ["Pellegrino 2018", "Tapestri", "Mission Bio scDNA", "MissionBio"]
tags: [Tapestri, MissionBio, droplet-scDNA, AML, targeted-panel, clonal-evolution, Eastburn, allele-dropout, MRD]
entities: []
concepts: ["[[allele-dropout]]", "[[intratumor-heterogeneity]]", "[[single-cell-variant-calling]]", "[[drop-seq]]", "[[doublet-detection]]", "[[umi-molecular-barcoding]]"]
topics: ["[[hematopoietic-malignancies]]", "[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]", "[[scdna-seq]]"]
created: 2026-05-13
updated: 2026-10-07
---

**Citation:** Pellegrino et al. (2018) — *High-throughput single-cell DNA sequencing of acute myeloid leukemia tumors with droplet microfluidics* — *Genome Research* 28:1345–1352. [DOI](https://doi.org/10.1101/gr.232272.117) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/30087104/)

# Pellegrino 2018 — droplet targeted scDNA-seq (Tapestri)

> Droplet barcoding had worked for scRNA-seq but not for genomic DNA, because crude lysate and chromatin inhibit PCR. This Mission Bio / MD Anderson paper solves it with a **two-step droplet workflow**: cells are first encapsulated with a protease-containing lysis buffer and incubated, the protease is heat-inactivated, and each lysate droplet is then merged with a droplet carrying PCR reagents and a barcoded hydrogel bead whose primers target a **62-amplicon AML panel**. Applied to longitudinal bone-marrow samples from two AML patients (more than 16,000 cells genotyped), the method found residual mutant cells in remission and clonal structures that bulk VAF inference got wrong. The paper does not use the name "Tapestri"; the workflow is the basis of Mission Bio's commercial platform, and all Mission Bio authors declare employment and shares. (synthesis for the platform lineage)

## Key claims

- **The protease step is the enabling trick.** In droplet TaqMan PCR for the single-copy *SRY* locus in DU145 cells, "only 5.2% of detected DU145 cells were positive" without protease, against "97.9%" with it. With barcoded beads targeting eight amplicons in *TP53*, *DNMT3A*, *IDH1*, *IDH2*, *FLT3* and *NPM1*, protease also raised library yield and per-cell read depth across all eight targets.
- **Panel and run metrics.** The 62-amplicon panel covers many of the 23 most commonly mutated AML genes. On average 74.7% of reads (MAPQ > 30) carried a cell barcode and mapped to a target. Each run loaded 200,000–250,000 bone-marrow cells with a ~1% Raji spike-in; per sample, 5,498–7,364 cells were found and 4,236–4,748 genotyped (patient 1). Workflow time was "<2 d" per sample.
- **Allele dropout measured in-run.** Using two heterozygous *TP53* SNVs in the Raji spike-in, average dropout was 7.0% across the three patient-1 runs; across nine Raji variants in six runs it was "8.7% ± 1.1% (SEM)". Per run, dropout ranged from 2.1% to 10.3%. Raji detection averaged 2.4% for a nominal ~1% spike. Multiplet rate was assessed with mixed cell lines (supplement only).
- **Patient 1 (66-year-old man, AML M5, normal karyotype).** Of 17 variants, three coding nonsynonymous SNVs were tracked — *TP53* H47R, *DNMT3A* R899C, *ASXL1* L815P (a known germline polymorphism, rs6058694, present in all cells) — plus a 21-bp *FLT3*-ITD; 13,368 cells were genotyped. A **TP53/DNMT3A/FLT3-ITD triple mutant** was the dominant clone at both diagnosis and relapse, supporting serial acquisition. Remission contained about 10 mutant cells, read as residual disease. Relapse came ~3 months after CR with almost unchanged architecture.
- **Bulk inference was wrong about the founder.** Bulk VAFs predicted a *DNMT3A* single-mutant population of 23.6% (implying a founder mutation); single-cell data showed it at only 1.7%, at a level explainable by dropout, and suggested *TP53* was more likely the founder.
- **Patient 2 (65-year-old man, AML with myelodysplasia-related changes, normal karyotype).** Of 20 variants, five were nonsynonymous; the authors tracked *IDH2* R140Q, *NRAS* G13R and *ASXL1* G646fs (bulk VAFs 31.7%, 13.1%, 22.5%) in 2,850 cells. Between diagnosis and relapse ~3 years later, the triple mutant grew "from 7% at diagnosis to 64% at relapse" and the *IDH2* single mutant shrank from 41% to 2%. Dropout was similar in both runs (8.0% and 9.0%), so the authors argue the shift is not technical. An *IDH2/NRAS* double mutant comprising 29% of the diagnosis tumour was not predicted from bulk VAFs.
- **MRD sensitivity.** The method detected "as few as three mutation-harboring cells out of about 4000 genotyped cells from remission biopsies", which the authors suggest could complement or one day replace multiparametric flow cytometry for minimal residual disease.

## Methods / evidence

Microfluidics: PDMS devices with fluorinated oil and PEG-PFPE surfactant; droplet merger by a microfluidic electrode. Lysis buffer: 100 mM Tris pH 8.0, 0.5% IGEPAL, proteinase K 1.0 mg/ml, incubated at 37 °C before heat inactivation. Beads: split-and-pool barcoded acrylamide hydrogel beads with ligated gene-specific primers, UV photo-released before PCR (~45% oligo conversion to full-length barcode). Library: emulsion breaking, SPRI clean-up, a 10-cycle index PCR, MiSeq 150- or 250-bp paired-end. Analysis: Cutadapt, BWA-MEM to hg19, barcode error correction against a whitelist, cell calling by knee plot of reads per barcode, GATK 3.7 joint genotyping thresholded on Raji variants, FreeBayes for *FLT3*-ITD. Bulk comparator: a 295-gene SureSelect hematologic panel on HiSeq 2000. Data: dbGaP phs001627.v1.p1.

Weight: a convincing technology demonstration with a built-in dropout control (Raji spike-in), but biological claims rest on two patients, a single bulk method and four tracked loci per patient. All biologically interesting cases (founder reassignment, unpredicted clones) are single-patient observations. The authors are company employees reporting their own platform. (synthesis)

## Limitations

**Authors' own:**
- Observations come from "a small number of patients and a single approach to bulk sequencing"; more patients are needed to confirm clinical utility.
- Some clonal populations are "likely technical in nature and probably a consequence of allele dropout"; in patient 2 relapse, several clones at <2.5%, three of them single-mutant genotypes, are explainable by dropout and do not fit serial acquisition.
- The 62-amplicon panel leaves a coverage deficit compared with well-based whole-exome or whole-genome single-cell methods; more multiplexing was in development.
- The link between remission length and clonal remodelling (3 months vs 3 years, plus low-dose maintenance) cannot be concluded from two patients.

**Reviewer notes:**
- Only SNVs and one ITD in a few loci are genotyped; no copy number, so clonal trees ignore CNV-defined subclones. (synthesis)
- The main text reports no multiplet rate, and Raji detection (~2.4% for a ~1% spike) hints at loading or doublet effects; low-frequency compound genotypes therefore need caution. (synthesis)
- Dropout of 2–10% per run is enough to create spurious single- or double-mutant "clones" at the few-percent level, which is exactly where MRD and rare-clone claims sit. (synthesis)

## Surprising or load-bearing bits

- **Lysis, not barcoding, was the bottleneck.** Without protease, droplet gDNA PCR detected ~5% of cells; the whole platform rests on a protease step that is then heat-killed before PCR.
- **Bulk VAF clonal inference can invert founder order.** The *DNMT3A* case (23.6% predicted vs 1.7% observed) is a concrete warning against reading founder status from bulk VAFs.
- **A spike-in cell line as an in-run truth set** for dropout is a design worth copying in any targeted single-cell genotyping study. (synthesis)
- **Two patients, two relapse modes:** unchanged architecture after a short remission versus outgrowth of a minor triple-mutant clone after a long one.

## Concepts touched

- [[allele-dropout]] — measured per run from Raji heterozygous SNVs (2.1–10.3%; 8.7% ± 1.1% across nine variants) and used to discount small clones.
- [[intratumor-heterogeneity]] — clonal architecture of two AML tumours resolved per cell.
- [[single-cell-variant-calling]] — GATK joint calling with thresholds set on known spike-in variants.
- [[drop-seq]] / [[umi-molecular-barcoding]] — droplet barcoding with split-and-pool hydrogel beads adapted from scRNA-seq to amplicon DNA.
- [[doublet-detection]] — multiplet rate assessed by mixed cell lines (supplement).

## Connections to other sources

- Droplet barcoding precedent from RNA: [[macosko-2015-drop-seq]]; droplet ChIP precedent: [[rotem-2015-drop-chip]].
- Well-based targeted single-cell genotyping it scales up: [[gawad-2014-all-clonal-origins]].
- Downstream methods built for this data type: [[sollier-2023-compass]] (Tapestri-based trees with CNV), [[singer-2018-sciphi]] (panel data caveats), [[ross-2016-onconem]] and [[jahn-2016-scite]] (small-*n* era methods). Derived platforms and uses: [[lindenhofer-2025-sdr-seq]], [[pancikova-2025-splongget]]; droplet DNA methylation analogue [[zhang-2023-drop-bs]].
- Contrast with genome-wide low-coverage CNV platforms: [[laks-2019-dlp-plus]]; well-based tumour single-cell DNA: [[kim-2018-tnbc-chemoresistance]]. (synthesis)

## Open questions

- How often does bulk VAF-based inference misassign founder mutations in larger AML cohorts?
- Can droplet targeted genotyping reach clinically useful MRD sensitivity once dropout and doublets are modelled, rather than counted as raw cells? (synthesis)
- Does remission length or maintenance therapy predict clonal remodelling at relapse? Two patients cannot answer this.

## Related

- [[allele-dropout]] · [[intratumor-heterogeneity]] · [[gawad-2014-all-clonal-origins]] · [[sollier-2023-compass]] · [[40-Topics/hematopoietic-malignancies]] · [[40-Topics/scdna-cancer-applications]] · [[40-Topics/cancer-clonal-evolution]]
