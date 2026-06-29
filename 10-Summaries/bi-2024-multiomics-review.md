---
type: summary
title: "Bi & Weng 2024 — Single-cell epigenomics and proteomics methods integrated in multiomics"
source: "[[00-Sources/papers/Single-cell epigenomics and proteomics methods integrated in multiomics]]"
source_kind: paper
author: Haiyue Bi, Xiaocheng Weng (corresponding)
published: 2024
ingested: 2026-05-27
doi: "10.1016/j.fmre.2023.11.014"
journal: "Fundamental Research"
tags: [review, single-cell-multiomics, epigenome, proteome, integration, taxonomy]
entities: ["[[20-Entities/xiaocheng-weng]]"]
concepts: ["[[30-Concepts/single-cell-multiomics]]", "[[30-Concepts/joint-single-cell-multi-omics]]", "[[30-Concepts/multimodal-integration-methods]]", "[[30-Concepts/cite-seq]]", "[[30-Concepts/dogma-seq]]"]
topics: ["[[40-Topics/single-cell-multiomics]]"]
---

**Citation:** Bi & Weng (2024) — *Single-cell epigenomics and proteomics methods integrated in multiomics* — *Fundamental Research*. [DOI](https://doi.org/10.1016/j.fmre.2023.11.014)

# Bi 2024 — multiomics methods catalog organized by data-integration topology

> Wuhan-University review covering ~40 single-cell multiomics methods, organized by which two (or three) omic layers they pair: **epigenome×transcriptome**, **protein×transcriptome**, and **triple-omics spanning the central dogma**. The review's most useful contribution is its **integration taxonomy** (horizontal / vertical / diagonal, after Argelaguet), and its explicit recognition of the **CRISPR-based dual-modal** family (Perturb-seq → Perturb-ATAC → Spear-ATAC) as a distinct branch. Most individual methods covered already have wiki pages; this source serves as a *cross-reference catalog* rather than introducing new techniques.

## Key claims (and what's new vs prior reviews)

1. **Three-axis integration taxonomy.** Reaffirms Argelaguet's classification: *horizontal* (same modality across cell populations, anchored on shared genomic features), *vertical* (different modalities in the same cell, anchored on the cell), *diagonal* (different modalities, different cells, no anchor). Vertical = matched assay; horizontal/diagonal = unmatched. Diagonal is hardest because batch correction risks erasing biology.
2. **Cell-isolation as a multiomics constraint.** Splits methods by isolation chemistry: micromanipulation (G&T-seq, scTrio-seq, scNOMeRe-seq) → FACS (scNOMe-seq, snNMT-seq, scDam&T-seq, Smart-RRBS, scONE-seq) → microfluidic (Fluidigm C1: Perturb-ATAC, ASTAR-seq) → droplet (CITE-seq, ASAP-seq, DOGMA-seq, TEA-seq, SNARE-seq) → combinatorial indexing (sci-CAR, Paired-seq, SHARE-seq, SNARE-seq2, Paired-tag, coTECH). The progression maps cell-throughput axis cleanly.
3. **CRISPR perturbation is a distinct family.** Perturb-seq, CRISP-seq, CROP-seq pair sgRNA delivery with scRNA-seq; Perturb-ATAC, CRISPR-sciATAC, Spear-ATAC pair with scATAC-seq; ECCITE-seq pairs with proteome + transcriptome. The pertinent design split is **how sgRNA identity is captured**: by barcode (Perturb-seq, CRISP-seq, Perturb-ATAC), by polyadenylated direct sequencing (CROP-seq, CRISPR-sciATAC), or by genomic integration (Spear-ATAC).
4. **Protein-quantification has two lineages.** NGS-based (CITE-seq, REAP-seq, ASAP-seq, RAID-seq, SPARC, inCITE-seq, PHAGE-ATAC) where antibody-oligo conjugates are amplified and sequenced, vs mass-spectrometry-based (PLAYR, scMS, MIBI) where isotope-labeled antibodies are ionized. NGS dominates current multiomics because it scales and shares pipelines with DNA/RNA. scMS is constrained to ~hundreds of cells and few proteins per cell.
5. **Triomics spanning the central dogma.** TEA-seq (transcriptome + ATAC + surface protein), DOGMA-seq (same + mtDNA), and NEAT-seq (transcriptome + ATAC + *nuclear* protein) are the three operational central-dogma platforms. NEAT-seq is the newest; it uses *E. coli* SSB to block antibody-oligo charge and enable nuclear-protein staining, which is otherwise prone to nonspecific binding.

## Methods / evidence

This is a review, not primary data. Tables 1–3 catalog scMethyl-mRNA methods (9), scATAC-mRNA methods (7), CRISPR-based dual-modal methods (7), with throughput, amplification strategy, and case study per row. Diagrams illustrate split-pool barcoding, droplet GEMs, antibody-oligo chemistry. References ~250 primary papers.

## Surprising or load-bearing bits

- **The horizontal/vertical/diagonal frame is genuinely useful.** It clarifies why some integration problems (matched vertical: SHARE-seq, scNMT-seq) are computationally easier than others (diagonal: scATAC from one experiment + scRNA from another). The wiki's [[30-Concepts/multimodal-integration-methods]] page already references this implicitly via MOFA / Seurat WNN / MultiVI / GLUE, but Bi & Weng give it a name.
- **PHAGE-ATAC is an unexpected design.** Uses phage-encoded nanobodies whose CDR3 region acts as a built-in barcode for surface-protein detection on a droplet-ATAC platform. Avoids antibody-oligo conjugation entirely.
- **Methodology bias toward 5mC.** The review notes that single-cell DNA-modification multiomics is "still in early stages" for marks other than 5mC. sn-m6A-CT (single-nucleus m⁶A cleavage under targets and tagmentation) is cited as the first integrated m⁶A + transcriptome method — RNA-modification × transcriptome is essentially a 2023+ frontier.
- **Combinatorial indexing's collision problem.** sci-CAR / SHARE-seq / Paired-seq all suffer unavoidable collision rates: some cells end up with identical barcode trios and become ambiguous. Reducing collision means more wells (higher cost) or fewer cells per well (lower throughput). This is the structural reason droplet platforms remain competitive despite lower theoretical scaling.
- **Citation accuracy caveat.** The frontmatter of the source clipping is mangled (author list is fragments of the abstract, no publication date). The actual journal is *Fundamental Research* (Chinese Academy of Sciences flagship); the DOI resolves to Volume 4, Issue 5 (2024). The first/corresponding-author pair is Bi (PhD student) and Weng (Wuhan University professor).

## Entities mentioned

- [[20-Entities/xiaocheng-weng]] — corresponding author, Wuhan U; focuses on nucleic acid epigenetic modifications and protein-nucleic-acid interactions

## Concepts touched

- [[30-Concepts/single-cell-multiomics]] — this review is one of the broad catalogs
- [[30-Concepts/joint-single-cell-multi-omics]] — methodology family
- [[30-Concepts/multimodal-integration-methods]] — introduces horizontal/vertical/diagonal frame
- [[30-Concepts/cite-seq]] — central to the protein-measurement section
- [[30-Concepts/dogma-seq]] — exemplar triomics platform
- [[30-Concepts/share-seq]] · [[30-Concepts/sci-car]] · [[30-Concepts/scnmt-seq]] · [[30-Concepts/sctrio-seq]] · [[30-Concepts/gt-seq]] · [[30-Concepts/dr-seq]] — all covered

## Connections to other sources

- **Overlaps heavily with** [[10-Summaries/baysoy-2023-multiomics-landscape]], [[10-Summaries/vandereyken-2023-scmultiomics-review]], [[10-Summaries/wang-2023-multimodal-review]]. The four reviews together form a 2023–2024 catalog cluster.
- **Differentiates by emphasizing**: (a) the integration topology taxonomy more explicitly than Baysoy or Vandereyken; (b) the CRISPR-perturbation family more thoroughly than Wang; (c) nuclear-protein multiomics (NEAT-seq) which is newer than most of the others cover.
- **Extends** the wiki's existing [[30-Concepts/multimodal-integration-methods]] taxonomy by naming the horizontal/vertical/diagonal split.

## Open questions

- Is the horizontal/vertical/diagonal distinction load-bearing for tool choice, or is it a post-hoc classification? Worth checking whether papers introducing new integration methods (GLUE, MultiVI) actually frame themselves in these terms.
- The review does not address the **scDNA-anchored** multiomics axis (genotype + epigenome + transcriptome) that the wiki's central thesis tracks via GoT / GoT-ChA / DAF-seq / Duplex-Multiome. This is a literature gap consistent with our [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|synthesis-gap note]] — DNA-mutation-anchored multiomics has not yet been packaged into the standard multiomics reviews.

## Related

- [[40-Topics/single-cell-multiomics]] · [[30-Concepts/single-cell-multiomics]]
- [[10-Summaries/baysoy-2023-multiomics-landscape]] · [[10-Summaries/vandereyken-2023-scmultiomics-review]] · [[10-Summaries/wang-2023-multimodal-review]] — companion reviews
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — what this catalog *misses*
