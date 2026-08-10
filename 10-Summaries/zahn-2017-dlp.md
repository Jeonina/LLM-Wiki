---
type: summary
title: "Zahn et al. 2017 — Scalable whole-genome single-cell library preparation without preamplification (DLP)"
source: "[[00-Sources/papers/Scalable whole-genome single-cell library preparation without preamplification]]"
source_kind: paper
author: "Hans Zahn, Adi Steif, Emma Laks, Peter Eirew, Michael VanInsberghe, Sohrab P. Shah, Samuel Aparicio, Carl L. Hansen (corresponding)"
published: 2017-01-09
ingested: 2026-08-10
doi: "10.1038/nmeth.4140"
journal: "Nature Methods"
tags: [DLP, amplification-free, direct-tagmentation, microfluidics, copy-number, bulk-equivalent-genome, founding-method, xenograft]
entities: []
concepts: ["[[dlp-plus]]", "[[scwga]]", "[[scwga-chemistries]]", "[[tn5-tagmentation]]", "[[dop-pcr]]", "[[pseudo-bulk]]", "[[phylogenetic-inference]]"]
topics: ["[[whole-genome-amplification]]", "[[cancer-clonal-evolution]]", "[[scdna-cancer-applications]]"]
---

**Citation:** Zahn et al. (2017) — *Scalable whole-genome single-cell library preparation without preamplification* — *Nature Methods* 14, 167–173. [DOI](https://doi.org/10.1038/nmeth.4140)

# Zahn 2017 — DLP

> The paper that made amplification-free single-cell genomics work. Tagment unamplified single-cell DNA in **nanolitre volumes** on a 192-chamber microfluidic device, add barcodes by PCR, sequence shallow. Because fragmentation happens *first*, every PCR copy is an exact duplicate that can be removed computationally — so every retained read is a unique representation of the original template.

## Key claims

- **The core argument against WGA, stated mechanistically.** WGA makes many copies of each template as long molecules that are fragmented *later*, so one original region appears as multiple inserts with non-overlapping coordinates that **cannot be filtered as duplicates**. DLP fragments the template first; all copies are exact duplicates and are computationally removable.
- Among WGA chemistries, DOP-PCR gives better coverage uniformity than MDA or MALBAC and is therefore the most CNA-amenable — but its coverage breadth **saturates with deeper sequencing**, making it unsuitable for SNVs.
- **782 cells** analysed: 152 × 184-hTERT-L2 and 123 × GM18507 near-diploid cells, plus 296 + 299 cells from two serial passages of a triple-negative breast cancer PDX (SA501X3F, SA501X4F).
- Coverage: mean **0.07–0.12× depth per cell**; merging 64 DLP cells gives median **94.5%** (184-hTERT-L2) and **96.8%** (GM18507) breadth. Trimmed and downsampled to match the C-DOP-L comparison, 64 DLP cells reach 57.7–58.8% breadth versus **44.5%** for C-DOP-L.
- **A merged genome of 48 DLP cells matches a true bulk genome** of the same depth in breadth and Lorenz-curve uniformity.
- Against DOP-PCR on tumour cells: WGA4 suffers low mappability from adaptor contamination, C-DOP-L has high duplicate rates — both needing ~2× the total reads for the same usable yield — and heavily downsampled DLP cells still show significantly lower MAD on the one chromosome diploid in all samples (KW P < 2.2 × 10⁻¹⁶).
- **Clonal structure and its dynamics.** SA501X3F resolved into clone A (n = 214, one copy chrX), minor clone B (n = 28, two copies chrX plus alterations on ten chromosomes) and clone C (n = 18, additional chr11 events). In the **next passage**, clones B and C were undetectable and clone A's descendants had diversified into numerous small subclones — including one that had lost the ancestral chr16 amplification (n = 20 cells).
- **Bulk-equivalent genomes work.** Merging all libraries in silico and running conventional callers — mutationSeq (SNVs), Titan (LOH), deStruct (breakpoints) — gives high concordance with a true bulk genome on variant allele prevalence, LOH state calls and individual breakpoints.
- Resolution: segments of **1–5 Mb** detectable in single cells against their clonal profile; in the highest-depth cells with smaller bins, **100–500 kb** — reported as the best sensitivity then achieved for low-depth single-cell CNA inference, against a contemporaneous finding that WGA single cells could not reliably detect germline variants <5 Mb.
- Cost and throughput: **~$0.50 per cell** and 192 libraries in 2.5 h hands-on, versus ~$15/cell and ~3 days for DOP-PCR protocols typically run on ≤96 samples.

## Methods / evidence

A custom 192-chamber microfluidic device with **inflatable reaction chambers** (arbitrary reagent additions and volumes), on-chip fluorescence imaging to distinguish single cells from doublets and debris, prespotted index primers sealed in during fabrication, and no-template-control chambers per column. Bootstrap merging (n = 30 draws per condition) for the coverage-breadth curves; matched downsampling and read trimming for fair cross-protocol comparison; mouse-genome alignment to detect xenograft contamination (one mouse cell and five contaminated libraries found and excluded).

The imaging step doing QC *before* library construction is the design decision that carries through to DLP+ and makes the platform's yield claims interpretable.

## Surprising or load-bearing bits

- **The duplicate-filtering argument is the conceptual core**, and it generalizes: any protocol that amplifies before fragmenting forfeits the ability to distinguish PCR duplicates from independent molecules. That single fact explains most of WGA's coverage pathology.
- **"Many cells shallow" beats "few cells deep" for copy number**, and the paper quantifies it: ten WGA cells at 30× costs the same as **6,000 DLP cells at 0.05×**, giving subclone detection sensitivity of ~0.05% (3/6,000). This is the clearest statement in the corpus of the breadth/depth trade tracked at [[droplet-vs-single-molecule-scdna]].
- **One experiment yields both single-cell resolution and a bulk genome.** The bulk-equivalent construct rescues low-cellularity clinical samples by *excluding* contaminating normal cells before merging — a capability true bulk sequencing structurally cannot have.
- Minor clones B and C were "not evident in the combined profile" — the merged genome loses exactly the subpopulations single cells exist to find. The authors state this as the reason both readouts are needed, and it is the cleanest demonstration in this corpus of what bulk deconvolution misses.
- **Read provenance is preserved after merging**, and the authors flag this as unexploited: future methods could use which-cell-each-read-came-from to call SNVs and breakpoints per subpopulation at lower depth. Partly realized by the clone-pseudo-bulk workflow in [[laks-2019-dlp-plus|DLP+]].
- Non-integer copy-number states appear in subpopulations of both normal cell lines, attributed to replication and apoptosis — the artefact that DLP+ later turns into a **measurement** of replication state.

## Concepts touched

- [[dlp-plus]] — this is the founding source for the DLP branch; DLP+ is its scaled successor.
- [[scwga-chemistries]] — DLP is the amplification-free alternative to the WGA chronology, not a step within it.
- [[pseudo-bulk]] — in-silico merging to bulk-equivalent and clonal genomes.

## Connections to other sources

- Scaled and re-engineered onto commodity nanowell hardware in [[laks-2019-dlp-plus]] (51,926 cells, imaging QC, replication state).
- Rejects [[telenius-1992-dop-pcr|DOP-PCR]], [[dean-2002-mda|MDA]] and [[zong-2017-malbac-protocol|MALBAC]] on the duplicate/uniformity argument; the opposite design philosophy is [[gonzalez-pena-2021-pnas|PTA]].
- CNV calling context: [[garvin-2015-natmethods|Ginkgo]], [[bakker-2016-aneufinder|AneuFinder]], [[wang-2020-scope|SCOPE]].
- Tumour-evolution lineage: [[navin-2011-sns-tumor-evolution]], [[kim-2018-tnbc-chemoresistance]], [[lu-2024-cnaphylogeny-review]].

## Open questions

- DLP explicitly "is not meant to capture complete single-cell genomes" — per-cell SNV calling remains out of reach, and the clone-aggregation workaround cannot see private mutations.
- Whether the approach transfers to droplet formats was proposed here and is still not standard in this corpus.

## Related

- [[laks-2019-dlp-plus]] · [[dlp-plus]] · [[scwga-chemistries]] · [[whole-genome-amplification]]
