---
type: topic
title: Cancer clonal evolution
explainer: cancer-clonal-evolution
aliases: [tumor clonal evolution, cancer phylogeny, tumor evolution]
tags: [cancer, clonal-evolution, phylogeny, intratumor-heterogeneity]
created: 2026-05-19
updated: 2026-10-12
paper_section: ["5.1"]
---

# Cancer clonal evolution

> The accumulation of somatic mutations and clonal selection that shapes tumor heterogeneity, treatment response and metastasis. Reconstructing tumor phylogenies from bulk and single-cell DNA reveals the order of driver events, clonal sweep dynamics and chemoresistance lineages ([[10-Summaries/navin-2011-sns-tumor-evolution|Navin 2011]]; [[10-Summaries/kim-2018-tnbc-chemoresistance|Kim 2018]]).

> [!abstract] 한눈에
> 종양 세포는 체세포 변이와 클론 선택을 거치며 여러 계통으로 갈라지고, single-cell DNA로 그 계통수를 재구성하면 driver 변이의 순서와 약물 내성 계통을 읽을 수 있다 ([[10-Summaries/navin-2011-sns-tumor-evolution|Navin 2011]]; [[10-Summaries/kim-2018-tnbc-chemoresistance|Kim 2018]]). 분석 도구는 SNV만 쓰던 계통수에서 copy number와 WGD까지 함께 다루는 모델로 넘어가 수만 개 세포 규모로 확장되고 있다 ([[10-Summaries/sollier-2023-compass|COMPASS]]; [[10-Summaries/zhang-2025-scistree2|ScisTree2]]; [[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [종양 계통수 시뮬레이터](../60-Explainers/cancer-clonal-evolution.html)
<!-- /explainer-links -->

## Key points

- **Copy-number change and point mutation run on different clocks.** In breast cancer, aneuploid rearrangements arose early and stayed frozen while point mutations accumulated gradually ([[10-Summaries/wang-2014-nuc-seq|Wang 2014]]); single-nucleus CNV profiles first showed punctuated clonal evolution ([[10-Summaries/navin-2011-sns-tumor-evolution|Navin 2011]]).
- **Tumours often hold several codominant clones.** Five of six childhood ALL patients had codominant clones, and structural variants preceded point mutations ([[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]).
- **Tree models moved past SNV-only, infinite-sites assumptions.** Later methods allow finite sites, mutation loss and joint SNV + CNA inputs ([[10-Summaries/zafar-2017-sifit|SiFit]]; [[10-Summaries/el-kebir-2018-sphyr|SPhyR]]; [[10-Summaries/satas-2020-scarlet|SCARLET]]; [[10-Summaries/sollier-2023-compass|COMPASS]]), and now scale to tens of thousands of cells ([[10-Summaries/zhang-2025-scistree2|ScisTree2]]).
- **Whole-genome doubling is an ongoing process, not a one-off event.** In 30,260 HGSOC tumour genomes WGD raised chromosomal instability yet repressed STING1 ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]); new copy-number callers target WGD directly ([[10-Summaries/wesley-2026-songbird|Songbird]]; [[10-Summaries/schneider-2024-scabsolute|scAbsolute]]; [[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]).
- **Clone-resolved genotypes still need single-cell data.** Bulk cancer-genome foundation models such as TESSERA learn from purity-adjusted, sample-level segments and encode no subclonal or cell-level structure ([[10-Summaries/sidhom-2026-tessera|TESSERA]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/phylogenetic-inference|Phylogenetic inference]] — Reconstructing a cell-division tree from heritable markers; model × search-strategy table.
> - `concept` [[30-Concepts/intratumor-heterogeneity|Intratumor heterogeneity]] — Variation between cells within one tumour, and the clone-detection design rule.
> - `concept` [[30-Concepts/copy-number-variation|Copy-number variation]] — Gains and losses of genomic segments; the most tractable single-cell readout.
> - `concept` [[30-Concepts/whole-genome-doubling|Whole-genome doubling]] — Duplication of the whole chromosome complement and how single cells reveal it.
> - `concept` [[30-Concepts/chromosomal-instability|Chromosomal instability]] — The rate of mis-segregation, as opposed to aneuploidy, the resulting state.
> - `concept` [[30-Concepts/lineage-tracing|Lineage tracing]] — Reconstructing cell ancestry from natural or synthetic marks.

## Foundational studies

| Study | Tumour | Design | Key finding |
|---|---|---|---|
| [[10-Summaries/navin-2011-sns-tumor-evolution\|Navin 2011]] | Breast | Single-nucleus CNV | Punctuated clonal evolution ([[10-Summaries/navin-2011-sns-tumor-evolution\|Navin 2011]]) |
| [[10-Summaries/xu-2012-single-cell-exome-kidney\|Xu 2012]] | ccRCC | Single-cell exomes, 17 cells | No detectable subclonal structure and no *VHL* or *PBRM1* driver — the counterexample ([[10-Summaries/xu-2012-single-cell-exome-kidney\|Xu 2012]]) |
| [[10-Summaries/wang-2014-nuc-seq\|Wang 2014]] | Breast (TNBC, ER⁺) | nuc-seq, deep per cell | Rearrangements early and frozen, point mutations gradual; a birth–death model gives a 13.3× elevated mutation rate in the TNBC and a normal-cell rate in the ER⁺ tumour (n = 1 each) ([[10-Summaries/wang-2014-nuc-seq\|Wang 2014]]) |
| [[10-Summaries/gawad-2014-all-clonal-origins\|Gawad 2014]] | Childhood ALL | 1,479 cells, targeted loci | Codominant clones in 5/6 patients; 13/16 deletions present in all clones; *KRAS* late and not sufficient for dominance; clones arrested at different B-cell stages ([[10-Summaries/gawad-2014-all-clonal-origins\|Gawad 2014]]) |
| [[10-Summaries/zahn-2017-dlp\|Zahn 2017]] | Xenograft, serial passages | DLP, 782 cells, amplification-free | Minor clones vanish and the dominant clone diversifies across passages ([[10-Summaries/zahn-2017-dlp\|Zahn 2017]]) |
| [[10-Summaries/kim-2018-tnbc-chemoresistance\|Kim 2018]] | TNBC | Longitudinal scDNA + scRNA through neoadjuvant chemotherapy, 20 patients | Pre-existing versus acquired resistance ([[10-Summaries/kim-2018-tnbc-chemoresistance\|Kim 2018]]) |
| [[10-Summaries/frankell-2019-eac-landscape\|Frankell 2019]] | Esophageal adenocarcinoma | Bulk, 551 tumours | Selection landscape of EAC ([[10-Summaries/frankell-2019-eac-landscape\|Frankell 2019]]) |
| [[10-Summaries/mcpherson-2025-ongoing-wgd\|McPherson 2025]] | HGSOC | DLP+, 30,260 tumour genomes | WGD is ongoing; it raises CIN but represses STING1 ([[10-Summaries/mcpherson-2025-ongoing-wgd\|McPherson 2025]]) |

Process-level interpretation of passenger mutations comes from 21 mutational signatures across 7,042 cancers ([[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]). See [[30-Concepts/intratumor-heterogeneity]] for the consolidated argument.

## Phylogeny methods

The 2016–2019 generation was designed for fewer than 100 cells, which is why mixture models were rejected ([[10-Summaries/ross-2016-onconem|OncoNEM]]); these methods should be re-evaluated against droplet-scale data ([[10-Summaries/pellegrino-2018-tapestri|Tapestri]]) (synthesis). See [[30-Concepts/phylogenetic-inference]] for the model × search-strategy table.

| Tool | Year | Input | Model or search | Note |
|---|---|---|---|---|
| [[10-Summaries/jahn-2016-scite\|SCITE]] | 2016 | SNV | MCMC over mutation histories | One of the founding single-cell tumour-tree methods ([[10-Summaries/jahn-2016-scite\|SCITE]]) |
| [[10-Summaries/ross-2016-onconem\|OncoNEM]] | 2016 | SNV | Nested effects models | Infers unobserved subpopulations ([[10-Summaries/ross-2016-onconem\|OncoNEM]]) |
| [[10-Summaries/zafar-2017-sifit\|SiFit]] | 2017 | SNV | Finite-sites model | ([[10-Summaries/zafar-2017-sifit\|SiFit]]) |
| [[10-Summaries/el-kebir-2018-sphyr\|SPhyR]] | 2018 | SNV | *k*-Dollo | Because CNAs delete SNVs constantly ([[10-Summaries/el-kebir-2018-sphyr\|SPhyR]]) |
| [[10-Summaries/singer-2018-sciphi\|SCIΦ]] | 2018 | SNV | Joint calling + tree by MCMC | ([[10-Summaries/singer-2018-sciphi\|SCIΦ]]) |
| [[10-Summaries/malikic-2019-phiscs\|PhISCS]] | 2019 | SNV + bulk VAF | Subperfect phylogeny; ILP and Boolean CSP | ([[10-Summaries/malikic-2019-phiscs\|PhISCS]]) |
| [[10-Summaries/zafar-2019-siclonefit\|SiCloneFit]] | 2019 | SNV | Tree-structured CRP, finite sites | Joint clone clustering and genotyping, with a doublet model ([[10-Summaries/zafar-2019-siclonefit\|SiCloneFit]]) |
| [[10-Summaries/satas-2020-scarlet\|SCARLET]] | 2020 | SNV + CNA | Copy-number-constrained SNV loss | ([[10-Summaries/satas-2020-scarlet\|SCARLET]]) |
| [[10-Summaries/wang-2021-medalt\|MEDALT]] | 2021 | CNA | Minimal event distance | Lineage speciation statistic validated against survival in 20 TNBC patients ([[10-Summaries/wang-2021-medalt\|MEDALT]]) |
| [[10-Summaries/kaufmann-2022-medicc2\|MEDICC2]] | 2022 | Haplotype-specific CNA | WGD-aware minimum event distance | ([[10-Summaries/kaufmann-2022-medicc2\|MEDICC2]]) |
| [[10-Summaries/foroughmand-2022-scelestial\|Scelestial]] | 2022 | SNV | Steiner-tree approximation | Performance guarantees ([[10-Summaries/foroughmand-2022-scelestial\|Scelestial]]) |
| [[10-Summaries/kozlov-2022-cellphy\|CellPhy]] | 2022 | SNV genotype likelihoods | Finite-site ML (RAxML-NG) | ([[10-Summaries/kozlov-2022-cellphy\|CellPhy]]) |
| [[10-Summaries/kang-2022-sieve\|SIEVE]] | 2022 | SNV read counts | Finite-sites, joint SNV calling | Double mutants rare in CRC, frequent in TNBC ([[10-Summaries/kang-2022-sieve\|SIEVE]]) |
| [[10-Summaries/sollier-2023-compass\|COMPASS]] | 2023 | SNV + CNA/CNLOH, amplicon | Joint phylogeny | Convergent evolution in AML/MPN ([[10-Summaries/sollier-2023-compass\|COMPASS]]) |
| [[10-Summaries/kuipers-2025-scicone\|SCICoNE]] | 2025 | Shallow scWGS read counts | Joint CN calling + CNA event tree (MCMC) | WGD as the first event in TNBC ([[10-Summaries/kuipers-2025-scicone\|SCICoNE]]) |
| [[10-Summaries/zhang-2025-scistree2\|ScisTree2]] | 2025 | SNV | Infinite sites; SPR + branch-and-bound | Tens of thousands of cells; tested on HGSOC DLP+ ([[10-Summaries/zhang-2025-scistree2\|ScisTree2]]) |

## Copy-number callers that feed the trees

| Tool | Year | What it adds |
|---|---|---|
| [[10-Summaries/bakker-2016-aneufinder\|AneuFinder]] | 2016 | Separates chromosomal instability (a rate) from aneuploidy (a state): pooled cells reproduce a clonal karyotype while 56% of single cells are unique ([[10-Summaries/bakker-2016-aneufinder\|AneuFinder]]) |
| [[10-Summaries/schneider-2024-scabsolute\|scAbsolute]] | 2024 | Per-cell ploidy and S-phase status from shallow scDNA-seq; read density detects recent WGD and offers an alternative to FACS ploidy sorting ([[10-Summaries/schneider-2024-scabsolute\|scAbsolute]]) |
| [[10-Summaries/zhao-2025-hiscanner\|HiScanner]] | 2025 | High-resolution, allele-specific CNAs from high-coverage scWGS ([[10-Summaries/zhao-2025-hiscanner\|HiScanner]]) |
| [[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]] | 2025 | Absolute, allele-specific CN from ultra-low-coverage tagmentation scWGS with no matched normal, then a MEDICC2 tree ([[10-Summaries/kolbeinsdottir-2025-ascent\|ASCENT]]) |
| [[10-Summaries/ivanovic-2025-cnrein\|CNRein]] | 2025 | Evolution-aware haplotype-specific CN by deep reinforcement learning; larger shared clones and far more parsimonious trees than SIGNALS/CHISEL; consistent clones across 10x and ACT in one breast tumour ([[10-Summaries/ivanovic-2025-cnrein\|CNRein]]) |
| [[10-Summaries/wesley-2026-songbird\|Songbird]] | 2026 | WGD-aware DLP+ calling from fragment-geometry ploidy and unbalanced Haar segmentation ([[10-Summaries/wesley-2026-songbird\|Songbird]]) |

## Longitudinal, metastatic and clinical tracking

- **Remission dynamics.** Over a 3-year remission, an IDH2/NRAS/ASXL1 triple-mutant AML clone expanded from 7% to 64% ([[10-Summaries/pellegrino-2018-tapestri|Pellegrino 2018]]).
- **Immune escape under therapy.** Longitudinal single-cell CNAs, pseudobulk SVs/SNVs and parallel evolution of CD19 immune-escape alleles in B-ALL under CAR-T selection (preprint) ([[10-Summaries/pancikova-2025-splongget|SPLONGGET]]).
- **Minor subclones missed by bulk.** In a paediatric B-ALL, an 8-cell (3%) subclone and a copy-neutral LOH that bulk WGS missed ([[10-Summaries/kolbeinsdottir-2025-ascent|ASCENT]]).
- **Progression.** In a grade II → grade III meningioma pair (179 PTA cells, 0.5×): a 1p/22q-loss clone, a descendant clone adding 6q/9p/11q losses that already contains one grade II cell, and a tetraploid subclone; CNA clusters agree with SECEDO SNV clusters (ARI 0.83) ([[10-Summaries/zhao-2025-hiscanner|HiScanner]]).
- **Metastatic seeding depends on the tree model.** In colorectal patient CRC2, allowing one ISA-violating mutation (*ATP7B*) to be eliminated changed the number of seeding events from two to one ([[10-Summaries/malikic-2019-phiscs|PhISCS]]). A CellPhy reanalysis of the same patient (86 cells) placed all metastatic cells in one well-supported clade (monoclonal seeding), agreeing with SCARLET over SCITE and SiCloneFit ([[10-Summaries/kozlov-2022-cellphy|CellPhy]]).
- **Extrachromosomal DNA.** Single-cell Hi-C tracks ecDNA gain and loss and boundary changes under erlotinib (GBM39) and after azacitidine + venetoclax (AML) ([[10-Summaries/chang-2025-droplet-hi-c|Droplet Hi-C]]). In an esophageal adenocarcinoma organoid, ecDNA kept constant between-bin ratios across cells while a breakage–fusion–bridge did not ([[10-Summaries/wesley-2026-songbird|Songbird]]).

## Beyond SNV trees

- **Mitochondrial variants** as a complementary clonal marker ([[10-Summaries/kwok-2022-mquad|MQuad]]).
- **Bulk methylation clocks.** EVOFLUx infers growth rate, malignancy age and epimutation rate from bulk methylation arrays across 1,976 lymphoid cancers, trading per-cell resolution for clinical cohort scale; the seed of a Richter-transformed CLL clone existed decades before presentation ([[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]]).
- **Genotype to epigenotype.** Mapping chromatin accessibility across breast-cancer CNA subclones separates hardwired from plastic programs ([[10-Summaries/wang-2024-wellda-seq|wellDA-seq]]).
- **Sequence models.** DNA language-model features classified somatic cancer point mutations as driver or passenger with AUROC 84.64% on a 71-mutation xenograft set ([[10-Summaries/zeng-2025-somatic-driver-lm|Zeng 2025]]).

## Reviews

- [[10-Summaries/lim-2020-cancercell|Lim & Navin 2020]] — single-cell genomics in cancer.
- [[10-Summaries/lu-2024-cnaphylogeny-review|Lu 2024]] — copy-number-based cancer phylogenetics.
- [[10-Summaries/mallory-2020-cna-review|Mallory 2020]] — CNA detection from scDNA-seq.
- [[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]] — open problems in single-cell tumour phylogenetics: scale, CNV and indel integration, population-genetic parameters, metastatic seeding.

## Open questions

- Do the sub-100-cell tree methods of 2016–2019 still hold at droplet scale, or do they need re-benchmarking ([[10-Summaries/ross-2016-onconem|OncoNEM]]; [[10-Summaries/pellegrino-2018-tapestri|Tapestri]])? (synthesis)
- Metastatic seeding counts change with the tree model (two events vs one in CRC2), so seeding claims depend on how ISA violations are handled ([[10-Summaries/malikic-2019-phiscs|PhISCS]]; [[10-Summaries/kozlov-2022-cellphy|CellPhy]]). (synthesis)
- CNRein reports that CHISEL calls a unique copy-number profile for almost every cell ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]), so clone labels from per-cell callers may overstate heterogeneity when used as ground truth. (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/scdna-cancer-applications|scDNA cancer applications]] — Intratumor heterogeneity, chemoresistance, metastatic lineage and copy-number tools in cancer.
> - `hub` [[40-Topics/hematopoietic-malignancies|Hematopoietic malignancies]] — Cancers and pre-cancerous clonal expansions of blood stem and progenitor cells.
> - `hub` [[40-Topics/single-cell-lineage-tracing|Single-cell lineage tracing]] — Reconstructing the ancestry of individual cells in development, ageing and cancer.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one body.

## All sources on this page

> [!info]- 43 summaries cited here
> - [[10-Summaries/alexandrov-2013-mutational-signatures|Alexandrov 2013]]
> - [[10-Summaries/bakker-2016-aneufinder|Bakker 2016]]
> - [[10-Summaries/chang-2025-droplet-hi-c|Chang 2025]]
> - [[10-Summaries/el-kebir-2018-sphyr|El-Kebir 2018]]
> - [[10-Summaries/foroughmand-2022-scelestial|Foroughmand-Araabi 2022]]
> - [[10-Summaries/frankell-2019-eac-landscape|Frankell 2019]]
> - [[10-Summaries/gabbutt-2025-evoflux|Gabbutt 2025]]
> - [[10-Summaries/gawad-2014-all-clonal-origins|Gawad 2014]]
> - [[10-Summaries/ivanovic-2025-cnrein|Ivanovic & El-Kebir 2025]]
> - [[10-Summaries/jahn-2016-scite|Jahn 2016]]
> - [[10-Summaries/kang-2022-sieve|Kang 2022]]
> - [[10-Summaries/kaufmann-2022-medicc2|Kaufmann 2022]]
> - [[10-Summaries/kim-2018-tnbc-chemoresistance|Kim 2018]]
> - [[10-Summaries/kolbeinsdottir-2025-ascent|Kolbeinsdottir 2025]]
> - [[10-Summaries/kozlov-2022-cellphy|Kozlov 2022]]
> - [[10-Summaries/kuipers-2025-scicone|Kuipers 2025]]
> - [[10-Summaries/kwok-2022-mquad|Kwok 2022]]
> - [[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]
> - [[10-Summaries/lim-2020-cancercell|Lim & Navin 2020]]
> - [[10-Summaries/lu-2024-cnaphylogeny-review|Lu 2024]]
> - [[10-Summaries/malikic-2019-phiscs|Malikic 2019]]
> - [[10-Summaries/mallory-2020-cna-review|Mallory 2020]]
> - [[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]
> - [[10-Summaries/navin-2011-sns-tumor-evolution|Navin 2011]]
> - [[10-Summaries/pancikova-2025-splongget|Pančíková 2025 (bioRxiv preprint)]]
> - [[10-Summaries/pellegrino-2018-tapestri|Pellegrino 2018]]
> - [[10-Summaries/ross-2016-onconem|Ross & Markowetz 2016]]
> - [[10-Summaries/satas-2020-scarlet|Satas 2020]]
> - [[10-Summaries/schneider-2024-scabsolute|Schneider 2024]]
> - [[10-Summaries/sidhom-2026-tessera|Sidhom 2026 (bioRxiv)]]
> - [[10-Summaries/singer-2018-sciphi|Singer 2018]]
> - [[10-Summaries/sollier-2023-compass|Sollier 2023]]
> - [[10-Summaries/wang-2014-nuc-seq|Wang 2014]]
> - [[10-Summaries/wang-2021-medalt|Wang 2021]]
> - [[10-Summaries/wang-2024-wellda-seq|Wang 2024]]
> - [[10-Summaries/wesley-2026-songbird|Wesley 2026]]
> - [[10-Summaries/xu-2012-single-cell-exome-kidney|Xu 2012]]
> - [[10-Summaries/zafar-2017-sifit|Zafar 2017]]
> - [[10-Summaries/zafar-2019-siclonefit|Zafar 2019]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
> - [[10-Summaries/zeng-2025-somatic-driver-lm|GenomeBert]]
> - [[10-Summaries/zhang-2025-scistree2|Zhang 2025]]
> - [[10-Summaries/zhao-2025-hiscanner|Zhao 2025]]
