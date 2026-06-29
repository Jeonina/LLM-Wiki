---
type: summary
title: "Macaulay 2015 — G&T-seq: Parallel sequencing of single-cell genomes and transcriptomes"
source: "[[00-Sources/papers/G&T-seq_ parallel sequencing of single-cell genomes and transcriptomes]]"
aliases: [Macaulay 2015, G&T-seq, GT-seq joint-assay]
tags: [G&T-seq, joint-assay, single-cell-multiomics, scDNA, scRNA-seq, foundational]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Macaulay et al. (2015) — *G&T-seq: Parallel sequencing of single-cell genomes and transcriptomes* — *?*. [DOI](https://doi.org/10.1038/nmeth.3370)

# Macaulay et al. 2015 — G&T-seq

> Iain C Macaulay, Wilfried Haerty, Parveen Kumar, Yang I Li, Tim Xiaoming Hu, Mabel J Teng, Mubeen Goolam, … Thierry Voet, Magdalena Zernicka-Goetz, Frederick J Livesey, Chris P Ponting. *Nature Methods* **12**, 519–522 (April 2015). DOI: 10.1038/nmeth.3370.

## Thesis

G&T-seq physically **separates** polyadenylated mRNA from genomic DNA in a single cell using a biotinylated oligo-dT primer captured on streptavidin beads, then **amplifies each pool independently** (Smart-seq2 for RNA, MDA or PicoPlex for DNA). This separation-before-amplification strategy contrasts with the contemporaneous one-pot DR-seq method ([[10-Summaries/dey-2015-dr-seq|Dey 2015]]) and enables full-length transcripts + flexible WGA choice from the same single cell.

## Mechanism summary

1. FACS or pick cell into RLT-Plus lysis buffer + ERCC spike-ins.
2. Biotinylated oligo-dT magnetic beads pull mRNA out; supernatant (gDNA) is moved to a fresh well.
3. Beads → on-bead reverse transcription with Smart-seq2 chemistry → cDNA → Nextera XT.
4. Supernatant gDNA → MDA (preferred for SNV / deep sequencing) or PicoPlex (preferred for copy-number) → Nextera XT.
5. Both libraries multiplexed and sequenced together.

## Key claims (evidence-anchored)

1. **>220 single cells** profiled across mouse and human. QC pass rate 75.6%.
2. **HCC38 + HCC38-BL benchmarking** (patient-matched breast cancer + lymphoblastoid lines): CNV concordance with bulk maintained; PicoPlex outperforms MDA for CNV; MDA outperforms PicoPlex for SNV discovery and breadth (~78% genome covered, 33× depth on HiSeq X).
3. **Subclonal trisomy 11 in HCC38-BL** detected at 10% frequency by G&T-seq, confirmed independently by FISH — first demonstration of single-cell joint detection of an aneuploid subclone.
4. **Reversine-treated mouse 8-cell embryos**: reciprocal aneuploidies between sister blastomeres, with **concordant chromosome-wide expression dosage** detected in the *same* cells. First evidence that aneuploidy-driven dosage effects are established within a single division.
5. **Trisomy-21 iPSC-derived neurons**: trisomy detected in 95% of cells (18/19), with elevated chromosome-21 expression. Genome-wide chromatin/expression effects on other chromosomes consistent with prior literature on Down syndrome dysregulation.
6. **MTAP–PCDH7 fusion** in 21% of HCC38 cells confirmed at *both* RNA and DNA levels in the same cells, with PacBio long-read sequencing resolving full fusion transcript structure.
7. **SNV detection from gDNA + RNA in the same cell**: 86–90% concordance with bulk for DNA SNVs; 88.7–96.8% of concordant DNA variants in transcribed regions also detected in RNA.

## Surprising / load-bearing

- The **separation-before-amplification** design is the key contribution. It gives G&T-seq three advantages over one-pot DR-seq: (a) no need to mask coding regions in DNA reads; (b) any WGA chemistry can be used; (c) full-length Smart-seq2 transcripts (not 3′-biased).
- The reversine 8-cell mouse embryo experiment is one of the cleanest demonstrations anywhere that **single-cell joint genome+transcriptome enables causal inference about expression-dosing kinetics that bulk sequencing cannot provide**. This is the prototype use-case for DNA-anchored joint assays in the somatic-mosaicism context.
- For the review paper §4.6: G&T-seq is the **first true DNA+RNA joint single-cell assay**. It sits at the methodological root of the joint-assay tree, with sci-CAR / SHARE-seq / 10x Multiome substituting chromatin for DNA, and scNMT-seq / scTrio-seq layering on methylation.

## Entities / concepts touched

[[40-Topics/scdna-seq]] · [[scwga]] · [[mda]] · [[malbac]] · [[40-Topics/single-cell-multiomics]] · [[20-Entities/thierry-voet]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/whole-genome-amplification]]

## Related summaries

- [[10-Summaries/dey-2015-dr-seq]] — Dey DR-seq, contemporaneous one-pot alternative.
- [[10-Summaries/clark-2018-scnmt-seq]] — scNMT-seq inherits the G&T-seq separation chemistry.
- [[10-Summaries/hou-2016-sctrio-seq]] — scTrio-seq, conceptual successor adding methylation.

---
**Source:** [Open paper](https://www.nature.com/articles/nmeth.3370)
