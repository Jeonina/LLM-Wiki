---
type: summary
title: "Skene & Henikoff 2017 — An efficient targeted nuclease strategy for high-resolution mapping of DNA binding sites"
source: "[[00-Sources/papers/An efficient targeted nuclease strategy for high-resolution mapping of DNA binding sites]]"
source_kind: paper
author: "Peter J Skene, Steven Henikoff (corresponding)"
published: 2017-01-16
ingested: 2026-10-07
doi: "10.7554/eLife.21856"
journal: "eLife 6:e21856"
tags: [CUT&RUN, ChIC, pA-MNase, transcription-factor-binding, CTCF, chromatin-profiling, spike-in-normalization, native-ChIP, 3D-contacts, Henikoff-lab]
entities: ["[[20-Entities/steven-henikoff]]"]
concepts: ["[[30-Concepts/cut-and-run]]", "[[30-Concepts/chip-seq]]", "[[30-Concepts/chic-seq]]", "[[30-Concepts/damid]]", "[[30-Concepts/cut-and-tag]]", "[[30-Concepts/chia-pet]]", "[[30-Concepts/transcription-factor-motif]]", "[[30-Concepts/chromatin-loop]]"]
topics: ["[[40-Topics/histone-modifications]]", "[[40-Topics/chromatin-architecture]]", "[[40-Topics/3d-genome]]"]
---

**Citation:** Skene & Henikoff (2017) — *An efficient targeted nuclease strategy for high-resolution mapping of DNA binding sites* — *eLife* 6:e21856. [DOI](https://doi.org/10.7554/eLife.21856)

# Skene 2017 — CUT&RUN

> CUT&RUN (Cleavage Under Targets and Release Using Nuclease) turns the long-unused ChIC idea — antibody plus protein A–MNase (pA-MN) — into a genome-wide sequencing assay. Unfixed nuclei are immobilised on concanavalin-A magnetic beads, incubated with antibody and pA-MN, and calcium is added **at 0 °C**; MNase cuts on both sides of the bound protein and the small protein–DNA complex **diffuses out of the nucleus into the supernatant**, while the bulk genome stays in the pellet. Because only targeted fragments are released, background is near zero and **~1/10th the sequencing depth of ChIP** suffices. The paper's pitch is replacement: "in all important respects CUT&RUN provides an attractive alternative to ChIP-based strategies."

## Key claims

- **Limit digestion is fast and time-insensitive.** For yeast Abf1 and Reb1 (~2–3 million mapped paired-end reads per sample), fragment size distributions were "virtually superimposable" below ~150 bp from 4 s to 128 s — digestion time is not a critical parameter. TF fragments peak at ~100 bp; H2A (nucleosomal) at ~150 bp, so ≤120 bp and ≥150 bp classes are analysed separately.
- **Sensitive and specific**: against motif sets derived independently from ORGANIC ChIP (1,899 Abf1 and 1,413 Reb1 motifs), >90% of TF sites were occupied over the motif; Abf1 fragments showed negligible occupancy at Reb1-only sites and vice versa. CUT&RUN matched ORGANIC ChIP-seq dynamic range for both TFs "with ~10 fold fewer paired-end reads"; standard crosslinked ChIP-seq was inferior.
- **Near base-pair footprints**: ~20 bp protected footprints for Abf1/Reb1, with a ~10 bp sawtooth cleavage periodicity on flanking DNA (one face of the B-form helix accessible to tethered MNase). For CTCF in K562, cut-site "tram-tracks" 44 bp apart, with a predominant single base-pair cut on each side, stable over a ~300-fold digestion time range.
- **Large, rare, insoluble complexes**: Mot1 and Sth1 (RSC) mapped by extracting total DNA and removing large fragments; Mot1 with ~15% of ORGANIC's reads. The Cse4 centromeric nucleosome (~1% the molar abundance of Abf1/Reb1, part of the insoluble kinetochore) was mapped at all 16 yeast centromeres with resolution 4-fold better than standard X-ChIP; **insoluble H2A co-localises with Cse4**, which the authors say "directly addresses the continuing controversy" over centromeric nucleosome composition. The >90% A+T centromere surviving a >100-fold digestion range argues against an MNase AT bias.
- **Human TFs and heterochromatin**: CTCF, Myc, Max and H3K27me3 in K562. At 10 million reads, CUT&RUN had higher dynamic range than ENCODE X-ChIP-seq and ChIP-exo; for Max (same antibody as ENCODE) it identified many more sites, which X-ChIP data showed occupancy at on re-inspection. H3K27me3 fragments are released from intact nuclei — pA-MN accesses compacted chromatin. **Low temperature is required**: a no-antibody control showed undetectable background only when cleavage was done cold.
- **Direct vs indirect sites**: a new native ChIP protocol found 2,298 high-motif-score (direct) CTCF sites; CUT&RUN found ~22,000 sites also present in X-ChIP. 91% of direct sites were in CTCF ChIA-PET data, and 43% of those ChIA-PET fragments contacted an indirect site — so CUT&RUN + native ChIP maps 3D contact sites and their directionality at near base-pair resolution.
- **Quantitative with spike-in**: adding a constant small amount of *Drosophila* DNA after cleavage made cleavage events proportional to starting cell number (600,000 to 10 million K562 cells) and revealed a ~4-fold increase in cleavage over a time course that internal normalisation hid. Mapping ~22,000 CTCF sites from 600,000 cells is estimated to match ultra-low-input native ChIP-seq sensitivity (typically ~5,000 cells for abundant marks) but with near base-pair rather than ~2 kb resolution.

## Methods / evidence

Yeast: the same FLAG-tagged strains, nuclei preparations, anti-FLAG antibody and library protocol as the ORGANIC ChIP-seq comparison (Kasinathan 2014) — a controlled head-to-head; a rabbit anti-mouse secondary is needed because protein A binds mouse IgG weakly (the secondary amplifies cleavage 1–2 orders of magnitude). Human: centrifugation- or bead-based protocol on K562 nuclei, compared against ENCODE X-ChIP-seq, CTCF ChIP-exo and ChIA-PET/Hi-C, downsampled to 10 million reads. 25-cycle paired-end HiSeq 2500; peaks by a threshold method (99.5th percentile). Appendices give step-by-step protocols, including the new native ChIP.

Weight: strong for resolution and signal-to-noise — the yeast comparison controls nearly every variable. Low-input claims here are modest (≥600,000 cells); the "direct vs indirect" interpretation of CTCF sites relies on native ChIP sensitivity being complete, which is argued but not proven.

## Surprising or load-bearing bits

- **Why it works: zero-order cleavage + diffusion.** Tethered MNase is pre-positioned, so cutting is near-instant on ice; doing it cold stops released fragments and free MNase from wandering. Background in ChIP comes from pulverising the whole genome; CUT&RUN never solubilises what it does not cut.
- **Low background breaks standard normalisation.** ChIP normalises to its genome-wide background; CUT&RUN has almost none, so a heterologous DNA spike-in becomes necessary — a quirk inherited by the CUT&Tag family. (synthesis)
- **CUT&RUN peaks include indirect (3D-contact) sites.** Not every CUT&RUN CTCF peak is a CTCF motif — a caution for anyone treating CUT&RUN/CUT&Tag peaks as direct binding.
- ChIC had been published 12 years earlier and, per the authors, never used; the five modifications (beads, native nuclei, 0 °C, solubility fractionation, paired-end sequencing) are what made it practical.

## Concepts touched

- [[cut-and-run]] — the founding paper. Note the wiki concept page's "~100 cells" input figure is *not* supported by this source, which used 600,000–10 million K562 cells.
- [[chic-seq]] — CUT&RUN is a re-engineered ChIC (Schmid 2004).
- [[chip-seq]] — benchmarked against X-ChIP, ORGANIC native ChIP and ChIP-exo.
- [[damid]] — enzyme-tethering predecessor whose resolution is limited by GATC distribution; flexible tethering reaches >1 kb like DamID.
- [[chia-pet]] / [[chromatin-loop]] — CUT&RUN + native ChIP distinguishes direct CTCF sites from contact partners.
- [[cut-and-tag]] — later Henikoff-lab successor that replaces MNase with Tn5 (synthesis — not in this source).

## Connections to other sources

- Successor assays in the same lab: [[kaya-okur-2019-cut-and-tag]] (Tn5 tethering), [[janssens-2023-scicut-tag]]; peak calling for these sparse-background data: [[meers-2019-seacr]].
- Single-cell ChIC descendants: [[ku-2019-scchic-seq]], [[yeung-2023-scchix-seq]].
- Later tethered-enzyme designs that write marks instead of cutting: [[shi-2026-dechic-seq]] (pA-DddA deamination; uses embryo CUT&RUN data as a reference), [[chi-2026-dd-seq]], [[altemose-2022-dimelo-seq]].
- CTCF-mediated looping context: [[li-2014-chia-pet]], [[dixon-2012-tads]].

## Open questions

- How low can input go? Not tested below 600,000 cells here.
- Are CUT&RUN-only (non-motif) CTCF peaks always 3D contacts, or partly accessibility-driven cleavage by tethered MNase? The paper shows correlation with Hi-C/ChIA-PET, not causation.
- Spike-in DNA quantifies released fragments but not antibody efficiency differences between samples.

## Related

- [[cut-and-run]] · [[kaya-okur-2019-cut-and-tag]] · [[20-Entities/steven-henikoff]] · [[40-Topics/histone-modifications]]
