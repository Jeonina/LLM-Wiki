---
type: summary
title: "Muyas et al. 2024 — De novo detection of somatic mutations in high-throughput single-cell profiling data sets"
source: "[[00-Sources/papers/De novo detection of somatic mutations in high-throughput single-cell profiling data sets]]"
source_quality: full
source_sha256: "61603a80360365f581f99afff972060a999b292b7e192610dfe685e94333f526"
source_kind: paper
author: "Francesc Muyas, Carolin M. Sauer, Jose Espejo Valle-Inclán, Ruoyan Li, Raheleh Rahbari, Thomas J. Mitchell, Sahand Hormoz, Isidro Cortés-Ciriano (last author)"
published: 2023-07-06
ingested: 2026-10-07
doi: "10.1038/s41587-023-01863-z"
journal: "Nature Biotechnology 42(5):758–767"
tags: [SComatic, somatic-SNV, scRNA-seq, scATAC-seq, de-novo-calling, beta-binomial, panel-of-normals, mutational-signatures, mutation-burden, clonal-mosaicism, polyclonal-tissue, cardiomyocytes, MSI]
entities: []
concepts: ["[[single-cell-variant-calling]]", "[[mutational-signatures]]", "[[scrna-seq]]", "[[scatac-seq]]", "[[intratumor-heterogeneity]]", "[[myeloproliferative-neoplasm]]", "[[cell-type-annotation]]"]
topics: ["[[mosaic-variant-calling]]", "[[somatic-mosaicism]]", "[[cancer-clonal-evolution]]", "[[computational-methods]]"]
---

**Citation:** Muyas et al. (2024) — *De novo detection of somatic mutations in high-throughput single-cell profiling data sets* — *Nature Biotechnology* 42(5):758–767. [DOI](https://doi.org/10.1038/s41587-023-01863-z)

# Muyas 2024 — SComatic

> Most attempts to read somatic mutations out of scRNA-seq or scATAC-seq data only *genotype* variants already found by matched DNA sequencing. SComatic calls somatic SNVs **de novo, with no matched DNA**. It pools reads by **cell type** and tests each site against a **beta-binomial background error model** fitted on unrelated non-neoplastic samples. The key biological filter: a germline variant should appear in **all** cell types, while a somatic one should be confined to one lineage. Variants seen in multiple cell types are therefore discarded, along with RNA-editing sites, common gnomAD SNPs and a **panel-of-normals** of recurrent artefacts. Across >2.6 million cells from 688 datasets, precision is far higher than for bulk or single-cell callers. That makes mutational signatures and burdens resolvable per cell type, including in polyclonal normal tissue.

## Key claims

- **Calling rules.** Depth ≥5 reads in the cell type; the mutation must be supported by ≥3 reads from ≥2 cells of that type. The beta-binomial test is significant (threshold 0.001) in the candidate type and **not** significant in each other type, or in all others aggregated. Sites within 4 bp of homopolymers are removed, as are mutations <5 bp apart (except known DBS signatures such as UV CC>TT). The PON also drops sites seen in ≥2 unrelated samples. In 10x scRNA-seq, recurrent errors are enriched in LINE/SINE (e.g., Alu) elements.
- **Validation in cSCC (8 tumours + adjacent skin; scRNA-seq vs WES).** On 9,788,377 positions with coverage in both, 266 of 10,477 WES mutations were present. SComatic called 179 mutations: 80 (45%) also in WES, 42 (23%) with sub-threshold WES read support, 55 (31%) scRNA-only. 38 of those 55 came from sample P7, which shows high genetic heterogeneity. 82% of scRNA-only and 82% of WES-only mutations carried UV signatures (SBS7a/b/d), implying both sets are largely real. Per-sample mutation rates correlated with WES at R² = 0.97.
- **Benchmark (30 tumours — 7 cSCC, 9 kidney, 14 ovarian; 416 DNA-confirmed mutations) against Strelka2, VarScan2, SAMtools, Monovar and SCReadCounts.** **Precision 0.67–0.87 for SComatic against 0.06–0.24 for the next best (Strelka2)**, with the highest F1. Sensitivity was 0.33–0.56: above Monovar and above SAMtools in two datasets, but **below Strelka2, VarScan2 and SCReadCounts**. The other tools' calls looked like SBS1/SBS5 rather than the WES spectrum; SComatic's cSCC spectrum matched WES (cosine 0.98). The advantage persists after removing common SNPs from all call sets, so it is attributed to background-error modelling.
- **Hypermutated colorectal cancer (70 tumours incl. 37 MSI; 40 normals).** 8,997 SNVs. Epithelial burden: MSI 24.7 vs MSS 8.3 SNVs/Mb vs normal 0.51. Non-epithelial cells were similar between MSI and MSS (0.41 vs 0.52). MMR signatures appeared in MSI, and one POLE-type sample (C172) had 82.9% SBS10a/b/SBS28. Other callers' burdens did not separate MSI from MSS.
- **Low-burden and normal tissues.** MPN CD34⁺ cells: 0.12 mutations/Mb per haploid genome, 96% SBS5/40, burden vs age r = 0.79 (P = 0.09, n = 5). Heart cell atlas (78 samples, 14 donors): cardiomyocytes ~302 mutations per haploid genome (range 92–1,284), below adipocytes (1,179) and smooth muscle (581); 35.4% SBS44; comparable to single-cell WGS estimates (P = 0.08). GTEx (24 datasets, 8 tissues, 15 donors): mean 598 per cell per haploid genome.
- **scATAC works too.** sciATAC-seq atlas (459,056 cells, 66 samples, 24 tissues): 389 SNVs, mostly intergenic, promoter or intronic, and 99% SBS5/40. Rates were comparable to the same cell types in scRNA-seq.
- **Clonality and ITH.** Clonal mutations appear in cSCC epithelium but not in normal skin (polyclonal). Non-neoplastic mutations mostly sit at <0.2 mutant-cell fraction. In multi-region ovarian scRNA (SPECTRUM-OV-003), mutation-based clones agreed with Numbat copy-number clones. Subclonal drivers (MLH1, TGFBR2, KRAS) were found in CRC.

## Methods / evidence

Uniform reprocessing (Cell Ranger v6; BWA-MEM + GATK for sciATAC) with published cell-type annotations. Ground truth came from WES/WGS (Strelka2 ∩ MuSE; SAGE/PURPLE). Precision, sensitivity and F1 used 50 bootstrap resamples. Signatures were fitted with MutationalPatterns against COSMIC v3 after trinucleotide renormalisation to callable regions.

Weight: strong, multi-dataset validation with DNA truth sets and signature-level sanity checks. Two caveats: (i) the truth set is only mutations *with* scRNA read support, which favours precision; (ii) burdens for normal tissues are extrapolated from small callable fractions and reported per haploid genome, because usually only one allele is observed per cell and site. (synthesis)

## Surprising or load-bearing bits

- **Cell-type granularity sets what can be detected.** Mutations acquired before two annotated types diverged look germline and are discarded. Fine annotations detect only late mutations; broad ones capture earlier lineage mutations. Annotation is therefore a scientific choice, not just preprocessing.
- **The gain is precision, not sensitivity.** Bulk callers find more true sites but drown them in artefacts (precision ≤0.24). For signature and burden work, precision matters more. (synthesis)
- **DNA-matched genotyping can *underperform* de novo calling in heterogeneous samples.** In P7, DNA and scRNA sampled different subclones. Methods that only genotype DNA-called sites would miss mutations specific to the profiled cells.
- **Cardiomyocyte SBS44 and the adipocyte excess** arise from expression data alone, echoing single-cell WGS findings without any DNA amplification.

## Concepts touched

- [[single-cell-variant-calling]] — de novo SNV calling from non-DNA single-cell assays; error-model-driven precision.
- [[mutational-signatures]] — signature fitting and de novo extraction at cell-type resolution with trinucleotide renormalisation.
- [[scrna-seq]] / [[scatac-seq]] — secondary genetic readouts from routine single-cell data.
- [[cell-type-annotation]] — annotation granularity sets the detectable mutation window.
- [[myeloproliferative-neoplasm]] — low-burden MPN HSPCs with clock-like signatures.

## Connections to other sources

- Benchmarked against [[zafar-2016-monovar]] and [[li-2009-samtools]]; complements genotyping-based approaches and germline-SNV calling from scRNA/scATAC in [[dou-2023-monopogen]]. (synthesis)
- Same-cell genotype + phenotype alternatives that need targeted DNA readout: [[nam-2019-got]], [[izzo-2024-got-cha]]. (synthesis)
- Signatures framework: [[alexandrov-2013-mutational-signatures]]. Duplex/single-molecule approaches that lose cell-type information, which the introduction contrasts: [[abascal-2021-nanoseq]].
- Cardiomyocyte burdens to compare with single-cell WGS data: [[hilal-2026-cardiac-somatic-review]]. HSC clock-like signature context: [[lee-six-2018-hsc-dynamics]]. (synthesis)
- Other genetic signal mined from scRNA/scATAC: mtDNA ([[kwok-2022-mquad]]) and CNAs ([[ramakrishnan-2023-epianeufinder]], [[gao-2021-copykat]]). (synthesis)
- Field review that listed SNV-from-scRNA (SSrGE) as early work: [[lahnemann-2020-grand-challenges]].

## Open questions

- Only a small fraction of the genome is callable (3′ UTRs, introns, open chromatin). Mutations at RNA-editing sites or outside expressed or accessible regions are unreachable.
- Allele-specific expression and the one-read-per-site regime make burdens "per haploid genome"; ploidy differences (cancer, cardiomyocytes) are not corrected.
- Indels are not addressed.
- How does SComatic behave at the low mutant-cell fractions typical of early-development mosaic variants that span many cell types, which its multi-cell-type filter would discard? (synthesis)

## Related

- [[single-cell-variant-calling]] · [[mutational-signatures]] · [[40-Topics/mosaic-variant-calling]] · [[40-Topics/somatic-mosaicism]]
