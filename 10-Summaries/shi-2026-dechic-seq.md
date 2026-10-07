---
type: summary
title: "Shi et al. 2026 — Genome-wide profiling of histone modifications and transcription factor binding at single-cell resolution by DeChIC-seq"
source: "[[00-Sources/papers/Genome-wide profiling of histone modifications and transcription factor binding at single-cell resolution by DeChIC-seq]]"
source_kind: paper
author: "Zhifei Shi, Xiyang Chen, Yijia Yang, Ang Wu, Heng Wang, Kai Chen, Chong Li, Lina Zou, Zhipeng Qu, Yuyan Zhao, Wenjing Gan, Shuhui Li, Jiayu Chen, Wenqiang Liu, Jiejun Shi, Hong Wang, Jia-min Zhang, Chenfei Wang, Shaorong Gao, Xiaoyu Liu"
published: 2026-07-13
ingested: 2026-10-07
doi: "10.1038/s41422-026-01275-z"
journal: "Cell Research 36:680–697"
tags: [DeChIC-seq, scDeChIC-seq, DddA, deaminase, C-to-U-conversion, histone-modification, transcription-factor-binding, CTCF, RAD21, H3K4me3, preimplantation-embryo, META-CS, scWGA, single-cell]
entities: []
concepts: ["[[30-Concepts/dd-seq]]", "[[30-Concepts/cut-and-tag]]", "[[30-Concepts/cut-and-run]]", "[[30-Concepts/chip-seq]]", "[[30-Concepts/damid]]", "[[30-Concepts/meta-cs]]", "[[30-Concepts/scwga]]", "[[30-Concepts/peak-calling]]", "[[30-Concepts/transcription-factor-motif]]", "[[30-Concepts/pseudo-bulk]]"]
topics: ["[[40-Topics/histone-modifications]]", "[[40-Topics/chromatin-architecture]]", "[[40-Topics/single-cell-multiomics]]"]
---

**Citation:** Shi et al. (2026) — *Genome-wide profiling of histone modifications and transcription factor binding at single-cell resolution by DeChIC-seq* — *Cell Research* 36:680–697. [DOI](https://doi.org/10.1038/s41422-026-01275-z)

# Shi 2026 — DeChIC-seq

> DeChIC-seq (DNA Deaminase-based Chromatin Immuno-Conversion sequencing) swaps *enrichment* for *recording*: an antibody tethers a **protein A–DddA_tox fusion (pA-DddA)** to a histone mark or chromatin-associated protein, and the deaminase writes C→U edits (read as C→T) into nearby DNA. Because nothing is immunoprecipitated or cut out, the whole genome is sequenced and the **background is retained**, so signal is a per-site *conversion rate* rather than a fragment count. Coupled to single-cell WGA ([[meta-cs|META-CS]] transposons, all-in-one-tube), scDeChIC-seq profiles H3K4me3, CTCF, RAD21 and TFs (NR5A2, TFAP2C, KLF5) from individual mouse preimplantation blastomeres — without pooling or combinatorial indexing.

## Key claims

- **Controllable deaminase**: pA-DddA keeps DddA's TC preference (conversion approaching 100% at TC sites in vitro), and its activity is **repressed in pH 8.0 Tris-HCl and reactivated in pH 6.4 MES buffer** — binding happens "off", deamination "on". Other dsDNA deaminases tested (Ddd_Ss, Ddd_Fa, SsdA_tox) were not fully repressible under the same conditions. A rigid linker (A(EAAAK)3A) outperformed a flexible one.
- **Low background**: at TSSs, mean conversion in IgG controls was <0.005 and in no-antibody controls <0.002. DeChIC-seq signal showed low correlation with ATAC-seq and limited overlap with open chromatin — the authors argue no pronounced open-chromatin bias.
- **Bulk concordance (MEF cells)**: H3K4me3 DeChIC-seq and ChIP-seq shared 26,092 peaks — 88.02% of DeChIC-seq peaks and 79.2% of ChIP-seq peaks. CTCF from 5 × 10³ MEFs: 29,638 peaks, 76.33% overlapping ChIP-seq and 74.46% overlapping CUT&Tag. Also works for H3K4me1, H3K9ac, H3K27ac, RAD21 and Pol II.
- **Phased nucleosomes around CTCF** (±1 kb) are visible in the conversion profile, which the authors take as indirect evidence of high resolution.
- **Semi-quantitative readout**: in R1:MEF mixing series, DeChIC-seq signal tracked cell proportion with R² = 0.89 (R1-specific peaks) and 0.94 (MEF-specific); ChIP-seq gave 0.70 / 0.84 and was flat at intermediate ratios (3:1 to 1:3); CUT&Tag gave 0.80 / 0.96. A synthetic *Klf2* template showed U proportion is stable through PCR.
- **Single-cell yield**: ~10,000 unique H3K4me3 peaks per cell (MEF/R1), described as higher per-cell peak numbers than the analysed single-cell protein–DNA datasets; **8–12 merged cells** reproduce ChIP-seq/bulk profiles. Embryo CTCF: mean 11,408 peaks per cell, 41,644 merged; 12 Morula cells approach the merged dataset. TFs: 2,714–11,158 unique peaks per individual cell; ~20 cells give tens of thousands of peaks; 12 cells give signals comparable to CUT&RUN from ~1,000 cells but with sharper motif-centred profiles.
- **Biology — H3K4me3 heterogeneity**: a **Peak Presence Percentage (PPP)** (fraction of cells with a peak at a locus) splits peaks into Common (≥60%), Variable (30–60%) and Rare (10–30%). Common peaks are promoter-proximal and housekeeping; Variable peaks separate ICM from TE (pluripotency vs TE genes); Morula Rare peaks overlap later ICM/TE-specific peaks, and Rare→Variable transitions are enriched for OCT4/SOX2/NANOG (ICM) or TEAD/KLF/CDX2 (TE) motifs. **Broad H3K4me3 domains (>5 kb)** decompose into a common core plus variable flanks contributed by different cells.
- **Non-canonical H3K4me3** at the L1C stage appears in single cells as extended (>5 kb) domains with *higher* conversion than at L2C/4C — i.e. the broad, low-amplitude bulk ChIP appearance does not simply reflect low abundance.
- **CTCF/cohesin**: global CTCF binding reduction from Morula to blastocyst; cleavage-specific CBSs decay (faster in TE), reserved CBSs are stable; RAD21 peaks near CTCF are retained while RAD21-only peaks are lost. In *Obox*-KO L2C embryos, NR5A2 occupancy is substantially reduced — but the design cannot separate reduced protein abundance from reduced binding.

## Methods / evidence

Bulk DeChIC-seq (CoA beads, CUT&RUN-like permeabilisation) and scDeChIC-seq (centrifugation or mouth-pipetting; droplet incubations for embryos) followed by META-CS-style Tn5 tagmentation and strand tagging with a U-tolerant polymerase (Phusion U). Reads aligned with Basal (C:T mode); per-TC-site conversion = T/(C+T); SNPs from the mouse strains masked. A custom blacklist removes high-TC-density bins (TC ≥ 6 per 20 bp; 4,558,691 regions), simple/low-complexity repeats and ENCODE mm10 blacklist. Peaks called with **Metilene** as differentially converted regions versus IgG (bulk) or a simulated pseudo-IgG from merged cells (single cell). Cell QC: duplicate rate ≤30%, signal-to-noise ≥8. Clustering via a binarised peak-by-cell conversion matrix in Signac (TF-IDF/LSI/UMAP); integration with published embryo scRNA-seq via Seurat CCA anchors. Pipeline released as **SCENE**. Comparators are the authors' own ChIP-seq/ULI-NChIP-seq/CUT&Tag and public CUT&RUN.

Weight: strong for bulk concordance and the mixing-series quantitation (three platforms run in parallel by the same lab). Single-cell peak-number comparisons against other methods are cross-study and depth-dependent. Embryo biology (PPP classes, primed rare peaks) is correlative and rests on 20–30 cells per condition. Repressive marks (H3K27me3, H3K9me3) are explicitly weak.

## Surprising or load-bearing bits

- **Signal ≠ fragment count.** Every other immuno-tethering assay (ChIP, CUT&RUN, CUT&Tag) measures where fragments were *pulled out*; DeChIC-seq measures a per-base edit fraction in a WGS-like library. That is why the mixing series is near-linear, and also why its peaks are "narrower and less peak-centred" and agree less with enrichment-based references for TFs — a measurement difference the authors flag rather than hide.
- **Presence/absence is recoverable per cell.** Because uncovered and unbound loci are distinguishable (background is sequenced), PPP can count true absences — something sparse fragment-based single-cell data cannot do. This is the conceptual payoff of retaining background. (synthesis)
- **The pH switch is the trick that makes it work** — binding at pH 8.0 without editing, then a 30-min MES pH 6.4 pulse. D&D-seq solves the same off-target problem with a split enzyme instead ([[chi-2026-dd-seq]]). (synthesis)
- **No pooling.** It uses one-cell-per-tube WGA rather than combinatorial barcoding, which helps rare embryos but caps throughput at tens of cells per experiment.
- **TC-context dependence** is a built-in coverage hole: loci with very low TC density lose sensitivity, and high-TC regions must be blacklisted to avoid false positives.

## Concepts touched

- [[dd-seq]] — the closest sibling: also an antibody-tethered DddA that writes C→U edits, but with a split nanobody–DddA rather than a pH-gated pA fusion.
- [[cut-and-tag]] / [[cut-and-run]] / [[chip-seq]] — the enrichment-based comparators; DeChIC-seq beats ChIP-seq and partly CUT&Tag on proportional signal in mixing series.
- [[damid]] — prior enzyme-labelling approach whose GATC dependence limits resolution, per the authors.
- [[meta-cs]] — single-cell WGA chemistry reused for library construction (transposons "fully referenced to META-CS").
- [[peak-calling]] — peaks defined as differentially converted regions (Metilene), a methylation-style caller repurposed for deamination.
- [[pseudo-bulk]] — single-cell peak calling uses merged cells against a simulated pseudo-IgG.

## Connections to other sources

- Deaminase-stencil family: [[chi-2026-dd-seq]] (split nb-DddA, single-cell multi-omic), [[swanson-2025-daf-seq]] (untethered SsDddA chromatin-accessibility footprinting with PTA). DeChIC-seq is the tethered, bulk-and-single-cell, short-read member.
- Enrichment-based single-cell histone/TF assays it positions against: [[kaya-okur-2019-cut-and-tag]], [[bartosovic-2021-sccut-tag]], [[wu-2021-sccut-tag]], [[bartosovic-2022-nano-cut-tag]], [[ku-2019-scchic-seq]], [[rotem-2015-drop-chip]].
- Methylation-based tethered recording that needs amplification-free long reads: [[altemose-2022-dimelo-seq]]; single-cell DamID: [[de-luca-2021-scdamid-protocol]], [[rooijers-2019-scdamt-seq]].
- Single-cell WGA chemistry reused for library construction: [[xing-2021-meta-cs]].
- Founding tethered-nuclease assay: [[skene-2017-cut-and-run]] (pA-MNase; the pA-fusion tethering idea DeChIC-seq reuses with a deaminase).
- Open-chromatin bias is the explicit concern of [[hu-2026-patty]] for CUT&Tag; DeChIC-seq claims to avoid it by design.

## Open questions

- Throughput: one cell per tube; the authors propose barcoding/multiplexing but have not shown it.
- TF peaks agree less with ChIP/CUT&RUN references — is the deamination footprint (flanking enrichment with a protected motif centre) systematically shifting peak calls?
- Repressive marks give diffuse signal; whether heterochromatin compaction limits DddA access or antibody access is untested.
- Whether "primed" Morula Rare peaks are causal footholds for lineage TFs or just early stochastic marks is inferred from motif enrichment only.

## Related

- [[chi-2026-dd-seq]] · [[swanson-2025-daf-seq]] · [[40-Topics/histone-modifications]] · [[meta-cs]]
