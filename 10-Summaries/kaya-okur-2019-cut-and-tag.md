---
type: summary
title: "Kaya-Okur et al. 2019 — CUT&Tag for efficient epigenomic profiling of small samples and single cells"
source: "[[00-Sources/papers/CUT&Tag for efficient epigenomic profiling of small samples and single cells]]"
source_kind: paper
author: "Hatice S. Kaya-Okur, Steven J. Wu, Christine A. Codomo, Erica S. Pledger, Terri D. Bryson, Jorja G. Henikoff, Kami Ahmad, Steven Henikoff (corresponding)"
published: 2019-04-29
ingested: 2026-08-10
doi: "10.1038/s41467-019-09982-5"
journal: "Nature Communications"
tags: [CUT&Tag, pA-Tn5, enzyme-tethering, histone-modifications, founding-method, low-input, single-cell, signal-to-noise]
entities: ["[[steven-henikoff]]"]
concepts: ["[[cut-and-tag]]", "[[cut-and-run]]", "[[chip-seq]]", "[[tn5-tagmentation]]", "[[chic-seq]]", "[[atac-seq]]", "[[icell8-nanowell]]"]
topics: ["[[histone-modifications]]"]
---

**Citation:** Kaya-Okur et al. (2019) — *CUT&Tag for efficient epigenomic profiling of small samples and single cells* — *Nature Communications* 10, 1930. [DOI](https://doi.org/10.1038/s41467-019-09982-5)

# Kaya-Okur 2019 — CUT&Tag

> The founding CUT&Tag paper. An antibody binds a chromatin protein in situ in permeabilized, **unfixed** cells; a protein A–Tn5 fusion is tethered to it; Mg²⁺ activates tagmentation, inserting sequencing adapters directly at the target. Live cells to sequencing-ready library, one tube, one day — with signal-to-noise that makes 2 million reads do the work of 20 million ChIP-seq reads.

## Key claims

- Chain of reasoning from prior art: ChIP-seq suffers low signal, high background, crosslinking-induced epitope masking, and needs many cells. CUT&RUN (pA-MNase, from Laemmli's ChIC) fixes signal-to-noise but requires end polishing and adapter ligation afterward, and **releases fragments into the supernatant — which is why it does not adapt to single-cell platforms.** CUT&Tag keeps fragments inside the nucleus because Tn5 stays bound to the DNA it tagments.
- Protocol: primary antibody → secondary antibody (to raise local antibody concentration) → excess pA-Tn5 preloaded with adapters → stringent washes → Mg²⁺ activation → PCR. Cells immobilized on Concanavalin A magnetic beads so every step is one tube. *E. coli* tracer DNA carried over from transposase production serves as the normalization spike-in.
- At matched 8M reads, ChIP-seq is background-dominated while CUT&RUN and CUT&Tag are clean; ChIP-seq's H3K4me1 dynamic range is **~1/20 of CUT&Tag's**.
- Efficiency: **~2 million CUT&Tag reads ≈ 8 million CUT&RUN ≈ 20 million ChIP-seq**. Only CUT&Tag reaches FRiP 0.6.
- H3K4me2 CUT&Tag recovers ATAC-seq peaks with higher read counts — active/accessible chromatin is capturable via a histone mark.
- RNAPII S2/5p CUT&Tag matches PRO-seq occupancy, validating against a method with no shared assumptions.
- **The Tn5 background is informative, not just noise.** Untethered pA-Tn5 binds exposed DNA, so every CUT&Tag run contains a low-level ATAC-like signal. For NPAT, ~99% of reads land at histone-gene promoters with a minor accessible-site distribution; for CTCF, read depth alone separates ~5,600 true sites at 1% FDR, and only the high-signal class carries the CTCF motif (E = 2.1 × 10⁻⁶⁹). The authors propose modelling both distributions for "de novo multi-omic CUT&Tag."
- Resolution: CTCF footprint of **~80 bp** over the motif (vs ~45 bp MNase protection in CUT&RUN).
- Input range: essentially identical H3K27me3 profiles from 100,000 down to **60 cells** (~1,500-fold); yield scales with cell number.
- **scCUT&Tag**: all steps through tagmentation done in bulk, then single cells dispensed into an ICELL8 5,184-nanowell chip, imaged to confirm singlets, indexed by well-specific primer pairs, pooled. 956 H3K27me3 and 808 H3K4me2 K562 cells; aggregate vs bulk Pearson r = 0.89 (K562) and 0.85 (H1). Single H1 vs K562 cells are discriminated with high efficiency; misassigned cells are the sparsest ones.

## Methods / evidence

Direct method-vs-method comparison at matched read depth with the *same antibody* throughout — the design choice that makes the signal-to-noise claims credible. Orthogonal validation via PRO-seq for RNAPII and motif enrichment for CTCF. Replicate correlation for reproducibility. Peak-calling efficiency measured as FRiP across a downsampling series.

## Surprising or load-bearing bits

- **Feature breadth rescues single-cell sparsity.** The authors state it directly: features range from ~5 nucleosomes (H3K4me2) to hundreds (H3K27me3 domains), and that breadth "assists the detection of chromatin features even with sparse sampling from individual cells." This is why broad repressive marks were the first to work at single-cell scale ([[wu-2021-sccut-tag]], [[zhang-2022-sccut-tag-pro]]) and why narrow TF binding remains hard per cell.
- The bulk-tagmentation-then-split architecture is the structural reason CUT&Tag scales to droplets while single-cell ChIP-seq ([[rotem-2015-drop-chip]]) and scCUT&RUN do not: adapters are added *before* cells are separated.
- The Tn5 accessibility background is a **standing interpretive caveat** for every downstream scCUT&Tag dataset — a fraction of reads in any run is ATAC signal, and salt stringency controls how much. [[wu-2021-sccut-tag]] treats this as a QC axis explicitly.
- The closing prediction — "barcoding of adapters will allow multiple epitopes to be simultaneously profiled in single cells" — is exactly [[gopalan-2022-multi-cut-and-tag|Multi-CUT&Tag]] and [[multi-tag]].
- Unfixed, in-situ, single-tube means CUT&Tag can be automated in a core facility — the paper argues the real virtue is not cost but **minimization of batch and handling effects**, which is what makes clinical assays possible.

## Entities mentioned

- [[steven-henikoff]] — corresponding author; CUT&RUN → CUT&Tag → single-cell CUT&Tag lineage.
- Kami Ahmad, Jorja Henikoff — co-developers; Steven J. Wu goes on to lead [[wu-2021-sccut-tag]].

## Concepts touched

- [[cut-and-tag]] — this is the founding source for the page.
- [[cut-and-run]] / [[chic-seq]] — direct predecessors; the fragment-release limitation is the stated reason for moving to tagmentation.
- [[tn5-tagmentation]] — pA-Tn5 fusion; also the source of the accessibility background.
- [[icell8-nanowell]] — the imaging-verified singlet platform used here.

## Connections to other sources

- Predicted-and-fulfilled by [[zhu-2020-multimodal-power-of-many]], which named pA-Tn5 as the way to add histone marks to scalable joint assays.
- Scaled to droplets and tissue in [[wu-2021-sccut-tag]] and [[bartosovic-2021-sccut-tag]]; multiplexed with protein in [[zhang-2022-sccut-tag-pro]]; multi-epitope in [[gopalan-2022-multi-cut-and-tag]] and [[yeung-2023-scchix-seq]].
- Contrast on the nuclease side: [[ku-2019-scchic-seq]] (scChIC-seq), [[sarah-2019-cell]]; see [[mnase-vs-tn5-chromatin]].
- Peak calling for broad domains uses SEACR ([[meers-2019-seacr|Meers 2019 (SEACR)]]), developed in the same lab for exactly this data type.

## Open questions

- Transcription-factor CUT&Tag in *single* cells is not demonstrated here — only bulk CTCF/NPAT. Whether per-cell TF occupancy is recoverable at all remains largely open in this corpus.
- The proposed two-distribution model separating tethered signal from accessibility background was never, as far as this corpus shows, implemented as a standard tool.

## Related

- [[cut-and-tag]] · [[wu-2021-sccut-tag]] · [[zhang-2022-sccut-tag-pro]] · [[histone-modifications]]
