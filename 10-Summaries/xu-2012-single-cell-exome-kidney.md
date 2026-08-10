---
type: summary
title: "Xu et al. 2012 — Single-cell exome sequencing reveals single-nucleotide mutation characteristics of a kidney tumor"
source: "[[00-Sources/papers/Single-Cell Exome Sequencing Reveals Single-Nucleotide Mutation Characteristics of a Kidney Tumor]]"
source_kind: paper
author: "Xun Xu, Yong Hou, Xuyang Yin, ... Jun Wang, Xiuqing Zhang (BGI)"
published: 2012-03-16
ingested: 2026-08-10
doi: "10.1016/j.cell.2012.02.025"
journal: "Cell"
tags: [single-cell-exome, ccRCC, MDA, intratumor-heterogeneity, no-subclones, VHL, PBRM1, founding-application]
entities: []
concepts: ["[[single-cell-variant-calling]]", "[[intratumor-heterogeneity]]", "[[mda]]", "[[allele-dropout]]", "[[phylogenetic-inference]]", "[[single-cell-variant-calling]]"]
topics: ["[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]"]
---

**Citation:** Xu et al. (2012) — *Single-cell exome sequencing reveals single-nucleotide mutation characteristics of a kidney tumor* — *Cell* 148, 886–895. [DOI](https://doi.org/10.1016/j.cell.2012.02.025)

# Xu 2012 — single-cell exome of a kidney tumour

> The first single-cell **SNV** landscape of a human tumour. [[navin-2011-sns-tumor-evolution|Navin 2011]] had shown single-cell sequencing could resolve copy number; this paper and its companion showed it could resolve point mutations — and immediately produced a negative result that mattered: **a clear cell renal carcinoma with no detectable clonal substructure**.

## Key claims

- Design: **25 single-cell exomes** from one 59-year-old male patient with stage IV clear cell renal cell carcinoma (ccRCC) — 20 cells from the tumour, 5 from adjacent normal tissue — plus bulk exomes of tumour and matched normal.
- **The tumour was VHL/PBRM1-negative**, the two canonical ccRCC drivers. No *VHL* coding mutation; three *PBRM1* mutations at <4% allele frequency; no LOH on chromosome 3 or at other reported ccRCC LOH hot spots. Conversely, genes rarely mutated at the population level (*AHNAK*, *SRGAP3*) carried high-frequency mutant alleles here.
- **229 somatic coding mutations** across the tumour cell population (260 before removing misassigned cells), averaging ~78.9 per cancer cell, versus ~20.4 per normal cell — a difference significant at P = 1.4 × 10⁻⁵, used as the argument that the calls are not amplification artefacts.
- Validation: 93.64% of somatic mutant alleles covered by ≥10 reads; single-cell mutation frequencies correlate with bulk tissue frequencies at r² ≈ 0.8; **82 of 85 (96.47%) randomly chosen sites confirmed by PCR–capillary sequencing**.
- **Three of the twenty "tumour" cells were actually normal.** PCA on the 260-mutation profile clustered RC15, RC17 and RC20 with the adjacent normal tissue, and they were removed before heterogeneity analysis.
- **The central negative result**: PCA and a modified neighbour-joining phylogeny both show the cancer cells as diffusely diverse with **no discernible subpopulations**. The branch separating cancer from normal cells is short relative to the branches separating cancer cells from one another.
- Interpretation offered: the transition from normal to malignant was fast, and the large inter-cell diversity reflects accumulated **passenger** mutations rather than competing clones.
- Most somatic mutations were present in only a small fraction of cells, and **mutations at different allele frequencies had markedly different mutation spectra** — read by the authors as a signature of selection during progression.

## Methods / evidence

MDA-amplified single-cell exomes with a modified variant-calling pipeline and explicitly measured false-positive and false-negative rates (developed jointly with the companion myeloproliferative-neoplasm paper in the same issue). Bulk exome as an independent frequency reference, orthogonal PCR–Sanger validation, PCA and phylogeny as two independent tests of substructure, and a cohort of 98 ccRCC patients as the population-level comparison.

The identification and removal of three contaminating normal cells *by their mutation profiles* is the methodological detail worth carrying forward: cell-type assignment came from the data, not from dissection.

## Surprising or load-bearing bits

- **"Recurrent in the population" does not mean "present in this tumour."** A textbook ccRCC lacking both textbook drivers is the paper's most durable point, and it is an argument for individual-level molecular diagnosis rather than panel-based inference.
- **No subclones is a real finding, not a failure to detect them** — but it is also a 17-cell result, and 17 cells cannot exclude subpopulations below roughly 6% frequency. Contrast [[zahn-2017-dlp|DLP]], which reaches ~0.05% sensitivity with 6,000 cells and finds clones where bulk sees none. The two results are compatible; the resolution differs by two orders of magnitude.
- **Spectrum varying with allele frequency** is an early, indirect observation of what [[alexandrov-2013-mutational-signatures|mutational signature]] analysis formalized the following year — different processes dominating at different stages of the lineage.
- The false-positive control (cancer vs normal cell mutation counts) is a **relative** control: it shows the excess is real without establishing the absolute per-cell error rate. MDA allelic dropout and amplification error are the acknowledged constraint, and the whole downstream chemistry literature — [[zong-2017-malbac-protocol|MALBAC]], [[gonzalez-pena-2021-pnas|PTA]] — exists to reduce it.
- Both this paper and its companion appeared in the same issue of *Cell*, which is why single-cell exome sequencing arrived in the field as a pair of results rather than one.

## Concepts touched

- [[intratumor-heterogeneity]] — a documented case of *low* structured heterogeneity, useful as the counterexample to clonal-architecture assumptions.
- [[single-cell-variant-calling]] — the FP/FN-rate-first pipeline design originates in this pair of papers.
- [[mda]] — the amplification chemistry underlying all early single-cell SNV work.

## Connections to other sources

- Direct predecessor: [[navin-2011-sns-tumor-evolution]] (copy number, not SNVs — a limitation this paper names explicitly).
- Successors that revisit clonal structure at scale: [[zahn-2017-dlp]], [[laks-2019-dlp-plus]], [[kim-2018-tnbc-chemoresistance]].
- Signature interpretation: [[alexandrov-2013-mutational-signatures]].
- Amplification-error context: [[scwga-chemistries]], [[gonzalez-pena-2021-pnas]].

## Open questions

- Whether the absence of subclones is specific to this tumour, to ccRCC, or an artefact of 17 cells — the paper cannot distinguish these, and no source in this corpus revisits the same tumour type at DLP-scale cell numbers.
- The absolute per-cell false-negative rate under MDA is estimated but not independently verified here; mutations private to single cells are the hardest class to validate and the most affected.

## Related

- [[navin-2011-sns-tumor-evolution]] · [[intratumor-heterogeneity]] · [[zahn-2017-dlp]] · [[cancer-clonal-evolution]]
