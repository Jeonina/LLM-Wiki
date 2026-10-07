---
type: summary
title: "Galasso et al. 2026 — map3C: a computational tool for processing multiomic single-cell Hi-C data"
source: "[[00-Sources/papers/map3C_ a computational tool for processing multiomic single-cell Hi-C data]]"
source_kind: paper
author: "Joseph Galasso, Ye Wang, Frank Alber, Jason Ernst, Chongyuan Luo"
published: 2026-07-29
ingested: 2026-10-07
doi: "10.1093/bioinformatics/btag562"
journal: "Bioinformatics 42(8):btag562"
tags: [map3C, single-cell-Hi-C, snm3C-seq, LiMCA, contact-calling, pairtools, multimapping, structural-variants, MAPQ, IGM, 3D-modelling, application-note]
entities: ["[[20-Entities/chongyuan-luo]]"]
concepts: ["[[single-cell-hi-c]]", "[[structural-variants]]", "[[read-alignment]]", "[[quality-control-metrics]]", "[[bisulfite-sequencing]]", "[[joint-single-cell-multi-omics]]"]
topics: ["[[3d-genome]]", "[[computational-methods]]"]
---

**Citation:** Galasso et al. (2026) — *map3C: a computational tool for processing multiomic single-cell Hi-C data* — *Bioinformatics* 42(8):btag562. [DOI](https://doi.org/10.1093/bioinformatics/btag562)

# Galasso 2026 — map3C

> An application note naming three gaps in contact-calling for **multiomic single-cell Hi-C** (LiMCA for transcription + 3C, snm3C-seq for methylation + 3C) and closing them in one tool. (1) **Sticky-end proximity ligation leaves a single restriction-enzyme motif at the junction that aligners multimap to both loci**; map3C trims it. (2) The earlier snm3C-seq contact callers (TAURUS-MH, YAP) **report no MAPQ-based QC**; map3C filters on MAPQ. (3) No multiomic scHi-C tool calls **structural-variant breakpoints at 1 bp**; map3C flags contacts far from RE cut sites, and soft-clipped junctions reveal exact breakpoints. Contact calling itself is delegated to Pairtools.

## Key claims

- **Pipeline.** Input is locally aligned paired-end reads: BWA-MEM/MEM2 for non-bisulfite data, Biscuit or BSBolt for bisulfite (snm3C-seq). Steps: MAPQ filter → Pairtools "mask" contact calling (optionally "all" for >2 loci per read pair) → RE-cut-site proximity annotation to flag likely SV-induced contacts → trimming of multimapped spans between adjacent soft-clipped alignments. Outputs are a trimmed BAM and an annotated PAIRS file.
- **Broader SV calls than HiNT-TL.** map3C reports all contacts likely caused by SVs, intra- and interchromosomal. HiNT-TL reports only interchromosomal SVs and is incompatible with sticky-end PL datasets such as LiMCA.
- **SV breakpoints in K562 (63 LiMCA cells).** 358,716 candidate bp-resolution breakpoints. Intersecting with 112 EagleC 5-kb breakpoints from the merged contacts left 61 1-bp breakpoints inside 44 EagleC SVs. **23 of 61 validated** within ±10 bp of 4,273 WGS SV calls. Precision **0.30**, recall **0.0033**. The authors attribute the low recall to the EagleC intersection and argue true precision may be higher because K562 clonal evolution could create SVs absent from the WGS data.
- **Artifact control by cross-cell-line comparison.** 93% of K562 EagleC breakpoints had no supporting contacts in LiMCA data from 221 GM12878 cells, even though the GM12878 data had 3.1× more reads. This suggests most breakpoints are not technical artifacts shared across lines.
- **Multimapping is common.** 26% of 3,342,056 soft-clipped alignments in one LiMCA mouse olfactory epithelium cell multimapped; trimming removed 8% (SD 4%) of their read span. In one snm3C-seq mESC, 30% of 251,356 soft-clipped alignments multimapped and 11% (SD 7%) of their span was trimmed.
- **Trimming fixes haplotype conflicts.** Among alignments covering ≥3 SNPs with conflicting haplotype assignments (5,810 in 40 DBA/2J×C57BL cells; 34,471 in 40 CAST/EiJ×C57BL/6J cells), trimming resolved **77% and 79%**. Randomly removing the same number of SNP observations resolved only 28% (SD 0.6%) and 29% (SD 0.2%).
- **MAPQ filtering raises contact quality in snm3C-seq (351 mESCs).** Intra-to-interchromosomal contact ratio: map3C 3.16 ± 1.23, TAURUS-MH 0.98 ± 0.26, YAP 1.10 ± 0.31. map3C is closest to the 4.22 reported by the 4DNucleome pipeline. Interchromosomal contacts were significantly lower with map3C (P < .001, one-sided Mann–Whitney U).
- **More physically consistent 3D models.** In modified IGM structures, the median restraint-violation rate was 0.004 with map3C, against 0.051 (TAURUS-MH) and 0.037 (YAP); P < .001. TAURUS-MH and YAP models packed ~88% and ~83% of chromatin into the two innermost shells, and their innermost shell was 75% and 55% denser than in map3C models.
- **Imaging agreement.** Against DNA seqFISH+ in mESC, map3C-derived models better recapitulate radial positioning. Interchromosomal contact probability correlates with imaging at Spearman r = 0.76, against 0.45 (YAP) and 0.51 (TAURUS-MH).

## Methods / evidence

Three worked cases on public LiMCA (GSE240128) and snm3C-seq (GSE124391) data: SV breakpoints in K562, multimapping trimming in mouse cells with SNP haplotype checks, and snm3C-seq QC feeding integrative genome modelling with seqFISH+ validation. Comparisons are against TAURUS-MH, YAP (contact callers), HiNT-TL (conceptual SV comparison) and EagleC (5-kb SV calls, used as a filter).

Weight: an application note with careful internal controls (random-removal baseline, cross-cell-line artifact filter, imaging benchmark). The SV result is the weakest: precision 0.30 against WGS ground truth, recall 0.0033, and dependence on EagleC pre-filtering. The QC/3D-model result is the strongest, since it rests on orthogonal imaging. Note that the two senior groups (Alber: IGM; Luo: snm3C-seq) also built the downstream models used for evaluation. (synthesis)

## Surprising or load-bearing bits

- **The "ligation junction motif" artifact.** A sticky-end junction contains one RE motif, but the aligner can place it on both flanking loci. The motif can only come from one locus *in vivo*, so the duplicated span yields false SNP calls and false haplotype conflicts. The haplotype-conflict test is a neat way to show the artifact matters. A similar artifact class, from a different mechanism, motivated scBS-map in single-cell methylation data.
- **Earlier snm3C-seq contacts were contaminated with spurious interchromosomal pairs.** The roughly 3× higher intra/inter ratio after MAPQ filtering means the older pipelines' outputs carried many low-MAPQ trans contacts. IGM then compressed chromatin toward the nuclear centre to satisfy them. Downstream 3D analyses built on TAURUS-MH/YAP contacts deserve re-checking. (synthesis)
- **scHi-C as a WGS-style SV caller.** Soft-clipped alignments spanning a ligation junction carry breakpoint-level information. Multiomic 3C data can therefore yield a genomic-variant layer alongside conformation and methylation, though precision is still low. (synthesis)

## Concepts touched

- [[single-cell-hi-c]] — a processing layer (multimapping trimming, MAPQ QC) specific to sticky-end, multiomic scHi-C.
- [[structural-variants]] — bp-resolution SV breakpoint candidates from scHi-C contacts.
- [[read-alignment]] — junction multimapping as an aligner-induced artifact; bisulfite-aware BWA-based aligners.
- [[quality-control-metrics]] — intra/inter contact ratio and IGM restraint-violation rate as quality readouts.
- [[joint-single-cell-multi-omics]] — LiMCA (RNA + 3C) and snm3C-seq (methylation + 3C).

## Connections to other sources

- Processes data from the assays in [[lee-2019-natmethods]] (sn-m3C-seq); multiomic scHi-C context in [[tan-2018-science]], [[liu-2023-mouse-brain-methylome-3d]], [[chang-2025-droplet-hi-c]] (which also uses pairtools and EagleC).
- Bulk Hi-C processing lineage it builds on: [[lieberman-aiden-2009-hic]], [[servant-2015-hicpro]], [[durand-2016-juicer]], [[abdennur-2020-cooler]]; aligner [[li-2009-bwa]].
- Complements the unified sc3DG pipeline in [[jiang-2026-stark-scnucleome]] and the method overview in [[hong-2025-sc3d-genome-review]]. map3C targets an earlier step (alignment → contacts) for multiomic data specifically. (synthesis)
- Downstream single-cell 3D tools that consume contact files: [[zhou-2019-schicluster]], [[zhang-2022-higashi]], [[yu-2021-snaphic]].

## Open questions

- How many published conclusions from TAURUS-MH/YAP-processed snm3C-seq data (e.g., trans-contact or compartment patterns) change after MAPQ filtering? (synthesis)
- Can SV precision be raised without discarding most calls through EagleC intersection? WGS-style artifact filters across many cell lines are proposed but not done.
- Contamination of trans contacts may also affect cell-type clustering from scHi-C; this is not tested. (synthesis)

## Related

- [[chongyuan-luo]] · [[single-cell-hi-c]] · [[lee-2019-natmethods]] · [[40-Topics/3d-genome]]
