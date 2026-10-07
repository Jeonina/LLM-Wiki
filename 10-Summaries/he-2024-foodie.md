---
type: summary
title: "He et al. 2024 — Genome-wide single-cell and single-molecule footprinting of transcription factors with deaminase (FOODIE)"
source: "[[00-Sources/papers/Genome-wide single-cell and single-molecule footprinting of transcription factors with deaminase.pdf]]"
source_quality: full
source_sha256: "970d1952fcb2d392b94b1f7d17d5fb4339a69c872daa48b69d75738957ede467"
source_kind: paper
author: "Runsheng He, Wenyang Dong, Zhi Wang, Chen Xie, Long Gao, Wenping Ma, Ke Shen, Dubai Li, Yuxuan Pang, Fanchong Jian, Jiankun Zhang, Yuan Yuan, Xinyao Wang, Zhen Zhang, Yinghui Zheng, Shuang Liu, Cheng Luo, Xiaoran Chai, Jun Ren, Zhanxing Zhu, Xiaoliang Sunney Xie (corresponding)"
published: 2024-12-17
ingested: 2026-05-13
doi: "10.1073/pnas.2423270121"
journal: "PNAS 121(52):e2423270121"
aliases: ["He 2024 FOODIE", "FOODIE", "scFOODIE"]
tags: [FOODIE, scFOODIE, single-molecule-footprinting, deaminase, DddB, Tn5, single-cell-genomics, TF-binding, cooperativity, correlated-gene-module, Xie-lab, Peking]
entities: ["[[20-Entities/x-sunney-xie]]"]
concepts: ["[[single-molecule-footprinting]]", "[[tn5-tagmentation]]", "[[transcription-factor-motif]]", "[[chromatin-accessibility]]", "[[atac-seq]]", "[[dnase-seq]]", "[[chip-seq]]", "[[fiber-seq]]", "[[cell-type-annotation]]"]
topics: ["[[chromatin-architecture]]", "[[single-cell-atac-seq]]"]
created: 2026-05-13
updated: 2026-10-07
---

**Citation:** He et al. (2024) — *Genome-wide single-cell and single-molecule footprinting of transcription factors with deaminase* — *PNAS* 121(52):e2423270121. [DOI](https://doi.org/10.1073/pnas.2423270121) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/39689177/)

# He 2024 — FOODIE

> FOODIE (FOOtprinting with DeamInasE) adds one step to ATAC-seq: after Tn5 tagments open chromatin in permeabilised nuclei, the double-stranded DNA cytosine deaminase **DddB** converts C→U wherever no protein sits on the DNA. After PCR and short-read sequencing, a TF footprint is a run of unconverted cytosines inside an otherwise converted open region. Because every read is one DNA molecule, FOODIE gives each footprint a **binding fraction** and each pair of adjacent footprints a **cooperativity** value γ = ad/bc from counts of co-bound, singly bound and unbound molecules. Because the marks are sequence changes, they survive amplification, and a plate-based **single-cell FOODIE (scFOODIE)** first types cells from their accessibility and then pools cells of one type to footprint them. The authors use GM12878 footprints of 79 ChIP-seq-assigned TFs to argue that genes in a correlated gene module (CGM) share TFs: at promoters for housekeeping and cell-cycle modules, at enhancers for tissue-specific modules.

## Key claims

- **Enzyme choice.** DddA acts "only on cytosine preceded by thymine (TC)", which makes it "incapable of footprinting the majority of TFs bound to the genome". DddB (also known as BadTF3) "converts cytosine to uracil largely independent of adjacent bases", with minor biases "restricted mainly to the two bases neighboring the cytosine (−2 to +2)", corrected by measuring deamination on naked human DNA as a positive control. A second enzyme, MGYPDa829, also footprinted CTCF, but it deaminates "in a processive manner", so neighbouring conversions are correlated, which would confound cooperativity. All experiments therefore used DddB.
- **Cell input.** FOODIE "requires sequencing only thousands of cells, significantly fewer than those required for ChIP-seq or DNase-seq"; bulk reactions start from 30,000 nuclei.
- **CTCF benchmark (GM12878).** CTCF sites from FOODIE overlapped ENCODE ChIP-seq (1,486 FOODIE-only / 8,031 shared / 1,165 ChIP-only) and DNase-seq footprinting (5,929 / 3,588 / 2,023) (Fig. 1D). ChIP-seq has 200–500 bp resolution and "could not tell whether both or just one" of nearby CTCF motifs was occupied; FOODIE could. Fiber-seq, "limited by sequencing depth", did not match the resolution and accuracy of FOODIE or DNase-seq footprinting.
- **Large complexes.** FOODIE detected the footprint of SNAPc and RNA polymerase III at the *RN7SK* promoter, which DNase-seq footprinting did not.
- **Perturbation and genotype.** Heat shock reduced conversion within HSF motifs at the *HSP90AA1* promoter, consistent with HSF binding. An allele-specific T→A mutation in the promoter of ENSG00000279088 in GM12878 gave different NRF1 binding fractions on the two alleles. Fixed cells gave minimal differences from fresh cells, arguing against TF loss during preparation.
- **scFOODIE.** A mixture of GM12878, K562, HEK293T and HeLa separated into four clusters by UMAP of the accessibility signal, and pooling GM12878 cells recovered an NRF1 footprint (Fig. 2A). About 11,200 **mouse hippocampus** cells formed eight cell types; an AP-1 footprint appeared in hippocampal pyramidal cells and an SPI1 footprint was unique to microglia.
- **TF assignment is the bottleneck.** A footprint has many possible TF assignments from JASPAR and HOCOMOCO, so the authors kept only TFs with strong GM12878 ChIP-seq support. This gave "reliable assignments to only 79 known TFs". CTCF footprints sit upstream of the TSS and YY1 downstream, and a 10 bp oscillation in footprint positions was visible.
- **Shared TFs in correlated gene modules.** Using scMicro-C 3D structures of GM12878, genes of a CGM (for example MD20, cell cycle, 317 genes) are "not clustered but relatively randomly distributed within the nucleus". Of 61 GM12878 CGMs, many showed enrichment of specific TFs (hypergeometric test; BH FDR 0.05), for example E2F in the promoters of the MD16 cell-cycle CGM and RELB in the enhancers of the MD47 immune CGM; randomly drawn gene sets of 30–150 genes showed no enrichment. Enrichment was "primarily in promoters" for cell-cycle and housekeeping CGMs (NF-Y in the MD14 cholesterol module) and "primarily in enhancers" for tissue-specific CGMs (STAT3 in the MD48 immune module).
- **Cooperativity.** For two adjacent footprints, γ = ad/bc (a co-bound, b and c singly bound, d both unbound), interpreted thermodynamically as the factor by which each TF's binding constant changes when the other is bound, independent of TF concentration. RFX and CREB at the *HLA-DRA* promoter were positively cooperative ("all or none"); two NRF1 sites at the *ACTN4* promoter were negatively cooperative, γ ~ 0.4 (95% CI 0.23 to 0.55). Genome-wide, bootstrap CIs found **3,722 positively and 55 negatively cooperative** adjacent footprint pairs in GM12878, "more positive than negative".
- **Resource.** A FOODIE web server and genome browser (foodie.sunneyxielab.org) hosts the data; a "systematic FOODIE database of different human tissues is underway".

## Methods / evidence

Bulk FOODIE: 30,000 nuclei permeabilised (IGEPAL, Tween-20, digitonin), Tn5 tagmentation 30 min at 37 °C, then DddB deamination 10 min at 37 °C (45 min for fixed cells), proteinase K, purification, PCR with Q5U plus Bst 3.0 (uracil-tolerant), 10–12 cycles monitored by qPCR, Illumina 2 × 150 bp (2 × 250 bp for the cooperativity library). Deaminases were expressed in *E. coli* with their immunity proteins, then denatured in 8 M urea to remove the immunity protein and refolded. scFOODIE (cell lines): stained single nuclei sorted by FACS into 96-well plates after bulk tagmentation and deamination, with per-well barcodes added during PCR. scFOODIE (mouse hippocampus): a high-throughput workflow with 96 barcoded Tn5 complexes per plate, 6,000 nuclei per well, pooling, deamination, then 10 nuclei per well sorted into a second plate for a second barcode. Analysis: Trim Galore and Bismark (hg38 or mm10), C→T conversion per position corrected by naked-DNA conversion for all 4^6 contexts (−4 to +2); ArchR for scFOODIE QC (TSS enrichment > 4, > 10 unique fragments), LSI and UMAP; de novo footprints called by sliding windows with conversion lower than flanks (adapted from the Noble lab footprinting code); footprints overlapping single-molecule nucleosome calls (≥ 100 bp with ≤ 2 deaminated Cs per 100 bp window) excluded from cooperativity if > 10% of fragments overlapped. Binding states come from a **Bernoulli mixture model** on each strand (one to three clusters, five EM restarts, BIC selection; two clusters accepted only if ≥ 80% of cytosines separate), and a **debiased BMM** fits a, b, c, d by minimising the KL divergence between observed and theoretical conversion patterns to correct for incomplete deamination of unbound DNA; γ uncertainty is bootstrapped.

Weight: a methods paper with strong single-locus demonstrations and one genome-wide cooperativity analysis, all in GM12878. Validation against orthogonal data is a Venn overlap with ChIP-seq and DNase-seq for one TF (CTCF), plus a comparison table to other footprinting methods in the supplement; there is no ground-truth benchmark for binding fractions or γ. The single-cell result is cell typing plus pseudo-bulk footprints, not per-cell footprinting. The CGM conclusions rest on 79 assigned TFs out of ~1,600. The corresponding author contributed the paper (PNAS "Contributed" track), and four authors hold a patent application on the method. (synthesis)

## Limitations

**Authors' own:**
- One cell has one maternal and one paternal allele per gene, "insufficient to provide reliable statistics for TF footprints", so scFOODIE must pool "thousands of cells identified for a specific cell type".
- Most footprints cannot yet be assigned to TFs "because of the lack of binding affinities from databases and the intracellular concentrations"; only 79 TFs were assigned, and "a higher fraction is expected when TF footprints are fully assigned".
- Footprints near the edge of an open region can overlap nucleosomes and be miscounted; the nucleosome filter is conservative and may call ambiguous windows nucleosomal. Fragments not fully sequenced from both ends leave gap bases of unknown status.
- Deaminase batches vary, so titration is recommended to reach saturating conversion; incomplete conversion of unbound DNA biases γ, which the debiased BMM is designed to correct.

**Reviewer notes:**
- Short reads limit cooperativity to footprint pairs within one Tn5 fragment (≤ ~500 bp), unlike long-read deaminase methods that phase whole fibers and haplotypes. (synthesis)
- The 3,722 vs 55 positive/negative split may partly reflect detectability: positively cooperative pairs produce "all or none" patterns that a mixture model separates easily, while mutual exclusion needs both singly bound classes to be well populated. The paper does not test this with simulation at the genome-wide level. (synthesis)
- The brain demonstration is mouse hippocampus, not human tissue, and footprints shown there (AP-1, SPI1) are single loci. (synthesis)

## Surprising or load-bearing bits

- **Amplification-survivable marks on a standard ATAC library.** Because deamination writes C→T into the sequence, FOODIE runs on short-read Illumina and PCR, which is what makes the single-cell version possible; methyltransferase marks (m6A, GpC) need native long reads or bisulfite. (synthesis)
- **Enzyme processivity matters for cooperativity, not just sequence bias.** MGYPDa829 footprinted CTCF fine but was dropped because processive deamination correlates neighbouring sites, which would mimic cooperativity.
- **Promoter vs enhancer modes of module coordination.** Housekeeping and cell-cycle modules share TFs at promoters, tissue-specific modules at enhancers; the authors read this as robustness vs tunability.
- **Co-regulated genes are not co-localised.** scMicro-C structures show CGM genes scattered in 3D, so the paper argues coordination comes from shared TFs rather than transcription hubs.

## Entities mentioned

- [[20-Entities/x-sunney-xie]] — corresponding author (Peking University / Changping Laboratory); also cites his lab's Dip-C, scMicro-C and CGMFinder work.

## Concepts touched

- [[single-molecule-footprinting]] — short-read, deaminase-based, Tn5-enriched variant that reports binding fraction and pairwise cooperativity per footprint.
- [[tn5-tagmentation]] — tagmentation is done before deamination "to preserve Tn5 tagmentation efficiency" and restricts sequencing to open chromatin.
- [[transcription-factor-motif]] — JASPAR/HOCOMOCO motif overlap (> 50% of motif length) plus ChIP-seq support to assign footprints.
- [[dnase-seq]] / [[chip-seq]] — CTCF benchmark comparators.
- [[fiber-seq]] — long-read comparator, judged depth-limited for TF footprinting.
- [[atac-seq]] / [[chromatin-accessibility]] — FOODIE is ATAC-seq plus one enzymatic step.
- [[cell-type-annotation]] — scFOODIE cell typing via ArchR and marker genes.

## Connections to other sources

- Closest contemporary: [[swanson-2025-daf-seq]] also footprints with a dsDNA deaminase but reads long fibers and phases haplotypes; FOODIE trades fiber length for short-read cost and per-TF resolution. (synthesis)
- Methyltransferase-based single-molecule predecessors: [[andrewb-2020-science]] (Fiber-seq, the comparator here), [[pott-2017-elife]] (GpC MTase scNOMe-seq), [[doughty-2024-smf-tf]] (SMF with M.CviPI, which the paper notes covers only GpC-containing sequence).
- 3D-genome lineage from the same lab: [[tan-2018-science]] (Dip-C).
- Other single-molecule chromatin readouts: [[altemose-2022-dimelo-seq]], [[peter-2024-brain-fiberseq]].

## Open questions

- How accurate are FOODIE binding fractions and γ against an orthogonal truth set (e.g., in vitro reconstitution or CAP-SELEX pairs)? (synthesis)
- Can scFOODIE footprint without pooling, for example at high-occupancy sites, or is pseudo-bulk the floor?
- How many of the unassigned footprints are real TF binding, and does full assignment change the promoter/enhancer CGM pattern?
- The promised human tissue FOODIE database and its application to clinical samples are not shown here.

## Related

- [[single-molecule-footprinting]] · [[swanson-2025-daf-seq]] · [[doughty-2024-smf-tf]] · [[altemose-2022-dimelo-seq]] · [[peter-2024-brain-fiberseq]] · [[pott-2017-elife]] · [[40-Topics/chromatin-architecture]]
