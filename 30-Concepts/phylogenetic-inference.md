---
type: concept
title: Single-cell phylogenetic inference
aliases: [phylogenetic reconstruction, cell phylogeny, lineage tree inference]
tags: [lineage-tracing, phylogenetics, computational, fate-mapping]
created: 2026-06-02
updated: 2026-10-12
---

# Single-cell phylogenetic inference

> The computational reconstruction of a cell-division tree from heritable markers — synthetic CRISPR edits or natural somatic variants — including the ancestral relationships and, ideally, branch lengths ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).

> [!abstract] 한눈에
> 단일세포 계통 추론은 CRISPR 편집이나 체세포 변이 같은 유전되는 표지로부터 세포 분열 tree를 복원하는 일이며, 대부분의 기준에서 NP-hard라 휴리스틱 탐색에 기대야 한다 ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]; [[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]). 방법들은 어떤 진화 모델을 가정하는지와 어떻게 탐색하는지로 나뉘고, 모델 선택은 돌연변이 과정에 대한 주장이다 ([[10-Summaries/foroughmand-2022-scelestial|Scelestial]]; [[10-Summaries/el-kebir-2018-sphyr|SPhyR]]).

## Definition

Given a character matrix (e.g. CRISPR indels) or variant calls per cell, phylogenetic inference searches for the tree topology that best explains the data under a distance-based or character-based (parsimony/likelihood) criterion ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]). The problem is NP-hard and the number of topologies grows super-exponentially with cell number, so exact search is infeasible at scale ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]). Phylogenetic inference is NP-hard under most scoring criteria, and exhaustive search is infeasible beyond roughly 20 single cells ([[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]).

## Why it matters

- Clonal grouping identifies shared ancestry; a resolved *tree* additionally exposes continuous temporal dynamics and ancestral dependencies needed for fate mapping ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).
- Errors in the inferred tree propagate into every downstream analysis (state-transition rates, ancestral states, velocity) ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).
- Non-probabilistic methods (distance, parsimony) are robust and scalable but cannot produce time-resolved branch lengths, which precludes asking *when* migration, fate or fitness changes occurred ([[10-Summaries/chu-2025-laml|LAML]]).

## Evolutionary models

The single-cell tree-inference landscape sorts on **two axes: evolutionary model × search strategy** ([[10-Summaries/foroughmand-2022-scelestial|Scelestial]] supplies the taxonomy) (synthesis). The evolutionary model is a claim about the mutational process, not a ladder of generality (synthesis).

| Model | Rule | Method | Source |
|---|---|---|---|
| Infinite sites (perfect phylogeny) | Gained once, never lost | [[10-Summaries/jahn-2016-scite\|SCITE]], [[10-Summaries/ross-2016-onconem\|OncoNEM]] | ([[10-Summaries/jahn-2016-scite\|SCITE]]; [[10-Summaries/ross-2016-onconem\|OncoNEM]]) |
| *k*-Dollo | Gained once, lost ≤ *k* times | [[10-Summaries/el-kebir-2018-sphyr\|SPhyR]] (and SASC) | ([[10-Summaries/el-kebir-2018-sphyr\|SPhyR]]) |
| Finite sites | Any state change allowed | [[10-Summaries/zafar-2017-sifit\|SiFit]] | ([[10-Summaries/zafar-2017-sifit\|SiFit]]) |
| Subperfect | Keep perfect phylogeny as target, **eliminate** up to k_max violating mutations (likelihood objective under FP/FN rates) | [[10-Summaries/malikic-2019-phiscs\|PhISCS]] | ([[10-Summaries/malikic-2019-phiscs\|PhISCS]]) |
| Star homoplasy | Mutate at most once *per lineage*, convergence allowed | [[10-Summaries/sashittal-2023-startle\|Startle]] | ([[10-Summaries/sashittal-2023-startle\|Startle]]) |
| PMM (mixed-type missing) | Non-modifiability + rate decay + heritable vs dropout missingness + heterogeneous sites | [[10-Summaries/chu-2025-laml\|LAML]] | ([[10-Summaries/chu-2025-laml\|LAML]]) |

What the model encodes depends on the marker:

- For cancer SNVs the model encodes a biological claim — loss via copy-number aberration is ubiquitous, parallel gain is rare ([[10-Summaries/el-kebir-2018-sphyr|SPhyR]]).
- For CRISPR recorders it encodes a property of the *engineering*: non-modifiability exists because an edited target no longer matches its guide RNA ([[10-Summaries/sashittal-2023-startle|Startle]]), which makes those models far better justified (synthesis).
- Encoding the recorder's irreversibility and unedited founder state into the algorithm is what reduces an NP-hard multi-state perfect-phylogeny problem to a tractable binary one ([[10-Summaries/jones-2020-cassiopeia|Cassiopeia]]).
- Under aneuploidy a locus is repeatedly altered by successive CNAs, so the **infinite-sites assumption is violated**, and Euclidean, Hamming or correlation distances misrepresent the segmental, non-linear nature of CNA evolution ([[10-Summaries/wang-2021-medalt|MEDALT]]). Minimal event distance is the appropriate metric, with homozygous loss encoded as infinite distance because deleted fragments cannot be recovered ([[10-Summaries/wang-2021-medalt|MEDALT]]).
- CNA trees differ from SNV mutation trees because overlapping, nested and recurrent CNAs break the infinite-sites assumption; SCICoNE allows arbitrary violations at the bin level, forbids regaining a segment after CN 0, and forbids duplicate genotypes ([[10-Summaries/kuipers-2025-scicone|SCICoNE]]).

MEDALT and Cassiopeia make the same structural point from different data: assay-specific physical constraints belong in the model, not around it (synthesis).

## Search strategies

- **Classic algorithms**: distance methods (neighbour-joining, UPGMA) and character methods (maximum parsimony, maximum likelihood) — foundational but strained by missing data and tens of thousands of cells ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).
- **MCMC**: [[10-Summaries/jahn-2016-scite|SCITE]], [[10-Summaries/singer-2018-sciphi|SCIΦ]], [[10-Summaries/seidel-2022-tidetree|TiDeTree]], [[10-Summaries/seidel-2026-sciphy|SciPhy]] ([[10-Summaries/jahn-2016-scite|SCITE]]; [[10-Summaries/singer-2018-sciphi|SCIΦ]]; [[10-Summaries/seidel-2022-tidetree|TiDeTree]]; [[10-Summaries/seidel-2026-sciphy|SciPhy]]).
- **Heuristic likelihood**: [[10-Summaries/ross-2016-onconem|OncoNEM]] ([[10-Summaries/ross-2016-onconem|OncoNEM]]).
- **ILP/CSP with optimality guarantees**: [[10-Summaries/el-kebir-2018-sphyr|SPhyR]], [[10-Summaries/malikic-2019-phiscs|PhISCS]] ([[10-Summaries/el-kebir-2018-sphyr|SPhyR]]; [[10-Summaries/malikic-2019-phiscs|PhISCS]]).
- **Approximation algorithm with performance bounds**: [[10-Summaries/foroughmand-2022-scelestial|Scelestial]] ([[10-Summaries/foroughmand-2022-scelestial|Scelestial]]).
- **EM + topology search**: [[10-Summaries/chu-2025-laml|LAML]] ([[10-Summaries/chu-2025-laml|LAML]]).
- **Distance-based**: [[10-Summaries/gong-2022-dclear|DCLEAR]] ([[10-Summaries/gong-2022-dclear|DCLEAR]]).

## Methods by marker

The review's overview groups methods by the heritable marker they read ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]):

- **Natural somatic variants**: SNV-based (SCIΦ, SIEVE, CellPhy, ScisTree), CNV-based (SCICoNE, MEDICC2), joint SNV+CNV (SCARLET, COMPASS), methylation-based (MethylTree) ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).
- **CRISPR-aware**: Cassiopeia (parsimony via greedy/ILP, edit irreversibility + dropout), STARTLE (star-homoplasy, each site mutates once), FRACTAL (divide-and-conquer to millions of cells); time-scaled trees via LAML, ConvexML, TiDeTree ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).
- **Expression-aided / expression-only**: LinTIMaT and LinRace integrate transcriptomes; GEMLI and CellTreeQM infer lineage from expression alone — with the caveat that transcriptional convergence is not ancestry ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).

Methods with their own summary in this wiki:

| Method | Marker | What it adds | Source |
|---|---|---|---|
| [[10-Summaries/kozlov-2022-cellphy\|CellPhy]] | Somatic SNVs | Extends the 4-state GTR model to a 16-state diploid-genotype model (GT16) with explicit allelic-dropout and amplification/sequencing-error parameters, implemented in RAxML-NG so that SNV trees get maximum-likelihood search, bootstrap branch support and ancestral-state mutation mapping | ([[10-Summaries/kozlov-2022-cellphy\|CellPhy]]) |
| [[10-Summaries/kang-2022-sieve\|SIEVE]] | Somatic SNVs | Corrects the acquisition bias of using only variant sites (which overestimates branch lengths) with the count of invariant background sites, reporting branch lengths as expected somatic mutations per site | ([[10-Summaries/kang-2022-sieve\|SIEVE]]) |
| [[10-Summaries/zhang-2025-scistree2\|ScisTree2]] | Somatic SNVs | Scales infinite-sites maximum-posterior tree search to tens of thousands of cells via an SPR local search that evaluates the full O(n²) neighbourhood in O(n²m) time plus branch-and-bound pruning; calls genotypes as a by-product of mutation placement | ([[10-Summaries/zhang-2025-scistree2\|ScisTree2]]) |
| [[10-Summaries/zafar-2019-siclonefit\|SiCloneFit]] | Somatic SNVs | Couples a tree-structured Chinese restaurant process (clones at the leaves of a clonal phylogeny) with SiFit's finite-site model, an FP/FN error model and a Beta-binomial doublet model, sampling clone number, membership, genotypes and tree jointly by MCMC | ([[10-Summaries/zafar-2019-siclonefit\|SiCloneFit]]) |
| [[10-Summaries/sollier-2023-compass\|COMPASS]] | SNVs + CNAs (gains, losses, copy-neutral LOH) from amplicon scDNA-seq | Models per-amplicon coverage weights, per-variant dropout, doublets and learned node attachment probabilities | ([[10-Summaries/sollier-2023-compass\|COMPASS]]) |
| [[10-Summaries/kuipers-2025-scicone\|SCICoNE]] | CNAs | Reuses SCITE's prune-and-reattach and label-swap MCMC moves and adds event, node and genotype-preserving moves | ([[10-Summaries/kuipers-2025-scicone\|SCICoNE]]) |
| [[10-Summaries/wang-2021-medalt\|MEDALT]] | CNAs | Minimal event distance, with homozygous loss as infinite distance | ([[10-Summaries/wang-2021-medalt\|MEDALT]]) |
| [[10-Summaries/jones-2020-cassiopeia\|Cassiopeia]] | CRISPR edits | Builds recorder irreversibility and the unedited founder state into the algorithm | ([[10-Summaries/jones-2020-cassiopeia\|Cassiopeia]]) |

## Cross-cutting lessons

- **Tree inference and error correction are the same problem.** This was reached independently in 2018 at two different levels — read counts ([[10-Summaries/singer-2018-sciphi|SCIΦ]]) and genotype matrices ([[10-Summaries/el-kebir-2018-sphyr|SPhyR]]). The tree is a prior on genotypes, so a mutation can be called in a cell with zero variant reads ([[10-Summaries/singer-2018-sciphi|SCIΦ]]) — powerful when the tree is right, and a generator of correlated false positives when it is not (synthesis).
- **Imputation belongs inside the objective**, not before it ([[10-Summaries/foroughmand-2022-scelestial|Scelestial]]; [[10-Summaries/chu-2025-laml|LAML]]).
- **Missing data can be informative.** Heritable missingness is inherited by descendants and carries phylogenetic signal; dropout does not — and the two look identical in the data ([[10-Summaries/chu-2025-laml|LAML]]).
- **Tree parsimony can check copy-number calls.** CNRein's authors read high parsimony scores as homoplasy produced by spurious, unstructured cell-specific CNAs ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]).

## Evidence and examples

- An extension of RAxML-NG with a 10-state unphased diploid genotype model outperformed a ternary model only slightly and only at very high (10–50%) error rates ([[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]); this line was later published as CellPhy ([[10-Summaries/kozlov-2022-cellphy|CellPhy]]).
- In its simulations CellPhy was the most accurate of the methods tested (TNT, infSCITE, SiFit, SCIPhI, ScisTree), especially at 5× depth when it uses genotype likelihoods, and it ran about 1–2 orders of magnitude faster than SiFit, SCIPhI or infSCITE ([[10-Summaries/kozlov-2022-cellphy|CellPhy]]).
- SIEVE outperformed CellPhy and SiFit on branch-score distance in all simulated scenarios ([[10-Summaries/kang-2022-sieve|SIEVE]]).
- Models under the finite-sites assumption performed as well as ISA models when ISA held, while SCIPhI degraded at 100 cells when ISA was violated ([[10-Summaries/kang-2022-sieve|SIEVE]]).
- In simulations ScisTree2 remained more accurate than SiFit and CellPhy even with up to 75% finite-sites sites ([[10-Summaries/zhang-2025-scistree2|ScisTree2]]).
- In two targeted CRC datasets, 104/120 and 347/630 SNV pairs violated the four-gamete test ([[10-Summaries/zafar-2019-siclonefit|SiCloneFit]]).
- COMPASS outperformed BiTSC² (which assumes uniform coverage) and SCITE (uniform attachment prior) in Tapestri-like simulations ([[10-Summaries/sollier-2023-compass|COMPASS]]).
- Using Lazac trees with the ZCNT distance, CNRein's simulated calls had a median parsimony score of 1012 against 248,891 for SIGNALS and 52,370 for CHISEL, with a ground-truth median of 736 ([[10-Summaries/ivanovic-2025-cnrein|CNRein]]).
- For copy-number data, WGD-aware MEDICC2 trees plus SNV-based doubleTime timing were used to separate truncal, parallel and subclonal WGD histories ([[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]).
- [[10-Summaries/chu-2025-laml|LAML]] uses time-resolved branch lengths to map metastasis to real time, finding three epochs and a burst at ~month 2 ([[10-Summaries/chu-2025-laml|LAML]]).

## Contested points

- Synthetic barcodes have heterogeneous mutation rates and hotspots that distort trees ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).
- Without ground truth, branch support relies on bootstrap/approximately-unbiased tests and Robinson–Foulds congruence; phylogenetic artifacts (long-branch attraction, saturation) can create clusters from technical noise ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).
- Expression-only lineage inference rests on transcriptional similarity, but transcriptional convergence is not ancestry ([[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]).
- No method recovered accurate topologies below 1× coverage or with few sites ([[10-Summaries/zhang-2025-scistree2|ScisTree2]]).
- Growing-population genealogies have short internal branches and need hundreds to tens of thousands of SNVs to resolve, a limit the authors say applies to every method ([[10-Summaries/kozlov-2022-cellphy|CellPhy]]).
- COMPASS's two-stage search keeps CNA false positives very low but misses CNAs in subclones not marked by an SNV or LOH ([[10-Summaries/sollier-2023-compass|COMPASS]]).
- Using the tree as a genotype prior lets a wrong tree produce correlated false positives (synthesis, from [[10-Summaries/singer-2018-sciphi|SCIΦ]]).

## Related

> [!cards]
> - `concept` [[30-Concepts/crispr-lineage-recording|CRISPR lineage recording]] — Synthetic recorders that accumulate heritable Cas9 edits to encode a cell-division phylogeny.
> - `concept` [[30-Concepts/lineage-tracing|Lineage tracing]] — Reconstructing cell ancestry from natural or synthetic marks.
> - `concept` [[30-Concepts/single-cell-variant-calling|Single-cell variant calling]] — Calling SNVs and indels from scDNA data dominated by amplification artifacts and dropout.
> - `concept` [[30-Concepts/monovar|Monovar]] — Single-cell SNV caller that pools base counts across cells.
> - `entity` [[20-Entities/zheng-hu|Zheng Hu]] — Lab studying single-cell cancer evolution; senior author of the multimodal lineage-tracing review.
> - `hub` [[40-Topics/single-cell-lineage-tracing|Single-cell lineage tracing]] — Reconstructing the ancestry of individual cells in development, ageing and cancer.

## All sources on this page

> [!info]- 24 summaries cited here
> - [[10-Summaries/chu-2025-laml|Chu 2025]]
> - [[10-Summaries/el-kebir-2018-sphyr|El-Kebir 2018]]
> - [[10-Summaries/foroughmand-2022-scelestial|Foroughmand-Araabi 2022]]
> - [[10-Summaries/gong-2022-dclear|Gong 2022]]
> - [[10-Summaries/ivanovic-2025-cnrein|Ivanovic & El-Kebir 2025]]
> - [[10-Summaries/jahn-2016-scite|Jahn 2016]]
> - [[10-Summaries/jones-2020-cassiopeia|Jones 2020]]
> - [[10-Summaries/kang-2022-sieve|Kang 2022]]
> - [[10-Summaries/kozlov-2022-cellphy|Kozlov 2022]]
> - [[10-Summaries/kuipers-2025-scicone|Kuipers 2025]]
> - [[10-Summaries/lahnemann-2020-grand-challenges|Lähnemann 2020]]
> - [[10-Summaries/malikic-2019-phiscs|Malikic 2019]]
> - [[10-Summaries/mcpherson-2025-ongoing-wgd|McPherson 2025]]
> - [[10-Summaries/ross-2016-onconem|Ross & Markowetz 2016]]
> - [[10-Summaries/sashittal-2023-startle|Sashittal 2023]]
> - [[10-Summaries/seidel-2022-tidetree|Seidel & Stadler 2022]]
> - [[10-Summaries/seidel-2026-sciphy|Seidel 2026]]
> - [[10-Summaries/singer-2018-sciphi|Singer 2018]]
> - [[10-Summaries/sollier-2023-compass|Sollier 2023]]
> - [[10-Summaries/wang-2021-medalt|Wang 2021]]
> - [[10-Summaries/wang-2026-multimodal-lineage-computational|Wang 2026]]
> - [[10-Summaries/zafar-2017-sifit|Zafar 2017]]
> - [[10-Summaries/zafar-2019-siclonefit|Zafar 2019]]
> - [[10-Summaries/zhang-2025-scistree2|Zhang 2025]]
