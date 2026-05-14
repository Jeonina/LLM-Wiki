---
type: summary
title: "Payne 2021 — In Situ Genome Sequencing (IGS): spatially resolved single-cell genomes"
aliases: [Payne 2021, IGS, in situ genome sequencing, AndrewC_2020_Science]
tags: [IGS, in-situ-sequencing, 3d-genome, single-cell, spatial-genomics, foundational]
created: 2026-05-12
updated: 2026-05-12
sources: ["00-Sources/papers/AndrewC_2020_Science.pdf"]
---

# Payne et al. 2021 — In Situ Genome Sequencing (IGS)

> Andrew C. Payne, Zachary D. Chiang, Paul L. Reginato, Sarah M. Mangiameli, Evan M. Murray, Chun-Chen Yao, Styliani Markoulaki, Andrew S. Earl, Ajay S. Labade, Rudolf Jaenisch, George M. Church, Edward S. Boyden, Jason D. Buenrostro, Fei Chen. *Science* **371**, eaay3446 (26 Feb 2021). DOI: 10.1126/science.aay3446. (The "AndrewC_2020" filename is misleading — this is Payne 2021, not Stergachis.)

## Thesis

IGS sequences DNA **directly inside intact, fixed cells**, then matches each in-situ read to a high-quality paired-end ex-situ read of the same amplicon — producing thousands of genomic paired-end reads with **(x, y, z) spatial coordinates inside the nucleus** for each cell. Unlike Hi-C (which reads contact frequency in bulk) or DNA FISH (which reads spatial position at a handful of loci), IGS gives genome-wide spatial DNA at base-pair resolution in single cells.

## Mechanism

1. Fixed cells / embryos → Tn5 tagmentation inserts adapters at random genomic positions in their native spatial context.
2. Fragments circularized by hairpin ligation carrying a unique molecular identifier (UMI) and primer sites.
3. **Rolling circle amplification** in situ → clonally amplified amplicons (~400–500 nm features) at their original spatial position, each visible as a punctate spot.
4. **18 rounds of in situ sequencing by ligation + fluorescence imaging** → reads the UMI of each amplicon at its 3D position.
5. Amplicons dissociated from the sample → PCR → ex situ paired-end Illumina sequencing reads the full genomic insert.
6. Probabilistic matching pairs each ex-situ paired-end read to its in-situ UMI/position → spatially-resolved genomic reads.

## Key claims

- **Applied to 106 PGP1 human fibroblasts + 113 mouse embryo cells** across PN4 zygote, late 2-cell, and early 4-cell stages.
- 66.35% of clearly resolvable amplicons (87.6% in PGP1f, 61.0% in mouse embryos) confidently matched between in-situ and ex-situ reads → thousands of paired-end gDNA reads per cell with 3D coordinates.
- **Parent-of-origin chromosome assignment via SNPs**: in the mouse zygote, maternal and paternal pronuclei are spatially separated, and IGS distinguishes them at single-base resolution using parental SNPs — directly imaging genome mixing as zygotic development proceeds.
- **Single-cell chromatin domains in zygotes**: paternal zygotic pronuclei show lamina-distal boundary structures and lamina-proximal interior domains; maternal pronuclei differ.
- **Epigenetic memory of chromosome positioning**: clonal cells (daughters from one division) retain similar chromosome-territory arrangements — demonstrated by intercellular comparison of genome structure within intact embryos.

## Surprising / load-bearing

- IGS is methodologically orthogonal to the DAF-seq / fiber-seq / GoT lineage. It is the **spatial-3D-DNA analog** of what those methods do for chromatin state. For the review's §3.5 (3D genome) section, IGS belongs alongside scHi-C, sn-m3C-seq, and Dip-C as the spatial-imaging-anchored member of the 3D-genome family.
- The **(in-situ short barcode) + (ex-situ paired-end) hybrid sequencing strategy** is a generalizable trick — it sidesteps the throughput ceiling of pure in-situ sequencing by using imaging only for barcode-to-position assignment, not for the genomic sequence itself.
- For §4.6 (DNA-anchored multimodal integration) of the review, IGS is the spatial coordinate "modality" that could anchor genotype + chromatin state + 3D position in the same cell — a direction the field is heading.

## Entities / concepts touched

[[3d-genome]] · [[single-cell-hi-c]] · [[tn5-tagmentation]] · [[umi-molecular-barcoding]] · [[chromatin-compartments]] · [[topologically-associating-domain]] · [[40-Topics/3d-genome]] · [[40-Topics/single-cell-multiomics]]

## Related summaries

- [[harmonizing-single-cell-3d-genome-data-with-stark-and-scnucleome]] — STARK / scNucleome computational framework for 3D-genome data harmonization.
- [[navigating-the-3d-genome-at-single-cell-resolution-techniques-computation-and-mechanistic-landscapes]] — 3D-genome single-cell methods review.

## Note on filename

The source file is `AndrewC_2020_Science.pdf` but the paper is Payne et al. 2021 (the "Andrew C" in the filename is Andrew C. Payne, the first author). It is **not** a Stergachis paper despite the "Andrew" prefix — pure filename coincidence with `AndrewB_2020_Science.pdf` which IS Stergachis Fiber-seq.

---
**Source:** [DOI](https://doi.org/10.1126/science.aax2656) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33509999/)
