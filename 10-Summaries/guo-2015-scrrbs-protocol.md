---
type: summary
title: "Guo et al. 2015 — Profiling DNA methylome landscapes of mammalian cells with single-cell reduced-representation bisulfite sequencing (scRRBS) [protocol]"
source: "[[00-Sources/papers/Profiling DNA methylome landscapes of mammalian cells with single-cell reduced-representation bisulfite sequencing]]"
source_kind: paper
author: "Hongshan Guo, Ping Zhu, Fan Guo, Xianlong Li, Xinglong Wu, Xiaoying Fan, Lu Wen, Fuchou Tang (corresponding)"
published: 2015-04-02
ingested: 2026-08-13
doi: "10.1038/nprot.2015.039"
journal: "Nature Protocols 10:645–659"
tags: [scRRBS, RRBS, MspI, single-tube-reaction, CpG-island, protocol, PGC, sperm, pronuclei]
entities: ["[[fuchou-tang]]", "[[xiaoying-fan]]"]
concepts: ["[[bisulfite-sequencing]]", "[[scbs-seq]]", "[[cpg-island]]", "[[allele-specific-methylation]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[dna-methylation]]", "[[scdna-seq]]"]
---

**Citation:** Guo et al. (2015) — *Profiling DNA methylome landscapes of mammalian cells with single-cell reduced-representation bisulfite sequencing* — *Nature Protocols* 10, 645–659. [DOI](https://doi.org/10.1038/nprot.2015.039)

# Guo 2015 — scRRBS protocol

> The protocol for [[guo-2013-scrrbs|scRRBS]], and the clearest statement of the counting argument that governs all single-cell methylation chemistry: **a diploid cell has two DNA molecules and every purification step loses some of them irreplaceably.** Standard RRBS has five purification points before PCR; scRRBS collapses all five into **one tube**, purifying only after bisulfite conversion. Result: ~1 million CpGs per diploid cell, including **~70% of CpG islands**.

## Key claims

- **The one-tube reaction is the entire innovation.** MspI digestion, end repair/dA tailing, adaptor ligation, and bisulfite conversion all proceed in a single tube — buffer system and reaction volumes were re-tuned (Tango buffer throughout) so each enzyme retains activity at its stage, with heat inactivation between steps. Even the gel-free RRBS protocols of the time still required three purifications; scRRBS requires zero before conversion.
- **~1 million CpG dinucleotides per single mouse diploid cell**, roughly **40% of the ~2.5 million recovered by standard RRBS from thousands of cells**, and ~70% of mouse CpG islands.
- **Coverage plateaus at five cells (~60% of standard RRBS)** — evidence that the single-tube approach itself imposes a ceiling, not merely input scarcity. This is a candid limitation the protocol states about its own design.
- **scRRBS and [[clark-2017-scbs-seq-protocol|scBS-seq]] are complementary, not competing.** scBS covers ~3.7 million CpGs per mouse cell — more total — but the authors identify two scBS limitations: **lower CGI coverage** despite including more CpG-sparse regions, and a **more random, less consistent** genomic sampling, so different cells overlap less at the same CpG sites. Choose by question: consistent CGI-focused comparison across cells → scRRBS; maximum total coverage per cell → scBS.
- **MspI plus size selection is the enrichment logic.** Standard RRBS sequences ~10% of the genome and reproducibly recovers >70% of promoters, >80% of CGIs, plus CGI shores, enhancers, exons, 3′ UTRs and repeats — the informative fraction, at a tenth of the WGBS cost.
- **Overnight ligation with premethylated adaptors and highly concentrated T4 ligase**; carrier tRNA present during the post-conversion purification; PCR then 200–700 bp gel selection.
- **Validated on the hardest and most valuable samples**: individual mouse sperm (where every recovered CpG reads as fully methylated or fully unmethylated, as expected for a haploid genome — an internal consistency check the assay design makes possible), individual human and mouse pronuclei from zygotes (capturing global demethylation dynamics), and 20-cell mouse embryonic samples (faithfully recovering the 50% methylation of imprinted regions).
- **Three weeks, strong molecular biology skills required** — an unusually blunt statement of protocol difficulty.

## Methods / evidence

Protocol paper backed by the lab's prior applications (Guo 2013, and the pronuclei/PGC work). The scRRBS-vs-scBS comparison is a literature comparison against Smallwood et al., not a head-to-head experiment.

## Surprising or load-bearing bits

- **The haploid sperm check is elegant validation.** In a single sperm every CpG has one copy, so any intermediate methylation value is an error. The assay's own biology supplies a ground truth that no other single-cell methylation experiment gets for free.
- **"Consistency of which CpGs are covered" is a distinct axis from "how many CpGs are covered"** — and scRRBS wins the former by construction, because MspI cuts the same sites in every cell. This matters enormously for cross-cell comparison: random coverage means two cells rarely share the same CpG, so any per-site comparison is mostly missing data. Almost no downstream methylation-analysis paper states this tradeoff as clearly.
- **The five-cell coverage plateau is an admission that the single-tube design trades ceiling for floor.** More input does not rescue it.
- **Reduced representation is the road not taken by the field.** Everything after 2015 — [[luo-2017-snmc-seq|snmC-seq]], [[mulqueen-2018-sci-met|sci-MET]], [[zhang-2023-drop-bs|Drop-BS]] — went whole-genome-and-sparse instead. Given that the high-throughput methods now cover ~1% of CpGs *randomly*, scRRBS's 1 million *consistent* CpGs is arguably still competitive for cross-cell comparison, and the corpus contains no benchmark testing that.
- **Three weeks of hands-on time** is the real reason it lost, not the coverage numbers.

## Entities mentioned

- [[fuchou-tang]] — corresponding author; single-cell multi-omics and germline/embryo epigenetics.
- [[xiaoying-fan]] — coauthor.

## Concepts touched

- [[cpg-island]] — the enrichment target that defines the reduced-representation strategy.
- [[bisulfite-sequencing]] — MspI-based reduced representation as the low-cost variant.
- [[scbs-seq]] — the explicit comparison partner.

## Connections to other sources

- Founding paper this protocol operationalises: [[guo-2013-scrrbs]].
- The whole-genome alternative it compares itself against: [[smallwood-2014-natmethods]], [[clark-2017-scbs-seq-protocol]].
- Used as the methylation arm inside a multi-omic assay: [[hou-2016-sctrio-seq]] (scTrio-seq uses scRRBS read distribution to call CNVs *and* methylation from the same nucleus) — the most consequential downstream use of this chemistry in the corpus.
- Higher-throughput whole-genome descendants: [[luo-2017-snmc-seq]], [[mulqueen-2018-sci-met]], [[nichols-2022-scimet-v2]], [[zhang-2023-drop-bs]].
- Germline/embryo methylation context from the same lab lineage: [[smith-2013-methylation-development]], [[schubeler-2015-methylation-review]].

## Open questions

- **Why coverage plateaus at five cells** is observed, not explained.
- **No head-to-head scRRBS vs scBS experiment exists** in the corpus — the complementarity claim rests on comparing published numbers across labs and samples.
- Whether the "consistent CpG coverage" advantage translates into better cross-cell DMR detection has never been benchmarked, despite being the strongest argument for the method.
- MspI restricts observation to CCGG-proximal CpGs; enhancers outside that fraction are structurally invisible, which matters for the distal-element discovery that [[luo-2017-snmc-seq]] makes central.

## Related

- [[guo-2013-scrrbs]] · [[clark-2017-scbs-seq-protocol]] · [[hou-2016-sctrio-seq]] · [[40-Topics/dna-methylation]]
