---
type: summary
title: "Ahn et al. 2021 — Phase separation drives aberrant chromatin looping and cancer development (NUP98-HOXA9)"
source: "[[00-Sources/papers/Phase separation drives aberrant chromatin looping and cancer development]]"
source_kind: paper
author: "Jeong Hyun Ahn, Eric S. Davis, Timothy A. Daugird, Shuai Zhao, Ivana Yoseli Quiroga, Hidetaka Uryu, Jie Li, Aaron J. Storey, Yi-Hsuan Tsai, Daniel P. Keeley, Samuel G. Mackintosh, Ricky D. Edmondson, Stephanie D. Byrum, Ling Cai, Alan J. Tackett, Deyou Zheng, Wesley R. Legant, Douglas H. Phanstiel, Gang Greg Wang (corresponding)"
published: 2021-06-23
ingested: 2026-05-18
ingest_depth: full-intro+results
doi: "10.1038/s41586-021-03662-5"
journal: "Nature"
tags: [LLPS, phase-separation, cancer, leukaemia, NUP98, HOXA9, IDR, FG-repeats, chromatin-loops, CTCF-independent, super-enhancer, Wang-lab]
entities: []
concepts:
  - "[[30-Concepts/chromatin-phase-separation]]"
  - "[[30-Concepts/topologically-associating-domain]]"
  - "[[40-Topics/histone-modifications]]"
topics:
  - "[[40-Topics/chromatin-architecture]]"
  - "[[40-Topics/hematopoietic-malignancies]]"
---

**Citation:** Ahn et al. (2021) — *Phase separation drives aberrant chromatin looping and cancer development* — *Nature*. [DOI](https://doi.org/10.1038/s41586-021-03662-5)

# Ahn et al. 2021 — LLPS-driven oncogenic chromatin looping

> Thesis: recurrent leukaemic translocations producing **NUP98-HOXA9** fusion proteins owe their oncogenic capacity to **LLPS**. The intrinsically disordered region (IDR — FG repeats) of NUP98 is *necessary and sufficient* for phase-separated nuclear puncta, leukaemic transformation, broad super-enhancer-like binding, and **CTCF-independent chromatin loops at proto-oncogenes**. Swapping the FG-IDR for an unrelated LLPS-competent IDR (FUS) reproduces all four effects — LLPS competence itself, not specific sequence, is the driving feature.

## Verbatim key claims (from source body)

- **IDR-mediated LLPS is necessary for leukaemogenesis** (Abstract):
  > "IDRs contained within NUP98-HOXA9 ... are essential for establishing **liquid-liquid phase separation (LLPS) puncta of chimera and for inducing leukaemic transformation**."

- **LLPS expands binding into super-enhancer-like patterns** (Abstract):
  > "LLPS of NUP98-HOXA9 not only promotes chromatin occupancy of chimera transcription factors, but also is required for the formation of a **broad 'super-enhancer'-like binding pattern typically seen at leukaemogenic genes**, which potentiates transcriptional activation."

- **IDR identity is replaceable; LLPS competence is the load-bearing property** (Abstract):
  > "An **artificial HOX chimera, created by replacing the phenylalanine and glycine repeats of NUP98 with an unrelated LLPS-forming IDR of the FUS protein**, had similar enhancing effects on the genome-wide binding and target gene activation of the chimera."

- **CTCF-independent loops** at oncogenes (Abstract):
  > "Deeply sequenced Hi-C revealed that **phase-separated NUP98-HOXA9 induces CTCF-independent chromatin loops that are enriched at proto-oncogenes**."

- **Hi-C loop quantification** (Results — "IDRs and LLPS induce chromatin looping"):
  > "Differential analysis revealed **232 loops specific to N-IDR_WT/A9 and 52 specific to N-IDR_FS/A9**... **Most (91%) N-IDR_WT/A9-specific-loop anchors overlapped N-IDR_WT/A9 binding, whereas only 31% overlapped a CTCF-binding site**... Thus, N-IDR_WT/A9 loops form in a largely CTCF-independent manner, consistent with a phase-separation-driven mechanism."

- **Long-distance and trans contacts** (Results):
  > "Regions with high occupancy of N-IDR_WT/A9 exhibited **increased interaction frequencies, even between binding sites separated by great distances (greater than 2 Mb) or on different chromosomes entirely**."

- **LLPS loops co-localize with H3K27ac**:
  > "The vast majority (82%) of N-IDR_WT/A9-specific-loop anchors overlapped H3K27ac, in contrast to only 31% observed for non-differential loop anchors, which suggests that N-IDR_WT/A9-specific loops rewire connections between enhancers and target genes."

- **Single-molecule confirmation of binding stabilization**:
  > "Two-state kinetic modelling of single-molecule trajectories showed that, compared with N-IDR_FS/A9, N-IDR_WT/A9 had **a greater fraction of molecules in the low-diffusion bound state and had slower diffusion coefficients**, which suggests that assemblies of transcription factors, confined within phase-separated puncta, engage target DNA sequences more tightly."

- **Discussion summary** (paper conclusion):
  > "This study provides a **proof-of-principle example of an oncogenic mutation that promotes LLPS-driven transcription factor binding and 3D chromatin reorganization** during transformation of tumours. As a wide range of IDR-containing LLPS-competent molecules are implicated in diseases, this mechanism can potentially be generalized to many pathological settings."

## Why this matters for the wiki

- **Genetic ↔ Structural-Physical axis coupling** — direct evidence that a translocation (genetic alteration) reshapes 3D chromatin via LLPS (biophysical state). Anchors the "closely linked to transcriptional and epigenetic activity" claim in the locus-state framework.
- **CTCF-independent loop class** is a new mechanism for 3D-genome rewiring, complementing CN-driven (CHISEL, MEDICC2) and SV-driven (scTRIP, Liu 2025 LSCC) classes.
- Generalizable: many cancer fusion oncoproteins (EWS-FLI1, FUS fusions, NUP214 chimeras) may act through LLPS competence rather than novel DNA-binding specificity.

## Methods / evidence (from text)

- **Cell systems**: HSPCs (mouse primary haematopoietic stem/progenitor cells, transformation assays), 293FT (stable expression for ChIP-seq/Hi-C), in vivo leukaemia model.
- **LLPS criteria**: 1,6-hexanediol sensitivity, in-vitro recombinant IDR droplet formation (38× / 36× / 27× / 11× FG-repeat variants), live-cell coalescence imaging.
- **IDR mutagenesis**: Phe→Ser mutations in FG repeats abolish LLPS and abolish leukaemogenesis. FUS-IDR substitution rescues both.
- **Genomic profiling**: ChIP-seq (multiple tags), RNA-seq, **deeply sequenced Hi-C** (6,615 loops detected). 1,6-hexanediol treatment dissolves N-IDR_WT/A9 binding but not N-IDR_FS/A9.
- **Single-molecule tracking**: HaloTag-fused N-IDR/A9 in live cells; LLPS-competent variant has slower diffusion and longer bound-state residence.

## Open questions

- How many other recurrent fusion oncoproteins act primarily through LLPS competence rather than novel DNA-binding specificity?
- Can the CTCF-independent loop class be **single-cell mapped** with scHi-C in patient samples? If so, LLPS-driven loops could become a clinical biomarker.
- What distinguishes pathological from physiological condensate-loops (since chromatin LLPS itself is a normal process per [[10-Summaries/gibson-2019-chromatin-llps]])?

---
**Source:** [DOI](https://doi.org/10.1038/s41586-021-03662-5) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/34163069/) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8647409/)

## Related

- [[30-Concepts/chromatin-phase-separation]] · [[30-Concepts/topologically-associating-domain]] · [[40-Topics/histone-modifications]]
- [[10-Summaries/gibson-2019-chromatin-llps]] · [[10-Summaries/daugird-2024-viscoelastic-chromatin]] · [[10-Summaries/qi-zhang-2021-nucleoli-coalescence]]
- [[40-Topics/chromatin-architecture]] · [[40-Topics/hematopoietic-malignancies]]
