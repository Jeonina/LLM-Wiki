---
type: summary
title: "Wang et al. 2024 — Single cell genome and epigenome co-profiling reveals hardwiring and plasticity in breast cancer"
source: "[[00-Sources/papers/Single cell genome and epigenome co-profiling reveals hardwiring and plasticity in breast cancer.pdf]]"
source_quality: full
source_sha256: "c44dbb7cbedbe30a816db531014f45605997188df187db4f184604d6d655ed4f"
source_kind: paper
author: "Kaile Wang*, Yun Yan*, Heba Elgamal*, Jianzhuo Li, Chenling Tang, Shanshan Bai, Zhenna Xiao, Emi Sei, Yiyun Lin, Junke Wang, Jessica Montalvan, Changandeep Nagi, Alastair M. Thompson, Nicholas Navin (corresponding) (*equal contribution)"
published: 2024-09-10
ingested: 2026-10-07
updated: 2026-10-07
doi: "10.1101/2024.09.06.611519"
journal: "bioRxiv (preprint, not peer reviewed)"
tags: [wellDA-seq, scDNA-seq, scATAC-seq, genome-epigenome-co-profiling, copy-number-aberration, breast-cancer, ER-positive, cell-of-origin, nanowell, Tn5, preprint]
entities: ["[[nicholas-navin]]", "[[smaht-network]]"]
concepts: ["[[joint-single-cell-multi-omics]]", "[[copy-number-variation]]", "[[chromatin-accessibility]]", "[[scatac-seq]]", "[[intratumor-heterogeneity]]", "[[tn5-tagmentation]]", "[[icell8-nanowell]]", "[[phylogenetic-inference]]", "[[doublet-detection]]"]
topics: ["[[scdna-cancer-applications]]", "[[cancer-clonal-evolution]]", "[[single-cell-multiomics]]", "[[somatic-mosaicism]]"]
---

**Citation:** Wang et al. (2024) — *Single cell genome and epigenome co-profiling reveals hardwiring and plasticity in breast cancer* — *bioRxiv* 2024.09.06.611519 (preprint, posted 10 Sep 2024). [DOI](https://doi.org/10.1101/2024.09.06.611519)

# Wang 2024 — wellDA-seq

> **Version note:** the source PDF is the **bioRxiv preprint** (every page carries the bioRxiv header "this version posted September 10, 2024 … not certified by peer review"); 28 pages: main text, methods and main figures 1–6. Extended Data and Supplementary Tables are not included. Crossref (checked 2026-10-07) lists no journal version linked to this DOI.
>
> wellDA-seq (nano**well** **D**NA & **A**TAC) measures genome-wide copy number and chromatin accessibility in the same single cell by **two sequential, differently-barcoded Tn5 tagmentations**: Tn5-1 marks open chromatin in bulk permeabilised nuclei; then, after dispensing single nuclei into an ICELL8 nanowell chip and **protease-stripping all chromatin in the well**, Tn5-2 tagments the remaining (previously closed) DNA. Physical compartmentalisation is what lets it remove nucleosomes completely for even DNA coverage, the trade-off the authors say limited earlier co-assays (scGET-seq, dTag). In 2 normal breasts and 9 ER+ breast cancers (22,123 cells overall) it finds rare LumSec-identity aneuploid cells (chr1q gain, chr10q loss) in normal tissue, chrX-loss T cells and pericytes in tumours, LumHR-like ancestral cancer clones that progressively lose LumHR identity, ~82% of subclone-to-subclone chromatin-hub differences sitting on subclonal CNA bins (*cis*), and tumour-to-tumour variation between "hardwired" and "plastic" genotype–epigenotype relationships.

## Key claims

- **Assay design.** Tn5-1 (custom-loaded adapters) tagments open chromatin in ~30–35k permeabilised nuclei in bulk; DAPI-stained nuclei are dispensed into a **5,184-nanowell** ICELL8 chip and imaged, keeping only single-cell wells (**1,200–2,600 per chip**) to avoid doublets, degraded nuclei and empty wells. Each well is lysed with a protease buffer to "completely remove the chromatin", then tagmented with Tn5-2 (Illumina). Combinatorial **72 × 72 DNA and 72 × 72 ATAC index primers** dispensed per well give each cell a barcode; pooled products are split into DNA and ATAC libraries by modality-specific PCR.
- **"First" claim.** The authors call wellDA-seq "the first high-genomic resolution, high-throughput" single-cell whole-genome + chromatin-accessibility co-assay (their claim; scGET-seq and dTag are cited as prior co-assays with lower genomic resolution).
- **ATAC quality (MDA-MB-231).** TSS enrichment and unique-fragment numbers comparable to 10x Genomics scATAC on the same line; aggregate accessibility correlates with 10x at **R = 0.91 and 0.92** and between the two wellDA-seq replicates at **R = 0.99**.
- **DNA quality.** Against four unimodal scDNA methods (**Arc-well, 10x Genomics CNV, DLP+, DOP-PCR**; 120 randomly downsampled cells each), overdispersion was similar to Arc-well and significantly lower than the other three; breadth of coverage at a matched **750K reads per cell** was significantly higher than 10x, DLP+ and DOP-PCR (p < 2.2e-16, Wilcoxon).
- **Dual-modality yield.** **78.71% and 74.88%** of QC-passing cells had both modalities in the two replicates (1,623 and 1,455 shared cells).
- **ATAC cannot resolve subclones.** In 2,603 MDA-MB-231 cells, DNA gave 3 superclones / 7 subclones; ATAC gave 3 clusters matching the superclones, but subclones C4–C7 intermixed in one ATAC cluster.
- **ATAC-inferred CNA is unreliable.** CNAs inferred from wellDA-seq's own ATAC (method of Satpathy et al., 10-Mb windows) correlated with the measured CNAs at only **median R = 0.47**, with many false-positive events; in tumours P3, P5 and P10 the inferred profiles resolved none of the clonal substructure seen in the DNA, with false positives concentrated in diploid regions.
- **Normal breast.** P1 (late-20s donor, 1,339 cells): **10 aneuploid cells (0.75%)**, all LumSec by ATAC, carrying a 1q gain plus losses on chr9, 10q or 16q. P2 (early-40s donor, 1,115 cells): **5 aneuploid cells (0.45%)**, all LumSec, all with 1q gain, one also with 10q loss.
- **Tumour cohort.** **19,669 cells from 9 ER+ tumours (3 DCIS, 6 invasive)**; mean 2,185 cells (SEM 197) and 1,088 cancer cells (SEM 298) per tumour; **10,054 cells (51.11%)** had CNAs. ATAC clustering gave 8 normal cell types plus 9 LumHR-like (cancer) clusters; aneuploid cells sat almost entirely in LumHR-like clusters and formed patient-specific clusters, whereas diploid cells intermixed across patients. 1q gain and 16q loss were the most frequent events.
- **CNAs outside the epithelium.** **225 aneuploid non-epithelial cells**: **80.88% had chrX loss**, mostly in T cells (68%) and pericytes (25%), across multiple patients. chrX loss frequency was **4.30% of 2,838 T cells**, **0 of 911 myeloid cells**, and **5.50% (49/891) of pericytes**; the pericyte finding is described as not previously reported.
- **Ancestral cells and cell-of-origin.** In 6 tumours (P4–P6, P8–P10) the authors identified ancestral subclones by MEDICC2 phylogeny on consensus integer CNAs and scored their ATAC against Basal/LumHR/LumSec epithelial modules. In P10 (1,203 cells, 6 subclones) the ancestral clone C6 carried 4 CNA events and had the highest LumHR score; in P6 (1,734 cells, 15 subclones) the ancestor C1 carried 16q and 18p losses. Ancestral cells were LumHR-derived in all 6, though in P4 and P9 the ancestor did not have the highest LumHR score among subclones.
- **Loss of lineage identity.** Across the 6 tumours, LumHR module score fell with CNA distance from diploid (**R = −0.51, p = 0.29 × 10⁻³**); chr16q loss was an ancestral event in 3 tumours and chr1q gain in 2.
- **Cis effects of subclonal CNAs.** In P8 (382 cells, 4 subclones), C1 vs C4 had **780 subclonal genomic bins (SGBs)**, **36 differentially accessible peaks** (28 of 29 peak-bearing bins = 96.55% were SGBs) and **420 bins with differentially accessible chromatin hubs (DACHs, from Cicero)**, of which **340 overlapped SGBs**: "EbyG" = 340/420 = **80%**, "GtoE" = 340/780 = **43%**. Example: *IGF1R* had fewer copies and concordantly fewer ATAC fragments in C1.
- **Across all tumours.** 128 of 142 subclone comparisons had DACHs; absence of DACHs tracked smaller phylogenetic distance rather than cell or fragment number. Mean **EbyG 82.27% (SEM 2.59%)**, mean **GtoE 25.12% (SEM 1.85%)**; SGB count correlated with DACH count (**R = 0.63**). The discussion reads the remaining **17.73%** of accessibility changes as *trans* effects of CNAs.
- **Hardwiring vs plasticity.** A "global concordance" score = Pearson correlation between subclone-pairwise CNA (Manhattan) and ATAC (top 30 LSI) distances; per-hallmark heritability = correlation of ATAC-module-score distances with CNA distances. Concordance ranged **0.43–0.99** across tumours (mean 0.73, SEM 0.07, over the 7 samples besides P6 and P10); "about half" of tumours were highly concordant. Recurrent heritable programs: reactive oxygen species, myogenesis, apoptosis, P53; recurrent plastic programs: G2M checkpoint, coagulation, EMT, interferon-gamma response.
- **Data and IP.** SRA PRJNA1081815, GEO GSE260864, code at github.com/navinlabcode/wellDA-seq. A US patent application (PCT/US2024/018634) has been filed.

## Methods / evidence

- **DNA processing:** Bowtie2 to hg19, ~220-kb variable bins, LOWESS GC correction, CBS (DNAcopy) and mergeLevels, then CopyKit for log-ratio, integer copy number (segment ratio × 2) and clustering; low-quality cells removed by mapping quality, <100,000 reads, or >10% empty bins. Tumour samples were split into tentative diploid/aneuploid groups first, because CopyKit's default outlier filter "was likely to remove the rare cells harboring small CNA events". Non-diploid subclones correlating with an aneuploid subclone but with lower log-ratio were labelled **doublets** (diploid contamination) and removed. A CNA call required segment ratio >1.3 or <0.7.
- **ATAC processing:** scATAC-pro, MACS2 peaks, Signac (TF-IDF, LSI, UMAP), ArchR TSS scores; cells kept with >1,000 fragments and TSS enrichment >6. Cell types from Signac gene-activity scores, hdbscan clustering and marker genes. Only cells passing QC in both modalities were analysed.
- **Lineage and statistics:** MEDICC2 trees on consensus integer profiles; minimum-evolution (ape fastme.bal) trees on Manhattan distances for the hardwiring analysis; SGBs by per-bin Wilcoxon (BH); DAPs and DACHs by Wilcoxon (Bonferroni) with log2FC > log2(1.1); GSEA via a module-based approach; hallmark scores via UCell on Cicero-inferred expression. Subclones with <15 cells were excluded from GtoE/EbyG unless >3% of the sample; P5 was excluded from the heritability analysis because it had no DACHs.

Weight: a well-documented preprint from an experienced scDNA lab, with orthogonal benchmarks for both modalities in a cell line and independent replicate runs. But the cohort is small (2 normals, 9 ER+ tumours; the authors call it a proof of concept), DNA is sparse (750K-read comparisons; the authors state it is "not amenable for mutation detection"), and the biology rests on rare-cell calls: 15 aneuploid cells in normal tissue and 225 non-epithelial aneuploid cells, with no orthogonal validation (e.g., FISH) described in the main text. The doublet filter is CNA-pattern-based, while cell type comes from the same cell's ATAC; that makes the LumSec and T-cell/pericyte assignments more direct than inference, but a tumour–stromal collision would still read as an "aneuploid stromal cell" if it escaped imaging and the filter. (synthesis) The heritability/plasticity results are correlations between distance matrices across often few subclones, and the expression readout is inferred from ATAC (Cicero gene activity), not measured. (synthesis)

## Surprising or load-bearing bits

- **Protease in the well is the trick.** Separating the "open" and "rest-of-genome" reads by two Tn5s with different adapters, and stripping chromatin only after single nuclei are isolated in nanowells, avoids the nucleosome-removal vs nuclear-integrity paradox the authors identify in droplet-style co-assays. The DNA library is therefore the complement of the ATAC library in tagmentation terms, not a re-read of it.
- **ATAC-inferred CNA fails on real tumours here.** Median R = 0.47 to measured CNAs and no recovered substructure in three tumours is a strong same-cell negative result for CNA-from-scATAC inference, although only one inference method (Satpathy-style 10-Mb windows) was tested. (synthesis)
- **Normal-breast aneuploid cells are LumSec, not LumHR,** while ER+ cancers originate from LumHR — so the recurrent 1q gain in normal LumSec cells and in cancers is not shown to be on the same lineage path. (synthesis)
- **chrX loss in tumour pericytes (5.5%)** is a new microenvironment observation; chrX loss in T cells echoes a cited colorectal-cancer multi-omics study.
- **Internal inconsistency:** P6's global concordance is "0.48" in the results text but 0.55 in Fig. 6c and 6i (P10 is also 0.55). The abstract's "6 estrogen-receptor positive breast cancers" refers to the ancestral-cell subset; all 9 tumours are described as ER+ in the results. The text cites the MSigDB hallmark database as ref. 15, which is Laks et al. (DLP+), a citation slip.

## Entities mentioned

- [[nicholas-navin]] — corresponding author (MD Anderson Department of Systems Biology).
- [[smaht-network]] — named in the discussion as a setting for future multi-tissue somatic-mosaicism studies with wellDA-seq.

## Concepts touched

- [[joint-single-cell-multi-omics]] — same-cell DNA copy number + chromatin accessibility at thousands-of-cells scale.
- [[tn5-tagmentation]] — two sequential Tn5 loadings with different adapters separate open from closed chromatin.
- [[icell8-nanowell]] — 5,184-nanowell chip with DAPI imaging for single-cell well selection; compartmentalisation enables full chromatin removal.
- [[copy-number-variation]] — CNAs define subclones; rare CNAs in normal LumSec cells and chrX loss in stromal/immune cells.
- [[chromatin-accessibility]] / [[scatac-seq]] — cell type, epithelial lineage score, DACHs, hallmark programs.
- [[intratumor-heterogeneity]] — hardwiring vs plasticity across subclones; tumour-level concordance 0.43–0.99.
- [[phylogenetic-inference]] — MEDICC2 and minimum-evolution trees on consensus integer CNAs.
- [[doublet-detection]] — imaging-based single-cell well selection plus a CNA-correlation doublet filter.

## Connections to other sources

- Same lab's scDNA lineage: [[navin-2011-sns-tumor-evolution]], [[wang-2014-nuc-seq]], [[kim-2018-tnbc-chemoresistance]]; wellDA-seq adds a same-cell epigenomic layer to that CNA-lineage approach.
- Benchmarked against DLP+ ([[laks-2019-dlp-plus]]) and 10x CNV, Arc-well and DOP-PCR on overdispersion and breadth of coverage.
- Uses [[kaufmann-2022-medicc2]] for trees, [[pliner-2018-cicero]] for chromatin hubs, [[granja-2021-archr]] for TSS scores, and Signac ([[stuart-2021-natmethods]]) for ATAC processing.
- **Tension with CNA-from-scATAC methods:** [[ramakrishnan-2023-epianeufinder]] reports pseudo-bulk correlation 0.86 with scWGS on a cell line, whereas wellDA-seq's same-cell comparison of an ATAC-inference method gave median R = 0.47 and missed tumour substructure. Different inference methods and per-subclone vs pseudo-bulk evaluation, so not directly contradictory, but wellDA-seq is the stronger same-cell test. (synthesis) Expression-based inference ([[gao-2021-copykat]], [[tickle-2019-infercnv]]) faces the same lack of same-cell ground truth.
- Earlier genome-plus-other-layer single-cell co-assays: [[hou-2016-sctrio-seq]] (genome, methylome and transcriptome), [[macaulay-2015-gt-seq]] (genome plus transcriptome).
- ICELL8 nanowell chemistry precedents: [[mezger-2018-microfluidic-atac]], [[janssens-2023-scicut-tag]].

## Open questions

- Orthogonal validation (FISH or targeted sequencing) of the rare LumSec aneuploid cells and chrX-loss pericytes; neither the main text nor the main figures show it.
- Per-cell DNA read depth and genomic resolution in the tumour data beyond the ~220-kb bins; the authors note sparse coverage precludes SNV detection.
- How sensitive the concordance and heritability scores are to the number of subclones per tumour, and which value (0.48 or 0.55) is correct for P6.
- Whether the *trans* fraction (17.73%) reflects CNAs in transcription factors/epigenetic regulators, as the authors speculate, or residual noise.
- Re-check against the peer-reviewed version when one appears; Extended Data and Supplementary Tables were not in this source.

## Related

- [[nicholas-navin]] · [[joint-single-cell-multi-omics]] · [[40-Topics/scdna-cancer-applications]] · [[40-Topics/single-cell-multiomics]] · [[ramakrishnan-2023-epianeufinder]]
