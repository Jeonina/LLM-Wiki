---
type: summary
title: "Mukamel 2025 — Cell-type-specific enrichment of somatic aneuploidy in the mammalian brain"
source: "[[00-Sources/papers/Cell-type-specific enrichment of somatic aneuploidy in the mammalian brain]]"
aliases: [Mukamel 2025, Eran 2025, snmC-seq aneuploidy detection, chr16 trisomy mouse brain]
tags: [somatic-mosaicism, neuro-mosaicism, aneuploidy, single-cell-methylation, snmC-seq, snm3C-seq, BICCN, foundational]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Mukamel et al. (2025) — *Cell-type-specific enrichment of somatic aneuploidy in the mammalian brain* — *Neuron*. [DOI](https://doi.org/10.1016/j.neuron.2025.08.006)

# Mukamel et al. 2025 — snmC-seq aneuploidy detection in mammalian brain

> Eran A. Mukamel, Hanqing Liu, M. Margarita Behrens, **Joseph R. Ecker\***. *Neuron* **113**, 2814–2821 (3 September 2025). DOI: 10.1016/j.neuron.2025.08.006. UCSD + Salk + HHMI.

## Thesis

**Single-cell DNA methylation sequencing (snmC-seq) data, originally collected for cell-type taxonomy, can detect aneuploidies** — whole-chromosome gains or losses — because the bisulfite-converted read distribution doubles as a copy-number signal. Applied to **415,103 single-cell methylomes covering the entire adult mouse brain** (BICCN dataset), the study finds aneuploidy in 0.175–0.349% of cells, with **strong cell-type-specific enrichment**: trisomy of chromosome 16 (mouse syntenic with human chr21) is **13-fold enriched** vs other autosomes, and aneuploidy of any chromosome is preferentially enriched in **oligodendrocyte precursor cells (OPCs)**, **Pons neurons**, and **pericytes**. Methodologically, this is the scTrio-seq logic (RRBS read distribution → CNV signal) extended to snmC-seq at 1,000× the cell number ever applied to brain aneuploidy.

## Method

1. **415,103 single nuclei** from adult C57BL/6 male mice (post-natal day 56–63), covering 73 dissected brain regions, **6 major cell classes, 48 cell types, 71 clusters** based on DNA methylation patterns. Source: BICCN multimodal mouse brain atlas ([[10-Summaries/yao-2021-nature]] family of papers). Two assay types: **snmC-seq3** (methylation only) and **snm3C-seq** (multi-omic methylation + chromatin conformation).
2. **CNV inference**: snmC-seq fragments are uniformly distributed under bisulfite chemistry, so read density in genomic bins reports relative copy number (Spearman r ≈ 0.85 between read density and GC content; ginkgo-style GC correction recovers uniform bin coverage).
3. Validate by comparing chrX (single copy in male) vs autosomes (diploid) across bin sizes 100 kb–12.7 Mb: AUROC ≈ 0.94 at 100 kb, >0.9997 at 12.7 Mb. Aneuploidies ≥5 Mb are reliably detected with high sensitivity and specificity (~97.5%).
4. **Circular binary segmentation** for CNV calling. Quality filter: MAPD <0.3, ≥900,000 uniquely mapped reads per cell. Cell defined as aneuploid if a chromosome has duplication/deletion over >90% of its extent.

## Key claims

1. **723 aneuploid cells at 100 kb resolution / 1,433 at 1 Mb resolution** out of 415,103 — i.e., **0.175–0.349% of brain cells carry whole-chromosome aneuploidy**. Consistent with prior small-scale scWGS estimates (0.5–5%, but typically at the lower end), and **two orders of magnitude lower** than older in-situ FISH/karyotype claims of 10–60% aneuploidy in brain.

2. **Chromosome 16 trisomy is 13-fold enriched** vs other autosomes (P < 10⁻³⁰⁰, binomial test). Mouse chr16 distal region is **syntenic with human chromosome 21** (where constitutional trisomy = Down syndrome). The Ts65Dn mouse model of Down syndrome uses partial chr16 trisomy. Mouse chr16 carries oligodendrocyte-lineage genes Olig1 and Olig2.

3. **Cell-type-specific enrichment of aneuploidy** (across 48 cell types):
   - **Oligodendrocyte precursor cells (OPCs)**: 1.65% aneuploid (95% CI 1.33–2.00%). Highest of all major classes.
   - **Pericytes**: 1.77% (0.89–2.94%).
   - **Pons neurons**: 0.47% (0.29–0.70%). Highest among neurons.
   - **Microglia**: 0.11% (0.043–0.20%).
   - **Trisomy 16 specifically** is enriched in **OPCs (0.42%), Pons (0.48%), midbrain (MB), dentate gyrus granule cells, claustrum, retrosplenial cortex** — across both neuronal and glial lineages, suggesting **chr16 nondisjunction is a recurrent mechanism** rather than a lineage-specific event.

4. **Multiple aneuploidies in the same cell are non-independent**: 153 cells (~21% of aneuploid cells) carry ≥2 aneuploidies, **82-fold more than expected for independent events** (P < 10⁻¹⁰). 131 cells carry 1 deletion + 1 duplication — consistent with **chromosome-pair missegregation during a single mitosis**. Suggests catastrophic single-division origin rather than serial accumulation.

5. **No correlation between chromosome length and aneuploidy frequency for duplications**, but more deletions among short chromosomes (Spearman r = −0.53, P = 0.016). Suggests duplications are biological (some chromosomes nondisjoin preferentially) while a fraction of detected deletions may be FANS-related artifacts (physical chromosome loss during fluorescence-activated nuclei sorting) — though this cannot explain duplications.

## Surprising / load-bearing for the review

- **Direct methodological precedent for the synthesis claim in [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]]**: this paper is the **scTrio-seq trick scaled to 415K cells**. Single-cell DNA methylation reads jointly yield CNV calls. The mosaicism + epigenome synthesis can now cite **two** anchor papers for joint single-cell DNA-alteration + epi: [[sctrio-seq]] (small-scale tumor; CNV + methylome + RNA) and Mukamel 2025 (atlas-scale mouse brain; CNV + methylome + chromatin conformation via snm3C-seq). **The synthesis note needs an update** — Mukamel extends the precedent from tumor to brain and from 25 cells to 415K cells.

- **The chr16 (= human chr21) trisomy finding is biologically major**: somatic chr21 trisomy has been reported in human brain in aging and Alzheimer's contexts (refs 33–36 in the paper). This paper provides the mouse atlas-scale companion result — recurrent somatic chr16 trisomy at a much higher rate than other chromosomes, with cell-type preferences (OPCs especially). For the review's §5 brain/Alzheimer's application section, this paper extends the [[10-Summaries/kousi-2022-alzheimer-mosaicism|Kousi/Kellis AD result]] from human SNV-burden cell-type-specificity to mouse atlas-scale aneuploidy cell-type-specificity.

- **Methodology generalizable to human atlases**: BRAIN Initiative Cell Census Network has analogous human methylome atlases (Liu 2023 *Nature*). Applying the same CNV-from-methylation logic would extend this approach to human aneuploidy mosaicism.

- **Limitations** the paper acknowledges:
  - Only male mice, single age (P56–63). Age dependence of brain aneuploidy (Bae 2022 result for SNVs) not addressed.
  - <1% aneuploidy rate means even 415K cells yields only ~720 aneuploid cells — small enough that some cell-type-specific findings have wide confidence intervals.
  - Methylation reads cover only ~5–15% of the genome per cell, capping CNV resolution; sub-5-Mb events not reliably called.
  - Bisulfite chemistry destroys DNA sequence → cannot get point-mutation calls from same reads. Joint *mutation* + epi at single-cell is still gap.

## Entities / concepts touched

[[somatic-mosaicism]] · [[scbs-seq]] · [[dna-methylation]] · [[single-cell-multiomics]] · [[3d-genome]] · [[alzheimers-disease]] · [[autism-spectrum-disorder]] · [[40-Topics/somatic-mosaicism]] · [[40-Topics/dna-methylation]] · [[40-Topics/3d-genome]] · [[40-Topics/single-cell-multiomics]]

## Related summaries

- [[10-Summaries/hou-2016-sctrio-seq]] — scTrio-seq, the methodological precedent (CNV from RRBS distribution).
- [[10-Summaries/taejeong-2022-science]] — Bae 2022 human-brain hypermutability, with chromosomal aneuploidies in some hypermutable brains (e.g., LIBD82).
- [[10-Summaries/kousi-2022-alzheimer-mosaicism]] — human-brain cell-type-specific SNV burden in AD.
- [[10-Summaries/clark-2018-scnmt-seq]] — scNMT-seq, similar logic for accessibility + methylation.
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — synthesis note that needs an update reflecting Mukamel 2025 as a second major anchor for joint CNV + epi at single-cell scale.

---
**Source:** [DOI](https://doi.org/10.1016/j.neuron.2025.08.006) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/40907475/)
