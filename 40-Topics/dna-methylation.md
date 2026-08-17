---
type: topic
title: DNA methylation
aliases: [5mC, cytosine methylation, methylation]
tags: [methylation, epigenetics, regulation]
created: 2026-05-11
updated: 2026-08-10
---

# DNA methylation

> Covalent modification of the fifth carbon of cytosine to produce 5-methylcytosine (5mC), predominantly at symmetric CpG dinucleotides in mammals ([[10-Summaries/smith-2013-methylation-development]]). It is the most stable and best-studied epigenetic mark, maintained through mitosis by DNMT1 ([[10-Summaries/kim-2017-methylation-memory-review]]), contributes to cell identity ([[10-Summaries/kim-2017-methylation-memory-review]]), silences transposons ([[10-Summaries/smith-2013-methylation-development]]), establishes imprints ([[10-Summaries/smith-2013-methylation-development]]), and is dysregulated in cancer and aging ([[10-Summaries/smith-2013-methylation-development]]). This cluster covers the biology of methylation, the canonical measurement chemistries (bisulfite, long-read direct detection), and the enzymatic machinery (DNMT, TET).

## Biology and definition

In mammals, ~60–80% of the ~28 million CpG dinucleotides in the human genome are methylated ([[10-Summaries/smith-2013-methylation-development]]). Less than 10% of CpGs sit in **CpG islands** — short (~200–2000 bp) regions of high CpG density at promoters of housekeeping and developmental genes, which are constitutively unmethylated ([[10-Summaries/smith-2013-methylation-development]]). Methylation is globally reset during two developmental windows: pre-implantation and primordial germ cell specification ([[10-Summaries/smith-2013-methylation-development]]).

Other modification forms ([[10-Summaries/fu-2025-longread-methylation]]):

- **5-hydroxymethylcytosine (5hmC)** — TET-catalyzed oxidation intermediate; a functional readout in some contexts ([[10-Summaries/fu-2025-longread-methylation]]; see also [[10-Summaries/bai-2024-simple-seq]] for joint 5mC/5hmC measurement).
- **N6-methyladenine (6mA)** — common in prokaryotes; rare in mammals ([[10-Summaries/fu-2025-longread-methylation]]).
- **N4-methylcytosine (4mC)** — prokaryotic ([[10-Summaries/fu-2025-longread-methylation]]).
- **Non-CpG 5mC (mCpH)** — found in brain and pluripotent cells ([[10-Summaries/fu-2025-longread-methylation]]).

## Why it matters

- **Stable propagation of cell identity** — marks established during differentiation are maintained through mitosis, contributing to epigenetic memory ([[10-Summaries/kim-2017-methylation-memory-review]]).
- **Genomic imprinting and X-inactivation** — methylation establishes parent-of-origin and chromosome-of-origin gene-expression patterns, with imprinted loci established in primordial germ cells ([[10-Summaries/smith-2013-methylation-development]]).
- **Transposon silencing** — most repetitive elements are heavily methylated ([[10-Summaries/smith-2013-methylation-development]]); loss of methylation can derepress LINE-1, SINE, and ERV elements, triggering "viral mimicry" interferon responses ([[10-Summaries/hunt-2022-sctem-seq]]).
- **Disease biomarker** — cancer-associated promoter hypermethylation silences tumor suppressors; global hypomethylation enables oncogene activation and chromosome instability ([[10-Summaries/smith-2013-methylation-development]]).
- **Therapeutic target** — DNMT inhibitors (hypomethylating agents) are approved for MDS / AML ([[10-Summaries/hunt-2022-sctem-seq]]); decitabine vs azacitidine produce divergent demethylation patterns ([[10-Summaries/shen-2026-splicool-seq]]).
- **Predicts and is predicted by chromatin accessibility** — methylation–accessibility coupling strengthens along differentiation ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018 scNMT-seq]]).
- **Largely independent of CNVs** — CNVs drive expression but do not propagate to local methylation state ([[10-Summaries/hou-2016-sctrio-seq|Hou 2016 scTrio-seq]]).

## Measurement chemistries

- **Bisulfite sequencing** — C→U→T conversion of unmethylated C; the standard short-read assay. Suffers from the three-base alignment problem ([[10-Summaries/fu-2025-longread-methylation]]).
- **EM-seq / TAPS-seq** — enzymatic, bisulfite-free alternatives with less DNA damage ([[10-Summaries/fu-2025-longread-methylation]]); TAPS uses TET + borane ([[10-Summaries/fu-2025-longread-methylation]]).
- **Long-read direct detection** — PacBio (kinetic features) and Oxford Nanopore (current changes through the pore) call methylation without base conversion, preserving full alignment quality in repeats and structural variants ([[10-Summaries/fu-2025-longread-methylation]]).
- **NOMe-seq** — GpC methyltransferase footprint for an accessibility readout ([[10-Summaries/clark-2018-scnmt-seq|Clark 2018 scNMT-seq]]).
- **Microarrays** — limited to pre-selected ~935,000 CpGs (synthesis; standard EPIC array specification).

### Single-cell methylation methods

scBS-seq, scRRBS, snmC-seq2, and sciMETv2 are sparse but compatible with multi-omic combinations ([[10-Summaries/iqbal-2023-methylome-review]]).

- [[30-Concepts/sctem-seq]] — single-cell SINE Alu methylation as a global-methylation proxy ([[10-Summaries/hunt-2022-sctem-seq]]).
- [[30-Concepts/simple-seq]] — single-cell 5mC + 5hmC joint at base resolution ([[10-Summaries/bai-2024-simple-seq]]).
- [[30-Concepts/splicool-seq]] — single-cell 5mC + accessibility ([[10-Summaries/shen-2026-splicool-seq]]).
- [[30-Concepts/scepi2-seq]] — single-cell histone mark + 5mC ([[10-Summaries/geisenberger-2025-scepi2-seq]]).
- [[30-Concepts/6-base-cut-and-tag]] — 5mC + 5hmC at histone-marked fragments ([[10-Summaries/tavares-2026-6-base-cut-tag]]).

## Enzymatic machinery and core concepts

- [[30-Concepts/cpg-island]] — unmethylated regulatory features.
- [[30-Concepts/dnmt]] — methyltransferase enzymes (maintenance + de novo).
- [[30-Concepts/tet-enzymes]] — active demethylation pathway.
- [[30-Concepts/5hmc]] — oxidative intermediate / stable enhancer mark.
- [[30-Concepts/uhrf1]] — DNMT1 maintenance cofactor.
- [[30-Concepts/epigenetic-memory]] — heritable cell-type memory through methylation.
- [[30-Concepts/transposable-elements]] — silenced by methylation; [[30-Concepts/viral-mimicry]] when re-expressed.
- [[30-Concepts/epigenetic-aging]] — methylation clocks.
- [[30-Concepts/cancer-of-unknown-primary]] — methylation as a tissue-of-origin classifier.
- [[30-Concepts/bisulfite-sequencing]] — standard short-read assay.
- [[40-Topics/long-read-sequencing]] — direct methylation detection without conversion.
- [[30-Concepts/taps]] — bisulfite-free 5mC chemistry (TET + borane).
- [[30-Concepts/nome-seq]] — GpC methyltransferase for accessibility readout.

## Examples

- Cancer-associated hypermethylation of CDKN2A, MLH1, BRCA1 promoters ([[10-Summaries/smith-2013-methylation-development]]).
- X-inactivation: random monoallelic silencing maintained via methylation of XIST and downstream genes ([[10-Summaries/smith-2013-methylation-development]]).
- DNMT3A R882 mutations in clonal hematopoiesis perturb early progenitor states through selective hypomethylation ([[10-Summaries/nam-2022-natgenet]]).

## Key entities

- [[20-Entities/alexander-meissner]] — foundational methylation development review.
- [[20-Entities/fritz-sedlazeck]] — long-read methylation analysis.
- [[20-Entities/winston-timp]] — nanopore methylation pioneer.
- [[20-Entities/chengqi-yi]] — bisulfite-free chemistry (SIMPLE-seq, hmC-CATCH).
- [[20-Entities/chun-xiao-song]] — TAPS chemistry inventor.
- [[20-Entities/heather-lee]] — scTEM-seq, single-cell methylation in AML.
- [[20-Entities/xiaoying-fan]] — SpliCOOL-seq high-throughput multi-omics.
- [[20-Entities/joseph-costello]] — glioma methylation, EPICUP classifier.
- [[20-Entities/shankar-balasubramanian]] — 6-base sequencing (biomodal evoC).
- [[20-Entities/biomodal]] — 6-base sequencing kits (5mC + 5hmC).

## Sources, by sub-theme

### Biology

- [[10-Summaries/smith-2013-methylation-development]] — Smith & Meissner 2013 foundational development review.
- [[10-Summaries/kim-2017-methylation-memory-review]] — Kim/Costello 2017 epigenetic memory review.

### Computational analysis and long-read methods

- [[10-Summaries/fu-2025-longread-methylation]] — Fu et al. computational long-read methylation analysis.
- [[10-Summaries/liu-2025-long-read-epigenome-review]] — Liu/Conesa 2025 NRG epigenome long-read review.

### Single-cell methylation methods

- [[10-Summaries/hunt-2022-sctem-seq]] — Hunt/Lee 2022 (scTEM-seq).
- [[10-Summaries/bai-2024-simple-seq]] — Bai/Yi 2024 (SIMPLE-seq).
- [[10-Summaries/shen-2026-splicool-seq]] — Shen/Fan 2026 (SpliCOOL-seq).
- [[10-Summaries/geisenberger-2025-scepi2-seq]] — Geisenberger/van Oudenaarden 2025 (scEpi²-seq).
- [[10-Summaries/iqbal-2023-methylome-review]] — Iqbal 2023 single-cell methylome analysis review.

### Methylation + chromatin joint readouts

- [[10-Summaries/tavares-2026-6-base-cut-tag]] — Tavares/Balasubramanian 2026 (6-base-CUT&Tag).

### Long-read methylation in repetitive regions

- [[10-Summaries/mo-2023-stam-seq]] — Mo/Zhai 2023 (STAM-seq, plant HRRs).

### Cancer methylation applications

- [[10-Summaries/nichols-2022-scimet-v2]] — sciMETv2 robust scMethylation.
- [[10-Summaries/luo-2018-snmc-seq2]] — snmC-seq2 single-cell methylome profiling.

### Computational tooling (lint pass 2026-05-21)

- [[10-Summaries/ghorbani-2019-comp-epigenetics]] — Ghorbani 2019 — Computational approaches in epigenetic research (review).
- [[10-Summaries/krueger-2011-bismark]] — Krueger 2011 — Bismark: aligner and methylation caller for bisulfite-seq.

## Synthesized notes

- [[50-Notes/regulatory-layers-overview]] — methylation as one of the four molecular regulatory layers.

## Open questions

- Methylation-calling accuracy benchmarking across PacBio and ONT platforms — no community-standard benchmark ([[10-Summaries/fu-2025-longread-methylation]]).
- 5hmC: functional mark vs intermediate — unresolved ([[10-Summaries/bai-2024-simple-seq]]; [[10-Summaries/fu-2025-longread-methylation]]).
- Single-cell methylation at scale — current methods are sparse; intersection with [[40-Topics/scdna-seq]] remains an open methodological frontier ([[10-Summaries/iqbal-2023-methylome-review]]).
- Non-CpG methylation (mCpH) in adult tissues, especially brain — functional significance ([[10-Summaries/fu-2025-longread-methylation]]).
- Are HMAs (decitabine vs azacitidine) clinically interchangeable? Single-cell data argues no — divergent demethylation patterns, and viral-mimicry response decoupled from raw methylation loss ([[10-Summaries/shen-2026-splicool-seq]]; [[10-Summaries/hunt-2022-sctem-seq]]).

## Additions — 2026-08-10 ingest

- **Function is context-dependent, not uniformly repressive.** Methylation near the TSS blocks initiation; gene-body methylation does not block and may stimulate elongation and affect splicing; in *Neurospora* the relationship is exactly inverted, so the mark does not carry the meaning — the context does ([[10-Summaries/jones-2012-dna-methylation-functions]]).
- **Silencing usually precedes methylation.** De novo methylation requires a nucleosome, and active TSSs are nucleosome-depleted, so methylation acts as a lock on an already-silenced state; the less-expressed allele is preferentially methylated ([[10-Summaries/jones-2012-dna-methylation-functions]]).
- **Enhancers are "low-methylated regions" whose intermediate bulk values must reflect either dynamic turnover or inefficient maintenance through division** — the bulk statement of why methylation epimutation clocks work ([[10-Summaries/jones-2012-dna-methylation-functions]]), operationalized as de novo VMR discovery in single cells ([[10-Summaries/kremer-2024-methscan]]).
- **Population-scale confirmation**: >18,000 intermediate-methylation regions (~57% mCpG) persist within purified cell types, "probably reflecting a stable state of cell-to-cell variability" ([[10-Summaries/roadmap-2015-111-epigenomes]]).
- **Methylation-dependent activation breaks the silencing dogma** — KLF2/KLF4/KLF5 bind specific sequences *because* they are methylated, and 5mC recognition stimulates KLF4-mediated transcription ([[10-Summaries/rothbart-2014-histone-dna-language]]).
- **Bisulfite-free single-cell chemistry** now separates 5mC from 5hmC at single-base resolution ([[10-Summaries/chen-2025-sctaps-sccaps-plus]]); the kinetic route dates to [[10-Summaries/flusberg-2010-smrt-methylation]] and the enzymatic origin of 5hmC to [[10-Summaries/tahiliani-2009-tet1-5hmc]].

## Related

- [[cpg-island]]
- [[dnmt]]
- [[tet-enzymes]]
- [[bisulfite-sequencing]]
- [[40-Topics/long-read-sequencing]]
- [[5hmc]]
- [[decitabine]]
- [[epigenetic-memory]]
- [[50-Notes/regulatory-layers-overview]]
- [[10-Summaries/jones-2012-dna-methylation-functions]] · [[10-Summaries/kremer-2024-methscan]] · [[10-Summaries/chen-2025-sctaps-sccaps-plus]] · [[10-Summaries/tahiliani-2009-tet1-5hmc]]

## Added 2026-08-13

Five sources ingested 2026-08-13 complete the single-cell methylation methods tree.

**The founding cell-typing result.** [[10-Summaries/luo-2017-snmc-seq]] (snmC-seq) established methylation as a primary typing modality by exploiting **mCH**: modulated over large domains, so 100-kb-bin estimates hold across >90% of the genome despite 4.7–5.7% coverage per cell. 16 mouse / 21 human cortical neuron clusters, ~500,000 CG-DMRs per species (68–73% >10 kb from any TSS), with an ISH-validated prediction that cluster mDL-2 differs in projection target. Its DMRs are now the annotation reference every higher-throughput method depends on.

**Two protocols defining opposite ends of the coverage axis.** [[10-Summaries/clark-2017-scbs-seq-protocol]] (PBAT, five-round preamplification, ~50% of CpGs per cell) and [[10-Summaries/guo-2015-scrrbs-protocol]] (one-tube MspI-based reduced representation, ~1M CpGs but **consistently the same** CpGs across cells, ~70% of CGIs).

**Two throughput strategies.** [[10-Summaries/mulqueen-2018-sci-met]] (combinatorial indexing via cytosine-depleted adaptors; alignment rate 68 ± 8% vs the field's 25 ± 20%) and [[10-Summaries/zhang-2023-drop-bs]] (droplets, up to 10,000 cells in 2 days; in-droplet bisulfite conversion yields 9× more library than bulk).

See [[30-Concepts/bisulfite-sequencing]] for the consolidated comparison table.

## Added 2026-08-17

Two epimutation-clock sources ingested 2026-08-14 add a use of methylation the corpus had not covered: methylation as a **timer** rather than as a cell-type fingerprint.

[[10-Summaries/shahryary-2020-alphabeta]] (plants) estimates forward and backward epimutation rates from pedigree data and establishes the three properties a clock needs — neutral accumulation, somatic origin, and demonstrable age-dating. [[10-Summaries/gabbutt-2025-evoflux]] (human) reads **fluctuating CpGs** from bulk methylation arrays across 1,976 lymphoid cancers to infer growth rate, malignancy age, epimutation rate and subclonal structure at clinical scale.

Both share an unquantified limit: gain/loss equilibrium means the clock **saturates**, bounding how far back it can read. (synthesis) See [[30-Concepts/methylation-clones-epimutation]].
