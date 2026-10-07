---
type: summary
title: "Liu et al. 2024 — SnapHiC-G: identifying long-range enhancer–promoter interactions from single-cell Hi-C data via a global background model"
source: "[[00-Sources/papers/SnapHiC-G_ identifying long-range enhancer–promoter interactions from single-cell Hi-C data via a global background model]]"
source_quality: full
source_sha256: "a5dd4fa18b0e3f562cfd51d7f7263be1992a7c33c3847fd87461504bded3356b"
source_kind: paper
author: "Weifang Liu, Wujuan Zhong, Paola Giusti-Rodríguez, Zhiyun Jiang, Geoffery W. Wang, Huaigu Sun, Ming Hu, Yun Li"
published: 2024-09-02
ingested: 2026-10-07
doi: "10.1093/bib/bbae426"
journal: "Briefings in Bioinformatics 25(5):bbae426"
tags: [SnapHiC-G, single-cell-Hi-C, enhancer-promoter, loop-calling, random-walk-with-restart, global-background, sn-m3C-seq, GWAS, eQTL, S-LDSC, brain-cell-types, Alzheimers, schizophrenia]
entities: ["[[20-Entities/ming-hu]]"]
concepts: ["[[single-cell-hi-c]]", "[[chromatin-loop]]", "[[imputation]]", "[[cis-regulatory-element]]", "[[alzheimers-disease]]", "[[pseudo-bulk]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]", "[[computational-methods]]"]
---

**Citation:** Liu et al. (2024) — *SnapHiC-G: identifying long-range enhancer–promoter interactions from single-cell Hi-C data via a global background model* — *Briefings in Bioinformatics* 25(5):bbae426. [DOI](https://doi.org/10.1093/bib/bbae426)

# Liu 2024 — SnapHiC-G

> SnapHiC finds scHi-C loops by combining global and local backgrounds. The local background favours sharp, CTCF-anchored **structural** loops and has low sensitivity for **enhancer–promoter (E–P)** contacts. SnapHiC-G drops the local background. It keeps SnapHiC's per-cell **random walk with restart (RWR)** imputation and distance-stratified z-scores, restricts candidate bin pairs to promoter–promoter ("AND") or promoter–enhancer ("XOR") pairs from TSS plus H3K4me3/H3K27ac/ATAC annotations, and runs a **one-sample t-test across cells** against zero. The result is far higher recall of reference E–P interactions (80% vs ≤16% in 742 mESCs) with comparable top-ranked precision, which makes cell-type-specific GWAS-to-gene mapping possible from sn-m3C-seq brain data.

## Key claims

- **Algorithm.** 10-kb bins; RWR (restart 0.05) in 2 Mb × 2 Mb sliding windows overlapping by 1 Mb; z-scores stratified by 1D distance. A bin pair is called if mean z > 0, >10% of cells have z > 1.96, FDR < 10% and t > 3. The range is 20 kb–1 Mb. Mappability >0.8 and the ENCODE blacklist are used as filters. Bin pairs <20 kb are excluded because short-range contacts can be random collisions.
- **mESC benchmark (742 cells; reference = HiCCUPS bulk loops ∪ MAPS H3K4me3 PLAC-seq ∪ cohesin and H3K27ac HiChIP; 38,588 interactions).** Power: **SnapHiC-G 0.793** (121,469 calls), FitHiC2 0.160, FastHiC 0.116, SnapHiC 0.076, HiC-ACT 0.074, Chromosight 0.061, HiC-DC+ 0.050. Bulk tools were run on pseudo-bulk with the same AND/XOR filter.
- **Fewer cells (100 mESCs).** SnapHiC-G power 0.607; all others below 0.10.
- **Precision of top calls.** Top-1,000 precision in 742 mESCs was 0.93, against HiC-DC+ 0.96, FastHiC 0.96, HiC-ACT 0.73, FitHiC2 0.73, SnapHiC 0.72 and Chromosight 0.46. With 100 mESCs, precision was 0.60–0.76 for the top 1,000–10,000. At 5-kb resolution in 100 mESCs, top-1,000 precision was 0.82.
- **Specificity.** Of 200 CRISPR-tested non-functional E–P pairs (Fulco et al.), 37 were called, giving a **specificity of 81.5%**. CRISPR-validated E–P interactions at *Sox2*, *Atpif1*, *Phactr4* and *Med13l* were detected; SnapHiC and FitHiC2 detected only *Sox2*.
- **Structural loops are a minority.** About 21% of SnapHiC-G-specific calls have CTCF at both anchors, against 28–50% for calls shared between methods.
- **Human cortex (sn-m3C-seq, 2,869 cells: astrocytes 338, microglia 323, oligodendrocytes 1,038, L2/3 neurons 261).** Calls are enriched for eQTL–TSS pairs over flipped pseudo-pairs, more for brain than liver eQTLs, and more for matched cell types. Microglia ORs: Bryois brain-cell-type 1.41, CMC 1.22, GTEx liver 1.05 (CI spans 1). >83% of genes from cell-type-specific SnapHiC-G interactions were not found by SnapHiC.
- **GWAS-to-gene (261 cells per type after downsampling).** 137,418 / 154,261 / 157,181 / 236,802 interactions (astro / microglia / oligo / L2/3), of which 14,440 / 39,220 / 23,853 / 65,819 were cell-type-specific. 222 matched interactions resolved >600 SNP–disease associations. The mean number of target genes per variant was ~1, against 25–83 genes within ±1 Mb. Of 331 matched AD variants in microglia, 29 were fine-mapped; of 18 matched SCZ variants in L2/3 neurons, 9 were. SnapHiC mapped no fine-mapped SNPs and FitHiC2 one.
- **Example loci.** SCZ rs2565064 → *PNOC* in neurons; SCZ rs28541694 plus 10 AD SNPs → *ZNF395* in astrocytes; AD rs1880949 → *ARPC1B* in microglia; EDU rs10241492 → *STAG3* in microglia; an SCZ locus → *SFXN2* (microglia) and *INA* (neurons).
- **Heritability (S-LDSC, 12 traits).** AD is most enriched in microglia target regions (P = 1.07 × 10⁻⁶ with SnapHiC-G vs P = 0.01 with SnapHiC). BP and SCZ are enriched in neurons > astrocytes > oligodendrocytes, PD in oligodendrocytes, and white blood cell count in microglia.

## Methods / evidence

Reanalysis of public scHi-C (742 mESCs, >150,000 contacts per cell) and sn-m3C-seq prefrontal cortex. Comparators: SnapHiC plus bulk callers on pseudo-bulk (FitHiC2, FastHiC, HiC-ACT, HiC-DC+, Chromosight). Reference interaction sets come from HiCCUPS/MAPS/HiChIP in mESC and H3K4me3 PLAC-seq in the brain cell types.

Weight: the sensitivity gain is large and robust to cell number, but the method calls **10⁵-scale interactions** and the reference sets are acknowledged as non-gold-standard. In brain cell types the advantage was **not substantial**, especially for oligodendrocytes (1,038 cells, ~278 million intrachromosomal contacts >20 kb when pooled), where bulk tools have enough depth. The median −log10(FDR) of 17.5 versus 1.7–7.5 for others makes ranking by significance uninformative. (synthesis on weight)

## Surprising or load-bearing bits

- **Global vs local background maps onto E–P vs structural loops.** Local-maximum callers find punctate CTCF loops; E–P contacts are diffuse enrichments over the distance expectation, which a global test captures. This is a useful way to read any loop-caller output. (synthesis)
- **The win is a low-cell-number win.** The gap is largest at 100 cells and shrinks when pooled depth approaches bulk. This matches the earlier SnapHiC finding. (synthesis)
- **Epigenomic annotation does much of the work.** Restricting tests to TSS × enhancer bin pairs narrows the search space. Without annotation, SnapHiC-G falls back to "promoter-interacting regions".
- **Still a cell-type-level caller.** The test aggregates across cells of one type, so calls are population-level, as the authors note.

## Concepts touched

- [[single-cell-hi-c]] / [[chromatin-loop]] — an E–P-specific single-cell caller; global-background framing.
- [[imputation]] — RWR with sliding windows as the sparsity fix; Higashi, Fast-Higashi and scVI-3D were not compared because they cannot impute 10-kb data, per the authors.
- [[cis-regulatory-element]] — linking noncoding GWAS variants to target genes by cell type.
- [[alzheimers-disease]] — microglia-specific heritability enrichment and *ARPC1B* target assignment.

## Connections to other sources

- Direct successor of [[yu-2021-snaphic]] (same RWR and t-test framework; same Hu/Li groups). The 1,038-oligodendrocyte / ~278M-contact observation that bulk tools catch up at high cell numbers appears in both.
- RWR imputation originates in [[zhou-2019-schicluster]]; alternative imputers: [[zhang-2022-higashi]].
- Data source assay: [[lee-2019-natmethods]] (sn-m3C-seq); same data family processed by [[galasso-2026-map3c]], whose MAPQ filtering changes trans-contact content (SnapHiC-G uses only intrachromosomal 20 kb–1 Mb pairs). (synthesis)
- Reference-truth assays: [[li-2014-chia-pet]] context for protein-anchored E–P maps; loop background in [[chromatin-loop]].

## Open questions

- With ~10⁵ calls per cell type, what fraction are functional? The 81.5% specificity rests on only 200 negatives.
- Per-cell E–P variability, the motivation stated in the introduction, is still not measured.
- Would better imputation (Higashi-class at 10 kb) or cleaner contacts change the calls? (synthesis)

## Related

- [[yu-2021-snaphic]] · [[ming-hu]] · [[chromatin-loop]] · [[40-Topics/3d-genome]]
