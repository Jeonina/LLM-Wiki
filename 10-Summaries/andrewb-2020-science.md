---
type: summary
title: "Stergachis 2020 — Single-molecule regulatory architectures captured by chromatin fiber sequencing (Fiber-seq)"
source: "[[00-Sources/papers/Single-molecule regulatory architectures captured by chromatin fiber sequencing]]"
aliases: [Stergachis 2020, Fiber-seq paper, AndrewB_2020_Science]
tags: [fiber-seq, single-molecule, chromatin, m6A, methyltransferase, PacBio, foundational]
created: 2026-05-12
updated: 2026-05-12
---

**Citation:** Stergachis et al. (2020) — *Single-molecule regulatory architectures captured by chromatin fiber sequencing (Fiber-seq)* — *Science*. [DOI](https://doi.org/10.1126/science.aaz1646)

# Stergachis et al. 2020 — Fiber-seq foundational paper

> Andrew B. Stergachis, Brian M. Debo, Eric Haugen, L. Stirling Churchman, John A. Stamatoyannopoulos. *Science* **368**, 1449–1454 (26 June 2020). DOI: 10.1126/science.aaz1646.

## Thesis

Current chromatin-mapping methods (DNase-seq, ATAC-seq, MNase-seq, Hi-C) sample large populations of fibers and dissolve them. The primary architecture of individual multikilobase chromatin fibers — how regulatory DNA is actuated, how neighboring elements co-actuate, how nucleosomes are positioned, how TFs occupy single fibers — is invisible to those methods. The authors solve this by **using nonspecific N6-adenine DNA methyltransferases (m6A-MTases) to stencil protein-occupancy state onto the DNA itself, then reading the methylation pattern with PacBio long-read CCS sequencing**. The result, **Fiber-seq**, gives nucleotide-resolution chromatin maps of individual fibers up to ~30 kb long.

## Key claims

1. **Adenine is the right base for chromatin stenciling, not cytosine.** Adenine in eukaryotes is nearly devoid of endogenous methylation and occurs ~1 in every 2 bp without the CpG-style clustering and deserts. This makes nonspecific m6A-MTases ideal probes — they can mark any accessible adenine with no sequence-context bias and no confounding endogenous signal.
2. **Five m6A-MTases were screened** (Hia5, EcoGII, Btr192IV, EcoGI, Hin1523); all marked accessible DNA quantitatively. **Hia5 was the most efficient.** AdMTase-seq (short-read m6A-IP) showed the genomic m6A distribution mirrors DNase-I cleavage density (Hia5 vs DNase-seq R²=0.84).
3. **Fiber-seq operating point**: average fiber length 10.9 kb, max ~30 kb; 43× average coverage per DHS; nearly all fibers (99.7%) carry m6A marks. Two classes of methylase-accessible DNA (MAD) emerge: ~272 bp MADs that coincide with DHSs, and far more numerous ~67 bp MADs with regularized spacing — internucleosomal linkers. Nucleosome-wrapped DNA is m6A-free, consistent with the requirement for base-flipping by m6A-MTases.
4. **All-or-none actuation of regulatory DNA.** At any given DHS, only 81% of fibers carry an actuated open MAD; the remaining 19% are in a closed nucleosome-occupied state. The bulk DNase-seq signal at a DHS is the *frequency of actuation* across fibers, not a graded accessibility. TSS-distal DHSs are preferentially closed; promoter DHSs preferentially open.
5. **Co-actuation of neighboring elements in cis.** When a fiber spans two DHSs, the probability of both being actuated is significantly higher than the product of marginals, and the effect is distance-dependent (strongest for tightly clustered elements). Co-actuation is independent of whether the two DHSs share a TF — a physicochemical, not regulatory-network, phenomenon. This provides a single-molecule basis for the field's observed clustering of distal regulatory elements (super-enhancers, LCRs).
6. **Boundary model of nucleosome positioning.** Comparing fibers where the same DHS is open vs closed shows that the well-positioned nucleosome arrays around DHSs only exist on *actuated* fibers. So nucleosome positioning at regulatory elements is not encoded in the DNA sequence but emerges as a **boundary condition imposed by regulatory DNA actuation**.
7. **Single-molecule TF footprinting.** Within actuated MADs, m6A methylation is punctuated by short gaps that correspond to bound TFs at nucleotide resolution. For CTCF in K562 cells: **only 30% of accessible CTCF-bound elements (per bulk ChIP-seq) actually carry a CTCF footprint on any individual fiber**; 70% are accessible but TF-vacant. Elements with a higher fraction of CTCF-footprinted fibers participate in significantly more RAD21 ChIA-PET long-range interactions, linking single-molecule occupancy to function.

## Methods and evidence

- Drosophila S2 cells (primary system) + human K562 cells (validation). m6A-MTase treatment of intact nuclei → PCR-free PacBio CCS library → ≥10× resequencing per fiber for accurate base modification calling.
- Validation against bulk DNase-seq, ATAC-seq, CTCF ChIP-seq, RAD21 ChIA-PET.
- Code at Zenodo (doi:10.5281/zenodo.3743228); data at GEO GSE146942.

## Surprising / load-bearing

- The single most important insight for the [[somatic-mosaicism]] + epigenetic-state synthesis being assembled in this wiki is the **all-or-none actuation finding**: bulk accessibility signal at a DHS is a population frequency, not a continuous variable. This makes single-cell single-molecule chromatin profiling fundamentally different in interpretation from bulk, even when bulk data exists.
- The **boundary model of nucleosome positioning** flips a long-standing question (sequence-encoded vs activity-driven) decisively toward activity-driven for regulatory regions.
- The **CTCF "70% unbound but accessible" finding** is in tension with the textbook view that CTCF gating establishes loops; it argues that loops persist through TF unbinding cycles.

## Structural limitation acknowledged in the paper itself

Fiber-seq is a **bulk method**. m6A marks on DNA are erased during any DNA amplification (PCR, MDA, PTA), so chromatin stencils on a single cell's genome cannot be amplified up to sequencing depth. Each cell would yield ~1–2 fibers per locus. This is precisely the structural ceiling that [[10-Summaries/elliott-2025-naturebiotechnology]] (DAF-seq) breaks five years later by replacing methylation with deamination — sequence changes that survive amplification.

## Entities / concepts touched

[[20-Entities/andrew-b-stergachis]] · [[fiber-seq]] · [[single-molecule-footprinting]] · [[chromatin-actuation]] · [[chromatin-accessibility]] · [[atac-seq]] · [[dnase-seq]] · [[pacbio]] · [[long-read-sequencing]] · [[transcription-factor-motif]] · [[cis-regulatory-element]] · [[daf-seq]] (successor)

## Related summaries

- [[elliott-2025-naturebiotechnology]] — DAF-seq, the deamination-based successor that extends single-molecule chromatin profiling to single cells.
- [[10-Summaries/abdulhay-2020-samosa]] — SMRT-Tag, methodologically adjacent single-molecule footprinting.
- [[10-Summaries/mo-2023-stam-seq]] — STAM-seq, m6A-MTase chromatin footprinting in plants.

---
**Source:** [DOI](https://doi.org/10.1126/science.aaz1646) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/32587015/)

## Related

- [[40-Topics/chromatin-architecture]]
- [[40-Topics/long-read-sequencing]]
- [[40-Topics/single-cell-multiomics]]
