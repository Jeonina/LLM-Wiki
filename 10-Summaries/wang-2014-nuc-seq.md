---
type: summary
title: "Wang et al. 2014 — Clonal evolution in breast cancer revealed by single nucleus genome sequencing (nuc-seq)"
source: "[[00-Sources/papers/Clonal evolution in breast cancer revealed by single nucleus genome sequencing]]"
source_kind: paper
author: "Yong Wang, Jill Waters, Marco L. Leung, Anna Unruh, Whijae Roh, Xiuqing Shi, Ken Chen, Paul Scheet, Selina Vattathil, Han Liang, Asha Multani, Hong Zhang, Rui Zhao, Franziska Michor, Funda Meric-Bernstam, Nicholas E. Navin (corresponding)"
published: 2014-07-30
ingested: 2026-08-13
doi: "10.1038/nature13600"
journal: "Nature 512:155–160"
tags: [nuc-seq, G2/M-nuclei, breast-cancer, clonal-evolution, punctuated-evolution, duplex-sequencing, mutation-rate, MDA]
entities: ["[[nicholas-navin]]", "[[ken-chen]]"]
concepts: ["[[scwga]]", "[[mda]]", "[[allele-dropout]]", "[[copy-number-variation]]", "[[intratumor-heterogeneity]]", "[[tn5-tagmentation]]", "[[sscce]]"]
topics: ["[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]", "[[whole-genome-amplification]]", "[[duplex-sequencing]]"]
---

**Citation:** Wang et al. (2014) — *Clonal evolution in breast cancer revealed by single nucleus genome sequencing* — *Nature* 512, 155–160. [DOI](https://doi.org/10.1038/nature13600)

# Wang 2014 — nuc-seq

> Exploit the cell cycle instead of fighting it: flow-sort **G2/M nuclei**, which have already doubled their DNA from 6 pg to 12 pg, so [[mda|MDA]] starts from four copies of each locus rather than one. That single trick takes coverage breadth from ~10% (sparse [[dop-pcr|DOP-PCR]]) to **91%** and allele dropout to **9.7%**. Applied to an ER⁺ and a triple-negative breast cancer, it yields the paper's real claim: **aneuploid rearrangements arise early and then freeze; point mutations keep accumulating gradually** — two clocks running at different speeds in the same tumour.

## Key claims

- **The cell cycle is the amplification trick.** Cells in G2/M carry 12 pg of DNA instead of 6 pg, giving ≥4 copies of each genomic locus as MDA input. More starting template means less stochastic dropout and less error amplification. Critically, this works on *fixed/frozen* nuclei — unlike chemical polyploidy induction, which needs live cells.
- **MDA is deliberately time-limited to 80 minutes** to reduce φ29 infidelity artifacts. Amplification quality is checked with 22 chromosome-specific primer pairs: 45.3% of G2/M cells (39/86) show full chromosome amplification versus 25.6% (11/43) of G1/G0 cells.
- **Validation on monoclonal SK-BR-3**: coverage depth 61×, breadth 83.7%, ADR 9.73 ± 2.19% (versus 7–46% in prior work), FPR 1.24 × 10⁻⁶ — one to two errors per million bases, roughly **20–30× better than MDA and [[malbac|MALBAC]]** (2.52 × 10⁻⁵ and 4 × 10⁻⁵).
- **Aneuploid CNAs are early and stable.** 50 single nuclei per tumour profiled by [[navin-2011-sns-tumor-evolution|SNS]]: the ER⁺ tumour is copy-number monoclonal (mean R² = 0.89); the TNBC splits into two subpopulations (A and H, mean R² = 0.91 and 0.88) distinguished by two large deletions. Within each subpopulation the rearrangements are near-identical — they were acquired once and then propagated.
- **Point mutations are gradual and generate extensive diversity.** Single-nucleus exome sequencing found 22 new subclonal mutations in the ER⁺ tumour beyond the 17 clonal ones, and **145 subclonal non-synonymous mutations in the TNBC** beyond the 374 clonal ones, splitting the TNBC into A1 (66 unique) and A2 (52 unique) subclones.
- **Targeted duplex sequencing confirms the rare mutations are real.** Using [[schmitt-2012-pnas|Duplex Sequencing]] at ~117,000× raw / ~5,700–6,600× single-molecule depth, the ERBC validated 94.4% of clonal, 90.5% of subclonal, and **19.4% of *de novo* (single-cell-only) mutations**; the TNBC validated 99.7%, 64.8%, and 27.0% respectively. Clonal mutations sit at high frequency (0.45 mean in TNBC), subclonal at ~0.05, *de novo* at 0.0005.
- **The TNBC has a 13.3× elevated mutation rate; the ER⁺ tumour does not.** A stochastic birth–death model parameterised with Ki-67 (birth), caspase-3 (death), flow-sorted cell counts, and a 168-day doubling time yields M_R = 0.6–0.9 mutations/division for the ERBC — indistinguishable from normal cells (~0.6) — versus M_R = 8 for the TNBC.

## Methods / evidence

Two patients plus a monoclonal cell line control. Per tumour: bulk WGS of sorted aneuploid nuclei and matched normal (46–74×), 50 single nuclei for [[copy-number-variation|CNA]] profiling by SNS, 4 nuclei for single-cell WGS, and 47–59 nuclei for single-cell exome. Orthogonal validation by spectral karyotyping and duplex sequencing. Mutation rates from a parameterised mathematical model rather than direct measurement.

Weight: n = 2 patients. The mutation-rate contrast (13.3× vs 1×) rests on one tumour of each subtype, and the model's doubling-time parameter is a literature mean, not a per-patient measurement. The *method* validation (SK-BR-3) is far stronger than the *biology* claim.

## Surprising or load-bearing bits

- **"No two single tumour cells are genetically identical."** With 91% breadth you can finally ask the question, and the answer dissolves the strict definition of a clone. Clonality survives at the copy-number level and fails at the point-mutation level — in the *same cells*.
- **Two clocks, one tumour.** The punctuated-CNA / gradual-SNV split is the paper's durable contribution and is only visible because both layers were measured per cell. It is the copy-number analogue of the decoupling [[hou-2016-sctrio-seq|scTrio-seq]] later found between CNV and methylation.
- **19–27% of single-cell-only mutations validate by duplex.** Read the other way: **73–81% do not** — the *de novo* class is majority artifact even in a high-quality library. This is the most honest number in the paper and the reason single-cell-only calls need orthogonal confirmation, an argument that runs straight through to [[luquette-2025-pta-duplex-mosaicism]] eleven years later.
- **Duplex sequencing as the arbiter of single-cell calls appears here in 2014** — the pairing that the wiki treats as a 2025 frontier ([[50-Notes/single-cell-duplex-sequencing]]) was prototyped in this paper as targeted validation.
- **Tn5 tagmentation is applied post-MDA** to fragment and adapter-ligate in one step, which is why the protocol scales to exome capture across 59 nuclei.

## Entities mentioned

- [[nicholas-navin]] — corresponding author; also [[navin-2011-sns-tumor-evolution|SNS]] and later [[kim-2018-tnbc-chemoresistance]].
- [[ken-chen]] — coauthor; computational analysis.

## Concepts touched

- [[scwga]] — nuc-seq is the G2/M-input variant of MDA; the input-copy-number lever is distinct from every chemistry lever in [[scwga-chemistries]].
- [[allele-dropout]] — reduced to 9.7% by starting from four copies rather than one.
- [[intratumor-heterogeneity]] — the punctuated-CNA / gradual-SNV two-clock model.

## Connections to other sources

- Direct predecessor from the same lab: [[navin-2011-sns-tumor-evolution]] (SNS, copy number only, ~10% breadth ceiling).
- Direct successor: [[kim-2018-tnbc-chemoresistance]] (TNBC chemoresistance evolution).
- Validation chemistry: [[schmitt-2012-pnas]] (Duplex Sequencing); protocol at [[kennedy-2014-duplex-protocol]].
- Compared against: [[chenghang-2012-science]] (MALBAC — 69.5% breadth on unique reads, FPR 4 × 10⁻⁵), [[dean-2002-mda]].
- Contemporary clonal-structure work with a different design: [[gawad-2014-all-clonal-origins]] (targeted, 1,479 cells, ALL).
- Later CNA-phylogeny methods that consume this kind of data: [[kaufmann-2022-medicc2]], [[wang-2021-medalt]].
- Amplification-free alternative that removes the WGA problem entirely: [[zahn-2017-dlp]], [[laks-2019-dlp-plus]].

## Open questions

- **Is the 13.3× TNBC mutation rate a subtype property or a patient property?** n = 1 per subtype cannot separate them.
- The model assumes a constant mutation rate over tumour history; punctuated bursts (which the CNA data supports for rearrangements) would break that assumption for SNVs too.
- G2/M sorting selects proliferating cells. Whether quiescent tumour cells carry the same clonal structure is unaddressed and unaddressable by this design.

## Related

- [[navin-2011-sns-tumor-evolution]] · [[schmitt-2012-pnas]] · [[scwga]] · [[40-Topics/cancer-clonal-evolution]] · [[50-Notes/single-cell-duplex-sequencing]]
