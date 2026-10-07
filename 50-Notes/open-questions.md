---
type: note
title: "Open questions — tensions and gaps by domain"
aliases: [open questions, open threads, unresolved tensions]
description: Tensions and gaps surfaced during ingest or lint. Resolve, then move out.
tags: [meta, open-questions]
created: 2026-05-13
updated: 2026-10-07
---

# Open Questions

Tensions and gaps surfaced during ingest or lint. When a question is resolved, remove it here and update the relevant concept/topic page with the resolution.

## Duplex sequencing

- ~~**Single-cell + duplex**~~ — Resolved 2025: closed from two directions ([[50-Notes/single-cell-duplex-sequencing]]). Remaining sub-questions: Duplex-Multiome generalization beyond brain ([[10-Summaries/kriz-2025-duplex-multiome]]); cross-method single-cell duplex benchmark needed.
- Mutation-rate concordance across duplex platforms (SMaHT benchmark) — does it hold for brain, aging muscle, FFPE samples?
- UDSeq vs the SMaHT-benchmarked methods — no cross-comparison yet.
- **Methylation layer absent from single-cell duplex** — Duplex-Multiome reads accessibility + RNA + mutations but not methylation. Closing this would give all four regulatory layers ([[50-Notes/regulatory-layers-overview]]).

## scDNA-seq methods

- Where does scDAF-seq's per-cell ~99% coverage / ~10-cell throughput win over GoT–ChA's ~38% genotyping / 10⁵-cell throughput? See [[50-Notes/droplet-vs-single-molecule-scdna]] for the full breadth-vs-depth synthesis.
- Throughput vs depth: DLP+ (>10⁴ cells low coverage) vs PTA (384 cells, ~95% coverage). Right operating point per question? ([[50-Notes/droplet-vs-single-molecule-scdna]])
- Why is intra-cell haplotype actuation divergence (~61%) nearly equal to inter-cell divergence (~63%)?

## Mosaicism biology

- Tissue-specific mosaic mutation rates beyond skin/intestine/brain.
- **Smoking × somatic SV** burden mechanism in head-and-neck cancer.
- Causality of cell-type-specific somatic mutation burden in AD.
- IRE1-XBP1 as a therapeutic target in CALR-mutant MPN.
- mtDNA heteroplasmy drop at P6 in mouse — mechanism unclear.

## Methylation / chromatin

- 5mC vs 5hmC functional distinction — most measurements still conflate.
- **Causal vs consequential**: does methylation-loss-driven viral mimicry require additional gating factors (e.g., SETDB1, TF availability)?
- Methylation calling accuracy benchmarking across long-read platforms.
- Single-cell long-read methylation — emerging but not routine.
- Decitabine vs azacitidine: distinct demethylation patterns, mechanistic basis unknown.

## 3D genome

- TAD/loop **causality** — drive expression or follow it?
- Per-cell 3D resolution still ~1 Mb; gap to bulk Hi-C ~kb.
- Sonication-based methods (scSPRITE) capture more contacts; will they generalize?

## Wiki

- Does flat-file + `index.md` navigation scale to ~150 pages?
- Practical contradiction-resolution policy beyond flagging.
- Measuring whether the wiki is actually compounding vs accumulating.


## Added 2026-08-10 (foundational/infrastructure ingest)

**Cross-cutting artifact confounds**
- **ADO vs LOH are the same signature in single cells.** LOH detection restricts to ancestral heterozygous sites and reads allele fraction ([[10-Summaries/smukowski-heil-2023-loh]]) — exactly what WGA-induced allele dropout produces. No source in this corpus separates them. The yeast LOH rate (5 orders of magnitude above point mutation) has no human somatic equivalent measured.
- **All bisulfite-based methylomes report 5mC+5hmC.** In hippocampal neurons 5hmC is 22.04% of CpGs ([[10-Summaries/chen-2025-sctaps-sccaps-plus]]) — so brain methylome atlases built on [[10-Summaries/luo-2018-snmc-seq2|snmC-seq2]]/[[10-Summaries/nichols-2022-scimet-v2|sciMETv2]] carry an unquantified composite. Where does it change conclusions?
- **74% of Roadmap "data" is imputed** ([[10-Summaries/roadmap-2015-111-epigenomes]]). Analyses using Roadmap tracks rarely state whether a given track was observed or predicted.
- **Cell-line aneuploidy rates overstate tissue rates ~4–8×** (5.2% vs 0.6–1.2%; [[10-Summaries/laks-2019-dlp-plus]]). Somatic-aneuploidy estimates benchmarked on lines are measuring culture.

**Method assumptions nobody has tested at single-cell scale**
- **Leiden's badly-connected-community defect** was measured on web and citation graphs (14–25%) — never on sparse binary scATAC/scBS kNN graphs, where every published cell-type call depends on it ([[10-Summaries/traag-2019-leiden]]).
- **UMAP distortion on sparse binary epigenomic matrices** is unbenchmarked ([[10-Summaries/mcinnes-2018-umap]]).
- **GREAT's binomial null** assumes point-binding events over a fixed regulatory-domain rule; whether it holds for pseudo-bulked, cluster-size-dependent scATAC differential peaks is unaddressed ([[10-Summaries/mclean-2010-great]]).
- **No systematic benchmark exists** for tagmentation-based joint accessibility+transcriptome methods — stated outright in [[10-Summaries/vandereyken-2023-scmultiomics-review]].
- **No diagonal integration of an epigenomic modality has been validated against ground truth** in this corpus, though matched multimodal assays are the obvious standard ([[10-Summaries/argelaguet-2021-integration-principles]]).

**Biology left open**
- **Is TAD boundary insulation all-or-none per cell, or probabilistic across a population?** Bulk 4C cannot distinguish "every cell leaks a little" from "10% leak a lot" ([[10-Summaries/lupianez-2015-tad-disruption]]).
- **Can 3D-genome measurement distinguish cell identity in a mitotic cell?** Metaphase folding is cell-type-invariant ([[10-Summaries/naumova-2013-mitotic-chromosome]]) — a hard limit for single-cell Hi-C in proliferating tissue.
- **Is bivalency per-cell or a population average?** Sequential ChIP settled it for chromatin fibers; the marks sit on adjacent histones in one nucleosome ([[10-Summaries/rothbart-2014-histone-dna-language]]), and no single-cell method operates at nucleosome-face resolution.
- **Are enhancer LMRs dynamic turnover or maintenance failure?** [[10-Summaries/jones-2012-dna-methylation-functions|Jones 2012]] poses both; the epimutation-clock literature assumes the second without excluding the first.
- **Is the glioblastoma H3K27me3 heterogeneity clonal or plastic?** [[10-Summaries/wu-2021-sccut-tag]] has no paired genotype — the [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|synthesis gap]] restated for histone marks.
- **Do regulatory-primed loci actually get induced later?** 1,340 monocyte-specific repressive-state genes are silent in every cell type ([[10-Summaries/zhang-2022-sccut-tag-pro]]); the priming interpretation is a hypothesis.

**Methods that do not exist**
- Methylome + 3D structure + transcriptome in one cell ([[10-Summaries/vandereyken-2023-scmultiomics-review]]).
- Single-cell proteome-wide analysis alongside other omics layers.
- A bridge for modalities with no RNA-paired multiomic assay — single-cell Hi-C and most scDNA-seq have none, so bridge integration cannot reach them ([[10-Summaries/hao-2024-seurat-v5]]).

## Added 2026-10-07 (ingest of 70 sources)

**Benchmarks that disagree**
- **Imputation helps or hurts?** Non-imputing BandNorm beats Higashi/scHiCluster on bulk-concordance metrics and shows over-imputation artefacts ([[10-Summaries/zheng-2022-bandnorm-scvi-3d]]); scDIAGRAM argues imputation homogenises single-cell compartments ([[10-Summaries/peng-2026-scdiagram]]); SnapHiC/SnapHiC2 rely on RWR imputation for loops ([[10-Summaries/li-2022-snaphic2]]). The gold standards differ (bulk Hi-C vs imaging), so these are not yet commensurable. For methylation the same split: imputation framed as indispensable ([[10-Summaries/liang-2026-scmeth-imputation-benchmark]]) vs skipped entirely in high-coverage or window-aggregated analyses ([[10-Summaries/spix-2025-scdeep-mc]]; [[10-Summaries/rylaarsdam-2025-amethyst]]).
- **Embedding rankings are modality-specific.** TF-IDF/LSI wins for single-cell histone PTMs ([[10-Summaries/raimundo-2023-schptm-benchmark]]) while SnapATAC/feature aggregation beat LSI for scATAC ([[10-Summaries/luo-2024-scatac-benchmark]]). Bin size likewise: 100–200 kb optimal for scHPTM ([[10-Summaries/raimundo-2023-schptm-benchmark]]) vs 5–50 kb recommended in a scCUT&Tag review that also misdescribes that benchmark ([[10-Summaries/wu-2026-sccut-tag-review]]).
- **Wilcoxon for scATAC differential accessibility** over-calls in a replicate null ([[10-Summaries/ashuach-2022-peakvi]]) but is over-conservative in ZINB simulations ([[10-Summaries/zhao-2024-scada]]) — calibration unresolved.
- **Developer-run benchmarks only**: scCASE vs scOpen ([[10-Summaries/tang-2024-sccase]]), MambaCpG (rated volatile by an independent benchmark, [[10-Summaries/liang-2026-scmeth-imputation-benchmark]]), SCICoNE vs CONET ([[10-Summaries/kuipers-2025-scicone]]), Amethyst, CellSpace, Fast-Higashi. No independent head-to-head yet.
- **scHi-C protocol ranking is not depth-matched** ([[10-Summaries/dautle-2025-schic-review]]); scSPRITE contact counts are n-choose-2 per cluster and mostly indirect/trans per [[10-Summaries/li-2023-scnanohi-c]], so "most contacts per cell" comparisons need a contact-type qualifier.

**Biology claims revised by newer primary data**
- **Neuronal CNAs**: PTA found large CNAs in only 2/52 neurons, "in contrast to previous reports of pervasive copy number alterations" ([[10-Summaries/luquette-2022-neuron-scan2-indels]]) — MDA/DOP-era neuronal CNV claims (e.g. [[10-Summaries/mcconnell-2017-science]]) need this caveat.
- **Neuronal SNV rate converges ~15–16/year** across PTA ([[10-Summaries/luquette-2021-scan2]]) and META-CS ([[10-Summaries/xing-2021-meta-cs]]), below MDA-era estimates ([[10-Summaries/lodato-2017-aging-neurons]]). META-CS's single-strand calls read as ssDNA damage are ~13× higher than HiDEF-seq's ([[10-Summaries/liu-2024-hidef-seq]]).
- **Strand dropout on MDA**: negligible for LiRA's phased subset ([[10-Summaries/bohrson-2019-lira]]) vs ~550 SNV / 136 indel artefacts per MDA genome estimated from haploid X ([[10-Summaries/luquette-2022-neuron-scan2-indels]]).
- **CRC2 metastatic seeding**: monoclonal per CellPhy and SCARLET ([[10-Summaries/kozlov-2022-cellphy]]; [[10-Summaries/satas-2020-scarlet]]) vs polyclonal per SCITE/SiCloneFit ([[10-Summaries/zafar-2019-siclonefit]]).
- **Infinite-sites violations** are frequent in TNBC16 scWES but absent in CRC28 scWGS ([[10-Summaries/kang-2022-sieve]]) — biological or artefactual double mutants?
- **CpG-guided scA/B scores converge to CpG density** at typical scHi-C sparsity ([[10-Summaries/peng-2026-scdiagram]]) — single-cell compartment results using scA/B ([[10-Summaries/tan-2018-science]]) may partly reflect CpG density.
- **mCH typing is not neuron-only**: extends to glia ([[10-Summaries/rylaarsdam-2025-amethyst]]); and on captured targets only CG methylation separated excitatory from inhibitory neurons ([[10-Summaries/acharya-2024-scimet-cap]]).
- **CUT&Tag signal-to-noise advantage is mark-dependent** — reproduced for H3K27me3, not for H3K27ac ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark]] vs [[10-Summaries/kaya-okur-2019-cut-and-tag]]). Tn5 open-chromatin bias persists even with high salt ([[10-Summaries/hu-2026-patty]]), unlike MNase CUT&RUN ([[10-Summaries/skene-2017-cut-and-run]]) and deaminase DeChIC-seq ([[10-Summaries/shi-2026-dechic-seq]]).
- **pA-Tn5 was developed in parallel** by CoBATCH ([[10-Summaries/wang-2019-cobatch]]) and CUT&Tag ([[10-Summaries/kaya-okur-2019-cut-and-tag]]); CoBATCH's comparison with scChIC-seq uses different marks, cells and FRiP definitions.
- **H3K4me3 at enhancers**: Barski found all three H3K4 methylation states at T-cell enhancers and disputed an H3K4me1-only signature ([[10-Summaries/barski-2007-histone-methylation-chip-seq]]) vs the H3K4me1-based enhancer framing ([[10-Summaries/creyghton-2010-h3k27ac-enhancers]]).
- **Enzymatic conversion completeness**: complete in bulk EM-seq ([[10-Summaries/vaisvila-2021-em-seq]]) but incomplete CpY conversion in 43–49% of reads in a single-cell enzymatic method ([[10-Summaries/spix-2025-scdeep-mc]]). Bisulfite reads 5hmC as C and CMS may under-amplify ([[10-Summaries/huang-2010-5hmc-bisulfite]]).
- **Loop counts**: global-background callers implying >100,000 loops mostly capture same-domain pairs ([[10-Summaries/rao-2014-in-situ-hic]]); contact domains median 185 kb vs ~1 Mb TADs ([[10-Summaries/dixon-2012-tads]]) — a resolution effect.
- **SComatic cannot see cross-lineage mosaicism**: variants in >1 cell type are discarded as germline ([[10-Summaries/muyas-2024-scomatic]]), so its burdens are not comparable to scWGS mosaic call sets.
- **map3C reprocessing**: earlier snm3C-seq contact files carry many low-MAPQ interchromosomal contacts ([[10-Summaries/galasso-2026-map3c]]) — analyses built on them may need re-checking.

**Source quality to fix by re-clipping** — abstract- or reference-only clippings: [[10-Summaries/argelaguet-2018-mofa]], [[10-Summaries/pancikova-2025-splongget]], [[10-Summaries/wang-2024-wellda-seq]], [[10-Summaries/fan-2026-gfetm]]; partial: [[10-Summaries/hsieh-2015-micro-c]]. Internal inconsistencies noted in [[10-Summaries/sollier-2023-compass]] (123 vs 120 samples), [[10-Summaries/acharya-2024-scimet-cap]], [[10-Summaries/dautle-2025-schic-review]], [[10-Summaries/yadav-2025-scffpe-atac]], [[10-Summaries/zhou-2024-scdmv]], [[10-Summaries/hard-2023-long-read-scwgs]] (28 somatic SNVs = 27 nuclear + 1 mtDNA).

**Pending decision**: [[10-Summaries/luquette-2021-scan2]] (bioRxiv: 76 PTA neurons, 15 SNVs/yr) looks like the preprint of [[10-Summaries/luquette-2022-neuron-scan2-indels]] (Nature Genetics: 52 neurons analysed, 16.5 SNVs/yr) — merge or keep both?

## Related

- [[50-Notes/synthesis-targets]] — promising syntheses that would resolve clusters of these questions
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — the central conceptual gap this wiki is built around
