---
type: summary
title: "Mo et al. 2023 — STAM-seq: nanopore-adaptive-sampling accessibility + methylation in plant HRRs"
source: "[[00-Sources/papers/Single-molecule targeted accessibility and methylation sequencing of centromeres, telomeres and rDNAs in Arabidopsis]]"
source_kind: paper
author: "Weipeng Mo, Yi Shu, Bo Liu, Yanping Long, Tong Li, Xiaofeng Cao, Xian Deng, Jixian Zhai (corresponding)"
published: 2023-08-20
ingested: 2026-05-12
doi: "10.1038/s41477-023-01498-7"
journal: "Nature Plants"
tags: [long-read, nanopore, Arabidopsis, centromeres, telomeres, rDNA, adaptive-sampling, EcoGII, plant-epigenomics]
entities:
  - "[[20-Entities/jixian-zhai]]"
  - "[[20-Entities/weipeng-mo]]"
  - "[[20-Entities/xiaofeng-cao]]"
concepts:
  - "[[30-Concepts/stam-seq]]"
  - "[[30-Concepts/nanopore-adaptive-sampling]]"
  - "[[30-Concepts/highly-repetitive-regions]]"
  - "[[30-Concepts/dna-methylation]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/long-read-sequencing]]"
topics:
  - "[[40-Topics/long-read-sequencing]]"
  - "[[40-Topics/chromatin-architecture]]"
  - "[[40-Topics/dna-methylation]]"
---

**Citation:** Mo et al. (2023) — *STAM-seq: nanopore-adaptive-sampling accessibility + methylation in plant HRRs* — *Nature Plants*. [DOI](https://doi.org/10.1038/s41477-023-01498-7)

# Mo et al. 2023 — STAM-seq

> Thesis: Plant centromeres, telomeres, and rDNA arrays are highly repetitive regions (HRRs) that NGS cannot uniquely map and bisulfite sequencing cannot preserve. **STAM-seq** combines nanopore long-read sequencing + EcoGII 6mA methyltransferase labeling of accessible regions + nanopore **adaptive sampling** to enrich HRRs by real-time rejection of non-target reads. Simultaneously detects 6mA (chromatin accessibility) and endogenous 5mC (DNA methylation) on the same fiber. Reveals strand-specific epigenetic patterns at *Arabidopsis* CEN180 centromeric repeats, transcription-state-linked methylation at rDNA variants, and asymmetric telomere/subtelomere modifications.

## Key claims

- **Method**: nuclei → EcoGII 6mA methylation of accessible regions → nanopore sequencing with adaptive sampling (genomic-coordinate-based real-time read selection) targeting HRRs ±100 kb. Modification-aware basecalling distinguishes 6mA (accessibility) from 5mC (methylation).
- **4.8× enrichment of HRRs** with adaptive sampling; minor flow-cell-yield reduction is acceptable. Ratio-based methylation/accessibility quantification is robust to coverage depth.
- **Faithfully reproduces ATAC-seq accessibility and WGBS methylation patterns at genes/TEs**. Validated in CG-deficient (*met1*) and non-CG-deficient (*drm1 drm2 cmt2 cmt3*) mutants with expected methylation losses.
- **Strand-specific centromere epigenetics**: CEN180 repeats show **higher accessibility and lower CG/CHH methylation on the forward strand**, paralleling the known strand-asymmetric transcription of CEN180. Likely related to factors enriched at centromeres (RNA, R-loops, non-B DNA).
- **ATHILA retrotransposon islands** within centromeres have reduced accessibility and higher CHG methylation than surrounding CEN180 repeats — suppressing transposon mobility.
- **rDNA variants** (VAR1 silenced, VAR2/VAR3 active): VAR1 highly methylated and inaccessible; VAR2/VAR3 less methylated, more accessible. Same VAR class shows heterogeneity at the single-molecule level — hypomethylated vs hypermethylated sub-populations exist.
- **Telomere–subtelomere asymmetry**: lower accessibility and CHH methylation at telomeres vs adjacent subtelomeric regions, consistent with telomere heterochromatin.
- DNA-methylation-deficient mutants show **increased HRR accessibility**, confirming that DNA methylation maintains heterochromatic status in plant HRRs.

## Methods / evidence

Single-molecule nanopore with adaptive sampling, EcoGII methylation labeling (commercial enzyme that 6mA-methylates accessible regions in *Arabidopsis*, which has very low endogenous 6mA). Reference assemblies Col-CEN and Col-PEK (telomere-to-telomere). Mutant comparisons: *met1* (CG-deficient), *ddcc* (non-CG-deficient).

## Surprising or load-bearing bits

- **Adaptive sampling is the key methodological enabler**: nanopore's real-time read rejection turns the whole flow cell into a "targeted long-read sequencer" without prior capture or amplification. Adapts the high-cost HRR mapping problem to a cost-effective single-flow-cell experiment.
- The **strand-asymmetric accessibility at CEN180** is a novel biological finding made possible by single-molecule resolution — bulk methods average across strands.
- Plant centromeres differ from human centromeres: humans have centromere "dip regions" (hypomethylated zones for kinetochore formation) that *Arabidopsis* lacks. **Epigenetic centromere architecture is species-specific.**

## Connections to other sources

- Direct example of the long-read + methyltransferase footprinting paradigm reviewed by [[10-Summaries/profiling-the-epigenome-using-long-read-sequencing]] (Liu/Conesa 2025) and [[10-Summaries/yilei-2025-naturereviewsgenetics]] (Fu/Sedlazeck/Timp 2025).
- Conceptually parallel to SAMOSA / SAMOSA-Tag ([[10-Summaries/direct-transposition-of-native-dna-for-sensitive-multimodal-single-molecule-sequencing]]) in animals — same EcoGII-6mA strategy but combined with adaptive sampling rather than tagmentation.
- Demonstrates the HRR-mapping advantage of LRS, central to telomere-to-telomere assembly efforts and rDNA biology.

## Open questions

- Adaptive-sampling target design depends on prior knowledge of HRR coordinates — what about uncharacterized repetitive regions?
- Single-cell extension unattempted.

---
**Source:** [DOI](https://doi.org/10.1038/s41477-023-01498-7)
## Related

- [[40-Topics/long-read-sequencing]] · [[30-Concepts/stam-seq]] · [[30-Concepts/nanopore-adaptive-sampling]] · [[30-Concepts/highly-repetitive-regions]]
