---
type: summary
title: "Wu et al. 2021 — Single-cell CUT&Tag analysis of chromatin modifications in differentiation and tumor progression"
source: "[[00-Sources/papers/Single-cell CUT&Tag analysis of chromatin modifications in differentiation and tumor progression]]"
source_kind: paper
author: "Steven J. Wu, Scott N. Furlan, Anca B. Mihalas, Hatice S. Kaya-Okur, ... Kami Ahmad, Steven Henikoff, Anoop P. Patel (corresponding)"
published: 2021-04-12
ingested: 2026-08-10
doi: "10.1038/s41587-021-00865-z"
journal: "Nature Biotechnology"
tags: [scCUT&Tag, H3K27me3, Polycomb, repressive-chromatin, glioblastoma, droplet, ICELL8, chromatin-silencing-score]
entities: ["[[steven-henikoff]]"]
concepts: ["[[cut-and-tag]]", "[[scatac-seq]]", "[[chromvar]]", "[[pseudo-bulk]]", "[[icell8-nanowell]]"]
topics: ["[[histone-modifications]]", "[[cancer-clonal-evolution]]"]
---

**Citation:** Wu et al. (2021) — *Single-cell CUT&Tag analysis of chromatin modifications in differentiation and tumor progression* — *Nature Biotechnology* 39, 819–824. [DOI](https://doi.org/10.1038/s41587-021-00865-z)

# Wu 2021 — repressive chromatin as a cell-identity readout

> scCUT&Tag scaled to nanowell and droplet platforms, applied to a deliberately counterintuitive target: **H3K27me3**. What is silenced turns out to identify cell type as well as what is open — an orthogonal axis to accessibility, and one that works on frozen tissue and archival tumor material.

## Key claims

- H3K27me3 signal binned at **5 kb** (matched to the >10 kb scale of PcG domains) → LSI → UMAP → Louvain in ArchR separates 100% of 804 hESCs from 908 K562 cells.
- hESCs carry **6% as many unique fragments** as K562 (median 375 vs 6,064) — a real biological signal (stem cells have globally lower H3K27me3), and the authors control for it by downsampling to matched median depth, after which separation persists.
- Directed hESC→definitive endoderm differentiation (1,830 cells, median 279 fragments) traces a trajectory: stem-like on days 1–2, rapid progression days 3–5. H3K27me3 at marker genes is **inversely correlated** with published scRNA-seq expression — *SOX2/KLF4/FOXD3* lose expression and gain the mark; *FOXA2/SOX17/PRDM1* activate and lose it; ectoderm markers *PAX6/LHX2* accumulate it. The transient mesendoderm state (days 2–3) shows reduced silencing at mesoderm markers.
- Adapted to **10x Genomics**: 9,917 PBMCs, median 1,110 fragments. A **chromatin silencing score (CSS)** repurposes ArchR's gene-activity model, so a cell-type marker gene shows *low* CSS in its own cell type. Cluster identities from CSS match identities from projecting downsampled ENCODE bulk H3K27me3 ChIP-seq onto the same embedding; recovered proportions fall in the normal adult blood range. **Cell-type-specific PcG landscapes are obtained without sorting.**
- souporcell demultiplexes two donors from genotype in the reads — clustering is driven by cell type, not donor.
- Glioblastoma, primary (1,311 cells) and post-treatment autopsy (1,168 cells): four populations annotated by CSS (microglia/*PTPRC*, neurons/*RBFOX3*, oligodendrocytes/*MOBP*, tumor+neural/*SOX2*) and confirmed by projecting patient-derived glioma stem cell CUT&RUN, neural stem cell lines, and ENCODE monocyte/astrocyte bulk data.
- Relapse cells enrich in tumor subcluster **T1**. The proneural gene set is silenced there, consistent with proneural-to-mesenchymal shift; low CSS at high-CpG H3K27me3-marked brain gene sets suggests the resistant cluster's PcG landscape resembles a **stem-like rather than terminally differentiated** state.
- Motif analysis on H3K27me3 requires a trick: domains span 10–100 kb, so scATAC data is used to restrict motif searching to accessible enhancers/promoters *within* the domains. Pseudotime from T1 reveals shared early silencing (NEUROD1, SNAI2, TCF12) then trajectory-specific (NR1DA2 vs ETV5) and shared late (DNMT1) motif silencing.

## Methods / evidence

Two platforms (ICELL8 nanowell with imaging-verified singlets; 10x scATAC kit after bulk tagmentation), with a stated QC ladder for droplet data: remove clusters with nucleosomal fragment-length distributions indicating **untethered transposition**, remove clusters with high mean fragment counts, then iteratively remove clusters with no significantly enriched or depleted CSS genes. Overlap with ATAC peaks is measured per cell as an explicit artifact check — minimal for H3K27me3, higher for the active mark H3K4me2, exactly as expected.

Honest limitation, stated: only 71 autopsy tumor cells passed QC, so relapse conclusions rest on co-embedding with 640 primary cells rather than standing alone. Relapse cells also had higher background by FRiP.

## Surprising or load-bearing bits

- **Silenced chromatin is a first-class cell-identity signal.** This inverts the field's default (accessibility = identity) and has a practical consequence: repressive marks are broad, so they tolerate sparsity better than narrow active marks — cell typing works at ~300–1,100 fragments per cell, depths where scATAC struggles.
- Global mark abundance is itself biology, not just a quality metric. The hESC/K562 6% difference would look like a batch effect in a routine QC pass. Any pipeline that regresses out per-cell fragment count risks regressing out the signal.
- The untethered-transposition QC step operationalizes the ATAC-background caveat from [[kaya-okur-2019-cut-and-tag]]: it is detectable as a **nucleosomal fragment-length ladder** in specific clusters.
- Frozen glioblastoma and rapid-autopsy tissue both work. Combined with no-sorting cell-type resolution, this makes archival clinical material tractable — the strongest translational argument for the method.
- Silencing of the DNMT1 motif across both tumor pseudotime endpoints ties PcG silencing to DNA-methylation machinery targeting — a cross-layer link relevant to [[regulatory-layers-overview]].

## Concepts touched

- [[cut-and-tag]] — first scaled single-cell application across platforms and primary tissue.
- [[chromvar]] — motif deviation analysis adapted to a repressive mark by masking to accessible sub-regions.
- [[pseudo-bulk]] — cell-type-specific bulk-equivalent tracks generated computationally instead of by sorting.

## Connections to other sources

- Direct successor to [[kaya-okur-2019-cut-and-tag]] (shared authors); parallel to [[bartosovic-2021-sccut-tag]] (mouse brain, same year).
- Used as the **query dataset** mapped onto the multimodal reference in [[zhang-2022-sccut-tag-pro]], which resolves its broad clusters into granular subsets.
- Analysis stack: [[granja-2021-archr|ArchR]], [[traag-2019-leiden|Louvain/Leiden]], [[mcinnes-2018-umap|UMAP]].
- Bivalency and poised-state context: [[bernstein-2006-bivalent-chromatin]], [[roadmap-2015-111-epigenomes]].
- Tumor-heterogeneity framing connects to [[cancer-clonal-evolution]] and [[kim-2018-tnbc-chemoresistance]].

## Open questions

- Is H3K27me3 heterogeneity within the tumor **clonal** (genetically determined) or **plastic**? This paper cannot say — it has no paired genotype. That is precisely the gap [[izzo-2024-got-cha|GoT-ChA]] addresses for accessibility and which remains open for histone marks; tracked at [[mosaicism-and-epigenome-the-synthesis-gap]].
- 71 cells is thin for the resistance claim; no independent replication in this corpus.

## Related

- [[kaya-okur-2019-cut-and-tag]] · [[zhang-2022-sccut-tag-pro]] · [[cut-and-tag]] · [[histone-modifications]]
