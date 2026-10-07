---
type: summary
title: "Chang et al. 2025 — Droplet Hi-C enables scalable, single-cell profiling of chromatin architecture in heterogeneous tissues"
source: "[[00-Sources/papers/Droplet Hi-C enables scalable, single-cell profiling of chromatin architecture in heterogeneous tissues]]"
source_kind: paper
author: "Lei Chang, Yang Xie, Brett Taylor, Zhaoning Wang, Jiachen Sun, Ethan J. Armand, Shreya Mishra, Jie Xu, Melodi Tastemel, Audrey Lie, Zane A. Gibbs, Hannah S. Indralingam, Tuyet M. Tan, Rafael Bejar, Clark C. Chen, Frank B. Furnari, Ming Hu, Bing Ren (corresponding)"
published: 2024-10-18
ingested: 2026-10-07
doi: "10.1038/s41587-024-02447-1"
journal: "Nature Biotechnology 43:1694–1707"
tags: [Droplet-Hi-C, Paired-Hi-C, single-cell-Hi-C, droplet-microfluidics, 10x-scATAC, ecDNA, HSR, glioblastoma, AML, CNV, structural-variants, multi-way-contacts, mouse-cortex]
entities: ["[[bing-ren]]", "[[ming-hu]]"]
concepts: ["[[single-cell-hi-c]]", "[[chromatin-compartments]]", "[[topologically-associating-domain]]", "[[chromatin-loop]]", "[[multi-way-chromatin-interaction]]", "[[copy-number-variation]]", "[[structural-variants]]", "[[joint-single-cell-multi-omics]]", "[[tn5-tagmentation]]", "[[imputation]]", "[[cell-type-annotation]]", "[[intratumor-heterogeneity]]", "[[convolutional-neural-network]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]", "[[single-cell-multiomics]]", "[[cancer-clonal-evolution]]"]
---

**Citation:** Chang et al. (2025) — *Droplet Hi-C enables scalable, single-cell profiling of chromatin architecture in heterogeneous tissues* — *Nature Biotechnology* 43:1694–1707. [DOI](https://doi.org/10.1038/s41587-024-02447-1)

# Chang 2025 — Droplet Hi-C

> Single-cell Hi-C had been stuck between **microwell methods** (deep per cell, but slow, costly, low scale) and **combinatorial indexing** (scalable but lengthy and manual). Droplet Hi-C sidesteps both by doing in situ Hi-C (digest + ligate inside fixed nuclei), removing histones with SDS, and then running the ligated nuclei through the **unmodified commercial 10x Genomics scATAC kit** — Tn5 fragments and droplet barcodes the 3C products. The result is ~10 h from fixed cells to libraries, 8 samples in parallel, ≥40,000 cells per run. The paper's second half shows the payoff is not only cortex cell-type 3D maps but **cancer genomics**: per-cell CNV, SVs and — the headline — a single-cell **ecDNA vs HSR classifier**, used to track ecDNA evolution under drug treatment in glioblastoma and AML. A Multiome-kit variant, **Paired Hi-C**, adds the transcriptome from the same nucleus.

## Key claims

- **Throughput and ease**: ~10 h protocol, 8 samples processed in parallel, profiling of "40,000 or more cells simultaneously"; throughput surpasses plate-based single-cell Hi-C "by an order of magnitude" with the shortest experimental and hands-on time to date (authors' Fig. 1b comparison).
- **Cell-line validation**: HeLa S3 + mESC species mix gave 1,773 human and 3,489 mouse high-quality cells (>1,000 read pairs) plus 284 potential doublets after shallow sequencing. A K562/GM12878/HeLa S3 mix gave 3,709 high-quality cells with median 108,439 unique read pairs per cell (duplication 23.9%), including 140 cells with mitotic-like contact patterns; compartment and insulation scores reproduced bulk in situ Hi-C. Even two karyotypically normal lines (GM12878, WTC-11) separated (2,236 and 1,202 cells, plus 231 mitotic cells).
- **Mouse cortex (8-week-old)**: 6,235 high-quality cells, median 175,021 unique read pairs/cell (22,456 *cis*-long >1 kb and 9,954 *trans* contacts per cell, 58% duplication). Distance decay, compartments and TAD boundaries were consistent with Dip-C and sn-m3C-seq; *cis*-long ratio higher than Dip-C but lower than sn-m3C-seq; "minimal open chromatin biases" despite Tn5 fragmentation.
- **Annotation via gene-body contacts**: cell-by-gene GAD (gene associating domain) scores co-embedded with snRNA-seq resolved **20 cell groups** (5 non-neuronal, 9 glutamatergic, 6 GABAergic), cross-validated by integration with sn-m3C-seq.
- **Minimum cells for features**: down-sampling ITL23GL neurons showed compartment/insulation correlations drop below **400 cells or <10 million long-range interactions**; loops probably need more reads.
- **Cortex 3D biology**: 895 regions with variable compartment scores linked to chromatin states; *Pdgfra* in an OPC-specific domain boundary; genes with variable expression more likely near variable TAD boundaries; H3K27ac enriched and H3K27me3 depleted at loop anchors; ~5% of 10 kb bins called as cell-type-specific **multi-way chromatin hubs** (≥3 bins per read pair), enriched at super-enhancers and marker genes.
- **ecDNA vs HSR from single-cell contacts**: in COLO320DM (*MYC* on ecDNA) vs COLO320HSR (*MYC* in HSR), aggregate Hi-C and adjnTIF both **failed** to distinguish the two forms, but per-cell features did — a **hub index** (Gini coefficient of a 1 Mb bin's interchromosomal contacts; lower = more even, ecDNA-like), inferred copy number (~47% more *MYC* copies in DM), and *trans*-to-*cis* contact ratio. A logistic-regression caller reached 0.99 specificity / 0.97 precision / 0.89 accuracy / 0.71 sensitivity; a CNN caller reached 0.80 sensitivity / 0.99 specificity / 0.93 accuracy / 0.99 precision and called *MYC* ecDNA in 96% of COLO320DM cells and HSR in 99.54% of COLO320HSR cells. No ecDNA was detected in a mouse cortex control (logistic model).
- **ecDNA evolution under erlotinib (GBM39, 9,204 cells)**: five chromatin-architecture clusters; cluster C2 nearly vanished, C0 expanded, C1/C3/C4 emerged. ecEGFR disappeared nearly completely after treatment; ecMDM2 appeared only in resistant cells (dominant in C3); ecMYC persisted with highly variable boundaries/internal structure after treatment (supported by *MYC* break-apart FISH); a rare ecChr18 (1.5%) and a *MYC* HSR in GBM39-ER (FISH-validated) were also called. 4.7% of C0 cells carried both ecMYC and ecEGFR. The authors reason erlotinib "probably induced" a new ecMYC population rather than selecting a pre-existing one.
- **Primary tumors**: an IDH-wildtype GBM sample separated malignant from non-malignant cells, showed chr7 gain/chr10 loss and ecEGFR (FISH-confirmed), a malignant-specific SV translocating *IKZF1* (without promoter) onto ecEGFR with decreased *IKZF1* transcription, a B→A switch at *SOX2-OT*, and 1,782 switched compartments between MES-like and OPC-like states. AC- and MES-like cells had higher ecEGFR copy number. In an MDS/secondary AML patient, a ~5 Mb ecMYC present pretreatment disappeared after azacitidine + venetoclax, along with a *MYC*–blood enhancer cluster loop.
- **Paired Hi-C** (10x Multiome kit; milder SDS, 0.6% vs 1% formaldehyde, revised cDNA prep): mouse cortex 12,361 joint profiles, 42,210 read pairs/cell Hi-C (66.2% duplication), median 3,914 UMIs and 1,746 genes/cell RNA; 20 cell types. Human PBMC: 7,585 profiles, RNA comparable to 10x Multiome and DOGMA-seq. In GBM39 under erlotinib, 1,066 A→B and 2,796 B→A compartment switches tracked expression changes; ecMYC 5′ genes (*CASC8*, *PCAT1*) tracked copy number while 3′ *CCDC26* was highly expressed despite low copy number.

## Methods / evidence

In situ Hi-C with three restriction enzymes (DpnII, MboI, NlaIII), 0.5% SDS, ligation in nuclei, FANS sorting, then 10x Chromium scATAC v1.1/v2 with modified PCR elongation and size selection. Processing: barcode extraction, BWA-MEM `-SP5M`, pairtools, Cooler. Analysis reuses existing single-cell Hi-C tools — Higashi embeddings for cell lines/tumors, scHiCluster imputation for cortex (no imputation for cancer samples because of CNV/SV), cooltools compartments/insulation/dots, TopDom, SnapHiC-style loop calling, dcHiC differential compartments, NeoLoopFinder for CNV (diploid assumption) and EagleC for SVs. ecDNA callers trained on COLO320DM/HSR and GBM39/GBM39-ER *MYC*/*EGFR* loci, with 90/10 train/validation cell splits. Validation by FISH in cell lines and tumor sections.

Weight: strong on scale and on the ecDNA application; the ecDNA classifier is trained and validated on essentially two cell-line pairs whose ecDNA status is known, so its generalisation to arbitrary tumors rests on the GBM/AML case studies plus FISH, not on an independent benchmark. The single-cell 3D-structure claims rest heavily on pseudo-bulk aggregation; per-cell depth (~42–175k read pairs) is modest. Note the logistic-regression threshold differed by dataset (0.5 vs 0.95).

## Surprising or load-bearing bits

- **A Hi-C assay run through an ATAC kit with "minimal open chromatin bias"** — the SDS histone stripping is presumably what makes Tn5 behave as a general fragmentase here. (synthesis)
- **Bulk-level ecDNA indicators failed where single-cell features worked**: aggregate interchromosomal patterns and adjnTIF could not tell ecDNA from HSR in COLO320, yet per-cell contact evenness could. This is a concrete case where single-cell resolution changes a classification, not just its granularity. (synthesis)
- ***cis*-short (<1 kb) contacts, normally discarded, are "valuable for analyzing CNVs and SVs"** — Droplet Hi-C doubles as a single-cell karyotyping assay, putting it in the same functional space as scDNA-seq CNV methods. (synthesis)
- **ecDNA also forms hubs**: COLO320DM's hub index, though lower than HSR, was higher than a shuffled background.
- **Treatment-induced, not selected, ecMYC** is an inference from structural dissimilarity of ecMYC within the same transition cluster — an interesting but indirect argument.

## Concepts touched

- [[single-cell-hi-c]] — droplet-microfluidic entry in the method family; a third axis beside microwell and combinatorial indexing.
- [[multi-way-chromatin-interaction]] — multi-way hubs called from pairtools `parse2`-rescued complex ligations in short-read single-cell data.
- [[copy-number-variation]] / [[structural-variants]] — inferred per cell from Hi-C contacts (NeoLoopFinder, EagleC).
- [[chromatin-compartments]], [[topologically-associating-domain]], [[chromatin-loop]] — cell-type-specific variation in cortex and GBM states.
- [[joint-single-cell-multi-omics]] — Paired Hi-C (Hi-C + RNA, 10x Multiome).
- [[tn5-tagmentation]] — Tn5 used as fragmentation/barcoding step on ligated chromatin.
- [[imputation]], [[cell-type-annotation]] — scHiCluster imputation and GAD-score co-embedding with snRNA-seq.
- [[intratumor-heterogeneity]] — ecDNA species and cell states within GBM.
- [[convolutional-neural-network]] — CNN ecDNA/HSR caller over 5 × 3,044 binarized contact matrices.

## Connections to other sources

- Earlier single-cell Hi-C methods it compares against or builds upon: [[nagano-2013-nature]], [[ramani-2017-scihi-c]] (sci-Hi-C), [[tan-2018-science]] (Dip-C), [[lee-2019-natmethods]] (sn-m3C-seq), [[liu-2023-mouse-brain-methylome-3d]] (BICCN mouse-brain sn-m3C-seq reference).
- Computational tools it uses (not benchmarks): [[zhang-2022-higashi]], [[zhou-2019-schicluster]], [[yu-2021-snaphic]], [[chakraborty-2022-dchic]], [[abdennur-2020-cooler]], [[li-2009-bwa]], [[korsunsky-2019-harmony]], [[traag-2019-leiden]], [[mcinnes-2018-umap]], [[butler-2018-seurat-cca]], [[mclean-2010-great]], [[heinz-2010-homer]].
- Listed among droplet-scale platforms in [[hong-2025-sc3d-genome-review]].
- Single-cell CNV calling from a non-DNA-seq modality parallels [[gao-2021-copykat]] / [[tickle-2019-infercnv]] (from RNA) and contrasts with direct scDNA-seq CNV callers such as [[zaccaria-2021-chisel]]. (synthesis)

## Open questions

- How well does the ecDNA/HSR CNN generalise beyond the *MYC*/*EGFR* loci and cell lines it was trained on? Sensitivity on the validation set was 0.80.
- Per-cell *cis*-long depth is lower than sn-m3C-seq; the authors suggest biotin enrichment of ligation junctions could help — untested here.
- Paired Hi-C library complexity is explicitly flagged as needing improvement; it currently relies on co-embedding with Droplet Hi-C to recover 3D features.
- CNV inference assumes diploid samples; how this behaves in highly aneuploid tumors is not discussed.

## Related

- [[single-cell-hi-c]] · [[40-Topics/3d-genome]] · [[bing-ren]] · [[ming-hu]]
