---
type: concept
title: CRISPR lineage recording
aliases: [evolvable barcodes, CRISPR recorder, molecular recording, synthetic evolvable barcodes]
tags: [lineage-tracing, CRISPR, synthetic-barcodes, phylogenetics, prime-editing, base-editing]
created: 2026-06-02
updated: 2026-10-12
---

# CRISPR lineage recording

> A class of *prospective, evolvable* synthetic lineage-tracing systems in which Cas9 (or relatives) progressively accumulates heritable edits in a transgenic reporter, so the order of edits reconstructs a cell-division phylogeny ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).

> [!abstract] 한눈에
> CRISPR lineage recording은 Cas9 계열 효소가 transgenic reporter에 유전되는 편집을 계속 쌓게 해서, 그 편집 기록으로 세포 분열 계통수를 복원하는 합성 lineage tracing 방식이다 ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]). 기록 화학은 빠르게 발전하고 있지만, 어떤 recorder가 만든 데이터인지에 따라 맞는 재구성 모델이 다르고 재구성 방법에 따라 결과도 달라진다 ([[10-Summaries/seidel-2026-sciphy|SciPhy]]; [[10-Summaries/chu-2025-laml|LAML]]).

## Definition

Inducible Cas9 plus single-guide RNAs generate double-strand breaks in a multi-target reporter cassette; error-prone repair (typically non-homologous end joining) writes a different sequence in each cell ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]). Repeated cutting makes the barcode *evolvable*: it accumulates new mutations over time and diversifies the record ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]). Slightly mismatched guides tune the editing rate for temporal resolution ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).

CRISPR recording is distinct from *static* synthetic barcodes (one immutable label per cell) and from *retrospective* tracing with natural variants ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).

## Why it matters

- It enables detailed phylogenetic trees, up to whole-organism scale, rather than only clonal grouping ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).
- Barcode coverage decides which fate questions can be answered: down-sampling DARLIN to CARLIN-level coverage erased an early megakaryocyte-bias signal ([[10-Summaries/li-2023-darlin|DARLIN]]).

## Recorder designs

| Design | Examples | What it changes | Source |
|---|---|---|---|
| Original tandem-target Cas9 reporter | — | Inter-site deletions, reporter dropout and unedited cells limit diversity (see Contested points) | ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review\|Rodriguez-Fraticelli 2026]]) |
| Self-homing guide RNAs | hgRNAs | Self-targeting gives very high diversity; used for organism-wide trees | ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review\|Rodriguez-Fraticelli 2026]]) |
| Base editors | — | Write substitutions rather than deletions | ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review\|Rodriguez-Fraticelli 2026]]) |
| Cas12a | — | Cuts outside its guide-recognised sequence | ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review\|Rodriguez-Fraticelli 2026]]) |
| Cas9 + TdT fusion | DARLIN | Template-independent polymerase adds insertions, shifting edits from large deletions toward random insertions; used to trace the fetal-to-adult HSC transition | ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review\|Rodriguez-Fraticelli 2026]]; [[10-Summaries/li-2023-darlin\|DARLIN]]) |
| Prime-editing recorders | PE-tracer | Write known "symbols", enabling probe-based spatial readout | ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review\|Rodriguez-Fraticelli 2026]]) |
| Prime-editing sequential recorders | — | Each insertion deactivates its site and activates the next, so edit order is recorded | ([[10-Summaries/seidel-2026-sciphy\|SciPhy]]) |
| Cas9-independent deaminase fusions | TRACE (T7 polymerase), SMALT (SceI) | Fused to cytidine deaminases for continuous editing | ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review\|Rodriguez-Fraticelli 2026]]) |

## Reconstruction models

The models have followed the recorders: each recorder generation brought a new error and edit structure, and a model built for it (synthesis).

| Recorder data | Key property modelled | Method | Source |
|---|---|---|---|
| Plain Cas9 indels | Non-modifiability (an edited site never changes again) plus convergent edit outcomes, i.e. star homoplasy | Startle | ([[10-Summaries/sashittal-2023-startle\|Startle]]) |
| CRISPR recorders in general | Edit irreversibility and dropout | Cassiopeia, Startle | ([[10-Summaries/wang-2026-multimodal-lineage-computational\|Wang 2026]]) |
| Advanced recorders (KP-tracer, intMEMOIR, CARLIN) | Heritable missingness, mutation-rate decay, heterogeneous per-site edit sets (PMM) | LAML | ([[10-Summaries/chu-2025-laml\|LAML]]) |
| Prime-editing sequential recorders | Order of insertions (sequential-insertion likelihood) | SciPhy | ([[10-Summaries/seidel-2026-sciphy\|SciPhy]]) |
| Same, before SciPhy | Order only through pairwise distances, ignoring higher-order information | UPGMA with custom order-aware distances | ([[10-Summaries/seidel-2026-sciphy\|SciPhy]]) |
| Distance-based reconstruction | Edit-aware distances instead of Hamming | DCLEAR | ([[10-Summaries/gong-2022-dclear\|DCLEAR]]) |
| Bayesian phylodynamics in BEAST 2 | Trees plus birth rate, death rate and sampling proportion | TiDeTree | ([[10-Summaries/seidel-2022-tidetree\|TiDeTree]]) |

- **Choose the model by recorder.** Anyone choosing a tool must first ask which recorder generated the data (synthesis).
- **The distance metric matters.** Plain Hamming distance treats every state difference as equivalent, although a handful of indel outcomes dominate, so sharing a *rare* edit is much stronger evidence of shared ancestry than sharing a common one; better metrics substantially outperform Hamming ([[10-Summaries/gong-2022-dclear|DCLEAR]]). The probabilistic methods model the same information as variable insert propensities ([[10-Summaries/seidel-2026-sciphy|SciPhy]]) (synthesis).
- **Interpretation is the bottleneck.** Bioinformatic interpretation of sparse edits across many alleles is the main downstream bottleneck ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).

## Evidence and examples

- Fusing Cas9 to TdT shifts editing from large deletions toward random insertions: in the DARLIN mouse ~65% of alleles were singletons versus ~30% for Cas9/CARLIN, with ~5× the Shannon allele diversity ([[10-Summaries/li-2023-darlin|DARLIN]]).
- With three independent target arrays (*Col1a1*, *Tigre*, *Rosa26*), DARLIN has a theoretical ~10¹⁸ barcodes, and ~60% of single cells carry a detected, edited, rare allele versus ~10% for Cas9/CARLIN ([[10-Summaries/li-2023-darlin|DARLIN]]).
- Down-sampling DARLIN to CARLIN-level coverage erased an early megakaryocyte-bias signal ([[10-Summaries/li-2023-darlin|DARLIN]]).
- The Allen Institute's Cell Lineage Reconstruction DREAM Challenge (2020) had three sub-challenges: 76 in-vitro trees of <100 cells, 1,000 cells in silico, and 10,000 cells in silico; DCLEAR won sub-challenges 2 and 3, the two scale tiers ([[10-Summaries/gong-2022-dclear|DCLEAR]]).
- SciPhy reports significant differences from UPGMA trees on the same data, "underscoring the impact of the reconstruction method on the inferred cellular relationships and growth dynamics" ([[10-Summaries/seidel-2026-sciphy|SciPhy]]).
- In TiDeTree's validation, trees above 700 lineages were discarded because of MCMC cost ([[10-Summaries/seidel-2022-tidetree|TiDeTree]]).

## Contested points

- **Reporter limits.** Original tandem-target reporters suffer inter-site deletions that collapse effective diversity, low reporter expression that causes scRNA-seq dropout, and low editing efficiency that leaves cells unedited ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).
- **The chemistry keeps outrunning the models.** New recorders keep appearing faster than reconstruction methods built for them (synthesis).
- **Benchmarks are mostly self-run.** The DREAM Challenge is the only blinded, organiser-scored comparison in this literature ([[10-Summaries/gong-2022-dclear|DCLEAR]]); every other tool paper in the area benchmarks itself (synthesis).
- **The method changes the answer.** SciPhy and UPGMA give significantly different trees from the same data ([[10-Summaries/seidel-2026-sciphy|SciPhy]]); this is the lineage-tracing counterpart of the caller-concordance problem in [[40-Topics/mosaic-variant-calling|mosaic variant calling]] ([[10-Summaries/ha-2023-natmethods|Ha 2023]]) (synthesis).
- **Phylodynamic estimates depend on a fixed rate.** Birth–death models are non-identifiable unless one rate is fixed, so every phylodynamic estimate rests on an externally supplied number ([[10-Summaries/seidel-2022-tidetree|TiDeTree]]).
- **BEAST-based methods are costly.** LAML criticises the BEAST-based methods as built for older recorders and very computationally intensive ([[10-Summaries/chu-2025-laml|LAML]]).
- **None of it transfers to human tissue.** Engineered recorders cannot be installed in humans, so human somatic lineage tracing is restricted to endogenous markers (somatic SNVs, [[mitochondrial-lineage-tracing|mtDNA]], or [[methylation-clones-epimutation|epimutations]]), at far lower mutation rates and with no controlled recording window (synthesis).

## Related

> [!cards]
> - `concept` [[30-Concepts/lineage-tracing|Lineage tracing]] — Reconstructing cell ancestry from natural or synthetic marks.
> - `concept` [[30-Concepts/phylogenetic-inference|Phylogenetic inference]] — Reconstructing a cell-division tree from heritable markers, synthetic or natural.
> - `concept` [[30-Concepts/mitochondrial-lineage-tracing|Mitochondrial lineage tracing]] — Somatic mtDNA mutations as natural barcodes for retrospective tracing.
> - `concept` [[30-Concepts/methylation-clones-epimutation|Methylation clones and epimutations]] — Heritable CpG methylation changes as endogenous lineage markers in human cells.
> - `hub` [[40-Topics/single-cell-lineage-tracing|Single-cell lineage tracing]] — Methods and algorithms that reconstruct the ancestry of individual cells.
> - `hub` [[40-Topics/mosaic-variant-calling|Mosaic variant calling]] — Detecting low-allele-frequency somatic variants; the caller-concordance problem.

People: [[20-Entities/jay-shendure|Jay Shendure]].

## All sources on this page

> [!info]- 9 summaries cited here
> - [[10-Summaries/chu-2025-laml|Chu 2025]]
> - [[10-Summaries/gong-2022-dclear|Gong 2022]]
> - [[10-Summaries/ha-2023-natmethods|Ha 2023]]
> - [[10-Summaries/li-2023-darlin|Li 2023]]
> - [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]
> - [[10-Summaries/sashittal-2023-startle|Sashittal 2023]]
> - [[10-Summaries/seidel-2022-tidetree|Seidel & Stadler 2022]]
> - [[10-Summaries/seidel-2026-sciphy|Seidel 2026]]
> - [[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]
