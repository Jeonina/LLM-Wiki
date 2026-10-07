---
type: summary
title: "Malikic et al. 2019 — PhISCS: a combinatorial approach for subperfect tumor phylogeny reconstruction via integrative use of single-cell and bulk sequencing data"
source: "[[00-Sources/papers/PhISCS-a combinatorial approach for subperfect tumor phylogeny reconstruction via integrative use of single-cell and bulk sequencing data.pdf]]"
source_quality: full
source_sha256: "1e3c7970ec0bc0697d95f80e8ba4848ff25fd6d65aa8dd118f1c2bb18ec50994"
source_kind: paper
author: "Salem Malikic, Farid Rashidi Mehrabadi, Simone Ciccolella (joint first), Md. Khaledur Rahman, Camir Ricketts, Ehsan Haghshenas, Daniel Seidman, Faraz Hach, Iman Hajirasouliha, S. Cenk Sahinalp (co-senior; corresponding)"
published: 2019-11-01
ingested: 2026-08-17
updated: 2026-10-07
doi: "10.1101/gr.234435.118"
journal: "Genome Research 29:1860–1877"
tags: [PhISCS, subperfect-phylogeny, ISA-violation, integer-linear-programming, constraint-satisfaction, Max-SAT, bulk-integration, VAF, B-SCITE, MLTD, TPTED, three-gametes-rule]
entities: []
concepts: ["[[phylogenetic-inference]]", "[[allele-dropout]]", "[[copy-number-variation]]", "[[intratumor-heterogeneity]]", "[[doublet-detection]]"]
topics: ["[[cancer-clonal-evolution]]", "[[computational-methods]]"]
---

**Citation:** Malikic et al. (2019) — *PhISCS: a combinatorial approach for subperfect tumor phylogeny reconstruction via integrative use of single-cell and bulk sequencing data* — *Genome Research* 29, 1860–1877. [DOI](https://doi.org/10.1101/gr.234435.118)

# Malikic 2019 — PhISCS

> PhISCS turns tumour phylogeny inference from single-cell SNV calls into an exact combinatorial optimisation. The input is a ternary cell × mutation matrix (0, 1, ?). PhISCS finds the **conflict-free** matrix (one satisfying the **three-gametes rule**, i.e. a perfect phylogeny) that maximises the likelihood of the observed calls under false-positive rate α and false-negative rate β. It may also **eliminate up to k_max mutations** that cannot fit a perfect phylogeny, such as infinite-sites (ISA) violations from LOH, deletions, convergent evolution or wrong copy-number estimates. When bulk data exist, VAFs from copy-number-neutral SNVs become **hard lineage constraints**: an ancestor's cellular prevalence must be at least its descendant's, and at least the sum of two sibling lineages. The same problem is written two ways: as an ILP solved with Gurobi (**PhISCS-I**), and, for the first time in tumour phylogenetics, as a **weighted Max-SAT** Boolean CSP solved with open-source solvers (**PhISCS-B**). Both return provably optimal solutions for the objective. The authors call PhISCS the first method to combine single-cell and bulk data while allowing ISA violations.

## Key claims

- **Exact likelihood objective, not ad hoc weights.** The objective is log P(I|Y) summed over observed entries. Each 0→1 flip is weighted log(β/(1−α)) and each 1→0 flip log((1−β)/α), so false negatives, which are common, cost much less than false positives, which are rare. Missing entries are filled in at no cost. Pairwise binary variables B(p, q, a, b) enforce the three-gametes rule as linear constraints.
- **ISA violations are handled by a cap, not by pricing.** Each mutation q has an elimination variable K(q). Eliminated columns are exempt from the three-gametes constraints and drop out of the objective. Because "mutation elimination never decreases data likelihood", the number eliminated is bounded by Σ K(q) ≤ k_max. k_max is "an empirically estimated constant" or can be estimated computationally (Supplement). The abstract describes "a linear combination" that includes the number of violating mutations, but the Methods implement that term as a hard cap.
- **VAF lineage constraints apply only to SNVs outside copy-number aberrations.** Cellular prevalence is defined as vaf(M) = 2v/(v + r), which assumes a diploid locus. With a root node and a germline "null mutation" M₀ (vaf = 1), the constraints are: if p is an ancestor of q, then vaf(p)(1 + δ) ≥ vaf(q); and for a parent p with two separate descendant lineages q and r, vaf(p)(1 + δ) ≥ vaf(q) + vaf(r). Here δ is a user-set tolerance for sequencing variance. Each extra bulk sample adds its own constraints. A "general-VAF" constraint covering any number of children is quadratic and slower. The authors still recommend the triple constraint, which in practice gave the same trees.
- **Eliminating ISA violators matters most because VAFs can be wrong.** An undetected copy-number gain on the variant allele inflates the VAF, and a gain on the other allele deflates it. Either can contradict the single-cell data. Eliminating the mutation removes the contradiction. In the model, "losses of reference allele and copy number gains [of any of the two alleles]" are treated as ISA violations.
- **Max-SAT beats ILP on speed (Table 1, single core, 24 h limit, no ISA violations, no bulk data).** The tested solvers were the top performers of the 2017 Max-SAT competition (MaxHS, Z3, MAXINO) plus Gurobi for PhISCS-I. PhISCS-B "outperforms PhISCS-I with respect to running time in all cases". MAXINO was fastest, "typically terminating in a few seconds". Examples: 7 subclones at FN = 0.05, Gurobi 98 s vs. MAXINO 2.8 s; 10 subclones at FN = 0.25, 71 s vs. 3.9 s. The hard cases are **few subclones with high FN**. At 4 subclones and FN = 0.25, Gurobi solved only 2/10 instances (average 5,713 s) and MAXINO 6/10 (average 26,795 s, with the average taken over terminated instances). CPLEX/ILOG did worst and is not reported.
- **Simulations (FP = 0.0001, missing = 0.05, minimum subclone prevalence 5%, 10 replicates per setting).**
  - *vs. SiFit*, scored by normalised Robinson–Foulds distance after converting trees to cell lineage trees: 100 cells, 10 subclones, 40 mutations. PhISCS "outperforms SiFit across all of the simulation settings", with or without a single 10,000× bulk sample. Adding VAFs from even one bulk sample lowered RF distance further.
  - *vs. SCITE*, scored by MLTSM and TPTED. Under ISA with single-cell data only, the two "have comparable performance". The authors suspect most differences come from SCITE's MCMC not converging. Allowing ISA violations gave PhISCS "a slightly better performance". Adding one 10,000× bulk sample made PhISCS outperform SCITE "in all simulations".
  - *Scale-up with multiple bulk samples*: 15 subclones, 100 mutations, up to 5 ISA violations, 5,000× bulk. Accuracy improved as the number of bulk samples h went from 1 to 3 to 5. Results held in trees with one or two mutations per node.
  - *vs. B-SCITE*, with three SNVs placed in regions of clonal copy number 3 or 4 in all cancer cells: 7 subclones, 40 mutations, 5,000× bulk. PhISCS "is quite robust to copy number alterations", outperforming B-SCITE "in most of the simulation settings". In B-SCITE, bulk data only feed into the objective. In PhISCS, they are hard constraints.
  - OncoNEM "terminated with an error" on most inputs. ddClone was not compared because it does not infer trees.
- **New tree-comparison measure.** Standard tree edit distance (TED) assumes one label per node and is NP-hard to compute. The authors extend it to multilabelled tumour trees as **TPTED**, with TPTED(T, G) ≤ MLTD(T, G). They also use their group's polynomial-time **MLTD** and its dual **MLTSM** (Karpov et al. 2019). They argue that RF distance, lineage/nonlineage consistency and clustering accuracy are poorly suited to noisy single-cell trees: moving a single misplaced cell "can result in a very high RF distance".
- **Real data 1, CRC2/CO8 colorectal cancer with liver metastasis (Leung et al. 2017).** After filtering, the matrix had 86 cells × 25 loci. Most loci were non-diploid in copy-number gain regions, so **VAF constraints were not used**. The authors argue that gains barely affect presence/absence calls and may even reduce allelic dropout. With ISA elimination allowed, PhISCS eliminated **ATP7B**. The resulting tree needs a **single metastatic seeding event**, rooted at *FUS*. The tree without elimination needed two. In the ISA-strict tree, *ATP7B* and *NR4A3* have metastatic VAFs of 0.03 and 0.02, far below *FUS* (0.29), even though they sit above it. That placement implies 10 of 20 *FUS*-positive metastatic cells are false positives, a 50% FP rate, although no FP was reported for this site in any of 137 primary cells. SCITE's solution, "nearly identical", likewise called 10 of 13 *PTPRD* calls false positives. Bulk coverage at these sites was 100.92× (primary) and 110.60× (metastasis).
- **Real data 2, childhood ALL Patient 2 (Gawad et al. 2014).** The matrix had 16 mutations × 102 cells, with an estimated FN rate of 0.181749. Using VAFs and allowing elimination, PhISCS removed **RRP8, CMTM8 and RIMS2**. The first two had VAFs that contradicted their single-cell presence: *CMTM8* has a higher VAF than *RRP8* but appears in 20 fewer of 38 single cells. ISA violation in *RIMS2* had been reported before (Kuipers et al. 2017). The result is a tree with no VAF contradictions. SCITE's tree ignores VAFs. B-SCITE moves *CMTM8* up the tree and reorders the *FGD4* chain to fit VAFs. The authors argue that this kind of elimination can flag **undetected CNAs**, which is useful "especially through targeted platforms, where CNA calls could be unreliable".

## Methods / evidence

Combinatorial formulations: PhISCS-I, an ILP solved with Gurobi in which the quadratic K·Y terms are linearised; and PhISCS-B, weighted Max-SAT with hard clauses for the three-gametes rule, the k_max cap (as clauses over every (k_max + 1)-tuple of K variables) and the tree/VAF constraints, plus soft clauses whose weights equal the log-likelihood terms. VAF constraints are precomputed as Boolean functions Pvaf(p, q) and Tvaf(p, q, r). Doublets are removed beforehand with Single Cell Genotyper (Roth et al. 2016). PhISCS-B and PhISCS-I give "the same value of the objective in all cases", with small differences in Y that reflect multiple optima. Simulation follows the B-SCITE generator; details are in the Supplement. Accuracy is measured with three metrics (MLTD/MLTSM, TPTED, normalised RF). Real data: two published single-cell + bulk datasets. Code: github.com/sfu-compbio/PhISCS.

Weight: rigorous on the algorithmic side, with exact optimality, clear constraint derivations and a fair solver comparison. The empirical evidence is mostly simulation from the authors' own pipeline, scored partly with a metric family from the same group. The real-data validation is two small matrices (25 and 16 mutations) with no ground truth, judged on biological plausibility. PhISCS's clearest gains depend on bulk data. With single-cell data under ISA alone, it ties SCITE. (synthesis)

## Limitations

**Authors' own:**
- PhISCS "assumes doublets have been eliminated in a preprocessing step". The authors expect this to matter less as doublet rates fall with newer library preparation.
- VAF constraints are valid only for SNVs outside copy-number aberrations. In the CRC case most loci were in gain regions, so bulk VAFs could not be used.
- The general-VAF constraint is quadratic and slows PhISCS. The weaker triple constraint is recommended instead.
- Hard instances (few subclones with high FN) can exceed a 24 h limit with every solver tested (Table 1).

**Reviewer notes:**
- k_max effectively *is* the ISA model. Since elimination never lowers likelihood, the optimum will tend to use the full budget, so results depend on how k_max is estimated, and the main text leaves that to the Supplement. (synthesis)
- The bulk-constraint advantage applies exactly where ISA violations are least likely. Copy-number-altered regions, which drive many apparent violations, are excluded from the VAF constraints by construction. (synthesis)
- The method rests on hard constraints and a tolerance δ. If bulk VAFs are noisy beyond δ, the model can become infeasible or force eliminations. How sensitive the results are to δ is not shown in the main text. (synthesis)

## Surprising or load-bearing bits

- **"Subperfect" keeps the perfect phylogeny and edits the data.** Instead of relaxing the evolutionary model, as [[el-kebir-2018-sphyr|SPhyR]] (*k*-Dollo) or [[zafar-2017-sifit|SiFit]] (finite sites) do, PhISCS removes the few mutations that do not fit. Violations stay explicit and countable rather than absorbed into the model. (synthesis)
- **Solver choice is a real lever.** On identical instances, Max-SAT (MAXINO) ran one to two orders of magnitude faster than Gurobi in most settings. Few subclones with high FN, not more subclones, was the hard regime.
- **Copy-number gains can help single-cell genotyping.** The authors argue that extra copies of a variant allele give more template for PCR and so reduce allelic dropout. This reverses the usual view of CNAs as a problem for single-cell calling. (See [[allele-dropout]].)
- **Elimination as CNA detection.** The *ATP7B* and *RRP8/CMTM8* cases show that mutations whose VAFs contradict their single-cell frequencies point to undetected copy-number events, so a phylogeny tool doubles as a QC check on CNV calls.
- **Metastatic seeding counts depend on the ISA model.** In CRC2 the choice moved the answer between one and two seeding events, which is a biological conclusion that depends on modelling assumptions. (synthesis)

## Concepts touched

- [[phylogenetic-inference]] — conflict-free matrix / three-gametes rule; ILP and Max-SAT formulations; bounded mutation elimination; VAF lineage constraints; TPTED/MLTD tree metrics.
- [[allele-dropout]] — FN rate β drives the asymmetric flip weights; copy-number gains argued to reduce dropout.
- [[copy-number-variation]] — undetected CNAs as a cause of VAF contradictions and apparent ISA violations; CNA regions excluded from VAF constraints.
- [[intratumor-heterogeneity]] — subclonal trees from combined single-cell and bulk data; metastatic seeding inference.
- [[doublet-detection]] — assumed done upstream (Single Cell Genotyper); a stated limitation.

## Connections to other sources

- Direct comparators: [[jahn-2016-scite]] (ties PhISCS under ISA with single-cell data only) and its bulk-integrating variant B-SCITE (not in the wiki; bulk enters only the objective). [[zafar-2017-sifit]] was compared via RF distance. [[ross-2016-onconem]] could not be run.
- Alternative ISA relaxations: [[el-kebir-2018-sphyr]] (*k*-Dollo), [[zafar-2017-sifit]] (finite sites), [[satas-2020-scarlet]] (CNA-informed loss).
- Doublet-aware alternative cited in the introduction: [[zafar-2019-siclonefit]] (Gibbs sampling); PhISCS instead removes doublets upstream.
- Real-data source: [[gawad-2014-all-clonal-origins]] (ALL Patient 2). The CRC data (Leung et al. 2017) are not in the wiki.
- Benchmarked against by [[foroughmand-2022-scelestial]]. Later SNV-tree methods that compare with or extend it: [[kang-2022-sieve]], [[sollier-2023-compass]], [[zhang-2025-scistree2]].
- Bulk/single-cell hybrid designs in practice: [[gawad-2014-all-clonal-origins]], [[wang-2014-nuc-seq]].

## Open questions

- How should k_max be chosen, and how sensitive are trees to it and to δ? The main text defers both to the Supplement.
- Can VAF constraints be extended to copy-number-altered SNVs, using allele-specific copy number, so that bulk data help where ISA violations are most common? (synthesis)
- Does exact optimisation of a simplified objective beat approximate optimisation of a richer likelihood? This is the running argument between the combinatorial and MCMC camps. (synthesis)
- The 50% false-positive pattern for *FUS* in metastatic cells is resolved by elimination, but its biological cause is not determined.

## Related

- [[jahn-2016-scite]] · [[el-kebir-2018-sphyr]] · [[zafar-2017-sifit]] · [[phylogenetic-inference]] · [[40-Topics/cancer-clonal-evolution]]
