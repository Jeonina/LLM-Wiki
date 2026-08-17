---
type: summary
title: "Gong et al. 2022 — Single cell lineage reconstruction using distance-based algorithms and the R package, DCLEAR"
source: "[[00-Sources/papers/Single cell lineage reconstruction using distance-based algorithms and the R package, DCLEAR]]"
source_kind: paper
author: "Wuming Gong, Hyunwoo J. Kim, Daniel J. Garry, Il-Youp Kwak (corresponding)"
published: 2022-03-24
ingested: 2026-08-17
doi: "10.1186/s12859-022-04633-x"
journal: "BMC Bioinformatics 23:103"
tags: [DCLEAR, DREAM-challenge, distance-based, CRISPR-barcode, GESTALT, Hamming-distance, benchmark]
entities: []
concepts: ["[[crispr-lineage-recording]]", "[[lineage-tracing]]", "[[phylogenetic-inference]]", "[[clustering-algorithms]]"]
topics: ["[[single-cell-lineage-tracing]]", "[[computational-methods]]"]
---

**Citation:** Gong, Kim, Garry & Kwak (2022) — *Single cell lineage reconstruction using distance-based algorithms and the R package, DCLEAR* — *BMC Bioinformatics* 23, 103. [DOI](https://doi.org/10.1186/s12859-022-04633-x)

# Gong 2022 — DCLEAR

> The DREAM Challenge winner, and its lesson is deflationary: for CRISPR-barcode lineage reconstruction, **the distance metric matters more than the tree algorithm**. DCLEAR splits the problem into two steps — estimate a distance matrix, then build a tree from it — and shows that two better distance metrics substantially outperform plain **Hamming distance**, which had been the default.

## Key claims

- **The problem was unbenchmarked until 2020.** CRISPR recorder technologies ([[mckenna-2016-science|GESTALT]], scGESTALT, and successors) had produced reconstruction algorithms with no comparative evaluation, so the Allen Institute created the **Cell Lineage Reconstruction DREAM Challenge** with three sub-challenges: (1) 76 in vitro trees of <100 cells, (2) an in silico tree of 1,000 cells, (3) an in silico tree of 10,000 cells.
- **DCLEAR won sub-challenges 2 and 3** — the two *scale* sub-challenges (1,000 and 10,000 cells), not the small in vitro one. This is a scalability result as much as an accuracy result. (synthesis)
- **Two steps, and the first one carries the improvement**: distance matrix estimation, then tree reconstruction from that matrix. Two novel distance methods are proposed, and both display "a substantially improved level of performance compared to the traditional Hamming distance method."
- **Open source on CRAN under GPLv3** — the practical reason it became a standard baseline.

## Methods / evidence

DREAM Challenge submissions evaluated by the organisers against known ground-truth trees, at three scales. The competition setting is the strongest form of benchmark available in this literature: blinded, organiser-scored, common data.

Weight: the DREAM framing makes the comparison unusually credible. The clipping does not contain the specific distance-metric definitions or the numeric results.

## Surprising or load-bearing bits

- **A blinded competition is the only clean benchmark in this whole area.** Every other tool paper in the corpus benchmarks itself. The DREAM Challenge is therefore the single most trustworthy comparison point for CRISPR-barcode lineage methods, and DCLEAR's standing comes from that rather than from self-report. (synthesis)
- **Hamming distance was the default and it was leaving accuracy on the table.** For CRISPR barcodes, Hamming treats every state difference as equivalent — ignoring that some edit outcomes are far more probable than others, so sharing a *rare* edit is much stronger evidence of shared ancestry than sharing a common one. This is exactly the information the probabilistic methods ([[seidel-2026-sciphy|SciPhy]], [[chu-2025-laml|LAML]]) model mechanistically. (synthesis)
- **DCLEAR is the reference distance-based method** in subsequent benchmarks — [[chu-2025-laml|LAML]] classifies it under "non-probabilistic / distance-based" alongside its parsimony cousins [[jones-2020-cassiopeia|Cassiopeia]] and [[sashittal-2023-startle|Startle]].
- **Distance-based methods cannot produce time-resolved branch lengths**, which is precisely the gap that motivates the probabilistic generation that followed. Winning the accuracy competition and being unable to answer the timing question are compatible. (synthesis)

## Concepts touched

- [[crispr-lineage-recording]] — reconstruction from edited barcodes.
- [[phylogenetic-inference]] — the distance-matrix-then-tree decomposition.

## Connections to other sources

- Barcode technologies it reconstructs from: [[mckenna-2016-science]] (GESTALT), and see [[jones-2020-cassiopeia]] for the parsimony counterpart.
- Classified as distance-based (topology only, no branch times) by [[chu-2025-laml]].
- Parsimony alternative with a CRISPR-specific evolutionary model: [[sashittal-2023-startle]].
- Probabilistic/Bayesian alternatives that add timing: [[seidel-2022-tidetree]], [[seidel-2026-sciphy]].
- Review context: [[rodriguez-fraticelli-2026-lineage-tracing-review]], [[wang-2026-multimodal-lineage-computational]].
- The distance-based revival also appears in the somatic-mutation phylogeny world: [[foroughmand-2022-scelestial]].

## Open questions

- **The two distance metrics are not described in the ingested clipping** — the substance of the contribution needs a full-text re-ingest.
- Whether the DREAM ranking transfers to modern high-information recorders (prime-editing, sequential insertion) is untested; those systems change the distance geometry substantially.
- No branch-length or timing output, by construction.

## Related

- [[jones-2020-cassiopeia]] · [[sashittal-2023-startle]] · [[crispr-lineage-recording]] · [[40-Topics/single-cell-lineage-tracing]]
