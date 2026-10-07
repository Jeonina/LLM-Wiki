---
type: summary
title: "Vaisvila et al. 2021 — Enzymatic methyl sequencing detects DNA methylation at single-base resolution from picograms of DNA"
source: "[[00-Sources/papers/Enzymatic methyl sequencing detects DNA methylation at single-base resolution from picograms of DNA]]"
source_quality: full
source_sha256: "3bb8b6e9a97bd03c7fb4a1b6ad272a5ca5e5794aa15d9ea19be81c5347cd7246"
source_kind: paper
author: "Romualdas Vaisvila, V.K. Chaithanya Ponnaluri, Zhiyi Sun, Bradley W. Langhorst, ... Theodore B. Davis (corresponding) — 20 authors, New England Biolabs"
published: 2021-06-17
ingested: 2026-10-07
doi: "10.1101/gr.266551.120"
journal: "Genome Research 31(7):1280–1289"
tags: [EM-seq, enzymatic-conversion, TET2, T4-BGT, APOBEC3A, bisulfite-free, WGBS, 5mC, 5hmC, low-input, cfDNA, FFPE, GC-bias, NA12878]
entities: []
concepts: ["[[bisulfite-sequencing]]", "[[5hmc]]", "[[tet-enzymes]]", "[[taps]]", "[[sequencing-depth-and-coverage]]", "[[duplicate-marking]]"]
topics: ["[[dna-methylation]]"]
---

**Citation:** Vaisvila et al. (2021) — *Enzymatic methyl sequencing detects DNA methylation at single-base resolution from picograms of DNA* — *Genome Research* 31(7):1280–1289. [DOI](https://doi.org/10.1101/gr.266551.120)

# Vaisvila 2021 — EM-seq

> Bisulfite's harsh temperature and pH degrade DNA, preferentially damage unmethylated cytosines and leave AT-rich, GC-poor, gappy libraries. **EM-seq** replaces the chemistry with three enzymes: **TET2** oxidises 5mC (→5hmC→5fC→5caC) and **T4-BGT** glucosylates 5hmC (→5gmC), protecting both; **APOBEC3A** then deaminates only unmodified C to U. The readout is identical to bisulfite (modified C reads as C, unmodified as T), so existing pipelines (Bismark, bwa-meth) work unchanged — but libraries are more complex, GC-even, and usable from **100 pg**, cfDNA and FFPE DNA.

## Key claims

- **Enzymes are efficient and selective**: TET2 oxidised ≥99% of 5mC across mouse, human and *Arabidopsis* DNA (96% in phage XP12, whose cytosines are 100% methylated); by LC-MS on NA12878, 5mC fell from 2.675% to ~0.02% with TET2, and became undetectable with TET2 + T4-BGT + APOBEC3A. The authors report 0.9% residual 5mC available for deamination after TET2/T4-BGT vs 2.7% reported for commercial bisulfite kits. APOBEC3A fully deaminated C and 5mC oligos (~50% of 5hmC by 180 min); 5fC was a poor substrate, 5caC and 5gmC appeared unreactive.
- **Same methylation, better libraries** (NA12878; 10, 50, 200 ng; 324 M read pairs each): CpG methylation ~52% for both methods, CHG/CHH <0.6%; controls: lambda <0.6%, CpG-methylated pUC19 ~96%. EM-seq gave higher yields with fewer PCR cycles, fewer duplicates, and an even GC profile versus bisulfite's AT-rich/GC-poor skew.
- **More CpGs covered at low depth**: of 56 million CpGs (both strands), EM-seq covered ~54 M at ≥1× for all inputs vs ~45 M (50/200 ng) and 36 M (10 ng) for WGBS; at ≥8× EM-seq covered ~7× more CpGs at 10 ng and 2.2× more at 200 ng. In a pairwise comparison EM-seq covered 53.4 M vs 25.9 M CpGs at 1× and 14.8 M vs 3.5 M at 5×, but WGBS covered more at 10× (615,413 vs 179,991) — read by the authors as bisulfite **focusing** coverage on a subset of CpGs. Above ~11× depth thresholds bisulfite libraries cover more CpGs.
- **Low input**: 100 pg to 10 ng libraries (810 M reads) kept even GC and ~53% CpG methylation; 1 ng and 10 ng covered 54 M CpGs at 1×; 500 pg and 100 pg covered ~50 M and ~24 M (vs 37 M for a 10-ng WGBS library).
- **Damaged/limited samples**: 10 ng cfDNA and lung FFPE DNA gave better insert size, duplication and GC metrics and more CpGs over genomic features than bisulfite.
- **Inserts stay long**: libraries up to 350 bp inserts and long amplicons from converted DNA, reflecting intact DNA.
- **Limits**: EM-seq reports 5mC + 5hmC together (5hmC-only needs a TET2-free, T4-BGT-only variant or ACE-seq); it cannot detect 5fC/5caC; in fully methylated XP12 DNA, detected methylation was lower than expected (90.2–97.4%).

## Methods / evidence

NEBNext Ultra II library prep with methylated EM-seq adaptors ligated *before* conversion for both EM-seq and WGBS (Zymo EZ Gold), so comparisons share the pre-conversion ligation design. Same flowcells; reads subsampled to equal numbers; bwa-meth, samblaster, MethylDackel, methylKit, Picard metrics; Nextflow pipeline released.

Weight: careful head-to-head with internal methylated/unmethylated controls, but all authors are NEB employees and the work is NEB-funded (the competing-interest statement says so). The bisulfite comparator is adaptor-ligation-then-bisulfite — the design most prone to bisulfite damage; the authors themselves note PBAT-style bisulfite libraries have less extreme AT/GC bias. No single-cell libraries are shown; "single cells" is a stated prospect, with 100 pg (~15 diploid human genomes) the demonstrated floor (synthesis for the genome-equivalent).

## Surprising or load-bearing bits

- **Coverage evenness, not just yield, is the gain**: WGBS concentrates reads on fewer CpGs, so at high depth thresholds it can *look* better while missing tens of millions of CpGs at low depth.
- **Drop-in compatibility** with bisulfite analysis tools is a deliberate design advantage over TAPS, whose output (modified bases read as T) needs dedicated callers.
- EM-seq is the conversion chemistry later adopted by single-cell protocols as an alternative to bisulfite (e.g. offered in sciMETv3; used by Cabernet as reported by Spix 2025 — where it showed incomplete CpY conversion) (synthesis).

## Concepts touched

- [[bisulfite-sequencing]] — the canonical alternative chemistry; same C/T logic without DNA degradation.
- [[5hmc]] — 5mC and 5hmC are not distinguished by standard EM-seq; separation requires an auxiliary 5hmC-only reaction.
- [[tet-enzymes]] — TET2 used as a reagent to oxidise 5mC to protected forms.
- [[taps]] — the contemporaneous TET + chemical method; differs in output encoding.
- [[sequencing-depth-and-coverage]] — CpGs covered as a function of depth threshold is the core comparison.

## Connections to other sources

- Sources of the bisulfite biases it targets: [[olova-2018-wgbs-library-bias]]; 5hmC behaviour in bisulfite: [[huang-2010-5hmc-bisulfite]]; TAPS family: [[chen-2025-sctaps-sccaps-plus]].
- Single-cell methylation protocols that use or are compared with enzymatic conversion: [[nichols-2025-scimetv3]] (bisulfite or EM-seq conversion), [[spix-2025-scdeep-mc]] (finds enzymatic-conversion Cabernet libraries with incomplete CpY conversion), [[shen-2026-splicool-seq]].
- PBAT single-cell bisulfite it contrasts with: [[smallwood-2014-natmethods]], [[clark-2017-scbs-seq-protocol]].
- Analysis compatibility: [[krueger-2011-bismark]].

## Open questions

- Whether DNA damage (e.g. FFPE) inhibits the enzymatic reactions is "not clear from the current data".
- Conversion completeness at single-cell input — where incomplete conversion cannot be averaged out — is not tested here and is disputed by later single-cell comparisons (see [[spix-2025-scdeep-mc]]).
- Lower-than-expected methylation in fully methylated XP12 DNA hints at density-dependent under-protection; relevance to dense methylated CpG islands is unexplored (synthesis).

## Related

- [[bisulfite-sequencing]] · [[taps]] · [[5hmc]] · [[40-Topics/dna-methylation]]
