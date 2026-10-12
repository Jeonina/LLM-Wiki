---
type: concept
title: Topologically associating domain (TAD)
aliases: [TAD, TAD boundary]
tags: [3D-genome, chromatin, Hi-C]
created: 2026-05-12
updated: 2026-10-12
---

# Topologically associating domain (TAD)

> A self-interacting genomic neighbourhood (~100 kb–1 Mb) defined by frequent within-domain Hi-C contacts and a sharp drop in contacts at the domain boundary, with CTCF and cohesin as the major boundary architects ([[10-Summaries/dixon-2012-tads|Dixon 2012]]; [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

> [!abstract] 한눈에
> TAD는 Hi-C에서 내부 접촉이 잦고 경계에서 접촉이 뚝 떨어지는 유전체 구역이며, 경계가 무너지면 enhancer가 엉뚱한 유전자와 만나 질환을 일으킬 수 있다 ([[10-Summaries/dixon-2012-tads|Dixon 2012]]; [[10-Summaries/lupianez-2015-tad-disruption|Lupiáñez 2015]]). 다만 TAD 크기와 경계는 해상도와 caller에 따라 달라지고, single cell에서는 같은 TAD가 세포마다 있다가 없다가 하는 분포로 나타난다 ([[10-Summaries/kerpedjiev-2018-higlass|HiGlass]]; [[10-Summaries/zhang-2022-higashi|Higashi]]; [[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).

<!-- explainer-links -->
> [!tip] 📘 교재
> [3D 유전체 교재](../60-Explainers/3d-genome.html)
<!-- /explainer-links -->

## Definition

TADs are insulated regulatory neighbourhoods; loss of a TAD boundary can rewire enhancer–promoter contacts and dysregulate gene expression, a mechanism implicated in cancer and developmental disorders ([[10-Summaries/lupianez-2015-tad-disruption|Lupiáñez 2015]]; [[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]).

[[10-Summaries/dixon-2012-tads|Dixon 2012]] is the founding source: a directionality index plus an HMM called 2,200 domains in mouse ES cells at median 880 kb covering ~91% of the genome, with boundaries enriched for CTCF, housekeeping genes, tRNAs and SINEs, and conservation of 53.8–75.9% between mouse and human against a 21–29% random expectation ([[10-Summaries/dixon-2012-tads|Dixon 2012]]).

Two operational definitions coexist: Dixon-style insulation-score TADs, and Arrowhead "contact domains" called by dynamic programming on the transformed contact matrix ([[10-Summaries/durand-2016-juicer|Juicer]]). At kilobase resolution, contact domains range from 40 kb to 3 Mb with a median of 185 kb, much smaller than the ~1 Mb TADs seen in lower-resolution maps ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]; [[10-Summaries/dixon-2012-tads|Dixon 2012]]); Rao et al. attribute the difference to resolving additional boundaries ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

## Why it matters

TADs constrain which enhancer–promoter contacts can occur. Disrupting TAD boundaries, by CTCF binding-site mutation or by structural variation, is a known mechanism of cancer dysregulation (e.g. TAL1 enhancer hijacking in T-ALL).

## Calling approaches

| Approach | Example | What it gives | Source |
|---|---|---|---|
| Directionality index + HMM | [[10-Summaries/dixon-2012-tads\|Dixon 2012]] | 2,200 mouse ES-cell domains, median 880 kb | ([[10-Summaries/dixon-2012-tads\|Dixon 2012]]) |
| Insulation score | Dixon-style TADs | Domains from local insulation | ([[10-Summaries/durand-2016-juicer\|Juicer]]) |
| Arrowhead dynamic programming | [[10-Summaries/durand-2016-juicer\|Juicer]]; [[10-Summaries/rao-2014-in-situ-hic\|Rao 2014]] | Contact domains of 40 kb–3 Mb (median 185 kb) at kilobase resolution | ([[10-Summaries/durand-2016-juicer\|Juicer]]; [[10-Summaries/rao-2014-in-situ-hic\|Rao 2014]]) |
| Single-cell insulation scores | [[10-Summaries/zhang-2022-higashi\|Higashi]] | Per-cell boundaries that are present/absent across cells and that slide along the genome | ([[10-Summaries/zhang-2022-higashi\|Higashi]]) |
| Single-cell TAD callers | Higashi, scHiCEmbed, HiCS, DeDoc2 | Four tools call TADs from single-cell Hi-C; Higashi and scHiCEmbed also cluster, and Higashi also calls compartments | ([[10-Summaries/dautle-2025-schic-review\|Dautle 2025]]) |
| Boundary recovery from aggregated scHi-C | BandNorm, scVI-3D, Higashi, scHiCluster | A benchmark axis for scHi-C normalization | ([[10-Summaries/zheng-2022-bandnorm-scvi-3d\|Zheng 2022]]) |
| Sequence-to-contact models | [[10-Summaries/fudenberg-2020-akita\|Akita]]; [[10-Summaries/avsec-2021-enformer\|Enformer]]; [[10-Summaries/fang-2025-evo2hic\|Evo2HiC]] | Contact maps or insulation predicted from DNA sequence alone | ([[10-Summaries/fudenberg-2020-akita\|Akita]]; [[10-Summaries/avsec-2021-enformer\|Enformer]]; [[10-Summaries/fang-2025-evo2hic\|Evo2HiC]]) |

## Boundaries: what makes and breaks them

- **Boundaries are load-bearing, and distance is not the explanation.** CRISPR-engineered mouse alleles reproducing three human limb-malformation rearrangements at the *EPHA4* locus each disrupt a boundary, let an *EPHA4* enhancer cluster capture *PAX3*, *WNT6* or *IHH*, and phenocopy the disease; near-identical deletions that **spare the boundary** give normal limbs, no misexpression and reduced ectopic contact ([[10-Summaries/lupianez-2015-tad-disruption|Lupiáñez 2015]]).
- **Contact is necessary but not sufficient.** Many genes fall inside the new contact domain yet stay silent; promoter receptiveness matters, and the responders are developmental genes ([[10-Summaries/lupianez-2015-tad-disruption|Lupiáñez 2015]]).
- **Boundary identity is combinatorial.** Only 15% of CTCF binding sites lie within boundaries, so boundaries are not CTCF-determined ([[10-Summaries/dixon-2012-tads|Dixon 2012]]).
- **Insulation is not absolute.** The *SHH* ZRS enhancer acts across a boundary when genomic distance is reduced enough, and deleting only the boundary plus its CTCF sites at *Sox9* had no major effect ([[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]).
- **Cohesin separates TADs from compartments.** Cohesin-loading loss erases TADs while *strengthening* compartments ([[10-Summaries/kerpedjiev-2018-higlass|HiGlass]]).
- **Boundaries coincide with other features.** Nearly all kilobase-resolution boundaries coincide with a subcompartment transition or a loop ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).
- **TADs are an interphase-only feature.** Both A/B compartments and sub-megabase TADs collapse in metaphase across HeLa S3, K562 and primary HFF1, giving a homogeneous locus- and cell-type-invariant fold, so boundary function is re-established every cell cycle ([[10-Summaries/naumova-2013-mitotic-chromosome|Naumova 2013]]).
- **Yeast boundaries sit at active promoters.** Boundary nucleosomes are mostly promoter +1 nucleosomes carrying H3K18ac/H3K4me3, high histone turnover, RSC and the cohesin loader Scc2, and strong boundaries lie upstream of more highly transcribed genes ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).

## Evidence and examples

**Bulk maps**

- Micro-C revealed TAD-like chromosomal interaction domains in budding yeast spanning roughly one to five genes (~2–10 kb), bounded mostly at promoter nucleosome-depleted regions of highly transcribed genes ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).
- Domain size appears conserved in gene number rather than base pairs across yeast and mammals ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).
- Within yeast domains, gene compaction is anticorrelated with transcription (r = −0.56) ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).
- The inactive X is split into two "superdomains" whose boundary lies near *DXZ4* ([[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).

**Single cells**

- In single mESCs profiled by scSPRITE, 95% of cells have a positive average TAD detection score across 2,602 ensemble boundary regions, yet most individual TADs are highly variable between cells, and the variable TADs cluster in shared genomic regions ([[10-Summaries/arrastia-2022-scsprite|scSPRITE]]).
- At chr4:38.5–43.6 Mb, a subset of scSPRITE cells forms an alternative TAD spanning an ensemble A/B compartment boundary, which suggests mutually exclusive structural states not explained by cell cycle ([[10-Summaries/arrastia-2022-scsprite|scSPRITE]]).
- In single cells TADs are far less consistently detected than compartments: in scNanoHi-C GM12878 data a TAD was on average detected in ≤60% of cells, and 12% of boundaries (295/2,503) were rarely detected ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).
- CTCF-bound boundaries scored higher in scNanoHi-C, which the authors read as dynamic loop extrusion reinforced by CTCF ([[10-Summaries/li-2023-scnanohi-c|scNanoHi-C]]).
- For GM12878, the median share of aggregated single-cell boundaries within 1 Mb of bulk boundaries was 85.71% (BandNorm), 66.67% (scVI-3D), 60% (Higashi) and 60.87% (scHiCluster) ([[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]).

**Sequence models and tumour predictions**

- Akita, a sequence-only CNN, finds CTCF the dominant motif for TAD-scale folding (CTCFL second), yet 19.9% of high-impact single-nucleotide changes fall outside CTCF, promoter and enhancer annotations ([[10-Summaries/fudenberg-2020-akita|Akita]]).
- Enformer, a sequence-only model, learned to pay less attention across TAD boundaries, a pattern that matches insulation ([[10-Summaries/avsec-2021-enformer|Enformer]]).
- Predicting 4 kb Micro-C from sequence, Evo2HiC beat Orca on distance-stratified Spearman correlation (+10.9%) and insulation-score correlation in H1ESC and HFF, with larger gains at long range ([[10-Summaries/fang-2025-evo2hic|Evo2HiC]]).
- Five 1 Mb recurrently disrupted regions with predicted TAD-boundary or loop loss were found across paediatric tumours; only three were also mutation hotspots, so predicted 3D disruption flagged regions that recurrence counting missed ([[10-Summaries/gjoni-2026-pediatric-tumor-3d|Gjoni 2026]]).

## Contested points

- **TAD calling is threshold-dependent.** Identification "relies heavily on computational methods, which display a high degree of variation depending on the resolution and the adjustment of thresholds," and substantial genome regions have no detectable TADs ([[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]).
- **Callers disagree.** Seven TAD callers on the same matrix produce inconsistent domains of widely varying size ([[10-Summaries/kerpedjiev-2018-higlass|HiGlass]]).
- **TAD size depends on resolution.** ~1 Mb TADs in lower-resolution maps versus a 185 kb median for kilobase-resolution contact domains ([[10-Summaries/dixon-2012-tads|Dixon 2012]]; [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]).
- **Per cell, boundaries are distributions.** Single-cell insulation scores show boundaries that are present/absent across the population *and* boundaries that slide along the genome between cells ([[10-Summaries/zhang-2022-higashi|Higashi]]).
- **What drives folding is open.** The yeast Micro-C authors speculate that boundary establishment, not regular secondary structure, drives chromosome folding ([[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]).
- **Sequence models show correlation, not causal use.** Enformer's reduced attention across TAD boundaries matches insulation but does not show the model uses boundaries causally ([[10-Summaries/avsec-2021-enformer|Enformer]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/chromatin-compartments|Chromatin compartments]] — Megabase-scale A/B segregation of active and inactive chromatin, which behaves differently from TADs.
> - `concept` [[30-Concepts/single-cell-hi-c|Single-cell Hi-C]] — Chromatin contacts measured per cell, where TADs become boundary distributions.
> - `hub` [[40-Topics/3d-genome|3D genome]] — How chromosomes fold in the nucleus, from loops to compartments.

## All sources on this page

> [!info]- 17 summaries cited here
> - [[10-Summaries/arrastia-2022-scsprite|Arrastia 2022]]
> - [[10-Summaries/avsec-2021-enformer|Enformer 2021]]
> - [[10-Summaries/dautle-2025-schic-review|Dautle 2025]]
> - [[10-Summaries/dixon-2012-tads|Dixon 2012]]
> - [[10-Summaries/durand-2016-juicer|Durand 2016]]
> - [[10-Summaries/fang-2025-evo2hic|Evo2HiC 2025]]
> - [[10-Summaries/fudenberg-2020-akita|Akita 2020]]
> - [[10-Summaries/gjoni-2026-pediatric-tumor-3d|Gjoni 2026]]
> - [[10-Summaries/hsieh-2015-micro-c|Hsieh 2015]]
> - [[10-Summaries/kerpedjiev-2018-higlass|Kerpedjiev 2018]]
> - [[10-Summaries/li-2023-scnanohi-c|Li 2023]]
> - [[10-Summaries/lupianez-2015-tad-disruption|Lupiáñez 2015]]
> - [[10-Summaries/naumova-2013-mitotic-chromosome|Naumova 2013]]
> - [[10-Summaries/rao-2014-in-situ-hic|Rao 2014]]
> - [[10-Summaries/spielmann-2018-sv-3d-genome|Spielmann 2018]]
> - [[10-Summaries/zhang-2022-higashi|Zhang 2022]]
> - [[10-Summaries/zheng-2022-bandnorm-scvi-3d|Zheng 2022]]
