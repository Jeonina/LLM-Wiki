---
type: summary
title: "Wang et al. 2024 — Single cell genome and epigenome co-profiling reveals hardwiring and plasticity in breast cancer"
source: "[[00-Sources/papers/Single cell genome and epigenome co-profiling reveals hardwiring and plasticity in breast cancer]]"
source_kind: paper
author: "Kaile Wang, Yun Yan, Heba Elgamal, Jianzhuo Li, Chenling Tang, Shanshan Bai, Zhenna Xiao, Emi Sei, Yiyun Lin, Junke Wang, Jessica Montalvan, Changandeep Nagi, Alastair M. Thompson, Nicholas Navin"
published: 2024-09-10
ingested: 2026-10-07
doi: "10.1101/2024.09.06.611519"
journal: "bioRxiv (preprint, not peer reviewed)"
tags: [wellDA-seq, scDNA-seq, scATAC-seq, genome-epigenome-co-profiling, copy-number-aberration, breast-cancer, ER-positive, cell-of-origin, abstract-only]
entities: ["[[nicholas-navin]]"]
concepts: ["[[joint-single-cell-multi-omics]]", "[[copy-number-variation]]", "[[chromatin-accessibility]]", "[[scatac-seq]]", "[[intratumor-heterogeneity]]"]
topics: ["[[scdna-cancer-applications]]", "[[cancer-clonal-evolution]]", "[[single-cell-multiomics]]"]
---

**Citation:** Wang et al. (2024) — *Single cell genome and epigenome co-profiling reveals hardwiring and plasticity in breast cancer* — *bioRxiv* 2024.09.06.611519 (preprint). [DOI](https://doi.org/10.1101/2024.09.06.611519)

# Wang 2024 — wellDA-seq

> **Source limitation:** the clipping contains only the bioRxiv abstract and landing-page metadata. There are no methods, figures or results text, so this summary is restricted to what the abstract states.
>
> wellDA-seq measures **whole-genome DNA (copy number) and chromatin accessibility in the same single cell**, at high genomic resolution and in thousands of cells. That lets epigenomic phenotypes be read directly onto genetically defined cancer subclones. Applied to breast tissue, it finds evidence for both genetic "hardwiring" (epigenome following genotype) and epigenetic "plasticity" (epigenome varying within a genotype). It also pinpoints the ancestral cancer cells and the epithelial cell-of-origin of ER+ tumours.

## Key claims

- The authors describe wellDA-seq as "the first high-genomic resolution, high-throughput method that can simultaneously measure the whole genome and chromatin accessibility profiles of thousands of single cells" (their priority claim, not independently verified here).
- **Scale:** 22,123 single cells from 2 normal breast tissues and 9 breast tumours.
- **Hardwiring and plasticity:** mapping epigenomic phenotypes onto genetic lineages across subclones gave evidence of both.
- **Ancestral cells and cell-of-origin:** in 6 ER-positive breast cancers, the authors directly identified ancestral cancer cells. Their epithelial cell-of-origin was **Luminal Hormone Responsive** cells.
- **CNAs outside the tumour compartment:** cell types carrying copy-number aberrations were found in *normal* breast tissue. In breast cancers, *non-epithelial* microenvironment cell types carried CNAs.
- A US patent application (PCT/US2024/018634) covering wellDA-seq has been filed.

## Methods / evidence

The clipping gives no details: assay chemistry, genomic resolution, CNA-calling approach and validation are not described in what was captured. All claims are abstract-level.

Weight: low until the full text is ingested. It is a preprint, and only the abstract is available. The "first" claim and the CNA-positive non-epithelial cells are the statements most in need of methodological scrutiny. Doublets between tumour and stromal cells are an obvious alternative explanation that the abstract does not address. (synthesis)

## Surprising or load-bearing bits

- **CNA-carrying non-epithelial cells in tumours**, and CNA-carrying cell types in normal breast. If these hold up, either clonal aberrations extend beyond the epithelial lineage or there is a technical-artefact problem that genome–epigenome co-profiling is well placed to adjudicate, since cell identity comes from the same cell's ATAC profile rather than from inference. (synthesis)
- **Cell-of-origin by direct observation.** Calling an ancestral clone by genotype and then reading its cell type from chromatin accessibility in the same cell replaces the indirect expression-similarity arguments typically used for cell-of-origin. (synthesis)

## Concepts touched

- [[joint-single-cell-multi-omics]] — a DNA plus ATAC co-assay at thousands-of-cells scale.
- [[copy-number-variation]] — CNAs define the genetic lineages onto which chromatin states are mapped.
- [[chromatin-accessibility]] / [[scatac-seq]] — the epigenomic readout used for cell type and phenotype.
- [[intratumor-heterogeneity]] — the subclone-level genotype-to-phenotype mapping (hardwiring vs. plasticity).

## Connections to other sources

- The same lab's lineage of breast-cancer scDNA work: [[navin-2011-sns-tumor-evolution]], [[wang-2014-nuc-seq]], [[kim-2018-tnbc-chemoresistance]]. wellDA-seq adds an epigenomic layer to the CNA-lineage approach of those papers.
- Earlier genome-plus-other-layer single-cell co-assays: [[hou-2016-sctrio-seq]] (genome, methylome and transcriptome), [[macaulay-2015-gt-seq]] (genome plus transcriptome).
- Inferring CNAs from expression rather than measuring DNA: [[gao-2021-copykat]], [[tickle-2019-infercnv]]. A direct DNA measurement is the benchmark these inference methods lack.

## Open questions

- Full-text details: genomic resolution (bin size), per-cell coverage, the doublet/collision rate, and how CNA and ATAC signals are separated from the same nucleus.
- How "hardwiring" versus "plasticity" is quantified, and in what fraction of subclones each dominates.
- Whether the CNA-positive non-epithelial and normal-tissue cells are validated orthogonally.
- Note for the wiki: re-ingest when the peer-reviewed version or full text is available.

## Related

- [[nicholas-navin]] · [[joint-single-cell-multi-omics]] · [[40-Topics/scdna-cancer-applications]]
