---
type: concept
title: Topologically associating domain (TAD)
aliases: [TAD, TAD boundary]
tags: [3D-genome, chromatin, Hi-C]
created: 2026-05-12
updated: 2026-10-07
---

# Topologically associating domain (TAD)

> A self-interacting genomic neighborhood (~100 kb–1 Mb) defined by frequent within-domain Hi-C contacts and a sharp drop in contacts at the domain boundary. CTCF and cohesin are the major TAD-boundary architects.

## Definition

TADs are insulated regulatory neighborhoods. Loss of a TAD boundary can rewire enhancer-promoter contacts and dysregulate gene expression — a mechanism implicated in cancer and developmental disorders.

## Why it matters

TADs constrain which enhancer–promoter contacts can occur. Disrupting TAD boundaries (by CTCF binding site mutation or by structural variation) is a known mechanism of cancer dysregulation (e.g., TAL1 enhancer hijacking in T-ALL).

## Causal evidence and boundary conditions

- **Boundaries are load-bearing, and distance is not the explanation.** CRISPR-engineered mouse alleles reproducing three human limb-malformation rearrangements at the *EPHA4* locus each disrupt a boundary, let an *EPHA4* enhancer cluster capture *PAX3*, *WNT6* or *IHH*, and phenocopy the disease; near-identical deletions that **spare the boundary** give normal limbs, no misexpression and reduced ectopic contact ([[10-Summaries/lupianez-2015-tad-disruption]]).
- **Contact is necessary but not sufficient.** Many genes fall inside the new contact domain yet stay silent — promoter receptiveness matters, and the responders are developmental genes ([[10-Summaries/lupianez-2015-tad-disruption]]).
- **TADs are an interphase-only feature.** Both A/B compartments and sub-megabase TADs collapse in metaphase across HeLa S3, K562 and primary HFF1, giving a homogeneous locus- and cell-type-invariant fold — so boundary function is re-established every cell cycle ([[10-Summaries/naumova-2013-mitotic-chromosome]]).
- **TAD calling is threshold-dependent.** Identification "relies heavily on computational methods, which display a high degree of variation depending on the resolution and the adjustment of thresholds," and substantial genome regions have no detectable TADs ([[10-Summaries/spielmann-2018-sv-3d-genome]]).
- **Insulation is not absolute** — the *SHH* ZRS enhancer acts across a boundary when genomic distance is reduced enough, and deleting only the boundary plus its CTCF sites at *Sox9* had no major effect ([[10-Summaries/spielmann-2018-sv-3d-genome]]).
- **Two operational definitions coexist**: Dixon-style insulation-score TADs, and Arrowhead "contact domains" called by dynamic programming on the transformed contact matrix ([[10-Summaries/durand-2016-juicer]]).

## Founding source and its qualifications (added 2026-08-10)

[[10-Summaries/dixon-2012-tads]] is the founding source: the directionality index plus an HMM, 2,200 domains in mouse ES cells at median 880 kb covering ~91% of the genome, boundaries enriched for CTCF, housekeeping genes, tRNAs and SINEs, and conservation of 53.8–75.9% between mouse and human against a 21–29% random expectation.

Three standing qualifications. **Only 15% of CTCF binding sites lie within boundaries**, so boundary identity is combinatorial rather than CTCF-determined ([[10-Summaries/dixon-2012-tads]]). **Callers disagree**: seven TAD callers on the same matrix produce inconsistent domains of widely varying size ([[10-Summaries/kerpedjiev-2018-higlass]]), and cohesin-loading loss erases TADs while *strengthening* compartments ([[10-Summaries/kerpedjiev-2018-higlass]]). **Per cell, boundaries are distributions**: single-cell insulation scores show boundaries that are present/absent across the population *and* boundaries that slide along the genome between cells ([[10-Summaries/zhang-2022-higashi]]).


## Added 2026-10-07

Micro-C revealed TAD-like chromosomal interaction domains in budding yeast spanning roughly one to five genes (~2–10 kb), bounded mostly at promoter nucleosome-depleted regions of highly transcribed genes; domain size appears conserved in gene number rather than base pairs across yeast and mammals ([[10-Summaries/hsieh-2015-micro-c]]). The authors speculate that boundary establishment, not regular secondary structure, drives chromosome folding ([[10-Summaries/hsieh-2015-micro-c]]). Boundary nucleosomes are mostly promoter +1 nucleosomes carrying H3K18ac/H3K4me3, high histone turnover, RSC and the cohesin loader Scc2, and strong boundaries lie upstream of more highly transcribed genes ([[10-Summaries/hsieh-2015-micro-c]]). Within domains, gene compaction is anticorrelated with transcription (r = −0.56) ([[10-Summaries/hsieh-2015-micro-c]]).

In single mESCs profiled by scSPRITE, 95% of cells have a positive average TAD detection score across 2,602 ensemble boundary regions. Yet most individual TADs are highly variable between cells, and the variable TADs cluster in shared genomic regions ([[10-Summaries/arrastia-2022-scsprite]]). At chr4:38.5–43.6 Mb, a subset of cells forms an alternative TAD spanning an ensemble A/B compartment boundary, which suggests mutually exclusive structural states not explained by cell cycle ([[10-Summaries/arrastia-2022-scsprite]]).

In single cells TADs are far less consistently detected than compartments. In scNanoHi-C GM12878 data, a TAD was on average detected in ≤60% of cells, and 12% of boundaries (295/2,503) were rarely detected. Boundaries bound by CTCF scored higher, which the authors read as dynamic loop extrusion reinforced by CTCF ([[10-Summaries/li-2023-scnanohi-c]]).

TAD-boundary recovery from aggregated single-cell maps is a benchmark axis for scHi-C normalization. For GM12878, the median share of boundaries within 1 Mb of bulk boundaries was 85.71% (BandNorm), 66.67% (scVI-3D), 60% (Higashi) and 60.87% (scHiCluster) ([[10-Summaries/zheng-2022-bandnorm-scvi-3d]]).

At kilobase resolution, contact domains (called with Arrowhead) range from 40 kb to 3 Mb with a median of 185 kb, much smaller than the ~1 Mb TADs seen in lower-resolution maps ([[10-Summaries/rao-2014-in-situ-hic]], [[10-Summaries/dixon-2012-tads]]). Rao et al. attribute the difference to resolving additional boundaries, and nearly all boundaries coincide with a subcompartment transition or a loop ([[10-Summaries/rao-2014-in-situ-hic]]). The inactive X is split into two "superdomains" whose boundary lies near *DXZ4* ([[10-Summaries/rao-2014-in-situ-hic]]).

In a 2025 survey, four tools call TADs from single-cell Hi-C: Higashi, scHiCEmbed, HiCS and DeDoc2. Higashi and scHiCEmbed also do clustering, and Higashi does compartment calling as well ([[10-Summaries/dautle-2025-schic-review]]).


## Related

- [[40-Topics/3d-genome]] · [[30-Concepts/chromatin-compartments]] · [[30-Concepts/single-cell-hi-c]] · [[40-Topics/3d-genome]]
- [[10-Summaries/lupianez-2015-tad-disruption]] · [[10-Summaries/spielmann-2018-sv-3d-genome]] · [[10-Summaries/naumova-2013-mitotic-chromosome]] · [[10-Summaries/durand-2016-juicer]]
