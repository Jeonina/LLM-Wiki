---
type: summary
title: "Rooijers et al. 2019 — scDam&T-seq: simultaneous protein–DNA contacts + transcriptome in single cells"
source: "[[00-Sources/papers/Simultaneous quantification of protein–DNA contacts and transcriptomes in single cells]]"
source_kind: paper
author: "Koos Rooijers, Corina M. Markodimitraki, Franka J. Rang, Sandra S. de Vries, Alex Chialastri, Kim L. de Luca, Dylan Mooijman, Siddharth S. Dey, Jop Kind (corresponding)"
published: 2019-06-17
ingested: 2026-05-15
doi: "10.1038/s41587-019-0150-y"
journal: "Nature Biotechnology"
tags: [single-cell, multi-omics, DamID, scDamID, scDamT-seq, lamina, LAD, nuclear-periphery, chromatin-accessibility, polycomb, X-inactivation]
entities:
  - "[[20-Entities/jop-kind]]"
  - "[[20-Entities/siddharth-dey]]"
concepts:
  - "[[30-Concepts/damid]]"
  - "[[30-Concepts/scdamt-seq]]"
  - "[[30-Concepts/lamina-associated-domains]]"
  - "[[30-Concepts/nuclear-lamina]]"
  - "[[30-Concepts/chromatin-accessibility]]"
  - "[[30-Concepts/single-cell-multiomics]]"
topics:
  - "[[40-Topics/3d-genome]]"
  - "[[40-Topics/chromatin-architecture]]"
  - "[[40-Topics/single-cell-multiomics]]"
---

**Citation:** Rooijers et al. (2019) — *scDam&T-seq: simultaneous protein–DNA contacts + transcriptome in single cells* — *Nature Biotechnology*. [DOI](https://doi.org/10.1038/s41587-019-0150-y)

# Rooijers et al. 2019 — scDam&T-seq

> Thesis: cell-to-cell heterogeneity in protein–DNA binding is causally linked to gene expression variability, but no method jointly measures both in the same cell. scDam&T-seq fuses single-cell DamID (Dam-fusion protein → m6A at GATC near a protein-of-interest) with CEL-Seq2 mRNA capture, using **linear amplification by in vitro transcription** to amplify gDNA and cDNA in one reaction. This unlocks per-cell coupling of genome–nuclear-lamina contacts, chromatin accessibility, or polycomb (RING1B) occupancy to the transcriptome.

## Key claims

- **Methodological linchpin: linear amplification.** Replacing PCR with T7 IVT on DamID-adapter-ligated fragments enables (i) compatibility with mRNA IVT in the same reaction, (ii) unbiased recovery, (iii) >100× throughput via robotic 384-well processing, (iv) UMI compatibility for both gDNA and mRNA reads. Median 42k unique DamID reads/cell + ~2,300 detected genes/cell ([DOI](https://doi.org/10.1038/s41587-019-0150-y)).
- **scDam&T-seq reproduces scDamID and CEL-Seq at the population level** (DamID CF concordance r=0.97; mESC Dam-LMNB1 matches bulk LAD coordinates of Peric-Hupkes 2010), while gaining single-cell joint coverage.
- **Three modes from one assay**:
  1. **Dam-LMNB1** → lamina contact frequencies; defines per-cell LAD attachment.
  2. **Untethered Dam** → accessible-chromatin proxy; gives sharp peaks at active TSSs/enhancers, 174-bp nucleosome periodicity at CTCF sites, comparable to scNMT-seq at 30× shallower depth.
  3. **Dam-RING1B** → single-cell polycomb (PRC1) binding; recapitulates bulk ChIP-seq genome-wide and on HOX clusters.
- **Single-cell causal coupling, lamina ↔ transcription.** Genome-wide negative log2FC of expression between Dam-LMNB1 contact vs no-contact states (and the symmetric positive coupling for untethered Dam). Critically, the negative association is restricted to **low-CF facultative LADs (fLADs, H3K27me3-enriched)** — not the H3K9me3-rich constitutive cLADs. Implication: it's the dynamic fLADs that mediate transcriptional responses to NL release, not the static heterochromatin floor.
- **X-inactivation in single cells.** In differentiating F1 hybrid (129/Sv:CAST/EiJ) mESCs, allelic RING1B enrichment marks the inactive X allele in the same cell where transcription is allelically biased — the earliest measurable XCI event, consistent with Zylicz 2019's H2AK119ub priority over H3K27me3.

## Methods / evidence

- **Cell systems**: haploid KBM7 (Dam-LMNB1 / Dam controls, Shield1-inducible); F1 hybrid 129/Sv:CAST/EiJ mESCs (AID-Dam-LMNB1, AID-Dam, AID-Dam-RING1B; 12 h auxin washout induction); 2i vs serum mESC clusters.
- **Chemistry**: lyse → RT (CEL-Seq2 primer) → 2nd-strand cDNA synthesis → DpnI digest of m6A-GATC → adapter ligation to gDNA → pool 384 wells → IVT amplification → Illumina paired-end. Both gDNA and cDNA carry UMIs.
- **Computational**: 100-kb bins, observed/expected (OE) framework adapted from Kind 2015; binary "contact" defined OE≥1; log2FC in expression between contact vs no-contact cells per bin; allelic biases resolved with 129/Sv and CAST/EiJ pseudo-genomes.
- **Comparisons**: vs scDamID (Kind 2015), vs CEL-Seq, vs scNMT-seq (Clark 2018), vs bulk RING1B ChIP-seq. Reduced complexity vs scDamID (~4×) offset by 100× throughput.

## Surprising or load-bearing bits

- **fLAD-only coupling**: cell-to-cell expression sensitivity to NL contact is concentrated in *low-CF, H3K27me3-marked, cell-type-specific* LADs. Constitutive LADs (cLADs, H3K9me3) are inert in this analysis. This is the cleanest single-cell evidence that lamina detachment is a *regulatable* axis, not a uniform repression state.
- **Untethered Dam outperforms DNase at lowly expressed regions** because Dam marks gene bodies (H3K36me3-rich), not just promoters — extends accessibility readout from peaks to gene units.
- **TAD-scoped accessibility changes**: 2i→serum, *Peg10* TSS accessibility rise extends across its entire TAD; differential accessibility variances are higher within TADs than randomized control. Single-cell accessibility respects 3D-domain boundaries.
- **Reaction architecture innovation** — gDNA digestion (DpnI) and adapter ligation happen *after* mRNA reverse transcription in the same well without intermediate cleanup. Loss minimization here is what makes the multi-omic readout possible at scale.

## Entities mentioned

- [[20-Entities/jop-kind]] — corresponding author; PI of scDamID lineage (Kind 2013, 2015); Hubrecht Institute / Oncode.
- [[20-Entities/siddharth-dey]] — co-senior; UCSB Chemical Engineering; G&T-seq (Dey 2015) prior work.
- Bas van Steensel — DamID inventor (van Steensel 2000, 2001); ancestral citation chain.

## Concepts touched

- [[30-Concepts/damid]] — extends to linear-amplification + multi-omic compatibility; first joint genome-protein + transcriptome single-cell readout.
- [[30-Concepts/scdamt-seq]] — defines the method.
- [[30-Concepts/lamina-associated-domains]] — operationalizes fLAD vs cLAD distinction at single-cell resolution; only fLADs are transcriptionally responsive to NL detachment.
- [[30-Concepts/nuclear-lamina]] — single-cell measurement of genome–NL contact heterogeneity in cycling mammalian cells.
- [[30-Concepts/chromatin-accessibility]] — untethered Dam as an alternative to ATAC/DNase, with gene-body sensitivity advantage.
- [[30-Concepts/single-cell-multiomics]] — extends the genome+RNA single-cell family (G&T-seq, scNMT-seq) into the protein–DNA contact axis.

## Connections to other sources

- **Extends** [[10-Summaries/chenghang-2012-science]] (Kind 2013/2015 lineage) — same chemistry, IVT amplification rescues throughput and adds RNA.
- **Echoes / complements** [[10-Summaries/clark-2018-scnmt]] (scNMT-seq) — comparable joint readout, but scDam&T-seq uses contact-based (Dam) rather than chemical (bisulfite/NOMe) accessibility, at ~30× shallower sequencing depth.
- **Echoes** [[10-Summaries/nagano-2013-nature]] and the scHi-C family — orthogonal angle on the same question (how spatial genome organization varies per cell and links to expression).
- **Bridges** [[40-Topics/3d-genome]] and [[40-Topics/chromatin-architecture]] via the NL axis — a layer that pure Hi-C–based methods miss.
- **Future link**: if 5-base / 6-base CUT&Tag-style joint readouts ([[10-Summaries/tavares-2026-6base-cutandtag]]?) eventually pair with single-cell DamID, the genome–protein–histone-mark triad becomes addressable in one cell.

## Open questions

- Why is **lamina-only** the contact axis that gates fLAD activity? The 2026 question is whether other peripheral compartments (nucleolus, speckles) show similar single-cell coupling — addressable with scDam&T-seq using nucleolar / SC35-fusion Dam.
- The 12-h Dam labeling window averages contact histories — does it obscure short-lived contacts that may be the *causal* trigger of expression changes? Inducible / time-resolved variants are needed.
- Throughput vs depth tradeoff vs scDamID: is the 4× lower DamID complexity a meaningful biological limitation, or just a sequencing-depth artifact?

---
**Source:** [DOI](https://doi.org/10.1038/s41587-019-0150-y) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/31209373/) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6609448/)

## Related

- [[30-Concepts/damid]] · [[30-Concepts/scdamt-seq]] · [[30-Concepts/lamina-associated-domains]] · [[30-Concepts/nuclear-lamina]]
- [[10-Summaries/de-luca-2021-scdamid-protocol]] — Methods Mol Biol protocol from the same lab
- [[10-Summaries/mali-2025-conformational-heterogeneity]] — uses lamina-DamID data downstream as a 3D-modeling constraint
- [[40-Topics/3d-genome]] · [[40-Topics/chromatin-architecture]] · [[40-Topics/single-cell-multiomics]]
