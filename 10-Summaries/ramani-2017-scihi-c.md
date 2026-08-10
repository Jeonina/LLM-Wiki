---
type: summary
title: "Ramani et al. 2017 — Massively multiplex single-cell Hi-C (sciHi-C)"
source: "[[00-Sources/papers/Massively multiplex single-cell Hi-C]]"
source_kind: paper
author: "Vijay Ramani, Xinxian Deng, Ruolan Qiu, Kevin L. Gunderson, Frank J. Steemers, Christine M. Disteche, William S. Noble, Zhijun Duan, Jay Shendure (corresponding)"
published: 2017-01-30
ingested: 2026-08-10
doi: "10.1038/nmeth.4155"
journal: "Nature Methods"
tags: [sciHi-C, combinatorial-indexing, single-cell-Hi-C, cell-cycle, in-silico-sorting, translocations, throughput]
entities: ["[[jay-shendure]]", "[[vijay-ramani]]"]
concepts: ["[[single-cell-hi-c]]", "[[combinatorial-indexing]]", "[[chromatin-compartments]]", "[[structural-variants]]", "[[scatac-seq]]"]
topics: ["[[3d-genome]]", "[[chromatin-architecture]]"]
---

**Citation:** Ramani et al. (2017) — *Massively multiplex single-cell Hi-C* — *Nature Methods* 14, 263–266. [DOI](https://doi.org/10.1038/nmeth.4155)

# Ramani 2017 — sciHi-C

> Combinatorial indexing applied to chromosome conformation. Barcode intact nuclei twice — once by bridge-adaptor ligation before proximity ligation, once by Y-adaptor ligation after — and 96 × 96 barcode combinations tag far more nuclei than the ≤25-per-well dilution allows, so most cells get a unique index **without ever physically isolating a cell**. 10,696 single-cell contact maps in one workflow, two orders of magnitude beyond the prior state of the art.

## Key claims

- **The protocol.** 5–10 M cells fixed, lysed to nuclei, DpnII-digested *in situ*; distributed to 96 wells for barcoded biotinylated bridge-adaptor ligation; **pooled and proximity-ligated together**; diluted to a second 96-well plate at **≤25 nuclei per well**; lysed and given a second barcode by Y-adaptor ligation. 2 × 250 bp reads recover genomic sequence plus both barcodes.
- Nuclei stay intact through proximity ligation — confirmed by phase-contrast microscopy and by **0.006–0.008% mouse–human contacts** in species-mixing experiments, i.e. essentially no crosstalk between cellular indices.
- Quality on par with bulk Hi-C: *cis*:*trans* ratio 4.41 and 4.38 in the two replicate libraries; per-cell medians 4.43 and 4.34.
- Yield: 1,081 and 841 cellular indices at ~8,300–9,300 unique read pairs each in the primary libraries; **8,141 single-cell maps** across four experiments after filtering; **10,696 cells with ≥1,000 unique contacts** overall, of which 3,515 exceed 10,000 contacts — against **ten** cells in the only prior single-cell Hi-C study.
- Collision rate 4.53%/4.40%, matching the birthday-problem expectation; the authors note explicitly that **within-species collisions remain invisible** and likely occur at a similar rate.
- **Cell types separate on contact structure alone.** PCA on chromosome-pair contact matrices separates HeLa S3 from HAP1; the PC2 loadings recover **known HAP1 translocations (15–19, 9–22) and documented HeLa translocations** — the separation is driven by real karyotypic differences, not batch.
- **Per-cell conformational heterogeneity is real**: contact-probability-versus-distance curves for 769 cells are markedly more disperse than shuffled controls, and per-cell power-law scaling coefficients (50 kb–8 Mb) correlate with *cis*:*trans* ratio.
- **In-silico cell-cycle sorting.** Nocodazole-arrested HeLa gives a clearly **bimodal** distribution of scaling coefficients; splitting on it yields two contact maps — one with the interphase plaid compartment pattern, one with the condensed, compartment-free mitotic pattern described by [[naumova-2013-mitotic-chromosome|Naumova]]. No genotype filtering was needed for this separation.

## Methods / evidence

Species-mixing with programmed barcode associations (specific cell types receive specific first-round barcodes) so the single-cell origin of each index is independently checkable; replicate libraries; a HeLa-genotype filter removing 20.4% of human indices as an extra conservative step; and the nocodazole experiment as a positive control for the scaling-coefficient readout.

The authors are careful about what the filters cannot do — within-species collisions are acknowledged as unmeasurable, and they publish per-barcode species purity and restriction-fragment copy counts so users can apply stricter filters for structural modelling.

## Surprising or load-bearing bits

- **Cell-cycle state is the dominant axis of variation in single-cell Hi-C, and it is measurable from the data itself.** A single scalar — the *P(s)* scaling coefficient — separates mitotic from interphase cells with no marker, no sorting and no genotype. Every single-cell Hi-C dataset from proliferating tissue contains this mixture, and this is the tool for handling it. It also operationalizes [[naumova-2013-mitotic-chromosome|Naumova's]] two-folding-state result at the level of individual cells.
- **Translocations are recoverable from single-cell contact structure**, which the authors flag as valuable for "tissue containing a mixture of normal cells and cancerous cells harboring translocations" — a somatic-SV readout from conformation rather than sequence. Relevant to [[cancer-clonal-evolution]] and to the balanced-SV blind spot in [[eichler-2007-completing-sv-map]].
- **The throughput jump is architectural, not incremental.** [[nagano-2013-nature|Nagano 2013]] processed physically isolated nuclei one at a time; combinatorial indexing removes isolation entirely, which is why sciHi-C reaches thousands. Same conceptual move as [[cusanovich-2015-sciatac|sciATAC-seq]] from the same lab.
- The trade is depth: **~8,000–9,000 contacts per cell**. Against the *n*²-resolution rule from [[lieberman-aiden-2009-hic|Hi-C]], that is a very coarse per-cell map — which is precisely why imputation methods ([[zhou-2019-schicluster|scHiCluster]], [[zhang-2022-higashi|Higashi]]) exist.
- Coverage per index is **bimodal**, with the low mode representing barcoded free DNA rather than intact nuclei — the same artefact structure as sciATAC, and a reminder that "cellular index" ≠ "cell" without filtering.
- HAP1 turned out to be ~40% diploid by FACS despite being an engineered haploid line — reported candidly as a caveat on the copy-number-based filters.

## Entities mentioned

- [[jay-shendure]] — corresponding author; combinatorial indexing program.
- [[vijay-ramani]] — first author.

## Concepts touched

- [[single-cell-hi-c]] — the high-throughput branch; contrast with physical-isolation methods.
- [[combinatorial-indexing]] — demonstrated as generalizable beyond accessibility to conformation.
- [[chromatin-compartments]] — compartment presence/absence is the mitotic-vs-interphase discriminator.

## Connections to other sources

- Scales [[nagano-2013-nature]]; shares the indexing strategy with [[cusanovich-2015-sciatac]].
- Operationalizes [[naumova-2013-mitotic-chromosome]] per cell; assay substrate from [[lieberman-aiden-2009-hic]].
- Downstream sparsity handled by [[zhou-2019-schicluster]] and [[zhang-2022-higashi]]; storage and pipelines via [[abdennur-2020-cooler|Cooler]] and [[servant-2015-hicpro|HiC-Pro]] (used here for DpnII site definition).
- Higher-coverage alternatives: [[tan-2018-science|Dip-C]], [[lee-2019-natmethods|sn-m3C-seq]].

## Open questions

- **Within-species barcode collisions are acknowledged as invisible** and estimated to occur at roughly the interspecies rate (~4.5%). No dataset in this corpus corrects for them.
- Whether ~8,000 contacts per cell suffices for any structural claim beyond compartment-scale and cell-cycle state — the authors defer to users to apply stricter filters for modelling.
- The correlation between *cis*:*trans* ratio and scaling coefficient held in four of five experiments; the exception is unexplained.

## Related

- [[nagano-2013-nature]] · [[combinatorial-indexing]] · [[naumova-2013-mitotic-chromosome]] · [[3d-genome]]
