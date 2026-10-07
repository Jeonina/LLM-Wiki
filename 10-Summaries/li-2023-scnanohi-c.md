---
type: summary
title: "Li et al. 2023 — scNanoHi-C: a single-cell long-read concatemer sequencing method to reveal high-order chromatin structures within individual cells"
source: "[[00-Sources/papers/scNanoHi-C_ a single-cell long-read concatemer sequencing method to reveal high-order chromatin structures within individual cells]]"
source_kind: paper
author: "Wen Li, Jiansen Lu, Ping Lu, Yun Gao, Yichen Bai, Kexuan Chen, Xinjie Su, Mengyao Li, Jun'e Liu, Yijun Chen, Lu Wen, Fuchou Tang (corresponding)"
published: 2023-08-28
ingested: 2026-10-07
doi: "10.1038/s41592-023-01978-w"
journal: "Nature Methods 20:1493–1505"
tags: [scNanoHi-C, single-cell-Hi-C, Oxford-Nanopore, concatemer, multi-way-contacts, Pore-C, enhancer-promoter, ecDNA, COLO320DM, haplotype-resolved-3D, CNV, SV, SALSA2, scaffolding, scSPRITE-comparison]
entities: ["[[20-Entities/fuchou-tang]]"]
concepts: ["[[single-cell-hi-c]]", "[[multi-way-chromatin-interaction]]", "[[oxford-nanopore]]", "[[sc-sprite]]", "[[dip-c]]", "[[chromatin-compartments]]", "[[topologically-associating-domain]]", "[[chromatin-loop]]", "[[copy-number-variation]]", "[[structural-variants]]", "[[single-cell-genome-assembly]]", "[[malbac]]", "[[tn5-tagmentation]]"]
topics: ["[[3d-genome]]", "[[long-read-sequencing]]", "[[chromatin-architecture]]"]
---

**Citation:** Li et al. (2023) — *scNanoHi-C: a single-cell long-read concatemer sequencing method to reveal high-order chromatin structures within individual cells* — *Nature Methods* 20:1493–1505. [DOI](https://doi.org/10.1038/s41592-023-01978-w)

# Li 2023 — scNanoHi-C

> Short-read single-cell Hi-C sees each ligation junction as a pair; a Nanopore read sees the whole **concatemer** — every fragment ligated together in one proximity cluster. scNanoHi-C is plate-based single-cell Hi-C (FA + DSG crosslink, MboI, ligation, FACS into 96-well plates, 24 barcoded Tn5s, ~3-kb amplicons) read on PromethION, so that **about half of all concatemers are high-order (cardinality ≥3)**. Because it stays ligation-based, its multi-way contacts keep the ~200-nm contact radius of 3C methods — the authors position it against [[sc-sprite|scSPRITE]] as the tool for *direct* cis-regulatory hubs (enhancer–promoter cliques, ecDNA hubs) rather than large indirect nuclear-body clusters. Long monomers (610 bp mean) also double the phasable fraction relative to Dip-C, and the same data yield CNVs, SVs and assembly scaffolds.

## Key claims

- **Scalable by design**: 24 Tn5 barcodes × 96 PCR barcodes, so one PromethION run can hold a few cells to "several thousands of cells (up to 24 × 96)". Three GM12878 depth strategies — ~24, ~100 and ~500 cells per run — gave median **464,844 / 158,590 / 58,871 contacts per cell** from 4 / 0.8 / 0.2 Gb per cell. Duplicate-contact ratios were 70.5% / 55.6% / 30.3% (high / medium / low depth), so shallow sequencing of more cells yields more effective contacts per base.
- **Low cross-contamination**: in human HG002 + mESC species mixing, collision rates were 4.2% (crosslinking) and 1.0% (amplification), with collisions defined as <95% of monomers mapping to one species.
- **Coverage**: high-depth cells covered ~99.3% of 100-kb bin pairs; even low-depth cells covered 99.1% of 1-Mb bins.
- **Fidelity to bulk Hi-C** (merged high/medium-depth vs bulk in situ GM12878 Hi-C): raw 1-Mb contacts r = 0.96/0.96; compartment score r = 0.85/0.93; 50-kb insulation score r = 0.78/0.88. *Trans* ratio was comparable to previous scHi-C.
- **High-order fraction**: about half of concatemers were high-order; among them ~58% triplets, ~26% quadruplets, the rest cardinality 5–11.
- **Versus scSPRITE** (mESC, 576 cells / 380.7 Gb vs top 1,000 scSPRITE cells / 380.9 Gb): ~70% of effective scSPRITE reads sit in clusters of cardinality >10, negligible in scNanoHi-C; scSPRITE high-cardinality clusters decay more slowly with distance than bulk Hi-C, and its *trans* ratio is 54% vs 11%. The authors read this as scSPRITE capturing mainly indirect/trans interactions plausibly mediated by subnuclear compartments, while scNanoHi-C's pairwise and high-order contacts share the 3C contact radius.
- **Single-cell structure detection** (normalized detection score, method borrowed from scSPRITE): all cells separated chromosome territories; 87.0% (548/630) of A-B-A / B-A-B compartment triplets were detectable in single cells. TADs were much weaker: on average a TAD was detected in ≤60% of cells, and 12% of boundaries (295/2,503) were rarely detected. Boundary nDS correlated with merged-data boundary strength and was higher at CTCF-bound boundaries — read as dynamic loop extrusion reinforced by CTCF.
- **Loops**: SnapHiC at 10 kb gave performance "comparable" to previous scHi-C; loop clusters around *MIR155HG*/*RUNX3* super-enhancers (GM12878) and *Sox2*/*Nanog* (mESC) were recovered.
- **Phasing and 3D models**: mean monomer length 610 bp vs ≤150 bp for short-read scHi-C; directly phasable monomers **25% vs 9% in Dip-C**. Haplotype-resolved 20-kb models (hickit + Dip-C) reproduced territories, compartments, inverse scA/B–radial position relationship, and X inactivation (active maternal X with higher scA/B and more extended structure).
- **Cell typing**: 696 cells (464 GM12878, 71 HG002, 161 K562) clustered cleanly by UMAP on scA/B values, even separating the two LCLs. Differentially compartmentalized windows between K562 and GM12878 were consistent with RNA expression and enriched for K562 super-enhancers.
- **CNV/SV from contacts**: 93/262 GM12878 cells (>100,000 contacts) carried CNVs, mostly chr1 or chr16, matched by MALBAC scWGS (35% vs 38% of cells with clear CNV signatures). Merged scNanoHi-C (88 K562 cells) correlated with ~60× bulk WGS CNV better than bulk Hi-C did; BCR–ABL1 and NUP214–XKR3 fusions were detected in merged K562 data (hic_breakfinder). Copy-number gains appeared as more "compacted" structures in models.
- **Multi-way enhancer–promoter structures**: using ABC-model E–P pairs, 1,097 promoter bins contacted ≥2 enhancer bins in single high-order concatemers (genes more highly expressed, GO-enriched for B-cell function, incl. *EBF1*, *MIR155HG*, *IKZF3*, *ETS1*); 1,422 enhancer bins contacted ≥2 promoter bins. Only ~30% of multiway E–P interactions were seen in >3 cells.
- **Synergies** (Pore-C Synergy/Chromunity models adapted): 917 E–P synergies in GM12878, ~20% (187) inter-chromosomal, 167 overlapping GM12878 super-enhancers; examples include two super-enhancers downstream of *PAX5* and a *MIR155HG* super-enhancer interacting with a locus 4 Mb away.
- **ecDNA hubs**: in COLO320DM (MYC-amplified ecDNA), copy-number-adjusted nTIF peaks on Chr6, Chr8, Chr13 and Chr16 in merged and single-cell data; single concatemers linking the four ecDNA loci were captured — "direct evidence" of multiway ecDNA interactions — and 56 ecDNA-associated synergies were called.
- **Assembly scaffolding**: SALSA2 scaffolding of prior HG002 single-cell draft assemblies with 12/24/48 scNanoHi-C cells improved contiguity; 20 scWGS cells + 12 scNanoHi-C cells beat 30 scWGS cells (NG50 2.49 vs 1.34 Mb).
- **Cost**: ~USD 3 per cell at ~500 cells per PromethION run.

## Methods / evidence

Cell lines only: GM12878, HG002, K562, COLO320DM, mESC (V6.5, F15). Snakemake pipeline: Nanoplexer demultiplexing → Cutadapt → Pore-C Snakemake (bwasw alignment, whatshap haplotype tagging, restriction-fragment assignment) → scHi-C artifact filtering (adjacent, close, duplicate, promiscuous, isolated contacts) → virtual pairwise contacts. QC: >10,000 contacts and *trans* ratio <30%. Downstream: SnapHiC (loops), hickit + Dip-C (3D models, scA/B), NeoLoopFinder calculate-cnv + DNAcopy CBS (CNV), hic_breakfinder (SV), SALSA2/QUAST/BUSCO (scaffolding), ABC-model E–P sets, Synergy/Chromunity (cooperativity). Validation by bulk in situ Hi-C, MALBAC scWGS, bulk WGS, metaphase DNA FISH (MYC). Data: GEO GSE217189.

Weight: strong as a methods paper — orthogonal validation for CNVs (MALBAC) and ecDNA (FISH), a same-data-volume head-to-head with scSPRITE. Biological claims about multiway E–P hubs are correlational: detection rates per structure are low, and the high-order ratio is partly driven by technical factors (negatively correlated with monomer length; enrichment in open chromatin attributed partly to restriction-enzyme cutting efficiency). No tissue data. The authors (F.T., W.L., J. Lu) hold a patent on the method.

## Surprising or load-bearing bits

- **"High-order" is not one thing.** Same sequencing volume, similar overall cardinality distributions, yet scSPRITE puts ~70% of reads into >10-way clusters with a 54% trans ratio, while scNanoHi-C's multi-way contacts decay like pairwise Hi-C. Ligation-based and ligation-free multi-way assays sample different physical scales — direct contact vs shared nuclear neighbourhood — and should not be pooled as "multi-way data" without saying which. (synthesis)
- **TADs are population averages, compartments are not.** 87% of compartment triplets are visible per cell, but an average TAD shows up in ≤60% of cells and 12% of boundaries almost never — consistent with the loop-extrusion view that single-cell TAD-like domains are transient.
- **Merged single-cell Hi-C beat bulk Hi-C at CNV calling** (lower CV in GM12878; better K562 correlation with WGS) — the authors attribute this to their contact filtering. A 3D-genome assay doubling as a CNV assay is relevant to anyone using scHi-C on aneuploid tumours. (synthesis)
- **Read length buys phasing**: 25% vs 9% directly phased monomers is the practical route to haplotype-resolved single-cell 3D models without deep sequencing.
- **Duplication dominates at depth**: 70.5% duplicate contacts at high depth — library complexity, not sequencing, caps per-cell resolution.

## Concepts touched

- [[single-cell-hi-c]] — long-read, plate-based member of the family; concatemers rather than pairs.
- [[multi-way-chromatin-interaction]] — direct, ligation-based multi-way contacts in single cells; E–P hubs and ecDNA hubs.
- [[sc-sprite]] — explicit comparison: scSPRITE dominated by >10-way, trans-rich clusters.
- [[dip-c]] — phasing comparison (25% vs 9%) and reuse of Dip-C/hickit model reconstruction.
- [[oxford-nanopore]] — PromethION R9.4.1 enables concatemer reads.
- [[chromatin-compartments]], [[topologically-associating-domain]], [[chromatin-loop]] — single-cell detectability gradient (territories > compartments > TADs).
- [[copy-number-variation]], [[structural-variants]] — CNV/SV calling from contact maps, validated against MALBAC and WGS.
- [[single-cell-genome-assembly]] — Hi-C-style scaffolding of single-cell assemblies.
- [[malbac]] — orthogonal scWGS validation of CNVs.
- [[tn5-tagmentation]] — 24 barcoded low-density Tn5s for per-cell indexing.

## Connections to other sources

- Single-cell Hi-C lineage it extends: [[nagano-2013-nature]], [[tan-2018-science]] (Dip-C; phasing and modelling comparator), [[ramani-2017-scihi-c]].
- Loop calling via [[yu-2021-snaphic]]; bulk Hi-C foundations [[lieberman-aiden-2009-hic]], [[dixon-2012-tads]].
- Multi-way analysis downstream: [[park-2026-mintsc]] uses scNanoHi-C concatemer counts to validate cliques and derives its 200-kb clique-distance constraint from scNanoHi-C support.
- Benchmark/framework context: [[jiang-2026-stark-scnucleome]] (processes scNanoHi-C but does not deeply benchmark it), [[hong-2025-sc3d-genome-review]] — that summary marks the "first long-read single-cell Hi-C" framing as unverified; this source states it detects proximal high-order interactions in single cells "for the first time".
- SVs and 3D genome: [[spielmann-2018-sv-3d-genome]]. Long-read epigenome context: [[liu-2025-long-read-epigenome-review]] (Pore-C family).
- MALBAC validation chemistry: [[zong-2017-malbac-protocol]].

## Open questions

- How much of the "high-order" signal reflects restriction-cutting and monomer-length biases rather than biology? The partial correlations suggest a substantial technical component.
- Multiway E–P structures are each seen in few cells (~30% in >3 cells); whether rare hubs are real transient states or noise needs perturbation, not more sequencing.
- No tissue application — whether the ~50% high-order rate and low collision rate hold in primary nuclei is untested here.
- Conflict to resolve against the scSPRITE paper's own framing: the [[sc-sprite]] concept page says scSPRITE captures more contacts per cell than any ligation method; this paper argues most of those contacts are indirect. Both may be true. (synthesis)

## Related

- [[single-cell-hi-c]] · [[multi-way-chromatin-interaction]] · [[sc-sprite]] · [[40-Topics/3d-genome]] · [[40-Topics/long-read-sequencing]]
