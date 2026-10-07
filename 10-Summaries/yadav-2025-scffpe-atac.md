---
type: summary
title: "Yadav et al. 2025 — scFFPE-ATAC enables high-throughput single cell chromatin accessibility profiling in formalin-fixed paraffin-embedded samples"
source: "[[00-Sources/papers/scFFPE-ATAC enables high-throughput single cell chromatin accessibility profiling in formalin-fixed paraffin-embedded samples]]"
source_kind: paper
author: "Ram Prakash Yadav, Pengwei Xing, Miao Zhao, Peter Hollander, Carina Strell, Minglu Xie, Maede Salehi, Emma Torell, Tobias Sjöblom, Gunilla Enblad, Rose-Marie Amini, Fredrik Johansson Swartling, Ingrid Glimelius, Patrick Micke, Mats Hellström, Xingqi Chen (corresponding)"
published: 2025-11-14
ingested: 2026-10-07
doi: "10.1038/s41467-025-66170-4"
journal: "Nature Communications 16:10022"
tags: [scFFPE-ATAC, FFPE, scATAC-seq, split-and-pool, combinatorial-indexing, T7-IVT, Tn5, DNA-damage-rescue, follicular-lymphoma, DLBCL, lung-cancer, tumor-invasive-edge, SnapATAC2, chromVAR, Slingshot]
entities: []
concepts: ["[[scatac-seq]]", "[[chromatin-accessibility]]", "[[tn5-tagmentation]]", "[[combinatorial-indexing]]", "[[transcription-factor-motif]]", "[[chromvar]]", "[[trajectory-inference]]", "[[pseudo-bulk]]", "[[quality-control-metrics]]", "[[intratumor-heterogeneity]]"]
topics: ["[[single-cell-atac-seq]]", "[[scdna-cancer-applications]]", "[[hematopoietic-malignancies]]"]
---

**Citation:** Yadav et al. (2025) — *scFFPE-ATAC enables high-throughput single cell chromatin accessibility profiling in formalin-fixed paraffin-embedded samples* — *Nature Communications* 16:10022. [DOI](https://doi.org/10.1038/s41467-025-66170-4)

# Yadav 2025 — scFFPE-ATAC

> Conventional scATAC-seq fails on FFPE nuclei not because cells are lost but because formalin/paraffin damage breaks DNA **between** the two Tn5 insertions a PCR-based library needs, so each cell's library collapses in complexity. scFFPE-ATAC sidesteps this by making amplification depend on a **single** insertion: an FFPE-Tn5 carrying 64 sample barcodes, three rounds of split-and-pool ligation barcoding (96 × 96 × 96; 56,623,104 combinations per run) ending in a **T7 promoter**, then reverse-crosslinking and **in vitro transcription** that copies every barcoded, accessible fragment regardless of downstream breaks. It recovers cell types and lineage TFs from mouse FFPE spleen, from human lymph nodes archived 8–12 years, from lung-cancer punch cores (tumor center vs invasive edge) and from paired primary/relapsed follicular lymphoma.

## Key claims

- **Conventional scATAC-seq on FFPE nuclei cannot resolve cell types.** On mouse FFPE spleen, merged FFPE profiles correlated only r = 0.41–0.46 with fresh tissue (bulk and merged single-cell, ±reverse crosslinking); peaks dropped to 32,512 (−RV) / 47,809 (+RV) vs 89,328 in fresh. At ≥1500 fragments and TSS ≥4, only 30 (−RV) and 595 (+RV) cells passed vs 4843 fresh; the +RV clusters were not supported by spleen marker gene activity, and this held at relaxed thresholds (e.g. 8777 cells, seven clusters at ≥500 fragments) — no spleen cell-type genes were detected.
- **Reverse crosslinking raises DNA yield but not library complexity.** +RV and −RV bulk ATAC profiles correlate at r = 0.94; duplication rates were 57.41% (−RV) and 68.85% (+RV) vs 34.73% fresh; median fragments/cell 1865 / 1863 vs 6722 fresh.
- **scFFPE-ATAC restores per-cell complexity and cell-type resolution.** Mouse FFPE spleen: 18,200 cell-associated barcodes, 13,954 high-quality cells (76.67%) at the same cutoffs; median duplication 30.81% (vs 34.73% fresh), median unique fragments 2722 (vs 6722 fresh; ~1.45× conventional FFPE scATAC), 86,518 peaks (vs 89,328 fresh), genome-wide correlation with fresh r = 0.83. T, B and myeloid cells recovered in fresh-like proportions with matching lineage TFs (EBF1/TCF3/POU in B; TCF7L2, LEF1, ETS, RUNX in T; FOS/MAF/GATA1 in myeloid).
- **Costs of the design are explicit.** Merged TSS enrichment was 7.5 (below fresh) and median FRiP 21% (vs 42% fresh, and below conventional FFPE scATAC's ~29–30%); the authors attribute this to single-insertion amplification admitting noise, possible T7 IVT sequence bias, and formalin restricting Tn5 access.
- **~200–300 cells suffice.** Merging 200 FFPE cells gives r > 0.7 with a 5,000-cell profile; 300 cells capture the spleen's cell components on downsampling — which the authors use to rule out "too few cells" as the reason conventional scATAC failed.
- **Archived human tissue works.** Four benign lymph nodes stored 8–12 years: 12,243 cells after doublet removal (LN1–4: 1,883 / 7,035 / 3,116 / 209), median FRiP 13.87%, median 1356 unique fragments, duplication 48.5%; five populations (T, myeloid, three B-cell states) with lineage TFs (CEBP family in myeloid; EBF1/TCF3 in B, strongest in B S3).
- **Spatial tumor biology from punch cores.** A lung-cancer FFPE block sampled with a 1 mm puncher at tumor center (TC, 4,833 cells) and invasive edge (IE, 6,731 cells): 11,564 cells, six populations. Epithelial TC vs IE differential peaks (22,219 / 14,610) carried Wnt, Ras and mesenchymal-differentiation terms at the edge. Slingshot found two epithelial trajectories rooted in TC-dominated clusters (recovered in 97.5% and 93.5% of bootstraps): one proliferative/differentiated (FOXA1, GRHL1, HOX), one enriched for KLF5, RUNX2, HEY1, ONECUT2 — TFs the authors link to hypoxia-responsive programs.
- **Paired relapse samples.** Two FL patients (13,357 cells): patient 1 transformed FL→DLBCL over 7 years (Tumor B1 85.22%→12.75%; Tumor B2 0.6%→8.53%); patient 2 relapsed as FL over 2 years (Tumor B1 2.89%→74.56%; Tumor B2 32.58%→11.50%). Normal-B-rooted pseudotime gave two tumor trajectories (each recovered in 83% of bootstraps); the primary tumors of the two patients sat on different branches, read by the authors as different tumor origins.

## Methods / evidence

- **Nuclei isolation**: a modified density gradient (25%/36%/48%) because FFPE nuclei, unlike fresh, are *lighter* than debris and band at the 25–36% interface.
- **Chemistry**: FFPE-Tn5 with 64 indexed adaptors → three split-and-pool ligations (ligation-1/2 oligos kept to 22 nt so IVT products carry genomic sequence, not only barcode) → reverse crosslinking → gap filling → T7 IVT → library from RNA. Collision rate estimated at 2.77% for 50,000 input cells (birthday-paradox formula from SHARE-seq).
- **Computation**: in-house demultiplexing; minimum read length lowered to 17 bp (dropping 50→14 bp raised decoding 48%→70% and unique fragments +35.55% with mapping 97.85%→92.68%); BWA `mem -k17`; MACS2; SnapATAC2 (spectral embedding, scrublet doublets, Harmony, Leiden) + Scanpy/MAGIC for gene activity; pseudo-bulks of 500 random cells for differential peaks; chromVAR + JASPAR for TF enrichment; Slingshot with 1000-bootstrap support.
- **Practicalities**: overall recovery ~20% after split-and-pool (11.05–22.36% by sample), needs 250,000–500,000 nuclei, ~5 working days, ~$632 per 100,000–200,000 cells; tested fixation 16–72 h and storage 6 months–13 years.

Weight: the mouse spleen benchmark is a clean paired fresh-vs-FFPE comparison with conventional scATAC run in parallel, so the technical claims are well supported. The clinical biology rests on n = 1 lung tumor and n = 2 lymphoma patients, and TF "drivers" are motif enrichments interpreted from the literature — hypothesis-generating, not causal. No other FFPE single-cell accessibility method is benchmarked.

## Surprising or load-bearing bits

- **The failure mode is mechanistic and generalises**: two-sided PCR libraries need both Tn5 ends intact on one molecule; any break in between silently deletes the fragment. Linear amplification from a single anchored promoter tolerates breaks. This is the same logic as T7-based linear amplification elsewhere in single-cell genomics (synthesis).
- **Lower FRiP alongside higher complexity**: scFFPE-ATAC gains unique fragments but loses signal-to-noise relative to both fresh tissue and conventional FFPE scATAC — the authors concede single-insertion amplification can rescue noise as well as signal.
- **Fragment-size distributions are almost entirely short** (98.76% at 0–300 bp in mouse spleen; 96.28% at 0–100 bp in archived lymph nodes; 97.72% at 0–100 bp in lymphoma), so nucleosome-ladder QC used for fresh ATAC is not available as a quality readout here (synthesis).
- Library quality did not track FFPE DNA fragmentation; the authors currently pre-assess by nuclei purity and call for a DV200-like DNA metric.

## Concepts touched

- [[scatac-seq]] — extends scATAC to archival FFPE material via linear (IVT) amplification.
- [[combinatorial-indexing]] — 64 × 96³ barcode space; collision-rate estimate reused from SHARE-seq.
- [[tn5-tagmentation]] — a custom-adaptor FFPE-Tn5 carrying both sample index and T7 path.
- [[chromvar]] — used for TF deviation/variability on cell-type and condition peaks.
- [[trajectory-inference]] — Slingshot on gene-activity embeddings with bootstrap branch support.
- [[pseudo-bulk]] — 500-cell random pseudo-bulks to handle sparsity in differential testing.
- [[intratumor-heterogeneity]] — spatial (center vs edge) and temporal (primary vs relapse) heterogeneity read from accessibility.

## Connections to other sources

- Prior FFPE single-cell accessibility attempt with a different enzyme: [[jin-2015-nature]] (scDNase-seq on FFPE).
- Split-and-pool scATAC lineage it builds on: [[cusanovich-2015-sciatac]]; collision formula from [[ma-2020-share-seq]].
- Analysis stack: [[zhang-2024-snapatac2]], [[schep-2017-chromvar]], [[korsunsky-2019-harmony]], [[traag-2019-leiden]], [[zhang-2008-macs]], [[li-2009-bwa]].
- Benchmarks of scATAC processing that frame its QC choices: [[luo-2024-scatac-benchmark]], [[gur-2025-scatac-vs-bulk]].

## Open questions

- No head-to-head with fresh-frozen human tissue from the same patients; how much of the TC/IE and relapse signal is fixation-batch versus biology is not separable with these designs.
- Whether linear-amplification noise inflates "accessible" calls in low-FRiP cells — and how that interacts with differential peak calling on 500-cell pseudo-bulks — is not quantified.
- Matrix-rich tumors (e.g. PDAC), >72 h fixation and longer storage are untested; recovery (~20%) and nuclei input (≥250,000) limit small biopsies.

## Related

- [[scatac-seq]] · [[combinatorial-indexing]] · [[40-Topics/single-cell-atac-seq]] · [[40-Topics/hematopoietic-malignancies]]
