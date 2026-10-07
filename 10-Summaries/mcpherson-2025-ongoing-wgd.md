---
type: summary
title: "McPherson et al. 2025 — Ongoing genome doubling shapes evolvability and immunity in ovarian cancer"
source: "[[00-Sources/papers/Ongoing genome doubling shapes evolvability and immunity in ovarian cancer]]"
source_quality: full
source_sha256: "37f43e353eca54bd83bea195f9642c7297fe0282451c8fe326a9b00717102dae"
source_kind: paper
author: "Andrew McPherson, Ignacio Vázquez-García, Matthew A. Myers, Duaa H. Al-Rawi, Matthew Zatzman, Adam C. Weiner, ... Simon Tavaré, Samuel Aparicio, ..., Britta Weigelt, Samuel F. Bakhoum, Sohrab P. Shah"
published: 2025-07-16
ingested: 2026-10-07
doi: "10.1038/s41586-025-09240-3"
journal: "Nature 644(8078):1078–1087"
tags: [whole-genome-doubling, WGD, HGSOC, ovarian-cancer, DLP+, scWGS, chromosomal-instability, micronuclei, cGAS-STING, doubleTime, SIGNALS, MEDICC2, SBMClone, allele-specific-copy-number, MSK-SPECTRUM, tumour-microenvironment]
entities: []
concepts: ["[[dlp-plus]]", "[[chromosomal-instability]]", "[[copy-number-variation]]", "[[intratumor-heterogeneity]]", "[[phylogenetic-inference]]", "[[mutational-signatures]]", "[[pseudo-bulk]]", "[[structural-variants]]", "[[scrna-seq]]"]
topics: ["[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]", "[[scdna-seq]]"]
---

**Citation:** McPherson et al. (2025) — *Ongoing genome doubling shapes evolvability and immunity in ovarian cancer* — *Nature* 644(8078):1078–1087. [DOI](https://doi.org/10.1038/s41586-025-09240-3)

# McPherson 2025 — ongoing WGD in HGSOC

> Bulk sequencing treats whole-genome doubling (WGD) as a once-per-tumour yes/no event. With DLP+ single-cell WGS of **30,260 high-quality tumour genomes from 70 samples of 41 treatment-naive high-grade serous ovarian cancer (HGSOC) patients**, this study shows WGD is an **ongoing mutational process**: 40 of 41 patients carry coexisting 0×, 1× and/or 2×WGD cells. WGD raises cell-to-cell copy-number diversity, missegregation rates and cGAS⁺ ruptured micronuclei; a new SNV-based timing method, **doubleTime**, distinguishes truncal, parallel, subclonal and unexpanded WGD histories. Paradoxically, despite more chromosomal instability (CIN), predominantly-WGD tumours show **repressed STING1, reduced interferon/inflammatory signalling and an immunosuppressive, pro-angiogenic microenvironment**, whereas the CIN → innate-immune link is preserved in predominantly diploid tumours.

## Key claims

- **Cohort and data.** 100,054 single-cell genomes sequenced (median 1,720 per patient; median depth 0.060, breadth 0.057 per cell) → 30,260 tumour genomes after QC. Signatures: 18 HRD-Dup, 8 HRD-Del, 14 FBI, 1 tandem duplicator. Matched scRNA-seq (previously published; 123 sites, 32 patients), multiplexed immunofluorescence (102 slides, 37 patients), MSK-IMPACT and bulk WGS (33 patients).
- **Per-cell WGD calls** from allele-specific copy number (SIGNALS): FM2 > 0.5 → ≥1×WGD; FM3 > 0.5 → ≥2×WGD; validated by correlation with mtDNA copy number, overlapping-read fraction and optically measured cell size.
- **WGD is ubiquitous and ongoing.** 4% of all tumour cells (1,213) are non-majority WGD multiplicities (median 2.5% per patient); mixed multiplicities across sites in 16/21 multi-site patients; additional-WGD cells in 37/41 patients. 27/41 tumours are WGD-high (66%), enriched for FBI and HRD-Del and in older patients.
- **Four evolutionary modes (doubleTime, 39 patients):** truncal WGD in 21; parallel WGD in two (OV-025, OV-045), with distinct WGD clones spread across anatomical sites; subclonal WGD in five; unexpanded WGD in 11 (small 1×WGD populations in all but one). In 8/25 WGD-high tumours WGD occurred >50% along the ancestral branch or after the MRCA; three late-WGD tumours retain residual 0×WGD cells (OV-045 0.8%, OV-075 3.3%, OV-081 35%). Absence of residual 0×WGD in early-WGD tumours is read as clonal sweeps.
- **WGD drives diversification.** Nearest-neighbour copy-number distance rises with WGD multiplicity; in eight patients cells differ from their closest neighbour by >10% of the genome. "Divergent" cells (NND >99th percentile of a beta fit) occur in 38/41 patients (mean 2.6%), more in WGD-high and late-WGD tumours, with higher nullisomy — likened to the "hopeful monsters" of colorectal organoids.
- **Higher missegregation rates after WGD** (MEDICC2 cell phylogenies): ploidy-adjusted chromosome and arm losses 2.6- and 2.4-fold higher, gains 2.3-fold higher, in WGD-high 1×WGD vs WGD-low 0×WGD cells; robust in GEE models with age, signature and site.
- **Orthogonal imaging:** 20,988,413 nuclei and 896,042 cGAS⁺ ruptured micronuclei segmented; micronuclei rate 3.3-fold higher in WGD-high tumours (P = 1.8 × 10⁻⁶); nuclear area larger.
- **Pseudo-triploidy from doubling plus losses.** Ancestral losses are an order of magnitude more frequent than gains; HGSOC pseudo-triploid karyotypes are inferred to arise via WGD with pre- and post-WGD losses, not incremental gains. Truncal WGD clones carry ~3× more chromosome/arm losses than subclonal ones, and losses scale with WGD age — favouring **gradual** post-WGD loss over punctuated catastrophe for expanding clones.
- **Immune phenotype splits by WGD status.** WGD-high tumours: fewer S-phase cells, altered MCM/CDC6 timing, lower type I/II interferon, inflammatory and TNF–NF-κB signalling, lower *STING1* RNA and protein; enrichment of endothelial cells, pericytes and CAFs. WGD-low: chromosome-loss rates correlate with immune programs and *STING1* (ρ = 0.75, P = 0.003), with CXCL10⁺CD274⁺ macrophages and IFN-producing dendritic cells enriched.
- **Cell-intrinsic in vitro.** *TP53*-mutant RPE-1 and FNE1 lines spontaneously produced WGD clones; CIN drugs (nocodazole, reversine) raised G1 fraction and *STING1* in non-WGD cells, while WGD cells had lower *STING1* than non-WGD cells — STING1 repression can occur without a tumour microenvironment.

## Methods / evidence

DLP+ (nanowell tagmentation, no pre-amplification) → bwa-mem, 500-kb bins, HMMcopy with six ploidy settings, random-forest cell QC (score ≥0.75), removal of normal cells, S-phase cells (2-of-3 of: Repli-seq correlation, breakpoint count, breakpoint prevalence), doublets (chr17 LOH, SNV features, two-rater review of nozzle images) and suspect high-ploidy cells (required a ≥10-Mb segment at CN 1, 3 or 5 — so perfectly doubled or G2 cells read as half ploidy). Haplotype-specific CN via SHAPEIT + SIGNALS. SNVs: pseudobulk Mutect2 per patient, ArtiCull artefact filter, SBMClone clones; SVs: consensus deStruct + Lumpy. doubleTime: perfect-phylogeny clone tree, cnLOH-SNV likelihood-ratio test for parallel vs shared WGD, Pyro beta-binomial assignment of C>T CpG SNVs before/after WGD for timing. Cell trees by MEDICC2 (`--wgd-x2`) with Sankoff parsimony ancestral reconstruction (manual WGD placement corrections for 10 patients). scRNA WGD labels propagated from scWGS; GEE and dreamlet for phenotype tests; miloR for abundance.

Weight: a large, carefully QC'd multimodal dataset with orthogonal validation (imaging, bulk, cell lines). Limitations acknowledged: DLP+ sequences live cells (may miss non-viable aneuploid cells), ploidy filtering undercounts perfect doublings, transcriptomic links are associative and patient-matched rather than same-cell, and some WGD placements required manual curation.

## Surprising or load-bearing bits

- **"Is this tumour WGD?" is the wrong question** — almost every tumour is a distribution over WGD multiplicities; fixation, not occurrence, is rate-limiting. WGD-low tumours keep generating WGD cells that simply fail to expand.
- **Parallel WGD events arose at roughly the same evolutionary time**, which the authors read as a cell-extrinsic, WGD-permissive state.
- **More CIN, less inflammation**: the CIN → micronuclei → cGAS-STING → interferon axis is decoupled in WGD-high tumours; *STING1* repression may be a prerequisite for WGD clonal expansion and may even precede WGD.
- **Single-cell CNA rates are closer to true rates** than bulk because cell-specific events (and non-expanding divergent cells) are visible — a key argument for scDNA in CIN research. (synthesis on generalisation)

## Concepts touched

- [[chromosomal-instability]] — measured three ways (cell-specific CNAs on phylogenies, divergent cells, ruptured micronuclei).
- [[dlp-plus]] — at 100,054-cell scale with optical doublet review and cell-size readout.
- [[copy-number-variation]] / [[phylogenetic-inference]] — allele-specific CN, WGD-aware MEDICC2 trees, SNV-based WGD timing.
- [[intratumor-heterogeneity]] — WGD multiplicity as a new axis of heterogeneity.
- [[pseudo-bulk]] — SNV and SV calling at ~0.06× per cell requires pooling.
- [[mutational-signatures]] — HRD-Dup / HRD-Del / FBI stratification via MMCTM.

## Connections to other sources

- Platform: [[laks-2019-dlp-plus]] (DLP+, also HGSOC) and [[zahn-2017-dlp]].
- WGD-aware CN phylogenetics: [[kaufmann-2022-medicc2]]; review context [[lu-2024-cnaphylogeny-review]].
- Allele-specific single-cell CN precedent: [[zaccaria-2021-chisel]]; scRNA CNV inference used here: [[tickle-2019-infercnv]].
- SNV-tree alternative tested on HGSOC DLP+ data: [[zhang-2025-scistree2]].
- Earlier scDNA tumour-evolution work: [[navin-2011-sns-tumor-evolution]], [[wang-2014-nuc-seq]], [[kim-2018-tnbc-chemoresistance]]; karyotype heterogeneity [[bakker-2016-aneufinder]].
- Reviews: [[lim-2020-cancercell]].

## Open questions

- Does STING1 repression precede WGD, and would STIC precursor lesions show it? Proposed, not tested.
- How do ongoing-WGD dynamics affect PARP-inhibitor or bevacizumab response? Raised as a stratification hypothesis only.
- Generality beyond *TP53*-mutant HGSOC is unknown; the authors point to xenograft and mouse evidence only.
- Perfectly doubled cells are filtered or halved by design — the true 2×WGD frequency may be underestimated. (synthesis)

## Related

- [[laks-2019-dlp-plus]] · [[kaufmann-2022-medicc2]] · [[chromosomal-instability]] · [[40-Topics/cancer-clonal-evolution]]
