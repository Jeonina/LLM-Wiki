---
type: topic
title: Single-cell lineage tracing
aliases: [lineage tracing, clonal tracing, cell phylogeny, fate mapping]
tags: [lineage-tracing, clonal-analysis, phylogenetics, development, cancer-evolution]
created: 2026-06-02
updated: 2026-10-12
paper_section: ["5.4"]
---

# Single-cell lineage tracing

> Methods and algorithms that reconstruct the ancestry of individual cells — which cell came from which — to study development, ageing, regeneration and cancer evolution at clonal and phylogenetic resolution. The field divides into engineered barcodes and naturally accumulated somatic variants, and into static and evolvable labels ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]; [[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).

> [!abstract] 한눈에
> 세포 계통 추적은 인위적으로 심은 barcode를 쓰는 전향적 방식과 자연히 쌓인 체세포 변이를 쓰는 후향적 방식으로 나뉘며, 계통수 정보량과 세포 상태 측정은 서로 맞바꾸는 관계에 있다 ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]). CRISPR recorder는 정보량이 많지만 사람에게는 쓸 수 없고, 사람 조직에서는 mtDNA나 메틸화 epimutation 같은 내재 marker에 기대야 한다 ([[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]; [[10-Summaries/chen-2025-methyltree|MethylTree]]).

## Key points

- **Two axes organise the field.** Prospective (engineered synthetic barcodes) vs retrospective (naturally accumulated somatic variants), and static (one immutable label per clone) vs evolvable (labels that keep mutating to build phylogenies) ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).
- **Phylogenetic signal trades against cell-state phenotyping.** Nuclear-SNV scWGS gives the best trees but poor phenotyping, while mtDNA and epimutation profiling trade phylogenetic depth for higher throughput and richer molecular state ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).
- **Homoplasy is the fundamental limit of any recorder.** Cassiopeia identifies it as such while tuning maximum parsimony to the Cas9 mutational process ([[10-Summaries/jones-2020-cassiopeia|Cassiopeia]]).
- **Engineered recorders cannot be used in humans.** Heteroplasmic mtDNA variants are the only lineage substrate usable in intact humans ([[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]), so recorder advances in timing, phylodynamics and uncertainty do not carry over to human somatic mosaicism (synthesis).
- **Topology alone cannot date events.** Non-probabilistic methods are robust and scalable but produce topology only; LAML's time-resolved trees show three metastasis epochs with a burst at ~month 2 ([[10-Summaries/chu-2025-laml|LAML]]).

## Start here

> [!cards]
> - `concept` [[30-Concepts/lineage-tracing|Lineage tracing]] — Umbrella concept, including retrospective tracing from nuclear SNVs and CNVs.
> - `concept` [[30-Concepts/crispr-lineage-recording|CRISPR lineage recording]] — Prospective evolvable barcodes (Cas9, base and prime editing) and the full model progression.
> - `concept` [[30-Concepts/phylogenetic-inference|Phylogenetic inference]] — Algorithms that turn markers into cell-division trees.
> - `concept` [[30-Concepts/mitochondrial-lineage-tracing|Mitochondrial lineage tracing]] — Clonal tracing from somatic mtDNA variants.
> - `concept` [[30-Concepts/methylation-clones-epimutation|Methylation clones and epimutation]] — Clonally heritable DNA-methylation epimutations as endogenous markers.

## Two review frameworks

The two Nature Reviews Genetics 2026 reviews form a pair ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]; [[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]):

- **Technology toolbox.** Rodriguez-Fraticelli & Parreno cover synthetic and natural barcodes ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]).
- **Computational toolbox.** Wang, He & Hu cover phylogenetics, fate mapping, ancestral states and integrative learning ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).

## Engineered recorders and their reconstruction

Engineered recorders give high-information barcodes and a controlled recording window but cannot be used in humans; endogenous markers work in human tissue but at far lower mutation rates with no controlled window (synthesis). See [[30-Concepts/crispr-lineage-recording]] for the full model progression.

| Tool | Year | Input | Model | Note |
|---|---|---|---|---|
| [[10-Summaries/jones-2020-cassiopeia\|Cassiopeia]] | 2020 | CRISPR-Cas9 recorder edits | Maximum parsimony | Irreversibility and an unedited founder reduce the multi-state problem to binary; simulation engine; 34,557 continuously traced cells as a benchmark ([[10-Summaries/jones-2020-cassiopeia\|Cassiopeia]]) |
| [[10-Summaries/gong-2022-dclear\|DCLEAR]] | 2022 | CRISPR recorder edits | Distance-based | DREAM Challenge winner at 1,000 and 10,000 cells ([[10-Summaries/gong-2022-dclear\|DCLEAR]]) |
| [[10-Summaries/sashittal-2023-startle\|Startle]] | 2023 | CRISPR-Cas9 recorder edits | Parsimony, star homoplasy | ([[10-Summaries/sashittal-2023-startle\|Startle]]) |
| [[10-Summaries/chu-2025-laml\|LAML]] | 2025 | CRISPR recorder edits | Maximum likelihood (PMM), time-resolved | Separates heritable missingness from dropout; three metastasis epochs with a burst at ~month 2 ([[10-Summaries/chu-2025-laml\|LAML]]) |
| [[10-Summaries/seidel-2022-tidetree\|TiDeTree]] | 2022 | Lineage-recorder edits | Bayesian phylodynamics (BEAST 2) | ([[10-Summaries/seidel-2022-tidetree\|TiDeTree]]) |
| [[10-Summaries/seidel-2026-sciphy\|SciPhy]] | 2026 | Sequential prime-editing insertions | Bayesian phylodynamics | Uses the order of insertions ([[10-Summaries/seidel-2026-sciphy\|SciPhy]]) |
| [[10-Summaries/li-2023-darlin\|DARLIN]] | 2023 | Cas9-TdT lineage mouse + Camellia-seq | — | DNA methylation carries clonal memory ([[10-Summaries/li-2023-darlin\|DARLIN]]) |
| [[10-Summaries/weinreb-2020-larry\|LARRY]] | 2020 | Expressed lentiviral barcodes | — | State–fate maps; hidden heritable fate bias; trajectory-method benchmark ([[10-Summaries/weinreb-2020-larry\|LARRY]]) |

## Endogenous mtDNA markers

| Tool or study | Year | Input | Note |
|---|---|---|---|
| [[10-Summaries/ludwig-2019-mtdna-lineage-tracing\|Ludwig 2019]] | 2019 | scATAC and scRNA-seq | Heteroplasmic variants already captured by both assays; the only lineage substrate usable in intact humans; a better clonality measure than transcriptome-inferred CNVs ([[10-Summaries/ludwig-2019-mtdna-lineage-tracing\|Ludwig 2019]]) |
| [[10-Summaries/ludwig-2020-mtscatac-seq\|mtscATAC-seq]] | 2021 | scATAC | mtDNA genotyping plus chromatin profiling ([[10-Summaries/ludwig-2020-mtscatac-seq\|Lareau 2021]]) |
| [[10-Summaries/miller-2022-maester\|MAESTER]] | 2022 | scRNA-seq | mtDNA variant enrichment from scRNA-seq ([[10-Summaries/miller-2022-maester\|MAESTER]]) |
| [[10-Summaries/kwok-2022-mquad\|MQuad]] | 2022 | mtDNA variant calls | Selects clonally informative variants — the step that makes mtDNA tracing practical ([[10-Summaries/kwok-2022-mquad\|MQuad]]) |
| [[10-Summaries/sun-2025-scmitomut\|scMitoMut]] | 2025 | scDNA, scATAC or multiome reads | Beta-binomial per-cell mtDNA lineage-mutation calling ([[10-Summaries/sun-2025-scmitomut\|scMitoMut]]) |

## Methylation and epimutation tracing

- **MethylTree** reconstructs clones from whole-genome methylation ([[10-Summaries/chen-2025-methyltree|MethylTree]]).
- **EPI-Clone** uses somatic epimutations to trace blood ageing ([[10-Summaries/scherer-2025-nature|Scherer 2025]]).
- **Clonal memory in methylation.** In the DARLIN mouse, DNA methylation carries clonal memory ([[10-Summaries/li-2023-darlin|DARLIN]]).
- **The epimutation clock** is quantified in plants by AlphaBeta ([[10-Summaries/shahryary-2020-alphabeta|AlphaBeta]]) and applied at clinical scale in human cancer by EVOFLUx ([[10-Summaries/gabbutt-2025-evoflux|EVOFLUx]]).

## Nuclear somatic-variant phylogenies

Human-tissue phylogenies:

- **Blood.** HSC population dynamics from scWGS phylogenies ([[10-Summaries/lee-six-2018-hsc-dynamics|Lee-Six 2018]]).
- **Development.** Extensive human developmental phylogenies from somatic mutations ([[10-Summaries/coorens-2021-nature|Coorens 2021]]).

Tree-building tools for single-cell DNA:

| Tool | Year | Input | Model | Note |
|---|---|---|---|---|
| [[10-Summaries/wang-2021-medalt\|MEDALT]] | 2021 | CNA | Minimal event distance | A CNA-appropriate metric that explicitly rejects the infinite-sites assumption ([[10-Summaries/wang-2021-medalt\|MEDALT]]) |
| [[10-Summaries/kozlov-2022-cellphy\|CellPhy]] | 2022 | SNV genotype likelihoods | Finite-site ML with bootstrap support | Reanalysis supports monoclonal seeding of a CRC liver metastasis ([[10-Summaries/kozlov-2022-cellphy\|CellPhy]]) |
| [[10-Summaries/kang-2022-sieve\|SIEVE]] | 2022 | SNV read counts | Statistical phylogenetics (BEAST 2, finite sites) | Acquisition-bias-corrected branch lengths ([[10-Summaries/kang-2022-sieve\|SIEVE]]) |
| [[10-Summaries/zhang-2025-scistree2\|ScisTree2]] | 2025 | SNV | SPR local search | Tens of thousands of cells ([[10-Summaries/zhang-2025-scistree2\|ScisTree2]]) |

## Joint genotype and cell state

Methods that read genotype and state in the same cell enable multimodal tracing:

- **DEFND-seq** — scalable whole-genome + RNA from single nuclei ([[10-Summaries/olsen-2025-defnd-seq|DEFND-seq]]).
- **SDR-seq** — targeted DNA + RNA with clonal and variant structure ([[10-Summaries/lindenhofer-2025-sdr-seq|SDR-seq]]).
- **GoT** — genotyping of transcriptomes ([[10-Summaries/nam-2019-got|GoT]]).

## Process-level alternatives

Trajectory and graph methods describe processes rather than ancestry: PAGA ([[10-Summaries/wolf-2019-paga|PAGA]]) and Monocle 3 in MOCA ([[10-Summaries/cao-2019-moca|Cao 2019]]).

## Key people

- [[20-Entities/alejo-rodriguez-fraticelli]] — clonal hematopoiesis; lead author of the 2026 technology review.
- [[20-Entities/zheng-hu]] — single-cell cancer evolution; PhyloVelo; lead author of the 2026 computational review.
- [[20-Entities/jay-shendure]] — CRISPR and prime-editing molecular recording.
- [[20-Entities/alexander-van-oudenaarden]] — foundational synthetic and natural tracing methods.
- [[20-Entities/caleb-lareau]], [[20-Entities/leif-ludwig]] — mtDNA lineage tracing.
- [[20-Entities/tim-coorens]] — somatic-mutation phylogenetics in human tissues.

## Open questions

- Is loss of clonality a biomarker of, or a mechanism driving, organismal ageing ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]])?
- Do driver-less clonal expansions reflect positive selection or neutral drift ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]])?
- Can the temporal and heritable structure of lineage data supply the causal constraints that correlation-based "virtual cell" foundation models lack ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]])?
- The methylome reportedly beats ATAC and RNA for clonal inference against ground-truth barcodes — how general is this ([[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]])?
- Recorder-side advances in timing, phylodynamics and uncertainty are unavailable for human somatic mosaicism; how much of that gap can endogenous markers close? (synthesis)

## Related

> [!cards]
> - `hub` [[40-Topics/clonal-hematopoiesis|Clonal hematopoiesis]] — Age-related HSC clonal expansion; the central ageing and cancer payoff of lineage tracing.
> - `hub` [[40-Topics/somatic-mosaicism|Somatic mosaicism]] — Genetically distinct cell lineages within one body.
> - `hub` [[40-Topics/cancer-clonal-evolution|Cancer clonal evolution]] — Tumour phylogenies, clonal selection and the copy-number callers that feed them.

## All sources on this page

> [!info]- 30 summaries cited here
> - [[10-Summaries/cao-2019-moca|Cao 2019]]
> - [[10-Summaries/chen-2025-methyltree|Chen 2025]]
> - [[10-Summaries/chu-2025-laml|Chu 2025]]
> - [[10-Summaries/coorens-2021-nature|Coorens 2021]]
> - [[10-Summaries/gabbutt-2025-evoflux|Gabbutt 2025]]
> - [[10-Summaries/gong-2022-dclear|Gong 2022]]
> - [[10-Summaries/jones-2020-cassiopeia|Jones 2020]]
> - [[10-Summaries/kang-2022-sieve|Kang 2022]]
> - [[10-Summaries/kozlov-2022-cellphy|Kozlov 2022]]
> - [[10-Summaries/kwok-2022-mquad|Kwok 2022]]
> - [[10-Summaries/lee-six-2018-hsc-dynamics|Lee-Six 2018]]
> - [[10-Summaries/li-2023-darlin|Li 2023]]
> - [[10-Summaries/lindenhofer-2025-sdr-seq|Lindenhofer 2025]]
> - [[10-Summaries/ludwig-2019-mtdna-lineage-tracing|Ludwig 2019]]
> - [[10-Summaries/ludwig-2020-mtscatac-seq|Lareau & Ludwig 2021]]
> - [[10-Summaries/miller-2022-maester|Miller 2022]]
> - [[10-Summaries/nam-2019-got|Nam 2019]]
> - [[10-Summaries/olsen-2025-defnd-seq|Olsen 2025]]
> - [[10-Summaries/rodriguez-fraticelli-2026-lineage-tracing-review|Rodriguez-Fraticelli 2026]]
> - [[10-Summaries/sashittal-2023-startle|Sashittal 2023]]
> - [[10-Summaries/scherer-2025-nature|Scherer 2025]]
> - [[10-Summaries/seidel-2022-tidetree|Seidel & Stadler 2022]]
> - [[10-Summaries/seidel-2026-sciphy|Seidel 2026]]
> - [[10-Summaries/shahryary-2020-alphabeta|Shahryary 2020]]
> - [[10-Summaries/sun-2025-scmitomut|Sun 2025]]
> - [[10-Summaries/wang-2021-medalt|Wang 2021]]
> - [[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]
> - [[10-Summaries/weinreb-2020-larry|Weinreb 2020]]
> - [[10-Summaries/wolf-2019-paga|Wolf 2019]]
> - [[10-Summaries/zhang-2025-scistree2|Zhang 2025]]
