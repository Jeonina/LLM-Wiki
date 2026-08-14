---
type: summary
title: "Xiong, Zhang & Ma 2024 — scGHOST: identifying single-cell 3D genome subcompartments"
source: "[[00-Sources/papers/scGHOST_ identifying single-cell 3D genome subcompartments]]"
source_kind: paper
author: "Kyle Xiong, Ruochi Zhang, Jian Ma (corresponding)"
published: 2024-04-08
ingested: 2026-08-13
doi: "10.1038/s41592-024-02230-9"
journal: "Nature Methods 21:814–822"
tags: [scGHOST, subcompartments, graph-embedding, constrained-random-walk, node2vec, allele-specific, MERFISH, HiRES, Dip-C]
entities: ["[[jian-ma]]"]
concepts: ["[[single-cell-hi-c]]", "[[chromatin-compartments]]", "[[dimensionality-reduction]]", "[[imputation]]", "[[dip-c]]", "[[replication-timing]]", "[[allele-specific-methylation]]", "[[pseudo-bulk]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]", "[[single-cell-multiomics]]"]
---

**Citation:** Xiong, Zhang & Ma (2024) — *scGHOST: identifying single-cell 3D genome subcompartments* — *Nature Methods* 21, 814–822. [DOI](https://doi.org/10.1038/s41592-024-02230-9)

# Xiong 2024 — scGHOST

> Single-cell A/B compartments, TADs, and loops all had callers by 2023. **Subcompartments did not**, and for a specific reason: bulk subcompartment annotation needs ≥50 million *trans* reads, and essentially no scHi-C dataset has enough interchromosomal coverage — not even at pseudobulk level. scGHOST gets around this by **embedding genomic loci as graph nodes** (node2vec-style constrained random walks over [[zhang-2022-higashi|Higashi]]-imputed maps, borrowing from k-nearest-neighbour cells) and clustering the embeddings, producing five per-cell subcompartments scA1/scA2/scB1/scB2/scB3.

## Key claims

- **Binary A/B is insufficient and subcompartments were the missing single-cell feature.** Rao's five bulk subcompartments (A1, A2, B1, B2, B3) stratify epigenomic signal in ways A/B cannot; no method existed to call them per cell.
- **Four components.** (1) A node2vec-inspired second-order random-walk sampler that draws on both the cell's own imputed map and its neighbours in embedding space, yielding a sparse weighted graph of only the strongest contacts; (2) word-embedding-style neural node embedding aggregating walks across cells; (3) a clustering step constrained so that clusters on different chromosomes correspond to the same genome-wide subcompartments; (4) an alignment step making annotations comparable across cells.
- **Single-cell subcompartments have coherent contact behaviour.** In GM12878 at 500 kb, same-label locus pairs interact preferentially — intra-cluster O/E significantly above inter-cluster (one-sided P < 5.53 × 10⁻¹³⁴).
- **Aggregated single-cell annotations beat bulk annotations at segmenting the genome.** Pseudobulk scGHOST tracks contact-pattern shifts that bulk Hi-C labels miss (regions held at B3 by bulk but placed in refined active subcompartments by scGHOST), and avoids an unsupported bulk A2→B3 transition. Genome-wide, pseudobulk subcompartments correspond to reduced variance in scHi-C contact frequency.
- **scA/B compartment scores distinguish all five single-cell subcompartments, whereas bulk A2 and B1 are not separated** (mean P = 0.086) — the single-cell annotation is finer than the bulk one it was matched to.
- **Facultative heterochromatin is where the variability lives.** GM12878 loci with variable subcompartment assignment show significantly higher H3K27me3 enrichment than stable loci (P = 1.31 × 10⁻⁴), linking structural variability to the mark associated with heterogeneous repression.
- **Subcompartment variability tracks transcriptional variability.** In WTC11 iPSCs: stable-subcompartment regions are mostly scA1/scB3; variable regions distribute evenly across subcompartments. Regions with variable subcompartmentalisation are enriched for genes with variable transcription (P = 2.60 × 10⁻²), and **subcompartment boundaries even more so** (P = 3.79 × 10⁻⁹) — boundaries co-localise with TAD-like domain boundaries by insulation score. Notably, scB2 appears at TSSs of both stable and variable genes in variable regions, suggesting the "inactive" scB2 can be transiently active.
- **It works on imaging data too.** Applied to MERFISH chromatin tracing of chr21 in IMR90 (distance maps inverted into proximity maps), pseudobulk subcompartments show the expected histone-mark and replication-timing stratification, and scA1/scA2 co-occur with more frequently transcribing genes in the *same* imaged cells.
- **Cell-type resolution in tissue exceeds Higashi's own scA/B.** In human PFC, scGHOST embeddings separate inhibitory from excitatory neurons that Higashi scA/B scores leave mixed; classification accuracy matches full Higashi embeddings but with the advantage that features map to specific loci. Cell-type marker genes sit in significantly more active subcompartments than the same loci in other cell types (P < 1.44 × 10⁻¹⁰) and associate with subcompartment boundaries (P = 1.30 × 10⁻¹²).
- **Allele-specific subcompartments exist and relate to imprinting.** On [[tan-2018-science|Dip-C]] developing-mouse-brain data split into pseudo-haploids, haploids cluster by both cell type and parental genotype; inter-allele similarity *decreases* across developmental stages; two alleles from the same cell are more similar than random same-cell-type haploids; and regions around imprinted genes are enriched for allele-specific subcompartments (hypergeometric P < 1.18 × 10⁻⁴).
- **Subcompartment switching often *precedes* expression change.** On HiRES (joint RNA + Hi-C) mouse embryos, 81.5% of genes show higher scA1 frequency at the TSS in cells actively transcribing them. Clustering marker-gene trajectories across E8.5–E9.5 gives five patterns: **~50% of genes switch subcompartment before upregulation, only 14% change synchronously** (example: *Akt3*).

## Methods / evidence

Five datasets spanning three data types: GM12878 scHi-C (500 kb), WTC11 iPSC scHi-C with matched scRNA-seq residual-variance, IMR90 MERFISH imaging with co-assayed nascent transcription (chr21, 100 kb), human PFC scHi-C with methylation-derived labels, Dip-C developing mouse brain (haplotype-resolved), and HiRES mouse embryos (RNA + Hi-C co-assay). Validation against bulk subcompartments (Rao, SNIPER), histone marks, replication timing, imprinted-gene annotation, and co-assayed transcription.

Weight: the imaging and HiRES applications are the strongest evidence, because both provide *same-cell* transcription measurements — the subcompartment/transcription link is not inferred across assays. The dependence on Higashi imputation is a real coupling: scGHOST inherits whatever Higashi gets wrong.

## Surprising or load-bearing bits

- **The *trans*-read barrier is the reason this was hard, and it is a coverage-arithmetic argument, not an algorithmic one.** Bulk subcompartments are defined by interchromosomal patterns; scHi-C has essentially none. scGHOST substitutes graph-embedding structure for missing *trans* data — worth noting that it therefore does not measure subcompartments the way bulk does, it *reconstructs an analogous partition*.
- **"Structure changes first, expression follows" in 50% of genes** is the paper's most consequential biological claim and the one that most needs replication. It is only visible with same-cell RNA + contacts.
- **Variability, not mean state, carries the signal** — twice over: H3K27me3 marks variable loci, and variable loci host variable genes. Single-cell methods that report cluster averages discard exactly this.
- **Boundaries beat regions** for association with transcriptional variability (P = 3.79 × 10⁻⁹ vs 2.60 × 10⁻²). Subcompartment *transitions* may be the functional unit.
- **Allele similarity decreasing over development** implies the two parental genomes progressively individualise their folding — a finding only reachable with haplotype-resolved single-cell data.
- **Applying a Hi-C method to MERFISH proximity maps** by inverting Euclidean distances is a small methodological bridge with large implications: it means imaging and sequencing 3D data can share an analysis stack.
- The authors themselves flag the **unresolved discrepancy between single-cell and bulk subcompartments** and list disentangling cell type, cell cycle, intrinsic dynamics, and read-depth bias as future work — an unusually candid limitations section.

## Entities mentioned

- [[jian-ma]] — corresponding author; also Higashi and SNIPER.

## Concepts touched

- [[chromatin-compartments]] — extends the A/B framework to five per-cell subcompartments.
- [[single-cell-hi-c]] — graph representation learning as the sparsity workaround.
- [[dip-c]] — haplotype-resolved input enabling allele-specific analysis.

## Connections to other sources

- Direct dependency: [[zhang-2022-higashi]] supplies the imputation and embeddings; scGHOST is a layer on top, from the same lab.
- Predecessor in the same imputation lineage: [[zhou-2019-schicluster]].
- Sibling caller for a different feature: [[yu-2021-snaphic]] (loops).
- Input data: [[tan-2018-science]] (Dip-C), [[lee-2019-natmethods]] (PFC sn-m3C-seq), [[nagano-2013-nature]], [[ramani-2017-scihi-c]].
- Cell-type labels from methylation: [[luo-2017-snmc-seq]].
- Bulk compartment framework: [[lieberman-aiden-2009-hic]]; differential compartment analysis at [[chakraborty-2022-dchic]].
- Domain/boundary context: [[dixon-2012-tads]].
- 3D-genome single-cell review: [[hong-2025-sc3d-genome-review]]; atlas-scale context [[liu-2023-mouse-brain-methylome-3d]], [[jiang-2026-stark-scnucleome]].

## Open questions

- **Why single-cell and bulk subcompartments disagree is unresolved**, and the authors say so. Until it is, "scB1" and bulk "B1" should not be treated as the same object.
- Cell-to-cell variability confounds cell type, cell state, cell cycle, intrinsic dynamics, and read depth; scGHOST minimises technical bias but does not decompose the variance.
- Embeddings are not directly comparable across chromosomes; the workaround is an approximation of inter-chromosomal maps.
- Computational efficiency limits resolution — 500 kb here, versus 10 kb for loop calling.
- Whether the "structure precedes expression" ordering is causal or reflects a shared upstream driver is untestable in this design.

## Related

- [[zhang-2022-higashi]] · [[yu-2021-snaphic]] · [[chromatin-compartments]] · [[40-Topics/3d-genome]]
