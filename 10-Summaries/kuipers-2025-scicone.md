---
type: summary
title: "Kuipers et al. 2025 — Single-cell copy number calling and event history reconstruction"
source: "[[00-Sources/papers/Single-cell copy number calling and event history reconstruction]]"
source_kind: paper
author: "Jack Kuipers, Mustafa Anıl Tuncel, Pedro F. Ferreira, Katharina Jahn, Niko Beerenwinkel"
published: 2025-02-13
ingested: 2026-10-07
doi: "10.1093/bioinformatics/btaf072"
journal: "Bioinformatics 41(3):btaf072"
tags: [SCICoNE, copy-number-calling, CNA-tree, MCMC, Dirichlet-multinomial, breakpoint-detection, shallow-WGS, 10x-CNV, DLP, whole-genome-duplication, Beerenwinkel-lab]
entities: []
concepts: ["[[copy-number-variation]]", "[[phylogenetic-inference]]", "[[chromosomal-instability]]", "[[intratumor-heterogeneity]]", "[[dlp-plus]]", "[[sequencing-depth-and-coverage]]", "[[mappability]]"]
topics: ["[[cancer-clonal-evolution]]", "[[computational-methods]]", "[[scdna-cancer-applications]]", "[[single-cell-lineage-tracing]]"]
---

**Citation:** Kuipers et al. (2025) — *Single-cell copy number calling and event history reconstruction* — *Bioinformatics* 41(3), btaf072. [DOI](https://doi.org/10.1093/bioinformatics/btaf072)

# Kuipers 2025 — SCICoNE

> Per-cell copy-number callers treat each shallow (≤0.1×) single-cell genome as independent, and CN-tree builders take those noisy calls as fixed input, so calling errors propagate into the tree. **SCICoNE** does both at once: a cross-cell dynamic-programming step finds shared breakpoints and collapses bins into segments, then an MCMC searches over **CNA trees** — trees whose nodes are amplification/deletion events on segments, SCITE-style — with cells attached to nodes and read counts modelled by a **Dirichlet-multinomial**. Because CNAs overlap and recur, the model drops the infinite-sites assumption at the bin level. The shared evolutionary history denoises the per-cell calls.

## Key claims

- **Joint inference beats call-then-tree.** Earlier CN phylogeny methods (distance-based or maximum parsimony) assume predefined CN profiles, so profile errors propagate. CONET infers breakpoint presence/absence on a tree and rounds CN in post-processing; NestedBD treats bins independently in lineage space and corrects Ginkgo calls afterwards; SCICoNE models integer CN changes at the tree nodes.
- **CNA tree, not cell lineage tree.** For clinical use, the event history — which CNAs co-occur or are mutually exclusive, and their order — matters more than the full cell genealogy. Nodes carry events on segments; a cell's CN profile is read off the root-to-node path.
- **Infinite-sites violations are allowed**: CNAs may nest, overlap and recur across lineages, resolved at bin level. Constraints: a segment at CN 0 cannot be regained in descendants, and no two nodes may produce identical genotypes (parsimony).
- **Likelihood**: Dirichlet-multinomial over GC/mappability-corrected segment counts, with concentration ν (inverse overdispersion); a minimum CN η ≪ 1 absorbs residual reads in deleted segments. All cell attachments are computed in O(mn) via tree traversal. Two scores: "sum" (marginalise attachments, needs a tree-size penalty) and "max" (best attachment); **"max" performed better** and was used on real data.
- **MCMC moves**: prune-and-reattach and label swap (from SCITE), add/remove events, add/remove node, condense/split nodes, and a genotype-preserving prune-and-reattach (relative weight 0.4). Search runs first on PhenoGraph clusters, then on full data; 10 chains with robustness checks.
- **Simulation benchmark** (20-node trees, 400 cells, 10,000 bins, 2/4/8 reads per bin, 40 or 80 segments, ν = 4, 40 trees per setting): on root-mean-squared CN error Δ, full-data SCICoNE gave the best accuracy against diploid, hierarchical clustering, PhenoGraph, SCICoNE-on-clusters, CONET, HMMcopy, Ginkgo, SCOPE and NestedBD. HMMcopy was variable and often worse than PhenoGraph clustering at 2–8 reads/bin; SCOPE improved at higher depth but varied across repetitions; NestedBD slightly improved Ginkgo. Under higher coverage without overdispersion, SCICoNE still ranked best.
- **Tree accuracy** (adapted path-difference distance τ): SCICoNE "max" best; CONET worst, near Ginkgo + MEDALT. The authors trace CONET's poor showing — at odds with CONET's own published results — to CONET's simulations implicitly giving it much higher read depth.
- **Real data**: (i) 260 cells of TNBC xenograft SA501X3F (DLP; 18,175 bins of 150 kb, 153 reads/bin/cell mean), 316 candidate breakpoints; root node has *TP53* deletion, *MAPK*-gene deletions, *PIK3CA*/*AKT1* gain; *AKT1* repeatedly amplified; *ARID1B*/*ESR1* amplified then deleted in a sub-branch; *NTRK3* and *TBX3* deleted in two parallel lineages — read as chromosomal instability and a reason to allow recurrence. (ii) 2053 cells of a 10x Genomics TNBC (20 kb bins, 100-bin window → events ≥2 Mb): a **tetraploid root** fit much better than diploid, so a **whole-genome duplication** is inferred as the initial tumour event; root-attached cells show no CNAs and are reassigned as diploid normal cells.
- **RNA is a weak proxy for CN**: in matched xenograft passage SA501X2B scRNA-seq, smoothed expression showed some agreement but signals (e.g. chromosome 19) without DNA basis, and weak RNA–DNA correlation.

## Methods / evidence

Statistical model + MCMC (C++, Python wrapper, CellRanger interface, Snakemake reproduction workflows). Evaluation by simulation designed to mimic the very shallow depth of a large clinical project (Irmisch et al. 2021) and two real breast-cancer datasets without ground truth. Runtime: tree methods are more than an order of magnitude slower than clustering or per-cell callers; SCICoNE is among the slower tree methods; SCOPE is intensive among non-tree methods.

Weight: the accuracy claims rest on simulations generated under a model close to SCICoNE's own (Dirichlet-multinomial reads, events on segments) — a home-field advantage the paper does not discuss. (synthesis) The CONET discrepancy is relegated to a supplement and is a dispute between the two groups' benchmarks. Real-data results are qualitative.

## Surprising or load-bearing bits

- **Infinite-sites is explicitly abandoned for CNAs** — the key departure from SCITE-style SNV trees, from the same lab. Parallel deletions of *NTRK3*/*TBX3* in the xenograft are the empirical justification.
- **Ploidy choice as model comparison**: comparing diploid- vs tetraploid-rooted trees by likelihood detects WGD, which per-cell normalisation obscures.
- **Small events in few cells are smoothed away** by the complexity penalty — the price of denoising via the tree; the authors suggest relaxing the penalty at higher computational cost.
- **Segmentation quality caps everything downstream**; they propose making breakpoint add/remove an MCMC move and jointly inferring GC/mappability corrections, which depend on CN state.
- Cycling (S-phase) cells should be filtered before tree inference because replication mimics CN gains.

## Concepts touched

- [[copy-number-variation]] — joint CN calling and event-history inference for shallow scWGS.
- [[phylogenetic-inference]] — CNA event trees without the infinite-sites assumption.
- [[chromosomal-instability]] — recurrent/parallel CNAs and WGD inferred from single cells.
- [[intratumor-heterogeneity]] — clonal CN architecture of TNBC samples.
- [[dlp-plus]] — shallow, amplification-free protocol whose data SCICoNE targets.

## Connections to other sources

- Same lab, SNV analogues: [[jahn-2016-scite]] (mutation trees, moves reused here), [[singer-2018-sciphi]] (phylogeny boosts noisy single-cell calls).
- Benchmarked tools with wiki summaries: [[garvin-2015-natmethods]] (Ginkgo), [[wang-2020-scope]] (SCOPE), [[wang-2021-medalt]] (MEDALT, tree from called CN).
- CN-tree alternatives cited but not benchmarked here: [[kaufmann-2022-medicc2]].
- Data sources: [[zahn-2017-dlp]], [[laks-2019-dlp-plus]], [[navin-2011-sns-tumor-evolution]].
- Reviews: [[mallory-2020-cna-review]] (HMMcopy parameter recommendations followed here), [[lu-2024-cnaphylogeny-review]], [[wang-2026-multimodal-lineage-computational]].
- Allele-specific CN and RNA-based CN inference: [[zaccaria-2021-chisel]], [[gao-2021-copykat]], [[tickle-2019-infercnv]]; chemoresistance CN evolution: [[kim-2018-tnbc-chemoresistance]].

## Open questions

- Accuracy on data simulated under other generative models (e.g. replication noise, non-DM overdispersion) is untested. (synthesis)
- Allele-specific events and joint SNV+CN phylogenies are named as extensions, not implemented.
- Whether the CONET benchmark dispute resolves under a neutral simulation.

## Related

- [[copy-number-variation]] · [[phylogenetic-inference]] · [[40-Topics/cancer-clonal-evolution]] · [[jahn-2016-scite]]
