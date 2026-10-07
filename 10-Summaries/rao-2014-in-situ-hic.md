---
type: summary
title: "Rao et al. 2014 — A 3D Map of the Human Genome at Kilobase Resolution Reveals Principles of Chromatin Looping"
source: "[[00-Sources/papers/A 3D Map of the Human Genome at Kilobase Resolution Reveals Principles of Chromatin Looping]]"
source_quality: full
source_sha256: "b8f30e3d6bae534c48925d9cfdcb24c004680b0d0d130260bcb82c5dc78e7bed"
source_kind: paper
author: "Suhas S. P. Rao, Miriam H. Huntley, Neva C. Durand, Elena K. Stamenova, Ivan D. Bochkov, James T. Robinson, Adrian L. Sanborn, Ido Machol, Arina D. Omer, Eric S. Lander, Erez Lieberman Aiden (corresponding)"
published: 2014-12
ingested: 2026-10-07
doi: "10.1016/j.cell.2014.11.021"
journal: "Cell 159(7):1665–1680"
tags: [in-situ-Hi-C, Hi-C, chromatin-loops, HiCCUPS, Arrowhead, APA, contact-domains, subcompartments, CTCF, cohesin, convergent-CTCF, diploid-Hi-C, inactive-X, Juicebox, founding-paper]
entities: []
concepts: ["[[chromatin-loop]]", "[[topologically-associating-domain]]", "[[chromatin-compartments]]", "[[hi-c-normalization]]", "[[nuclear-lamina]]", "[[replication-timing]]", "[[chia-pet]]", "[[single-cell-hi-c]]", "[[transposable-elements]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Rao et al. (2014) — *A 3D Map of the Human Genome at Kilobase Resolution Reveals Principles of Chromatin Looping* — *Cell* 159:1665–1680. [DOI](https://doi.org/10.1016/j.cell.2014.11.021)

# Rao 2014 — in situ Hi-C at kilobase resolution

> Moving the ligation step **inside intact nuclei** (in situ Hi-C) and sequencing ~5 Tb produced Hi-C maps dense enough to see individual loops. The headline is not the resolution but what it revealed: **~10,000 loops in GM12878, anchored overwhelmingly at CTCF/cohesin sites whose motifs point toward each other (>90% convergent vs 25% expected)**; contact domains far smaller (median 185 kb) than the ~1 Mb TADs; and at least six subcompartments beneath A/B. It also introduced the tooling (HiCCUPS, Arrowhead, APA, Juicebox) that became the default bulk Hi-C vocabulary.

## Key claims

- **In situ beats dilution at high resolution.** Ligation in nuclei lowers spurious (random-ligation) contacts — fewer mitochondrial–nuclear junctions — runs in 3 days instead of 7, and uses a 4-cutter (MboI). At coarse scales it agrees with dilution Hi-C (GM12878 R > 0.96, 0.90, 0.87 at 500, 50, 25 kb).
- **Scale of data**: nine cell lines (human GM12878, IMR90, HMEC, NHEK, K562, HUVEC, HeLa, KBM7; mouse CH12-LX), >15 billion distinct contacts. GM12878 has 4.9 billion contacts and a **map resolution of 950 bp** (defined as the smallest bin at which 80% of loci have ≥1,000 contacts); the other eight maps have 395 M–1.1 B contacts at 5 kb. 201 Hi-C experiments in total, including no-crosslink controls.
- **Contact domains**: Arrowhead calls domains of 40 kb–3 Mb (median **185 kb**), with a 33% contact drop across boundaries; loci within a domain share histone marks (8 ENCODE marks), and when a domain's chromatin state changes, its long-range contact pattern changes too.
- **Subcompartments**: clustering 100 kb interchromosomal contact patterns gives five genome-wide (A1, A2, B1, B2, B3) plus B4 found only by clustering chr19 alone (11 Mb, 0.3% of the genome; 130 of 278 KRAB-ZNF genes). A1/A2 are gene-dense, active and early-replicating; B1 tracks H3K27me3 (facultative heterochromatin); B2 holds 62% of pericentromeric heterochromatin and is NAD-enriched (4.6×); B3 is lamina-enriched (1.6×) but NAD-depleted (76×).
- **Loops**: HiCCUPS finds **9,448 peaks** in GM12878 at 5 kb (12,903 peak loci); 98% span <2 Mb. Replicates give 8,054 and 7,484 peaks with 5,403 shared; 65% of 3,073 peaks from the sparser dilution map recur in situ. 3D-FISH on four loops confirmed anchors are closer than equidistant controls. 55–75% of a given cell line's peaks are also found in GM12878; 50% of mouse peaks and 45% of mouse domains are conserved in orthologous human regions.
- **Loops and genes**: 2,854/9,448 peaks join a promoter and an enhancer (30% vs 7% expected); loop-associated promoters are 6-fold more highly expressed; 557 GM12878-only loops overlap promoters of 43 genes >50-fold up in GM12878 versus one gene up in IMR90 (reciprocal: 510 loops, 94 vs 3 genes).
- **Loops and domains**: 38% of peaks sit at domain corners and 39% of domains have a corner peak ("loop domains"); overlapping loops occur 4-fold less than expected under a random model.
- **CTCF convergence**: 86% of peak loci bind CTCF, 86% RAD21, 87% SMC3 (from 86 ENCODE ChIP-seq experiments). Of 4,322 peaks with a single CTCF motif at each anchor, **92% are convergent**; convergent vs divergent counts are 3,971 vs 78 in GM12878 and similarly lopsided in all eight lines (51–362-fold); p < 10⁻¹⁹⁰⁰. In mouse, 7% of anchors lie in CTCF-containing SINEB2 elements, which show the same orientation bias.
- **Diploid maps**: SNP phasing gives maternal (238 M) and paternal (240 M) GM12878 maps. Autosomal homologs correlate at R > 0.998; Hi-C detected a paternal der(6)t(6;11) translocation predicted in 1.2–5.6% of cells and confirmed in 3 of 100 karyotyped cells. *H19/Igf2* shows parent-of-origin-specific loops. The inactive X splits into two **superdomains** (boundary near *DXZ4*) and carries 27 **superloops** (7–74 Mb), with anchors at lncRNA loci *loc550643*, *XIST*, *DXZ4* and *FIRRE*.

## Methods / evidence

In situ Hi-C (1% formaldehyde, MboI digestion, biotin fill-in, in-nucleus ligation, streptavidin pull-down); BWA mapping to b37/mm9; matrix balancing for normalization; Arrowhead transform for domains; HiCCUPS (local-background enrichment against four neighbourhoods — donut, lower-left, horizontal, vertical — with ≥50% excess and FDR < 10%, GPU-accelerated 200-fold); APA to test a loop list against sparse maps in aggregate; Juicebox for visualization. Orthogonal validation by 3D-FISH, karyotyping, ENCODE ChIP-seq and RNA-seq, and concordance with three ENCODE ChIA-PET experiments.

Weight: very strong — a reference dataset with replicates, no-crosslink controls and multiple orthogonal validations. The CTCF-orientation statistic is itself a validation of the loop calls, since random calls could not produce it. The loop count is explicitly conservative.

## Surprising or load-bearing bits

- **Local vs global background is the whole loop-count dispute.** Rao call far fewer loops than contemporaneous studies despite more data, because a pixel must beat its *neighbourhood*, not the genome-wide average; the paper argues that reports implying >100,000 or >1 million loops mostly capture same-domain/same-compartment pairs and show no APA enrichment.
- **Convergent orientation over ~360 kb** is the clue that later underpinned loop extrusion; here it is presented as implying a CTCF-dimerization mechanism, and engineering loops by flipping motifs is proposed as a test. (The extrusion interpretation is later literature, not this paper.) (synthesis)
- **Domain size depends on resolution**: the 185 kb contact domains versus ~1 Mb TADs is attributed to detecting more boundaries at higher resolution; nearly all boundaries coincide with a subcompartment transition (~every 300 kb) or a loop (~every 200 kb).
- **Hi-C as a cytogenetic tool**: detecting a translocation present in a few percent of cells and phasing it to the paternal homolog is an early hint that contact maps carry structural-variant and mosaicism information. (synthesis)
- The kilobase resolution needed **4.9 billion contacts from millions of cells**; this is the depth that single-cell Hi-C will never match per cell, which is why scHi-C loop callers pool or impute. (synthesis)

## Entities mentioned

- Erez Lieberman Aiden (corresponding) and Eric S. Lander — no entity pages yet.

## Concepts touched

- [[chromatin-loop]] — the canonical loop catalogue, HiCCUPS definition and convergent-CTCF rule.
- [[topologically-associating-domain]] — contact domains (median 185 kb) and "loop domains" refine the ~1 Mb TAD.
- [[chromatin-compartments]] — A/B subdivided into six subcompartments with distinct marks, replication timing and lamina/NAD association.
- [[hi-c-normalization]] — matrix balancing for coverage non-uniformity.
- [[chia-pet]] — concordance with ENCODE CTCF/RAD21 ChIA-PET.
- [[nuclear-lamina]] / [[replication-timing]] — subcompartment annotations.
- [[transposable-elements]] — SINEB2 exaptation of CTCF sites in mouse.

## Connections to other sources

- Extends [[lieberman-aiden-2009-hic]] (1 Mb maps, A/B compartments, same lab) to kilobase resolution.
- Revises the domain scale of [[dixon-2012-tads]] (TADs ~1 Mb) to median 185 kb contact domains.
- Its algorithms are packaged in [[durand-2016-juicer]] (HiCCUPS, Arrowhead, APA); storage/visualization alternatives in [[abdennur-2020-cooler]] and [[kerpedjiev-2018-higlass]].
- Promoter–enhancer loops echo the CTCF/Pol II ChIA-PET picture in [[li-2014-chia-pet]].
- The in-nucleus ligation it adopts parallels single-cell Hi-C ([[nagano-2013-nature]]); single-cell loop calling that inherits its HiCCUPS neighbourhood logic and convergent-CTCF validation: [[yu-2021-snaphic]]. Single-cell maps that test whether domains exist per cell: [[tan-2018-science]], [[zhou-2019-schicluster]], [[zhang-2022-higashi]].

## Open questions

- Mechanism of convergent-CTCF looping is left open (dimerization proposed); the physical-folding analysis is deferred to future work.
- Whether ~10,000 loops is complete or a sensitivity floor: cell lines with fewer contacts call only 2,634–8,040 peaks, so loop counts scale with depth.
- Whether loops and domains are present in every cell or are population averages cannot be resolved by ensemble Hi-C. (synthesis)

## Related

- [[chromatin-loop]] · [[topologically-associating-domain]] · [[chromatin-compartments]] · [[durand-2016-juicer]] · [[40-Topics/3d-genome]]
