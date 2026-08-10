---
type: summary
title: "Lim et al. 2024 — Advances in single-cell omics and multiomics for high-resolution molecular profiling"
source: "[[00-Sources/papers/Advances in single-cell omics and multiomics for high-resolution molecular profiling - Experimental & Molecular Medicine]]"
source_kind: paper
author: "Jongsu Lim, Chanho Park, Minjae Kim, Hyukhee Kim, Junil Kim, Dong-Sung Lee (corresponding)"
published: 2024-03-05
ingested: 2026-08-10
doi: "10.1038/s12276-024-01186-2"
journal: "Experimental & Molecular Medicine"
tags: [review, method-catalog, scWGA, scRNA-seq, methylome, chromatin-accessibility, scHi-C, histone-modifications, single-cell-proteomics]
entities: []
concepts: ["[[scwga-chemistries]]", "[[dop-pcr]]", "[[mda]]", "[[pta]]", "[[meta-cs]]", "[[scbs-seq]]", "[[scatac-seq]]", "[[nome-seq]]", "[[single-cell-hi-c]]", "[[cut-and-tag]]", "[[scchix-seq]]", "[[combinatorial-indexing]]"]
topics: ["[[single-cell-multiomics]]", "[[whole-genome-amplification]]"]
---

**Citation:** Lim et al. (2024) — *Advances in single-cell omics and multiomics for high-resolution molecular profiling* — *Experimental & Molecular Medicine* 56, 515–526. [DOI](https://doi.org/10.1038/s12276-024-01186-2)

# Lim 2024 — method catalog by omics layer

> A broad, method-by-method survey organized by molecular layer — isolation and barcoding, then genome, transcriptome, proteome, methylome, accessibility, chromatin conformation, histone modifications — with the operational differences between protocol variants stated explicitly. Its value here is comprehensiveness of the methylome and chromatin sections and coverage of the proteome layer this wiki otherwise lacks.

## Key claims

**Isolation and barcoding.** FACS enables multiparameter selection but needs sufficient cell density and the flow/fluorescence exposure can compromise viability. Microfluidic and nanowell devices shift reaction volumes to nanoliter/picoliter scale, which "can shift the main cost barrier from library preparation to sequencing." Barcoding timing matters structurally: plate methods add the cell barcode at final PCR, while microfluidic methods incorporate it early, allowing single-tube processing and **fewer handling steps and less sample loss**.

**Genome.** The WGA chronology with the failure modes named: DOP-PCR (low genome coverage from site-preferential amplification), MDA (high coverage, amplification bias), and the shared artifact list — **locus and allelic dropouts, uneven amplification, chimeric molecules, base-copy errors**. PTA achieves quasi-linear amplification via exonuclease-resistant terminators. **META-CS** labels the two DNA strands differently in a one-tube reaction so complementary positions can be compared and false positives filtered. **SISSOR** separates Watson and Crick strands into nanoliter compartments in a microfluidic device — high accuracy, reduced coverage from fragment loss during strand separation.

**Transcriptome.** CEL-seq2 and MARS-seq2.0 (reduced RT volume → less noise) capture 3′ ends only, so 5′ sequences and isoforms are inaccessible. Full-length methods (mcSCRB-seq, SMART-seq3, FLASH-seq) use template-switching oligos plus UMIs; VASA-seq captures **non-polyadenylated** transcripts including lncRNAs and small ncRNAs. Long-read methods MAS-ISO-seq and SnISOr-seq address isoform resolution; SnISOr-seq splits intronic from exonic cDNA and sequences only exonic.

**Proteome.** MALDI and LAESI mass spectrometry; single-cell western blotting (scWB) with in-gel electrophoresis of a lysed single cell.

**Methylome** — the most detailed section:
- scBS-seq vs scRRBS (CpG-enriched, single-tube, cheaper).
- **Adapter ligation before bisulfite treatment causes high DNA loss** — solved by post-bisulfite adapter tagging (PBAT) in scWGBS/scBS; Msc-RRBS avoids PBAT entirely by using a **methylated adapter** that survives conversion.
- snmC-seq2 uses random primer H (**lacking G**) to reduce hybridization frequency, plus extra quenching to cut dNTP contamination.
- scSPLAT uses a splinted second adapter, improving mappability without adding artificial low-complexity sequence or risking carryover-nucleotide artifacts.
- sci-MET → sci-METv2, split into **LA (linear amplification, high coverage)** and **SL (splint ligation, cheaper and faster)**; low insert size from bisulfite damage remains.
- **sciEM** replaces bisulfite with APOBEC/TET2 enzymatic conversion plus a G-depleted random linear primer for better CpH mapping, giving increased genomic coverage.
- MID-RRBS uses microfluidic reagent swapping to reduce DNA loss between bisulfite treatment and desulfonation.

**Accessibility.** scDNase-seq detects more DHSs per cell than scATAC-seq but needs longer hands-on time. **scMNase-seq** uses MNase as both endo- and exonuclease, uniquely cutting linker DNA so nucleosome boundaries are precisely determined — but captures only **3–10%** of nucleosome and subnucleosomal fragments. scNOMe-seq reads accessibility from GpC methylation per read rather than by counting reads, so individual CpG sites independently report accessibility.

**Chromatin conformation.** Hi-C variants split by cyclization system into dilute-ligation and in-situ-ligation groups. scHi-C introduced in-nucleus ligation; sciHi-C replaced physical nuclear isolation with combinatorial indexing; sciDLO Hi-C removes the biotin labeling and pulldown step entirely.

**Histone modifications.** ChIP-seq's low SNR requires many cells; Drop-ChIP, CUT&RUN (needing end polishing and adapter ligation), scCUT&Tag with pA-Tn5. **scChIX-seq** profiles two marks per cell by deconvolving double-incubated cells using single-incubated datasets as training data.

## Methods / evidence

Catalog review. Its strength is granular protocol-level differences that method papers state in passing and other reviews omit — which adapter chemistry, which primer modification, which step each variant fixes. Its weakness is that it does not benchmark or arbitrate; performance claims are as reported by each method's authors.

## Surprising or load-bearing bits

- **The methylome section is the most useful part of this ingest for protocol selection.** It traces a clear engineering lineage — every scBS variant is a fix for a specific loss mechanism (adapter-before-conversion loss → PBAT; PBAT's low complexity → Msc-RRBS methylated adapters; random-primer mis-hybridization → snmC-seq2's G-free primer; artificial low-complexity sequence → scSPLAT splinted adapters; bisulfite damage itself → sciEM enzymatic conversion). Read as a sequence, it shows the field converging on **abandoning bisulfite**, which is where [[chen-2025-sctaps-sccaps-plus|scTAPS/scCAPS+]] arrives.
- **scMNase-seq's 3–10% capture rate** is a number rarely quoted and it explains why MNase-based single-cell methods stayed niche despite superior nucleosome-boundary resolution — relevant to [[mnase-vs-tn5-chromatin]].
- **scDNase-seq detecting more DHSs per cell than scATAC-seq** is a claim worth flagging: the field standardized on ATAC for convenience, not sensitivity. Consistent with [[lake-2018-brain-snrna-scths|scTHS-seq]]'s distal-enhancer sensitivity claim.
- scNOMe-seq reading accessibility **per read** rather than by read count is a structural advantage over ATAC that this review states cleanly: each molecule reports its own accessibility, so sparsity behaves differently.
- **META-CS and SISSOR** are strand-aware scDNA approaches thinly represented in this corpus; both attack the same false-positive problem as duplex sequencing but by different means — complementary-strand comparison in one tube, and physical Watson/Crick separation respectively. See [[single-cell-duplex-sequencing]].
- VASA-seq's non-polyadenylated capture matters for anything involving lncRNA or small ncRNA, which standard poly(A) methods miss entirely.
- Includes single-cell **proteomics** (MALDI, LAESI, scWB) — a layer with no other bookmarked source in this wiki, and the one [[zhu-2020-multimodal-power-of-many]] named as the standing gap.

## Concepts touched

- [[scwga-chemistries]] — DOP-PCR → MDA → PTA plus META-CS and SISSOR as strand-aware alternatives.
- [[scbs-seq]] — the fullest protocol-variant catalog in this corpus.
- [[scchix-seq]] — the training-data deconvolution logic stated compactly.

## Connections to other sources

- Complements [[vandereyken-2023-scmultiomics-review]] (which organizes by *coupling principle*) and [[zhu-2020-multimodal-power-of-many]] (by throughput/depth). This one organizes by layer and protocol variant.
- Primary sources for its methylome catalog: [[smallwood-2014-natmethods]], [[guo-2013-scrrbs]], [[luo-2018-snmc-seq2]], [[nichols-2022-scimet-v2]].
- WGA lineage: [[telenius-1992-dop-pcr]], [[dean-2002-mda]], [[gonzalez-pena-2021-pnas]].
- Histone methods: [[kaya-okur-2019-cut-and-tag]], [[rotem-2015-drop-chip]], [[yeung-2023-scchix-seq]].
- 3D genome: [[nagano-2013-nature]], [[tan-2018-science]].

## Open questions

- No benchmarking — the review reports each method's self-declared performance. Comparative claims (scDNase-seq > scATAC-seq in DHS detection) are inherited, not tested; [[luo-2024-scatac-benchmark]] and [[xiao-2024-multiomics-benchmark]] are where such claims would be adjudicated.
- Several methods it catalogs — META-CS, SISSOR, sciEM, scSPLAT, Msc-RRBS, MID-RRBS, VASA-seq, scMNase-seq — have **no primary source bookmarked** in this wiki.

## Related

- [[vandereyken-2023-scmultiomics-review]] · [[scwga-chemistries]] · [[scbs-seq]] · [[single-cell-multiomics]]
