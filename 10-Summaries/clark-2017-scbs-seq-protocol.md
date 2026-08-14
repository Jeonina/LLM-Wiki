---
type: summary
title: "Clark et al. 2017 — Genome-wide base-resolution mapping of DNA methylation in single cells using single-cell bisulfite sequencing (scBS-seq) [protocol]"
source: "[[00-Sources/papers/Genome-wide base-resolution mapping of DNA methylation in single cells using single-cell bisulfite sequencing (scBS-seq)]]"
source_kind: paper
author: "Stephen J. Clark, Sébastien A. Smallwood, Heather J. Lee, Felix Krueger, Wolf Reik, Gavin Kelsey (corresponding)"
published: 2017-02-09
ingested: 2026-08-13
doi: "10.1038/nprot.2016.187"
journal: "Nature Protocols 12:534–547"
tags: [scBS-seq, PBAT, post-bisulfite-adaptor-tagging, protocol, preamplification, SPRI, automation, random-priming]
entities: ["[[wolf-reik]]", "[[heather-lee]]"]
concepts: ["[[scbs-seq]]", "[[bisulfite-sequencing]]", "[[gt-seq]]", "[[read-alignment]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[dna-methylation]]", "[[single-cell-multiomics]]"]
---

**Citation:** Clark, Smallwood, Lee, Krueger, Reik & Kelsey (2017) — *Genome-wide base-resolution mapping of DNA methylation in single cells using single-cell bisulfite sequencing (scBS-seq)* — *Nature Protocols* 12, 534–547. [DOI](https://doi.org/10.1038/nprot.2016.187)

# Clark 2017 — scBS-seq protocol

> The step-by-step protocol for [[smallwood-2014-natmethods|scBS-seq]], with the post-2014 optimisations. The conceptual core is **PBAT — post-bisulfite adaptor tagging**: invert the order of bisulfite treatment and adaptor ligation so that adaptors are added *after* the DNA has already been fragmented and converted, and you stop losing every molecule whose adaptor was destroyed by the conversion. On top of PBAT, the single-cell modification is a **five-round preamplification** — five independent chances to capture each genomic location.

## Key claims

- **PBAT is the enabling inversion.** In conventional BS-seq, adaptor-tagged molecules are bisulfite-treated and most are lost to conversion-induced degradation. PBAT (Miura et al.) uses bisulfite to do both the conversion *and* the fragmentation, tagging afterwards — recovering far more of the genome from limited input. It was demonstrated at 100 ng, then ~1,000 mouse oocytes, then ~100 human oocytes, before this line pushed it to one cell.
- **Five rounds of random priming with intermediate heat denaturation is the single-cell modification.** Each round is another opportunity to prime any given locus, and it generates multiple copies per fragment so that downstream purification does not collapse library complexity. This is Steps 6–12; a final PCR (Steps 33–34) brings the library to sequenceable quantity.
- **Random hexamers are recommended over the original tetramers or the scBS-seq nonamers.** Hexamers increased yield over tetramers and require less trimming than nonamers; the random segment is 25% of each base. Reduced guanidine to better capture converted sequence was tested and did not help (reported as unpublished data).
- **Lysis and bisulfite conversion happen on the raw lysate — no DNA purification.** RLT Plus buffer lyses and denatures protein in one step, removing the proteinase K digestion, shortening the protocol and cutting pipetting steps and contamination routes.
- **Three SPRI purifications, "with-bead" throughout.** The same beads stay in the same tubes from the exonuclease I step onward, eliminating transfer steps. Replacing the original streptavidin capture of preamplification products with an extra SPRI saved 2 h of hands-on time.
- **Exonuclease I after preamplification** removes leftover oligos that would otherwise form adaptor dimers during second-adaptor tagging.
- **Coverage: up to ~50% of CpGs in a single mouse cell.** The whole mouse oocyte methylome was reconstructed by merging <20 single cells; 12–14 single oocytes suffice.
- **Automation-ready.** The protocol is compatible with an Agilent Bravo liquid handler, allowing 96 samples in parallel; bead-based post-conversion purification (rather than columns) is required for the automated route.
- **Compatible with parallel RNA-seq from the same cell** via [[macaulay-2015-gt-seq|G&T-seq]], which is how the Reik/Kelsey line reached joint methylome–transcriptome analysis.
- **Timing**: library prep 2–3 d; sequencing, mapping, QC 2–11 d.

## Methods / evidence

A protocol paper, not a discovery paper: its evidence is the accumulated optimisation experience of the originating lab. The comparative claims (hexamer > tetramer, SPRI > streptavidin, no benefit from reduced guanidine) are reported as lab experience, some explicitly as unpublished data.

## Surprising or load-bearing bits

- **"Reorder the reactions" is a bigger lever than any reagent change.** PBAT's inversion is why single-cell bisulfite sequencing exists at all — a reminder that protocol *topology*, not just chemistry, sets the input floor.
- **~50% CpG coverage per cell is the high-water mark for single-cell methylation**, and it comes from the lowest-throughput method in the family. The tradeoff against [[mulqueen-2018-sci-met|sci-MET]]'s ~1% and [[zhang-2023-drop-bs|Drop-BS]]'s comparable sparsity is the central design decision in single-cell methylome work, and this protocol defines one end of it.
- **The "merge <20 cells to reconstruct a rare cell type's methylome" strategy** is the practical answer to sparsity for homogeneous populations, and it predates and underlies the [[pseudo-bulk|pseudobulk]] convention now universal in the field.
- **Automation compatibility is a stated design goal in a 2017 protocol** — unusual, and it is what made scBS-seq viable for the multi-hundred-cell studies that followed.
- **Sliding-window averaging for cross-cell comparison** is recommended here as the analysis approach; [[kremer-2024-methscan]] later shows tile-averaging dilutes signal and proposes VMR-based discovery instead. The protocol's own analysis advice is the thing that was superseded, not its chemistry.

## Entities mentioned

- [[wolf-reik]] — corresponding author; epigenetic reprogramming and single-cell multi-omics.
- [[heather-lee]] — coauthor; scBS-seq development.

## Concepts touched

- [[scbs-seq]] — this is the definitive protocol source for the concept.
- [[bisulfite-sequencing]] — PBAT as the low-input adaptation.
- [[gt-seq]] — the route by which scBS-seq becomes a multi-omic assay.

## Connections to other sources

- Founding paper this protocol operationalises: [[smallwood-2014-natmethods]].
- The parallel-modality extension: [[macaulay-2015-gt-seq]], [[macaulay-2016-gt-seq-protocol]]; the three-layer successor [[clark-2018-scnmt-seq]] (scNMT-seq) from the same authors.
- The reduced-representation alternative, and its protocol: [[guo-2013-scrrbs]], [[guo-2015-scrrbs-protocol]] — which argues its CGI coverage is better despite lower total CpG coverage.
- Higher-throughput descendants that trade coverage for cell count: [[luo-2017-snmc-seq]], [[mulqueen-2018-sci-met]], [[nichols-2022-scimet-v2]], [[zhang-2023-drop-bs]].
- Alignment software from a coauthor: [[krueger-2011-bismark]].
- Analysis methods for the resulting sparse matrices: [[angermueller-2017-genomebiol]], [[kapourani-2019-melissa]], [[kapourani-2021-scmet]], [[kremer-2024-methscan]].

## Open questions

- **Several optimisation claims rest on unpublished data** (the guanidine test explicitly). The hexamer-vs-nonamer recommendation is not accompanied by a quantitative comparison in this source.
- Bisulfite conflates 5mC and 5hmC; the protocol does not address the distinction (later handled by [[chen-2025-sctaps-sccaps-plus]] and [[bai-2024-simple-seq]]).
- Success rate per attempted cell is described as improved but not quantified here.

## Related

- [[smallwood-2014-natmethods]] · [[guo-2015-scrrbs-protocol]] · [[scbs-seq]] · [[40-Topics/dna-methylation]]
