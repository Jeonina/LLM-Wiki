---
type: note
title: "Mosaicism × epigenome at single-cell resolution — the synthesis gap"
aliases: [mosaicism-epigenome gap, the synthesis gap, dna-anchored joint-mosaicism]
tags: [synthesis, somatic-mosaicism, single-cell-multiomics, review-paper-anchor]
created: 2026-05-12
updated: 2026-05-12
sources: [
  "[[10-Summaries/hou-2016-sctrio-seq]]",
  "[[10-Summaries/izzo-2024-got-cha]]",
  "[[10-Summaries/swanson-2025-daf-seq]]",
  "[[10-Summaries/clark-2018-scnmt-seq]]",
  "[[10-Summaries/kousi-2022-ad-mosaicism]]",
  "[[10-Summaries/luquette-2025-pta-duplex-mosaicism]]"
]
---

# Mosaicism × epigenome at single-cell resolution — the synthesis gap

> **STATUS UPDATE (2026-05-13).** The gap that motivated this note has just been *methodologically closed* by a bioRxiv preprint: [[10-Summaries/kriz-2025-duplex-multiome|Kriz et al. 2025 — Duplex-Multiome]] (Walsh + Lee labs, Boston Children's). Duplex-Multiome integrates duplex consensus sequencing into the 10X Multiome platform to measure **point mutations + snATAC + snRNA in the same nucleus**, scaled to 51,400 nuclei from postmortem human brain. **All four wishlist criteria are met in one assay.** This note's framing shifts: the *technological* gap is closed; the *conceptual* gap — articulating a DNA-centric locus-state framework that interprets what such joint measurements mean — remains open and is exactly what the planned review can contribute.
>
> **Original framing (still useful as historical context).** Before Duplex-Multiome, no published single-cell assay measured somatic point mutations + chromatin/methylation state genome-wide in the same cell. The closest precedents — [[sctrio-seq]] (CNV+methylation+RNA), [[got-cha]] (targeted SNV + accessibility), [[daf-seq]] (single-fiber DNA+chromatin), [[10-Summaries/mukamel-2025-aneuploidy-brain|Mukamel 2025]] (aneuploidy+methylation atlas-scale) — each covered a slice. The neuro-mosaicism field measured mutations cell-type-specifically but used *bulk* epigenome annotations to interpret them. This note articulates why the gap mattered, who approached its edges, and how Duplex-Multiome closes it.

## Why the gap matters

Somatic mosaicism is the body's record of post-zygotic mutational history ([[somatic-mosaicism]]; [[10-Summaries/forsberg-2017-mosaicism-review]]; [[10-Summaries/ian-2015-trendsingenetics]]). The interpretive question almost always lands on **what does this mutation do to the cell's regulatory state?** — does it sit in a heterochromatin region (silent), an active enhancer (locus-specific consequence), a methylated CpG island (potentially disrupting silencing)? In practice the answer is currently inferred from *bulk* epigenome reference data (ENCODE, Roadmap, BluePrint) overlaid on single-cell genotype calls.

This is the workflow that has produced cell-type-specific somatic-mutation burden estimates in Alzheimer's brain ([[10-Summaries/kousi-2022-ad-mosaicism]]) and lung/colon ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]). It works because cell-type identity (and therefore which bulk reference to use) can usually be inferred from the same cell's transcriptome. But it cannot answer:

- **Does a mosaic point mutation perturb its own local epigenome at the single-cell level?** Bulk evidence is mixed (see scTrio-seq: large-scale CNVs do *not* change local methylation; but point-mutation effects could differ).
- **Are mosaic mutations in regulatory DNA preferentially active vs silent on the same cell's chromatin?** Single-molecule DAF-seq evidence on a 1.5% VAF mosaic CC→TT variant in COLO829 ([[10-Summaries/swanson-2025-daf-seq]]) suggests the variant *ablates* the local CTCF footprint on the same fiber it sits on — but this is one locus in one tumor mixture.
- **How does the cell's chromatin state at a future mutation site predict the mutation's likelihood of arising or being selected?** Mutational signatures (UV, smoking, replication-error) interact with chromatin (early-vs-late-replicating regions accumulate mutations differently — [[replication-timing]]). Single-cell joint measurement would test mechanism, not just correlation.

## The four anchor papers

### 1. scTrio-seq (Hou 2016) — closest CNV+epi+RNA precedent

[[10-Summaries/hou-2016-sctrio-seq]] · [[sctrio-seq]]

**Method**: mild lysis splits cytoplasm (→ scRNA-seq) from intact nucleus (→ scRRBS). RRBS read distribution doubles as the CNV signal at 10-Mb resolution after normalization.

**Key finding**: CNVs drive expression dosage (Pearson r ≈ 0.68–0.73) but do **NOT** alter DNA methylation in the affected regions (r ≈ 0.05). This is the cleanest single-cell evidence that **genomic alteration and epigenetic state are partly decoupled** at the per-cell scale — a result only visible because all three layers were jointly measured in the same cell. The decoupling implies that CNVs propagate to phenotype primarily through gene-dosage, not through indirect epigenetic remodeling.

**Coverage gaps for the synthesis claim**:
- CNV only; no point mutations.
- Tumor-only (25 HCC cells from one patient).
- Not applied to neuronal or developmental mosaicism.
- 10-Mb CNV resolution is too coarse for focal somatic variants.

### 2. GoT-ChA (Franco 2024) — targeted SNV + accessibility

[[10-Summaries/izzo-2024-got-cha]] · [[got-cha]]

**Method**: 10x scATAC-seq workflow modified to co-capture genomic DNA fragments containing a targeted mutation locus, then assigns genotypes via the cell barcode shared with the accessibility profile.

**Key finding**: in JAK2V617F-driven myeloproliferative neoplasms, mutant HSCs show **cell-intrinsic chromatin priming toward myeloid lineages before any transcriptional change is detectable**. The mutation acts at the chromatin level upstream of expression.

**Coverage gaps**:
- Targeted (one or a few loci per assay) — does not give genome-wide mutation calls.
- Designed for known mutations, not de novo mosaic discovery.
- Accessibility only; no methylation arm.

### 3. DAF-seq / scDAF-seq (Elliott 2025) — single-fiber DNA+chromatin

[[10-Summaries/swanson-2025-daf-seq]] · [[daf-seq]]

**Method**: dsDNA cytidine deaminase (SsDddA) stencils accessible cytosines as C→T sequence changes that survive amplification. Single-cell version sorts cells, performs PTA, sequences on PacBio. Each fiber yields its own sequence + chromatin state simultaneously.

**Key finding**: a 1.5% VAF mosaic CC→TT variant in COLO829 BL/T mixture **ablates the local CTCF footprint on the same single fibers that carry the variant**. This is the prototype demonstration of a mosaic mutation directly perturbing its own local chromatin state in a single cell.

**Coverage gaps**:
- ≤12 cells deeply benchmarked (4 with full analysis); throughput not yet established for cohort-scale studies.
- ~91–133 Gb of PacBio HiFi per cell — economics not yet established.
- Single cell line (GM24385 lymphoblastoid) for the scDAF-seq demonstration; primary tissue not yet tested.
- Methylation not directly measured; chromatin state only.

### 4. Mukamel 2025 — snmC-seq aneuploidy detection at 415K-cell mouse brain scale (NEW)

[[10-Summaries/mukamel-2025-aneuploidy-brain]]

**Method**: applies the scTrio-seq trick (RRBS read distribution → CNV signal) to the **snmC-seq3 / snm3C-seq BICCN mouse brain atlas (415,103 single-cell methylomes)**. Bisulfite-converted reads are uniformly distributed across the genome under bisulfite chemistry, so their density in genomic bins reports relative copy number.

**Key finding**: ~0.175–0.349% of brain cells carry whole-chromosome aneuploidy. **Trisomy of chromosome 16 (syntenic with human chr21) is 13-fold enriched** vs other autosomes (P < 10⁻³⁰⁰). Aneuploidy is **cell-type-specifically enriched** in oligodendrocyte precursor cells (OPCs), Pons neurons, pericytes, dentate gyrus granule cells, claustrum.

**Why this expands the precedent base for the synthesis claim**:
- This is the **scTrio-seq logic at 1,000× the cell number**. Where scTrio-seq used scRRBS on 25 HCC cells, Mukamel uses snmC-seq on 415K mouse brain cells.
- The methylome is measured *and* the CNV is measured *in the same cell* — so cell-type-specific aneuploidy can be assigned to cell-type-specific methylation/chromatin state. This is **mutation × epigenome × cell-type simultaneously**, at atlas scale.
- The mosaicism field can no longer be characterized as "bulk-epigenome annotated only" — methylation atlases generate single-cell paired (aneuploidy, methylome) at scale.

**Coverage gaps that remain**:
- snmC-seq reads cover ~5–15% of the genome per cell → CNV resolution limited to ≥5 Mb. **Cannot call sub-chromosomal CNVs and cannot call point mutations** because bisulfite destroys C→T sequence information.
- Aneuploidy alone is a narrow subset of mosaicism — the CNV+SNV+SV landscape is not jointly measured.
- Mouse, single age (P56–63), male only.

### 5. Duplex-Multiome (Kriz 2025) — point mutations + snATAC + snRNA per nucleus, atlas-scale (the gap-closer)

[[10-Summaries/kriz-2025-duplex-multiome]]

**Method**: integrates **duplex consensus sequencing into the 10X Multiome snATAC arm** by strand-tagging during library prep. Duplex consensus collapses sequencing error >10,000-fold, enabling accurate somatic SNV calls per nucleus. Same nucleus also yields snATAC chromatin profile + snRNA-seq transcriptome.

**Key finding**: applied to 51,400 nuclei from postmortem human brain. Cell-type-specific mutation rates and signatures distinguishable across all major brain cell types (including those previously inaccessible to scWGS — glia, rare neuron subtypes). Clonal sSNVs correlate with nearby gene-expression changes in both neurotypical and ASD brains — **first single-nucleus same-cell demonstration of mosaic mutation → expression causality** for genome-wide point mutations. 2% sensitivity at 92% precision on cell-line mixing benchmark.

**Why this closes the gap**:
- All four prior-gap criteria satisfied: (1) point mutations ✓, (2) genome-wide ✓, (3) paired chromatin (snATAC) + RNA ✓, (4) scaled beyond 10 cells (51,400) ✓.
- Methylation is the only missing layer (snATAC instead) — but the chromatin readout (accessibility) is functionally adjacent.
- Adoptable into standard 10X Multiome workflow — no custom hardware → likely to disseminate quickly.

**What remains open after Duplex-Multiome**:
- bioRxiv preprint as of 2026-05-13, not peer reviewed — replication and scale-up to be confirmed.
- Methylation arm not included (chromatin accessibility only). Adding bisulfite would re-introduce the C→T sequence-destruction problem.
- 2% VAF sensitivity is a real floor — sub-2% mosaic variants (which dominate in adult human brain) remain partially out of reach.
- Conceptual question — **what does it mean** when a mosaic SNV correlates with nearby expression in one cell? — is not answered by the method itself. This is where the planned review's locus-state framing contributes.

### 6. scNMT-seq (Clark 2018) — methylation + accessibility + RNA (no DNA mutation)

[[10-Summaries/clark-2018-scnmt-seq]] · [[scnmt-seq]]

**Method**: GpC-methyltransferase labels accessible DNA; physical DNA/RNA separation via G&T-seq logic; bisulfite + Smart-seq2. 11M usable CpGs/cell for methylation, ~15% GpC site coverage for accessibility, full-length transcriptome.

**Key finding**: methylation–accessibility coupling **strengthens** along the ESC → embryoid body pseudotime trajectory. The epigenetic layers do not act independently; their coupling is itself a dynamic property of cell state.

**Coverage gap for synthesis claim**: scNMT-seq measures the epigenome side beautifully but **does not measure DNA sequence variants** — its DNA reads are bisulfite-converted, which scrambles the very sequence information mosaicism researchers need.

## What is missing

Putting the six together, the gap is **methodologically closed for the SNV + accessibility + RNA configuration** by Duplex-Multiome, and **closed for the aneuploidy + methylation configuration** by Mukamel-style snmC-seq mining. The configurations still *not* met by any single assay:

- Point mutations + **methylation** (not accessibility) genome-wide same-cell at scale → no current assay; bisulfite chemistry inherently destroys the C→T signal that SNV calling needs.
- Point mutations + chromatin + methylation + RNA *together* in one nucleus at scale → no current assay.
- Sub-1% VAF mosaic SNVs + epigenome same-cell → below Duplex-Multiome's 2% sensitivity floor.

The remaining gaps are narrower than the original framing, and the field has demonstrated convincingly that the *conceptual* leap (treating each genomic locus as carrying a joint state across mutation, methylation, chromatin, and transcription layers) is justified by what these assays now reveal. The planned review's contribution shifts from "name an unsolved methodological frontier" to **"articulate the DNA-centric locus-state framework that interprets the joint measurements these new assays produce"**.

The closest hypothetical combinations:
- DAF-seq + bisulfite (would give DNA + accessibility + methylation per fiber) — chemistry incompatibility (deamination vs bisulfite use the same C→T signal channel).
- scNMT-seq + a low-error WGA (PTA) before the bisulfite step — would in principle give DNA + methylation + accessibility, but bisulfite-degraded DNA limits SNV sensitivity.
- 10x Multiome + targeted gDNA capture per mutation site (the GoT-ChA template) extended to a panel of mosaic loci — feasible today, throughput-permitting.
- scTrio-seq with WGA (instead of RRBS) on the nuclear fraction — would give SNV + methylation + RNA at higher cost.

## The cross-domain framing for the planned review

The review's stated novelty is "**DNA-centric, locus-as-unit, mutation + epigenome + transcriptome at single-cell**". The wiki's current source base supports articulating this as **a methodological frontier that the field is approaching from four directions but has not yet unified**:

| Direction | Anchor | What it has | What it lacks |
|---|---|---|---|
| **🟢 SNV + chromatin + RNA** (brain, genome-wide) | **Duplex-Multiome** (Kriz 2025) | **All four criteria met — closes the original gap.** 51,400 nuclei, human brain, 2% VAF sensitivity at 92% precision | No methylation arm; preprint status; sub-2% VAF still hard |
| **CNV + epi + RNA** (tumor) | scTrio-seq | All three layers in one cell | Tumor-only, 25 cells; CNV not SNV |
| **🟢 Aneuploidy + epi** (brain, atlas-scale) | Mukamel 2025 | 415K cells; CNV-from-methylation in mouse brain atlas | Aneuploidy only (≥5 Mb); not SNV |
| **Targeted SNV + chromatin** | GoT-ChA | Direct SNV → chromatin link in single cells | Few loci, no methylation |
| **Single-molecule DNA + chromatin** | DAF-seq | Direct same-fiber readout, 1.5% VAF mosaic CC→TT case | Low cell throughput, no methylation, no SNV at scale |
| **Methylation + accessibility + RNA** | scNMT-seq | Three layers in one cell | DNA sequence destroyed by bisulfite |
| **mtDNA + chromatin** | mtscATAC-seq | Same-cell mtDNA mutations + chromatin at thousands of cells | Restricted to mtDNA only |
| **Bulk-epi-annotated mosaic SNVs** | Bae 2022 ASD MEIS-motif | Genome-wide SNV + enhancer annotation | Annotation is from *reference* fetal brain epi, not the same cell |

The DNA-centric "locus state" framing in [[scdna-capabilities-framework]] anticipates this synthesis. The wiki's [[somatic-mosaicism]] page now flags the gap. This 50-Notes page is the canonical articulation, citable from review §1 (somatic mosaicism opening, framing the unsolved problem), §4.6 (joint-assay landscape, identifying the missing combination), §6 (limitations, naming what current methods cannot do), and §7 (future perspectives, what a future assay would look like).

## Open questions

- Is the right design **DNA-first** (sequence the mutation, then layer epigenome) or **epigenome-first** (read the chromatin/methylation state, then call mutations from the same DNA reads)? DAF-seq is DNA-first; scTrio-seq is methylation-first; the right choice probably depends on mutation VAF.
- For neuro-mosaicism specifically (the Walsh / Vaccarino / Gleeson program — see [[10-Summaries/bizzotto-2022-brain-mosaicism-review]]), is the right epigenetic layer DNA methylation (long-stable, cell-type-encoded) or chromatin accessibility (fast, regulatory-state-encoded)? They answer different questions.
- Does the mosaicism field need *throughput* (1000s of cells with single-locus genotype, à la GoT-ChA) or *depth* (10s of cells with genome-wide everything, à la DAF-seq)? The answer probably depends on whether the question is clonal-distribution (throughput) or mechanism-per-mutation (depth).
- The fiber-seq → DAF-seq trajectory shows how a single chemistry change (m6A erased by amplification → C→T preserved by amplification) unlocked single-cell single-molecule chromatin. **What is the analogous unlock for joint mutation + epi?** Maybe enzymatic bisulfite (EM-seq) preserving DNA integrity better than chemical bisulfite, or TAPS-style conversion combined with PTA preserving allelic dropout characteristics.

## Brain-mosaicism-specific anchors (added 2026-05-12 with neuro-batch)

The neuro-mosaicism literature provides the empirical foundation for the planned review's §1 (somatic mosaicism opening) and §5 (neuroscience applications). The bulk-epi-annotation problem is *most acute* in the brain because cell-type-specific epigenome references are needed to interpret cell-type-specific somatic mutations.

- [[10-Summaries/bae-2017-pregastrulation-mutations]] — Bae 2018: 200–400 mosaic SNVs/cell in fetal neuronal progenitors; mutation rate ~3 orders of magnitude higher than adult germline during neurogenesis; mutation spectrum shifts from CpG-deamination (early) to oxidative damage (neurogenesis); **10% mosaic SNV depletion in fetal-brain DHS sites** — direct evidence of chromatin-state-shaping-mutation-distribution within the same lineage.
- [[10-Summaries/taejeong-2022-science]] — Bae 2022: 131-brain BSMN cohort; ~6% hypermutable brains, aging-associated; **ASD brains enriched for somatic mutations creating MEIS TF binding motifs in fetal-brain enhancer-like regions** — the field's leading direct mosaic-mutation-to-enhancer causal pathway, but interpreted via *bulk* fetal-brain epigenome reference, not the same-cell measurement.
- [[10-Summaries/mukamel-2025-aneuploidy-brain]] — Mukamel 2025: snmC-seq atlas-scale (415K cells) brain aneuploidy with cell-type-specific enrichment (OPCs, Pons, chr16/chr21). The strongest current precedent for atlas-scale joint (mutation, epi) at single-cell resolution in the brain.
- [[10-Summaries/kousi-2022-ad-mosaicism]] — Kousi/Kellis 2022 AD: cell-type-specific mosaic SNV burden by FACS+WGS. Uses bulk-epigenome annotation for interpretation; methodologically the human-AD complement of Bae 2022.
- [[10-Summaries/luquette-2025-pta-duplex-mosaicism]] — Luquette/Walsh SMaHT 102-nucleus PTA + DS. Single-neuron point-mutation truth-set; no paired epi measurement.

## Related

- [[somatic-mosaicism]] — concept page; this note expands the "epigenome gap" section.
- [[sctrio-seq]], [[got-cha]], [[daf-seq]], [[scnmt-seq]] — four anchor concept pages.
- [[40-Topics/somatic-mosaicism]] — topic-level mosaicism index.
- [[40-Topics/single-cell-multiomics]] — joint-assay landscape.
- [[scdna-capabilities-framework]] — the DNA-centric "locus state" framing the review will articulate.
