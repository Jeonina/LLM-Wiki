---
type: summary
title: "Pančíková et al. 2025 — Long-read single-cell genome, transcriptome and open chromatin profiling links genotype to phenotypes (SPLONGGET)"
source: "[[00-Sources/papers/Long-read single-cell genome, transcriptome and open chromatin profiling links genotype to phenotypes.pdf]]"
source_quality: full
source_sha256: "82753e327c9d000ad6ac2be29112ddd5e8dc05640bc91b86e4600d157c5e23cf"
source_kind: paper
author: "Alexandra Pančíková, Ruben Cools, Marios Eftychiou, Margo Aertgeerts, Joris Vande Velde, Heidi Segers, Jan Cools, Luuk Harbers, Jonas Demeulemeester (corresponding)"
published: 2025-09-09
ingested: 2026-10-07
updated: 2026-10-07
doi: "10.1101/2025.09.08.674950"
journal: "bioRxiv (preprint)"
tags: [SPLONGGET, preprint, long-read, Oxford-Nanopore, 10x-Multiome, scDNA-seq, scATAC-seq, full-length-transcriptome, target-enrichment, genotype-to-phenotype, B-ALL, high-hyperdiploid, CD19, CAR-T, immune-escape, splice-site, LOH, structural-variants, CNA, SCENIC+]
entities: []
concepts: ["[[oxford-nanopore]]", "[[joint-single-cell-multi-omics]]", "[[scatac-seq]]", "[[tn5-tagmentation]]", "[[structural-variants]]", "[[copy-number-variation]]", "[[single-cell-variant-calling]]", "[[pseudo-bulk]]", "[[doublet-detection]]", "[[gene-regulatory-network]]", "[[intratumor-heterogeneity]]"]
topics: ["[[long-read-sequencing]]", "[[single-cell-multiomics]]", "[[scdna-cancer-applications]]", "[[hematopoietic-malignancies]]", "[[cancer-clonal-evolution]]"]
---

**Citation:** Pančíková et al. (2025) — *Long-read single-cell genome, transcriptome and open chromatin profiling links genotype to phenotypes* — *bioRxiv* (preprint, posted 2025-09-09; not peer-reviewed). [DOI](https://doi.org/10.1101/2025.09.08.674950)

# Pančíková 2025 — SPLONGGET

> SPLONGGET (Single-cell Profiling of LONG-read Genome, Epigenome, and Transcriptome) is a modified **10x Genomics Single Cell Multiome ATAC + Gene Expression** protocol read out on **Oxford Nanopore PromethION**. Tn5 tagmentation of nuclei produces fragments from ~35 bp to several kbp, but standard bead clean-ups, PCR and Illumina sequencing keep only the short ones, which is why ATAC data look like open-chromatin enrichment. SPLONGGET changes the clean-ups so **fragments of all sizes are retained**, switches to long-range PCR and omits cDNA fragmentation. The DNA library therefore carries sparse ATAC signal *plus* whole-genome coverage, and the cDNA library carries full-length transcripts, both under the same barcode pair. A biotinylated multiplex-PCR **target enrichment** step re-sequences chosen loci to saturation from the same libraries. Applied to four longitudinal bone-marrow samples from one paediatric high-hyperdiploid B-ALL (XG111: diagnosis plus three relapses, including after anti-CD19 CAR-T), it calls CNAs per cell and SNVs/SVs/allele-specific copy number from pseudobulks. It also detects the CAR vector and its integration sites, and finds **CD19-negative relapse driven by an 8 Mb chr16 deletion (LOH of *CD19*) plus four distinct splice-site SNVs** that long-read phasing places on distinct copies or subclones.

## Key claims

- **Library design.** SPLONGGET libraries span 300–3,500 bp (cDNA) and 200 bp to >10 kb (DNA), versus the narrow ranges of standard libraries. The workflow was optimised on RPMI-8402 cells. Nanopore was chosen because it is "independent of fragment length".
- **Throughput and yield (XG111).** 3,000 cells were targeted per time point, with cDNA and DNA libraries each run on two PromethION flow cells. Mean output was 175.7 M reads per DNA library and 169.2 M per cDNA library. Read-length N50 was 2,694 bp (DNA) and 854 bp (cDNA). Duplication averaged 21.1% (DNA) and 41.1% (cDNA).
- **Cells recovered.** 10,106 high-quality transcriptome cells (D0 1,808; Q1 3,897; Q2 2,051; Q3 2,350). 10,268 high-quality ATAC cells (D0 1,995; Q1 4,942; Q2 1,327; Q3 2,004). 3,800 high-quality single-cell copy-number profiles (D0 1,082; Q1 1,467; Q2 596; Q3 655), obtained with DNA libraries at "~20% saturation".
- **Backwards compatibility with short reads.** The Q3 libraries were re-processed into standard Illumina Multiome libraries. Genome coverage was much lower with short reads: 79–93% of the genome covered at ≥5× for SPLONGGET versus 6% for short reads. Per-barcode read counts correlated at Pearson r = 0.99 for both DNA and cDNA. 87% of cells received the same automated cell-type label in both read-outs, and clustering and marker-gene ATAC peaks were concordant.
- **Transcriptome layer.** On average 5,530 genes were differentially expressed per time point (range 3,972–7,106). *CD19* was downregulated at Q3, consistent with the clinical CD19-negative relapse. IsoQuant found 154,867 unique isoforms, 98,368 of them novel.
- **Accessibility layer.** 190,760 accessible regions were detected. ATAC clustering recapitulated the RNA clusters. 2,746 of the 10,268 ATAC cells lacked a passing transcriptome and were labelled by 5-nearest-neighbour majority vote. A small mid-erythroid population, misclassified as Q3 tumour from RNA alone, separated out in the ATAC data.
- **Single-cell CNAs.** Most CNAs were shared across all time points, including gains of chr6 and chr14. A chr5q gain and a simultaneous chr7p loss with chr7q gain, which suggests isochromosome formation, appeared only at later time points. InferCNVpy on the RNA and earlier DNA-amplicon data support the DNA-based calls.
- **Pseudobulk variant calling.** Cell-type labels split reads into a tumour pseudobulk and a matched-normal pseudobulk, so tumour–normal calling works from a single sample. ASCAT recovered the expected high-hyperdiploid karyotype: tetrasomy 21; trisomy 4, 6, 10, 14, 17 and 18; LOH of chrX; and copy-neutral LOH of chr3. Severus called 1,362 SVs (D0 1,231; Q1 1,221; Q2 1,038; Q3 1,184), with ~100 unique to a single time point. ClairS-TO called 28,785 SNVs (D0 14,429; Q1 16,561; Q2 17,133; Q3 18,923), and the number grew at later time points.
- **Targeted SPLONGGET.** Enrichment averaged 3,242-fold (DNA) and 4,402-fold (cDNA) at targeted regions. All variants previously found by MissionBio Tapestri were detected, including rare subclonal ones. On average 18.4% of cells could be genotyped per variant (range 0–75.1%), a 1,272.3-fold increase over untargeted SPLONGGET (0.01%). VAFs matched Tapestri (Fig. 4j, PCC = 0.92; Supp. Fig. 9k, DNA 0.83 and cDNA 0.96).
- **Gene regulatory networks.** SCENIC+ found direct eRegulons for 29 TFs. *ERG* was predicted to co-regulate 1,219 target genes in leukaemic cells. In 4,178 D0+Q1 tumour cells, the D0-specific *ETS2* and Q1-specific *JUN* eRegulons had observed-versus-expected target counts skewed on chr5 and chr7. Q1 expression and accessibility were lower on 7p and higher on 7q than at D0, matching the DNA copy-number change.
- **CAR-T detection.** CTAT-LR found *TNFRSF9*::*CD247* fusion transcripts only at Q3. Genomic reads containing the lentiviral LTR were assembled with Flye into a ~5 kb CTL019 vector contig. Realigning to hg38 plus this contig identified CAR-containing cells, all at Q3 and enriched in cytotoxic T cells. Supplementary alignments placed vector integration sites across nearly all chromosomes, indicating a polyclonal CAR-T population.
- **CD19 escape.** There is a Q3-specific 8 Mb chr16 deletion that includes *CD19*. The remaining copy carries three SNVs at the +1/+2 positions of the exon-4 5′ donor site (chr16:28,935,555 G>A; 28,935,556 T>C; 28,935,556 T>A) and one SNV at the −1 position of the exon-5 3′ acceptor (chr16:28,936,152 G>T). Long-read phasing shows the four variants sit on distinct copies or subclones, and VEP rates all four as likely high-impact. In the transcripts, the donor mutation gives intron retention and the acceptor mutation activates a cryptic intronic splice site. The authors call these SNVs "previously unreported" in CAR-T resistance and contrast them with the missense and nonsense mutations that dominate earlier reports.

## Methods / evidence

- **Wet lab.** Nuclei were isolated (10x CG000365) and 9,000 were targeted for transposition. The emulsion was broken for at least 3,000 nuclei. Pre-amplification used LongAmp Hot Start Taq with a 6-min extension, followed by a 1.6× SPRIselect clean-up "to retain fragments of all sizes". The ATAC library had 8 cycles with LongAmp and the cDNA was amplified with a 0.6× SPRI clean-up. Sequencing used Ligation Sequencing Kit V14 with Short Fragment Buffer, R10.4.1 flow cells and 72 h on a PromethION 24. The authors report ~80–100 M reads per flow cell and ~4,000 transcripts per cell for ~3,000 cells. The matching DNA "mean reads per cell" is left as a placeholder ("xxx") in the preprint.
- **Target enrichment.** Biotinylated 20–25-mer primers sit 3–300 bp from each target, with up to five targets per multiplex PCR. Input was 20 ng cDNA or 100 ng genome library. Products were pulled down on M280 streptavidin beads and amplified again in a post-pull-down PCR. Genotyping used cellsnp-lite, calling a variant at total depth ≥3 and alt depth ≥3 for cDNA, and ≥2 and ≥2 for DNA.
- **Compute.** Basecalling used dorado v0.7.2 (sup v5.0.0 model). RNA went through nf-core/scnanoseq v1.0.0 (nanofilt, BLAZE, minimap2, UMI-tools, IsoQuant). DNA went through the in-house IntGenomicsLab/scdnalong v0.0.1 (Flexiplex, minimap2, GATK MarkDuplicates).
- **ATAC analysis.** Reads <1 kb were used (SnapATAC2 fragment files → pyCisTopic with 25 topics; MACS2 on cell-type pseudobulks). Cells needed TSS enrichment ≥10 and ≥1,000 unique fragments.
- **Single-cell CNA.** ASCAT.sc on 500 kb bins, with GC lowess correction and multipcf (penalty 15).
- **Pseudobulk calling.** Used reads >1 kb. Clair3 called germline SNPs at 1000 Genomes loci and LongPhase did phasing and haplotagging. ASCAT v3.1 was adapted for long reads (loci_binsize 1200, aspcf penalty 150). Severus 1.1 ran in multi-sample tumour-only mode with ≥6 supporting reads. ClairS-TO 0.4.0 used minimum coverage 10. Private SNVs additionally needed QUAL >25, DP ≥30 and AF >0.15.
- **Doublets.** Scrublet "proved to be ineffective". Doublets were removed with hard thresholds (>20,000 RNA UMIs or >60,000 DNA reads). These thresholds were validated with a chr3 cn-LOH haplotype score, log2((ALT+1)/(REF+1)): cells with intermediate scores and high counts were called doublets.
- **Weight:** a preprint with **one patient** (four time points) plus a cell-line optimisation. Short-read concordance is shown on one time point (Q3). No orthogonal truth set is given for SV or SNV calls beyond the targeted Tapestri variants. Several placeholders remain (EGA accession "XXXX", "mean xxx reads per cell", private protocols.io link). Treat the performance numbers as single-sample demonstrations rather than benchmarks (synthesis).

## Surprising or load-bearing bits

- **"Keep every fragment" turns a commercial ATAC kit into a genome assay.** No separate WGA step is used. Whole-genome reads come from tagmentation fragments that standard protocols throw away, and nucleosomal ~150 bp periodicity is still visible in the DNA library (synthesis on Fig. 1f).
- **Untargeted per-cell genotyping is close to useless (0.01% of cells per variant).** Targeted re-amplification of the same libraries raises this to 18.4%. Discovery happens in pseudobulk and per-cell genotyping in a second, targeted pass. This answers the old stub's open question on single-cell genotype power (synthesis).
- **The cell-type layer supplies the matched normal.** Tumour and normal pseudobulks from one sample allow tumour–normal somatic calling without a separate germline sample, which helps for biopsies (synthesis on the authors' Discussion).
- **Phasing resolves parallel evolution.** Two hits at the same base (chr16:28,935,556 T>C and T>A) and two more at nearby splice sites are shown by long reads to lie on different copies or subclones. Without phasing this could look like one multi-allelic event (synthesis).
- **The CAR transgene can be assembled and mapped from the same data**, giving per-cell CAR presence in both RNA and DNA and polyclonal integration sites.
- **Accessibility caught what RNA missed:** a small mid-erythroid population was mislabelled as tumour from RNA alone.

## Concepts touched

- [[oxford-nanopore]]: length-independent readout of 200 bp to >10 kb Multiome fragments. Short Fragment Buffer is used to keep small fragments.
- [[tn5-tagmentation]]: tagmentation fragments of all sizes are retained, not only the short accessible-chromatin ones.
- [[scatac-seq]]: ATAC profiles are taken from the DNA reads below 1 kb. The Discussion points to Hu et al. (scNanoATAC-seq) for using all Tn5 sites.
- [[joint-single-cell-multi-omics]]: genome, accessibility and full-length transcriptome from one droplet barcode pair.
- [[copy-number-variation]]: per-cell CNAs (ASCAT.sc) and pseudobulk allele-specific CN (ASCAT), checked against InferCNVpy.
- [[structural-variants]]: Severus tumour-only SV calling on pseudobulks.
- [[single-cell-variant-calling]]: pseudobulk discovery followed by targeted per-cell genotyping (cellsnp-lite).
- [[pseudo-bulk]]: annotation-guided tumour and normal pseudobulks used as a matched pair.
- [[doublet-detection]]: an LOH-haplotype score replaces Scrublet.
- [[gene-regulatory-network]]: SCENIC+ eRegulons, and CNA effects on inferred regulon activity.
- [[intratumor-heterogeneity]]: parallel *CD19* escape alleles across subclones.

## Connections to other sources

- It positions itself against plate-based genome+transcriptome methods: [[macaulay-2015-gt-seq]] (G&T-seq), DNTR-seq, [[lindenhofer-2025-sdr-seq]] (SDR-seq) and scONE-seq. It names genotype-to-accessibility mapping ([[izzo-2024-got-cha]]) as the motivating need.
- [[pellegrino-2018-tapestri]] (the MissionBio Tapestri platform paper; not itself cited here): earlier Tapestri amplicon scDNA-seq of XG111, from Aertgeerts 2025 and Meyers 2022, is the genotype reference that SPLONGGET's targeted VAFs are compared against.
- [[bravo-2023-scenicplus]]: provides the GRN inference layer. pyCisTopic ([[bravo-2019-cistopic]] lineage) handles topic modelling.
- [[tickle-2019-infercnv]]: SPLONGGET uses its Python reimplementation (InferCNVpy) only as a cross-check, and argues that direct DNA CNAs avoid "circular" CNA inference from RNA or ATAC.
- Other long-read single-cell work: [[li-2025-scnanoatac-seq2]] (Nanopore single-cell ATAC), [[li-2024-scnanoseq-cut-tag]] (Nanopore single-cell CUT&Tag), [[hard-2023-long-read-scwgs]] (dMDA + PacBio long-read single-cell WGS, low throughput). SPLONGGET differs from these by using droplet Multiome barcoding at thousands of cells (synthesis). The review context is [[liu-2025-long-read-epigenome-review]] and [[vandereyken-2023-scmultiomics-review]].
- Analysis tools used: [[zhang-2024-snapatac2]], [[zhang-2008-macs]], [[mckenna-2010-gatk]], [[heumos-2023-best-practices]], [[traag-2019-leiden]].

## Open questions

- Per-cell DNA depth is never reported as a number (the Methods placeholder is "xxx"). Coverage per cell for single-cell genotyping in the untargeted library is visible only indirectly (0.01% of cells per variant genotypable).
- No allelic-dropout or false-positive estimates are given for single-cell genotypes. Tn5 insertion bias against closed chromatin in the "whole-genome" fraction is not quantified.
- One patient only. It is unknown whether the parallel splice-site escape is common under CAR-T, and the authors flag this themselves.
- Cost per cell, and how far DNA saturation (~20% here) can be pushed, are not evaluated.
- The Discussion suggests using all Tn5 sites, not just reads under 1 kb, for accessibility, but this is not tested.
