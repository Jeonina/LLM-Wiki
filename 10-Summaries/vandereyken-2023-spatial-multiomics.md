---
type: summary
title: "Vandereyken, Sifrim, Thienpont & Voet 2023 — Methods and applications for single-cell and spatial multi-omics"
source: "[[00-Sources/papers/Methods and applications for single-cell and spatial multi-omics - Nature Reviews Genetics]]"
source_kind: paper
author: "Katy Vandereyken, Alejandro Sifrim, Bernard Thienpont, Thierry Voet (corresponding)"
published: 2023-03-02
ingested: 2026-08-10
doi: "10.1038/s41576-023-00580-2"
journal: "Nature Reviews Genetics"
tags: [multi-omics, spatial-multiomics, coupling-principles, genome-plus-transcriptome, DamID, review, taxonomy]
entities: ["[[thierry-voet]]"]
concepts: ["[[joint-single-cell-multi-omics]]", "[[gt-seq]]", "[[dr-seq]]", "[[damid]]", "[[scdamt-seq]]", "[[scnmt-seq]]", "[[nome-seq]]", "[[spatial-multiomics]]", "[[combinatorial-indexing]]", "[[multi-tag]]", "[[cite-seq]]", "[[dogma-seq]]", "[[fiber-seq]]"]
topics: ["[[single-cell-multiomics]]", "[[somatic-mosaicism]]"]
---

**Citation:** Vandereyken, Sifrim, Thienpont & Voet (2023) — *Methods and applications for single-cell and spatial multi-omics* — *Nature Reviews Genetics* 24, 494–515. [DOI](https://doi.org/10.1038/s41576-023-00580-2)

# Vandereyken 2023 — coupling principles and spatial multi-omics

> The organizing insight is mechanical rather than biological: multi-omic methods differ by **when the analytes are uncoupled** — before, during or after library preparation. Four principles (physical separation, preamplification-and-split, seq-split by differential barcoding, combinatorial indexing) generate the whole method space and predict each method's throughput ceiling and failure modes.

## Key claims

**Genome + transcriptome, by coupling principle:**
- *Physical separation before library prep*: **G&T-seq** (oligo-dT beads pull poly(A) RNA from lysate; supernatant gDNA goes to WGA of your choice — the freedom to pick the WGA method for the variant class of interest is the stated advantage). **SIDR-seq** (hypotonic lysis, antibody-magnetic-bead nucleus isolation). **DNTR-seq** (centrifugation separates nuclei; nuclear DNA goes to **direct tagmentation**, bypassing WGA and its artifacts).
- These nuclear–cytosolic methods are "less amenable to comprehensive characterization of mitochondrial DNA and nuclear RNA" and require intact cells.
- *Preamplification and split*: **DR-seq** — cDNA and gDNA quasi-linearly co-amplified in one tube, then split; the caveat is stated plainly, contaminating cDNA co-amplifies into reads **indistinguishable from gDNA**. Only the cDNA carries a T7 promoter, so the IVT branch is clean. **TARGET-seq** targets a specific mutation with both cDNA and gDNA primers.
- *Seq-split*: **scONE-seq** differentially barcodes gDNA (6-nt tagmentation adapter) and RNA (6-nt RT primer) in one tube — elegant, but it "hampers sequencing RNA-seq and DNA-seq libraries separately to optimal depths."
- *Combinatorial indexing*: **sci-L3-RNA/DNA**, three-level indexing with IVT amplification, tens of thousands of nuclei and a path to >1 million — though "high-sensitivity and high-resolution profiling per cell was not demonstrated."

**Applications with concrete results:**
- DNTR-seq found minor genetic subclones with associated transcriptional perturbations in paediatric ALL, and showed structural imbalances produce **both linear and nonlinear transcriptional dosage effects** — *MYC* and *TCF7L2* showed strong dosage compensation and were largely unaffected by copy number.
- Genome editing safety: G&T-seq on *OCT4*-targeted human preimplantation embryos found **LOH extending beyond the on-target locus** plus segmental loss and gain of chromosome 6, with unintended edits in **~16%** of embryo cells — while the transcriptome showed LOH did not misexpress adjacent genes.
- Genome + transcriptome allows a variant called in DNA to be **confirmed in the RNA of the same cell**, raising genotyping reliability, and lets a genetic lineage tree be annotated with cell-type and phenotypic states.

**Epigenome + transcriptome:** the tagmentation family (scCAT-seq, Smart3-ATAC plate-based; sci-CAR, SHARE-seq, SNARE-seq2, Paired-seq by combinatorial indexing; SNARE-seq, ASTAR-seq, 10x Multiome by microfluidics; ISSAAC-seq either way) — with the honest note that **"a systematic benchmark of these methods is unfortunately currently lacking."** Antibody-directed variants (scPCOR-seq, coTECH, Paired-Tag, scSET-seq) target histone PTMs instead of accessibility; scCUT&Tag2for1 and scMulti-CUT&Tag target two epitopes at once, distinguished either by peak shape or by transposase-specific barcodes.

**Methylation-based:** costs and technical complexity are named as the barriers; PBAT covers 5–50% of the genome at high cost, RRBS 1–3% cheaply. GpC-methyltransferase methods (scCOOL-seq, scNOMe-seq; trimodal scNMT-seq, scNOMeRe-seq, scChaRM-seq, snmCAT-seq) show **higher coverage per promoter than ATAC-based methods** and make open-vs-truly-closed distinguishable, at higher sequencing cost — with GCG positions discarded as ambiguous. snm3C-seq and scMethyl-HiC pair methylome with 3D structure; **methods adding the transcriptome to those "have yet to be described."**

**6mA/DamID:** because 6mA is ultra-rare in mammalian DNA it marks nearly unambiguously. scDam&T-seq and EpiDamID tether Dam to chromatin proteins or PTM-recognizing nanobodies. Profiles reflect **aggregate residence time** — better signal-to-noise, poorer temporal resolution — and require transgenesis, but extend beyond antibody-available targets and **may suffer less from the accessible-chromatin bias of transposase methods**.

**Spatial multi-omics:** adjacent-section strategies (flexible, but sections differ in structure and composition and resolutions differ); DBiT-based spatial ATAC&RNA-seq and CUT&Tag-RNA-seq at 20–25 µm pixels over 2,500–10,000 pixels; imaging routes (DNA-MERFISH with >1,100 nascent transcripts plus >1,000 loci plus nuclear-body antibodies; DNA-seqFISH+ with 3,660 loci, 70 mRNAs and 17 nuclear structures); spatial transcriptome+protein (Visium, SPOTS 21 proteins, SM-Omics 6, GeoMx DSP, spatial-CITE-seq at ~200–300 proteins and 20 µm). Also LCM-based isolation feeding standard single-cell multi-omics at spatial resolution.

## Methods / evidence

Review from a lab that builds these assays (G&T-seq is Voet's). Consistently candid about limitations — the missing benchmark, DR-seq's cDNA contamination, sci-L3's undemonstrated per-cell resolution, DamID's temporal blurring.

## Surprising or load-bearing bits

- **The coupling-principle taxonomy predicts throughput.** Physical separation is inherently plate-based and low-throughput; only seq-split and combinatorial indexing scale. That is why genome+transcriptome methods lag epigenome+transcriptome methods in cell numbers, and it is a structural constraint rather than an engineering gap.
- **DNTR-seq's dosage-compensation result matters for this wiki's core question.** *MYC* and *TCF7L2* are copy-number-altered yet transcriptionally buffered — so inferring expression consequence from CNV, or CNV from expression ([[gao-2021-copykat|CopyKAT]], [[tickle-2019-infercnv|inferCNV]]), fails at exactly the genes people care most about.
- **The ~16% unintended-edit rate in human embryos**, detectable only because genome and transcriptome were read in the same cells, is the strongest clinical argument in this corpus for joint assays.
- **GpC-methyltransferase accessibility beats ATAC on promoter coverage and distinguishes truly closed from unsampled.** scATAC cannot tell "closed" from "not observed"; NOMe-type methods can, because every read reports. Underweighted in a field standardized on Tn5. See [[mnase-vs-tn5-chromatin]].
- **DamID may avoid the accessible-chromatin bias transposase methods carry** — the same bias [[kaya-okur-2019-cut-and-tag|CUT&Tag]] documents as untethered pA-Tn5 background. Orthogonal chemistry, orthogonal artifacts.
- Explicit gap flagged: **no method jointly profiles methylome + 3D structure + transcriptome.** A concrete, buildable target.
- Voet's framing of somatic mutation reaches beyond cancer — "normal tissues are also subjected to an extraordinary amount of mutation," and joint genome+transcriptome is how you ask what those mutations *do* to cellular state, competition, homeostasis and ageing. That is this wiki's central question, stated as a methods agenda.

## Entities mentioned

- [[thierry-voet]] — corresponding author; G&T-seq and the single-cell genome+transcriptome program.

## Concepts touched

- [[joint-single-cell-multi-omics]] — the four-principle taxonomy is the mechanistic complement to [[zhu-2020-multimodal-power-of-many]]'s throughput split and [[argelaguet-2021-integration-principles]]'s anchor split.
- [[damid]] / [[scdamt-seq]] — residence-time semantics and the transgenesis constraint.
- [[spatial-multiomics]] — resolution and area limits stated numerically.

## Connections to other sources

- Three complementary taxonomies: this (coupling mechanism), [[zhu-2020-multimodal-power-of-many]] (depth vs throughput), [[argelaguet-2021-integration-principles]] (computational anchor).
- Primary sources: [[macaulay-2015-gt-seq]], [[dey-2015-dr-seq]], [[cao-2018-sci-car]], [[ma-2020-share-seq]], [[clark-2018-scnmt-seq]], [[pott-2017-elife]], [[lee-2019-natmethods]], [[rooijers-2019-scdamt-seq]], [[de-luca-2021-scdamid-protocol]].
- Fiber-seq connection ([[andrewb-2020-science]]) noted for combining 6mA marking with long reads.
- Spatial: [[cardilla-2025-spatial-methylome]], [[morriss-2024-spatial-genomics-clonal]].
- Layer-pair coverage tracked at [[joint-assays-by-layer-pair]].

## Open questions

- **The missing benchmark** for tagmentation-based joint accessibility+transcriptome methods is stated outright and, as far as this corpus shows, still open.
- Methylome + 3D + transcriptome in one cell — named as nonexistent.
- Single-cell proteome-wide analysis alongside other omics layers is "currently lacking" despite mass-spec single-cell proteomics existing.
- Whether DamID's reduced accessibility bias is quantified anywhere, or asserted — unresolved here.

## Related

- [[zhu-2020-multimodal-power-of-many]] · [[argelaguet-2021-integration-principles]] · [[joint-single-cell-multi-omics]] · [[joint-assays-by-layer-pair]]
