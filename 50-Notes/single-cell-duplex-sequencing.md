---
type: note
title: "Single-cell duplex sequencing — the methodological frontier closes"
aliases: [scDuplex, scWGA + duplex, single-cell duplex frontier]
tags: [synthesis, duplex-sequencing, scDNA-seq, single-cell-multiomics, somatic-mosaicism, methods-frontier]
created: 2026-05-19
updated: 2026-05-19
sources: [
  "[[10-Summaries/schmitt-2012-pnas]]",
  "[[10-Summaries/kennedy-2014-duplex-protocol]]",
  "[[10-Summaries/abascal-2021-nanoseq]]",
  "[[10-Summaries/bae-2023-codec]]",
  "[[10-Summaries/nandi-2025-udseq]]",
  "[[10-Summaries/zhang-2025-smaht-duplex-benchmark]]",
  "[[10-Summaries/luquette-2025-pta-duplex-mosaicism]]",
  "[[10-Summaries/andrea-2025-biorxiv]]",
  "[[10-Summaries/diane-2025-naturereviewsgenetics]]",
  "[[10-Summaries/gonzalez-pena-2021-pnas]]",
  "[[10-Summaries/gilad-2021-annualreviewofgenomicsandhumangenetics]]"
]
---

# Single-cell duplex sequencing — the methodological frontier closes

> For ~13 years (2012-2025), single-cell DNA sequencing and duplex sequencing were *incompatible* — duplex requires strand identity preserved through library prep, but scWGA chemistries (MDA, MALBAC, PTA) destroy it ([[10-Summaries/diane-2025-naturereviewsgenetics]]; [[10-Summaries/gilad-2021-annualreviewofgenomicsandhumangenetics]]). The field could measure either *which mutations are present in bulk DNA at single-molecule fidelity* ([[10-Summaries/schmitt-2012-pnas]]; [[10-Summaries/kennedy-2014-duplex-protocol]]) or *which cells carry which mutations at single-cell resolution* ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]) — but not both. **2025 closed the gap from two directions**: PTA + duplex validation makes per-cell mutation calls trustworthy ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]), and Duplex-Multiome integrates duplex consensus into the 10x Multiome library, delivering point mutations + chromatin + RNA at single-nucleus resolution across >51,000 nuclei ([[10-Summaries/andrea-2025-biorxiv]]).

## The incompatibility

**Duplex sequencing** ([[10-Summaries/schmitt-2012-pnas]]) achieves error rates ≤10⁻⁸ per base by sequencing both strands of each DNA fragment independently and requiring agreement before calling a variant ([[10-Summaries/kennedy-2014-duplex-protocol]]). This relies on tagging both Watson and Crick strands of each molecule with complementary UMIs preserved through library construction ([[10-Summaries/diane-2025-naturereviewsgenetics]]).

**scWGA chemistries** (MDA, MALBAC, PicoPLEX, PTA) amplify femtogram-scale single-cell DNA into nanogram quantities through random-priming or transposon-based mechanisms that produce daughter strands without preserved parent-strand identity ([[10-Summaries/gawad-2016-scgenome-review]]; [[10-Summaries/diane-2025-naturereviewsgenetics]]). Once the original duplex is destroyed by amplification, no downstream protocol can recover it.

The collision is fundamental: detecting a true variant at low VAF requires both strands of the *original* molecule to agree ([[10-Summaries/schmitt-2012-pnas]]); single-cell genome coverage requires amplification ([[10-Summaries/gawad-2016-scgenome-review]]). For ~13 years this meant somatic-mosaicism inference combined bulk-DNA duplex measurements (mutation rates, signatures) with single-cell genotype calls (clonality, lineage) as separate experimental modalities ([[10-Summaries/gilad-2021-annualreviewofgenomicsandhumangenetics]]).

## What duplex sequencing matured into (2012–2025)

Four implementation strategies emerged, each addressing a different limitation ([[10-Summaries/diane-2025-naturereviewsgenetics]] Fig 3a):

| Strategy | Example | Trade-off addressed |
|---|---|---|
| Y-adaptor based | NanoSeq ([[10-Summaries/abascal-2021-nanoseq]]) | Library complexity, scalable to nuclear genome |
| Tn5-based | META-CS ([[10-Summaries/diane-2025-naturereviewsgenetics]]) | Only single-cell-compatible variant; preserves strand orientation via Tn5 insertion |
| Quadruplex adaptor | CODEC ([[10-Summaries/bae-2023-codec]]) | Both strands in same read; no bottleneck dilution |
| Circularized | HiDEF-seq, SMM-seq ([[10-Summaries/diane-2025-naturereviewsgenetics]]) | PacBio/rolling-circle for ~10⁻¹⁶ error rate |

Lower-input chemistries followed: UDSeq achieves ~2.5×10⁻⁹/bp from 100 pg ([[10-Summaries/nandi-2025-udseq]]). The **SMaHT consortium duplex benchmark** ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]) cross-compared six methods (CODEC, CompDuplex-seq, HiDEF-seq, NanoSeq, ppmSeq, VISTA-seq) on shared cell-line and tissue samples — methods produced concordant mutation rates and signatures, but disagree on absolute mutation spectra at extreme low VAF ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]).

All of these remained **bulk** duplex methods. The strand-identity prerequisite made per-cell duplex resolution impractical: even META-CS, the lone single-cell-compatible variant, requires extensive plate-based preparation that doesn't scale.

## What single-cell DNA sequencing matured into (2011–2025)

scDNA-seq's parallel track addressed amplification, not strand identity. **PTA** (Primary Template-Directed Amplification, [[10-Summaries/gonzalez-pena-2021-pnas]]) achieves the most uniform single-cell coverage to date — typically ~95% genome coverage per cell with reduced allelic dropout vs MDA ([[10-Summaries/gonzalez-pena-2021-pnas]]; [[10-Summaries/diane-2025-naturereviewsgenetics]]). Combined with sensitive variant callers, PTA enables direct per-cell sSNV calling at low VAFs (synthesis based on [[10-Summaries/gonzalez-pena-2021-pnas]] + [[10-Summaries/luquette-2025-pta-duplex-mosaicism]]).

PTA is the substrate for the most ambitious recent single-cell mosaicism studies: the SMaHT consortium's flagship 102-nuclei PTA application across lung and colon of a 74-year-old donor, validated via duplex sequencing on the same individual ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]). Validation at this scale was previously infeasible.

## The 2025 inflection — closing the gap from two directions

### Path A: PTA + duplex as validation, not as same-molecule co-capture

[[10-Summaries/luquette-2025-pta-duplex-mosaicism]] does **not** unify PTA and duplex on the same molecule. Instead, it uses PTA on 102 single nuclei to produce a per-cell mutation catalog, then performs independent bulk duplex sequencing on matched DNA from the same individual to validate the mutation calls at population level ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]). This is a *trust-but-verify* architecture: per-cell calls are confirmed by per-population gold-standard fidelity. Practical compromise; doesn't solve the fundamental incompatibility but works around it.

### Path B: Duplex-Multiome — true same-molecule single-cell duplex

[[10-Summaries/andrea-2025-biorxiv|Kriz 2025 (Duplex-Multiome)]] solves the incompatibility differently: by integrating duplex consensus barcoding **into the 10x Multiome snATAC arm itself**, both strands of each DNA molecule get independently sequenced before any amplification destroys identity. Three layers emerge from a single library prep per nucleus:

1. **Somatic SNVs at duplex-grade accuracy** — >10,000-fold sequencing error reduction.
2. **Single-nucleus ATAC-seq** — chromatin accessibility per cell.
3. **Single-nucleus RNA-seq** — transcriptome per cell.

Cell-line mixing validation: at 98%/2% mixture, the assay identifies sSNVs present in 2% of cells with **92% precision** ([[10-Summaries/andrea-2025-biorxiv]]). Applied to >51,400 nuclei from postmortem human brain, the platform recovers cell-type-specific somatic mutation rates and signatures across major brain cell types ([[10-Summaries/andrea-2025-biorxiv]]).

**This is the assay that the [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap|wiki's central synthesis note]] previously claimed did not yet exist.** As of June 2025 (bioRxiv preprint), it does.

## Why the two paths matter differently

The PTA+duplex pairing and Duplex-Multiome solve overlapping but distinct problems:

| Property | PTA + duplex validation ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]) | Duplex-Multiome ([[10-Summaries/andrea-2025-biorxiv]]) |
|---|---|---|
| Per-cell duplex calls? | No — duplex on bulk only | Yes — duplex on same molecule per nucleus |
| Genome coverage per cell | ~95% (PTA) | Multiome-scale — sparser than PTA |
| Throughput | ~10²-10³ cells | ~10⁴-10⁵ nuclei |
| Multi-modal? | Genome-only | Genome + chromatin + RNA |
| Tissue applied to | Lung, colon (non-brain) | Brain |
| Cost per cell | High (deep PTA + bulk duplex) | Lower per cell at scale |

PTA + duplex is the **high-depth, low-throughput, single-modality** corner; Duplex-Multiome is the **medium-depth, high-throughput, multi-modal** corner. The two don't compete; they cover different experimental questions (synthesis based on direct comparison of the two papers).

## What this enables that wasn't possible before

- **Cell-type-specific somatic mutation rates** measured directly per cell, not inferred from cohort modeling ([[10-Summaries/andrea-2025-biorxiv]]).
- **Mutational signatures per cell type** — confirms that signature decomposition can be done at single-cell resolution, not just bulk.
- **Linking somatic SNVs to chromatin and transcriptional consequences in the same cell** — for the first time, an experiment can ask "does this somatic mutation, in this cell type, perturb local accessibility or expression?" ([[10-Summaries/andrea-2025-biorxiv]]).
- **PTA + duplex validation in non-brain tissue** — opens lung, colon, and other organ systems to scDNA-seq with confidence ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]).
- **Body-wide ancestry from a single individual** — shared embryonic mutations identifiable from 102 cells across two organs in one donor ([[10-Summaries/luquette-2025-pta-duplex-mosaicism]]).

## What remains open

- **Duplex-Multiome generalization beyond brain** — Kriz 2025 only applies it to one tissue ([[10-Summaries/andrea-2025-biorxiv]]). Will the chemistry work on FFPE, frozen blood, sorted populations?
- **Cross-method benchmarking** — the SMaHT duplex benchmark covered six bulk methods ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]); a single-cell duplex benchmark across Duplex-Multiome, PTA+duplex, and META-CS is overdue.
- **Mutation spectra at extreme low VAF** — even bulk duplex methods disagree below ~0.1% VAF ([[10-Summaries/zhang-2025-smaht-duplex-benchmark]]). Per-cell duplex sensitivity at clonal frequencies <1% needs characterization.
- **The methylation layer is still missing from single-cell duplex** — Duplex-Multiome reads accessibility + RNA + mutations. Methylation would close the [[50-Notes/regulatory-layers-overview|four-layer]] regulatory picture.
- **Cost** — Duplex-Multiome library prep is more expensive than 10x Multiome alone; production-scale economics not yet established.

## How this changes the wiki's framing

Two pages need follow-up edits:

1. **[[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]]** — already updated 2026-05-13 to acknowledge Duplex-Multiome closes the gap. This new note provides the deeper *methodological* explanation of why the gap existed and how it closed.
2. **[[50-Notes/open-questions]]** — the "single-cell + duplex" entry under Duplex Sequencing is no longer fully open; should be downgraded to "Duplex-Multiome generalization" and "cross-method single-cell duplex benchmark needed".

## Related

- [[40-Topics/duplex-sequencing]] — sub-theme index
- [[40-Topics/somatic-mosaicism]] — biological domain
- [[40-Topics/scdna-seq]] — methodology parent
- [[30-Concepts/duplex-sequencing]] · [[30-Concepts/pta]] · [[30-Concepts/meta-cs]]
- [[50-Notes/mosaicism-and-epigenome-the-synthesis-gap]] — the broader synthesis this enables
- [[50-Notes/regulatory-layers-overview]] — the four molecular regulatory layers, three of which Duplex-Multiome now co-measures
- [[50-Notes/synthesis-targets]] — this note resolves the "Single-cell duplex sequencing" target
