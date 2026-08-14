---
type: summary
title: "Telenius et al. 1992 — Degenerate oligonucleotide-primed PCR (DOP-PCR)"
source: "[[00-Sources/papers/Degenerate oligonucleotide-primed PCR_ General amplification of target DNA by a single degenerate primer]]"
source_kind: paper
author: "Hakan Telenius, Nigel P. Carter, Charles E. Bebb, Marisa Nordenskjöld, Bruce A. J. Ponder, Alfredo Tunnacliffe"
published: 1992-07
ingested: 2026-08-10
doi: "10.1016/0888-7543(92)90147-K"
journal: "Genomics"
tags: [DOP-PCR, whole-genome-amplification, scWGA, founding-method, PCR, historical-anchor]
entities: []
concepts: ["[[dop-pcr]]", "[[scwga]]", "[[scwga-chemistries]]"]
topics: ["[[whole-genome-amplification]]"]
---

**Citation:** Telenius et al. (1992) — *Degenerate oligonucleotide-primed PCR: general amplification of target DNA by a single degenerate primer* — *Genomics* 13, 718–725. [DOI](https://doi.org/10.1016/0888-7543%2892%2990147-K)

# Telenius 1992 — DOP-PCR

> The first general-purpose whole-genome amplification chemistry: a single partially degenerate primer (fixed 3′ hexamer, degenerate core, fixed 5′ tag) primes at ~10⁶ sites genome-wide under low-stringency cycles, then switches to high-stringency cycles that amplify only the tagged products — species-independent amplification from minute or single-cell input.

> ⚠️ **Source caveat.** The bookmarked clipping is a ScienceDirect landing page (metadata, citation counts, recommended articles) rather than the article body. The claims below are the method's canonical description as it is used throughout this wiki's corpus, not a paraphrase of full text this wiki has read. Treat the mechanistic detail as background, and cite [[gawad-2016-scgenome-review]] or [[dean-2002-mda]] where a read source is needed.

## Key claims

- One degenerate primer suffices for general amplification of any target DNA — no prior sequence knowledge, no species restriction.
- The two-phase cycling design (low-stringency priming → high-stringency tag-driven amplification) is the mechanism that converts random priming into an exponentially amplifiable library.
- The method works from very small inputs, which is what made it the first WGA chemistry adopted for single-cell and single-chromosome work.

## Methods / evidence

Original demonstration was on flow-sorted chromosomes and small genomic inputs, with comparative genomic hybridization as the downstream readout. Because the amplification is PCR-based and exponential from the first cycle, locus-to-locus yield differences compound — the quantitative weakness that later chemistries were built to fix.

## Surprising or load-bearing bits

- DOP-PCR's enduring role is not as a working method but as the **baseline against which every later chemistry is measured**. [[dean-2002-mda|Dean 2002]] reports 4–6 orders of magnitude locus-to-locus bias for DOP-PCR/PEP versus <3-fold for MDA — that contrast is the entire argument for isothermal strand displacement.
- Despite the bias, DOP-PCR's *uniformity at coarse resolution* kept it in service for CNV/karyotype work long after it was abandoned for SNV calling: [[navin-2011-sns-tumor-evolution|Navin 2011]] used DOP-PCR-style amplification precisely because copy-number binning tolerates amplitude bias that variant calling does not.
- 1,300+ citations and still cited by [[lahnemann-2021-natcomm|Lähnemann 2020]] and [[gawad-2016-scgenome-review|Gawad 2016]] — the field never stopped referencing its failure modes.

## Concepts touched

- [[dop-pcr]] — this is the founding citation for the page.
- [[scwga-chemistries]] — DOP-PCR occupies the first slot in the chronology DOP-PCR → [[mda]] → [[malbac]] → LIANTI → [[pta]].
- [[allele-dropout]] — PCR-based WGA's exponential bias is the origin of the ADO problem that dominates [[single-cell-variant-calling]].

## Connections to other sources

- Directly superseded on uniformity grounds by [[dean-2002-mda]].
- The CNV-tolerant use case is carried forward by [[navin-2011-sns-tumor-evolution]] and, in the direct-tagmentation era, by [[zahn-2017-dlp|DLP]]-style preamplification-free protocols that make the bias question moot.

## Open questions

- The clipping lacks the article body; if the original uniformity figures are needed for the review's methods chronology, the PDF should be re-clipped.

## Related

- [[dop-pcr]] · [[scwga-chemistries]] · [[whole-genome-amplification]] · [[dean-2002-mda]]
