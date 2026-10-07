---
type: summary
title: "Abdulhay et al. 2020 — Massively multiplex single-molecule oligonucleosome footprinting (SAMOSA)"
source: "[[00-Sources/papers/Massively multiplex single-molecule oligonucleosome footprinting.pdf]]"
source_quality: full
source_sha256: "ce5de58747f4e6d2557485a5efbd0ad7685157196d4abb6f4486e1b40ea378ab"
source_kind: paper
author: "Nour J Abdulhay, Colin P McNally (co-first), Laura J Hsieh, Sivakanthan Kasinathan, Aidan Keith, Laurel S Estes, Mehran Karimzadeh, Jason G Underwood, Hani Goodarzi, Geeta J Narlikar, Vijay Ramani (corresponding)"
published: 2020-12-02
ingested: 2026-05-13
updated: 2026-10-07
doi: "10.7554/eLife.59404"
journal: "eLife 9:e59404 (Tools and Resources)"
aliases: ["Abdulhay 2020 SAMOSA", "SAMOSA"]
tags: [SAMOSA, single-molecule-footprinting, EcoGII, m6A, PacBio-SMRT, oligonucleosome, nucleosome-positioning, nucleosome-repeat-length, heterochromatin, K562, Ramani-lab, UCSF]
entities: ["[[20-Entities/vijay-ramani]]"]
concepts: ["[[30-Concepts/samosa]]", "[[30-Concepts/single-molecule-footprinting]]", "[[30-Concepts/pacbio]]", "[[30-Concepts/fiber-seq]]", "[[30-Concepts/chromatin-accessibility]]", "[[30-Concepts/transcription-factor-motif]]", "[[30-Concepts/clustering-algorithms]]", "[[30-Concepts/chromatin-phase-separation]]"]
topics: ["[[40-Topics/long-read-sequencing]]", "[[40-Topics/chromatin-architecture]]", "[[40-Topics/histone-modifications]]"]
---

**Citation:** Abdulhay, McNally et al. (2020) — *Massively multiplex single-molecule oligonucleosome footprinting* — *eLife* 9:e59404. [DOI](https://doi.org/10.7554/eLife.59404) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33263279/)

# Abdulhay 2020 — SAMOSA

> SAMOSA (single-molecule adenine methylated oligonucleosome sequencing assay) marks linker DNA on chromatin fibres with the nonspecific adenine methyltransferase **EcoGII** and reads the m6dA marks natively, from polymerase kinetics, on the **PacBio** single-molecule real-time platform. Applied in vivo, it starts from a light MNase digest of K562 nuclei. Oligonucleosomes are released into solution, methylated, and sequenced, so each read carries two signals: the MNase cut ends, which mark "barrier" protein-DNA contacts, and the m6dA footprint of nucleosomes along the molecule. The paper autocorrelates each molecule's methylation signal and clusters molecules with Leiden to sort fibres into seven "oligonucleosome patterns" by regularity and nucleosome repeat length (NRL). Its main biological claim is that every epigenomic domain is a heterogeneous mixture of regular and irregular fibres, and that domains differ only in the *relative usage* of these patterns. The most surprising case is constitutive heterochromatin, which is enriched for irregular fibres.

## Key claims

- **PacBio detects EcoGII m6dA on chromatin templates.** On in vitro arrays of nine Widom 601 repeats (~46 bp linkers), 33,594 molecules showed raised interpulse duration (IPD) only at accessible linker adenines. Called dyads matched expected 601 dyads with "median ±median absolute deviation [MAD] = 4 ± 2.97 bp". The NRL was 193 ± 7.40 bp from adjacent-dyad distances and 192 ± 1.30 bp per molecule, against an expected 193 bp. A small 10-mer sequence-context bias in IPD remained.
- **In vivo, one read carries two orthogonal signals.** K562 SAMOSA gave n = 1,855,316 molecules (two replicates of 926,458 and 936,755). Fragment lengths show the oligonucleosome ladder (2n, 3n, 4n, 5n…), and averaged m6dA shows phased nucleosomes from the MNase cut. The authors call it, to their knowledge, the first method to capture nucleolytic-cleavage and methylation footprints on the same molecule.
- **Seven oligonucleosome patterns genome-wide.** Molecules ≥500 bp were autocorrelated and Leiden-clustered (1,636,291 molecules). Each cluster held "6.54% (Cluster 4)–20.1% (Cluster 1)" of molecules, consistent across replicates. There are three irregular clusters (IRS = irregular-short, IRL = irregular-long, IR170) and four regular ones with single-molecule NRLs from "~172 bp" to ">200 bp" (NRL172, NRL187A/B, NRL192). Mean methylation per molecule was largely invariant across clusters, so clusters are not driven by methylation level. More autocorrelogram peak calls were "missing" in irregular clusters.
- **TF motifs: MNase sees footprints, methylation does not.** At predicted K562 sites for CTCF, NRF1, REST, PU.1, c-MYC and GATA1, MNase cut ends accumulated next to motifs, with phased nucleosomes around CTCF, REST and PU.1. m6dA showed raised accessibility at CTCF, NRF1 and c-MYC motifs, but no TF "footprints". The authors put this down to TF turnover during solubilisation or to sterics, since EcoGII is "roughly twice the molecular weight" of MNase.
- **13 accessibility states around motifs.** Leiden clustering of 500 bp windows gave methyltransferase-resistant (MR), nucleosome-occluded (NO1–8), stochastically accessible (SA1–2), accessible (A) and hyper-accessible (HA) states. State A was depleted in every GC/repeat-matched control set and enriched at bona fide motifs for most TFs. PU.1 and GATA1 were the exceptions, which fits their ability to bind nucleosomal DNA. The authors propose a "site exposure" model: NO/SA registers become A when a TF binds, then HA.
- **Epigenomic domains differ by pattern usage, not by uniform structure.** Shifts in median NRL were small: "a shift of ~5 bp (180 bp vs. 185 bp) in H3K9me3 chromatin" and "~4 bp (182 bp vs 186 bp) for H3K36me3" against matched controls. H3K4me3 chromatin had fewer successful NRL calls (78.0% vs 88.6%). H3K4me3 and H3K4me1 domains were enriched for irregular IRL and IR170 fibres. H3K36me3 domains were enriched for IRS (O.R. = 1.13; q = 1.71E-50) and short regular NRL172 (O.R. = 1.39; q = 3.69E-170).
- **Constitutive heterochromatin is enriched for irregular fibres.** Both mappable H3K9me3 regions and unmappable alpha/beta/gamma satellite reads were enriched for IRS (Satellite O.R. = 1.13, q = 5.71E-11; H3K9me3 O.R. = 1.35, q = 3.95E-23) as well as regular NRL172 (Satellite O.R. = 1.61, q = 5.25E-80; H3K9me3 O.R. = 1.23, q = 3.86E-6). The authors argue short-read NRL estimates "may have been confounded by in vivo heterogeneity". A reanalysis of K562 Fiber-seq data (Stergachis 2020) also found H3K9me3 domains enriched for irregular fibres. The authors speculate the irregularity links to HP1-driven restructuring and phase separation.

## Methods / evidence

In vitro: nonanucleosome arrays assembled by salt-gradient dialysis, EcoGII methylation (2.5 µL enzyme, 30 min, 37 °C, SAM replenished), Sequel I or II sequencing, with unmethylated and fully methylated naked-DNA controls. In vivo: 100 × 10⁶ K562 cells; MNase at 1 U per 50 × 10⁶ nuclei for 1 min at 37 °C; overnight lysolecithin dialysis to release fibres; EcoGII methylation of the solubilised chromatin; G-tube shearing; three 30 h Sequel II movies. Further SAMOSA runs varied digestion temperature and time to tune fragment lengths. Analysis: CCS with pbmm2 alignment; a Gaussian mixture model on normalised IPD gives per-adenine methylation posteriors; 33 bp smoothing; per-molecule autocorrelograms; Scanpy Leiden clustering; scipy peak calling for single-molecule NRL. TF sites come from ENCODE IDR peaks plus FIMO/CISTROME PWMs, with gkmSVM-matched GC/repeat controls, Fisher's exact tests and Storey q-values. Satellite reads were found by BLAST against DFAM consensus sequences. Data: GEO GSE162410 and Zenodo 10.5281/zenodo.3834705. Code: github.com/RamaniLab/SAMOSA.

Weight: a careful proof-of-concept with a strong in vitro ground truth and two in vivo replicates in one cell line. The biological claims are enrichment odds ratios. Many are small in size (O.R. 1.1–1.6), though very significant because the molecule counts are huge. The heterochromatin result is supported by an independent assay (the Fiber-seq reanalysis). One PacBio employee (J.G. Underwood) is an author. (synthesis)

## Limitations

**Authors' own:**
- The protocol enriches fragments of only ~500 bp to ~2 kb, although PacBio CCS can handle 10–15 kb, so kilobase-domain-scale patterns are not yet reachable.
- Fibres are methylated *after* solubilisation, so the assay is "unlikely to capture protein-DNA interactions weaker or more transient than the stable nucleosome-DNA interaction". This fits the absence of TF footprints.
- Cells were unsynchronised, so the contribution of the cell cycle to the heterogeneity cannot be addressed.
- The data fall "short of generating a high-coverage reference map of the K562 epigenome". Targeted enrichment (CRISPR-based, SMRT-ChIP) is suggested.

**Reviewer notes:**
- The Introduction says the method "reveals enrichment for long, regular chromatin arrays in actively elongating chromatin". The Results instead report H3K36me3 enriched for irregular-short and *short* regular NRL172 fibres. The authors themselves say this only "partially corroborate[s]" earlier long-regular-array reports. (synthesis)
- MNase digestion and lysolecithin solubilisation both select which fibres are released and sequenced. The cluster abundances are therefore a "rough estimate of the equilibrium composition" (the authors' words), and may not represent all nuclear chromatin equally. (synthesis)
- This is bulk input from 100 million cells. The "single-molecule" resolution is per fibre, not per cell, so the assay cannot tell whether heterogeneity lies within cells or between them. (synthesis)

## Surprising or load-bearing bits

- **Bulk NRL differences are mixtures.** Epigenomic domains look distinct in MNase-Southern data because they use the same pattern repertoire in different proportions, not because each domain has its own uniform fibre structure. This reframes decades of averaged NRL measurements.
- **Heterochromatin is not conformationally static.** Irregular fibres are enriched in H3K9me3 and satellite chromatin, including unmappable satellites that short reads cannot reach.
- **An accessible fibre need not show a footprint.** Post-solubilisation methylation captures nucleosome registers but loses TF footprints. Later in-nucleus stenciling methods (Fiber-seq, SAMOSA-Tag, SMRT-Tag) changed exactly this design choice. (synthesis)
- **Single-cell analysis toolkit applied to molecules.** Leiden clustering and autocorrelation treat each fibre like a "cell", an analogy the authors make explicitly.

## Entities mentioned

- [[20-Entities/vijay-ramani]] — corresponding author (UCSF).

## Concepts touched

- [[30-Concepts/samosa]] — the defining paper. In this version EcoGII acts on solubilised oligonucleosomes, not in intact nuclei.
- [[30-Concepts/single-molecule-footprinting]] — methyltransferase stenciling with native PacBio detection; per-fibre nucleosome registers.
- [[30-Concepts/pacbio]] — IPD-based m6dA detection on CCS reads.
- [[30-Concepts/chromatin-accessibility]] — accessibility states (MR/NO/SA/A/HA) at TF motifs.
- [[30-Concepts/transcription-factor-motif]] — ENCODE/FIMO-predicted motifs for six TFs.
- [[30-Concepts/clustering-algorithms]] — Leiden community detection on autocorrelograms ([[10-Summaries/traag-2019-leiden]]).
- [[30-Concepts/chromatin-phase-separation]] — proposed link between heterochromatin irregularity and HP1-driven phase separation, and NRL-dependent array phase separation ([[10-Summaries/gibson-2019-chromatin-llps]]).
- [[40-Topics/histone-modifications]] — H3K4me1/3, H3K27me3, H3K36me3 and H3K9me3 domains compared by fibre composition.

## Connections to other sources

- Independent support from [[10-Summaries/andrewb-2020-science]]: the authors reanalysed K562 Fiber-seq data and also found H3K9me3 domains enriched for irregular fibres. Fiber-seq uses Hia5 on intact nuclei, SAMOSA uses EcoGII on solubilised fibres.
- Other long-read methylation-footprinting methods the paper cites: [[10-Summaries/shipony-2020-smac]] (SMAC-seq) and [[10-Summaries/lee-2020-nanonome]] (nanoNOMe), both read on Oxford Nanopore.
- Short-read GpC/CpG single-molecule and single-cell predecessors whose sequence and bisulfite biases SAMOSA avoids: NOMe-seq lineage, including [[10-Summaries/pott-2017-elife]] (scNOMe-seq).
- Successors that adapt EcoGII/m6A stenciling: [[10-Summaries/nanda-2024-smrt-tag]] (SMRT-Tag), [[10-Summaries/mo-2023-stam-seq]] (STAM-seq), and [[10-Summaries/altemose-2022-dimelo-seq]] (antibody-targeted m6A). (synthesis)
- Complements contact-map views of nucleosome-scale folding: [[10-Summaries/hsieh-2015-micro-c]]. (synthesis)

## Open questions

- Would in-nucleus methylation, done before MNase, recover TF footprints and change the state distribution? The authors suggest this as future work.
- Are the irregular heterochromatin fibres caused by HP1 or remodelers (SWI/SNF, ISWI, INO80, CHD)? The authors call for perturbation experiments.
- Is the fraction of "stochastically accessible" motifs (state SA) a measure of site exposure that predicts TF binding in nucleosome-occluded regions?
- Do pattern compositions differ between cells (cell-cycle stage, cell type), given that the data are bulk and unsynchronised? (synthesis)

## Related

- [[30-Concepts/samosa]] · [[30-Concepts/samosa-tag]] · [[30-Concepts/single-molecule-footprinting]] · [[30-Concepts/fiber-seq]] · [[30-Concepts/pacbio]]
- [[10-Summaries/shipony-2020-smac]] · [[10-Summaries/lee-2020-nanonome]] · [[10-Summaries/altemose-2022-dimelo-seq]] · [[10-Summaries/andrewb-2020-science]] · [[10-Summaries/doughty-2024-smf-tf]]
- [[40-Topics/long-read-sequencing]] · [[40-Topics/chromatin-architecture]]
