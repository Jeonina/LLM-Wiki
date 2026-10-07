---
type: summary
title: "Li et al. 2023 — A mouse model with high clonal barcode diversity for joint lineage, transcriptomic, and epigenomic profiling in single cells"
source: "[[00-Sources/papers/A mouse model with high clonal barcode diversity for joint lineage, transcriptomic, and epigenomic profiling in single cells]]"
source_quality: full
source_sha256: "65a7b7a449b5769ba77d41104c9e4e771c8ab57167f6752f27763554659c4318"
source_kind: paper
author: "Li Li, Sarah Bowling, Sean E. McGeary, Qi Yu, Bianca Lemke, Karel Alcedo, Yuemeng Jia, Xugeng Liu, Mark Ferreira, Allon M. Klein, Shou-Wen Wang, Fernando D. Camargo (corresponding)"
published: 2023-11
ingested: 2026-10-07
doi: "10.1016/j.cell.2023.09.019"
journal: "Cell 186(23):5183-5199.e22"
tags: [DARLIN, Camellia-seq, CARLIN, Cas9-TdT, CRISPR-lineage-recording, lineage-tracing, scNMT-seq, NOMe-seq, clonal-memory, DNA-methylation, hematopoiesis, HSC-migration, CoSpar, barcode-homoplasy]
entities: ["[[alejo-rodriguez-fraticelli]]", "[[fuchou-tang]]"]
concepts: ["[[crispr-lineage-recording]]", "[[lineage-tracing]]", "[[scnmt-seq]]", "[[nome-seq]]", "[[epigenetic-memory]]", "[[methylation-clones-epimutation]]", "[[hematopoietic-differentiation]]", "[[joint-single-cell-multi-omics]]", "[[scbs-seq]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[single-cell-multiomics]]", "[[dna-methylation]]"]
---

**Citation:** Li et al. (2023) — *A mouse model with high clonal barcode diversity for joint lineage, transcriptomic, and epigenomic profiling in single cells* — *Cell* 186:5183–5199.e22. [DOI](https://doi.org/10.1016/j.cell.2023.09.019)

# Li 2023 — DARLIN + Camellia-seq

> An engineered-barcode lineage mouse is only as useful as the fraction of profiled cells that carry a barcode which is **detected, edited and rare**. Cas9/CARLIN managed ~10%; DARLIN reaches ~60% by fusing Cas9 to **terminal deoxynucleotidyl transferase (TdT)** — trading CRISPR's large deletions for random insertions — and by adding two more independent target arrays (*Tigre*, *Rosa26*). With that coverage the paper does three things: resolves early megakaryocyte bias in fetal-labelled HSCs, measures low-level native HSC migration between bones, and — via a new joint assay, **Camellia-seq** (lineage + RNA + CpG methylation + GpC accessibility per cell) — shows that **DNA methylation, not expression or accessibility, carries clonal memory** in self-renewing HSCs.

## Key claims

- **Cas9 editing is deletion-dominated, which wastes barcode space.** In the published Cas9/CARLIN data there were on average 1.5 insertion and 2.5 deletion events per allele; an edited allele had a median of 163 bp deleted out of the 270-bp array (≈6 of 10 target sites) versus a median 2 bp inserted. Common alleles were enriched for deletion-only alleles, rare alleles for insertions.
- **TdT fusion shifts the balance.** In adult CARLIN livers (hydrodynamic plasmid injection, bulk RNA-seq after 1 week), Cas9-TdT gave fewer deletions and twice the insertion events per allele compared with Cas9. In the germline DARLIN-v0 line versus Cas9/CARLIN (granulocytes; n = 7 vs 5 mice): ~65% vs ~30% singleton alleles (replicates with >10,000 alleles), 2.3-fold as many alleles per edited UMI, ~5× the Shannon allele diversity, and fewer than one deletion per insertion versus three.
- **Capacity.** DARLIN-v0 editing efficiency was >90% across intestine, kidney, lung, liver, spleen and gonad (vs 30–50% reported for Cas9/CARLIN), with ~4% background editing without Dox. Pooled data gave 5.2 × 10⁵ unique alleles with distinct-allele counts rising linearly with edited cells (r² = 0.97, no saturation); Chao1 estimated 1.3 × 10⁶ possible alleles, at least 30× the 44,000 reported for Cas9/CARLIN.
- **Three independent arrays.** DARLIN-v1 adds *Tigre* (TA) and *Rosa26* (RA) arrays reusing the same 10 target sequences in different orders; the three edit independently with similar efficiency and diversity, giving a theoretical ~10¹⁸ barcodes (assuming ≥10⁶ alleles per locus) against ~10¹⁰ cells in an adult mouse. At FDR 0.01 the allele bank could label ~10⁴ reliable clones with one array and ~10¹² with all three; ~80% of alleles in actual experiments were *de novo* (absent from the bank).
- **Single-cell lineage coverage ~60% vs ~10%.** Detected at least one locus in ~80% vs ~50% of cells; ~80% vs ~35% of detected barcodes edited; ~93% vs 55% of edited cells carried a rare allele (DARLIN vs Cas9/CARLIN). In a skull bone-marrow Lin⁻cKit⁺ dataset labelled at E17.0: 6,094 cells after QC, 81% with ≥1 locus detected, 3,839 (63%) with ≥1 rare allele, 1,034 clones.
- **Early MkP bias in HSCs.** Clonal coupling linked MkPs with HSCs (p < 0.001) and monocytes with LMPPs (p < 0.05); 48% of 187 multi-cell clones containing an HSPC had a single clonal fate, and only MkP-biased clones had distinct transcriptomic signatures. CoSpar predicted MkPs arise from a subset of HSCs; **this inference failed when DARLIN data were down-sampled to Cas9/CARLIN coverage**. Early MkP-biased HSCs expressed long-term HSC genes (*Mecom*, *Mllt3*, *Hlf*), cell-cycle inhibitors and megakaryopoiesis regulators, plus TFs without an established link (*Klf12*, *Sox5*, *Rora*, *Pbx3*, *Pbx1*, *Gata2*).
- **HSC migration between bones is real but low.** Labelling at 2 months and reading out 4 months later: ~5% of HSC-containing clones shared with HSCs in another bone, rising to ~14% for MPPs and ~40% for MyPs; ~12% for HSCs after a 1-year chase; ~11% when labelled as neonates. E17.0 labelling still gave predominantly local haematopoiesis, while E10.0 labelling gave ~80% shared clone fraction. A 3-day label-and-read control gave ~1% sharing (background).
- **Camellia-seq = scNMT-seq + lineage barcodes.** Cytoplasmic RNA (modified STRT-seq, including expressed barcode transcripts) is separated from the nucleus, which gets GpC methyltransferase then scBS-seq. In HSCs labelled at E10.0 and profiled at 9 months: ~50% of cells had a rare barcode, median ~100,000 UMIs from ~3,000 genes, ~70% of promoters and ~90% of gene bodies covered (≥3 GpC and ≥1 CpG), pseudobulk accessibility vs bulk ATAC Pearson r = 0.63.
- **DNA methylation carries clonal memory; expression and accessibility barely do.** Across 21 clones of ≥2 cells: intra-clone similarity for gene expression p = 0.049, chromatin accessibility p = 0.34, DNA methylation p = 1.2 × 10⁻¹⁰; 19 of 21 clones individually significant for methylation. 279 clone-differential CpG regions were neither near differentially regulated genes nor GO-enriched — the authors read them as random loci. Replicated across five mice (~750 cells passing QC, 63 clones of ≥2 cells; labelling windows from 36 h to 10 weeks).

## Methods / evidence

Germline knock-in mice (Dox-inducible Cas9-TdT at *Col1a1*, plus CA/TA/RA arrays); bulk RNA/DNA amplicon sequencing for allele statistics; 10x 3′ scRNA-seq with separate array amplification for single-cell lineage; plate-based Camellia-seq. Clone calling uses an explicit homoplasy model: per-allele generation probabilities from an allele bank (~300,000 granulocytes × 3 mice, sampled 3 days after Dox; ~110k/62k/37k alleles for CA/TA/RA), an FDR-based cutoff, and graph-based merging of cells sharing rare alleles across the three loci. Migration analysis used only *de novo* alleles with allele complexity ≥4. Tools: CARLIN pipeline (extended), snakemake_DARLIN, MosaicLineage (Python), CoSpar, Bismark.

Weight: the DARLIN vs Cas9/CARLIN comparison is internal to the same lab and mostly bulk granulocyte statistics, but the down-sampling experiment (fate bias lost at CARLIN-level coverage) is the strongest argument that coverage matters. The clonal-memory result rests on small clones (mostly 2–3 cells) and one cell type (HSCs), with accessibility assayed by GpC footprinting rather than ATAC. Camellia-seq is acknowledged to be low-throughput, costly and plate-based.

## Surprising or load-bearing bits

- **Methylation is a better clonal record than the transcriptome or accessibility** — exactly the property that endogenous-epimutation lineage methods exploit, shown here with engineered barcodes as ground truth. The differential regions being functionally random fits the idea of neutral, heritable epimutations rather than regulated states. (synthesis)
- **Coverage is not a nice-to-have.** Down-sampling DARLIN to CARLIN's ~10% rare-allele coverage erased the MkP-bias signal; a lineage system's barcode diversity and capture rate decide which biological questions are answerable at all. (synthesis)
- **The homoplasy model is the quiet methodological core**: rare-allele calling with an empirical allele bank and FDR, rather than treating every distinct allele as a clone.
- Array deletions remain a limitation for multi-generation tree reconstruction — DARLIN is a clone-labelling system more than a phylogeny recorder.

## Concepts touched

- [[crispr-lineage-recording]] — Cas9-TdT insertional editing and three independent arrays as a route to ~10¹⁸ barcode capacity.
- [[lineage-tracing]] — state–fate analysis (clonal coupling, CoSpar) with ~60% of cells clonally labelled.
- [[scnmt-seq]] / [[nome-seq]] — Camellia-seq extends scNMT-seq with transcribed lineage barcodes (GpC methyltransferase accessibility + CpG methylation).
- [[epigenetic-memory]] / [[methylation-clones-epimutation]] — clonal memory carried by CpG methylation in HSCs, not by expression or accessibility.
- [[hematopoietic-differentiation]] — early MkP bias in fetal-liver-stage HSCs; low-level inter-bone HSC circulation.

## Connections to other sources

- Ground-truth support for methylation-based clonal inference: [[scherer-2025-nature]] (EPI-Clone, validated against LARRY-barcoded HSCs) and [[chen-2025-methyltree]]; DARLIN shows the same clonal signal in genome-wide methylation with CRISPR barcodes as truth. (synthesis)
- Expressed-barcode state–fate predecessor from the same groups: [[weinreb-2020-larry]].
- Assay ancestry: [[clark-2018-scnmt-seq]] (scNMT-seq), [[smallwood-2014-natmethods]] / [[clark-2017-scbs-seq-protocol]] (scBS-seq back end).
- Other CRISPR recorders and their tree-building tools: [[mckenna-2016-science]] (GESTALT), [[jones-2020-cassiopeia]], [[sashittal-2023-startle]], [[chu-2025-laml]].
- Native haematopoiesis clonal dynamics by somatic mutations: [[lee-six-2018-hsc-dynamics]].
- Reviews placing CoSpar and multimodal lineage methods: [[wang-2026-multimodal-lineage-computational]], [[rodriguez-fraticelli-2026-lineage-tracing-review]].

## Open questions

- Is clonal methylation memory specific to self-renewing HSCs, or does it hold through differentiation, where methylation is remodelled?
- If the 279 clone-differential regions are random, is the memory just stochastic maintenance error inherited down a clone — and how quickly does it decay? (synthesis)
- Camellia-seq's GpC-based accessibility showed no clonal memory (p = 0.34); whether ATAC-based single-cell accessibility would agree is not tested.
- Allele generation probabilities are overestimated for the rarest bank alleles (acknowledged), so reliable-clone capacity figures are conservative.

## Related

- [[crispr-lineage-recording]] · [[40-Topics/single-cell-lineage-tracing]] · [[weinreb-2020-larry]] · [[scherer-2025-nature]]
