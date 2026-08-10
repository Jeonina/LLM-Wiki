---
type: summary
title: "Jones 2012 — Functions of DNA methylation: islands, start sites, gene bodies and beyond"
source: "[[00-Sources/papers/Functions of DNA methylation_ islands, start sites, gene bodies and beyond - Nature Reviews Genetics]]"
source_kind: paper
author: "Peter A. Jones (University of Southern California)"
published: 2012-05-29
ingested: 2026-08-10
doi: "10.1038/nrg3230"
journal: "Nature Reviews Genetics"
tags: [DNA-methylation, CpG-island, gene-body-methylation, silencing-order, DNMT3, review, context-dependence]
entities: []
concepts: ["[[cpg-island]]", "[[dnmt]]", "[[tet-enzymes]]", "[[5hmc]]", "[[epigenetic-memory]]", "[[transposable-elements]]", "[[allele-specific-methylation]]", "[[enhancer-states]]"]
topics: ["[[dna-methylation]]"]
---

**Citation:** Jones, P. A. (2012) — *Functions of DNA methylation: islands, start sites, gene bodies and beyond* — *Nature Reviews Genetics* 13, 484–492. [DOI](https://doi.org/10.1038/nrg3230)

# Jones 2012 — methylation is context-dependent

> The review that dismantled "DNA methylation = silencing." Once whole-methylome data let the field look outside CpG-island promoters, the function of 5mC turned out to depend entirely on where it sits: blocking at start sites, permissive-to-stimulatory in gene bodies, variable and dynamic at enhancers, and switch-like at insulators.

## Key claims

- **Position within the transcription unit determines function.** Methylation near the TSS blocks initiation; gene-body methylation does not block and may stimulate elongation, and may affect splicing.
- Most CGIs stay unmethylated in somatic cells. Methylated promoter CGIs are restricted to genes needing **long-term** repression — imprinted genes, inactive-X genes, germ-cell-specific genes — stable across a 100-year lifespan.
- **Silencing usually precedes methylation, not the reverse.** Lock et al. showed *Hprt* methylation follows X-inactivation. Cancer genome-wide studies show Polycomb-silenced CGI promoters are the ones that become methylated. Methylation is a "lock," not the initiating event — though DNMT3A's requirement in short-lived HSC differentiation raises doubt about universality.
- The mechanistic reason: **de novo methylation requires a nucleosome** (Ooi et al.'s DNMT3A2–DNMT3L tetramer), and active TSSs are nucleosome-depleted, so they lack the substrate. Direct test in differentiating embryonal carcinoma cells gave the order: nucleosome appears → DNMT3A recruited → de novo methylation.
- CGIs are further protected by **H3K4me3 and H2A.Z** (both incompatible with DNMT3 ADD-domain binding, both anti-correlated with methylation), CFP1 maintaining H3K4me3, and TET1 occupying high-CpG promoters to oxidize any stray 5mC.
- Prediction confirmed: **the less-expressed allele is the one that gets methylated.** A low-activity *MLH1* promoter variant was preferentially methylated in cancer families; an extra SP1 site in a *RIL/PDLIM4* allele conferred resistance to de novo methylation.
- Gene bodies are CpG-poor, heavily methylated, and full of repeats. Methylation there blocks initiation from repeats while permitting readthrough of the host gene. **34% of intragenic CGIs are methylated in human brain**, and their function is unknown.
- Gene-body methylated CGIs carry H3K9me3 and bind MECP2 — marks that repress at a TSS — yet elongation proceeds. In *Neurospora*, methylation blocks elongation but not initiation, the exact inverse of mammals. **The mark does not carry the meaning; the context does.**
- Exons are more methylated than introns with transitions at exon–intron boundaries; nucleosome occupancy is higher on exons and nucleosomes are preferred methylation substrates; CTCF binding (methylation-sensitive) pauses Pol II. Together this sketches a methylation→splicing link.
- **Alternative promoters confound everything.** Most genes have ≥2 TSSs, so a downstream promoter sits inside the "body" of the upstream one. Expression probes measure all promoters' output while only one may be active — a structural source of apparent methylation/expression discordance.
- Enhancers are CpG-poor with **variable methylation**; Stadler et al. defined them operationally as "low-methylated regions" (LMRs) — neither 100% methylated nor unmethylated. Since a given cytosine is binary, LMR status means either dynamic competing methylation/demethylation or **inefficient maintenance through cell division**.
- Insulators: CTCF binding at *IGF2*/*H19* is blocked by methylation, but genome-wide in CpG-poor regions CTCF binding is generally *not* methylation-sensitive and instead **initiates local demethylation**. No universal rule.

## Methods / evidence

Review, written at the moment whole-genome bisulfite data first made non-CGI methylation visible. Careful about causality throughout — repeatedly distinguishing "methylation correlates with silencing" from "methylation causes silencing," and flagging where the field's data were "not yet mature enough to be sure."

## Surprising or load-bearing bits

- **The LMR interpretation is the single most important item for single-cell methylomics.** Jones states the logic explicitly: a cytosine is binary, so "variable methylation" in bulk is an average over cells or over time. The two candidate explanations — dynamic turnover vs. **inefficient inheritance during cell division** — are distinguishable only at single-cell resolution, and the second one is precisely the epimutation process that [[chen-2025-methyltree|MethylTree]], EPI-Clone and [[gaiti-2019-cll-epigenetic]] exploit as a lineage clock. This review is the bulk-era statement of why that clock exists.
- Enhancer LMRs being the *most* variable regions means methylation-based lineage tracing is reading the least stable part of the methylome — a feature for clocks, a bug for cell-type assignment.
- The **silencing-before-methylation** ordering matters for interpreting single-cell methylome clusters: methylation state reports on a locus's *history* of repression, not its current activity, at CGI promoters.
- Bisulfite cannot distinguish 5mC from 5hmC (stated in the review's Box). Every methylation claim here, and in [[bisulfite-sequencing]]-based single-cell methods, is a 5mC+5hmC composite — the gap [[tahiliani-2009-tet1-5hmc]] opened and [[chen-2025-sctaps-sccaps-plus]] closes.
- The alternative-promoter confound is an under-appreciated source of noise in any methylation–expression correlation, including single-cell joint assays like [[scnmt-seq]] and [[sctrio-seq]].
- Non-CpG methylation is noted as recently reported in mammals with function "currently unknown" — later central to neuronal methylomes ([[luo-2018-snmc-seq2]], where mCH is the discriminative signal).

## Concepts touched

- [[cpg-island]] — the protection mechanism (nucleosome depletion + H3K4me3 + H2A.Z + TET1) is stated most cleanly here.
- [[dnmt]] — DNMT1 alone is insufficient for maintenance; DNMT3A/3B participate ongoing.
- [[maintenance-asymmetry]] / [[methylation-clones-epimutation]] — the "inefficient inheritance" reading of LMRs is the conceptual root.
- [[allele-specific-methylation]] — the *MLH1* and *RIL* examples give a mechanism: expression level determines methylation susceptibility per allele.

## Connections to other sources

- Complements [[schubeler-2015-methylation-review]] and [[kim-2017-methylation-memory-review]]; predates and is refined by [[rothbart-2014-histone-dna-language]] on methylation-dependent TF *activation*.
- The LMR/epimutation logic is realized in [[chen-2025-methyltree]], [[gaiti-2019-cll-epigenetic]] and [[methylation-cancer-origin-classifiers]].
- Gene-body methylation is what [[hunt-2022-sctem-seq|scTEM-seq]] targets via transposable elements.
- Population-scale confirmation of context-dependence: [[roadmap-2015-111-epigenomes]] (intermediate methylation at enhancers).

## Open questions

- Are enhancer LMRs dynamic turnover or maintenance failure? Jones poses both; the corpus's epimutation-clock papers assume the second without directly excluding the first.
- Function of the 34% methylated intragenic CGIs in brain — unresolved here and unaddressed by any bookmarked source.
- Why only a minority of CpG islands ever become methylated is stated as unknown, and remains so.

## Related

- [[dna-methylation]] · [[cpg-island]] · [[schubeler-2015-methylation-review]] · [[methylation-clones-epimutation]]
