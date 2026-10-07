---
type: summary
title: "Zong 2017 — MALBAC for the analysis of DNA copy number variation (Neuromethods chapter)"
source: "[[00-Sources/papers/Multiple Annealing and Looping-Based Amplification Cycles (MALBAC) for the Analysis of DNA Copy Number Variation.pdf]]"
source_quality: full
source_sha256: "e7054ef8665a29634c2b92d47c4c64aa3263a0b29c0d952e71fbb7f3e1285ffa"
source_kind: paper
author: "Chenghang Zong"
published: 2017
ingested: 2026-08-10
updated: 2026-10-07
doi: "10.1007/978-1-4939-7280-7_7"
journal: "Neuromethods vol. 131 — Genomic Mosaicism in Neurons and Other Cell Types (Frade & Gage, eds.), Chapter 7, pp. 133–142"
tags: [MALBAC, scWGA, copy-number-variation, review-chapter, quasi-linear-amplification, Lorenz-curve, power-spectrum, CTC, PGS, polar-body]
entities: ["[[x-sunney-xie]]"]
concepts: ["[[malbac]]", "[[scwga]]", "[[scwga-chemistries]]", "[[mda]]", "[[copy-number-variation]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[whole-genome-amplification]]", "[[brain-somatic-mosaicism]]"]
---

**Citation:** Zong, C. (2017) — *Multiple annealing and looping-based amplification cycles (MALBAC) for the analysis of DNA copy number variation* — in Frade & Gage (eds), *Genomic Mosaicism in Neurons and Other Cell Types*, Neuromethods 131, pp. 133–142. [DOI](https://doi.org/10.1007/978-1-4939-7280-7_7)

# Zong 2017 — MALBAC chapter

> A ten-page review chapter by MALBAC's first author, despite the series' protocol format. It contains **no bench protocol, no Materials or Methods section, and no new data**. It describes the MALBAC chemistry (five looping pre-amplification cycles, then PCR), restates the coverage, uniformity and CNV results of the 2012 *Science* paper, and points to two clinical uses: CNV profiling of circulating tumour cells (Ni et al. 2013) and aneuploidy screening of oocytes from polar bodies (Hou et al. 2013). Every figure is reprinted from those three papers. Although the chapter sits in a volume on neuronal mosaicism, it contains **no neuron data**. Its message is that MALBAC's low large-scale bias, unlike MDA's, makes single-cell CNV calling reliable enough for clinical genome screening.

## Key claims

- **The problem with earlier chemistries.** First-generation PCR-based WGA leaves a "significant portion of genomes (over 50%)" uncovered because of priming inefficiency and early PCR bias. MDA solves priming with φ29 at 30 °C and "can robustly cover 80% of the genome" with alkaline lysis. But displaced strands re-hybridise into "nanoball" hyper-branched structures of varying size, giving "considerable regional bias", which "makes MDA unsuitable for reliable detection of copy number variations". MDA is "essentially a nonlinear amplification with the exponential dependence of DNA yield on the time of reaction, which makes it difficult to accurately detect single-nucleotide variations."
- **Chemistry.** Primers are a common 27-nt sequence made only of G, A and T, plus eight variable 3′ nucleotides ("5N3G and 5N3T"), so they "can evenly hybridize to the templates at 0 °C". Each cycle quenches to 0 °C, extends at 65 °C with Bst (strand-displacing) polymerase to make 0.5–1.5-kb semi-amplicons, and melts at 94 °C. Copying a semi-amplicon gives a full amplicon with complementary ends, which loops at 58 °C so that it is not amplified in the next cycle. Five pre-amplification cycles are followed by PCR on the common 27-nt sequence. Producing ">10 copies of amplicons" in pre-amplification means "the initial-stage PCR bias with single copy of DNA fragments can be significantly reduced" (Fig. 1).
- **Coverage.** In single SW480 cancer cells at ~25× mean depth, MALBAC "consistently achieved ~85% and up to 93% genome coverage at ≥1× depth on either strand". A single-cell MDA at 25× covered 72% even at ~1×. "MALBAC coverage is highly reproducible."
- **Uniformity.** In Lorenz curves at ~25×, MALBAC lies between bulk and MDA: "It is evident that MALBAC outperforms MDA in uniformity of genome coverage" (Fig. 3). In the power spectrum of read density, MDA has large amplitudes at low spatial frequency, meaning regions of several megabases are over- or under-amplified, while MALBAC "has a power spectrum similar to that of the unamplified bulk" (Fig. 4).
- **CNV calling.** Three single SW480 cells sequenced at only 0.8× (200-kb bins, HMM fit) show distinct cell-to-cell CNV differences against the bulk at 25×. An MDA cell at 25× cannot resolve them (Fig. 5). "The gross features of CNVs detected by MALBAC are consistent with karyotyping data (data not shown)."
- **Circulating tumour cells.** Single CTCs from patients with lung adenocarcinoma (ADC) showed reproducible CNV patterns "among five patients", "in contrast to the patients with a mixture of ADC and SCLC". Recurrent gains include *MYC*, *PIK3CA*/*PIK3CB*, *TERT* and *MYCL1* (Fig. 6, from Ni et al. 2013). From this the author concludes that CNVs "can be specific to cancer types, reproducible from cell to cell, and even from patient to patient".
- **Preimplantation genetic screening.** In Hou et al. 2013, MALBAC on the first and second polar bodies predicted the female pronucleus's chromosome copy numbers, and direct measurement confirmed the prediction. Downsampling to 0.1×, 0.01× and 0.001× suggests "0.01× data are sufficient for aneuploidy deduction at megabase resolutions" (Fig. 7). "The consistent result proves that MALBAC can provide reliable detection of copy number variations for PGD or PGS."

## Methods / evidence

There are no methods. The chapter's evidence is seven figures, all reprinted with permission from Zong et al. 2012 *Science* (Figs. 1–5: SW480 cells, Lorenz curves, power spectrum, CNV profiles), Ni et al. 2013 *PNAS* (Fig. 6: CTC gain/loss significance) and Hou et al. 2013 *Cell* (Fig. 7: polar bodies and pronucleus). The 16 references are mostly WGA and single-cell sequencing primaries. The chapter does not give reagent lists, volumes, cycle times, library prep or CNV-calling parameters, and does not discuss MALBAC's limitations.

Weight: a secondary, author-written overview whose numbers come entirely from earlier primary papers. Cite those papers ([[chenghang-2012-science]] for the SW480 coverage and CNV results) rather than this chapter for any quantitative claim. The text has small editing slips: it points to "dashed boxes in Fig. 3" for cell-to-cell CNV differences, but the dashed boxes are in Fig. 5. It mentions "CNVs of five cells are included in the supplementary materials", but the chapter has no supplement; the sentence is carried over from the 2012 paper. And the CTC text says "five patients" while the Fig. 6 caption says six. (synthesis)

## Limitations

**Authors' own:**
- None stated. The chapter presents MALBAC's results without discussing weaknesses, error rates or allelic balance.

**Reviewer notes:**
- The chapter is not a protocol. Anyone looking for a MALBAC bench procedure must go to the 2012 *Science* supplement or a commercial kit manual. (synthesis)
- The chapter compares MALBAC only with MDA. SNV performance is raised only as an MDA weakness; MALBAC's own SNV false-positive behaviour is not discussed, though the wiki's primary source and later benchmarks address it ([[10-Summaries/chenghang-2012-science]]; [[10-Summaries/hou-2015-wga-comparison]]). (synthesis)
- No neuronal application is shown, so the chapter does not by itself support any claim about neuron CNV rates. (synthesis)

## Surprising or load-bearing bits

- **Clinical uses carry the argument.** The chapter's case for MALBAC rests less on uniformity metrics than on two clinical demonstrations: CTC CNV profiles that recur across patients, and pronucleus aneuploidy predicted from polar bodies at as little as 0.01× depth. (synthesis)
- **Power spectrum as the uniformity diagnostic.** A Lorenz curve shows *how much* bias there is. The power spectrum shows *at what scale*. MDA's excess sits at megabase wavelengths, which is exactly the scale that CNV binning is sensitive to. This is the clearest statement in the wiki of why MDA fails for CNV even when it covers more bases. (synthesis)
- **0.8× is enough.** The SW480 CNV profiles came from single cells sequenced at 0.8×, and polar-body aneuploidy at 0.01×. Shallow sequencing for CNV, later standard in DLP and 10x CNV, is already present here. (synthesis)
- **The neuronal framing comes from the volume, not the chapter.** The neuron connection comes only from the volume and from the reference list (Evrony 2012, Lodato 2015). (synthesis)

## Entities mentioned

- [[x-sunney-xie]] — senior author of every primary study whose figures the chapter reprints (Zong 2012, Ni 2013, Hou 2013).

## Concepts touched

- [[malbac]] — chemistry details: G/A/T-only 27-nt common sequence, 8-nt variable 3′ end, 0 °C quench, 65 °C Bst extension, 58 °C looping, five cycles.
- [[mda]] — described as nonlinear, nanoball-forming, regionally biased and unsuitable for CNV.
- [[copy-number-variation]] — HMM CNV calling from 0.8× single-cell data in 200-kb bins; CTC and polar-body applications.
- [[sequencing-depth-and-coverage]] — Lorenz curves and power spectra as uniformity metrics; coverage of 85–93% against 72%.
- [[scwga-chemistries]] — MALBAC set against PCR-based WGA and MDA.

## Connections to other sources

- Every quantitative result restates [[chenghang-2012-science]], the primary MALBAC paper in this wiki.
- [[hou-2015-wga-comparison]] independently benchmarks MALBAC between MDA and DOP-PCR, and reanalyses the same published MALBAC SW480 data.
- The PCR-based first generation it criticises begins with [[telenius-1992-dop-pcr]]; MDA with [[dean-2002-mda]].
- Later alternatives: [[gonzalez-pena-2021-pnas]] (PTA, quasi-linear without looping) and the amplification-free [[zahn-2017-dlp]] / [[laks-2019-dlp-plus]] (see [[dlp-plus]]).
- The neuronal-mosaicism context comes through its references to Lodato 2015 ([[lodato-2015-science]]); single-neuron aneuploidy is also treated in [[mukamel-2025-aneuploidy-brain]].
- Reviews of MALBAC alongside other chemistries: [[huang-2015-scwga-review]], [[gawad-2016-scgenome-review]].

## Open questions

- Does MALBAC keep a niche now that PTA and amplification-free tagmentation outperform it on SNVs and on CNVs respectively? The chapter, written before both, does not address this. (synthesis)
- The chapter never addresses how MALBAC's early-cycle polymerase errors affect SNV calls, the main trade-off discussed elsewhere in the wiki. (synthesis)

## Related

- [[malbac]] · [[scwga-chemistries]] · [[chenghang-2012-science]] · [[whole-genome-amplification]] · [[hou-2015-wga-comparison]]
